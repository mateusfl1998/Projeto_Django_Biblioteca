from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'login.html')

def registry_view(request):
    return render (request, 'registry.html')

def registry_validation(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    email = request.POST.get('email')
    return HttpResponse(f' {name} -- {password} -- {email}')