import streamlit as st
from PIL import Image

# Set page config to apply background color
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
)

# Add CSS to customize the page style
st.markdown(
    """
    <style>
    /* Apply blue background color to Streamlit app container */
    .stApp {
        background-color: #0000FF;
    }
    /* Apply neon green font color to text elements */
    .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6, .stMarkdown li, .stMarkdown strong {
        color: #39FF14 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Open the image
image = Image.open("Myla_me_baseball.jpg")
# Rotate the image by 90 degrees clockwise
image = image.rotate(-90)
# Display the rotated image
st.image(image, caption="Us at the Indian's game!!!",width=1000)

# Open the "me.jpeg" image
me_image = Image.open("me.jpeg")
# Get the width of the image and calculate the new width (half the original width)
width = me_image.width
new_width = width // 8
# Display the image with the new width
st.image(me_image, caption="It's me!", width=new_width)
