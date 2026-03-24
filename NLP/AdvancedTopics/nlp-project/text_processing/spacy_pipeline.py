import spacy

# Load the small English model
# Run 'python -m spacy download en_core_web_sm' first
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("spaCy model not found. Downloading...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def process_text_spacy(text):
    """
    Production-ready processing using spaCy:
    - Tokenization
    - Lemmatization (root form)
    - Part-of-Speech (POS) tagging
    - Stopword detection
    """
    doc = nlp(text)
    
    # Filter out punctuation and stopwords, returning lemmas
    results = [
        {
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "is_stop": token.is_stop
        }
        for token in doc if not token.is_punct
    ]
    return results

if __name__ == "__main__":
    sample = "NLP is amazing! It enables machines to understand human language."
    processed = process_text_spacy(sample)
    print("spaCy Processed (First 3 tokens):")
    for p in processed[:3]:
        print(f"  {p['text']} -> {p['lemma']} ({p['pos']})")
