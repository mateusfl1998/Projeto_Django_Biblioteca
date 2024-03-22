from django.urls import path
<<<<<<< HEAD
from .views import view_detail,cadastrar_categoria, cadastrar_emprestimo, cadastrar_autor, cadastrar_emprestimo
from library.views import cadastrar_livro, excluirlivro

urlpatterns = [
    path('ver_livro/<int:pk>', view_detail, name='detail_book'),
    path('cadastrar_livro', cadastrar_livro, name='cadastrar_livro'),
    path('cadastrar_categoria', cadastrar_categoria, name='cadastrar_categoria'),
    path('exluir/<int:pk>', excluirlivro, name='excluir_livro'),
    path('cadastrar_emprestimo ', cadastrar_emprestimo, name="cadastrar_emprestimo"),
    path('cadastrar_autor ', cadastrar_autor, name="cadastrar_autor"),  
    path('cadastrar_emprestimo ', cadastrar_emprestimo, name="cadastrar_emprestimo"),  
=======
from .views import NewCategory,NewAuthor, BookDetailView
from library.views import NewBookCreateView

urlpatterns = [
    path('ver_livro/<int:pk>', BookDetailView.as_view(), name='detail_book'),
    path('cadastrar_livro', NewBookCreateView.as_view(), name='cadastrar_livro'),
    path('cadastrar_categoria', NewCategory.as_view(), name='cadastrar_categoria'),
    path('cadastrar_autor', NewAuthor.as_view(), name='cadastrar_author'),
>>>>>>> d74c26f852ab527e7bf82b4686ece52613a36a80
]
