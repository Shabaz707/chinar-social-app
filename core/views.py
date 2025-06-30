# F:\chinar\core\views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import JsonResponse
from django.views.decorators.http import require_POST # Ensures only POST requests are accepted

from .models import Post, Like # Make sure Like is imported
from .forms import PostForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to Chinar.')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.replace('_', ' ').title()}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    posts = Post.objects.all()
    # For each post, check if the current user has liked it
    for post in posts:
        post.is_liked_by_user = Like.objects.filter(user=request.user, post=post).exists()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been shared successfully!')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.replace('_', ' ').title()}: {error}")
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@require_POST # Ensure this view only accepts POST requests
@login_required
def like_post(request):
    post_id = request.POST.get('post_id')
    # Use get_object_or_404 for cleaner error handling if post doesn't exist
    post = get_object_or_404(Post, id=post_id)

    # Check if the user has already liked this post using the Like model
    user_liked = Like.objects.filter(user=request.user, post=post).exists()

    if user_liked:
        # If already liked, then unlike (delete the Like object)
        Like.objects.filter(user=request.user, post=post).delete()
        post.likes -= 1 # Decrement the likes count on the Post model
        action = 'unliked'
    else:
        # If not liked, then like (create a new Like object)
        Like.objects.create(user=request.user, post=post)
        post.likes += 1 # Increment the likes count on the Post model
        action = 'liked'

    post.save() # Save the updated Post object (with new likes count)

    return JsonResponse({'success': True, 'likes': post.likes, 'action': action})
