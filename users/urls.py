from django.contrib.auth import admin
from django.urls import path
from .views import login_view, registry_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registry/', registry_view, name='registry'),
]

