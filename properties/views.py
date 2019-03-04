from django.shortcuts import render
from rest_framework import viewsets
from .models import Property
from properties.serializers import PropSerializer

class PropViewSet(viewsets.ModelViewSet):

    queryset = Property.objects.all().order_by('created')
    serializer_class = PropSerializer

