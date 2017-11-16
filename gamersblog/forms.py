from django import forms
from gamersblog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_body', 'post_images', 'post_author')
