from django.urls import path
from . import views as challenges_views

app_name = 'challenges'

urlpatterns = [
    path('', challenges_views.index, name='index'),
    path('<int:month>/', challenges_views.monthly_challenge_by_number, name='month-by-number'),
    path('<str:month>/', challenges_views.monthly_challenge, name='month-by-name'),
]
