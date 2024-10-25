import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import ServiceGenres


def genres():
  genre_service=ServiceGenres()
  genre=genre_service.get_genre()
  st.write(genre)
  genre_df=pd.json_normalize(genre)

  st.title('Gêneros Cadastrados...')
  AgGrid(data=pd.DataFrame(genre_df), reload_data=True, key='genres_grid')

  name=st.text_input("Cadastre algum Gênero:")
  if st.button('Cadastrar'):
    create=genre_service.create_genre(name=name)
    st.success('Gênero Cadastrado com sucesso')
    st.rerun()
 