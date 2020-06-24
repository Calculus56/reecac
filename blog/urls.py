from django.urls import path, include
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

# The empty string tells Python to match all values
# The urls are custom made, just be professional.
urlpatterns = [
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
