from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
   path('', views.index),
   path('database/<int:id>/', views.post_view)
]