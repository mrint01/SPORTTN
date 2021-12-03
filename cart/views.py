from django.shortcuts import render
from .utils import cookieCart, cartData, guestOrder
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        itemss = order.orderitem_set.all()
       
    else:
        itemss = []
        order = {'get_cart_total' :0 , 'get_cart_items' :0}
   
    context = {'itemss' : itemss , 'order' : order}
    return render(request,  "cart/index.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    value = data['valeur']



    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	

    if action =="add" and int(value) >1:
        orderItem.quantity = (orderItem.quantity + int(value)) 
    elif action == 'add':
    	orderItem.quantity = (orderItem.quantity  + 1)
    
    elif action == 'remove':
    	orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()


    if orderItem.quantity <= 0:
    	orderItem.delete()

    return JsonResponse('Item was added', safe=False)