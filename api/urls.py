from django.urls import path

from .views import CategoryApiView, FoodApiView


urlpatterns = [
    path('categories/', CategoryApiView.as_view()),
    path('categories/<int:pk>/', CategoryApiView.as_view()),

    path('foods/', FoodApiView.as_view()),
    path('foods/<int:pk>/', FoodApiView.as_view()),
]