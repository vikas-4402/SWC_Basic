from django.shortcuts import render
from .models import Item,OrderItem
# Create your views here.
def home(request):
    context ={
        'items' : Item.objects.all()
    }
    return render(request,'shop/home.html',context)

def cart(request):
    content ={
        'things' : OrderItem.objects.all()
    }
    return render(request,'shop/cart.html',content)
