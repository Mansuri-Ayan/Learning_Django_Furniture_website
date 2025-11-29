from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("blog/", blog, name="blog"),
    path("cart/", cart, name="cart"),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("contact/", contact, name="contact"),
    path("checkout/", checkout, name="checkout"),
    path("shop/", shop, name="shop"),
    path("thankyou/", thankyou, name="thankyou"),
    path("pricing/", pricing, name="pricing"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),
]
