from django.contrib import admin
from .models import Author, Books, RenterInformations, LoanInformations

admin.site.register(Author)  
admin.site.register(Books)  
admin.site.register(RenterInformations)  
admin.site.register(LoanInformations)  