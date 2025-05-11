# ♻️ Automated Waste Classifier (Streamlit App)

A simple and interactive web application built with **Streamlit** that classifies waste images into **Recyclable**, **Compost**, or **Landfill** using a Convolutional Neural Network (CNN).

---

## 🚀 Project Overview

This app helps users determine how to dispose of an item just by uploading a picture of it. The model was trained using a combination of the **TrashNet** dataset and **custom collected compost images**.

---

## 🧠 Model Details

- Model Type: Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Input: JPG images resized to 512×384
- Output: One of three categories:
  - ♻️ **Recyclable** (plastic, glass, paper, metal, cardboard)
  - 🌱 **Compost** (food waste, organic material)
  - 🗑️ **Landfill** (non-recyclable trash)

---

## 📂 Dataset

- Base: [TrashNet](https://github.com/garythung/trashnet)
- Additional: Manually collected biological (compost) images
- Images were resized, reformatted, and organized into three folders.

---

## ⚙️ How to Run

 Clone this repository:
   ```bash
   git clone https://github.com/yourusername/waste-classifier-app.git
   cd waste-classifier-app
Install dependencies:

pip install -r requirements.txt
Launch the app:


streamlit run app.py
Upload a waste image and view the predicted category with confidence scores.
