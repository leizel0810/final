import streamlit as st

st.title("ALL ABOUT LEIZEL👩👈")



st.title("📷SELF PORTRAIT")


image_paths = ["./pictures/l5.jfif", "./pictures/l4.jfif", "./pictures/l6.jfif"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header(" SUMPAY, LEIZEL P.")


# Personal Information
st.header("Personal Information✨")
st.write("**NAME:** 🎀𓂃 ࣪˖SUMPAY LEIZEL PASILAN")
st.write("**Date of Birth:** August 10, 2002")
st.write("**AGE:** 21 YEARS OLD")
st.write("**Address:**  Hda. San Antonio 1, Brgy. Dos Hermanas, Talisay City, Negros Occidental")
st.write("**EDUCATION:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**COURSE AND YEAR:** 3rd year Bachelor of Science in Information Systems Student")

with st.expander("GET TO KNOW ME BETTER ୧⍤⃝💐"):
    st.markdown("""
    
    #
On a personal level, I will be more mature and confident, having balanced my professional aspirations with my personal
                 life. I will have built strong relationships both inside and outside of work, and possibly started a 
                family. My journey over the past decade will have taught me valuable lessons in perseverance, 
                adaptability, and the importance of lifelong learning. Overall, I will be proud of the person I have 
                become and excited about the future opportunities that lie ahead.
           
    """, unsafe_allow_html=True)

st.header("Hobbies")
st.write("1. *\"Playing Online Gamws\"*")
st.write("2. *\"Watching Kdarams\"*")


st.header("Quotes in Life")

st.write("The most courageous act is still to think for yourself. Aloud. - Coco Chanel")

st.write("Empathy is seeing with the eyes of another, listening with the ears of another, and feeling with the heart of another. - Alfred Adler")

st.write("No one can make you feel inferior without your consent. - Eleanor Roosevelt")

st.write("The future belongs to those who believe in the beauty of their dreams.- Eleanor Roosevelt")

st.write("You can never leave footprints that last if you are always walking on tiptoe.- Leymah Gbowee")

st.header("Favorite Food")
st.write("2. *\"Carbonara\"*")
st.write("3. *\"Adobo\"*")

st.header("Life Lessons")
st.write("1. *\"Embrace failure as a stepping stone to success, and remember to prioritize self-care along the way.\"*")
st.write("2. *\"Trust your intuition, seek continuous learning, find balance in all aspects of life\"*")
st.write("3. *\"Live with intention, practice mindfulness, foster perseverance, embrace diversity, prioritize meaningful connections\"*")





images = [
    {"path": "pictures/l2.jfif", "caption": "There is a remarkable group of people who have been instrumental in helping me survive and thrive during my school days: my classmates. They are a diverse and dynamic bunch, each bringing their unique strengths and personalities to the table."},
    {"path": "pictures/l1.jfif", "caption": "These classmates are more than just peers; they are friends who have stood by me through thick and thin. From late-night study sessions and group projects to sharing notes and encouraging words, they have always been there to lend a helping hand."},
]


st.title("🎓👨‍🎓 COLLEGE MEMORIES")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: #AD88C6;
        padding: 2em;
    }
    h1, h2 {
        color: #005C78;
    }
    .stText {
        font-size: 1.5em;
        color: #005C78;
    }
    </style>
    """,
    unsafe_allow_html=True
)
