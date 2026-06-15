import json
import random


def get_questions(domain, num_questions=5):
    with open("questions.json", "r") as file:
        data = json.load(file)

    questions = data[domain]

    if len(questions) >= num_questions:
        return random.sample(questions, num_questions)

    return questions