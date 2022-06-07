from django.shortcuts import render, redirect
from rest_framework.reverse import reverse

from posts.forms import PostForm
from posts.models import Post


def main(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts/main.html', {'posts': posts})


def delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect(reverse("posts:main"))


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    post_form = PostForm(instance=post)
    if request.POST:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse("posts:main"))

    return render(request, 'posts/edit.html', {'form': post_form, 'btn': 'Отредактировать'})

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
