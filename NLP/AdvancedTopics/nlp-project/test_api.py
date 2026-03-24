import requests

def test_nlp_api(text):
    url = "http://127.0.0.1:5000/analyze"
    health_url = "http://127.0.0.1:5000/health"
    payload = {"text": text}
    
    try:
        # Check health first
        health_check = requests.get(health_url)
        if health_check.status_code == 200:
            print(f"Server Health: {health_check.json()}")
        
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Testing with: '{text}' ---")
            print(f"Sentiment: {data['sentiment'][0]['label']} (Method: {data['sentiment'][0].get('method', 'BERT')})")
            print(f"Tokens: {[t['lemma'] for t in data['processed_tokens']]}")
            print(f"AI Assistant: {data['assistant_reply']}\n")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed to connect to API: {e}")

if __name__ == "__main__":
    test_nlp_api("I love learning NLP, it is so much fun!")
    test_nlp_api("This installation was a bit difficult but I'm glad it works now.")
