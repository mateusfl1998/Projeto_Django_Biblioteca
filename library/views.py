from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from users.models import Users
from books.models import Books,LoanInformations, Category, Author
<<<<<<< HEAD
from books.forms import CadastroNovoLivro, NewCategoryForm
from django.urls import reverse_lazy


def home_view(request):
    if request.session.get('user'):
        user = Users.objects.get (id = request.session['user'])  
        books = Books.objects.filter(user=user.id)
        form =  CadastroNovoLivro()
        form.fields['user'].initial = user.id
        form.fields['category'].queryset = Category.objects.filter(user=user.id)
        form.fields['author'].queryset = Author.objects.filter(user=user.id)
        form_categoria = NewCategoryForm()
        
        list_of_books = []
        for book in books:
            list_of_books.append({
            'name':book.name,
            'author': book.author,
            'category':book.category,
            'id': book.pk,
            
            })

        context = {'user':user, 
                   'books':list_of_books, 
                   'form':form,
                   'form_categoria' : form_categoria,
                   
                   
                   
                   } 
        return render(request, 'index.html', context)
    else:
        return redirect ('/auth/login/?status=2')
=======
from books.forms import CadastroNovoLivro, NewCategoryForm, NewAuthorForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django import forms

class BooksListView(ListView):
    model = Books
    template_name = 'index.html'
>>>>>>> d74c26f852ab527e7bf82b4686ece52613a36a80
    
    def dispatch(self, request, *args, **kwargs):
        if 'user' not in request.session:
        # Se o usuário não estiver autenticado, redireciona para a página de login
            return redirect(reverse_lazy('login'))  # Substitua 'nome_da_view_do_login' pelo nome da sua view de login
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # Pegar User ID
        user_id = self.request.session.get('user')
        # Mostrar os Livros Cadastrados pelo User
        books = Books.objects.filter(user=user_id)
        context['books'] = books
        # Form de Cadastro de Novo Livro
        form = CadastroNovoLivro()
        form.fields['category'].queryset = Category.objects.filter(user=user_id)
        form.fields['author'].queryset = Author.objects.filter(user=user_id)
        form.fields['user'].initial = Users.objects.get(id=user_id)
        context['form'] = form  
        #Form de Cadastro de Nova Categoria
        form1 = NewCategoryForm()
        form1.fields['user'].initial = Users.objects.get(id=user_id)
        context['form1'] = form1
        #Form de Cadastro de Author Categoria
        form2 = NewAuthorForm()
        form2.fields['user'].initial = Users.objects.get(id=user_id)
        context['form2'] = form2
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = CadastroNovoLivro()
    #     return context
        
  


class NewBookCreateView(CreateView):
    model = Books
    form_class = CadastroNovoLivro
    success_url = reverse_lazy('home')
    


def excluirlivro(request, pk):
    livro = Books.objects.get(id=pk).delete()
    return redirect (reverse_lazy('home'))
