from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Post


# Register your models here.


class PostInline(admin.TabularInline):
    """
    Inline representation of blog posts for the admin panel.

    """

    model = Post
    fields = ("title", "approved", "excerpt")
    extra = 0


class ProfileInline(admin.StackedInline):
    """
    Inline representation of user profiles for the admin panel.

    """

    model = Profile


class UserAdmin(admin.ModelAdmin):
    """
    Admin model configuration for user accounts.

    This class defines the admin panel configuration for user accounts, allowing
    administrators to manage user information such as username, first name, last name,
    and email. It also includes an inline representation of user profiles using the
    `ProfileInline` class

    Example:
        To use this admin configuration for user accounts:

        admin.site.register(User, UserAdmin)

    """

    model = User
    fields = ("username", "first_name", "last_name", "email")
    inlines = [ProfileInline, PostInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
