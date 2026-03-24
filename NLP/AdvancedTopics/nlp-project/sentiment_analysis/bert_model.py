# Try to import Transformers and its backends (PyTorch/TF/Flax)
# If it fails (common on Windows DLL issues), we'll fall back to our classical model.
TRANSFORMERS_AVAILABLE = False
try:
    from transformers import pipeline
    # Test if the default sentiment pipeline can be loaded without DLL errors
    _test = pipeline("sentiment-analysis")
    TRANSFORMERS_AVAILABLE = True
except Exception as e:
    print(f"BERT Sentiment Analysis is unavailable on this system: {e}")

def analyze_sentiment_bert(text):
    """
    Deep Learning sentiment analysis using a pre-trained BERT-based model.
    Falls back gracefully if the backend (PyTorch/TF) is missing.
    """
    if not TRANSFORMERS_AVAILABLE:
        return [{"label": "ERROR", "score": 0.0, "message": "BERT Backend (PyTorch) is not working."}]
    
    try:
        classifier = pipeline("sentiment-analysis")
        result = classifier(text)
        return result
    except Exception as e:
        return [{"label": "ERROR", "score": 0.0, "message": str(e)}]

if __name__ == "__main__":
    sample = "This tutorial is incredibly helpful!"
    print(f"BERT Analysis Result: {analyze_sentiment_bert(sample)}")
