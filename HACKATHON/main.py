from cohere import get_questions , get_quizzes
from extraction import extract_questions , extract_calendar , extract_quizzes
from summarizer import get_summary
from Calander import create_calendar
from QandA import MindMapGenerator

# Enter Field , Specialty , Course Length , Username
field = input("Enter Field: ")
specialty = input("Enter Specialty: ")
course_length = input("Enter Course Length: ")
username = input("Enter Username: ")

questions = get_questions(field, specialty, course_length, username)
quizzes = get_quizzes()

genrate_answers = MindMapGenerator(questions, quizzes)
genrate_answers.ask_questions()
genrate_answers.ask_quizzes()
print(genrate_answers.generate_report())
report = genrate_answers.generate_report()

summary = get_summary(report , 0.2)
print(summary)
extracted_calendar = extract_calendar(summary)
print(extracted_calendar)
create_calendar(extracted_calendar)

