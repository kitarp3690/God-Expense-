import streamlit as st
import signin as sn
import signup as su

st.set_page_config(
    page_title='Expense-Tracker',
    layout='wide'
)

if 'loggedin_user' not in st.session_state:
    st.session_state.loggedin_user=None  
    
def logout():
    st.session_state.loggedin=False 

def main():
    st.title('Expense-Tracker')
    tab1, tab2 = st.tabs(["Login","Sign-up"])
    with tab1:
        sn.signin()
    with tab2:
        su.signup()

if __name__=="__main__":
    main()