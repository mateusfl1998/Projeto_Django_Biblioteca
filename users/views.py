from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'login.html')

def registry_view(request):
    return render (request, 'registry.html')