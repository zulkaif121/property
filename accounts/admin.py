from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username','address','phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'username')


