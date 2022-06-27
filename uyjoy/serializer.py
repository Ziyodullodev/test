from rest_framework.serializers import ModelSerializer
from .models import Ijara
from django.contrib.auth.models import User

class IjaraSerializer(ModelSerializer):
    class Meta:
        model = Ijara
        fields = '__all__'