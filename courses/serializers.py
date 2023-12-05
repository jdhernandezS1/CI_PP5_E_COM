from rest_framework import serializers
from .models import Post


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'featured_image',
            'created_on',
            'likes'
            )
