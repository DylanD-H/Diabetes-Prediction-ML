# Diabetes-Prediction-ML

## Problem Description
Diabetes is a chronic disease that affects how the body regulates blood sugar. Undiagnosed or poorly managed diabetes can lead to serious complications, including heart disease, kidney failure, and nerve damage. Early identification of individuals at risk can help guide timely intervention and lifestyle changes to prevent the disease.

The goal of this project is to build a machine learning model that predicts whether a patient is likely to have diabetes based on measurable health indicators. The [dataset](https://www.kaggle.com/datasets/simaanjali/diabetes-classification-dataset) used in this project includes several clinical and demographic features:

* Age: Older age is associated with increased diabetes risk.
* Gender: Men and women may show different risk patterns for developing diabetes.
* BMI (Body Mass Index): Higher BMI often indicates overweight or obesity, which are major risk factors.
* Chol (Total Cholesterol): Elevated cholesterol levels can contribute to metabolic disorders, including diabetes.
* TG (Triglycerides): High triglyceride levels are linked to insulin resistance.
* HDL (High-Density Lipoprotein): The “good” cholesterol, higher levels can reduce risk.
* LDL (Low-Density Lipoprotein): The “bad” cholesterol, higher levels can increase risk.
* Cr (Creatinine): Indicates kidney function, which can be impaired in diabetic patients.
* BUN (Blood Urea Nitrogen): Another marker of kidney and liver function, potentially linked to diabetes risk.
* Diagnosis: The target variable indicating whether the patient has diabetes.

By analyzing these features, the model aims to classify patients as diabetic or non-diabetic. The resulting predictive model could serve as a decision-support tool for healthcare professionals or wellness applications to help identify at-risk individuals early, prompting further medical evaluation or lifestyle interventions.

## Model Training & Selection
To predict whether a patient has diabetes, several models were trained and evaluated on the dataset.
Each model's hyperparameters were tuned to optimize predictive performance. Since this is a medical classification problem, the F1 score was used as the main evaluation metric during tuning. The F1 score balances precision (avoiding false positives) and recall (avoiding false negatives), which is especially important in healthcare contexts where both types of errors can have serious consequences.
|Model|Accuracy|Precision|Recall|F1|ROC-AUC|
|-----|--------|---------|------|--------|-------|
|Logistic Regression|0.817|0.748|0.800|0.773|0.892|
|Decision Tree|0.793|0.679|**0.888**|0.770|0.852|
|Random Forest|**0.831**|**0.751**|0.848|**0.796**|**0.914**|
|Gradient Boosting|0.823|0.751|0.818|0.783|0.910|

Among all tested models, the Random Forest Classifier achieved the best overall performance, with the highest accuracy (0.831), F1 score (0.796), and ROC-AUC (0.914). This indicates that it provides the most reliable balance between correctly identifying diabetic patients and minimizing false predictions. The Random Forest model was chosen as the final model since it achieved the strongest balance of accuracy and reliability.

## Feature Importance
After training the Random Forest model, feature importance analysis was conducted to identify which variables had the greatest influence on diabetes prediction. The model revealed that Age, HDL, LDL, and BMI were the most significant predictors:
|Feature|Importance|
|-------|----------|
|Age|0.433|
|HDL|0.222|
|LDL|0.197|
|BMI|0.148|

Age was the strongest predictor, which aligns with medical research showing that diabetes risk increases with age. HDL and LDL cholesterol levels also played major roles, indicating that cholesterol levels are closely related to overall metabolic and cardiovascular health. BMI, though slightly less influential, still contributed meaningfully as a measure of body fat and obesity risk.

Because these four features are among the most commonly accessible health metrics, an additional experiment was conducted using only these variables to train a simplified model. Despite using fewer inputs, this reduced model maintained strong performance:
|Metric|Score|
|------|-----|
|Accuracy|0.826|
|Precision|0.783|
|Recall|0.766|
|F1| 0.774|
|ROC-AUC|0.906|

The results show that even with a limited set of features, the model performs comparably to the full-feature version. This suggests that diabetes risk can be estimated fairly accurately using just basic health indicators, making the model potentially useful for lightweight screening tools or preliminary risk assessments accessible to the general public.

## Replicating the Project
1. **Requirements:**
    * Ensure Docker is installed on your machine  

2. **Clone the repository:**
    ```
    git clone https://github.com/DylanD-H/Diabetes-Prediction-ML.git
    cd Diabetes-Prediction-ML
    ```
3. **Build the Docker image:**
    ```
    docker build -t diabetes-prediction .
    ```
    The Dockerfile copies all necessary files and dependencies into the container. The trained model (RandomForestClassifier.bin) is already included. If you prefer to train the model yourself, you can run:
   ```
   python Scripts/train.py
   ```
4. **Run the Docker container:**
   ```
   docker run -it --rm -p 9696:9696 diabetes-prediction
   ```
5. **Test the model:**
   
   From your local machine, run:
   ```
   python Scripts/patient.py
   ```
   This will return the predicted probability that the patient has diabetes. The optimal threshold for classifying a patient as diabetic in this model is 0.45. You can adjust the input numbers in this file to experiment with different patient scenarios.
 
