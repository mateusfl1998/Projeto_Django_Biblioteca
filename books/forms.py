from django import forms
from .models import Books, Category, Author, Users

class CadastroNovoLivro(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

    def __init__(self,user,*args, **kwargs, ):
        super().__init__(*args,**kwargs)
        # self.fields['user'].widget = forms.HiddenInput()
        self.fields['user'].initial = user   
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['category'].queryset = Category.objects.filter(user=user)
        self.fields['author'].queryset = Author.objects.filter(user=user)
            
        