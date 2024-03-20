from django import forms
from .models import Books, Category, Author, Users

class CadastroNovoLivro(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

    def __init__(self,*args, **kwargs, ):
        super().__init__(*args,**kwargs)
        # self.fields['user'].widget = forms.HiddenInput()
        self.fields['category'].label = "Categoria"
        
            
        