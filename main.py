

from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import fitz  # PyMuPDF for PDF handling

load_dotenv()  # take environment variables from .env.

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini model and get responses
def get_gemini_response(input, content=None):
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Modify the prompt based on whether content (document text) is available
    if content:
        prompt = """
        You are an advanced document processing assistant skilled in extracting text from various documents, including images and PDFs, in any language. Your primary objective is to facilitate user inquiries based on the extracted content.

        1. **Initial Document Processing**: The user uploaded a document, and you have extracted the following content from it. Use this content to answer their questions. If any text is non-English, provide a translation.
        
        Extracted Document Content:
        {}
        
        2. **Conversational Context**: The user may ask questions based on the content. Maintain context throughout the conversation, allowing for seamless follow-up questions.

        User's Input: {}
        """.format(content, input)
    else:
        prompt = """
        You are a highly knowledgeable assistant capable of answering a wide range of questions. The user has not uploaded a document, so respond based on your knowledge and the user's input.

        User's Input: {}
        """.format(input)

    response = model.generate_content([prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def extract_text_from_pdf(uploaded_file):
    # Load PDF and extract text
    uploaded_file.seek(0)  # Reset file pointer to the beginning
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    
    if doc.page_count == 0:  # Check if the PDF has no pages
        raise ValueError("The PDF document has no pages.")
    
    text = ""
    for page in doc:
        text += page.get_text()
    return text

## Initialize the Streamlit app
st.set_page_config(page_title="DocuSage")

st.header("DocuSage")
input = st.text_area("Input Prompt:", key="input", height=150)
uploaded_file = st.file_uploader("Choose an image or PDF (optional)...", type=["jpg", "jpeg", "png", "pdf"])

content = None  # Initialize content to None
if uploaded_file is not None:
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        content = input_image_setup(uploaded_file)
    elif uploaded_file.type == "application/pdf":
        try:
            content = extract_text_from_pdf(uploaded_file)
        except ValueError as e:
            st.error(str(e))
    else:
        st.error("Unsupported file type.")

submit = st.button("Submit")

## If submit button is clicked
if submit:
    response = get_gemini_response(input, content)
    # st.subheader("Response:")
    st.write(response)
    content = None 
    # st.session_state.input = "" 
