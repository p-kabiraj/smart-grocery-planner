from django.contrib import admin
from .models import Product, Platform, Price


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)
    ordering = ('name',)


class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'platform', 'price')
    list_filter = ('platform', 'product')
    search_fields = ('product__name', 'platform__name')
    ordering = ('-id',)
    
    def get_readonly_fields(self, request, obj=None):
        # Make fields read-only after creation
        if obj:
            return ('product', 'platform')
        return ()


admin.site.register(Product, ProductAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Price, PriceAdmin)