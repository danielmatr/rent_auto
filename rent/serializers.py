
from rest_framework import serializers
from .models import RentAuto


class RentAutoSerializers(serializers.ModelSerializer):

    class Meta:
        model = RentAuto
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.user
        rent = RentAuto.objects.create(**validated_data)
        return rent

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id')
        representation['user'] = f'{instance.user}'
        return representation