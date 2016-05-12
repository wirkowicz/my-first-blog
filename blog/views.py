from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
	
def kotel(request):
    return render(request, 'blog/kotel.html', {})
	
def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})