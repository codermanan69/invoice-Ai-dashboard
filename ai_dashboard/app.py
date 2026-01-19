import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Dashboard AI", layout="centered")

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Load RemixIcon CDN  ✅✅
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

# Input Card
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
