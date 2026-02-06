# Minimalist Portfolio with AI Chatbot

A simple, non-scrollable dashboard-style portfolio website featuring an integrated AI chatbot trained on resume data.

## Features

- **Dashboard Layout**: Single-viewport design with a sidebar and scrollable internal content panels.
- **Minimalist Design**: Clean aesthetic using the Google color palette.
- **AI Chatbot**: A floating chat widget powered by the Groq API (`llama-3.1-8b-instant`) that answers questions based on the user's resume.
- **Dynamic Context**: The chatbot automatically reloads resume data from the text file on every request.

## Setup & Installation

1.  **Clone/Copy the project** to your local machine.

2.  **Install Dependencies**:
    Ensure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **PDF Extraction** (Optional):
    If you update the resume PDF (`Copy of Rezi Resume Template - Updated Dec. 2025.pdf`), run the extraction script to update the text content:
    ```bash
    python extract_pdf.py
    ```
    This will generate `resume_content.txt`.

## Running the Application

1.  **Start the Flask Server**:
    ```bash
    python app.py
    ```

2.  **Access the Website**:
    Open your browser and navigate to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Configuration

- **API Key**: The application is configured to use the Groq API. The key is set in `app.py`.
- **Resume File**: The bot reads from `resume_content.txt`. To change the source material, simply edit this text file or re-run the PDF extraction.

## Project Structure

- `app.py`: Flask backend server.
- `index.html`: Main portfolio page.
- `style.css`: Stylesheet.
- `chat.js`: Frontend logic for the chatbot.
- `extract_pdf.py`: Script to parse the resume PDF.
- `requirements.txt`: Python dependencies.
