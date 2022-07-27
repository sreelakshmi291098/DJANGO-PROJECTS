from django.shortcuts import render
from app8.models import Register

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def viewsdata(request):
    data=Register.objects.all()
    return render(request,'views.html',{'data':data})

    