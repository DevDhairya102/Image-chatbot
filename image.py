from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = genai_api_key)

#function to load openai model 
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title = "Image chatbot")
st.header("Image text generator")
input = st.text_input("Input prompt: ",key = "input")

uploaded_image = st.file_uploader("Choose an image:.... ",type=["jpg","jpeg","png"])
image  = ""
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image,caption= "Iploaded image..", use_container_width = True)


submit = st.button("Tell me about image")
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The response is...")
    st.write(response)