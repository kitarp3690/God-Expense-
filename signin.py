import streamlit as st
import connection as db
import time

def signin():
    with st.form(key='Signin', clear_on_submit=True, border=True):
        username:str=st.text_input('Username:', label_visibility='collapsed',placeholder='Username')
        password:str=st.text_input('Passsword:', label_visibility='hidden', type='password',placeholder='Password')
        if st.form_submit_button('Login'):
            placeholder=st.empty()
            if db.check_user_existence(username):
                if db.check_pw(username,password):
                    placeholder.success('Logged In Successfully')
                    st.session_state.loggedin_user=username
                    st.session_state.loggedin=True
                else:
                    placeholder.error('Invalid Password')
            else:
                placeholder.error('User Not Found')
            time.sleep(3)
            placeholder.empty() 