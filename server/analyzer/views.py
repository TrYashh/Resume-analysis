from django.shortcuts import render

def front(request):
    return render(request, 'front.html')  # Render front page

def login_page(request):
    return render(request, 'login.html')  # Render login page
