from django.urls import path
from .views import view_detail, NewCategory
from library.views import cadastrar_livro, excluirlivro

urlpatterns = [
    path('ver_livro/<int:pk>', view_detail, name='detail_book'),
    path('cadastrar_livro', cadastrar_livro, name='cadastrar_livro'),
    path('cadastrar_categoria', NewCategory.as_view(), name='cadastrar_categoria'),
    path('exluir/<int:pk>', excluirlivro, name='excluir_livro'),
]
