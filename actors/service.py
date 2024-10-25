import streamlit as st
from actors.repository import RepositoryActors


class ServiceActors:
    
    def __init__(self):
        self.actors=RepositoryActors()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors=self.actors.get_actors()
        st.session_state.actors=actors
        return actors
    
    def create_actors(self, name, age, nationality):
        data = {'name': name, 'age': age, 'nationality': nationality}
        new_actors=self.actors.create_actors(data)
        st.session_state.actors.append(new_actors)
        return new_actors
            