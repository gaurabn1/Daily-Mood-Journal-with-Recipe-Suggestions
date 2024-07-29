from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('recipes', recipes, name='recipes'),
    path('recipes/<str:mood>/', mood_recipes, name='mood_recipes'),
    path('recipe/<int:id>/', recipe, name='recipe'),
    path('journal/', daily_journal, name='journal'),
    path('edit-journal/<int:id>/', edit_journal, name='edit_journal'),
    path('delete-journal/<int:id>/', delete_journal, name='delete_journal'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
