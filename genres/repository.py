import requests
import streamlit as st
from login.service import logout


class RepositoryGenres:

    def __init__(self):
        self.__url_genre='https://CainaPV.pythonanywhere.com/api/v1/genres/'
        self.__headers={'Authorization': f'Bearer {st.session_state.token} '}

    def get_genres(self):
        response=requests.get(url=self.__url_genre, headers=self.__headers,)
        if response.status_code==200:
            return response.json()
        if response.status_code==401:
            return logout()
        raise Exception(f'Error: {response.status_code}')
    
    def create_genres(self, name):
        response=requests.post(url=self.__url_genre, headers=self.__headers, data=name,)
        if response.status_code==201:
            return response.json()
        if response.status_code==401:
            return logout()
        raise Exception(f'Error: {response.status_code}')

        