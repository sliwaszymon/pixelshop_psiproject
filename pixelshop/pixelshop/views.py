from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView
from .models import PixelArt, User
from .forms import RegisterForm


class HomePageView(TemplateView):
    template_name = 'homepage.html'

class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User

class ProfileUpdateView(UpdateView):
    model = User
    fields = ['email', 'first_name', 'last_name']
    template_name = 'profile_update.html'

def registerView(request):
    template_name = 'registration/register.html'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pixelshop:login')

    context = {'form': form}
    return render(request, template_name, context)


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
