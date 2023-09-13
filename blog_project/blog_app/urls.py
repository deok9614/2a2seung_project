from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views  # 로그인 된 사용자만 권한 부여하기

urlpatterns = [
    path("admin", admin.site.urls),
<<<<<<< HEAD
    path("", views.board, name="board"),
    path("write", views.write, name="write"),
    # path("", include("tinymce.urls")),
    path("signup", views.signup, name="signup"),
    path("board/", views.login_success, name="board"),
    path("logout/", views.logout_view, name="logout"),
    path("login", views.social_login_view, name="login"),
]
=======
    path("board_client", views.board_client, name="board_client"),
    path("board_admin", views.board_admin, name="board_admin"),
    # path("", include("tinymce.urls")),
]
>>>>>>> client/admin
