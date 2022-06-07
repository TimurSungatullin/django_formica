from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Название')
    text = forms.CharField(label='Текст', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ["title", "text"]