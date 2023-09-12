from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views  # 로그인 된 사용자만 권한 부여하기

urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.board, name="board"),
    path("write", views.write, name="write"),
    # path("", include("tinymce.urls")),
]
