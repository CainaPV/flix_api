import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from reviews.service import ServiceReviews
from movies.service import ServiceMovies


def reviews():
    st. text("Avaliações Cadastradas...")
    review_service=ServiceReviews()
    reviews=review_service.get_reviews()
    reviews_df=pd.json_normalize(reviews)

    AgGrid(data=pd.DataFrame(reviews_df), reload_data=True, key='movie_grid')

    st.text('Filmes Cadastrados')
    service_movie=ServiceMovies()
    movies=service_movie.get_movies()
    movie_names={movie['title']: movie['id'] for movie in movies}
    select_movies=st.selectbox('Filmes', list(movie_names.keys()))
    movie_id=movie_names[select_movies]
    st.write(movie_id)
    
    stars=st.number_input(label='Avalie o Filme', min_value=0, max_value=5, step=1)
    st.write(stars)

    comment=st.text_area('Comentário')
    
    if st.button('Cadastrar'):
        new_reviews=review_service.create_reviews(movie=movie_id, stars=stars, comment=comment)
        if new_reviews:
            st.rerun()
        else:
            st.error('Error ao cadastrar avaliação')