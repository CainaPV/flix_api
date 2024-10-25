import requests
import streamlit as st
from login.service import logout


class RepositoryActors:

    def __init__(self):

        self.__url_actor='https://CainaPV.pythonanywhere.com/api/v1/actors/'
        self.__headres={'Authorization': f'Bearer {st.session_state.token}'}
    
    def get_actors(self):

        response=requests.get(url=self.__url_actor, headers=self.__headres,)
        if response.status_code==200:
            return response.json()
        if response.status_code==401:
            return logout()
        raise Exception(f'Erro - Verificação {response.status_code}')
    
    def create_actors(self, actor):

        response=requests.post(url=self.__url_actor, headers=self.__headres, data=actor)
        if response.status_code==201:
            return response.json()
        if response.status_code==401:
            return logout()
        raise Exception(f'Erro - Verificação {response.status_code}')
