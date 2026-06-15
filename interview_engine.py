import json
import random


def get_questions(domain, num_questions=5):

    with open("questions.json", "r") as file:
        data = json.load(file)

    questions = data[domain]

    if len(questions) >= num_questions:
        return random.sample(
            questions,
            num_questions
        )

    return questions


def get_questions_from_skills(skills):

    skill_questions = []

    question_bank = {

        "Python": "What are Python lists and tuples?",

        "OpenCV": "What is OpenCV and where is it used?",

        "Machine Learning": "Explain Machine Learning with examples.",

        "Deep Learning": "What is Deep Learning?",

        "TensorFlow": "What is TensorFlow?",

        "YOLO": "What is YOLO object detection?",

        "MySQL": "What are primary keys in MySQL?",

        "Pandas": "What is Pandas used for?",

        "NumPy": "What is NumPy?",

        "HTML": "What is the difference between HTML and CSS?",

        "CSS": "What is CSS Flexbox?",

        "JavaScript": "What are JavaScript functions?",

        "WordPress": "What is WordPress?",

        "MediaPipe": "What is MediaPipe used for?"
    }

    for skill in skills:

        if skill in question_bank:

            skill_questions.append(
                question_bank[skill]
            )

    if len(skill_questions) > 5:

        skill_questions = random.sample(
            skill_questions,
            5
        )

    return skill_questions