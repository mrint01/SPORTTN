from django.contrib import admin
from .models import Product,Proteines,Materiels,Vetements
# Register your models here.


#admin.site.register(Product)
@admin.register(Proteines)
class ProductProt(admin.ModelAdmin):
    list_display = ['id','nameP','prixP','image']
    readonly_fields = ['image']
@admin.register(Materiels)
class ProductM(admin.ModelAdmin):
    list_display = ['id','nameP','prixP','image']
    readonly_fields = ['image']

@admin.register(Vetements)
class ProductV(admin.ModelAdmin):
    list_display = ['id','nameP','prixP','image']
    readonly_fields = ['image']
