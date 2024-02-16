from django.shortcuts import render, redirect
from vege.models import *
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()

# Create your views here.
def home(request):
    return render(request, "Home/index.html")


def search_recipe(request):
    query = request.GET["query"]
    recipe_name = Recipe.objects.filter(recipe_name__icontains=query)
    recipe_description = Recipe.objects.filter(recipe_description__icontains=query)
    recipes = recipe_name.union(recipe_description)

    if len(recipes) == 0:
        context = {'find':False, 'query':query}
        return render(request, "Home/search.html", context)

    else:
        context = {'recipes':recipes, 'find':True, 'query':query}
        return render(request, "Home/search.html", context)
        
def login_page(request):
    if request.method == 'POST':
        data = request.POST
        phone = data.get("phone")
        password = data.get("password")

        if not User.objects.filter(phone_number = phone).exists():
            messages.error(request, "Invalid phone")
            return redirect("/login/")

        user = authenticate(request, phone_number=phone, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "Invalid password")
            return redirect("/login/")
        
    return render(request, "Home/login.html")

def register(request):
    if request.method == 'POST':
        data = request.POST
        phone = data.get("phone")
        password = data.get("password")

        user = User.objects.filter(phone_number = phone)

        if user.exists():
            messages.error(request, "Username is already exists!")
            return redirect("/register/")
        
        user = User(
            phone_number = phone,
        )

        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("/")
        
    return render(request, "Home/register.html")


def logout_page(request):
    print("logout executed")
    logout(request)
    return redirect("/recipes/")