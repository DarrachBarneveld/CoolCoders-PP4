"""URL Patterns"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("add-post/", views.AddPostPage.as_view(), name="add-post"),
    path("profile/<str:username>/", views.ProfilePageView.as_view(), name="profile"),
    path("update_profile/", views.UpdateProfileView.as_view(), name="update_profile"),
    path("<slug:slug>/", views.CategoryPage.as_view(), name="index"),
    path("post/<slug:slug>/", views.PostDetailPage.as_view(), name="post-detail"),
]
