from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from ..models import Textos, labels, TextosLabels
from ..repositories.textos_labels_repository import textos_labels_repository
from ..services.listar_textos_tipoidlabel_service import listar_textos_tipoidlabel_service
from ..services.listar_labels_service import listar_labels_service
from ..services.listar_textos_labels_service import listar_textos_labels_service
from ..services.atualizar_texto_service import atualizar_texto_service

class AtualizarTextoView(APIView):
    def put(self, request):
        # extrair dados
        idtextoslabels = request.data.get('id')
        texto_data = request.data.get('texto')
        tipo_data = request.data.get('tipo')
        labels_data = request.data.get('labels')

        return atualizar_texto_service().atualizar_texto(idtextoslabels, texto_data, tipo_data, labels_data)
    
class ListarLabelsView(APIView):
    def get(self, request):

        labels_list_json = listar_labels_service().listar_labels()
        return JsonResponse(labels_list_json, safe=False, status=status.HTTP_200_OK)
    
class ListarTextosLabelsView(APIView):
    def get(self, request):

        textos_labels_list_json = listar_textos_labels_service().listar_textos_labels()

        return JsonResponse(textos_labels_list_json, safe=False, status=status.HTTP_200_OK)
    
class ListarTextosTipoIdLabelView(APIView):
    def get(self, request):

        Lista = listar_textos_tipoidlabel_service().listar_textos_tipo_idlabel()
        return JsonResponse(Lista, safe=False, status=status.HTTP_200_OK)