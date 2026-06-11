# Sales Prediction Using Machine Learning

## Project Overview

This project predicts product sales based on advertising budgets allocated across TV, Radio, and Newspaper platforms using a Linear Regression Machine Learning model. The project includes data preprocessing, exploratory data analysis (EDA), feature importance analysis, model evaluation, future sales prediction, and deployment using Streamlit.

---

## Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Correlation Analysis
* Feature Importance Analysis
* Linear Regression Model Training
* Model Evaluation using MAE, MSE, and R² Score
* Future Sales Prediction
* Interactive Streamlit Web Application

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Jupyter Notebook

---

## Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

---

## Project Structure

```text
Sales-Prediction-ML/
│
├── Advertising.csv
├── Sales_Prediction.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Sales-Prediction-ML.git
cd Sales-Prediction-ML
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter Notebook

Open the notebook and run all cells:

```text
Sales_Prediction.ipynb
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open automatically in your browser at:

```text
http://localhost:8501
```

---

## Results

* Successfully developed a Linear Regression model for sales prediction.
* Performed Exploratory Data Analysis (EDA) to understand relationships between advertising channels and sales.
* Conducted feature importance analysis to determine the impact of each advertising platform.
* Evaluated model performance using MAE, MSE, and R² Score.
* Achieved an R² Score of approximately 0.90, indicating strong predictive accuracy.
* Generated accurate future sales predictions based on user-provided advertising budgets.

---

## Streamlit Web Application

The project includes an interactive Streamlit application that allows users to:

* Enter TV advertising budget
* Enter Radio advertising budget
* Enter Newspaper advertising budget
* Predict expected sales instantly

### Live Demo

Add your deployed Streamlit application link below after deployment:

```text
https://sales-prediction-vasanthi.streamlit.app/
```

---

## Future Enhancements

* Compare multiple regression algorithms
* Add Random Forest and Decision Tree models
* Deploy on cloud platforms
* Add advanced visualizations and dashboards
* Improve prediction accuracy through feature engineering




