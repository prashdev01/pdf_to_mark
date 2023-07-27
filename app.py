import PyPDF2
import re
from flask import Flask, render_template, request

app = Flask(__name__)

# Your code for PDF processing and Markdown file generation will be added here


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    # Get inputs from the form
    drive_link = request.form.get("drive-link")
    pdf_file = request.files.get("pdf-file")

    # Process the PDF and generate the Markdown content
    markdown_content = process_pdf(pdf_file)

    # Save the Markdown content to a file
    with open("output.md", "w", encoding="utf-8") as output_file:
        output_file.write(markdown_content)

    return render_template("result.html")

def process_pdf(pdf_file):
    # Function to process the PDF file and extract questions and answers
    # Add your PDF processing logic here

    # For demonstration purposes, let's assume the content is extracted as a list of tuples
    # where each tuple contains (question, answer)
    content = [
        ("Question 1", "Answer 1"),
        ("Question 2", "```python\nprint('Answer 2')\n```"),
        # Add more questions and answers here
    ]

    # Generate the Markdown content
    markdown_content = ""
    for question, answer in content:
        markdown_content += f"# **{question}**\n\n"  # Heading for the question
        markdown_content += f"**Answer:**\n\n{answer}\n\n"  # Answer with code block if needed

    return markdown_content

if __name__ == "__main__":
    app.run(debug=True)
