from django.test import TestCase


class HomePageTests(TestCase):

    """Test whether the Coffee Club application homepage"""
    def setUp(self):
        return

    def test_homepage(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'This is My Home Page')
        self.assertContains(response, 'This is my footer')
