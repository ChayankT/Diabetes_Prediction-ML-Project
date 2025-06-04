# Diabetes_Prediction-ML-Project

This is a Machine Learning project that predicts whether a person is diabetic or not using medical attributes from the Pima Indians Diabetes dataset.

## 📌 Overview
The project uses a **Support Vector Machine (SVM)** classifier from scikit-learn to build a prediction model. The dataset is preprocessed with feature scaling (`StandardScaler`) and evaluated using accuracy score.

## 🧰 Technologies Used
- Python
- NumPy
- Pandas
- scikit-learn

## 📁 Dataset
Dataset: [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)  
Filename: `diabetes.csv`

## 🧪 Steps Performed
1. **Data Loading and Exploration** using `pandas`
2. **Feature Scaling** using `StandardScaler`
3. **Train-Test Split** using `train_test_split`
4. **Model Training** using `sklearn.svm.SVC`
5. **Model Evaluation** using `accuracy_score`


## 🚀 How to Run

```bash
# 1. Clone the Repository
git clone https://github.com/your-username/Diabetes_Prediction-ML-Project.git
cd Diabetes_Prediction-ML-Project

# 2. Install Dependencies
pip install -r requirements.txt

# If you don’t have a requirements.txt yet, create one:
# pip freeze > requirements.txt
# Or manually install:
# pip install numpy pandas scikit-learn

# 3. Run the Code

# Option A: If you're using a Jupyter Notebook
jupyter notebook
# Then open diabetes_predictor.ipynb and run all cells

# Option B: If you're using a Python script
python diabetes_predictor.py
