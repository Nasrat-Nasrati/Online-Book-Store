from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import CartItem

def index_of_carts(request):
    carts=CartItem.objects
    # return HttpResponse("Hello Dear viewer,Welcome to the index of Carts page")
    return render(request,'index_of_carts.html',{'carts':carts})



