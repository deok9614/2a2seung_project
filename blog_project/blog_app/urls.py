from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views  # 로그인 된 사용자만 권한 부여하기
from django.conf import settings
from django.conf.urls.static import static
from .views import image_upload

urlpatterns = [
    path("login", views.userLogin, name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.board_client, name="board_client"),
    path("board", views.board, name="board"),
    path("write", views.write, name="write"),
    path("editPost/<int:post_id>", views.write, name="editPost"),
    path("image_upload", image_upload.as_view(), name="image_upload"),
    path("post/<int:post_id>", views.post_detail, name="post_detail"),
    # path("", include("tinymce.urls")),
    # path("board", views.login_success, name="board"),
    path("board_admin", views.board_admin, name="board_admin"),
    path("autocomplete/", views.autocomplete, name="autocomplete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
