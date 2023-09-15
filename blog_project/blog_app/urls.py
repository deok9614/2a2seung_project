from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views  # 로그인 된 사용자만 권한 부여하기

urlpatterns = [
    path("admin", admin.site.urls),
    path("board", views.board, name="board"),
    path("write", views.write, name="write"),
    # path("", include("tinymce.urls")),
    # path("board", views.login_success, name="board"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.board_client, name="board_client"),
    path("board_admin", views.board_admin, name="board_admin"),
    # path("", include("tinymce.urls")),
]
