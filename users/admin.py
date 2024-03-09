from django.contrib import admin
from .models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'password')
    
    def has_add_permission(self, request):
        return False    