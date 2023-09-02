import json
import requests

def MindMapGenerator():
    def __init__(self, questions, quizzes):
        self.questions = questions
        self.quizzes = quizzes
        self.answers = []
    
    def ask_questions(self):
        for question in self.questions:
            print(f"{question['number']}. {question['text']}")
            if question['type'] == 'Closed':
                for option in question['options']:
                    print(option)
                answer = input("Enter your answer: ")
                self.answers.append({'question': question, 'answer': answer})
            elif question['type'] == 'Open':
                answer = input("Enter your answer: ")
                self.answers.append({'question': question, 'answer': answer})
    
    def ask_quizzes(self):
        for quiz in self.quizzes:
            print(f"{quiz['number']}. {quiz['question']}")
            for i, option in enumerate(quiz['options']):
                print(f"{i+1}. {option}")
            answer = int(input("Enter the number of your answer: ")) - 1
            self.answers.append({'quiz': quiz, 'answer': answer})
            explanations = quiz['explanation'].split('. ')
            if answer == 0:
                print(f"Correct because {explanations[0]}")
            else:
                print(f"Wrong because {explanations[0]}")

    def generate_report(self):
        report = []
        for answer in self.answers:
            if 'question' in answer:
                question = answer['question']
                if question['type'] == 'Closed':
                    options = '\n'.join(question['options'])
                    report.append(f"{question['number']}. {question['text']}\nOptions:\n{options}\nAnswer: {answer['answer']}")
                elif question['type'] == 'Open':
                    report.append(f"{question['number']}. {question['text']}\nAnswer: {answer['answer']}")
            elif 'quiz' in answer:
                quiz = answer['quiz']
                options = '\n'.join(quiz['options'])
                report.append(f"{quiz['number']}. {quiz['question']}\nOptions:\n{options}\nAnswer: {quiz['options'][answer['answer']]}\nExplanation: {quiz['explanation']}")
        return '\n\n'.join(report)




mind_map_generator = MindMapGenerator(questions, quizzes)

# Ask questions
mind_map_generator.ask_questions()

# Ask quizzes
mind_map_generator.ask_quizzes()

# Generate report
report = mind_map_generator.generate_report()
print(report)


