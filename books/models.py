from django.db import models
from users.models import Users
from datetime import date, datetime


class Author(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Nome do Autor")
    user = models.ForeignKey(  Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nome do Livro:'  )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name = 'Autor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='capa_livro', null=True,blank=True)
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
    loan_date = models.DateField(default=datetime.datetime.now())
    return_data = models.DateTimeField(blank=True, null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE )
    user = models.ForeignKey(Users, on_delete=models.CASCADE) 
    avaliacao = models.CharField(max_length=1, choices=choices)
    
def __str__(self):
    return f'{self.book}'
