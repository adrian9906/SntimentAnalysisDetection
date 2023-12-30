import fitz

def extractText(pdfPath):
    textPdf = []
    
    doc = fitz.open(pdfPath)
    
    for page in doc:
        text = page.get_text()
        textPdf+= text
    
    return textPdf