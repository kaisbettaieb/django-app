from django.test import RequestFactory, TestCase, Client
from app.views import MajDetails, AccueilView
from django.contrib.auth.models import User


class MajDetailsTest(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='test')

    def test_accueil(self):
        request = self.request_factory.get("/")
        response = AccueilView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_post_logged_in(self):
        client = Client()
        client.login(username='test', password='test')
        response = client.post("/update/email", data={"email": "nouveau_test@gmail.com"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, "nouveau_test@gmail.com")

    def test_post_not_logged(self):
        client = Client()
        client.login(username='tst', password='test')
        response = client.post("/update/email", data={"email": "nouveau_test@gmail.com"}, follow=True)
        self.assertEqual(response.status_code, 401)

    def test_no_email(self):
        client = Client()
        client.login(username='test', password='test')
        response = client.post("/update/email", follow=True)
        self.assertEqual(response.status_code, 500)
