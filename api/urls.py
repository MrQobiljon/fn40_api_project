from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, FoodApiViewSet)

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('foods', FoodApiViewSet, basename='food')


urlpatterns = [

    path('', include(router.urls)),

    # path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('categories/<int:pk>/', CategoryViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
    # )),

    # path('foods/', FoodApiView.as_view()),
    # path('foods/<int:food_id>/', FoodDetailApiView.as_view()),
    #
    path('foods/category/<int:category_id>/', FoodApiViewSet.as_view({'get': 'list'})),
    #
    # path('foods/<int:food_id>/comments/', CommentApiView.as_view()),
    # path('foods/<int:food_id>/comments/<int:pk>/', CommentDetailApiView.as_view()),
]