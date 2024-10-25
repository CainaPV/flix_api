import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from actors.service import ServiceActors


nacionalidade = ['USA', 'BR', 'CN', 'ING']


def actors():

    st.text('Atores Cadastrados...')
    actor_serive=ServiceActors()
    actor = actor_serive.get_actors()
    actor_df=pd.json_normalize(actor)
    
    AgGrid(data=pd.DataFrame(actor_df), reload_data=True, key='actors_grid')

    name=st.text_input('Cadastre um Ator(a):')
    age=st.number_input('Informe a idade do Ator', min_value=0, max_value=120, value=25)
    nati_dropdown=st.selectbox(label='Nacionalidade', options=nacionalidade)
   
    if st.button('Cadastrar'):
        new_actor=actor_serive.create_actors(name=name, age=age, nationality=nati_dropdown)
        if new_actor: 
            st.rerun()    
        else:
            st.error('Erro ao cadastrar ator')
               
        
