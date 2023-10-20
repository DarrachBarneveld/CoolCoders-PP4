"""Forms"""
from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import UserChangeForm
from .models import Post


class PostForm(forms.ModelForm):
    """
    A form for creating  blog post instances.

    """

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["excerpt"].widget = forms.Textarea(attrs={"rows": 3})

    class Meta:
        """Get post model, choose fields to display"""

        model = Post
        fields = ["title", "category", "excerpt", "content", "featured_image"]
        widgets = {"content": SummernoteWidget()}


class UpdateUserForm(UserChangeForm):
    """
    A form for editing user information.

    """

    password = None

    class Meta:
        """Get User model, choose fields to display"""

        model = User
        fields = ["username", "email", "first_name", "last_name"]
        help_texts = {"username": None}
