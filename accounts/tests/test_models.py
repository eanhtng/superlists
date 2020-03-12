from django.test import TestCase
from django.contrib import auth
from accounts.models import Token


User = auth.get_user_model()

TEST_EMAIL_ADDRESS = 'a@b.com'

class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        user = User(email=TEST_EMAIL_ADDRESS)
        user.full_clean()

    def test_email_is_primary_key(self):
        user = User(email=TEST_EMAIL_ADDRESS)
        self.assertEqual(user.pk, TEST_EMAIL_ADDRESS)

    def test_no_problem_with_auth_login(self):
        user = User.objects.create(email='edith@example.com')
        user.backend = ''
        request = self.client.request().wsgi_request
        auth.login(request, user)

class TokenModelTest(TestCase):

    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email = TEST_EMAIL_ADDRESS)
        token2 = Token.objects.create(email = TEST_EMAIL_ADDRESS)
        # Same email address, different created tokens
        self.assertNotEqual(token1.uid, token2.uid)
