from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView

from rest_framework.decorators import api_view
from rest_framework.response import Response
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

class CreateItem(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

    def get_absolute_url(self):
        return reverse('/home', kwargs={'pk': self.id})

class DeleteItem(DeleteView):
    model = Item
    success_url = '/'