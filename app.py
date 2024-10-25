import streamlit as st
from home.page import home
from genres.page import genres
from actors.page import actors
from movies.page import movies
from reviews.page import reviews
from login.page_login import show_login


def main():
    if 'token' not in st.session_state:
        show_login()
    else:    
        st.title('API FLIX')
        menu=st.sidebar.selectbox('Opções', ['Início', 'Filmes', 'Atores', 'Gêneros', 'Avaliações'])

        if menu=='Início':
            home()

        if menu=='Filmes':
            movies()

        if menu=='Atores':
            actors()

        if menu=='Gêneros':
            genres()

        if menu=='Avaliações':
            reviews()             

        
if __name__=='__main__':
    main()