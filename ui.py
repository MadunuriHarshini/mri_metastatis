import streamlit as st
import requests
from PIL import Image

st.title("Brain MRI Metastasis Segmentation")

uploaded_file = st.file_uploader("Upload an MRI image", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)
    
    if st.button("Segment Image"):
        response = requests.post("http://127.0.0.1:8000/segment", files={"file": uploaded_file.getvalue()})
        if response.status_code == 200:
            segmentation_result = response.json()["segmentation_result"]
            # Display segmentation result (convert to image, overlay, etc.)
            st.image(segmentation_result, caption="Segmentation Result")
