from django.contrib import admin
from .models import Author, Books, RenterInformations, LoanInformations, Category

admin.site.register(Author)  
admin.site.register(Books)  
admin.site.register(RenterInformations)  
admin.site.register(LoanInformations)  
admin.site.register(Category)  