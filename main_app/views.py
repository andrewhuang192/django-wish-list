from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView

# from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import ItemSerializer 
from django.urls import reverse


def home(request):
  item_list = Item.objects.all()
  print('=================================')
  print(request)
  print(item_list)
  return render(request, 'index.html', { 'items': item_list })

def about(request):
  print('=================================')
  print(request)
  
  return render(request, 'about.html')

# def items_index(request):
#   item_list = Item.objects.all()
#   print('=================================')
#   print(request)
#   print(item_list)
#   return render(request, 'index.html', { 'items': item_list })

# @api_view
# def create_item(request):
#     print('================')
#     data = request.data
#     item = Item.objects.create(
#         description=data['description']
#     )
#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     return Response(serializer.data)

# class ItemList(ListView):
#     model = Item
    
    # def get_object(self, queryset=None):
    #     obj = Item.objects.filter(pk=self.kwargs['post_id']).first()
    #     return obj

class CreateItem(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

    def get_absolute_url(self):
        return reverse('/home', kwargs={'pk': self.id})

class DeleteItem(DeleteView):
    model = Item
    success_url = '/'