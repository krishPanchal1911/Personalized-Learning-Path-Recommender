from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend/', views.recommend_path, name='recommend_path'),
    path('quiz/', views.quiz, name='quiz_view'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
    path('my-recommendations/', views.my_recommendations, name='my_recommendations'),
]