import os
from supabase import create_client, Client

# Hardcoding for development; consider using environment variables properly
url: str = "https://zcfuychanpnrfkhiqhes.supabase.co"  # Replace with os.environ.get("SUPABASE_URL") if needed
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpjZnV5Y2hhbnBucmZraGlxaGVzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDMzOTc1MTEsImV4cCI6MjA1ODk3MzUxMX0.47aIljB6bc-Z1bBD_Eud2A6VlRZrz_Q34BEIxldEk3U"  # Replace with os.environ.get("SUPABASE_KEY") if needed
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
        .select("Question, Score")
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
