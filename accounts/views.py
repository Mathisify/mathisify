from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateUserForm, UserUpdateForm
from django.core.mail import EmailMessage

from django.views import View
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken...")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Registered...")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.is_active = False
                user.save()
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

                domain = get_current_site(request).domain
                link = reverse(
                    "verify",
                    kwargs={
                        "uidb64": uidb64,
                        "token": token_generator.make_token(user),
                    },
                )
                activate_url = f"https://{domain}{link}"
                email_body = f"""
                Hey {user.first_name}!
                Please use this link to verify your account.
                {activate_url}
                """
                email = EmailMessage(
                    "Activate your Account",
                    email_body,
                    "accounts@mathisify.org",
                    [email],
                )
                email.send(fail_silently=False)
                return render(request, "verify_email.html")
        else:
            messages.info(request, "Password Not Matching...")
            return redirect("register")

    else:
        return render(request, "register.html")


class VerificationView(View):
    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                messages.info(request, "User is already activated")
                return redirect("login")

            if user.is_active:
                return redirect("login")
            user.is_active = True
            user.save()

            messages.success(request, "Account activated successfully")
            return redirect("login")

        except Exception as ex:
            pass

        return redirect("login")


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
