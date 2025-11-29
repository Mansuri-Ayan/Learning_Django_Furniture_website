from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def cart(request):
    return render(request, "cart.html")


def index(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


def pricing(request):
    return render(request, "pricing.html")


def checkout(request):
    return render(request, "checkout.html")


def shop(request):
    return render(request, "shop.html")


def thankyou(request):
    return render(request, "thankyou.html")


def login(request):
    if request.method == "POST":
        u1 = request.POST["uname"]
        p1 = request.POST["password"]
        print(u1, p1)
        user = auth.authenticate(username=u1, password=p1)
        if user is not None:
            auth.login(request, user)
            print("Login Successfull")
            return redirect("/")
        else:
            print("Login falid")
            return redirect("/login/")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    print("Logout Successfully")
    return redirect("/login/")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confo_password = request.POST["confo_password"]
        if password != confo_password:
            print("Password does't Match")
            return redirect("/signup/")
        if User.objects.filter(username=username).exists():
            print("User already exits! Try another Username")
            return redirect("/signup/")

        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        print("User Created Successfully")
        return redirect("/login/")

    return render(request, "signup.html")
