from django.contrib import admin
from store.models import Category, Product, ProductImages, VariationValue


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(VariationValue)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     readonly_fields = ('thumbnail_preview',)
#
#     def thumbnail_preview(self, obj):
#         return obj.thumbnail_preview
#
#     thumbnail_preview.short_description = 'Thumbnail Preview'
#     thumbnail_preview.allow_tags = True


# admin.site.register(Product, ProductAdmin)
