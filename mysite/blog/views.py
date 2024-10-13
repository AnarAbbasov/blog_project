from datetime import timezone
from django.shortcuts import render
from django.views.generic import (
    TemplateView,ListView,
    DetailView, CreateView,
    UpdateView,DeleteView
    
)
from blog.forms import Postform,CommentForm
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class AbouView(TemplateView):
    template_name="about.html"


class PostListView(ListView):
    model=Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by("-published_date"))



class PostDetailView(DetailView):
    model=Post
    

class CreatePostView(LoginRequiredMixin,CreateView):
      login_url="/login/"
      redirect_field_name="blog/post_detail.html"
      
      form_class=Postform
      model=Post
      
class PostUpdateView(LoginRequiredMixin,UpdateView):
      login_url="/login/"
      redirect_field_name="blog/post_detail.html"
      
      form_class=Postform
      model=Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
       model=Post
      