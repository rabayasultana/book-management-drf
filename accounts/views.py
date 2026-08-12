from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Registration successful. You can now log in."
            )

            return redirect("login")

    else:
        form = UserRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )
    
    
def login_view(request):

    if request.user.is_authenticated:
        return redirect("book_list")

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            # Django session login
            login(request, user)

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)

            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            next_url = request.GET.get("next")

            messages.success(
                request,
                "Welcome back!"
            )

            return render(
                request,
                "accounts/login_success.html",
                {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "next_url": next_url or "",
                }
            )

    else:
        form = AuthenticationForm()

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )


# def login_view(request):

    if request.user.is_authenticated:
        return redirect("book_list")

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            # Django session login
            login(request, user)

            next_url = request.GET.get("next")

            if next_url:
                return redirect(next_url)

            messages.success(
                request,
                "Welcome back!"
            )

            return redirect("book_list")

    else:
        form = AuthenticationForm()

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )