from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions')
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_admin',
    )
