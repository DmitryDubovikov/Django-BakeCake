from django.shortcuts import render

def index(request):
    template = 'index.html'
    title = 'Hello, world!'
    context = {'title': title,}
    return render(request, template, context)

