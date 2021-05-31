from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('add/', views.CreateItem.as_view(), name='create_item'),
  path('<int:pk>/delete/', views.DeleteItem.as_view(), name='delete_item'),

]