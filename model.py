import streamlit as st
import pickle

# Load trained model
file_name = './multi_linear.pkl'  # Change this if your model filename is different
with open(file_name, 'rb') as file:
    loaded_model = pickle.load(file)

# App UI
st.set_page_config(page_title="Startup Profit Predictor", layout="centered")
st.title("📊 Startup Profit Predictor")
st.markdown("Enter your startup expenses and choose a state to predict your profit.")

# Input fields
rd_spend = st.number_input("💰 R&D Spend", min_value=0.0, value=70000.0, step=1000.0)
admin = st.number_input("📋 Administration Spend", min_value=0.0, value=80000.0, step=1000.0)
marketing = st.number_input("📢 Marketing Spend", min_value=0.0, value=500000.0, step=1000.0)

state = st.selectbox("🌍 State", ["California", "Florida", "New York"])

# Convert state to one-hot encoding (assuming California is the baseline)
state_florida = 1 if state == "Florida" else 0
state_newyork = 1 if state == "New York" else 0

# Prediction
if st.button("🚀 Predict Profit"):
    input_data = [[rd_spend, admin, marketing, state_florida, state_newyork]]
    prediction = loaded_model.predict(input_data)
    st.success(f"💸 Predicted Profit: **${prediction[0].item():,.2f}**")

