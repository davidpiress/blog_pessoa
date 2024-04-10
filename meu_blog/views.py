from django.shortcuts import render

def welcome(request):
    return render(request, 'meu_blog/welcome.html')
