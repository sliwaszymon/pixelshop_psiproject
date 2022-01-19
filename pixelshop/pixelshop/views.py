from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView
from .models import PixelArt, User, Order
from .forms import RegisterForm
from django.http import JsonResponse
import json


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
            user = form.cleaned_data.get('username')
            messages.success(request, f"Konto dla użytkownika {user} zostało stworzone pomyślnie!")
            return redirect('pixelshop:login')

    context = {'form': form}
    return render(request, template_name, context)

class AboutusView(TemplateView):
    template_name = 'aboutus.html'

class ShopView(ListView):
    template_name = 'shop.html'
    model = PixelArt
    paginate_by = 10

class ProductView(DetailView):
    template_name = 'product.html'
    model = PixelArt

class RegulationsView(TemplateView):
    template_name = 'regulations.html'

def orderCompleteView(request):
    paymentjson = json.loads(request.body)
    pixelart = PixelArt.objects.get(pk=paymentjson['productId'])
    buyer = User.objects.get(pk=paymentjson['buyerId'])
    Order.objects.create(
        user=buyer,
        pixelart=pixelart,
        status='payment_received'
    )
    return JsonResponse('Płatność zakończona pomyślnie!', safe=False)