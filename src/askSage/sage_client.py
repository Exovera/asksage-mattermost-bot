import logging
from os import environ

import redis
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class SageAPI:
    def __init__(self, email, password, get_token_url, query_url, train_url):
        self.email = email
        self.password = password
        self.get_token_url = get_token_url
        self.query_url = query_url
        self.train_url = train_url
        self.token = None
        self.redis_client = redis.Redis.from_url(url=environ.get('REDIS_URL', 'redis://localhost:6379/0'))
        self.token_key = "sage_api_token"
        self.token_expiration = int(environ.get('TOKEN_EXPIRATION', 60 * 60))  # Defaults to 1 hour

    def sage_request(self, data):
        if not self.token:
            self.check_token()

        headers = {
            "Content-Type": "application/json",
            "x-access-tokens": self.token
        }

        for _ in range(3):
            response = requests.post(self.query_url, headers=headers, json=data)
            if response.status_code == 400:
                if response.json().get('response') == 'Token is invalid [1]':
                    self.check_token()
                    continue
            if response.ok:
                return response
        raise Exception("Error communicating with Sage, too many failures.")

    def check_token(self):
        token = self.redis_client.get(self.token_key)
        if token:
            self.token = token.decode('utf-8')
        else:
            self.request_new_token()

    def request_new_token(self):
        creds = {'email': self.email, 'password': self.password}
        response = requests.post(self.get_token_url,
                                 headers={'Content-Type': 'application/json'},
                                 json=creds)

        if not response.status_code <= 299:
            raise Exception("Error communicating with Sage")

        self.token = response.json().get('response', {}).get('access_token')
        self.redis_client.setex(self.token_key, self.token_expiration, self.token)

    def query_sage(self, message, model=None, temperature=None):
        model = model if model else environ.get('MODEL', 'openai_gpt')  # Defaults to 'openai_gpt'
        temperature = float(temperature) if temperature else float(environ.get('TEMPERATURE', 0.0))  # Defaults to 0.0

        data = {
            "message": message,
            "model": model,
            "temperature": temperature,
        }

        response = self.sage_request(data)
        if response.ok:
            return response.json()
        else:
            raise Exception("Query failed")
