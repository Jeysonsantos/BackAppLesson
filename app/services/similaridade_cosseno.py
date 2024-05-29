from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class similaridade_cosseno:
    
    def similaridade_entrada(self,entrada, dados):
        tfidf_vectorizer = TfidfVectorizer()

        #Transforma a entrada e os dados em vetores de palavras
        matriz_tfidf = tfidf_vectorizer.fit_transform([item.get("descricao") for item in dados])
        entrada_tfidf = tfidf_vectorizer.transform([entrada])

        #Calcula a similaridade entre a entrada e os dados
        similaridades = cosine_similarity(entrada_tfidf, matriz_tfidf).flatten()

        #Retorna o dado mais similar
        indice_melhor_correspondencia = similaridades.argsort()[-1]

        return [dados[indice_melhor_correspondencia]]