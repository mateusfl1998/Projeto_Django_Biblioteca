from django import forms
from .models import Books, Category, Author, Users

class CadastroNovoLivro(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

    def __init__(self,*args, **kwargs, ):
        super().__init__(*args,**kwargs)
        self.fields['category'].label = "Categoria"
        self.fields['user'].widget = forms.HiddenInput()
      

<<<<<<< HEAD
class NewCategoryForm (forms.Form):
    name = forms.CharField(max_length=30)
    descricao = forms.CharField(max_length=100)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['descricao'].widget = forms.Textarea()
        self.fields['name'].label = "Nome"
        self.fields['descricao'].label = "Descrição"
=======
class NewCategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['description'].label = 'Descrição'
        self.fields['name'].label = 'Nome da Categoria'

class NewAuthorForm (forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        widgets = {'user': forms.HiddenInput()}
>>>>>>> d74c26f852ab527e7bf82b4686ece52613a36a80
    
            
        