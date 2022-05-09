from turtle import st
from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinkSerializer

from rest_framework.decorators import api_view


from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def dink_list(request):

    if request.method == "GET":

        drink = Drinks.objects.all()

        serializer = DrinkSerializer(drink, many=True)

        return Response(serializer.data)

    if request.method == "POST":

        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drinkdetail(request, pk):

    try:

        drinkss = Drinks.objects.get(id=pk)

    except drinkss.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":

        serializer = DrinkSerializer(drinkss)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = DrinkSerializer(drinkss, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":

        drinkss.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
