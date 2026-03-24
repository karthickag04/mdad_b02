from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Toy Dataset
texts = [
    "I love this product", "Fantastic service", "Best purchase ever",
    "I hate this", "Terrible experience", "Worst service",
    "It's okay I guess", "Not bad but could be better"
]
labels = [1, 1, 1, 0, 0, 0, 1, 0] # 1: Positive, 0: Negative

def train_classical_model():
    # 2. Vectorization (TF-IDF)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    
    # 3. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=42)
    
    # 4. Model Training
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # 5. Evaluation (Practical Addition)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=["Negative", "Positive"])
    
    return model, vectorizer, report

if __name__ == "__main__":
    model, vec, evaluation = train_classical_model()
    print("--- Model Evaluation Report ---")
    print(evaluation)
    
    # Test Prediction
    test_text = vec.transform(["I love AI"])
    prediction = model.predict(test_text)
    print(f"Prediction for 'I love AI': {'Positive' if prediction[0] == 1 else 'Negative'}")
