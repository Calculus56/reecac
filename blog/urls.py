from django.urls import path, include
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogCreateContent,
    BlogUpdateView,
    BlogDeleteView,
    BlogContact,
    BlogAbout,
    BlogPolicy,
    BlogTeam,
)

# The empty string tells Python to match all values
# The urls are custom made, just be professional.
urlpatterns = [
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/new/<int:pk>/content/', BlogCreateContent.as_view(), name='post_content'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('contact', BlogContact.as_view(), name='contact'),
    path('chat', BlogAbout.as_view(), name='chat'),
    path('policy', BlogPolicy.as_view(), name='policy'),
    path('about', BlogTeam.as_view(), name='about'),
    path('', BlogListView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
