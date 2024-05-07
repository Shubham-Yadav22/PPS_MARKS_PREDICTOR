import numpy as np
import pickle
import sklearn
import pandas as pd

import streamlit as st

pickle_in = open("PPS.pkl", "rb")
Predictor = pickle.load(pickle_in)


def predict_pps_marks(physics, maths, ee, evs):
    prediction = Predictor.predict([[physics, maths, ee, evs]])
    print(prediction)
    return prediction


def main():
    st.title("PPS_Marks_Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">PPS_Marks_Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    physics = st.text_input("Physics", "Type Here")
    maths = st.text_input("Maths", "Type Here")
    ee = st.text_input("Electrical", "Type Here")
    evs = st.text_input("EVS", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_pps_marks(physics, maths, ee, evs)
    st.success(f'Marks in pps is {format(result)} ')
    if st.button("About"):
        st.text("Lets Check")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
