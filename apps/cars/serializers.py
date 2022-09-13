from rest_framework.serializers import ModelSerializer

from .models import CarModel

class CarSerializer (ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class CarAllSerializer(ModelSerializer):
    class Meta:
         model = CarModel
         fields = ('id','brand','year')