from django.contrib import admin
from .models import *
admin.site.register(CustomUser)
admin.site.register(Mood)
admin.site.register(MoodEntry)
admin.site.register(Recipe)
admin.site.register(RecentActivity)
