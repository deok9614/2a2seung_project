from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def board(request):
    articles = Post.objects.all().order_by("-modified")
    username = request.user
    return render(request, "blog_app/board.html", {"username": username, "articles": articles})


# def write(request):
#     if request.method == "POST":
#         title = request.POST["title"]
#         content = request.POST["content"]
#         Post.objects.create(title=title, content=content)
#         return redirect("board")
#     return render(request, "blog_app/write.html")


def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            image = form.cleaned_data["image"]
            is_draft = bool(request.POST.get("draft"))  # '글 임시저장' 버튼 확인
            if is_draft:
                # 글을 임시 저장합니다.
                Post.objects.create(title=title, content=content, image=image, is_draft=True)
            else:
                # 글을 업로드합니다.
                Post.objects.create(title=title, content=content, image=image, is_draft=False)
            return redirect("board")  # 글 목록 페이지로 이동
    else:
        form = PostForm()
    return render(request, "blog_app/write.html", {"form": form})


########## LOGIN ##########


def social_login_view(request):
    return render(request, "registration/login.html")


def signup(request):
    # 회원가입 버튼을 눌렀을때,
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")

    # url 경로를 타고 맨 처음에 회원가입 페이지를 들어왔을때
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


def login_success(request):
    username = request.user
    return render(request, "blog_app/board.html", {"username": username})


def logout_view(request):
    logout(request)
    return redirect("login")


def board_client(request):
    return render(request, "blog_app/board_client.html")


def board_admin(request):
    return render(request, "blog_app/board_admin.html")
