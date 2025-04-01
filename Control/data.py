import os
import sys
from supabase import create_client, Client

module_path = os.path.abspath("/Users/adithshetty/Desktop/Programming Folder/Quiz App/Quiz_App")
if module_path not in sys.path:
    sys.path.insert(0, module_path)

import api_keys

# Hardcoding for development; consider using environment variables properly
url: str = api_keys.db_url_key  # Replace with os.environ.get("SUPABASE_URL") if needed
key: str = api_keys.db_api_key  # Replace with os.environ.get("SUPABASE_KEY") if needed
supabase: Client = create_client(url, key)
 
curr_id = 0

def insert_question(question, score, ans):
    global curr_id  # Declare that we are using the global variable
    curr_id += 1
    response = (
        supabase.table("Questions")
        .insert({"id": curr_id, "Question": question, "Score": score, "Answer": ans})
        .execute()
    )
    print("Insert Response:", response)

def delete_question():
    global curr_id  # Declare that we are using the global variable
    response = (
        supabase.table("Questions")  # Updated to use the "Questions" table
        .delete()
        .eq("id", curr_id)
        .execute()
    )
    print("Delete Response:", response)
    curr_id -= 1

def get_question(question_id):
    response = (
        supabase.table("Questions")
        .select("Question, Score, Answer")
        .eq("id", question_id)
        .execute()
    )
    # Access the data attribute instead of indexing the response directly.
    data = response.data
    if data and len(data) > 0:
        return data[0]  # Return the first (and expected only) row.
    else:
        return None

# Test the functions
# insert_question("What is Your Name?", 10, "true")
# question = get_question(1)
# if question is not None:
#     question_str = question["Question"]  # Question as a string
#     score_int = question["Score"]          # Score as an integer
#     print("Question:", question_str)
#     print("Score:", score_int)
# else:
#     print("No question found.")
