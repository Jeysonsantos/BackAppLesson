from django.db import models

class Dados(models.Model):
    descricao = models.TextField()
    elementos_list = models.JSONField()
    tipo_elementos = models.CharField(max_length=100)
    tipo_descricao = models.CharField(max_length=100)
    
    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'elementos_list': self.elementos_list,
            'tipo_elementos': self.tipo_elementos,
            'tipo_descricao': self.tipo_descricao,
        }
    
class labels(models.Model):
    label = models.CharField(max_length=100)
    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label,
        }

class DadosLabels(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE)
    labels = models.ForeignKey(labels, on_delete=models.CASCADE)
    def to_dict(self):
        return {
            'id': self.id,
            'dados': self.dados.to_dict(),
            'labels': self.labels.to_dict(),
        }
    
class Textos(models.Model):
    texto = models.TextField()
    TIPOS_CHOICES = [
        ('lesson', 'Lesson'),
        ('observation', 'Observation'),
        ('incident', 'Incident'),
    ]
    tipo = models.CharField(max_length=100, choices=TIPOS_CHOICES)

    def to_dict(self):
        return {
            'id': self.id,
            'texto': self.texto,
            'tipo': self.tipo,
        }

class TextosLabels(models.Model):
    textos = models.ForeignKey(Textos, on_delete=models.CASCADE)
    labels = models.ForeignKey(labels, on_delete=models.CASCADE)
    def to_dict(self):
        return {
            'id': self.id,
            'textos': self.textos.to_dict(),
            'labels': self.labels.to_dict(),
        }
