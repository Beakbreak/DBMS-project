from django.shortcuts import render

def index(request):
    return render(request,'lost_and_found/index.html')
