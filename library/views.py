from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from users.models import Users
from books.models import Books,LoanInformations
from books.forms import CadastroNovoLivro


def home_view(request):
    if request.session.get('user'):
        user = Users.objects.get (id = request.session['user'])       
        books = Books.objects.filter(user=user.id)
        form = CadastroNovoLivro()
        list_of_books = []
        for book in books:
            loan_informations = LoanInformations.objects.filter(id=book.id)
            list_of_books.append({
            'name':book.name,
            'author': book.author,
            'category':book.category,
            'id': book.pk,
            'data_locação': loan_informations[0].loan_date,
            'data_de_devolucao':loan_informations[0].return_data
            })
            print(book)
        context = {'user':user, 'books':list_of_books, 'form':form} 
        for book in books:
            print(book)
        return render(request, 'index.html', context)
    else:
        return redirect ('/auth/login/?status=2')
    
def cadastrar_livro(request):
    if request.method == "POST":
        form = CadastroNovoLivro(request.POST)
    


    return HttpResponse(form)


