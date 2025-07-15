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
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    # flip channels
    image_flipped = cv2.merge((image[:, :, [2]],
                       image[:, :, [1]],
                       image[:, :, [0]]))
    
    # Do the color correction and show both in tabs
    cc = pcv.transform.auto_correct_color(image_flipped)
    cc_flipped = cv2.merge((cc[:, :, [2]],
                       cc[:, :, [1]],
                       cc[:, :, [0]]))

    tab1.image(image_flipped, use_column_width=True)
    tab2.image(cc_flipped, use_column_width=True)
