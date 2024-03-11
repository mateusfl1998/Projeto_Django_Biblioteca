from django.contrib import admin
from .models import Author, Books, RenterInformations, LoanInformations, Category
from users.models import Users

admin.site.register(Author)  
admin.site.register(RenterInformations)  
admin.site.register(LoanInformations)  
admin.site.register(Category)  

class LoanInformationsInline(admin.StackedInline):
    model = LoanInformations
    extra = 1

class BooksAdmin(admin.ModelAdmin):
    inlines = [LoanInformationsInline]

admin.site.register(Books, BooksAdmin)  