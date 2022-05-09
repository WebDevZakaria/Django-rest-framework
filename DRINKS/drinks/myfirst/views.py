from django.shortcuts import render
# Create your views here.
from .models import Car, CarSpecs, Zakaria
from .serializers import CarsSerializer, ZakiSerializer

from rest_framework.decorators import api_view, permission_classes, throttle_classes

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from rest_framework import viewsets

from rest_framework.views import APIView

from django.core.mail import send_mail

import threading

# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def myfirstproject(request):

#   return


class HandleNotification(threading.Thread):

    def __init__(self, message, subject, recipient_list):

        self.message = message
        self.subject = subject
        self.recipient_list = recipient_list

        threading.Thread.__ini__(self)

    def run(self):

        from_email = 'zikoubouregbi@gmail.com'

        send_mail(self.subject, self.message, from_email,
                  self.recipient_list, fail_silently=False)


class CarSpecViewSet(viewsets.ModelViewSet):

    serializer_class = CarsSerializer

    def send_email(self, message, subject, recipient_list):

        from_email = 'zikoubouregbi@gmail.com'

        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)

    def get_queryset(self):

        car_specs = CarSpecs.objects.all()

        return car_specs

    def retrieve(self, request, *args, **kwargs):

        params = kwargs

        params_list = params['pk'].split('-')

        cars = CarSpecs.objects.filter(

            car_brand=params_list[0], production_year=params_list[1])

        serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        new_car = CarSpecs.objects.create(request.data['car_brand'], request.data['Car_model'],
                                          request.data['production_year'], request.data['car_body'], request.data['engine_type'])

        new_car.save()

       # self.send_email("this is notification", "notification",
        #                ["zakariabouregbi@gmial.com", ])

        HandleNotification("this is notification", "notification", [
                           "zakariabouregbi@gmial.com", ]).start()

        serializer = CarsSerializer(new_car)

        return Response(serializer.data)


class Zaki(APIView):

    serializer_class = ZakiSerializer

    def get_queryset(self):

        zaki = Zakaria.objects.all()

        return zaki

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]

            if id != None:

                carr = Zakaria.objects.get(id=id)

                serializer = ZakiSerializer(carr)

        except:

            cars = self.get_queryset()

            serializer = ZakiSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        serializer = ZakiSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
