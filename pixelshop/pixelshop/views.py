from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView
from .models import User


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'

class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    fields = ['email', 'username', 'password', 'first_name', 'last_name']

