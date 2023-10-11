import fitz

# function to load sample pdf and extract text from it
def readTextFromPdf() :
    doc = fitz.open('sample-resume.pdf')
    text = ""

    for page in doc: 
        text += page.get_text()
    
    return text

