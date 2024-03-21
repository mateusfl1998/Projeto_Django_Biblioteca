from django.urls import path
from .views import NewCategory,NewAuthor, BookDetailView
from library.views import NewBookCreateView

urlpatterns = [
    path('ver_livro/<int:pk>', BookDetailView.as_view(), name='detail_book'),
    path('cadastrar_livro', NewBookCreateView.as_view(), name='cadastrar_livro'),
    path('cadastrar_categoria', NewCategory.as_view(), name='cadastrar_categoria'),
    path('cadastrar_autor', NewAuthor.as_view(), name='cadastrar_author'),
]
