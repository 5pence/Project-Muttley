import factory

from blogpost.factories import BlogPostFactory
from comments import models
from user.factories import UserFactory


class CommentsFactory(factory.django.DjangoModelFactory):
    comment = factory.Sequence(lambda n: 'Comment %d' % n)
    user = factory.SubFactory(UserFactory)
    blogpost = factory.SubFactory(BlogPostFactory)

    class Meta:
        model = models.Comment
