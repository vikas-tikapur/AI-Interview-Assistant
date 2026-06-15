import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from interview_engine import get_questions
from score_manager import (
    save_results,
    calculate_score,
    generate_feedback
)

# -------------------------
# Global Variables
# -------------------------

current_questions = []
current_index = 0
answers = []

# -------------------------
# Functions
# -------------------------

def start_interview():
    global current_questions
    global current_index
    global answers

    name = name_entry.get()
    domain = domain_combo.get()

    if name == "" or domain == "":
        messagebox.showerror(
            "Error",
            "Please enter name and select domain."
        )
        return

    current_questions = get_questions(domain)
    current_index = 0
    answers = []

    question_label.config(
        text=f"Question: {current_questions[current_index]}"
    )

    counter_label.config(
        text=f"Question {current_index + 1}/5"
    )

    answer_text.delete("1.0", tk.END)


def next_question():
    global current_index
    global answers

    if not current_questions:
        return

    answer = answer_text.get("1.0", tk.END).strip()
    answers.append(answer)

    answer_text.delete("1.0", tk.END)

    current_index += 1

    if current_index >= len(current_questions):

        candidate_name = name_entry.get()
        domain = domain_combo.get()

        save_results(
            candidate_name,
            current_questions,
            answers,
            domain
        )

        score = calculate_score(answers)
        feedback = generate_feedback(score)

        question_label.config(
            text="Interview Completed!"
        )

        counter_label.config(
            text="5/5"
        )

        messagebox.showinfo(
            "Interview Result",
            f"Interview Completed!\n\n"
            f"Score: {score}/100\n\n"
            f"{feedback}"
        )

        return

    question_label.config(
        text=f"Question: {current_questions[current_index]}"
    )

    counter_label.config(
        text=f"Question {current_index + 1}/5"
    )


# -------------------------
# GUI
# -------------------------

root = tk.Tk()
root.title("AI Interview Assistant")
root.geometry("700x550")

title = tk.Label(
    root,
    text="AI Interview Assistant",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

name_label = tk.Label(root, text="Candidate Name")
name_label.pack()

name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

domain_label = tk.Label(root, text="Select Domain")
domain_label.pack()

domain_combo = ttk.Combobox(
    root,
    values=["Python", "AI_ML", "Computer_Vision"],
    state="readonly"
)
domain_combo.pack(pady=5)

start_btn = tk.Button(
    root,
    text="Start Interview",
    width=20,
    command=start_interview
)
start_btn.pack(pady=20)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    wraplength=500
)
question_label.pack(pady=20)

counter_label = tk.Label(
    root,
    text="Question 0/5",
    font=("Arial", 10)
)
counter_label.pack()

answer_label = tk.Label(
    root,
    text="Your Answer",
    font=("Arial", 12)
)
answer_label.pack()

answer_text = tk.Text(
    root,
    height=5,
    width=50
)
answer_text.pack(pady=10)

next_btn = tk.Button(
    root,
    text="Next Question",
    width=20,
    command=next_question
)
next_btn.pack(pady=10)

root.mainloop()