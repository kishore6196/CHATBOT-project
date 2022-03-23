import streamlit as st
from streamlit_chat import message

k =1
while(True):
    x = st.text_input('Your message',key=k)
    message("Bot's response",key=k) 
    message(x, is_user=True,key=k+1)
    
    k=k+3
    if x == 'bye':
        break