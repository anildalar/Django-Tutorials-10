from django.contrib import admin

from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    #1. Property
    #prepopulated_fields = { 'cat_slug':('cat_name',) }
    list_display = ('cat_name','cat_slug','cat_desc','cat_image') # Tuple
    #2. Constructor

    #3. Method


    #4. Nested Class

    pass


admin.site.register(Category, CategoryAdmin  )
