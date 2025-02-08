import pandas as pd
import streamlit as st
import joblib as jb

# Load the model
model = jb.load('xgb_model.jb')

# Streamlit UI
st.title("House Price Prediction")
st.write("Enter the details below to predict the house price")

# Define input features
inputs = ['OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
          'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
          'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
          'CentralAir']

# Create input dictionary
input_data = {}

for feature in inputs:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox(f"{feature}", options=['yes', 'no'], index=0)
    else:
        input_data[feature] = st.number_input(
            f"{feature}",
            value=0.0,
            step=1.0 if feature in ['OverallQual', 'FullBath', 'Fireplaces'] else 0.1
        )

# Predict button
st.write(input_data)  # Debugging: Show input values
if st.button("Predict Price"):
    # Convert 'yes'/'no' to 1/0 for CentralAir
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == 'yes' else 0

    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([input_data])

    # Make prediction
    prediction = model.predict(input_df)

    # Display result
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")
