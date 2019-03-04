from rest_framework import serializers
from .models import Property

class PropSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('pk','owner', 'address', 'price', 'image')