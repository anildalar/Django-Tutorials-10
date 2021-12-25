from django.db import models

# Create your models here.

class Category(models.Model):
    #1. Property 
    cat_name = models.CharField(max_length=100,unique=True)
    cat_desc = models.TextField(max_length=100,blank=True)
    cat_slug = models.SlugField(max_length=100)
    cat_image = models.ImageField(upload_to='uploads/categories')
    #2. Contstructor

    #3. Method Dunder/Magic 
    def __str__(self):
            return self.cat_name

    #4. Nested Class
    class Meta:
        #1. Property
        verbose_name = 'category'
        verbose_name_plural = 'categories'

        #2. Contstructor

        #3. Method
        
        #4. Nested Class
    
