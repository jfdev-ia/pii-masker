from PyPDF2 import PdfReader

reader = PdfReader("cvs/cv5.pdf")
page = reader.pages[0]

print(page.extract_text())