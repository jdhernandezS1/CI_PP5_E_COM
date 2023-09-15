from rest_framework import serializers
from .models import Prod


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod
        fields = (
            'id',
            'category',
            'title',
            'title_slug',
            'price',
            'scount',
            'quantity',
            'featured_image',
            'scountbool',
            'description',
            )
