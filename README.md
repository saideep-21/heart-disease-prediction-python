\# ❤️ Heart Disease Prediction using Logistic Regression (from Scratch \& Deployment)



\## 🔹 One-line Summary

An end-to-end project implementing \*\*logistic regression from scratch\*\* for predicting heart disease, achieving \*\*85% training accuracy\*\* and \*\*80% test accuracy\*\*, and deployed with \*\*Streamlit\*\* for real-time user predictions.



---



\## 📑 Table of Contents

1\. \[Overview](#overview)  

2\. \[Problem Statement](#problem-statement)  

3\. \[Dataset](#dataset)  

4\. \[Tools \& Technologies](#tools--technologies)  

5\. \[Methods](#methods)  

6\. \[Key Insights](#key-insights)  

7\. \[Model \& Outputs](#model--outputs)  

8\. \[How to Run This Project](#how-to-run-this-project)  

9\. \[Results \& Conclusion](#results--conclusion)  

10\. \[Future Work](#future-work)  

11\. \[Author \& Contact](#author--contact)  



---



\## 📖 Overview

This project aims to predict whether a person has heart disease based on clinical features such as age, cholesterol level, blood pressure, and more.  

The workflow includes \*\*data preprocessing, logistic regression (implemented from scratch), model evaluation, and deployment\*\*.



---



\## ❓ Problem Statement

Heart disease is one of the leading causes of death worldwide.  

Accurate and early prediction of heart disease can assist healthcare professionals in decision-making and treatment planning.  

This project builds a \*\*predictive ML model from scratch\*\* and provides a \*\*user-friendly web interface\*\* for predictions.



---



\## 📊 Dataset

\- \*\*Source:\*\* UCI Heart Disease Dataset (via Kaggle/online repositories)  

\- \*\*Size:\*\* 303 records × 14 attributes  

\- \*\*Features:\*\*

&nbsp; - Age, Sex, Chest Pain Type, Resting BP, Cholesterol, Fasting Blood Sugar, Resting ECG, Max Heart Rate, Exercise Angina, Oldpeak, Slope, Number of vessels, Thalassemia

\- \*\*Target:\*\* `0 = No Disease`, `1 = Disease`



---



\## 🛠 Tools \& Technologies

\- \*\*Languages:\*\* Python  

\- \*\*Libraries:\*\* NumPy, Pandas, Matplotlib, scikit-learn, Streamlit  

\- \*\*Deployment:\*\* Streamlit Web App  

\- \*\*Version Control:\*\* Git \& GitHub  



---



\## 🔎 Methods

1\. Data Loading \& Exploration  

2\. Null Value \& Data Type Checks  

3\. Feature Scaling using StandardScaler  

4\. Logistic Regression (implemented from scratch: gradient descent, sigmoid function, loss function)  

5\. Model Training \& Cost Function Visualization  

6\. Accuracy Evaluation (Train \& Test)  

7\. Model Saving with Pickle  

8\. Deployment using Streamlit  



---



\## 📈 Key Insights

\- Training Accuracy: \*\*85%\*\*  

\- Test Accuracy: \*\*80%\*\*  

\- Cost function plot shows \*\*smooth convergence\*\*, indicating stable training.  

\- Features such as \*\*age, chest pain type, cholesterol, and max heart rate\*\* strongly influenced predictions.  



---



\## 🤖 Model \& Outputs

\- \*\*Cost Function Trend:\*\*  

&nbsp; !\[Cost Function](Outputs/cost\_function\_plot.png)  



\- \*\*Streamlit UI Screenshot:\*\*  

&nbsp; !\[App Screenshot](Images/streamlit\_app\_screenshot.png)  



\- \*\*Pickle Model File:\*\* `trained\_model.sav`



---



\## 🚀 How to Run This Project



\### 🔧 Step 1: Clone Repository

```bash

git clone https://github.com/yourusername/heart-disease-prediction-python.git

cd heart-disease-prediction-python



\### 🔧 Step 2: Install Dependencies

```bash
pip install -r Requirements.txt



\### 🔧 Step 3: Run Jupyter Notebook (Optional, for training)

```bash
jupyter notebook Notebooks/heart\_disease\_prediction.ipynb



\### 🔧 Step p 4: Run Streamlit App

```bash
streamlit run Scripts/streamlit\_app.py



---



\## ✅ Results \& Conclusion



* Successfully implemented logistic regression from scratch with competitive accuracy.
* Built an interactive web app for real-time predictions.
* Demonstrated the importance of data preprocessing and gradient descent optimization.
  

---



\## 🔮 Future Work



* Improve accuracy with advanced models (Random Forest, XGBoost, Neural Nets).
* Hyperparameter tuning.
* Deployment on cloud platforms (Heroku/AWS/GCP) for public access.
* Enhanced UI with better visualizations and patient risk scoring.
  

---



\## 👨‍💻 Author \& Contact



Golla Sai Deep

📧 Email: saideepcct@gmail.com

🔗 LinkedIn: Your LinkedIn Profile

🔗 GitHub: Your GitHub Profile





