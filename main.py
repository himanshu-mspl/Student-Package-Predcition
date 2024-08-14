import streamlit as st
import pickle
import numpy as np
import sklearn

st.header('Student Package Prediction')

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Input from the user
package = st.number_input("Enter the number of CGPA:")

# Make prediction
if st.button("Predict"):
    prediction = model.predict(np.array([[package]]))[0]
    st.write(f"Predicted student package for {package} CGPA: {prediction:.2f}")


