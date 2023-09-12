from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse


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
