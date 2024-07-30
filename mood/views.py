from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Import Paginator
from django.core.paginator import Paginator


from .models import *
from mood.forms import *
# Create your views here.

@login_required
def index(request):
    moods = Mood.objects.all()

    context = {
        'moods' : moods,
    }
    return render(request, 'index.html', context)

@login_required
def recipes(request):
    recipes = Recipe.objects.all().order_by('?')
    return render(request, 'recipes.html', {'recipes': recipes})

@login_required
def mood_recipes(request, mood):
    _mood = Mood.objects.get(mood = mood)
    recipes = Recipe.objects.filter(mood = _mood)
    if not recipes:
        return redirect('recipes')

    return render(request, 'recipes.html', {"recipes": recipes})

@login_required
def recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    ingredients = recipe.ingredients.split('\n')
    instructions = recipe.instructions.split('\n')
    return render(request, 'recipe.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'instructions': instructions
    })


@login_required
def daily_journal(request):
    if request.method == "POST":
        journal_form = MoodEntryForm(request.POST)
        if journal_form.is_valid():
            journal = journal_form.save(commit=False)
            journal.user = request.user
            journal.save()
            RecentActivity.objects.create(user = request.user, activity = "You created the journal")
            return redirect('journal')
        print(journal)
    else:
        journal_form = MoodEntryForm()
    
    # Setup Paginator
    p = Paginator(MoodEntry.objects.filter(user = request.user), 2)
    page = request.GET.get('page')
    journals = p.get_page(page)
    
    return render(request, 'journal_entry.html', {"journal" : journal_form, "journals" : journals})


@login_required
def delete_journal(request, id):
    journal = MoodEntry.objects.get(id = id)
    journal.delete()
    RecentActivity.objects.create(user = request.user, activity = "You deleted the journal")
    return redirect('journal')


@login_required
def edit_journal(request, id):
    journal = MoodEntry.objects.get(id = id)
    journal_entry = request.POST.get('edit_journal_entry')
    if journal_entry:
        journal.journal_entry = journal_entry
        journal.save()
    
    return redirect('journal')

@login_required
def profile(request):
    user = CustomUser.objects.get(username = request.user.username)

    #Calculate journal count
    journal_count = MoodEntry.objects.filter(user = user).count()

    #Calculate Average Journals per week
    todays_date = timezone.now()
    start_of_the_year = todays_date.replace(month=1, day=1)
    journals_this_year = MoodEntry.objects.filter(user = user, date__gte = start_of_the_year).count()
    weeks_passed = (todays_date - start_of_the_year).days // 7
    average_journals_per_week = journals_this_year / max(weeks_passed, 1)

    #Recent Activities
    recent_activities = RecentActivity.objects.filter(user = user)

    context = {
        "user" : user,
        "journal_count" : journal_count,
        "average_journals_per_week" : average_journals_per_week,
        "recent_activities" : recent_activities,
    }

    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    
    return redirect('profile')


@login_required
def delete_recent_activity(request, id):
    entry = RecentActivity.objects.get(id = id)
    entry.delete()
    return redirect('profile')
    
    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, f"Account created for {user.first_name}!")
            return redirect('login')
        else:
            print("Form Not Valid")
    user_form = RegisterForm()
    return render(request, 'register.html', {"user_form": user_form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')    
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"{request.user.first_name}, You are Logged In!")
                return redirect("index")
            else:
                messages.error(request, "Wrong Credentials!")
                return redirect('login')
        else:
            print("Form Not Valid")
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {"login_form": login_form})
    
def logout_user(request):
    logout(request)
    return redirect('login')