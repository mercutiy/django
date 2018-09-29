from rest_framework import serializers
from api.models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('sku', 'name', 'image', 'collection', 'size')


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('collection',)
