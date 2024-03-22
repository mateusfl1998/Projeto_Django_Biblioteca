
from django.contrib import admin
from django.urls import path, include
from .views import BooksListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BooksListView.as_view(), name='home'),
    path('livros/', include('books.urls')),
    path('auth/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )