import fitz

def extract_text_from_resume(path_to_resume):
    doc = fitz.open(path_to_resume)
    text=""
    for page in doc:
        text += page.get_text()
    return text
