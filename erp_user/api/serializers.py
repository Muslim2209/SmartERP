from rest_framework import serializers

from document.api.serializers import InfoSerializer, DocumentSerializer
from erp_user.models import User


class UserSerializer(serializers.ModelSerializer):
    info = InfoSerializer()
    document = DocumentSerializer()

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'code',
                  'phone_number',
                  'email',
                  'date_of_birth',
                  'gender',
                  'language',
                  'role',
                  'supervisor',
                  'info',
                  'document',
                  'password']
