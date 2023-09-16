from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import *
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage


# Create your views here.
def board(request):
    articles = BlogPost.objects.all().order_by("-modified")
    username = request.user
    return render(request, "blog_app/board.html", {"username": username, "articles": articles})


##########  WRITE ##########


# 포스트 업로드, 업데이트, 삭제 (강사님 함수 create_or_update_post)
def write(request, post_id=None):
    # 글수정 페이지의 경우
    if post_id:
        post = get_object_or_404(BlogPost, id=post_id)

    # 글쓰기 페이지의 경우, 임시저장한 글이 있는지 검색 => 에러나서 미완
    else:
        post = BlogPost()

    # 업로드/수정 버튼 눌렀을 때
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # title = form.cleaned_data["title"]
            # content = form.cleaned_data["content"]
            # image = form.cleaned_data["image"]
            # is_draft = bool(request.POST.get("draft"))  # '글 임시저장' 버튼 확인
            # if is_draft:
            #     # 글을 임시 저장합니다.
            #     BlogPost.objects.create(title=title, content=content, image=image, is_draft=True)
            # else:
            #     # 글을 업로드합니다.
            #     BlogPost.objects.create(title=title, content=content, image=image, is_draft=False)

            # 글쓴이 설정
            post.author_id = request.user.username

            post.save()
            return redirect("post_detail", post_id=post.id)  # 업로드/수정 페이지로 이동
    else:
        form = BlogPostForm()
    return render(request, "blog_app/write.html", {"form": form})


# 이미지 업로드
class image_upload(View):
    # 사용자가 이미지 업로드 하는경우 실행
    def post(self, request):
        # file필드 사용해 요청에서 업로드한 파일 가져옴
        file = request.FILES["file"]

        # 저장 경로 생성
        filepath = "uploads/" + file.name

        # 파일 저장
        filename = default_storage.save(filepath, file)

        # 파일 URL 생성
        file_url = settings.MEDIA_URL + filename

        # 이미지 업로드 완료시 JSON 응답으로 이미지 파일의 url 반환
        return JsonResponse({"location": file_url})


########## LOGIN ##########

# def signup(request):
#     # 회원가입 버튼을 눌렀을때,
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("login")

#     # url 경로를 타고 맨 처음에 회원가입 페이지를 들어왔을때
#     else:
#         form = UserCreationForm()

#     return render(request, "registration/signup.html", {"form": form})


def board_client(request):
    return render(request, "blog_app/board_client.html")


def board_admin(request):
    return render(request, "blog_app/board_admin.html")


def post_detail(request, post_id):
    # 포스트 id로 게시물 가져옴
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "blog_app/board.html", {"post": post})
