from django.contrib import admin

from .models import Berry, Cake, Decor, Level, Order, Shape, Topping


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'address',
        'date',
        'time',
        'comment',
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
        'inscription',
        'image'
    ]


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
