import spacy
import re

nlp=spacy.load("en_core_web_sm")
def preprocess_text(text): 
    doc=nlp(text)
    clean_tokens=[]
    # phone_number= re.findall(r'(?:\+91|91)?[-\s]?[6-9]\d{9}', text)
    # email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    for token in doc:
        if not token.is_stop and not token.is_punct:
            clean_tokens.append(token.lemma_.lower())
    # print("Email:", email)
    # print("Phone number:", phone_number)
    return " ".join(clean_tokens)