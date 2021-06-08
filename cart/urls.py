#coding=utf-8

from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('',views.AddCartView.as_view()),
    path('queryAll/',views.CartListView.as_view(),name='queryAll'),
]