from flask import Flask, request, jsonify
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

def preprocess_text(text):
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

def calculate_similarity(text1, text2):
    preprocessed_text1 = preprocess_text(text1)
    preprocessed_text2 = preprocess_text(text2)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([preprocessed_text1, preprocessed_text2])
    
    similarity_matrix = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    
    return similarity_matrix[0][0]

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    data = request.get_json()
    text1 = data['text1']
    text2 = data['text2']
    
    similarity = calculate_similarity(text1, text2)
    
    return jsonify({'similarity': similarity * 100})  # Multiply by 100 to get a percentage

if __name__ == '__main__':
    app.run(debug=True)
