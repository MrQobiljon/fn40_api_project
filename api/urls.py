from django.urls import path

from .views import (CategoryApiView, CategoryDetailApiView,
                    FoodApiView, FoodDetailApiView)


urlpatterns = [
    path('categories/', CategoryApiView.as_view()),
    path('categories/<int:pk>/', CategoryDetailApiView.as_view()),

    path('foods/', FoodApiView.as_view()),
    path('foods/<int:food_id>/', FoodDetailApiView.as_view()),

    path('foods/category/<int:category_id>/', FoodApiView.as_view()),
]