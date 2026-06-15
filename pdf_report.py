from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    candidate_name,
    domain,
    score,
    feedback,
    questions,
    answers
):

    filename = f"results/{candidate_name}_Report.pdf"

    pdf = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Interview Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Candidate: {candidate_name}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Domain: {domain}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Score: {score}/100",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Feedback: {feedback}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    for i in range(len(questions)):

        content.append(
            Paragraph(
                f"<b>Question {i+1}:</b> {questions[i]}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Answer:</b> {answers[i]}",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 8)
        )

    pdf.build(content)

    return filename