from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('contact/', views.contact_request, name="contact"),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('order/', views.order_request, name="order"),
    path('logout/', views.logout_request, name="logout")
]
