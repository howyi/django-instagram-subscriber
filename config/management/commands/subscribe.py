from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        client_id = input('client_id:')
        client_secret = input('client_secret:')
        callback_url = input('callback_url(self URL):')

        url = "https://api.instagram.com/v1/subscriptions/"

        payload = {
            'client_id' : client_id,
            'client_secret' : client_secret,
            'object' : 'user',
            'aspect' : 'media',
            'verify_token' : '9mdWcibK4Wb4DtsZyt',
            'callback_url' : callback_url
        }

        response = requests.post(url, data=payload)

        print(response.text)
