from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.


def main(request):
    return render(request, "practice_static.html")


def upload(request):
    return render(request, "upload.html")


def upload_create(request):
    form = Profile()
    form.title = request.POST["title"]
    try:
        form.image = request.FILES["image"]
    except:
        pass
    form.save()
    return redirect("/practice_static_app/profile/")


def profile(request):
    profile = Profile.objects.all()
    return render(request, "profile.html", {"profile": profile})

