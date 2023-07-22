from django.contrib import admin
from django.utils.html import format_html

from .models import Berry, Cake, Decor, Level, Order, Shape, Topping


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'address',
        'date',
        'time',
        'status',
        'client'
    ]
    list_filter = [
        'status',
    ]


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'levels',
        'shape',
        'topping',
        'berries',
        'decor',
        'inscription'
    ]
    readonly_fields = [
        'get_image_preview',
    ]

    def get_image_preview(self, obj):
        if not obj.image:
            return 'выберите картинку'
        return format_html('<img src="{url}" style="max-height: 200px;"/>', url=obj.image.url)
    get_image_preview.short_description = 'превью'


@admin.register(Level)
class CakeLevelAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price'
    ]


@admin.register(Shape)
class CakeShapeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price'
    ]


@admin.register(Topping)
class CakeToppingAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price'
    ]


@admin.register(Berry)
class CakeBerryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price'
    ]


@admin.register(Decor)
class CakeDecorAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price'
    ]
