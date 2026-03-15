from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    FormView,
    ListView
)
from .models import Post
from .forms import LoginForm, RegisterForm
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
    template_name = 'login.html'
    
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')