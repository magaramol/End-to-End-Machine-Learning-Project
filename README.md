# Predicting Student Performance: An End-to-End Machine Learning Project

## Description:
This project aims to predict student performance in exams using the ["Students Performance in Exams"](https://www.kaggle.com/spscientist/students-performance-in-exams) dataset from Kaggle. The dataset contains 1000 entries with 8 attributes, including:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

## Technical Stack:
- Data Loading and Preprocessing: 🐼 pandas
- Exploratory Data Analysis (EDA): 📊 matplotlib
- Feature Engineering: 🛠️
- Model Selection and Training: ⚙️ scikit-learn
- Model Tuning and Optimization: 🔧 mlflow
- Model Deployment: 🚀
- Project Tracking and Collaboration: 🔄 DVC, 📊 dagshub

## Project Outline:
1. **Data Loading and Preprocessing:**
   - Load the dataset using 🐼 pandas and perform basic preprocessing steps such as handling missing values and encoding categorical variables.

2. **Exploratory Data Analysis (EDA):**
   - Use 📊 matplotlib to visualize the dataset and gain insights into the distribution of scores and the relationship between variables.

3. **Feature Engineering:**
   - Create new features or transform existing features to improve the performance of the model.

4. **Model Selection and Training:**
   - Use ⚙️ scikit-learn to select and train machine learning models for predicting student performance.
   - Split the dataset into training and testing sets and evaluate the models using appropriate metrics.

5. **Model Tuning and Optimization:**
   - Use 🔧 mlflow to track the performance of different models and hyperparameters.
   - Use this information to fine-tune the models for better performance.

6. **Model Deployment:**
   - Once a satisfactory model is trained, deploy it using a simple script or framework.
   - Create a basic user interface to interact with the deployed model, if necessary.

7. **Project Tracking and Collaboration:**
   - Use 🔄 DVC to track changes to the dataset and the code.
   - Use 📊 dagshub to collaborate with team members and manage the project workflow.

This project aims to provide insights into factors affecting student performance and demonstrate the application of machine learning in education.



### Mlflow Tracking

MLFLOW_TRACKING_URI=https://dagshub.com/magaramol/mlproj_01.mlflow \
MLFLOW_TRACKING_USERNAME=magaramol \
MLFLOW_TRACKING_PASSWORD=62f6856a26f5f44a037f93f20d04fe8d5e1060b1 \
python script.py