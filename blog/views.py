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
	
	# to jest widok post detail. przyjmuje on request (linka z url) oraz dodatkowa zmienna przekazana w linku
	# wywoluje on metody z modelu. get_object_or_404 jest zdefiniowana w Django. 
	# kolejny krok to renderowanie strony przy uzyciu templatki html przekazujac jej parametry w zmiennej post.
	# pk=pk mozna zastapic tocoDostalemzLinku = id (baza danych)