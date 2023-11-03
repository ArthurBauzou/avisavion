import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

from modules.prepdata import prepdata
from modules.modelmk import train_model




### FONCTIONS ###
def launch():

    df = pd.read_csv('data\clean_aiplane.csv')
    p_filter, f_filter, delay = send_filter()
    df = prepdata(p_filter, f_filter, df, take_delay_in=delay)
    st.session_state.columns = df.drop('satisfaction', axis=1).columns
    st.session_state.sample_size = df.shape[0]
    model, score = train_model(df)
    st.session_state.score = score
    st.session_state.model = model


def send_filter():

    # PASSENGERS
    p_dict = {
        'Femme': 'female',
        'Homme': 'male',
        'Fidèle': 'loyal customer',
        'Volage': 'disloyal customer',
        'plus que': '+',
        'moins que': '-'
    }
    p_filter = {}
    if gender != 'Tous': p_filter['gender'] = p_dict[gender]
    if age_dir != 'Tous': p_filter['age'] = (age, p_dict[age_dir])
    if customer_type != 'Tous': p_filter['type'] = p_dict[customer_type]

    # FLIGHT
    f_filter = {}

    # DELAY
    if delays : take_delays = True
    else: take_delays = False

    print(p_filter, f_filter, take_delays)
    return p_filter, f_filter, take_delays


### ST.SESSION ###
if 'score' not in st.session_state : st.session_state.score = 0
if 'sample_size' not in st.session_state : st.session_state.sample_size = 0
if 'model' not in st.session_state : st.session_state.model = None
if 'columns' not in st.session_state : st.session_state.columns = []

### CONFIG ###
st.set_page_config(
        page_title="avisavion",
        layout='wide'
    )


### PAGE ###
st.title('avisavion')

col1, col2 = st.columns([2,5])

with col1:
    st.header('passager')
    gender = st.selectbox('genre', ['Homme', 'Femme', 'Tous'])
    c1, c2 = st.columns(2)
    with c1 : 
        age_dir = st.selectbox('age', ['plus que', 'moins que', 'Tous'])
    with c2 :
        if age_dir == 'Tous': 
            age = st.number_input('agen', disabled=True, label_visibility='hidden')
        else: 
            age = st.number_input('agen', min_value=10, max_value=70, label_visibility='hidden')

    customer_type = st.selectbox('type de client', ['Fidèle', 'Volage', 'Tous'])

    st.divider()
    delays = st.checkbox('Prendre en compte les retards', value=True)

    st.divider()
    st.button('FILTER', on_click=launch)

with col2:
    st.header('stats')
    st.write(f'Taille echantillon: {st.session_state.sample_size} – Score du modèle : {st.session_state.score}')
    if st.session_state.model != None :
        influ = st.session_state.model.feature_importances_
        fig = plt.figure(figsize=(10, 10))
        plt.barh(st.session_state.columns, influ)
        plt.xlabel("Importance")
        plt.ylabel("Features")
        st.write(fig)