from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from books.models import Books, LoanInformations, Category, Author
from django.views.generic import DetailView, CreateView
from .forms import NewCategoryForm, NewAuthorForm
from django.urls import reverse_lazy
from .models import Users



class BookDetailView(DetailView):
    model = Books
    template_name = 'details.html'

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

<<<<<<< HEAD
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
=======
    def dispatch(self, request, *args, **kwargs):
        # Gerar a variável para armazenar o ID do usuário
        self.user_id = request.session.get('user')
        print(self.user_id)
        return super().dispatch(request, *args, **kwargs)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.user_id  # Passa o valor de self.user_id como valor inicial para o campo 'user'
        return initial

class NewAuthor(CreateView):
    model = Author
    form_class = NewAuthorForm
    template_name = 'new_author.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.session.get('user')
        print(self.user_id)
        return super().dispatch(request, *args, **kwargs)
    
    def get_initial(self):
        initial = {'user':self.user_id}
        return initial
    
>>>>>>> d74c26f852ab527e7bf82b4686ece52613a36a80
