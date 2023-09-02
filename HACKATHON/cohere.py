import requests
from dotenv import load_dotenv
import os
import json
from extraction import extract_questions, extract_quizzes
load_dotenv()
# Set your API key and model name
api_key = os.getenv("COHERE_API_KEY")
print(api_key)
model_name = "command"



def get_questions(question):
    # Set the API endpoint and headers
    endpoint = f"https://api.cohere.ai/{model_name}/generate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Set the request body
    body = {
        "prompt": question,
        "max_tokens": 500,
        "temperature": 0.2,
        "n": 1
    }
    # Send the request to Cohere's API
    response = requests.post(endpoint, headers=headers, data=json.dumps(body))
    return response


def genrate_questins(field, specialty, course_length, username):
    generate_questions = f"""[8 questions maximum, 1 question per message, 5-6 closed, 2-3 open]
    Introduction:             
    You are a roadmap specialist tasked with helping {username} create the most effective learning roadmap for {field} in the context of {specialty}. The course will span {course_length} weeks.

    INSTRUCTIONS:
    Your role is to generate questions for each response, the questions will be used to choose the best learning path for him.
    Follow the format below:
    1. (Closed) "Question : a) Option a, b) Option b, c) Option c, d) Option d"
    2. (Open) "Question"
    [optional]

    Examples:
    1. (Closed) "Are you currently employed or a student? : a) Employed, b) Student, c) Not employed, d) Other (please specify)"
    2. (Open) "What motivates you to learn {field}? (Please provide your answer)"
    """



    response = get_questions(generate_questions)
    # Parse the response to extract the generated text
    generated_text = response.json()["text"]
    extracted_questions = extract_questions(generated_text)
    print(extracted_questions)
    if extracted_questions == []:
        print("No questions generated")
        response = get_questions(generate_questions)
        # Parse the response to extract the generated text
        generated_text = response.json()["text"]
        extracted_questions = extract_questions(generated_text)
        print(extracted_questions)


def get_quizzes():
    get_quizzes = f"""Generate 3 quizzes to test the user's knowledge in creating an environment and managing time for their learning path. The quizzes should be in the following format:
    {{
        "question": "What is the most effective way to create a conducive learning environment?",
        "options": [
            "Set up a dedicated study space",
            "Study in a noisy and crowded area",
            "Study while multitasking"
        ],
        "answer": 0,
        "explanation": [
            "having a dedicated study space can help minimize distractions and improve focus.",
        ]
    }}
    """

    response = get_questions(get_quizzes)
    # Parse the response to extract the generated text
    generated_text = response.json()["text"]
    extracted_quizzes = extract_quizzes(generated_text)
    print(extracted_quizzes)
    if extracted_quizzes == []:
        print("No quizzes generated")
        response = get_questions(get_quizzes)
        # Parse the response to extract the generated text
        generated_text = response.json()["text"]
        extracted_quizzes = extract_quizzes(generated_text)
        print(extracted_quizzes)
