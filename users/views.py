from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect
from hashlib import sha256
from time import sleep





def login_view(request):
    status = request.GET.get('status')

    return render(request, 'login.html', {'status':status})


def registry_view(request):
    status = request.GET.get('status')
    return render (request, 'registry.html', {'status':status})

def registry_validation_view(request):



    name = request.POST.get('name').strip()
    email = request.POST.get('email').strip()
    password = request.POST.get('password').strip()

    """se o usuario já existe no banco de dados, se existir ele vai ser 
     redirecionado para a ágina de login """
    user = User.objects.filter(email=email)
    # if len(user) < 0:   
    #     return redirect(reverse_lazy('login'))
    
    """se a senha enviada pelo usuario for menor que 8 caracteres ele vai enviar para a pagina abaixo de request """
    if len(password) < 8:
        return redirect('/auth/registry/?status=1')
    
    if len(name) < 0:
        return redirect('/auth/registry/?status=2')
    
    try: 
        password = sha256(password.encode()).hexdigest()
        user = User(name = name, email = email, password = password)
        user.save()
        return redirect ('/auth/registry/?status=0') 
        sleep(3)
        # return redirect(reverse_lazy('login'))
    except:
        return HttpResponse('Oi gente')

def login_validation_view(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    password = sha256(password.encode()).hexdigest()

    user_email = User.objects.filter(email=email).filter(password=password)

    print(user_email)
    if len(user_email) == 0:
        '''Se usuario nao existe no sistema'''
        return redirect('/auth/login/?status=1')

    if len (user_email) == 1:
        request.session['user']


