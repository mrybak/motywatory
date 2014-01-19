from haystack import indexes
from motywatory.models import Motivator


class MotivatorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    created_on = indexes.DateTimeField(model_attr='created_on')

    def get_model(self):
        return Motivator
