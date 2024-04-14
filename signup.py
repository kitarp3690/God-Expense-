import streamlit as st
import connection as db
import time

def signup():
    with st.form(key="Signup Form", clear_on_submit=True, border=True):
        full_name=st.text_input('Full Name*', label_visibility='visible',placeholder='Full Name')
        username=st.text_input('UserName*', label_visibility='visible',placeholder='Username',key='s_up_u')
        password=st.text_input('Passsword*', type='password',label_visibility='visible',placeholder='Password',key='s_up_p')
        if st.form_submit_button('Sign Up'):
            placeholder=st.empty()
            if full_name.strip() and username.strip() and password.strip():
                hash_pw=db.hash_password(password)
                st.write(username,password,full_name,hash_pw)
                db.store_username_password(username, hash_pw, full_name)
                placeholder.success("User signup successful")
            else:
                placeholder.error('All field required')