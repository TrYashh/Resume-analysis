from django.contrib import admin
from django.urls import path, include
from analyzer import views  # Import views from the analyzer app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', views.front, name='front'),  # Homepage
    path('login/', views.login_page, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('register/', views.register_view, name='register'),  # Register page
]
