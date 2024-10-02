# DocuSage: AI Document Assistant

DocuSage is an advanced document processing assistant that enables users to extract text from various document formats, including images and PDFs, in any language. It provides a conversational interface for users to ask questions based on the extracted content, facilitating efficient information retrieval and analysis.

## Features

- **Document Upload**: Users can upload images or PDF documents for processing.
- **Text Extraction**: Extracts visible text from documents regardless of the language and provides English translations for non-English text.
- **Conversational Interface**: Users can engage in a dialogue to ask questions about the content extracted from the document.
- **Contextual Awareness**: Maintains context throughout the conversation for seamless follow-up questions.
- **Interactive Responses**: Provides detailed, relevant answers based on the extracted content.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hsinha11/DocuSage-AI-Document-Assistant.git
   cd DocuSage-AI-Document-Assistant
2.  **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
3.  **Activate the virtual environment**:
    ```bash
    .\venv\Scripts\activate
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
5.  **Set up environment variables: Create a `.env` file in the project root and add your Google API key**:
    ```bash
    GOOGLE_API_KEY=your_api_key_here
## Usage
1.  **Run the application**:
     ```bash
     streamlit run main.py
2.  **Upload a document: Choose an image or PDF file to upload.**
3.  **Ask questions: Use the input field to inquire about the content of the uploaded document.**
## Licence
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments
- **Special thanks to the creators of the Google Generative AI for providing the powerful API used in this project.**
## Leave a star ⭐ if you like this repository!
