from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from books.models import Books, LoanInformations, Category, Author
from django.views.generic import DetailView, CreateView
from .forms import NewCategoryForm
from django.urls import reverse_lazy
from .models import Users

   
def view_detail(request, pk):
    book = Books.objects.get(id=pk)
    user_id = request.session.get('user')
    category = Category.objects.filter(user_id=user_id)
    # print(user_id)
    # print(book.user_id)
    if user_id == book.user_id:
        return render(request, 'details.html', {'book':book, 'category':category} )
    else:
     
        return HttpResponse ('Esse livro não é seu!')

def cadastrar_categoria(request):
    form = NewCategoryForm(request.POST)
    name = form.data['name']
    user_id = form.data['user']
    user = Users.objects.get(id=user_id)
    descricao = form.data['descricao']
    categoria = Category(name=name,description=descricao, user=user)
    categoria.save()
    print(name,descricao,user)
    return HttpResponse('sucesso')

def cadastrar_emprestimo(request):
    return HttpResponse('TESTE')

def cadastrar_autor(request):
    if request.method == "POST":
        autor = request.POST.get('autor')
        user_id = request.POST.get('user')
        user = Users.objects.get(id=user_id)
        autor_salva = Author(name=autor, user=user)
        autor_salva.save()
        print(autor,user_id)
        return HttpResponse(f'{autor}, {user_id}')

def cadastrar_emprestimo(request):
    return HttpResponse('teste')