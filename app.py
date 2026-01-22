import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Dashboard AI", layout="centered")

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Load RemixIcon CDN
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/remixicon@4.8.0/fonts/remixicon.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Invoice AI</h1>
    <p>An interactive dashboard to demonstrate our AI model capabilities</p>
</div>
""", unsafe_allow_html=True)

# =========================
# 🤖 HARD-CODED CHATBOT / FAQ SECTION
# =========================

st.markdown("""
<div class="card">
    <h3>
        <i class="ri-question-answer-line" style="font-size:26px; vertical-align:middle;"></i>
        &nbsp; About This Project
    </h3>
    <p>Select a question to understand what this project does.</p>
</div>
""", unsafe_allow_html=True)

faq_questions = {
    "What does this project do?": "This project uses an AI model to analyze invoice images and extract useful information from them.",
    "How do I use this app?": "Simply upload an invoice image using the upload button and the system will process it and show the extracted results.",
    "What type of files are supported?": "Currently, this system supports JPG, PNG and JPEG image files.",
    "What AI model is used?": "We are using a deep learning based vision-language model trained for document understanding.",
    "What will be the output?": "The output will be structured information extracted from the invoice such as important fields and text."
}

selected_question = st.selectbox("Choose a question:", list(faq_questions.keys()))

st.info(faq_questions[selected_question])

# =========================
# INPUT SECTION
# =========================

st.markdown("""
<div class="card">
    <h3>
        <i class="ri-folder-image-fill" style="font-size:28px; vertical-align:middle;"></i>
        &nbsp; Model Input
    </h3>
    <p>Upload an image to test our AI pipeline.</p>
</div>
""", unsafe_allow_html=True)

uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    # Preview Card
    st.markdown("""
    <div class="card">
        <h3>
            <i class="ri-image-line" style="font-size:26px; vertical-align:middle;"></i>
            &nbsp; Preview
        </h3>
    </div>
    """, unsafe_allow_html=True)

    st.image(image, use_container_width=True)

    # Result Card
    st.markdown("""
    <div class="card">
        <h3>
            <i class="ri-magic-line" style="font-size:26px; vertical-align:middle;"></i>
            &nbsp; Result
        </h3>
        <p>Model output will appear here.</p>
    </div>
    """, unsafe_allow_html=True)

    st.success("Image processed successfully!")
