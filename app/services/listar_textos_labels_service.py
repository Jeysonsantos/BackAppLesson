
from app.repositories.textos_labels_repository import textos_labels_repository


class listar_textos_labels_service:
    def listar_textos_labels(self):
        textos_labels_list = textos_labels_repository().get_all_textos_labels()
        textos_labels_list_json = [textos_labels.to_dict() for textos_labels in textos_labels_list]

        # Enviar tambem textos sem labels
        textos_sem_labels = textos_labels_repository().exclude_textos_labels()
        textos_sem_labels_json = [textos.to_dict() for textos in textos_sem_labels]

        for texto in textos_sem_labels_json:
            dict = {}
            dict['id'] = texto['id']
            dict['texto'] = texto['texto']
            dict['tipo'] = texto['tipo']
            texto['textos'] = dict
            dict_labels = {}
            texto['labels'] = dict_labels
            texto['id']=None
            #deletar campo texto e tipo
            del texto['texto']
            del texto['tipo']


        textos_labels_list_json.extend(textos_sem_labels_json)

        return textos_labels_list_json