import streamlit as st
import numpy as np
import joblib
import requests
import os

def download_model():
    url = 'https://github.com/yasharthrana/Dynamic-Pricing-/releases/download/v1.0/rf_final_model.pkl'  # Replace with your actual URL
    local_filename = 'rf_final_model.pkl'
    
    if not os.path.exists(local_filename):
        with st.spinner('Downloading model...'):
            response = requests.get(url)
            with open(local_filename, 'wb') as f:
                f.write(response.content)
            st.success('Model downloaded successfully.')
    else:
        st.info('Model already exists locally.')

def load_model():
    with open('rf_final_model.pkl', 'rb') as file:
        model = joblib.load(file)
    return model

def prediction(input_data):
    pred = model.predict(input_data)[0]
    return f'Predicted Total Price: {pred:.2f}'

def main():
    st.title("Dynamic Pricing Prediction App")
    st.subheader("Enter the details to predict total price")
    
    # Download and load the model
    download_model()
    model = load_model()
    
    # Take user inputs
    price = st.text_input('Enter Price')
    discounted_price = st.text_input('Enter Discounted Price')
    quantity = st.text_input('Enter Quantity')
    avg_spend_cust = st.text_input('Enter Avg Spend Per Customer')
    avg_rev_product = st.text_input('Enter Avg Revenue Per Product')
    
    # Convert inputs to proper format
    try:
        inp_list = np.array([[float(price), float(discounted_price), int(quantity), 
                              float(avg_spend_cust), float(avg_rev_product)]])
    except ValueError:
        st.error("Please enter valid numeric inputs.")
        return  # Stop execution if values are not numeric

    if st.button('Predict'):
        response = prediction(inp_list)
        st.success(response)

if __name__ == '__main__':
    main()
