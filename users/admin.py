from django.contrib import admin
from users.models import User
# Register your models here.

class UserShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name')
    list_filter =  ('id', 'birth_date', 'is_active')

admin.site.register(User, UserShowAdmin)