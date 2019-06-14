from django.contrib import messages
from django.views.generic import ListView
from .models import Post


class PostView(ListView):
    model = Post
    print(Post.tags)