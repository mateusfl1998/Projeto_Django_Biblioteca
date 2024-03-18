from django.contrib import admin
from .models import Author, Books, RenterInformations, LoanInformations, Category
from users.models import Users

admin.site.register(Author)  
admin.site.register(RenterInformations)  
admin.site.register(LoanInformations)  
admin.site.register(Category)  
admin.site.register(Books)  