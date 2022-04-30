from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main/main.html', {})

def index(request):
    return render(request, 'main/index.html',{})