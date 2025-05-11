import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load model
model = load_model("waste_classifier_model.h5")  # Use your path
class_names = ['compost', 'landfill', 'recyclable']  # Adjust if needed

# UI title
st.title("♻️ Waste Image Classifier")
st.write("Upload a photo of waste, and I'll tell you if it's compost, landfill, or recyclable.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Show image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Preprocess
    img = img.resize((512, 384))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = round(np.max(predictions) * 100, 2)

    # Show result
    st.success(f"Prediction: **{predicted_class}** ({confidence}% confidence)")

