from django.contrib import admin
from properties.models import Property, PropertyImage
from django.contrib import admin

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    model=Property
    list_display=[field.name for field in model._meta.fields ]

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    model=PropertyImage
    list_display=[field.name for field in model._meta.fields ]