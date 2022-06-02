## how to create a pdf file

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=16)

f = open('demo1.txt', 'r')
for x in f:
    pdf.cell(50, 5, txt=x, ln=3)
pdf.output('text_to_pdf.pdf')