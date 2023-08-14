from django.contrib import admin
from.models import Product
# Register your models here.
class proyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Product, proyectAdmin)