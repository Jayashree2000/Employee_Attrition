import streamlit as st
import pandas as pd
import pickle

# ==================================================
# PAGE CONFIG 
# ==================================================
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# LOAD TRAINED MODEL 
# ==================================================
file_path = r"G:\DS_Projects\.venv\Employee_Attrition\best_model.pkl"

with open(file_path, "rb") as f:
    pickle_model = pickle.load(f)

# ==================================================
# HEADER SECTION 
# ==================================================
st.markdown(
    """
    <h1 style='text-align: center;'>📊 Employee Attrition Prediction Dashboard</h1>
    <p style='text-align: center; font-size: 18px;'>
    Helping HR teams identify <b>at-risk employees</b> and support
    <b>data-driven retention strategies</b>.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ==================================================
# SIDEBAR – INPUT SECTION 
# ==================================================
st.sidebar.header("🧾 Employee Details")

age = st.sidebar.number_input("Age", min_value=18, max_value=65, value=30)
monthly_income = st.sidebar.number_input("Monthly Income", min_value=1000, value=30000)
total_working_years = st.sidebar.number_input("Total Working Years", min_value=0, value=8)

years_at_company = st.sidebar.number_input("Years at Company", min_value=0, value=5)
years_in_current_role = st.sidebar.number_input("Years in Current Role", min_value=0, value=3)
years_with_curr_manager = st.sidebar.number_input("Years with Current Manager", min_value=0, value=3)

st.sidebar.markdown("---")

overtime = st.sidebar.selectbox("OverTime", ["Yes", "No"])
job_role = st.sidebar.selectbox(
    "Job Role",
    [
        "Sales Executive", "Research Scientist", "Laboratory Technician",
        "Manufacturing Director", "Healthcare Representative",
        "Manager", "Sales Representative", "Research Director", "Human Resources"
    ]
)
job_level = st.sidebar.selectbox("Job Level", [1, 2, 3, 4, 5])
environment_satisfaction = st.sidebar.selectbox("Environment Satisfaction", [1, 2, 3, 4])
work_life_balance = st.sidebar.selectbox("Work Life Balance", [1, 2, 3, 4])

# ==================================================
# MAIN PANEL – DATA PREVIEW 
# ==================================================
st.subheader("📋 Employee Profile Summary")

colA, colB, colC = st.columns(3)

colA.metric("Age", age)
colA.metric("Monthly Income", monthly_income)

colB.metric("Years at Company", years_at_company)
colB.metric("Years in Current Role", years_in_current_role)

colC.metric("Total Working Years", total_working_years)
colC.metric("Years with Manager", years_with_curr_manager)

st.markdown("---")

# ==================================================
# PREPARE INPUT DATA 
# ==================================================
input = pd.DataFrame([{
    "Age": age,
    "MonthlyIncome": monthly_income,
    "TotalWorkingYears": total_working_years,
    "YearsAtCompany": years_at_company,
    "YearsInCurrentRole": years_in_current_role,
    "YearsWithCurrManager": years_with_curr_manager,
    "OverTime": overtime,
    "JobRole": job_role,
    "JobLevel": job_level,
    "EnvironmentSatisfaction": environment_satisfaction,
    "WorkLifeBalance": work_life_balance
}])

input_encoded = input.copy()

input_encoded["OverTime"] = input_encoded["OverTime"].map({"Yes": 0, "No": 1})

input_encoded = pd.get_dummies(
    input_encoded,
    columns=["JobRole", "JobLevel", "EnvironmentSatisfaction", "WorkLifeBalance"],
    drop_first=False,
    dtype=int
)

input_encoded = input_encoded.reindex(
    columns=pickle_model.feature_names_in_,
    fill_value=0
)

# ==================================================
# PREDICTION SECTION 
# ==================================================
st.subheader("🔮 Attrition Prediction")

if st.button("🚀 Predict Attrition Risk"):
    prediction = pickle_model.predict(input_encoded)[0]
    prediction_prob = pickle_model.predict_proba(input_encoded)[0, 1]

    if prediction == 1:
        st.error(f"❌ High Risk of Attrition\n\nProbability: **{prediction_prob:.2f}**")
    else:
        st.success(f"✅ Low Risk of Attrition\n\nProbability: **{prediction_prob:.2f}**")

    st.markdown("### 🧠 How to Use This Insight")
    st.markdown(
        """
        - Focus retention efforts on **high-risk employees**
        - Review **workload, role satisfaction, and work-life balance**
        - Proactively engage **managers and HR partners**
        """
    )


