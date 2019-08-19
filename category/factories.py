import factory
from category import models


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Category %d' % n)
    description = factory.Sequence(lambda n: 'Description %d' % n)

    class Meta:
        model = models.Category
