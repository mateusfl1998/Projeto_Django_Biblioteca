from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from users.models import Users
from books.models import Books,LoanInformations, Category, Author
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
    
def cadastrar_livro(request):
    if request.method == "POST":
        form = CadastroNovoLivro(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')    


    return HttpResponse(form)

def excluirlivro(request, pk):
    livro = Books.objects.get(id=pk).delete()
    return redirect (reverse_lazy('home'))
