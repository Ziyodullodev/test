from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Ijara
from .serializer import IjaraSerializer


class IjaraViewSet(ListCreateAPIView):
    queryset = Ijara.objects.all()
    serializer_class = IjaraSerializer

class IjaraUpdateViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Ijara.objects.all()
    serializer_class = IjaraSerializer