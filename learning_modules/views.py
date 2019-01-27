from django.shortcuts import render


def index(request):
    return render(request, 'learning_modules/index.html')
