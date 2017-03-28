import datetime
from haystack import indexes
from models import *


class PacienteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    def get_model(self):
        return Paciente

class PreguntaRespuestaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    def get_model(self):
        return PreguntaRespuesta

class HistoriaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    fecha = indexes.DateTimeField(model_attr='fecha')

    def get_model(self):
        return Historia