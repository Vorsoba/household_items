from django.contrib import admin
from .models import Item


# admin.site.register(Item)

@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    fields = ('name', 'lifetime', 'price', 'consistency', 'usage_environment', 'depreciation')
    # list_display = ['name', 'lifetime', 'price']   model retur)
    readonly_fields = ['name', 'depreciation', 'lifetime', 'price', 'id']

'''    def depreciation(self, obj):
        if obj.price is None:
            return 0
        return round(obj.price / 12, 2)'''
