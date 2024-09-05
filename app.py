import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title='DevInvestor',
    layout='wide'
)

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized'],
    auto_hash= False
)

st.title('Dev Investor')
st.write("O melhor amigo do dinheiro do programador!")

authenticator.login()

if st.session_state['authentication_status']:
    st.sidebar.header(f'Olá *{st.session_state["name"]}*')
    authenticator.logout(location='sidebar')
elif st.session_state['authentication_status'] is False:
    st.error('Usuário/senha incorretos.')
elif st.session_state['authentication_status'] is None:
    st.warning('Insira seu usuário e senha.')

