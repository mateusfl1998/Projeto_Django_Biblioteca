from django import forms
from .models import Books, Category, Author, Users

class CadastroNovoLivro(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
    
# class CadastroNovoLivro(forms.Form):
#     name = forms.CharField(max_length = 100)