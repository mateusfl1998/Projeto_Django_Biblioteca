from django.contrib.auth import admin
from django.urls import path
from .views import login_view, registry_view, registry_validation_view, login_validation_view, logout

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login_validation/', login_validation_view, name='login_validation'),
    path('registry/', registry_view, name='registry'),
    path('registry_validation/', registry_validation_view, name='registry_validation'),
    path('logout', logout, name='logout'),
]

