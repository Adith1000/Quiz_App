from groq import Groq
import json
import sys
import os
from Control import data

# Absolute path to the folder that contains api_keys.py
module_path = os.path.abspath("/Users/adithshetty/Desktop/Programming Folder/Quiz App/Quiz_App")
if module_path not in sys.path:
    sys.path.insert(0, module_path)

import api_keys

client = Groq(api_key=api_keys.groq_api_key)


def generate_questions(contents):
    prompt="""Please read the following syllabus and generate exactly 10 true/false questions that test the knowledge expected from the syllabus. The questions should evaluate understanding, application, and analysis of the key concepts rather than simply asking for details stated verbatim in the syllabus. Arrange the questions in increasing order of difficulty (the first question should be the easiest and the last one the most challenging).
    For the output, provide the questions and answers in JSON format as an array of objects. Each object should have two keys: "question" and "answer". The "answer" should be either "True" or "False". Do not include any additional text or commentary outside of this JSON array.

    Example output format:
        [
            {
                "question": "Sample question 1?",
                "answer": "True"
            },
            {
                "question": "Sample question 2?",
                "answer": "False"
            }
            // ... more questions
            ]""" + f"""Syllabus:{contents}"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        top_p=1,
        stream=False
    )

    return response.choices[0].message.content


def store_questions(output_str):
    # Parse the JSON string into a Python list of dictionaries
    question_list = json.loads(output_str)

    # Create a dictionary mapping each question (string) to its answer (string)
    question_map = {item["question"]: item["answer"] for item in question_list}

    return question_map

def store_database(question_map):
    for question, answer in question_map.items():
        data.insert_question(question, 10, answer)


def run(file_path):
    with open(file_path, "r") as file:
        contents = file.read()

    llm_output=generate_questions(contents)
    question_map=store_questions(llm_output)
    store_database(question_map)

