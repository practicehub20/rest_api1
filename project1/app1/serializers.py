from rest_framework import serializers

from app1.models import ProductModel


class ProductSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price = serializers.FloatField()
    qty = serializers.IntegerField()

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)