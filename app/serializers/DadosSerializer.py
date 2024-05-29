from rest_framework import serializers

class DadosSerializer(serializers.Serializer):
    entrada = serializers.CharField()
    tipo = serializers.CharField()