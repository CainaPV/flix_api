import streamlit as st
from api.service import Auth


def login(username, password):
    auth=Auth()
    response=auth.get_token(username=username, password=password)
    if response.get('error'):
        st.error(f'Erro de Autorização {response.get('error')}')
    else:
        st.session_state.token=response.get('access')
        st.rerun()


def logout():
    for k in st.session_state.keys():
        del st.session_state[k]
    st.rerun()