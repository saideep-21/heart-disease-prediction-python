import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('path of trained_model.sav', 'rb'))

# Function for prediction
def heart_disease_prediction(input_data):
    # Convert input data to numpy array & reshape
    input_data_as_array_reshape = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_data_as_array_reshape)

    if (prediction[0] == 0):
        return '✅ The Person does NOT have Heart Disease'
    else:
        return '⚠️ The Person HAS Heart Disease'


# Main function for Streamlit UI
def main():
    st.title("❤️ Heart Disease Prediction App")

    # Collect user input
    st.subheader("Enter Patient Details:")
    age = st.text_input("Age (in years)")
    sex = st.text_input("Sex (0 = Female, 1 = Male)")
    cp = st.text_input("Chest Pain Type (0–3)")
    trestbps = st.text_input("Resting Blood Pressure (in mm Hg)")
    chol = st.text_input("Serum Cholesterol (in mg/dl)")
    fbs = st.text_input("Fasting Blood Sugar (>120 mg/dl: 1, else: 0)")
    restecg = st.text_input("Resting ECG Results (0–2)")
    thalach = st.text_input("Maximum Heart Rate Achieved")
    exang = st.text_input("Exercise Induced Angina (1 = Yes, 0 = No)")
    oldpeak = st.text_input("ST Depression induced by exercise")
    slope = st.text_input("Slope of the peak exercise ST segment (0–2)")
    ca = st.text_input("Number of major vessels (0–3)")
    thal = st.text_input("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)")

    Prediction = ""

    # Prediction button
    if st.button("🔍 Get Prediction"):
        try:
            # Convert all inputs to float
            input_values = [
                float(age), float(sex), float(cp), float(trestbps),
                float(chol), float(fbs), float(restecg), float(thalach),
                float(exang), float(oldpeak), float(slope), float(ca), float(thal)
            ]
            Prediction = heart_disease_prediction(input_values)

        except ValueError:
            Prediction = "⚠️ Please enter valid numeric values."

    # Display result
    st.success(Prediction)


if __name__ == '__main__':
    main()