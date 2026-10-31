

import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🎗️",
    layout="wide"
)

# Load the trained model and scaler
@st.cache_resource
def load_model():
    with open("knn_cancer_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    with open("scaler.pkl", "rb") as scaler_file:
        scaler = pickle.load(scaler_file)

    return model, scaler


loaded_model, loaded_scaler = load_model()

# Feature names
feature_names = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
    "smoothness_mean", "compactness_mean", "concavity_mean",
    "concave points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se",
    "smoothness_se", "compactness_se", "concavity_se",
    "concave points_se", "symmetry_se", "fractal_dimension_se",
    "radius_worst", "texture_worst", "perimeter_worst", "area_worst",
    "smoothness_worst", "compactness_worst", "concavity_worst",
    "concave points_worst", "symmetry_worst", "fractal_dimension_worst"
]

# Application title
st.title("🎗️ Breast Cancer Prediction")
st.write(
    "Enter the 30 diagnostic measurements to run the trained "
    "machine-learning model."
)

st.info(
    "Educational demonstration only. This model is not a medical "
    "diagnostic tool."
)

# Input form
with st.form("prediction_form"):

    st.subheader("Enter Feature Values")

    input_values = {}

    # Display inputs in three columns
    columns = st.columns(3)

    for i, feature in enumerate(feature_names):
        with columns[i % 3]:
            label = feature.replace("_", " ").title()

            input_values[feature] = st.number_input(
                label,
                min_value=0.0,
                value=0.0,
                step=0.01,
                format="%.6f",
                key=feature
            )

    submitted = st.form_submit_button(
        "Predict",
        type="primary",
        use_container_width=True
    )

# Prediction
if submitted:
    try:
        input_data = np.array(
            [[input_values[feature] for feature in feature_names]],
            dtype=float
        )

        # Scale input using the existing scaler
        input_scaled = loaded_scaler.transform(input_data)

        # Predict class
        prediction = loaded_model.predict(input_scaled)[0]

        # Class probabilities
        probabilities = loaded_model.predict_proba(input_scaled)[0]

        # Find the probability corresponding to the predicted class
        predicted_index = list(loaded_model.classes_).index(prediction)
        confidence = probabilities[predicted_index] * 100

        # Update these labels if your model uses different class encodings
        labels = {
            0: "Benign",
            1: "Malignant"
        }

        result = labels.get(prediction, str(prediction))

        st.subheader("Prediction Result")

        if result == "Benign":
            st.success(f"Model prediction: {result}")
        elif result == "Malignant":
            st.error(f"Model prediction: {result}")
        else:
            st.warning(f"Model prediction: {result}")

        st.metric(
            "Model-estimated class probability",
            f"{confidence:.2f}%"
        )

        st.caption(
            "This percentage is the model's estimated probability for "
            "its predicted class, not a person's probability of having cancer. "
            "It should not be interpreted as a clinical diagnosis."
        )

    except Exception as e:
        st.error(f"Error processing input: {e}")
