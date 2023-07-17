from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import *
# Create your views here.



class lap_get(APIView):

    def get(self,request):
        data = Laptop.objects.all()
        ser = laptop_serializer(data,many=True)
        return Response(ser.data)