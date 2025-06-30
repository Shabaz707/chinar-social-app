# F:\chinar\core\forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image_url'] # Fields that users can input
        widgets = {
            'caption': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your caption here...'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Enter image URL (e.g., https://example.com/image.jpg)'}),
        }
        labels = {
            'caption': 'Caption',
            'image_url': 'Image URL',
        }