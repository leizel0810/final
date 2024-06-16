import streamlit as st
import pickle
from nltk.classify import NaiveBayesClassifier

# Set the title of the Streamlit app
st.title("Feelings Analyzer")
st.subheader("*ੈ✩‧₊˚༺☆༻*ੈ✩‧₊˚")

# Input for the user to enter their message
message = st.text_input("Hi, Leizel here! Tell me what you feel today:⋆⭒˚.⋆🪐 ⋆⭒˚.⋆")

# Load the pre-trained sentiment analysis model
filename = 'pages/sumpayanalyzer.sav'
with open(filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

def word_features(words):
    return dict([(word, True) for word in words])

# Function to classify emotion based on the message
def sayFeeling():
    if message:
        message_tone = loaded_model.classify(word_features(message.split()))

        if message_tone == 'Happy':
            st.write("You are feeling happy 🤭.")
        elif message_tone == 'Scared':
            st.write("You are feeling is Valid⋆⭒˚.⋆.")
        elif message_tone == 'Angry':
            st.write("You are feeling angry 😠.")
        elif message_tone == 'Nervous':
            st.write("You are feeling nervous 😰.")
        else:
            st.write("You are feeling sad 🥺.")
    else:
        st.write("Please enter a message to analyze what you feel.")

# Button to trigger the sayFeeling function
if st.button('Say it'):
    sayFeeling()