import factory
from category.factories import CategoryFactory
from user.factories import UserFactory
from blogpost import models


class BlogPostFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'Blog Post%d' % n)
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = models.BlogPost
