# 🧠 Obesity Prediction: A Machine Learning Approach

Welcome to **Obesity Management: A Machine Learning Approach**, a data-driven solution to classify and predict individual obesity levels based on lifestyle, demographic, and medical history features. This project aims to enable personalized health interventions through accurate machine learning predictions.

---

## 📌 Table of Contents:

- [Overview](#Overview)
- [Dataset](#Dataset)
- [Features](#Features)
- [ML Pipeline](#Ml-pipeline)
- [Results](#Results)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#Contributors)
- [Model Details](#Model-Details)
- [License](#license)

---

## 📖 Overview:

Obesity is a major global health challenge with growing prevalence and serious economic implications. Traditional interventions often lack personalization. This project addresses the challenge by developing a machine learning pipeline to predict **NObeyesdad** (obesity levels) based on user input, offering potential for targeted health advice.

---

## Dataset:

- **Source**: Publicly available dataset from [UCI Machine Learning Repository](https://www.kaggle.com/datasets)
- **Target Variable**: `NObeyesdad` – Categorized obesity levels.
- **Features**:
  - Demographics: Gender, Age, Height, Weight
  - Family History
  - Dietary Habits: FAVC, FCVC, NCP, CAEC
  - Physical Activity
  - Daily Lifestyle

---

## Features:

- **Binary and Categorical Inputs**: Encoded with appropriate transformations.
- **Custom Pipelines**: Using `ColumnTransformer` and `Pipeline` for scalable preprocessing.
- **Feature Selection**: Empirical analysis showed **Weight** and **Family History** as strong predictors.

---

## ML Pipeline:

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

## Results:

After experimentation:
- Achieved **~90% accuracy** on test data.
- LightGBM yielded the best balance of performance and training time.
- Family history and weight were confirmed as dominant predictors.

---

## Installation:
1. Clone the repository:
   ```bash
   [git clone https://github.com/Israa/prediction-of-obesity-risk.git](https://github.com/IsraaAbdelghany9/Prediction-of-Obesity-Risk.git)
   ```
2. Navigate to the project directory:
   ```bash
   cd Prediction-of-Obesity-Risk
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage:
1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook prediction-of-obesity-risk-iti-project.ipynb
   ```
2. Follow the steps in the notebook to preprocess the data, train the model, and evaluate its performance.


## Contributors:
1. Amr Alaa: [GitHub](https://github.com/Amrokahla)- [LinkedIn](https://www.linkedin.com/in/amr-kahla-9447841a7/)
2. Ali Adel: [GitHub](https://github.com/adelian14) - [LinkedIn](https://www.linkedin.com/in/ali-adel-84b390101/)  
3. Adham Assy: [GitHub](https://github.com/adham3assy) - [LinkedIn](https://www.linkedin.com/in/adham-assy/)
4. Israa Abdelghany: [GitHub](https://github.com/IsraaAbdelghany9) - [LinkedIn](https://www.linkedin.com/in/israa-abdelghany/)

## Model Details:
The project uses the LightGBM (LGBM) model for prediction. LightGBM is a gradient boosting framework that is efficient and scalable for large datasets. The model is trained on preprocessed data and evaluated using metrics such as accuracy, precision, recall, and F1-score.

## License:
This project is licensed under the Apache2.0 License. See the LICENSE file for details.



