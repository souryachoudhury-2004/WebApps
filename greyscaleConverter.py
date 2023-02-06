import streamlit as st
from PIL import Image

def process():
    if camera_img:
        img = Image.open(camera_img)
        grey_img = img.convert("L")
        st.image(grey_img)

st.title("Greyscale Image Converter.")

with st.expander("Start Camera."):
    camera_img = st.camera_input("Camera.")
    process()

with st.expander("Upload image."):
    camera_img = st.file_uploader("Upload image from device.")
    process()

