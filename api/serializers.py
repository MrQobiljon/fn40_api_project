from rest_framework import serializers

from .models import Category, Food, Comment



class FoodSerializerForCategory(serializers.ModelSerializer):
    class Meta:
        model = Food
        # fields = '__all__'
        exclude = ['category']


class CategorySerializer(serializers.ModelSerializer):

    # foods = serializers.StringRelatedField(many=True)
    # foods = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # foods = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='food-detail')
    # foods = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    # url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    foods = FoodSerializerForCategory(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['id', 'name', 'foods']
        # fields = ['id', 'name']
        # exclude = ['id']


class CategorySerializerForFood(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    bolim = CategorySerializerForFood(read_only=True, source='category')

    class Meta:
        model = Food
        fields = '__all__'
        extra_kwargs = {'category': {'write_only': True}}


class FoodAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']



# class FoodSerializer(serializers.ModelSerializer):
#     my_category = serializers.ChoiceField(choices=Category.objects.all(), write_only=True)
#     class Meta:
#         model = Food
#         fields = '__all__'
#         # read_only_fields = ['text']
#         depth = 1
#
#     def create(self, validated_data):
#         category = validated_data.pop("my_category")
#         food = Food.objects.create(**validated_data, category=category)
#         return food
#
#     def update(self, instance, validated_data):
#         instance.category = validated_data.pop("my_category") if validated_data.get("my_category") else instance.category
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()
#         return instance






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
