from app.repositories.dados_repository import dados_repository
from app.services.similaridade_cosseno import similaridade_cosseno

class entrada_texto_service:

    def processar_entrada(self,tipo, entrada):

        repository = dados_repository()
        similaridade = similaridade_cosseno()

        if tipo == 'lesson':

            dados = repository.find_all_lesson()
                        
        elif tipo == 'incident':
            
            dados = repository.find_all_incident()

        elif tipo == 'observation':
            
            dados = repository.find_all_observation()

        dados = [item.to_dict() for item in dados]

        resultado = similaridade.similaridade_entrada(entrada, dados)
        
        return resultado