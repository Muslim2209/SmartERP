from rest_framework import serializers

from document.models import Info, Document
from reference.api.serializers import CitySerializer


class InfoSerializer(serializers.ModelSerializer):
    # city = CitySerializer()

    class Meta:
        model = Info
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
