import os
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

imgsize = 224
classnames = ["Healthy", "Tomato Mosaic Virus"]

st.set_page_config(page_title="Tomato Leaf Disease Detection")

root = os.path.dirname(os.path.abspath(__file__))
@st.cache_resource
def loadmodels():
    model_path = os.path.join(root, "tomato_model.keras")
    diseasemodel = tf.keras.models.load_model("tomato_model.keras")
    anomalymodel = tf.keras.models.load_model("tomatoAnomalyDetector.keras")
    with open("tomatoAnomalyThreshold.txt", "r") as f:
        threshold = float(f.read())
    return diseasemodel, anomalymodel, threshold


diseasemodel, anomalymodel, threshold = loadmodels()

st.title("Tomato Leaf Disease Detection")
st.write("Upload a photo of a tomato leaf to check for Tomato Mosaic Virus.")

uploadedfile = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploadedfile is not None:
    image = Image.open(uploadedfile).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    resized = image.resize((imgsize, imgsize))
    arr = np.array(resized, dtype="float32") / 255.0
    arr = np.expand_dims(arr, axis=0)

    reconstructed = anomalymodel.predict(arr)
    reconerror = np.mean(np.square(arr - reconstructed))

    if reconerror > threshold:
        st.error(
            f"This doesn't look like a tomato leaf. Please upload a photo of a tomato leaf"
        )
    else:
        prediction = diseasemodel.predict(arr)[0][0]

        if 0.4 <= prediction <= 0.6:
            st.warning(f"Uncertain prediction (confidence: {prediction:.2f}). Try a clearer image")
        else:
            label = classnames[1] if prediction > 0.5 else classnames[0]
            confidence = prediction if prediction > 0.5 else 1 - prediction
            st.success(f"Prediction: **{label}** (confidence: {confidence:.2%})")
