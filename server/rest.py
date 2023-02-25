from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import get_user_model
from django.urls import path, include
from rest_framework.reverse import reverse


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "is_staff", "slug", "email"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


router = routers.SimpleRouter(trailing_slash=True)
router.register("users", UserViewSet)

rest_urlpatterns = [
    path("", RootView.as_view()),
    path("", include(router.urls), name="api-root"),
    path("users/", UserViewSet.as_view({"get": "list"}), name="api-users"),
    path("who/", CurrentUserView.as_view(), name="api-who"),
]
