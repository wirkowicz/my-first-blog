from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
	
def kotel(request):
    return render(request, 'blog/kotel.html', {})
	
def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})