from django.shortcuts import render

def index(request):
    return render(request, 'learning_modules/index.html')

def learning(request):
    return render(request, 'learning_modules/learning.html')

def compare(request):
    return render(request, 'learning_modules/compare.html')

def compare_info_form(request):
    return render(request, 'learning_modules/compare_info.html')
