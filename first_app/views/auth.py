import re
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .employee import employee_list


def password_validation(request, password):
    has_error = False

    if len(password) < 8:
        messages.error(request, "Password must be at least 8 characters.")
        has_error = True
    if not re.search("[A-Z]", password):
        messages.error(request, "Must contain one uppercase letter.")
        has_error = True
    if not re.search("[a-z]", password):
        messages.error(request, "Must contain one lowercase letter.")
        has_error = True
    if not re.search("[0-9]", password):
        messages.error(request, "Must contain one number.")
        has_error = True
    if not re.search("[@#$%^&*!]", password):
        messages.error(request, "Must contain special character.")
        has_error = True

    return has_error


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return employee_list(request)
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "signup.html", {"email": email})

        if password_validation(request, password1):
            return render(request, "signup.html", {"email": email})

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, "signup.html", {"email": email})

        User.objects.create_user(username=email, email=email, password=password1)
        return render(request, "login.html")

    return render(request, "signup.html")


def forgot_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        new_password = request.POST.get("new_password")

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            return render(request, "login.html")
        except User.DoesNotExist:
            messages.error(request, "Email not found")

    return render(request, "forgot.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html")