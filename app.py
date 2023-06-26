import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('saved_model.pkl')
reg_load = model['model']
def predict(input_data):
    # Create a pandas DataFrame from the input data
    df = pd.DataFrame([input_data])

    # Make predictions using the loaded model
    prediction = reg_load.predict(df)
    return prediction

def main():
    st.title('Machine Learning Web App')
    st.write('Enter the input data:')

    # Create input fields for each feature
    item_weight = st.number_input('Item Weight', min_value=0.0, step=0.001, format='%.3f')
    item_fat_content = st.selectbox('Item Fat Content', [0.0, 1.0])
    item_visibility = st.number_input('Item Visibility', min_value=0.0, format='%.6f')
    item_mrp = st.number_input('Item MRP', min_value=0.0, format='%.4f')
    outlet_location_type = st.selectbox('Outlet Location Type', [0.0, 1.0, 2.0])
    outlet_type = st.selectbox('Outlet Type', [0.0, 1.0, 2.0, 3.0])
    item_outlet_sales = st.number_input('Item Sales', min_value=0.0, format='%.4f')
    
    # Create a dictionary with input data
    input_data = {
        'Item_Weight':item_weight,
        'Item_Fat_Content': item_fat_content,
        'Item_Visibility': item_visibility,
        'Item_MRP': item_mrp,
        'Outlet_Location_Type': outlet_location_type,
        'Outlet_Type': outlet_type,
        'Item_Outlet_Sales': item_outlet_sales,
    }

    if st.button('Predict'):
        # Call the predict function with the input data
        prediction = predict(input_data)

        # Display the prediction result
        st.write('Prediction:', prediction)

if __name__ == '__main__':
    main()
