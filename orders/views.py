from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Order
from django.views.generic import ListView


# Create your views here.
class OrderList(ListView):
    model = Order

    def get_queryset(self):
        data = Order.objects.filter(user=self.request.user)
        return  data
    
def checkout (request):
    return render (request,'orders/checkout.html',{})
 