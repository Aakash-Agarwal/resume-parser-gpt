import fitz

def readTextFromPdf() :
    doc = fitz.open('sample-resume.pdf')
    text = ""

    for page in doc: 
        text += page.get_text()
    
    return text

