from django.shortcuts import render, redirect
from vege.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

# Route to get and show the recipes content
def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = request.POST
            recipe_name = data.get('recipe_name')
            recipe_description = data.get('recipe_des')
            recipe_image = request.FILES.get('recipe_image')
            Recipe.objects.create(
                recipe_name = recipe_name,
                recipe_description = recipe_description,
                recipe_image = recipe_image
            )
            return redirect("/recipes/")
        else:
            return redirect("/login/")
    recipeQuerySet = Recipe.objects.all()
    context = {'recipes':recipeQuerySet}
    return render(request, "vege/index.html", context)

# Route to update the recipes 
@login_required(login_url="/login/")
def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_des = request.POST.get('recipe_des')
        recipe_image = request.FILES.get("recipe_image")

        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_des

        if recipe_image:
            recipe.recipe_image = recipe_image

        recipe.save()
        return redirect("/recipes/")

    context = {'recipe':recipe}
    return render(request, "vege/update_recipe.html", context);


# Route to delete the recipes 
@login_required(login_url="/login/")
def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()

    return redirect("/recipes/")

