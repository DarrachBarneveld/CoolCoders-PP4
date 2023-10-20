"""Views"""

# pylint: disable=E1101
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import View, ListView, DetailView, CreateView
from .models import Post, Comment, Category
from .forms import PostForm, UpdateUserForm, UpdateBioForm


class HomePageView(View):
    """
    A view class for displaying a list of categories and featured posts on the homepage.

    """

    def get(self, request, *args, **kwargs):
        """
        Retrieves the posts from the database and returns the most popular, trending by likes
        and editors pick

        """
        all_posts = Post.objects.filter(approved=True)
        popular_post = (
            all_posts.annotate(comment_count=Count("comments"))
            .order_by("-comment_count")
            .first()
        )

        trending_posts = all_posts.annotate(like_count=Count("likes")).order_by(
            "-like_count"
        )[:3]

        editors_pick = get_object_or_404(
            Post, slug="ais-influence-on-tech-shaping-the-future"
        )

        return render(
            request,
            "home.html",
            {
                "all_posts": all_posts,
                "popular_post": [popular_post],
                "trending_posts": trending_posts,
                "editors_pick": [editors_pick],
            },
        )


class CategoryPage(ListView):
    """
    A view class for displaying a list of posts based on a specific category.

    """

    template_name = "category.html"
    paginate_by = 3
    model = Category
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        """
        Queries the posts related to a category from the database
        """
        # Get the slug parameter from the URL
        slug = self.kwargs["slug"]

        # Filter the queryset based on the slug
        category = get_object_or_404(Category, title=slug)
        queryset = Post.objects.filter(category=category, approved=True)

        return queryset


class PostDetailPage(DetailView):
    model = Post
    template_name = "post-detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(approved=True).order_by(
            "-created_on"
        )
        context["commented"] = False
        context["liked"] = self.object.likes.filter(id=self.request.user.id).exists()
        context["top_related_posts"] = self.get_top_related_posts()
        return context

    def get_top_related_posts(self):
        return (
            Post.objects.filter(category=self.object.category, approved=True)
            .exclude(pk=self.object.id)
            .annotate(comment_count=Count("comments"))[:3]
        )


class AddPostPage(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create a new blog post.

    Methods:
    - form_valid: Overrides the base method to set the post author to the
      currently logged-in user before saving the form.

    Mixins:
    - LoginRequiredMixin: Ensures that only authenticated users can access
      this view.
    """

    form_class = PostForm
    template_name = "add_post.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Post created successfully! Review in progress!")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Post creation failed. Please check your input.")
        return response


class ProfilePageView(DetailView):
    template_name = "profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return get_object_or_404(User, username=self.kwargs.get("username"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        posts = Post.objects.filter(author=user, approved=True)
        total_posts = posts.count()

        # Filter by posts the user likes
        favourites = user.blogpost_like.filter(approved=True)

        # Generate total number of comments on authors posts
        total_comments = Comment.objects.filter(post__in=posts, approved=True).count()

        # Generate total number of likes of all posts
        total_likes = sum(post.number_of_likes() for post in posts)

        posts_with_comment_count = []
        for post in posts:
            comment_count = Comment.objects.filter(post=post, approved=True).count()
            posts_with_comment_count.append((post, comment_count))

        context["total_posts"] = total_posts
        context["total_comments"] = total_comments
        context["total_likes"] = total_likes
        context["posts_with_comment_count"] = posts_with_comment_count
        context["favourites"] = favourites

        return context


class UpdateProfileView(LoginRequiredMixin, View):
    """
    Allows a user to update their profile information, including username,
    password, and bio.
    """

    template_name = "update_profile.html"
    user_form_class = UpdateUserForm
    password_form_class = PasswordChangeForm
    bio_form_class = UpdateBioForm

    def get_context_data(self, **kwargs):
        user = self.request.user
        user_form = self.user_form_class(instance=user)
        bio_form = self.bio_form_class(instance=user.profile)

        password_form = self.password_form_class(user)

        return {
            "user_form": user_form,
            "bio_form": bio_form,
            "password_form": password_form,
        }

    def get(self, request, *args, **kwargs):
        """
        Handles HTTP GET requests for rendering the profile update page.

        Returns:
        - HttpResponse: Renders the profile update page with context data.
        """
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        user_form = self.user_form_class(request.POST, instance=request.user)
        password_form = self.password_form_class(request.user, request.POST)
        bio_form = self.bio_form_class(request.POST, instance=request.user.profile)

        print(request.POST)
        if "bio_form" in request.POST and bio_form.is_valid():
            print("bio change")
            # bio_form.save()
        elif "password_form" in request.POST and password_form.is_valid():
            print("password")

            # password_form.save()
            # update_session_auth_hash(request, request.user)
        elif "user_form" in request.POST and user_form.is_valid():
            print("user")
            # user_form.save()

        return render(request, self.template_name, context)
