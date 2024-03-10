from django.db import models
from users.models import User
from datetime import date 


class Author(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Nome do Autor")
    user = models.ForeignKey(  User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class RenterInformations(models.Model):
    name = models.CharField(max_length = 100)
    phone_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class LoanInformations(models.Model):
    loan_date = models.DateField()
    return_data = models.DateField
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    user4 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nome do Livro:'  )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name = 'Autor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_cad = models.DateField(default = date.today, verbose_name = 'Data do Cadastro' )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Cadastrado por')
