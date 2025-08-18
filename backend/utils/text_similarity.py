from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_tfid_similarity(resume_text, jd_text):
    tfid = TfidfVectorizer(input='content')
    
    result = tfid.fit_transform([resume_text, jd_text])
    similarity_score =  cosine_similarity(result)[0,1]       
    return round(similarity_score *100, 2)