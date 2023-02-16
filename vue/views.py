import os
from django.views.static import serve
from django.core.handlers.wsgi import WSGIRequest


def getVue(request: WSGIRequest):
    filepath = "vue/static/vue/generated/index.html"
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
