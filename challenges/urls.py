from django.urls import path
from . import views as challenges_views

app_name = 'challenges'

urlpatterns = [
    path('jan/', challenges_views.january, name='january'),
    path('feb/', challenges_views.february, name='feburary'),
    path('mar/', challenges_views.march, name='march'),
]
