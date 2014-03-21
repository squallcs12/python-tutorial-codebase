import factory
from polls import models

class ChoiceFactory(factory.Factory):
    FACTORY_FOR = models.Choice

    text = factory.Sequence(lambda n: 'Choice {0}'.format(n))
