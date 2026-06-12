from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
























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
