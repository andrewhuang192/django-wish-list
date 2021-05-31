from django.db import models
from django.urls import reverse
from datetime import date

class Item(models.Model):
  description = models.CharField(max_length=50)

  def __str__(self):
    return self.description
  
# class Meta:
#     model = Item 
#     fields = ['-date']

  def get_absolute_url(self):
    return reverse('base', kwargs={'pk': self.id})