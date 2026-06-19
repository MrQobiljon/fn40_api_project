from rest_framework import serializers

from .models import Category, Food


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['id']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        # read_only_fields = ['text']
        # depth = 1


class FoodAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        depth = 1


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#
#     def create(self, validated_data):
#         category = Category.objects.create(**validated_data)
#         return category
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.save()
#         return instance


# class FoodSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     text = serializers.CharField(required=False)
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     created = serializers.DateTimeField(read_only=True)
#     add_menu = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         category = Food.objects.create(**validated_data)
#         return category
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.text = validated_data.get("text", instance.text)
#         instance.price = validated_data.get("price", instance.price)
#         instance.add_menu = validated_data.get("add_menu", instance.add_menu)
#         instance.category_id = validated_data.get("category_id", instance.category_id)
#         instance.save()
#         return instance




















# from datetime import datetime
# from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
# import io
# from rest_framework.parsers import JSONParser
#
#
# class Comment:
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()
#
# comment = Comment(email='leila@example.com', content='foo bar')
#
#
# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()
#
#
# def serialization():
#     serializer = CommentSerializer(comment)
#     print(serializer.data)
#
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#
#
# def deserialization():
#     json = b'{"email":"leila@example.com","content":"foo bar","created":"2016-01-27T15:17:10.375877"}'
#     print('deserialization', json)
#
#     stream = io.BytesIO(json)
#     data = JSONParser().parse(stream)
#     print('deserialization', data)
#
#     serializer = CommentSerializer(data=data)
#     serializer.is_valid()
#     # True
#     print('deserialization', serializer.validated_data)
