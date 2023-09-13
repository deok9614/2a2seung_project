from django.shortcuts import render

# Create your views here.


def board_client(request):
    return render(request, 'blog_app/board_client.html')

def board_admin(request):
    return render(request, 'blog_app/board_admin.html')