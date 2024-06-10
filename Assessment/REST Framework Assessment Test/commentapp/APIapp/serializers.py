from rest_framework import serializers
from .models import commentInfo

class commentserializers(serializers.ModelSerializer):
    class Meta:
        model=commentInfo
        fields='__all__'