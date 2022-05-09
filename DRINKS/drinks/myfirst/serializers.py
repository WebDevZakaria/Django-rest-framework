from .models import CarSpecs, Zakaria
from rest_framework import serializers


class CarsSerializer(serializers.ModelSerializer):

    class Meta:

        model = CarSpecs
        fields = ['car_brand', 'Car_model',
                  'production_year', 'car_body', 'engine_type']


class ZakiSerializer(serializers.ModelSerializer):

    class Meta:

        model = Zakaria
        fields = ['zaki_brand', 'zaki_model',
                  'productions_year', 'zaki_body', 'engine_type']
