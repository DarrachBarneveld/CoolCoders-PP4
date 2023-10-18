"""Models"""
# pylint: disable=E1101
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Create your models here.
class Article(models.Model):
    """
    Model to represent a blog article.

    This model represents a blog article with various attributes such as title, author, content, and likes.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_article"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.CharField(
        max_length=200,
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="blog_article_like", blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """To display the posts by created_on in ascending order"""

        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"

    def number_of_likes(self):
        """To calculate the amount of likes on a post"""
        # pylint: disable=no-member
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
