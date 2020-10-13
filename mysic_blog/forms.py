from django import forms
from mysic_blog.models import Post, Category


choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)
# [('Vocal', 'Vocal'), ('Musical Instruments', 'Musical Instruments')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is the title?'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How about add some tag?'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'And the best author is...'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Sing or play'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enjoy'}),
        }
