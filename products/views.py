from django.shortcuts import render
from .models import Product
from django.views import View
from django.contrib import messages

class ProductView(View):
 def get(self,request):
  painting = Product.objects.filter(category='P')
  handicrafts= Product.objects.filter(category='H')
  statuary = Product.objects.filter(category='S')
  Minatory = Product.objects.filter(category='M')
  return render(request,'Artist/home.html',{'painting':painting,'handicraft':handicrafts,
   'statuary':statuary,'Minatory':Minatory})

class ProductDetailsView(View):
 def get(self,request,pk):
  product = Product.objects.get(pk=pk)
  return render(request,'Artist/productdetails.html',{'product':product})