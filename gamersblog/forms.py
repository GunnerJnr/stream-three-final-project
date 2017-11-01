from django import forms
from gamersblog.models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_body', 'post_images', 'post_author', 'post_status')

        def clean_title(self):
            cd = self.cleaned_data['post_title']
            if BlogPost.objects.filter(post_title=cd).exists():
                raise forms.ValidationError('The post title already exists')
            return cd
