from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import permission_classes, throttle_classes
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import viewsets


class DriverView(viewsets.ModelViewSet):
    serializer_class = DriverSerializer

    permission_class = [AllowAny]
    
    def get_queryset(self):

        driver = Driver.objects.all()

        return driver
        
