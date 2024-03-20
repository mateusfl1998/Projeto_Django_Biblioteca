from django.urls import path
from .views import view_detail
from library.views import cadastrar_livro

urlpatterns = [
    path('ver_livro/<int:pk>', view_detail, name='detail_book'),
    path('cadastrar_livro', cadastrar_livro, name='cadastrar_livro'),
]
