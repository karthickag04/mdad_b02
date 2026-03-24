import os
from dotenv import load_dotenv
from openai import OpenAI

# Load keys from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_chatbot_response(prompt, model="gpt-3.5-turbo"):
    """
    Secure chat completion with role prompting.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful NLP assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)} (Did you set your API key in .env?)"

if __name__ == "__main__":
    # Example usage
    print("Chatbot: ", get_chatbot_response("Explain why spaCy is used in production NLP."))
