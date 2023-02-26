from rest_framework import routers, serializers, viewsets, mixins
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import get_user_model
from django.urls import path, include, re_path
from rest_framework.reverse import reverse
from django.http import JsonResponse
from rest_framework import permissions


User = get_user_model()


class IsMeOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "slug",
            "username",
            "email",
            "is_staff",
            "is_superuser",
            "is_active",
            "groups",
            "date_joined",
            "last_login",
        ]
        read_only_fields = [
            "url",
            "email",
            "is_staff",
            "is_superuser",
            "is_active",
            "groups",
            "date_joined",
            "last_login",
        ]


class LookAndUpdateViewset(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """Allows looking (get) and updating (patch) but nothing else"""

    pass


class UserViewSet(LookAndUpdateViewset):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsMeOrReadOnly]


class CurrentUserView(APIView):
    def get(self, request: WSGIRequest, format=None):
        user = request.user
        if user.is_authenticated:
            ser = UserSerializer(user, context={"request": request})
            return Response({**ser.data, "auth": user.is_authenticated})
        return Response({"auth": user.is_authenticated})


class RootView(APIView):
    def get(self, request: WSGIRequest, format=None):
        return Response(
            {
                "users": reverse("api-users", request=request),
                "who": reverse("api-who", request=request),
            }
        )


def rest404view(request: WSGIRequest):
    return JsonResponse(
        {
            "error": "No such page",
        },
        status=404,
    )


router = routers.SimpleRouter(trailing_slash=True)
router.register("users", UserViewSet)

rest_urlpatterns = [
    path("", RootView.as_view()),
    path("", include(router.urls), name="api-root"),
    path("users/", UserViewSet.as_view({"get": "list"}), name="api-users"),
    path("who/", CurrentUserView.as_view(), name="api-who"),
    re_path(r"^.*$", rest404view),
]
