import streamlit as st
st.set_page_config(layout="wide", page_title="Learnings")

st.title("🔍Student Reflections on Learning Experiences")
st.header('📚🔍 Valuable Learnings🖊️📖✏️📚')


image_paths = ["./pictures/L8.jfif", "./pictures/l10.jfif"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)

# Section 1: Quantitative Methods
st.header("Quantitative Methods📚")
st.write("""
As a student, I have gained a comprehensive understanding of quantitative methods. Here are some key takeaways:

- **Descriptive Statistics:** I learned how to summarize and describe the main features of a dataset using measures like mean, median, mode, standard deviation, and variance.
- **Inferential Statistics:** This involves making inferences about a population based on a sample. I learned about hypothesis testing, confidence intervals, and p-values.
- **Data Visualization:** I gained skills in visualizing data using charts and graphs to interpret and present data findings effectively.
""")

# Section 2: Lessons Learned in Making a Streamlit Application
st.header("💡Lessons Learned in Making a Streamlit Application")
st.write("""
Creating a Streamlit application was a valuable learning experience. Here are some lessons I learned:

- **Ease of Use:** Streamlit is incredibly user-friendly, allowing for rapid development and deployment of web applications.
- **Interactivity:** Adding interactive widgets like sliders, buttons, and text inputs enhances the user experience and engagement.
- **Real-time Updates:** Streamlit's ability to update the app in real-time as code changes make the development process smooth and efficient.
- **Integration:** Streamlit integrates seamlessly with popular Python libraries such as Pandas, NumPy, and Matplotlib, making data manipulation and visualization straightforward.
- **Customization:** Despite its simplicity, Streamlit allows for significant customization to tailor the app's look and feel to specific needs.
""")

# Section 3: Image Classification
st.header("💡Image Classification")
st.write("""
In my journey with image classification, I learned the following:

- **Convolutional Neural Networks (CNNs):** CNNs are powerful tools for image classification tasks. I learned how to build and train CNNs to classify images accurately.
- **Data Augmentation:** Techniques like rotation, flipping, and zooming improve model generalization by artificially expanding the training dataset.
- **Transfer Learning:** Using pre-trained models like VGG16, ResNet, and Inception helps in achieving higher accuracy with less computational resources and training time.
- **Evaluation Metrics:** Understanding metrics like accuracy, precision, recall, and F1-score is crucial for assessing the performance of image classification models.
- **Practical Applications:** Image classification has diverse applications, from medical diagnosis to automated quality control in manufacturing.
""")

# Section 4: Sentiment Analysis
st.header("💡Sentiment Analysis")
st.write("""
Sentiment analysis was another fascinating area I explored. Key lessons include:

- **Text Preprocessing:** Techniques like tokenization, stemming, and lemmatization are essential for preparing text data for analysis.
- **Feature Extraction:** Methods like Bag of Words (BoW), Term Frequency-Inverse Document Frequency (TF-IDF), and word embeddings (Word2Vec, GloVe) help in converting text into numerical features.
- **Model Building:** I learned to build models using algorithms like Naive Bayes, Support Vector Machines (SVM), and deep learning models like LSTM and BERT for sentiment analysis.
- **Polarity and Subjectivity:** Sentiment analysis involves determining the polarity (positive, negative, neutral) and subjectivity (opinionated or factual) of text.
- **Applications:** Sentiment analysis is widely used in various fields, including marketing, customer service, and social media monitoring, to gauge public opinion and improve user experience.
""")

# Run the app using the command:
# streamlit run app.py

