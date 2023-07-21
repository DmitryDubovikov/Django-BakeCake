from django.shortcuts import render
from .models import Berry, Decor, Topping, Shape, Level


def index(request):
    template = "index.html"
    title = "Hello, world!"

    context = {
        "title": title,
        "berries": Berry.objects.all(),
        "decors": Decor.objects.all(),
        "toppings": Topping.objects.all(),
        "shapes": Shape.objects.all(),
        "levels": Level.objects.all(),
    }
    return render(request, template, context)
