import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Training the model and saving it with label encoders
def train_and_save_model():
    # Load the dataset
    file_path = 'pages/ObesityDataSet_raw_and_data_sinthetic.csv'  
    data = pd.read_csv(file_path)

    # Encode categorical variables
    label_encoders = {}
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

    # Split data into features and target
    X = data.drop('NObeyesdad', axis=1)  # assuming 'NObeyesdad' is the target column
    y = data['NObeyesdad']

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Save the model and label encoders
    with open('obesity_model.pkl', 'wb') as f:
        pickle.dump({'model': model, 'label_encoders': label_encoders, 'feature_names': X.columns.tolist()}, f)

# Load the trained model and label encoders
def load_model_and_encoders():
    with open('obesity_model.pkl', 'rb') as f:
        data = pickle.load(f)
    return data['model'], data['label_encoders'], data['feature_names']

# Train and save the model (only needed to run once, can be commented out after the model is saved)
train_and_save_model()

# Load the model and label encoders
loaded_model, label_encoders, feature_names = load_model_and_encoders()

# Load the label encoder for the target variable
label_encoder = label_encoders['NObeyesdad']

st.title("Obesity Level Predictor :weight_lifter:")
st.subheader("Enter your details to predict your obesity level:")

# User inputs for different factors
inputs = {}
inputs['Age'] = st.slider("Age: ", 10, 80)
inputs['Height'] = st.slider("Height (m): ", 1.0, 2.5)
inputs['Weight'] = st.slider("Weight (kg): ", 30, 200)
inputs['FCVC'] = st.slider("Frequency of consumption of vegetables (0-3): ", 0, 3)
inputs['NCP'] = st.slider("Number of main meals (1-4): ", 1, 4)
inputs['CH2O'] = st.slider("Consumption of water daily (liters): ", 1, 4)
inputs['FAF'] = st.slider("Physical activity frequency (days per week): ", 0, 7)
inputs['TUE'] = st.slider("Time using technology devices (hours per day): ", 0, 24)

# Function to make a prediction
def predict_obesity_level(input_features):
    # Ensure all features used during training are present
    features = {feature: input_features.get(feature, 0) for feature in feature_names}
    features_df = pd.DataFrame([features])
    prediction = loaded_model.predict(features_df)
    predicted_label = label_encoder.inverse_transform(prediction)
    return predicted_label[0]

# Display button and result
if st.button('Predict'):
    obesity_level = predict_obesity_level(inputs)
    st.text("The predicted obesity level is:")
    st.text_area(label="", value=obesity_level, height=100)
