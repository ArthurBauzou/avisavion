import streamlit as st

### FONCTIONS ###
def send_filter():

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

    testarea.write('envoyé')
    print(p_filter)
    # return p_filter


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
    st.button('FILTER', on_click=send_filter)

with col2:
    st.header('stats')
    testarea = st.empty()