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

simple_style = ParagraphStyle("Normal", parent=getSampleStyleSheet()["Normal"])
simple_style.textColor = colors.black

simple_style2 = ParagraphStyle("Normal", parent=getSampleStyleSheet()["Normal"])
simple_style2.textColor = colors.gray

small_style = ParagraphStyle("Normal", fontSize=10)
small_style.textColor = colors.ReportLabFidRed


# Read data from CSV and generate PDF
def generate_pdf(csv_filename, pdf_filename):
    data = []

    style = ParagraphStyle(name="Normal", fontSize=25, alignment=1, textColor="#000")

    blueStyle = ParagraphStyle(
        name="Normal", fontSize=16, alignment=0, textColor="#1177aa"
    )

    paragraph = Paragraph(f"GRE Words List<br/><br/><br/><br/>", style=style)

    with open(csv_filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        ins = 0
        for row in csv_reader:
            ins += 1
            if len(row) == 4:
                print(row)
                word, pos, definition, sentence = row
                data.append(Paragraph(f"<b><i>{pos}</i></b>", style=small_style))
                data.append(Paragraph(f"<b>{ins}. {word}</b>:<br/><br/>", style=blueStyle))
                data.append(Paragraph(f"{definition}<br/>", style=simple_style))
                data.append(Paragraph(f"<i>{sentence}</i><br/><br/>",style=simple_style2))

    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    flowables = [paragraph]
    flowables += data

    doc.build(flowables)


if __name__ == "__main__":
    csv_filename = "MoreWords.csv"
    pdf_filename = "Magoosh1000WordsList.pdf"
    generate_pdf(csv_filename, pdf_filename)
