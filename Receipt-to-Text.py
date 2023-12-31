import streamlit as st
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Function to preprocess the image
def preprocess_image(image):
    gray_image = image.convert('L')
    threshold_image = gray_image.point(lambda x: 0 if x < 128 else 255)
    denoised_image = threshold_image.filter(ImageFilter.MedianFilter())
    enhanced_image = ImageEnhance.Contrast(denoised_image).enhance(2)
    return enhanced_image

# Function to perform OCR on an image
def ocr_image(image, lang='eng'):
    processed_image = preprocess_image(image)
    text = pytesseract.image_to_string(processed_image, lang=lang)
    return text

# Streamlit app
def main():
    st.title("Receipt to Text - Anas Javaid")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Processing...")
        extracted_text = ocr_image(image)
        st.write("Extracted Text:")
        st.text_area("Result", extracted_text, height=250)

    # Logging the server URLcl
    logging.info("Streamlit server running on http://localhost:8501")

if __name__ == "__main__":
    main()
