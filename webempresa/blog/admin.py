from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #permite que se vea en el admin los campos created and updated del modelo
    #personalizar el admin
    list_display = ('title','author','published','post_categories') #columnas a mostrar en el listado
    ordering = ('author','published') #las opciones a ordenar
    search_fields = ('title','author__username','categories__name') #opciones por las cuales buscar
    date_hierarchy = 'published' #filtrar por fecha
    list_filter = ('author__username','categories__name') #filtrar por relaciones

    #crear campos personalizados
    def post_categories(self,obj):
        return ', '.join([c.name for c in obj.categories.all().order_by("name")])
    
    post_categories.short_description = 'Categorias'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


