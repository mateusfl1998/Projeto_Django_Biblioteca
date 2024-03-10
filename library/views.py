from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from users.models import User
from books.models import Books

def home_view(request):
    if request.session.get('user'):
        user = User.objects.get (id = request.session['user'])
        books = Books.objects.filter(user=user.id)
        print(books[0])
        context = {'user':user, 'books':books} 
        return render(request, 'index.html', context)
    else:
        return redirect ('/auth/login/?status=2')
    

