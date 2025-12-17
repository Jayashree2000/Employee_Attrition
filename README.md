# Employee_Attrition
Employee turnover is a major challenge for organizations, leading to increased recruitment and training costs, loss of experienced talent, reduced productivity, and disruptions in team dynamics. High attrition rates can negatively impact organizational performance, employee morale, and long-term business growth. As workforce competition intensifies, it has become increasingly important for organizations to understand why employees leave and to identify those who are at risk of attrition before it occurs.

This project focuses on analyzing employee-related data to uncover the key factors that influence attrition and to build predictive machine learning models that support proactive workforce management. By examining demographic attributes, job roles, work experience, compensation, satisfaction levels, and work–life balance indicators, the project aims to identify patterns and trends associated with employee turnover.

Exploratory Data Analysis (EDA) is performed to gain insights into the relationships between employee attributes and attrition, including univariate, bivariate, and multivariate analysis. Feature selection techniques are applied to retain the most relevant variables while reducing redundancy and multicollinearity. Based on these insights, multiple classification models are trained and evaluated using appropriate performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.

The final model is deployed through an interactive Streamlit web application, enabling HR professionals to input employee details and receive real-time attrition risk predictions. This dashboard provides an intuitive and practical tool for identifying high-risk employees and supporting data-driven retention strategies. Overall, the project demonstrates how data science and machine learning can be effectively applied to enhance decision-making in human resource management and improve employee retention outcomes.

📊 Dataset Description

The dataset contains employee-level information related to:

Demographics

Job roles and job levels

Work experience

Work-life balance

Satisfaction levels

Compensation details

🧪 Methodology
1️⃣ Data Preprocessing

Handling missing values

Outlier treatment (IQR method)

Encoding categorical variables

Feature scaling (where required)

2️⃣ Exploratory Data Analysis (EDA)

Univariate analysis (distribution, skewness)

Bivariate analysis (feature vs attrition)

Correlation analysis & multicollinearity checks

Insights derived using plots and statistical tests

3️⃣ Model Building

Algorithms evaluated:

Logistic Regression

Random Forest

Other classification models (for comparison)

Model performance evaluated using:

Accuracy

Precision

Recall

F1-score

ROC-AUC

4️⃣ Final Model

Random Forest Classifier

Selected based on balanced performance and robustness

Saved as a pickle file for deployment

Target Variable:

Attrition → Yes / No

🚀 Model Deployment (Streamlit App)

An interactive Streamlit dashboard allows users to:

Enter employee details

Predict attrition risk instantly

View probability scores

Understand how HR teams can act on the prediction

🔮 Prediction Output

High Risk of Attrition

Low Risk of Attrition

👩‍💻 Author

Jayashree
