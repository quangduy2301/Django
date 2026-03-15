from django.shortcuts import render
from django.views.generic import (
    FormView,
    ListView
)
from .models import Post
from .forms import LoginForm
from django.contrib.auth.models import User


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    
class LoginView(FormView):
    model = User
    form_class = LoginForm
    template_name = "login.html"