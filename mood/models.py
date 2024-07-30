from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)

    def __str__(self):
        return self.username

class Mood(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('stressed', 'Stressed'),
        ('relaxed', 'Relaxed'),
        ('excited', 'Excited'),
        ('anxious', 'Anxious'),
        ('angry', 'Angry'),
        ('content', 'Content'),
        ('bored', 'Bored'),
        ('motivated', 'Motivated'),
        ('grateful', 'Grateful'),
        ('overwhelmed', 'Overwhelmed'),
        ('hopeful', 'Hopeful'),
        ('tired', 'Tired'),
        ('confident', 'Confident'),
    ]

    mood = models.CharField(max_length=100, choices=MOOD_CHOICES, default='happy')

    def __str__(self):
        return self.mood


class MoodEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    journal_entry = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.mood}'

class Recipe(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    recipe_image = models.ImageField(upload_to='recipe_images', null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title
    

class RecentActivity(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE)
    activity = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.activity}'