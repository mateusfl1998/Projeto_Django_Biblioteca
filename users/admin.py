from django.contrib import admin
from .models import Users



@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'password')
    
    def has_add_permission(self, request):
        return False    