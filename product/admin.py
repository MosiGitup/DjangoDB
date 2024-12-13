from django.contrib import admin
from .models import Project, Region, Product


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'project']
    list_filter = ['available', 'project']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'region', 'created', 'updated']
    list_filter = ['available', 'region', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
