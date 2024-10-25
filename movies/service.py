import streamlit as st
from movies.repository import RepositoryMovies


class ServiceMovies:

    def __init__(self):
        self.movies=RepositoryMovies()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies=self.movies.get_movies()
        st.session_state.movies=movies
        return movies
    
    def create_movies(self, title, release_date, genre, actor, resume):
        movie={'title': title, 'release_date': release_date, 'genre': genre, 'actor': actor, 'resume': resume}
        new_movies=self.movies.create_movies(movie)
        st.session_state.movies.append(new_movies)
        return new_movies
    
    def get_movies_statics(self):
        return self.movies.get_movies_statics()
       