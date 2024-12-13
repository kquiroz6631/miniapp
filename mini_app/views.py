from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Mini App</h1><p style="color:green;">Funcionando en PythonAnywhere.com</p>')