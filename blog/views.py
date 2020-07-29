from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Content
from django.urls import reverse_lazy

# Create your views here.
# You can use the context_object_name to explicitly name your context object.


class BlogTeam(TemplateView):
    template_name = 'navbar/team.html'


class BlogPolicy(TemplateView):
    template_name = 'navbar/policy.html'


class BlogContact(TemplateView):
    template_name = 'navbar/contact.html'


class BlogAbout(TemplateView):
    template_name = 'navbar/about_me.html'


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# Part of the Forms chapter in the book.
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    # Specify the fields the user needs to input.
    fields = ['title', 'author', 'img']


class BlogCreateContent(CreateView):
    model = Content
    template_name = 'post_content.html'
    # Specify the fields the user needs to input.
    fields = ['head', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'img']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
