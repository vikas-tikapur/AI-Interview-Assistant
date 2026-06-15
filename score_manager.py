import csv
import os


def calculate_score(answers):

    total_words = 0

    for answer in answers:
        total_words += len(answer.split())

    average_words = total_words / len(answers)

    if average_words >= 20:
        return 90

    elif average_words >= 15:
        return 75

    elif average_words >= 10:
        return 60

    elif average_words >= 5:
        return 40

    return 20


def generate_feedback(score):

    if score >= 80:
        return (
            "Excellent Performance!\n"
            "✓ Strong communication skills\n"
            "✓ Good technical explanations\n"
            "✓ Ready for advanced interviews"
        )

    elif score >= 60:
        return (
            "Good Performance!\n"
            "✓ Basic concepts are clear\n"
            "✓ Improve answer explanations\n"
            "✓ Add more practical examples"
        )

    elif score >= 40:
        return (
            "Average Performance\n"
            "✓ Need more detailed answers\n"
            "✓ Practice technical concepts\n"
            "✓ Improve confidence"
        )

    return (
        "Needs Improvement\n"
        "✓ Answers are too short\n"
        "✓ Practice fundamentals\n"
        "✓ Explain concepts with examples"
    )


def save_results(candidate_name, questions, answers, domain):

    score = calculate_score(answers)
    feedback = generate_feedback(score)

    filename = f"results/{candidate_name}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write(f"Candidate: {candidate_name}\n")
        file.write(f"Domain: {domain}\n")
        file.write(f"Score: {score}/100\n\n")

        file.write("Feedback:\n")
        file.write(feedback)
        file.write("\n\n")

        for i in range(len(questions)):

            file.write(
                f"Question {i+1}: {questions[i]}\n"
            )

            file.write(
                f"Answer: {answers[i]}\n"
            )

            file.write(
                "\n---------------------------------\n\n"
            )

    csv_file = "results/interview_results.csv"

    file_exists = os.path.isfile(csv_file)

    with open(csv_file, "a", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        if not file_exists:
            writer.writerow(
                ["Candidate", "Domain", "Score"]
            )

        writer.writerow(
            [candidate_name, domain, score]
        )

    return score