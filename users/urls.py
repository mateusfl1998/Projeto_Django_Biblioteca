from django.contrib.auth import admin
from django.urls import path
from .views import login_view, registry_view, registry_validation

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registry/', registry_view, name='registry'),
    path('registry_validation/', registry_validation, name='registry_validation'),
]

