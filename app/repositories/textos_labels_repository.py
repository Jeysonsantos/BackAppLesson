from app.models import Textos, labels, TextosLabels

class textos_labels_repository:

    def get_or_create(self, texto, tipo):
        return Textos.objects.get_or_create(texto=texto, tipo=tipo)
    
    def get_or_create_label(self, label):
        return labels.objects.get_or_create(label=label)

    def create_textos_labels(self, texto, label):
        return TextosLabels.objects.create(textos=texto, labels=label)

    def get_textos_labels_by_id(self, id):
        return TextosLabels.objects.get(id=id)
    
    def delete_textos_labels_by_id(self, id):
        return TextosLabels.objects.filter(textos_id=id).delete()
    
    def get_textos_labels_by_texto_label(self, texto, label):
        return TextosLabels.objects.filter(textos=texto, labels=label)

    def create_textos_labels(self, texto, label):
        return TextosLabels.objects.create(textos=texto, labels=label)
    
    def get_all_labels(self):
        return labels.objects.all()

    def get_all_textos_labels(self):
        return TextosLabels.objects.all()
    
    def exclude_textos_labels(self):
        return Textos.objects.exclude(textoslabels__isnull=False)
