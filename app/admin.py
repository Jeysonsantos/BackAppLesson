from django.contrib import admin

# Register your models here.

from .models import Dados, labels, DadosLabels, Textos, TextosLabels

admin.site.register(Dados)
admin.site.register(labels)
admin.site.register(DadosLabels)
admin.site.register(Textos)
admin.site.register(TextosLabels)

