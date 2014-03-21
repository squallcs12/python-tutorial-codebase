import factory
from polls import models

class QuestionFactory(factory.Factory):
    FACTORY_FOR = models.Question

    text = factory.Sequence(lambda n: 'Poll {0}'.format(n))
