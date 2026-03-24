import sys
import os

# --- CRITICAL FIX FOR SHADOWED PACKAGES ---
# Filters out user-level site-packages (like AppData\Roaming\Python)
# This mimics the 'python -s' flag even when Flask restarts/reloads.
sys.path = [p for p in sys.path if "Roaming\\Python" not in p]

# Ensure the project root is in path for local imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify
from text_processing.spacy_pipeline import process_text_spacy
from sentiment_analysis.bert_model import analyze_sentiment_bert, TRANSFORMERS_AVAILABLE
from sentiment_analysis.classical_model import train_classical_model
from chatbot.openai_bot import get_chatbot_response

app = Flask(__name__)

# Initialize the Classical Model as a fallback
print("Initializing Classical ML Fallback...")
classical_model, vec, _ = train_classical_model()

@app.route("/analyze", methods=["POST"])
def analyze_and_chat():
    """
    Endpoint that:
    1. Processes text (spaCy)
    2. Analyzes sentiment (BERT with Classical Fallback)
    3. Gets a response (OpenAI)
    """
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # 1. spaCy Processing
    try:
        processed = process_text_spacy(text)
    except Exception as e:
        processed = [{"error": f"spaCy failed: {str(e)}"}]

    # 2. Sentiment Analysis (BERT -> Fallback to Classical)
    sentiment_result = analyze_sentiment_bert(text)
    
    # If BERT failed/is unavailable, use Classical ML
    if sentiment_result[0]["label"] == "ERROR":
        print("BERT Failed. Falling back to Classical ML...")
        test_vec = vec.transform([text])
        prediction = classical_model.predict(test_vec)[0]
        sentiment_result = [{"label": "POSITIVE" if prediction == 1 else "NEGATIVE", "score": 1.0, "method": "classical_fallback"}]

    # 3. Chatbot Response
    ai_response = get_chatbot_response(f"The user said: '{text}'. Summarize their sentiment.")
    
    return jsonify({
        "processed_tokens": processed[:5], # Return first 5 for brevity
        "sentiment": sentiment_result,
        "assistant_reply": ai_response,
        "status": "success"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ready", "bert_available": TRANSFORMERS_AVAILABLE})

if __name__ == "__main__":
    print("\n--- NLP PROJECT API IS STARTING ---")
    print("Binding to: http://0.0.0.0:5000")
    print("If testing locally, use: http://127.0.0.1:5000")
    # use_reloader=False and debug=False can sometimes help connection reliability on Windows
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
