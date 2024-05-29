from app.models import labels
from app.repositories.textos_labels_repository import textos_labels_repository

class listar_labels_service:
    def listar_labels(self):
        labels_list = textos_labels_repository().get_all_labels()
        labels_list_json = [label.to_dict() for label in labels_list]
        return labels_list_json