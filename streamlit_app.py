import streamlit as st
import plantcv.plantcv as pcv
import cv2
import numpy as np

# Don't know if this is necessary, but just in case
pcv.params.debug = None

st.title("Image Color Correction with PlantCV")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Add tabs
tab1, tab2 = st.tabs(["Original", "Color Corrected"])

# Read in array once a file has been uploaded
if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_BGR)
    
    # Do the color correction and show both in tabs
    cc = pcv.transform.auto_correct_color(image)

    tab1.image(image, use_column_width=True)
    tab2.image(cc, use_column_width=True)
