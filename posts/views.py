from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.reverse import reverse

from posts.forms import PostForm
from posts.models import Post
from posts.utils import get_temp


@login_required
def main(request):
    posts = Post.objects.all().order_by('-id')
    temp = get_temp()
    return render(request, 'posts/main.html', {'posts': posts, 'temp': temp})


@login_required
def delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect(reverse("posts:main"))


@login_required
def edit(request, pk):
    post = Post.objects.get(pk=pk)
    post_form = PostForm(instance=post)
    if request.POST:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse("posts:main"))

    return render(request, 'posts/edit.html', {'form': post_form, 'btn': 'Отредактировать'})


@login_required
def create(request):
    post_form = PostForm()
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect(reverse("posts:main"))

    return render(request, 'posts/edit.html', {'form': post_form, 'btn': 'Создать'})
