
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT: MACHINE LEARNING APPLICATIONS","🌟"),
        Section("MAIN PAGE","📚"),
        Page("pages/self.py", "👩‍💻 EVERYTHING ABOUT LEIZEL", "1️⃣", in_section=True),
        Page("pages/specification.py", "📲 APP DESCRIPTIONS", "2️⃣", in_section=True),
        Page("pages/learnings.py", "💡 INSIGHTS", "3️⃣", in_section=True),

        Section("APPLICATION PROJECT", "💼"),
        Page("pages/emotion.py", "🙌 FEELINGS ANALYZER", "1️⃣", in_section=True),
        Page("pages/classifyimage.py", "🌞 IMAGE CLASSIFICATION", "2️⃣", in_section=True),
        Page("pages/prediction.py", "🔮 PREDICTION", "3️⃣", in_section=True),

        Section("SOURCE CODE", "⚡"),
        Page("pages/emotion_src.py", "🔗 SENTIMENT ANALYZER SRC", "1️⃣", in_section=True),
        Page("pages/classifyimage_src.py", "🔗 ROOM CLASSIFICATION SRC", "2️⃣", in_section=True),
        Page("pages/prediction_src.py", "🔗 PREDICTION SRC", "3️⃣", in_section=True),

        
    ]
)

hide_pages(["Thank you"])
st.markdown("---")

st.header("SUMPAY, LEIZEL P of BSIS 3-B")
st.subheader("FINAL REQUIREMENTS IN ITEQMT")
st.image("pictures/l3.jfif")

st.markdown("---")

with st.expander("ALL ABOUT STREAMIT""🔗"):
    st.markdown("""
    
    #

        Streamlit is an open-source Python framework that allows developers to create interactive, 
                data-driven web applications with minimal code. It's particularly popular in the data
                 science and machine learning communities because it simplifies the process of creating
                 web apps for data visualization and model deployment. Here are some key features and concepts 
                of Streamlit:
                Key Features
* Easy to Use:
Streamlit is designed to be simple and intuitive. You can create a web app with just a few lines of Python code.
* Interactive Widgets:
Streamlit provides a variety of widgets such as sliders, buttons, and text inputs, which can be used to create interactive elements in your app.
* Real-time Updates:
Streamlit apps automatically update in real-time as you modify the code, making it easy to see changes immediately.
* Integration with Popular Libraries:
Streamlit integrates well with popular data science libraries such as Pandas, Matplotlib, Plotly, and others.
* Customizable Layout:
You can customize the layout of your app using simple and flexible layout functions.
                
### 🔎 Overview""", unsafe_allow_html=True)





st.markdown("""
Machine learning (ML) is a subset of artificial intelligence (AI) that focuses on developing algorithms and 
            statistical models that enable computers to perform tasks without explicit instructions. Instead,
             these systems learn from and make decisions based on data. Here are some key concepts and aspects
             of machine learning:
            
            Key Concepts
            
             Algorithms:

Machine learning uses algorithms to parse data, learn from it, and make informed decisions. Common algorithms include decision trees, neural networks, and support vector machines.

             Data:

Data is the foundation of machine learning. Datasets used for training and testing models consist of features (input variables) and labels (output variables).

             Training and Testing:

A model is trained on a training dataset, which includes input-output pairs. It is then tested on a separate testing dataset to evaluate its performance.

             Features:

Features are individual measurable properties or characteristics of the data. Feature engineering involves creating, selecting, and transforming features to improve model performance.

             Model Evaluation:

Models are evaluated using metrics such as accuracy, precision, recall, and F1-score. Cross-validation is often used to assess model performance more reliably.


                       
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
