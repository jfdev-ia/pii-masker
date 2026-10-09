from PyPDF2 import PdfReader

def extract_text(pdfFile):
    reader = PdfReader(pdfFile)
    page = reader.pages[0]
    text = page.extract_text()
    return text
    