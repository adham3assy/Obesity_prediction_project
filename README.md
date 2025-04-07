# 🧠 Obesity Prediction: A Machine Learning Approach

Welcome to **Obesity Management: A Machine Learning Approach**, a data-driven solution to classify and predict individual obesity levels based on lifestyle, demographic, and medical history features. This project aims to enable personalized health interventions through accurate machine learning predictions.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [ML Pipeline](#ml-pipeline)
- [Results](#results)
- [Usage](#usage)
- [Installation](#installation)
- [Contributors](#contributors)
- [License](#license)

---

## 📖 Overview

Obesity is a major global health challenge with growing prevalence and serious economic implications. Traditional interventions often lack personalization. This project addresses the challenge by developing a machine learning pipeline to predict **NObeyesdad** (obesity levels) based on user input, offering potential for targeted health advice.

---

## 📂 Dataset

- **Source**: Publicly available dataset from [UCI Machine Learning Repository](https://www.kaggle.com/datasets)
- **Target Variable**: `NObeyesdad` – Categorized obesity levels.
- **Features**:
  - Demographics: Gender, Age, Height, Weight
  - Family History
  - Dietary Habits: FAVC, FCVC, NCP, CAEC
  - Physical Activity
  - Daily Lifestyle

---

## 🎯 Features

- **Binary and Categorical Inputs**: Encoded with appropriate transformations.
- **Custom Pipelines**: Using `ColumnTransformer` and `Pipeline` for scalable preprocessing.
- **Feature Selection**: Empirical analysis showed **Weight** and **Family History** as strong predictors.

---

## 🛠️ ML Pipeline

- **Preprocessing**: Label encoding, scaling, null handling.
- **Models Evaluated**:
  - Random Forest
  - Gradient Boosting
  - LightGBM
- **Hyperparameter Tuning**: via `GridSearchCV` and `RandomizedSearchCV`
- **Evaluation Metrics**:
  - Accuracy
  - Precision/Recall
  - Confusion Matrix

> 🎯 **Goal**: Achieve at least **90% accuracy** while reducing false positives by **10%**

---

## 📊 Results

After experimentation:
- Achieved **~90% accuracy** on test data.
- LightGBM yielded the best balance of performance and training time.
- Family history and weight were confirmed as dominant predictors.

---

