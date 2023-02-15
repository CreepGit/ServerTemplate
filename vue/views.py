from django.http import HttpResponse
from django.shortcuts import render


def getVue(request):
    return render(request, template_name='vue/index.html')

