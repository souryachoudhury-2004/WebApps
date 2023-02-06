import streamlit as st
from PIL import Image

#starts camera
camera_image = st.camera_input("Camera")

#executes later lines only if camera has been opened
if camera_image:
    #opens image
    img = Image.open(camera_image)
    #converts image to greyscale
    grey_img = img.convert("L")
    #Displays image
    st.image(grey_img)