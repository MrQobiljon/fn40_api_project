from django.contrib.gis.geos.prototypes.errcheck import free
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Category, Food
from .serializers import CategorySerializer


class CategoryApiView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            categories = Category.objects.all()
            return Response(CategorySerializer(categories, many=True).data)
        else:
            return Response(CategorySerializer(Category.objects.get(pk=pk)).data)

    def post(self, request: Request, pk: int = None):
        if not pk:
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            category = serializer.save()
            return Response(CategorySerializer(category).data)
        else:
            return Response({"message": "Method POST not allowed!"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request: Request, pk: int = None):
        if not pk:
            return Response({"message": "Method PUT not allowed!"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            category = get_object_or_404(Category, pk=pk)
            serializer = CategorySerializer(data=request.data, instance=category)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(CategorySerializer(category).data)

    def delete(self, request: Request, pk: int = None):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response({"message": "Category Deleted Successful!!!"},
                        status=status.HTTP_204_NO_CONTENT)



class FoodApiView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            foods = Food.objects.order_by('-created')
            foods_list = []
            for food in foods:
                foods_list.append(
                    {
                        'id': food.pk,
                        'name': food.name,
                        "text": food.text,
                        "price": food.price,
                        "created": food.created,
                        "add_menu": food.add_menu,
                        "category_id": food.category.pk
                    }
                )
            return Response(foods_list)
        else:
            food = Food.objects.get(pk=pk)
            return Response(model_to_dict(food))

    def post(self, request: Request, pk: int = None):
        if not pk:
            name = request.data.get("name", None)
            price = request.data.get("price", None)
            category_id = request.data.get("category_id", None)
            if name and price and category_id:
                food = Food.objects.create(**request.data)
                return Response(model_to_dict(food), status=status.HTTP_201_CREATED)
            return Response({"message": "Xato!!!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Method POST not allowed!"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)