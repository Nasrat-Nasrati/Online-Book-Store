from django.shortcuts import render
from .models import  Order
# Create your views here.

from django.http import HttpResponse

def index_order_management(request):
    # return HttpResponse("Hello Dear reader, I have warm welcome to you and this is the order management page")
    orders=Order.objects
    return render(request,'index_of_orders.html',{'orders':orders})


