from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_page(request):
    print("Login page accessed.")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"User {username} logged in successfully.")
            return redirect('home_page')
        else:
            return redirect('login_page')
    else:
        return render(request, 'registration/login.html')