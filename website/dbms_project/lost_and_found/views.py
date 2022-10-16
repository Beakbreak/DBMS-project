from django.shortcuts import render

def index(request):
    return render(request,"lost_and_found/index.html")
    
def itemform(request):
    return render(request,"lost_and_found/itemform.html")

def item(request):
    return render(request,"lost_and_found/item.html")

def login(request):
    return render(request,"lost_and_found/login.html")

def category(request):
    return render(request,"lost_and_found/category.html")

def myreq(request):
    return render(request,"lost_and_found/my_requests.html")