
from django.urls import path, include
from posts import views

urlpatterns = [
    path('',views.index, name='homepage'),
    path('post_view/<int:id>/', views.post_view, name="post_view"),
    path('boast_view/', views.boast_view, name='boast'),
    path('roast_view/', views.roast_view, name='roast'),
    path('vote_view/', views.vote_view, name='vote'),
    path('up_vote/<int:post_id>/', views.up_vote, name='up-vote'),
    path('down_vote/<int:post_id>/', views.down_vote, name='down-vote')
]
