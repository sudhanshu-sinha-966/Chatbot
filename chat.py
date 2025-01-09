import streamlit as st
import pandas as pd
import cohere
import plotly.express as px
from io import StringIO
import docx
import PyPDF2
import os



# Initialize Cohere Client
cohere_api_key=st.secrets["cohere"]["key"]


co = cohere.Client(cohere_api_key)

# Function to handle XLSX files and extract data as a DataFrame
def parse_xlsx(file):
    return pd.read_excel(file)

# Function to process CSV files and return data as a DataFrame
def parse_csv(file):
    return pd.read_csv(file)

# Function to process DOCX files and return content as text
def parse_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract text from a PDF file
def parse_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages])

# Convert a DataFrame into plain text
def dataframe_to_text(df):
    return df.to_string(index=False)

# Function to answer questions using Cohere's generate API
def get_answer_from_cohere(question, document_text):
    prompt = f"Document: {document_text}\n\nQuestion: {question}\n\nAnswer:"
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=100,
        temperature=0.3,
    )
    return response.generations[0].text.strip()

# Main Streamlit function
def main():
    # Set page configuration
    st.set_page_config(page_title="AI-powered Document Q&A", page_icon="📄", layout="wide")
    
    # Custom CSS for sidebar and main heading
    st.markdown(
        """
        <style>
        /* Sidebar Customization */
        .css-1d391kg {
            background-color: #1E3A8A; /* Blue color */
            color: white;
            padding: 20px;
            border-radius: 10px;
        }

        /* Main Heading Customization */
        .css-1v0mbdj {
            color: #A7C7E7; /* Pastel color */
            font-weight: bold;
        }
        
        /* Watermark customization */
        .watermark {
            position: fixed;
            bottom: 10px;
            right: 10px;
            color: rgba(0, 0, 0, 0.6);
            font-size: 20px;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            z-index: 1000;
        }
        .watermark span {
            font-weight: normal;
        }
        .watermark a {
            font-weight: bold;
            color: rgba(0, 0, 0, 0.6);
            text-decoration: none;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Title
    st.title("AI-powered Document Q&A")

    # Sidebar instructions
    with st.sidebar:
        st.write("### Steps to use the tool:")
        st.write("1. Select the file type you want to upload (XLSX, CSV, DOCX, or PDF).")
        st.write("2. Upload the chosen file.")
        st.write("3. Once uploaded, ask any question related to the content of the file.")
        st.write("4. The AI will provide answers based on the document you uploaded.")
        st.write("5. Enjoy interacting with the document!")

    # File type selection
    file_type = st.selectbox("Select file type to upload", ["XLSX", "CSV", "DOCX", "PDF"])
    uploaded_file = st.file_uploader(f"Upload a {file_type} file", type=file_type.lower())

    if uploaded_file:
        # Parse the file and extract content
        if file_type == "XLSX":
            df = parse_xlsx(uploaded_file)
            document_text = dataframe_to_text(df)
        elif file_type == "CSV":
            df = parse_csv(uploaded_file)
            document_text = dataframe_to_text(df)
        elif file_type == "DOCX":
            document_text = parse_docx(uploaded_file)
        elif file_type == "PDF":
            document_text = parse_pdf(uploaded_file)

        # Display preview if the file is a DataFrame
        if 'df' in locals():
            st.write("Here's a preview of your document:")
            st.write(df.head())

        # User query
        question = st.text_input("Ask a question about the document:")
        if question:
            with st.spinner("Processing your question..."):
                answer = get_answer_from_cohere(question, document_text)
            st.write(f"Answer: {answer}")

        # Visualization example
        if 'product' in locals() and 'sales' in locals():
            st.write("### Data Visualization")
            fig = px.bar(df, x='product', y='sales', title="Sales by Product")
            st.plotly_chart(fig)

    # Add watermark with email on bottom-right
    st.markdown(
        """
        <div class="watermark">
            Made by <span>Sudhanshu Sinha</span> | <a href="mailto:sudhanshusinha966@gmail.com">Email Me</a>
        </div>
        """, unsafe_allow_html=True
    )

# Run the Streamlit app
if __name__ == "__main__":
    main()
