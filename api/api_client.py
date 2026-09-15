import requests

from api.endpoints import LOGIN_ENDPOINT


class APIClient:

    def __init__(self):
        self.access_token = None

    def login(self, username, password):

        login_data = {
            "username": username,
            "password": password
        }

        response = requests.post(
            LOGIN_ENDPOINT,
            json=login_data
        )

        if response.status_code == 200:
            self.access_token = response.json()["accessToken"]
        else:
            self.access_token = None

        return response

    def get_auth_headers(self):

        return {
            "Authorization": f"Bearer {self.access_token}"
        }

    def get(self, url, headers=None):

        if headers is None and self.access_token:
            headers = self.get_auth_headers()

        return requests.get(
            url,
            headers=headers
        )

    def post(self, url, data=None, headers=None):

        if headers is None and self.access_token:
            headers = self.get_auth_headers()

        return requests.post(
            url,
            json=data,
            headers=headers
        )

    def put(self, url, data=None, headers=None):

        if headers is None and self.access_token:
            headers = self.get_auth_headers()

        return requests.put(
            url,
            json=data,
            headers=headers
        )

    def delete(self, url, headers=None):

        if headers is None and self.access_token:
            headers = self.get_auth_headers()

        return requests.delete(
            url,
            headers=headers
        )