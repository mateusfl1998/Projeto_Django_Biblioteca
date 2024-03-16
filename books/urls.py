from django.urls import path
from .views import view_detail

urlpatterns = [
    path('ver_livro/<int:pk>', view_detail, name='detail_book')
]
