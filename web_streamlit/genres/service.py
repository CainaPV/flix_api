import streamlit as st
from genres.repository import RepositoryGenres


class ServiceGenres:
    def __init__(self):
        self.genres = RepositoryGenres()
        
    def get_genre(self):
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.genres.get_genres()
        st.session_state.genres = genres
        return genres
    
    def create_genre(self, name):
        genre = {'name': name}
        new_genres = self.genres.create_genres(genre)
        st.session_state.genres.append(new_genres)
        return new_genres
    