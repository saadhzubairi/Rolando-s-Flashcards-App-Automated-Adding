import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Define the style for bold text
bold_style = getSampleStyleSheet()["Heading1"]
bold_style.textColor = colors.darkblue

# Define the style for italic text
italic_style = ParagraphStyle("ItalicStyle", parent=getSampleStyleSheet()["Normal"])
italic_style.textColor = colors.black
italic_style.fontName = "Italic"


# Read data from CSV and generate PDF
def generate_pdf(csv_filename, pdf_filename):
    data = []

    style = ParagraphStyle(name="Normal", fontSize=25, alignment=1, textColor="#000")

    blueStyle = ParagraphStyle(
        name="Normal", fontSize=16, alignment=0, textColor="#1177aa"
    )

    paragraph = Paragraph(f"GRE Words List<br/><br/><br/><br/>", style=style)

    with open(csv_filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        ins = 0
        for row in csv_reader:
            ins += 1
            if len(row) == 3:
                word, definition, _ = row
                data.append(Paragraph(f"<b>{ins}. {word}</b>:<br/><br/>", style=blueStyle))
                data.append(Paragraph(f"<i>{definition}</i><br/><br/>"))

    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    flowables = [paragraph]
    flowables += data

    doc.build(flowables)


if __name__ == "__main__":
    csv_filename = "output.csv"
    pdf_filename = "words.pdf"
    generate_pdf(csv_filename, pdf_filename)
