from django.contrib import admin
from .models import Post, Category, PostCategory

# Register your models here.

class PostCatAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = [field.name for field in PostCategory._meta.get_fields()] # генерируем список имён всех полей
    #для более красивого отображения

class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title','text','autor') # генерируем список имён всех полей
    #для более красивого отображения
    list_filter = ('title','text','autor') # добавляем примитивные фильтры в нашу админку
    search_fields =('title','text', 'autor__name', 'category_post__category_name') # указываем поля фильтрации

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostCategory,PostCatAdmin)

