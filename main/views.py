from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Post, View
import requests
from dhooks import Webhook, Embed


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(",")[-1].strip()
    elif request.META.get("HTTP_X_REAL_IP"):
        print("returning REAL_IP")
        ip = request.META.get("HTTP_X_REAL_IP")
    else:
        print("returning REMOTE_ADDR")
        ip = request.META.get("REMOTE_ADDR")
    return ip


def discordLogger(ip_address):
    hook = Webhook(
        "https://discord.com/api/webhooks/789723530467606538/yKGanjuoO9CSP1soNSM9hmSaCNds7Ke68UsMS2GcyT18fuDpBO-0jZpqEG93pR7ck2eC"
    )
    headers = {"x-lookup-ip": f"{ip_address}"}
    resp = requests.get("https://uni.aadibajpai.workers.dev", headers=headers)
    if resp.ok:
        embed = Embed(
            description="University Found",
            color=0x2ECC71,
            timestamp="now",  # sets the timestamp to current time
        )
        embed.add_field(name="IP Address", value=ip_address)
        embed.add_field(name="University", value=resp.text)

        return hook.send(embed=embed)
    return print("no uni")


def index(request):
    views = View.objects.all()
    ip_address = get_client_ip(request)
    discordLogger(ip_address)
    return render(request, "index.html", {"views": views})


def uni(request):
    try:
        ip_add = request.headers["x-lookup-ip"]
    except KeyError:
        ip_add = get_client_ip(request)
    discordLogger(ip_add)
    return JsonResponse({"ip": f"{ip_add}"})


def chapterone(request):
    views = View.objects.all()
    return render(request, "chapterone.html", {"views": views})


def about(request):
    views = View.objects.all()
    return render(request, "about.html", {"views": views})


def compandint(request):
    views = View.objects.all()
    return render(request, "compandint.html", {"views": views})


def histcomp(request):
    views = View.objects.all()
    return render(request, "histcomp.html", {"views": views})


def chapterzero(request):
    views = View.objects.all()
    return render(request, "chapterzero.html", {"views": views})


def chapterzero2(request):
    views = View.objects.all()
    return render(request, "chapterzero2.html", {"views": views})


def welcometoscratch(request):
    views = View.objects.all()
    return render(request, "welcometoscratch.html", {"views": views})


def diginfo(request):
    views = View.objects.all()
    return render(request, "diginfo.html", {"views": views})


def index2(request):
    views = View.objects.all()
    return render(request, "index2.html", {"views": views})


def elements(request):
    views = View.objects.all()
    return render(request, "elements.html", {"views": views})


def loops(request):
    views = View.objects.all()
    return render(request, "loops.html", {"views": views})


def ifstate(request):
    views = View.objects.all()
    return render(request, "ifstate.html", {"views": views})


def firstprogram(request):
    views = View.objects.all()
    return render(request, "firstprogram.html", {"views": views})


def workshops(request):
    if request.user.is_authenticated:
        views = View.objects.all()
        return render(request, "workshops.html", {"views": views})
    else:
        return redirect("/accounts/register/")


def search(request):
    query = request.GET["query"]
    posts = Post.objects.filter(title__icontains=query)
    params = {"posts": posts}
    return render(request, "search.html", params)
