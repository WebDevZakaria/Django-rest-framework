from django.urls import path, include

from racing import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('driver', views.DriverView, basename='driver')

urlpatterns = [

    path('', include(router.urls))

]
