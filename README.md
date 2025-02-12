# AI-powered Document Q&A Tool

## Features
- Upload and parse files of various formats: XLSX, CSV, DOCX, and PDF.
- Extract and display the contents of uploaded files.
- Ask questions about the content of the uploaded documents, with answers generated by an AI model (Cohere).
- Visualize data (if applicable) using Plotly charts.
- User-friendly interface with a clear step-by-step guide.
- Custom sidebar design and pastel-themed main heading.

## Instructions for Running the Application Locally
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```



4. Run the application:
   ```bash
   streamlit run <script-name>.py
   ```

5. Open the displayed local URL in your web browser to access the app.

## Challenges Faced
- **Handling different file types**: Parsing and extracting content from multiple file formats (XLSX, CSV, DOCX, PDF) required different libraries and methods.
- **Customizing Streamlit UI**: Streamlit does not natively support advanced CSS customization, so inline CSS was used for sidebar and heading design.
- **OpenAI API Integration Limitations**: Initially considered using OpenAI's API, but faced rate limits. Switched to Cohere, which allowed unlimited requests but provided limited and sometimes less accurate answers.

## Additional Details
- If you encounter issues with library imports, verify that all required dependencies are installed correctly.

Feel free to contact [sudhanshusinha966@gmail.com](mailto:sudhanshusinha966@gmail.com) for any queries or feedback!
