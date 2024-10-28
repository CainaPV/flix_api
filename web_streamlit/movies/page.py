import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from movies.service import ServiceMovies
from datetime import datetime
from genres.service import ServiceGenres
from actors.service import ServiceActors


def movies():
    movie_service=ServiceMovies()
    movies=movie_service.get_movies()

    if movies:
        st.write('Lista de filmes...')

        movies_df=pd.json_normalize(movies)
        movies_df=movies_df.drop(columns=['actor', 'genre.id'])

        AgGrid(data=pd.DataFrame(movies_df), reload_data=True, key='movies_grid',)
     
    st.title('Cadastrar Novo Filme')

    title=st.text_input('Título')
    
    release_date=st.date_input(label='Data de Lançamento', value=datetime.today(), min_value=datetime(2000, 1, 1).date(), max_value=datetime.today())

    formatted_release_date=release_date.strftime('%d/%m/%Y')
    st.write(formatted_release_date)
    
    genre_service=ServiceGenres()
    genres=genre_service.get_genre()
    genre_names={genre['name']: genre['id'] for genre in genres}
    select_genre=st.selectbox('Gênero', list(genre_names.keys()))
    genre_id=genre_names[select_genre]    

    actor_service=ServiceActors()
    actors=actor_service.get_actors()
    actor_name={actor['name']: actor['id'] for actor in actors}
    selected_actors_names=st.multiselect('Atores', list(actor_name.keys()))
    selected_ids=[actor_name[name] for name in selected_actors_names]
  
    resume=st.text_area('Resumo')

    if st.button('Cadastrar'):
        if selected_ids:
            new_movie=movie_service.create_movies(title=title, release_date=formatted_release_date, genre=genre_id, actor=selected_ids, resume=resume)

        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao Cadastrar Filme!')
            