from app.models import Dados

class dados_repository:

    def find_all(self):
        return Dados.objects.all()

    def find_by_id(self, id):
        return Dados.objects.get(id=id).first()
        
    def find_all_lesson(self):
        return Dados.objects.filter(tipo_descricao='Licao')
    
    def find_all_incident(self):
        return Dados.objects.filter(tipo_descricao='Incidente')
    
    def find_all_observation(self):
        return Dados.objects.filter(tipo_descricao='Obs')
    
    def find_by_description_type_lesson(self, description):
        return Dados.objects.filter(tipo_descricao='Licoes', descricao=description)
    
    def find_by_description_type_incident(self, description):
        return Dados.objects.filter(tipo_descricao='Incidentes', descricao=description)