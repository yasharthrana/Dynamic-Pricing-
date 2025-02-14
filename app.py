import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model and scaler
with open('rff_final_model.pkl', 'rb') as file:
    model = pickle.load(file)




def prediction(input_data):
    
    pred = model.predict(input_data)[0]
    return f'Predicted Total Price: {pred:.2f}'




def main():
    st.title("Dynamic Pricing Prediction App")
    st.subheader("Enter the details to predict total price")
    
   
    price = st.text_input('Enter Price')
    discounted_price = st.text_input('Enter Discounted Price')
    quantity = st.text_input('Enter Quantity')
    avg_spend_cust = st.text_input('Enter Avg Spend Per Customer')
    avg_rev_product = st.text_input('Enter Avg Revenue Per Product')
    
    
    
    inp_list = [[Price,DiscountedPrice,Quantity,AvgSpendPerCustomer,AvgRevenuePerProduct]]

    if st.button('Predict'):
        response = prediction(inp_list)
        st.success(response)

if _name_ == '_main_':
    main()