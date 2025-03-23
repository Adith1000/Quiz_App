from flask import Flask, render_template, request
import os
from Control import getTxt

# Configure Flask to use the 'view' folder for both templates and static files,
# and set static_url_path to an empty string so that asset paths like /css/styles.css work.
app = Flask(__name__, template_folder="view", static_folder="view", static_url_path="")

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/question', methods=['POST'])
def upload_file():
    # Check if the file is included in the request
    if 'pdf_file' not in request.files:
        return "No file part"
    
    file = request.files['pdf_file']
    
    # Check if a file is selected
    if file.filename == '':
        return "No selected file"
    
    # Check if the file exists and is a PDF
    if file and file.filename.lower().endswith('.pdf'):
        # Define the destination directory and make sure it exists
        upload_dir = "/Users/adithshetty/Desktop/Programming Folder/Quiz App/Quiz_App/Model/assets"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        # Build the full file path and save the file
        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)
        txt=getTxt.process_file(file_path)
        
        # Optionally, process the file if needed before rendering the next page.
        # For now, we directly render the question page.
        return render_template('question.html')
    
    return "Invalid file type. Only PDF files are allowed."

if __name__ == "__main__":
    app.run(debug=True)
