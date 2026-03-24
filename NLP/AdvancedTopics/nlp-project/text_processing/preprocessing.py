import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure resources are available
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def clean_text_nltk(text):
    """
    Educational preprocessing using NLTK:
    - Lowercasing
    - Tokenization
    - Noise & Stopword Removal
    """
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    cleaned = [w for w in tokens if w.isalnum() and w not in stop_words]
    return cleaned

if __name__ == "__main__":
    sample = "NLP is amazing! It enables machines to understand human language."
    print(f"NLTK Cleaned: {clean_text_nltk(sample)}")
