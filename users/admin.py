from django.contrib import admin
from users.models import User
# Register your models here.

class UserShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'email')
    list_filter =  ('id', 'birth_date', 'is_active')
    search_fields= ('name', 'email', )

admin.site.register(User, UserShowAdmin)