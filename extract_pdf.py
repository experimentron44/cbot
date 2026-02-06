from pypdf import PdfReader
import sys
import os

def extract_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Using the exact path provided in the metadata
    path = r"e:\vworkshop\Copy of Rezi Resume Template - Updated Dec. 2025.pdf"
    content = extract_text(path)
    output_path = r"e:\vworkshop\resume_content.txt"
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully wrote content to {output_path}")
    except Exception as e:
        print(f"Failed to write file: {e}")
