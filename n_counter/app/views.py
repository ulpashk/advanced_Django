from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Food, Consume, HealthGoal
from django.contrib.auth.decorators import login_required
from .forms import HealthGoalForm, FoodForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    if request.method == "POST":
        if 'food_consumed' in request.POST:
            food_consumed = request.POST['food_consumed']
            consume = Food.objects.get(name=food_consumed)
            user = request.user
            consume = Consume(user=user, food_consumed=consume)
            consume.save()

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    actual_carbs = sum([food.food_consumed.carbs for food in consumed_food])
    actual_proteins = sum([food.food_consumed.proteins for food in consumed_food])
    actual_fats = sum([food.food_consumed.fats for food in consumed_food])
    actual_calories = sum([food.food_consumed.calories for food in consumed_food])

    context = {
        'foods': foods,
        'consumed_food': consumed_food,
        # 'nutrient_goals': nutrient_goals,
        'actual_carbs': actual_carbs,
        'actual_proteins': actual_proteins,
        'actual_fats': actual_fats,
        'actual_calories': actual_calories,
        # 'form': form
    }

    return render(request, 'app/index.html', context)


@login_required
def update_goals(request):
    goal, created = HealthGoal.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = HealthGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = HealthGoalForm(instance=goal)
    return render(request, "app/update_goals.html", {"form": form})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'app/delete.html')


@login_required
def chart_data(request):
    consumed = Consume.objects.filter(user=request.user)
    goal, _ = HealthGoal.objects.get_or_create(user=request.user)
    data = {
        "labels": [c.food_consumed.name for c in consumed],
        "carbs": [c.food_consumed.carbs for c in consumed],
        "proteins": [c.food_consumed.proteins for c in consumed],
        "fats": [c.food_consumed.fats for c in consumed],
        "calories": [c.food_consumed.calories for c in consumed],
        "goal_carbs": goal.carb_goal,
        "goal_proteins": goal.protein_goal,
        "goal_fats": goal.fat_goal,
        "goal_calories": goal.daily_calorie_goal,
    }
    return JsonResponse(data)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "app/register.html", {"form": form})


def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the food to the global registry
            return redirect("index")  # Redirects back to the homepage
    else:
        form = FoodForm()
    return render(request, "app/add_food.html", {"form": form})