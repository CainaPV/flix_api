from movies.service import ServiceMovies
import streamlit as st
import pandas as pd
import plotly.express as px


def home():
    movies_service=ServiceMovies()
    movies_stats=movies_service.get_movies_statics()

    if 'list_genres_in_movies' in movies_stats and len(movies_stats['list_genres_in_movies']) > 0:
        # Convertendo para DataFrame
        df_genres=pd.DataFrame(movies_stats['list_genres_in_movies'])

        # # Agrupando e contando os filmes por gênero
        genre_counts=df_genres.groupby('genre__name').size().reset_index(name='genre_by_movies')

        st.subheader('Filmes por Gênero')
        fig=px.pie(genre_counts, values='genre_by_movies', names='genre__name', title='Filmes por Gênero')
        st.plotly_chart(fig)
    else:
        st.warning("Não há dados de gêneros disponíveis.")

    st.subheader('Total de Filmes')
    st.write(movies_stats.get('total_movies', 'Dado não disponível'))

    st.subheader('Total de Reviews')
    st.write(movies_stats.get('total_reviews', 'Dado não disponível'))

    st.subheader('Gênero em Movies')
    st.write(movies_stats.get('list_genres_in_movies', 'Dado não disponível'))

    st.subheader('Total de Média de Estrelas')
    st.write(movies_stats.get('total_rate_stars', 'Dado não disponível'))