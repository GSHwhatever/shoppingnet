#conding=utf-8
from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('',views.IndexView.as_view())
]
