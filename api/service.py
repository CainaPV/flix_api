import requests


class Auth:

    def __init__(self):
        self.__auth_url='https://CainaPV.pythonanywhere.com/api/v1/authentication/token/'

    def get_token(self, username, password):
        auth_user={'username': username, 'password': password}
        auth_response=requests.post(url=self.__auth_url, data=dict(auth_user))

        if auth_response.status_code==200:
            return auth_response.json()
        return {'error': f'verificar status - {auth_response.status_code}'}