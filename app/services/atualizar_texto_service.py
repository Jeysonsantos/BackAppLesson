
from app.repositories.textos_labels_repository import textos_labels_repository
from rest_framework.response import Response
from rest_framework import status


class atualizar_texto_service:
    def atualizar_texto(self, idtextoslabels ,texto_data,tipo_data,labels_data):
        #if nao tiver id, crie um nova associacao
        if(idtextoslabels == None or idtextoslabels == '' or idtextoslabels == 0):

            # Verifica se o texto ja existe no banco de dados 
            texto, created = textos_labels_repository().get_or_create(texto=texto_data, tipo=tipo_data)
            # Criar os objetos Labels e associá-los ao Textos
            for label_data in labels_data:
                # Verificar se a label já existe no banco de dados 
                label,_ = textos_labels_repository().get_or_create_label(label=label_data)
                # Associar a label ao texto
                textos_labels_repository().create_textos_labels(texto, label)
            
            return Response({'message': 'Textos atualizado com sucesso'}, status=status.HTTP_201_CREATED)
            
            
        # carregar o objeto TextosLabels
        textos_labels = textos_labels_repository().get_textos_labels_by_id(idtextoslabels)
        texto_tipo = textos_labels.textos
        texto_id = texto_tipo.id
        label = textos_labels.labels

        # Atualizar o texto e o tipo
        texto_tipo.texto = texto_data
        texto_tipo.tipo = tipo_data
        texto_tipo.save()

        # Deletar textos_labels com id
        textos_labels_repository().delete_textos_labels_by_id(texto_id)

        # Criar os objetos Labels e associá-los ao Textos
        for label_data in labels_data:
            # Verificar se a label já existe no banco de dados
            label, _ = textos_labels_repository().get_or_create_label(label=label_data)
            # Verificar se a label ja esta associada ao texto
            if not textos_labels_repository().get_textos_labels_by_texto_label(texto=texto_tipo, label=label).exists():
            # Associar a label ao texto
                #TextosLabels.objects.create(textos=texto_tipo, labels=label)
                textos_labels_repository().create_textos_labels(texto_tipo, label)
    
        return Response({'message': 'Textos atualizado com sucesso'}, status=status.HTTP_200_OK)