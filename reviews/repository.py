import streamlit as st
import requests
from login.service import logout


class RepositoryReviews:

    def __init__(self):
        self.__url_reviews='https://CainaPV.pythonanywhere.com/api/v1/reviews/'
        self.__headers={'Authorization': f'Bearer {st.session_state.token}'}

    def get_reviews(self):
        response=requests.get(url=self.__url_reviews, headers=self.__headers)
        if response.status_code==200:
            return response.json()
        
        if response.status_code==401:
            return logout()
        
        raise Exception(f'Error: {response.status_code} - {response.text} ')
    
    def create_reviews(self, review):
        response=requests.post(url=self.__url_reviews, headers=self.__headers, data=review)
        if response.status_code==201:
            return response.json()
        
        if response.status_code==401:
            return logout()
        
        raise Exception(f'Error: {response.status_code} - {response.text}')


        
