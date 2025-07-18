from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.text_utils import preprocess

def detect_plagiarism(input_text, reference_text):
    input_clean = preprocess(input_text)
    reference_clean = preprocess(reference_text)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([input_clean, reference_clean])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return float(similarity[0][0])