import datetime
from haystack import indexes
from medico.models import *


class MedicoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    def get_model(self):
        return Medico
