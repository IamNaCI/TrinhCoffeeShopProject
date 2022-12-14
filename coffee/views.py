from django.shortcuts import render, redirect
from .models import Carousel, Contact, Order
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    carousel = Carousel.objects.all()
    context = {'carousel': carousel}
    return render(request, 'coffee/index.html', context)


def menu(request):
    context = {'menu': menu}
    return render(request, 'coffee/menu.html', context)


def contact_request(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.phone_number = phone_number
        contact.subject = subject
        contact.message = message
        contact.save()

    return render(request, 'coffee/contact.html')


# this is for user registration
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="coffee/register.html", context={"register_form": form})


# this is for user login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="coffee/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


def view_order(request):
    order = Order.objects.all()
    context = {'order': order}
    return render(request, 'coffee/order.html', context)


def create_order(request):
    form = Order(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order')

    return render(request, 'coffee/order.html', {'form': form})


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    form = Order(request.POST or None, instance=order)

    if form.is_valid():
        form.save()
        return redirect('order')

    return render(request, 'coffee/order.html', {'form': form})


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('order')

    return render(request, 'coffee/menu.html', {'order': order})


def order_request(request):
    if request.method == "POST":
        order = Order()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        drink = request.POST.get('drinkSelect')
        size = request.POST.get('sizeSelect')
        sugar = request.POST.get('sugarSelect')
        ice = request.POST.get('iceSelect')
        style = request.POST.get('hotorIce')

        order.name = name
        order.email = email
        order.phone_number = phone_number
        order.drink = drink
        order.size = size
        order.sugar = sugar
        order.ice = ice
        order.style = style
        order.save()

    return render(request, 'coffee/order.html')
