from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/login')
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    context = {
        'posts' : posts
    }
    return render(request, 'posts/posts_list.html', context)

@login_required(login_url='/users/login')
def post_new(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            form.save()
            return redirect('posts_list')
    else :
        form = CreatePostForm()
    return render(request, 'posts/post_new.html', {'form': form})

@login_required(login_url='/users/login')
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post' : post
    }
    return render(request, 'posts/post_detail.html', context)