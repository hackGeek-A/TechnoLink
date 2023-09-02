import re
from typing import List, Dict

def extract_quizzes(text):
    quizzes = []
    quiz_pattern = r'(\d+)\. (.*?)\nOptions: (.*?)\nAnswer: (.*?)\nExplanation: (.*?)(?=\n|$)'
    for match in re.finditer(quiz_pattern, text, re.DOTALL):
        quiz = {}
        quiz['number'] = int(match.group(1))
        quiz['question'] = match.group(2)
        quiz['options'] = [option.strip() for option in match.group(3).split(',')]
        quiz['answer'] = match.group(4)
        quiz['explanation'] = match.group(5)
        quizzes.append(quiz)
    return quizzes


def extract_questions(text):
    questions = []
    question_pattern = r'(\d+)\. \((.*?)\) (.*?):(.*?)(?=\n|$)'
    for match in re.finditer(question_pattern, text, re.DOTALL):
        question = {}
        question['number'] = int(match.group(1))
        question['type'] = match.group(2)
        question['text'] = match.group(3)
        if question['type'] == 'Closed':
            question['options'] = [option.strip() for option in match.group(4).split(',')]
        questions.append(question)
    return questions


def extract_calendar(text):
    calendar = {}
    pattern = r"\(Week (\d+)\)\(Day (\d+)\) ([\d:-]+[ap]m) - ([\d:-]+[ap]m): (.+)"
    for match in re.finditer(pattern, text):
        week, day, start_time, end_time, event = match.groups()
        week = int(week)
        day = int(day)
        if week not in calendar:
            calendar[week] = {}
        if day not in calendar[week]:
            calendar[week][day] = []
        calendar[week][day].append({
            "start_time": start_time,
            "end_time": end_time,
            "event": event
        })
    return calendar


def extract_text(text: str) -> Dict[str, List[Dict[str, str]]]:
    # Extract the week and day information from the text
    weeks = re.findall(r'\(Week\s*(\d+)\)', text)
    days = re.findall(r'\(Week\s*(\d+)\)(.+?)(?=\(Week|\Z)', text, re.DOTALL)
    
    # Create a dictionary to store the extracted information grouped by week
    result = {}
    for week in days:
        week_num, week_days = week
        if week_num not in result:
            result[week_num] = []
        days = re.findall(r'\(Day\s*(\d+)\)\s*(\d+:\d+\w+)\s*-\s*(\d+:\d+\w+):\s*(.+)', week_days)
        for day in days:
            day_num, start_time, end_time, event_name = day
            result[week_num].append({
                'day': day_num,
                'start_time': start_time,
                'end_time': end_time,
                'event_name': event_name.strip()
            })
    return result




