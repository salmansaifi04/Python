## how to read docx file

import docx
doc = docx.Document('first.docx')
all = doc.paragraphs
for i in all:
    print(i.text)