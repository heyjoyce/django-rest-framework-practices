from rest_framework.test import APITestCase
from rest_framework import status


class ArticleTests(APITestCase):
    def test_create_article(self):
        body = {'title': 'Hello', 'author': 'guest'}
        response = self.client.post('/api/v1/articles', body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
