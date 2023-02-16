from django.http import HttpResponse
from django.shortcuts import render
from django.views.static import serve
import os


def getVue(request):
    filepath = "vue/static/vue/generated/index.html"
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
