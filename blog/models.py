"""Models"""
# pylint: disable=E1101
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Create your models here.


class Profile(models.Model):
    """
    Model to represent extend auth User Class to add addition
    profile information.

    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    level = models.IntegerField(default=1)

    def __str__(self):
        """Return a string representation of the object (the post's title)."""
        return str(self.user)

    def get_level(self):
        """To get a users current level based on post count"""

        post_count = self.user.blog_posts.count()
        new_level = (post_count // 3) + 1

        self.level = new_level
        self.save()

        return self.level


def create_user_profile(instance, created):
    """
    Signal handler function to create a user profile when a
    new user is created.

    This function is connected to the User model's post_save signal.
    It creates a user profile with a slug based on the user's
    username when a new user is created.
    """
    if created:
        Profile.objects.create(user=instance)


models.signals.post_save.connect(create_user_profile, sender=User)


class Category(models.Model):
    """
    Model to represent categories for blog posts.
    """

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        """To update the name shown in the plural form"""

        verbose_name_plural = "Categories"

    def __str__(self):
        """Return a string representation of the object (the post's title)."""

        return f"{self.title}"


class Post(models.Model):
    """
    Model to represent a blog article.

    This model represents a blog article with various
    attributes such as title, author, content, and likes.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.CharField(
        max_length=200,
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=None)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name="blogpost_like", blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """To display the posts by created_on in ascending order"""

        ordering = ["-created_on"]

    def __str__(self):
        """Return a string representation of the object (the post's title)."""

        return f"{self.title}"

    def number_of_likes(self):
        """To calculate the amount of likes on a post"""
        return self.likes.count()

    def total_comments(self):
        """To calculate the total comments on a post"""

        return self.comments.filter(approved=True).count()

    def get_absolute_url(self):
        """Return the absolute URL for editing this post."""

        return reverse("edit_post", args=[str(self.pk)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Represents a comment on a blog post.
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """To display the comments by created_on in ascending order"""

        ordering = ["created_on"]

    def __str__(self):
        """Return a string representation of the object (the post's title)."""

        return f"Comment {self.body} by {self.name}"
        