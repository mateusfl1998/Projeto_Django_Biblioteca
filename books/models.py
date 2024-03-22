from django.db import models
from users.models import Users
from datetime import date 


class Author(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Nome do Autor")
    user = models.ForeignKey(  Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nome do Livro:'  )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name = 'Autor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name = 'Cadastrado por')

    def __str__(self):
        return self.name

class LoanInformations(models.Model):
    choices = (
        ('P','Péssimo'),
        ('R','Ruim'),
        ('B','Bom'),
        ('O','Ótimo'),
    )
    renter_name = models.CharField(max_length=30)
    loan_date = models.DateField()
    return_data = models.DateField()
    book = models.ForeignKey(Books, on_delete=models.CASCADE )
    user = models.ForeignKey(Users, on_delete=models.CASCADE) 
    avaliacao = models.CharField(max_length=1, choices=choices)
    
def __str__(self):
    return f'{self.book}'
