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

## Insights:

### Lunch vs Performance
- Standard lunch helps perform well in exams.
- Standard lunch helps perform well in exams be it a male or a female.
![Lunch vs Performance](https://github.com/magaramol/mlproj_01/raw/main/Images/lunch_02.png)

### Parent's Education vs Performance
- In general parent's education doesn't help students perform well in exams.
- 2nd plot shows that parents whose education is of associate's degree or master's degree, their male child tends to perform well in exams.
- 3rd plot we can see there is no effect of parent's education on female students.
![Parent's Education vs Performance](https://github.com/magaramol/mlproj_01/raw/main/Images/parent_edu.png)

### Race/Ethnicity Distribution
- Most of the students belong to group C / group D.
- The lowest number of students belong to group A.
![Race/Ethnicity Distribution](https://github.com/magaramol/mlproj_01/raw/main/Images/race_ethnicity_01.png)

### Race/Ethnicity vs Performance
- Group E students have scored the highest marks.
- Group A students have scored the lowest marks.
- Students from a lower socioeconomic status have a lower average in all course subjects.
![Race/Ethnicity vs Performance](https://github.com/magaramol/mlproj_01/raw/main/Images/race_ethnicity_02.png)

### Lunch Type vs Performance
- Students who get Standard Lunch tend to perform better than students who got free/reduced lunch.
![Lunch Type vs Performance](https://github.com/magaramol/mlproj_01/raw/main/Images/lunch_01.png)

### Test Preparation vs Performance
- Students who have completed the Test Preparation Course have scores higher in all three categories than those who haven't taken the course.
![Test Preparation vs Performance](https://github.com/magaramol/mlproj_01/raw/main/Images/test_prep_01.png)

### Pair Plot of Scores
- From the above plot, it is clear that all the scores increase linearly with each other.
![Pair Plot of Scores](https://github.com/magaramol/mlproj_01/raw/main/Images/pair_plot.png)

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

## Mlflow Tracking
- MLFLOW_TRACKING_URI=https://dagshub.com/magaramol/mlproj_01.mlflow 
- MLFLOW_TRACKING_USERNAME=magaramol 
- MLFLOW_TRACKING_PASSWORD=********** 
- python app.py

This project aims to provide insights into factors affecting student performance and demonstrate the application of machine learning in education.
