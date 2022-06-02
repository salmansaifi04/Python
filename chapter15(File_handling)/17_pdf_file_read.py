import PyPDF2

## creating a pdf file object

pdf_file_obj = open('text_to_pdf.pdf', 'rb')

## creating a pdf reader object

pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

## printing number of pages in pdf file

print(pdf_reader.numPages)

## creating a page object

pageobj = pdf_reader.getPage(0)

## extracting text from page

print(pageobj.extractText())