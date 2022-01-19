"""Views file."""

# Standard Library
import json

# Django
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

# Local
from .forms import RegisterForm
from .models import Order
from .models import PixelArt
from .models import User


class HomePageView(TemplateView):
    """HomePageView class."""

    template_name = 'homepage.html'


class ProfileView(DetailView):
    """ProfileView class."""

    template_name = 'profile.html'
    model = User


class ProfileUpdateView(UpdateView):
    """ProfileUpdateView class."""

    model = User
    fields = ['email', 'first_name', 'last_name']
    template_name = 'profile_update.html'


def RegisterView(request):
    """Registerview function view."""
    template_name = 'registration/register.html'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Konto dla użytkownika {user} zostało stworzone pomyślnie!',
                )
            return redirect('pixelshop:login')

    context = {'form': form}
    return render(request, template_name, context)


class AboutusView(TemplateView):
    """AboutusView class."""

    template_name = 'aboutus.html'


class ShopView(ListView):
    """ShopView class."""

    template_name = 'shop.html'
    model = PixelArt
    paginate_by = 10


class ProductView(DetailView):
    """ProductView class."""

    template_name = 'product.html'
    model = PixelArt


class RegulationsView(TemplateView):
    """RegulationsView class."""

    template_name = 'regulations.html'


def OrderCompleteView(request):
    """Ordercompleteview function view."""
    paymentjson = json.loads(request.body)
    pixelart = PixelArt.objects.get(pk=paymentjson['productId'])
    buyer = User.objects.get(pk=paymentjson['buyerId'])
    Order.objects.create(
        user=buyer,
        pixelart=pixelart,
        status='payment_received',
    )
    return JsonResponse('Płatność zakończona pomyślnie!', safe=False)
