"""Views"""

# pylint: disable=E1101
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import View, ListView, DetailView, CreateView
from .models import Post, Comment, Category
from .forms import PostForm, UpdateUserForm, UpdateBioForm, CommentForm


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


class PostDetailPage(View):
     """
    A view class for displaying the detail page of a blog post, including its
    comments, comment submission, and related posts.

    """
    template_name = "post-detail.html"

    def get_context_data(self, **kwargs):
        """
        Retrieve context data for rendering the post detail page.

        Args:
        - **kwargs: Additional keyword arguments passed to the view.

        Returns:
        - dict: A dictionary containing context data for rendering the page.
        """

        slug = kwargs.get("slug")
        post = get_object_or_404(Post, slug=slug)
        context = {
            "post": post,
            "comments": post.comments.filter(approved=True).order_by("-created_on"),
            "comment_form": CommentForm(),
            "commented": False,
            "liked": post.likes.filter(id=self.request.user.id).exists(),
            "top_related_posts": self.get_top_related_posts(post),
        }
        return context

    def get_top_related_posts(self, post):
        """
        Get a list of top-related posts within the same category as the given post.

        Args:
        - post: The Post object for which to find related posts.

        Returns:
        - QuerySet: A queryset of related Post objects.
        """
        return Post.objects.filter(category=post.category, approved=True).exclude(
            pk=post.id
        )[:3]

    def get(self, request, slug, *args, **kwargs):
        """
        Handle HTTP GET requests for rendering the post detail page.

        Args:
        - request: The HTTP request object.
        - slug: The slug of the requested post.
        - *args: Additional positional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - HttpResponse: Renders the post detail page with context data.
        """

        context = self.get_context_data(slug=slug)
        return render(request, self.template_name, context)

    def post(self, request, slug):
        """
        Handle HTTP POST requests for submitting a comment on the post.

        Args:
        - request: The HTTP request object.
        - slug: The slug of the post on which the comment is being submitted.

        Returns:
        - HttpResponse: Renders the post detail page with context data.
        """
        comment_form = CommentForm(data=request.POST)
        post = get_object_or_404(Post, slug=slug)
        context = self.get_context_data(slug=slug)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(
                self.request, "Comment created successfully! Review in progress!"
            )
        else:
            messages.error(self.request, "There was an error. Comment not registered")

        return render(request, self.template_name, context)


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
        """
        Retrieves context data for rendering the profile update page.
        Returns:
        - dict: A dictionary containing context data for rendering the page.
        """
        user = self.request.user
        context = {
            "user_form": kwargs.get("user_form", self.user_form_class(instance=user)),
            "password_form": kwargs.get(
                "password_form", self.password_form_class(user)
            ),
            "bio_form": kwargs.get(
                "bio_form", self.bio_form_class(instance=user.profile)
            ),
        }
        return context

    def get(self, request, *args, **kwargs):
        """
        Handles HTTP GET requests for rendering the profile update page.

        Returns:
        - HttpResponse: Renders the profile update page with context data.
        """
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def process_form(self, request, form, form_name):
        context = self.get_context_data()

        if form.is_valid():
            form.save()
            messages.success(self.request, f"{form_name} updated")
        else:
            messages.error(
                self.request, "Profile update failed, please check your input"
            )

        if form_name == "bio_form":
            context["bio_form"] = form
        elif form_name == "password_form":
            context["password_form"] = form
            update_session_auth_hash(self.request, self.request.user)
        elif form_name == "user_form":
            context["user_form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        user_form = self.user_form_class(request.POST, instance=request.user)
        bio_form = self.bio_form_class(request.POST, instance=request.user.profile)
        password_form = self.password_form_class(request.user, request.POST)

        if "bio_form" in request.POST:
            return self.process_form(request, bio_form, "bio_form")

        if "password_form" in request.POST:
            return self.process_form(request, password_form, "password_form")

        if "user_form" in request.POST:
            return self.process_form(request, user_form, "user_form")

        return render(request, self.template_name, context)
