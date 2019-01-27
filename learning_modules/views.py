from django.shortcuts import render

def index(request):
    return render(request, 'learning_modules/base.html')

<<<<<<< HEAD

def learning(request):
    return render(request, 'learning_modules/learning.html')
=======
def learn(request):
    return render(request, 'learning_modules/learn.html')

def compare(request):
    return render(request, 'learning_modules/compare.html')

def compare(request):
    return render(request, 'learning_modules/connect.html')
>>>>>>> perfectView
