from django.urls import path

from .views import (CategoryApiView, CategoryDetailApiView,
                    FoodApiView, FoodDetailApiView, CommentApiView,
                    CommentDetailApiView)


urlpatterns = [
    path('categories/', CategoryApiView.as_view()),
    path('categories/<int:pk>/', CategoryDetailApiView.as_view()),

    path('foods/', FoodApiView.as_view()),
    path('foods/<int:food_id>/', FoodDetailApiView.as_view()),

    path('foods/category/<int:category_id>/', FoodApiView.as_view()),

    path('foods/<int:food_id>/comments/', CommentApiView.as_view()),
    path('foods/<int:food_id>/comments/<int:pk>/', CommentDetailApiView.as_view()),
]