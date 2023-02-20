import os
from django.views.static import serve
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect


def getVue(request: WSGIRequest):
    filepath = "vue/static/vue/generated/index.html"
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def getVueWithCode(code: int):
    def getVueInternal(request: WSGIRequest):
        resp = getVue(request)
        resp.status_code = code
        return resp
    return getVueInternal
