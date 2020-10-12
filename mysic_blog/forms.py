from django import forms
from mysic_blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is the title?'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How about add some tag?'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'And the best author is...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enjoy'}),
        }
