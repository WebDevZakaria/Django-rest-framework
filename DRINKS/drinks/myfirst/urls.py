from django.urls import path, include

from myfirst import views


from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('car_specs', views.CarSpecViewSet, basename='car_spe')

urlpatterns = [

    path('', include(router.urls)),

    path('zakaria/', views.Zaki.as_view()),
    

]
