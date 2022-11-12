from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post  # uses the Post Model
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'  # the template our view will render
    paginate_by = 6   # limiting the amount of posts that show on a page

