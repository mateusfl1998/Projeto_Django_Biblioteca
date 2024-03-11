from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from users.models import Users
from books.models import Books,LoanInformations

def home_view(request):
    if request.session.get('user'):
        user = Users.objects.get (id = request.session['user'])
        books = Books.objects.filter(user=user.id)
        loan_informations = LoanInformations.objects.filter(book=books[0].id)
            
        context = {'user':user, 'books':books, 'loan_informations':loan_informations} 
        return render(request, 'index.html', context)
    else:
        return redirect ('/auth/login/?status=2')
    

