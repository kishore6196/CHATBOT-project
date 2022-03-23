# import module
import streamlit as st

# Title
st.title("EDITH BOT")

# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("logo.png")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

x = st.text_input('Chatbot', '...')
st.write(x)




