from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from users.models import User

def home_view(request):
    if request.session.get('user_email'):
        user = User.objects.get (id = request.session['user_email']).name
        return HttpResponse(f'Olá {user}')
    else:
        return redirect ('/auth/login/?status=2')