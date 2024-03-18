from django.db import models
from users.models import Users
from datetime import date 


class Author(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Nome do Autor")
    user = models.ForeignKey(  Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class RenterInformations(models.Model):
    name = models.CharField(max_length = 100)
    phone_number = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Informações de Locatário'
    
    def __str__(self):
        return f'{self.name}| {self.phone_number} '


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
    renter_information = models.ForeignKey(RenterInformations, on_delete=models.DO_NOTHING)
    loan_date = models.DateField()
    return_data = models.DateField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE )

    def __str__(self):
        return self.renter_information

    class Meta:
        verbose_name = 'Empréstimo'
    
def __str__(self):
    return f'{self.book}'
