from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from books.models import Books, LoanInformations, Category
from django.views.generic import DetailView

   
def view_detail(request, pk):
    book = Books.objects.get(id=pk)
    user_id = request.session.get('user')
    loaninformations = LoanInformations.objects.get(book_id=book.id)
    category = Category.objects.filter(user_id=user_id)
    # print(user_id)
    # print(book.user_id)
    if user_id == book.user_id:
        return render(request, 'details.html', {'book':book, 'loan':loaninformations, 'category':category} )
    else:
     
        return HttpResponse ('Esse livro não é seu!')
