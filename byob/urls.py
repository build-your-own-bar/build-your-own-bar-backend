from django.urls import path
from . import views

urlpatterns = [
    path('drinks/', views.DrinkList.as_view(), name='drink_list'),
    path('drinks/<int:pk>',
         views.DrinkDetail.as_view(), name='drink_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]
