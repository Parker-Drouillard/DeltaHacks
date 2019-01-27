from django.shortcuts import render


def base(request):
    return render(request, 'learning_modules/base.html')
