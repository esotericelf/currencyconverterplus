from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from oauth2_provider.models import Application, AccessToken
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class EnquiryCreateViewTests(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create an OAuth2 application
        self.application = Application.objects.create(
            name="Test Application",
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            user=self.user
        )

        # Create an access token
        self.token = AccessToken.objects.create(
            user=self.user,
            token='testtoken123',
            application=self.application,
            expires=timezone.now() + timedelta(days=1),
            scope='read write'
        )

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.token)

    def test_create_enquiry_authenticated(self):
        url = reverse('enquiry-create')  # Ensure this matches your URL pattern name
        data = {
            'user': self.user.id,  # Assuming you have a user created in setUp
            'buying_currency': 'USD',  # Replace with valid currency code
            'selling_currency': 'EUR',  # Replace with valid currency code
            'amount': 100.0,  # Replace with a valid amount
            'exchange_rate': 1.2  # Replace with a valid exchange rate
        }
        response = self.client.post(url, data, format='json')
        print(response.data)  # Keep this line to see the response data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_enquiry_unauthenticated(self):
        self.client.credentials()  # Remove authentication
        url = reverse('enquiry-create')
        data = {'field1': 'value1', 'field2': 'value2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
