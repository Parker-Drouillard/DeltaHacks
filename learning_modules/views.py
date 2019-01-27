from django.shortcuts import render

def index(request):
    return render(request, 'learning_modules/base.html')


def learning(request):
    return render(request, 'learning_modules/learning.html')
