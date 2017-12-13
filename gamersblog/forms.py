"""
Forms.py:
"""
from django import forms
from gamersblog.models import BlogPost


# Create the class for handling the blog post forms
class BlogPostForm(forms.ModelForm):
    """
    BlogPostForm(forms.ModelForm):
        This class handles the forms needed for the user to create a post
    """
    class Meta:
        """
        model: BlogPost - the blog post model
        fields: - the blog post form fields needed to create a blog post
        """
        model = BlogPost
        fields = ('post_title', 'post_body', 'post_images')
