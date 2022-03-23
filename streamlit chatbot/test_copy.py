import streamlit as st 
from nltk.chat.util import Chat, reflections
from pyjokes import get_joke


x = [
    
         ['my name is (.*)', ['Hi! Hello %1 Sir. I am EDITH. How may i Help You?']],
         ['hi', ['Hi Hello I am your EDITH. How can I Help you?????']],
         ['What can you Do', ['Yes Sir, I can Do many Tasks.']],
        
         ['do you think there is a creator', ['Yes, According to me there is creator of all this because even I have been created by kishore']],
         ['about you', ['I am a ChatBot created by kishore']],
         ['Who am i', ['please try typing "my name is --"']],
         
         ['tell me joke', [get_joke(language='en', category='neutral') ]],
         ['Who created you?', ['kishore has created me.']],
            
]


st.title("chatbot")
st.subheader("this is joke chatbot")


def main():
    st.write("start your chat by saying HI")
    ref = st.text_input("chat here")


    chat = Chat(x, reflections)
    respo = chat.respond(ref)
    st.write(respo)

if __name__=="__main__":
    main()