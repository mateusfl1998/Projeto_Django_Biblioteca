from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def home_view(request):
    # return render (request, 'index.html')
    return render (request, 'index.html')