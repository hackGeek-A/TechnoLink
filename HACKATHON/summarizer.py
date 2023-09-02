import requests
from dotenv import load_dotenv
import os
import json
from extraction import extract_calander
load_dotenv()
# Set your API key and model name
api_key = os.getenv("COHERE_API_KEY")
print(api_key)
model_name = "command"

def get_summary(question , temp):
    # Set the API endpoint and headers
    endpoint = f"https://api.cohere.ai/{model_name}/generate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Set the request body
    body = {
        "prompt": question,
        "max_tokens": 900,
        "temperature": temp,
        "n": 1
    }
    # Send the request to Cohere's API
    response = requests.post(endpoint, headers=headers, data=json.dumps(body))
    return response

def summarize_rport ():
    report_prompt = """“Given the user’s responses to the questions about their level of knowledge, learning style, 
    preferred learning environment, budget, goals, and previous experience with Cyber Security, 
    construct a dictionary that represents their preferences. The dictionary should contain key-value pairs that 
    represent the user’s responses to each question. The keys should be descriptive and easy to understand, 
    and the values should accurately reflect the user’s responses:
    1. "What is your current level of knowledge in Cyber Security?
    Options:
    a) Beginner
    b) Intermediate
    c) Advanced
    d) Other (please specify)"
    Answer: a

    2. "What is your learning style?
    Options:
    a) Visual
    b) Auditory
    c) Kinesthetic
    d) Other (please specify)"
    Answer: a

    3. "What is your preferred learning environment?
    Options:
    a) Online
    b) In-person
    c) Both
    d) Other (please specify)"
    Answer: a

    4. "What is your budget for the course?
    Options:
    a) $0-$100
    b) $101-$500
    c) $501-$1000
    d) $1001-$5000
    e) $5001-$10000
    f) Other (please specify)"
    Answer: a

    5. "What are your goals for the course?
    Options:
    a) Learn the basics of Cyber Security
    b) Advance your current knowledge
    c) Get a job in the field
    d) Other (please specify)"
    Answer: get a job

    6. "What are your concerns about the course? (Please provide your answer)"
    7. (Closed) "Do you have any previous experience with online learning?
    Answer: don't know

    8. "Do you have any previous experience with Cyber Security?
    Options:
    a) Yes
    b) No"
    Answer: no


    """

    response = get_summary(report_prompt , 0.7)
    # Parse the response to extract the generated text
    generated_text = response.json()["text"]
    print(generated_text)

def get_calendar(course_length, generated_text):
    
    get_calendar = f"""[just give times, no subject nither names are required] 
    Generate a calnder for a {course_length} week course and the user have mentioned these preferences:
    {generated_text}\n
    The calendar should be in the following format example:
    (Week 1)(Day 1) 10:00am - 11:00am: Lecture 1
    """

    response = get_summary(get_calendar, 0.2)
    # Parse the response to extract the generated text
    generated_calander = response.json()["text"]
    extracted_calendar = extract_calander(generated_calander)
    print(extracted_calendar)
