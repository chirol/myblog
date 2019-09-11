from django.contrib import messages
from django.views.generic import ListView
from .models import Post


class PostView(ListView):
    model = Post
    queryset = Post.objects.order_by('-date') # クエリセットを日付（降順）に
    paginate_by = 10 # ページネーション設定
    print(Post.tags)
