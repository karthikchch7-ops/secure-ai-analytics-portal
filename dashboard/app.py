import streamlit as st
import requests
import os

BACKEND = os.environ.get('BACKEND_URL','http://localhost:8000')

st.title('Secure AI Analytics Portal - Dashboard (Demo)')

st.markdown('Use this dashboard to demo upload, training, and prediction endpoints.')

if 'token' not in st.session_state:
    st.session_state['token']=''

with st.expander('Login'):
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        resp = requests.post(f"{BACKEND}/auth/token", data={'username': email, 'password': password})
        if resp.status_code==200:
            st.session_state['token']=resp.json()['access_token']
            st.success('Logged in')
        else:
            st.error('Login failed: '+resp.text)

if st.session_state['token']:
    headers = {'Authorization': f"Bearer {st.session_state['token']}"}
    st.subheader('Demo: Predict (echo)')
    sample_input = st.text_area('JSON input', value='{"age": 40, "feature": 1}')
    if st.button('Predict'):
        try:
            j = requests.post(f"{BACKEND}/predict", json={'data': sample_input}, headers=headers)
            st.write(j.json())
        except Exception as e:
            st.error(str(e))

    st.subheader('Start Training')
    if st.button('Start training'):
        r = requests.post(f"{BACKEND}/train", headers=headers)
        st.write(r.json())

else:
    st.info('Please login to access training and prediction endpoints')
