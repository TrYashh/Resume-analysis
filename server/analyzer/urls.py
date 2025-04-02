from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('login/', views.login_page, name='login'),
]
