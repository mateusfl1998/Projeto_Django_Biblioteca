from django.db import models
from django.contrib.auth.models import User
from datetime import date 


class Author(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Nome do Autor")

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'



class Books(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nome do Livro:'  )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name = 'Autor')
    date_cad = models.DateField(default = date.today, verbose_name = 'Data do Cadastro' )
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Cadastrado por')

class RenterInformations(models.Model):
    name = models.CharField(max_length = 100)
    phone_number = models.IntegerField()

class LoanInformations(models.Model):
    loan_date = models.DateField()
    return_data = models.DateField
