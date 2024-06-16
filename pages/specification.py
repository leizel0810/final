import streamlit as st

st.title("🧶 ITEQMT: APPLICATION DESCRIPTION ")


st.header('🦋⃤♡⃤🌈⃤ FEELINGS ANALYZER 🦋⃤♡⃤🌈⃤')
st.image("pictures/s4.jfif")

with st.expander("Feelings Analyzer"):
    st.markdown("""
    
    #
               This app uses smart software that learned from lots of examples to figure out how people are feeling from 
                what they write. It's made with a tool called Streamlit for making websites, so you can type in some words
                 and find out if they sound happy, sad, or angry. It helps you understand the feelings in your writing 
                quickly.

                Additionally, the app supports multiple languages and provides visual representations of the detected emotions, making it easier for users to analyze and interpret the results.
    It leverages NLP techniques to ensure accurate and fast emotion detection, enhancing user experience and application usability.
    
    """, unsafe_allow_html=True)

st.header('*ฅ^•ﻌ•^ฅ*IMAGE CLASSIFICATION *ฅ^•ﻌ•^ฅ*')
st.image("pictures/s1.jfif")


with st.expander("Image Classification 😻"):
    st.markdown("""
    
    #
              This project focuses on developing a predictive model using machine learning techniques to classify images of cats into different breeds. 
                By analyzing a dataset containing images of various cat breeds and employing image classification algorithms, the model aims to accurately predict the breed of a given cat image. 
    """, unsafe_allow_html=True)

st.header('📚👩‍💼 PREDICTOR 📚👩‍💼')
st.image("pictures/s2.jfif")
st.image("pictures/s3.jfif")


with st.expander("🔍Prediction"):
    st.markdown("""
    
    This project is centered on constructing a predictive model utilizing data sourced from various sources to
                 anticipate individuals' obesity levels. By scrutinizing historical data and harnessing machine
                 learning algorithms, the model endeavors to forecast the likelihood of obesity based on various
                 factors such as lifestyle, diet, genetics, and physical activity. This predictive tool aims to 
                offer valuable insights into potential obesity trends and risk factors, thereby enabling proactive
                 measures for promoting healthier lifestyles and reducing obesity rates.                  
    """, unsafe_allow_html=True)