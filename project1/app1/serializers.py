from rest_framework import serializers

from app1.models import ProductModel


class ProductSerializers(serializers.Serializer):
    idno = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    price = serializers.FloatField()
    qty = serializers.IntegerField()

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.qty = validated_data.get("qty", instance.qty)
        instance.save()
        return instance