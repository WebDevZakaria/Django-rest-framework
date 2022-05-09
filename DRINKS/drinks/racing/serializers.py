from .models import Driver
from rest_framework import serializers

times = 30


class DriverSerializer(serializers.ModelSerializer):

    records = serializers.SerializerMethodField('get_record')

    def get_record(self, driver_object):
        global times
        finish = getattr(driver_object, "rounds")
        if finish and finish < times:
            times = finish
            return times
        else:
            return times

    class Meta:

        model = Driver

        fields = ['driver_name', 'car_brand',
                  'rounds', 'records']
