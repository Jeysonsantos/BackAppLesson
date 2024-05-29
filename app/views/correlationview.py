from django.shortcuts import render
from ..services.entrada_texto_service import entrada_texto_service

from ..serializers.DadosSerializer import DadosSerializer
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Textos, labels, TextosLabels

class EntradaTextoView(APIView):

    def post(self, request):

        service = entrada_texto_service()
        serializer = DadosSerializer(data=request.data)

        if serializer.is_valid():
            entrada = serializer.validated_data.get('entrada')
            tipo = serializer.validated_data.get('tipo')

            resultado_query = service.processar_entrada(tipo, entrada)

            return JsonResponse({'resultado': resultado_query[0]}, safe=False, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 