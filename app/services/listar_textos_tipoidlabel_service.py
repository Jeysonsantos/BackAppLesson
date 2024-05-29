from app.models import TextosLabels, Textos

class listar_textos_tipoidlabel_service:
    def listar_textos_tipo_idlabel(self):
        Lista = []

        #amostragem aletoria de textos
        textos_labels_list = TextosLabels.objects.filter().order_by('?')[:300]
        textos_sem_labels = Textos.objects.exclude(textoslabels__isnull=False).order_by('?')[:300]

        for texto in textos_sem_labels:
            texto1 = texto.texto
            tipo = texto.tipo
            label = ''
            id_textoLabel = ''
            #adicionar a lista caso nao exista
            if not any(d['texto'] == texto1 for d in Lista):
                Lista.append({
                    'texto': texto1,
                    'tipo': tipo,
                    'label': {},
                    'id_textoLabel': id_textoLabel})
 
        for texto in textos_labels_list:
            texto1 = texto.textos.texto
            tipo = texto.textos.tipo
            label = texto.labels
            id_textoLabel = texto.id
            if not any(d['texto'] == texto1 for d in Lista):
                Lista.append({
                    'texto': texto1,
                    'tipo': tipo,
                    'label': [{
                        'id': label.id,
                        'label': label.label
                    }],
                    'id_textoLabel': id_textoLabel})
            else:
                for d in Lista:
                    if d['texto'] == texto1:
                        d['label'].append({
                            'id': label.id,
                            'label': label.label
                        })

        return Lista