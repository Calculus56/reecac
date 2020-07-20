"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.models import Post
from blog.sitemaps import (
    StaticViewSitemap,
    StaticViewContact,
    StaticViewAbout,
    StaticViewPolicy,
    StaticViewTeam,
)
from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap # new
# The empty string means URL requests should be redirected to the blog's URLs for further instruction.


sitemaps = {
    'blog': GenericSitemap({
        'queryset': Post.objects.all()
    }, priority=0.9),
    'static': StaticViewSitemap,
    'contacts': StaticViewContact,
    'about': StaticViewAbout,
    'policy': StaticViewPolicy,
    'team': StaticViewTeam,
}

urlpatterns = [
    path('thebossreecac/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('blog.urls')),
    path('sitemap.xml', sitemap, # new
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
