import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Advertising.csv")

X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

st.title("Sales Prediction App")

tv = st.slider("TV Budget", 0, 300, 100)
radio = st.slider("Radio Budget", 0, 50, 20)
news = st.slider("Newspaper Budget", 0, 100, 10)

prediction = model.predict(
    [[tv, radio, news]]
)

st.success(
    f"Predicted Sales: {prediction[0]:.2f}"
)