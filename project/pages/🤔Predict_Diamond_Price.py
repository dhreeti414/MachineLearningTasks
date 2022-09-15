import streamlit as st
import pandas as pd
from pickle import load

df = pd.read_csv("diamonds.csv")

st.set_page_config(page_title="Predict", page_icon="🤔",layout="wide")
st.title("💎 Diamond Price Prediction 💎")

scalar= load(open('models/standard_scaler.pkl', 'rb'))
rf_model= load(open('models/sv_model.pkl', 'rb'))

# Define the prediction function
def predict(carat, cut, color, clarity, depth, table, x, y, z):
    #Predicting the price of the carat
    if cut == 'Fair':
        cut = 1
    elif cut == 'Good':
        cut = 2
    elif cut == 'Very Good':
        cut = 3
    elif cut == 'Premium':
        cut = 4
    elif cut == 'Ideal':
        cut = 5

    if color == 'J':
        color = 1
    elif color == 'I':
        color = 2
    elif color == 'H':
        color = 3
    elif color == 'G':
        color = 4
    elif color == 'F':
        color = 5
    elif color == 'E':
        color = 6
    elif color == 'D':
        color = 7
    
    if clarity == 'I1':
        clarity = 1
    elif clarity == 'SI2':
        clarity = 2
    elif clarity == 'SI1':
        clarity = 3
    elif clarity == 'VS2':
        clarity = 4
    elif clarity == 'VS1':
        clarity = 5
    elif clarity == 'VVS2':
        clarity = 6
    elif clarity == 'VVS1':
        clarity = 7
    elif clarity == 'IF':
        clarity = 8

    query_point= pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z'])
    query_point_tranformed= scalar.fit_transform(query_point)
    prediction = rf_model.predict(query_point_tranformed)
    return prediction

cut = st.selectbox('Select the CUT rate of Diamond: 💎', list(df['cut'].unique()))
color = st.selectbox('Select the COLOR rate of Diamond: 💎', list(df['color'].unique()))
clarity = st.selectbox('Select the CLARITY rate of Diamond: 💎', list(df['clarity'].unique()))
carat = st.slider('Carat Weight of the Diamond 💎', min_value=0.1, max_value=10.00, value=1.00)
x = st.slider('Diamond Length (X) in mm: 💎', min_value=0.1, max_value=20.0, value=1.0)
y = st.slider('Diamond Width (Y) in mm: 💎', min_value=0.1, max_value=60.0, value=1.0)
z = st.slider('Diamond Height (Z) in mm: 💎', min_value=0.1, max_value=40.0, value=1.0)
depth = st.slider('Diamond Depth Percentage: 💎', min_value=0.1, max_value=100.0, value=1.0)
table = st.slider('Diamond Table Percentage: 💎', min_value=0.1, max_value=100.0, value=1.0)

if st.button('Predict'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f'The predicted price of the diamond is ${price[0]:.2f} USD')

page_bg_img = '''
<style>
.stApp {
background-image: url("https://cdn.wallpapersafari.com/49/83/CIYBXp.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)