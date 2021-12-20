from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.views.generic.edit import UpdateView
from .models import PixelArt, User


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'

class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User

class ProfileUpdateView(UpdateView):
    model = User
    fields = ['email', 'first_name', 'last_name']
    template_name = 'profile_update.html'

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    fields = ['email', 'username', 'password', 'first_name', 'last_name']

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutusView(TemplateView):
    template_name = 'aboutus.html'

class ShopView(ListView):
    template_name = 'shop.html'
    model = PixelArt
    paginate_by = 10

class ProductView(DetailView):
    template_name = 'product.html'
    model = PixelArt
