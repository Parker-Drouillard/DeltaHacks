from django.shortcuts import render


def base(request):
    return render(request, 'learning_modules/base.html')

def learn(request):
    return render(request, 'learning_modules/learn.html')

def compare(request):
    return render(request, 'learning_modules/compare.html')

def compare(request):
    return render(request, 'learning_modules/connect.html')