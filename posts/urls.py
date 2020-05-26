
from django.urls import path, include
from posts import views

urlpatterns = [
    path('',views.index, name='homepage'),
    path('post_view/<int:id>/', views.post_view),

]
