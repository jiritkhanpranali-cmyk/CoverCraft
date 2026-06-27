from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY


def create_pdf(text):

    filename = "cover_letter.pdf"

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    style = styles["Normal"]
    style.alignment = TA_JUSTIFY
    style.leading = 22

    story = []

    for paragraph in text.split("\n"):

        if paragraph.strip():

            story.append(Paragraph(paragraph, style))
            story.append(Spacer(1, 12))

    doc.build(story)

    return filename