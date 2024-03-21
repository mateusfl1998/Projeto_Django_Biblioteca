from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from books.models import Books, LoanInformations, Category, Author
from django.views.generic import DetailView, CreateView
from .forms import NewCategoryForm, NewAuthorForm
from django.urls import reverse_lazy

   
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

class NewCategory(CreateView):
    model = Category
    form_class = NewCategoryForm
    template_name = 'new_category.html'
    success_url = reverse_lazy('home')

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
    
