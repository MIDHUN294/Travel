from django.shortcuts import render
from  django.http import  HttpResponse
from.models import place

# Create your views here.
def fun(request):
    obj = place.objects.all()

    return render(request,"index.html",{'results':obj})

def blog(request):
    obj=blog.objects.all()
    return render(request,"index.html",{'news':obj})

def addition(request):
    num1 =int(request.POST["num1"])
    num2 =int(request.POST["num2"])
    num3=(num1+num2)
    return render(request,'result.html',{'add':num3})
