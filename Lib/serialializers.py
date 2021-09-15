from Lib.models import Lib
from rest_framework import serializers

class LibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lib
        fields = ['titulo','editora','resumo','autor','id']

