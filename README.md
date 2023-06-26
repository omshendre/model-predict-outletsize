# BigMart Sales Prediction

This project is based on the BigMart Sales dataset and aims to predict the Outlet Size of BigMart stores. The dataset can be found on [Kaggle](https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data?select=Train.csv).

## Description

The BigMart Sales dataset contains various features that can be used to predict the Outlet Size of BigMart stores. This project utilizes machine learning techniques to build a predictive model for estimating the Outlet Size based on different input variables.

## Website

To explore and interact with the trained model, a web application has been developed. You can access the website at [BigMart Sales Prediction](https://model-predict-outletsize-y8148thf29.streamlit.app/). The website allows users to input values for various features and obtain predictions for the Outlet Size.

## Input Features and Value Types

The following input features are used in the model:

1. **Item Weight**: Weight of the item in kilograms (numeric float value).
2. **Item Fat Content**: Indicates the fat content of the item. "Low Fat" is denoted by 0, while "Regular Fat" is denoted by 1.
3. **Item Visibility**: Numeric float value representing the visibility of the item.
4. **Item MRP**: Maximum Retail Price (MRP) of the item, represented by any numeric float value.
5. **Outlet Location Type**: Categorical variable representing the location type of the outlet. There are three categories: "Tier 1", "Tier 2", and "Tier 3". They are encoded as 0, 1, and 2 respectively.
6. **Outlet Type**: Categorical variable representing the type of outlet. There are four categories: 0, 1, 2, 3, and 4.
7. **Item Sales**: representing the sales of the item. It can take any numeric float value.
8. **Outlet Size**: The target variable to be predicted, representing the size of the outlet.

## Instructions

1. Clone the repository: `git clone https://github.com/omshendre/model-predict-outletsize.git`.
2. Navigate to the project directory: `cd model-predict-outletsize`.
3. Set up a virtual environment (optional): `python3 -m venv env` and activate it.
4. Install the required dependencies: `pip install -r requirements.txt`.
5. Run the application: `streamlit run app.py`.
6. Access the web application in your browser at `http://localhost:8501`.

