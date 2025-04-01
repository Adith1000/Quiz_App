from flask import Flask, render_template, request, session, jsonify
import os
from Control import getTxt, Process, data

# Configure Flask to use the 'view' folder for both templates and static files,
# and set static_url_path to an empty string so that asset paths like /css/styles.css work.
app = Flask(__name__, template_folder="view", static_folder="view", static_url_path="")
app.secret_key = os.urandom(24)
score=0

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
        output_path = "/Users/adithshetty/Desktop/Programming Folder/Quiz App/Quiz_App/Model/assets/text" + ".txt"
        Process.run(output_path)
        # Optionally, process the file if needed before rendering the next page.
        # For now, we directly render the question page.

        return render_template('question.html')
    
    return "Invalid file type. Only PDF files are allowed."

@app.route('/next_question', methods=['POST'])
def next_question():
    global score  # Consider moving this to session if you want to avoid globals.
    
    # Get the JSON data from the POST request
    request_data = request.get_json()
    selected_option = request_data.get('selected_option')  # "true" or "false"
    
    
    if score>0:
        # Retrieve the current question index from session (default to 0)
        current_index = session.get('current_index', 0)
        # Get the current question using your data accessor
        curr_question = data.get_question(current_index)
    
        # Ensure the question exists
        if curr_question is None:
            return jsonify({'question': "No more questions available."})
    
        # Compare the answer and update the score if correct
        if curr_question["Answer"] == selected_option:
            score += curr_question["Score"]
    
    else: 
        current_index=0
        score=1
    
    # Move to the next question if available.
    # Assuming data.curr_id holds the total number of questions
    if data and current_index < data.curr_id - 1:
        current_index += 1
        session['current_index'] = current_index
        nxt_question = data.get_question(current_index)
        next_question_text = nxt_question.get("Question", "Question text not available")
        return jsonify({'question': next_question_text})
    else:
        # If there are no more questions, return the final score.
        return jsonify({'question': "Your Score is: " + str(score)})


if __name__ == "__main__":
    app.run(debug=True)
