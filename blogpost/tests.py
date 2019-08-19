from django.test import TestCase
from rest_framework import reverse, status

from blogpost.models import BlogPost
from blogpost.factories import BlogPostFactory
from category.factories import CategoryFactory
from user.factories import UserFactory


class BlogPostTestCase(TestCase):

    def setUp(self):
        blogpost = BlogPostFactory()
        self.user = UserFactory()
        self.category = CategoryFactory()
        BlogPostFactory(user=self.user, category=self.category)


    def test_blogpost_list(self):
        posts = BlogPost.objects.all().count()
        self.assertEqual(posts, 2)

    def test_blog_by_user(self):
        self.assertEqual(BlogPost.objects.filter(user=self.user).count(), 1)

        # TODO: test filters, categories and endpoints
    def test_blogpost_endpoint_by_user(self):
        response = self.client.get('/blogpost/blogposts/?user=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_blogpost_endpoint_by_nonexisting_user(self):
        response = self.client.get('/blogpost/blogposts/?user=3')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_blogpost_endpoint_by_filtering_category(self):
        # how to filter on category
        response = self.client.get('/blogpost/blogposts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        print(response.data)
        print(response.data.category)




