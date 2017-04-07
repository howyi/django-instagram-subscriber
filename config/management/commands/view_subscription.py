from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        client_id = input('client_id:')
        client_secret = input('client_secret:')

        url = "https://api.instagram.com/v1/subscriptions/"

        payload = {
            'client_id' : client_id,
            'client_secret' : client_secret
        }

        response = requests.get(url, params=payload)

        print(response.text)
