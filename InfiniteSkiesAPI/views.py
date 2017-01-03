from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from InfiniteSkiesAPI.Serializers import DataSerializer
from InfiniteSkiesAPI.models import data


class createDataList(generics.ListCreateAPIView):
    queryset = data.objects.all()
    serializer_class = DataSerializer
