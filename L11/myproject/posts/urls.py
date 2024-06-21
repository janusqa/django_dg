from django.urls import path
from . import views

# this namespaces the URL patterns below so we can reuse
# generic names like "page" in different apps. We just need
# to prefix where ever we use such names with the the app_name.
# the patter would be for example if we want to specify a url
# {% url 'posts:list' %}
# {% url 'posts:page', slug=your_variable_here %}
app_name = "posts"

urlpatterns = [
    path("", views.posts_list, name="list"),
    path("new-post", views.post_new, name="new-post"),
    path("<slug:slug>", views.post_page, name="page"),
]
