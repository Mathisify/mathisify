from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CreateUserForm, UserUpdateForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(
                    request,
                    f"An account was created for {user}. Please complete your profile after logging in.",
                )
                return redirect("login")
        context = {"form": form}
        return render(request, "register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("/accounts/profile/")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Username Or Password is incorrect")

        context = {}
        return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your profile has been updated")
            return redirect("profile")

    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        "user_form": user_form,
    }
    return render(request, "profile.html", context)
