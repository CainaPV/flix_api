import requests
import streamlit as st
from login.service import logout


class RepositoryMovies:
    
    def __init__(self):
        self.__url='https://CainaPV.pythonanywhere.com/api/v1/movies/'
        self.__headres={'Authorization': f'Bearer {st.session_state.token}'}

    def get_movies(self):
        response=requests.get(url=self.__url, headers=self.__headres)
        if response.status_code==200:
            return response.json()
        if response==401:
            return logout()
        raise Exception(f'Error: {response.status_code}')
    
    def create_movies(self, movie):
        response = requests.post(url=self.__url, headers=self.__headres, data=movie)
        if response.status_code==201:
            return response.json()
        if response.status_code==401:
            return logout()
            
        raise Exception(f'Error: {response.status_code} - {response.text}')
    
    def get_movies_statics(self):
        response=requests.get(f'{self.__url}/statics', headers=self.__headres)
        if response.status_code==200:
            return response.json()
        if response.status_code==401:
            return logout()
        raise Exception(f'Error: {response.status_code} - {response.text}')
        