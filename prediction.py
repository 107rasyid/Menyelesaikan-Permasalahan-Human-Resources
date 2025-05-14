import datetime
import os
import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def preprocess_input(new_data):
    # Load cleaned dataset and merge for consistent encoding
    base = pd.read_csv('employee_data_cleaned.csv')
    base = base.drop(['EmployeeId', 'Attrition'], axis=1)
    combined = pd.concat([base, new_data], ignore_index=True)

    # Identify feature types
    num_cols = combined.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = combined.select_dtypes(include=['object']).columns

    # Encode categories and scale numericals
    for col in cat_cols:
        combined[col] = LabelEncoder().fit_transform(combined[col])
    combined[num_cols] = MinMaxScaler().fit_transform(combined[num_cols])

    # Return only the last row (the user input)
    return combined.iloc[[-1]]


def load_model_and_predict(features):
    model = joblib.load('best_model_gb.joblib')
    return model.predict(features)[0]


def app():
    st.title('Employee Attrition Predictor — Jaya Jaya Maju')

    # --- Input Section ---
    with st.form(key='user_inputs'):
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=18, max_value=65, value=30)
            business_travel = st.selectbox('Business Travel',
                                           ['Non-Travel', 'Travel Rarely', 'Travel Frequently'])
            distance = st.number_input('Distance From Home (km)', min_value=0)
        with col2:
            department = st.selectbox('Department',
                                      ['Human Resources', 'Research & Development', 'Sales'])
            education = st.selectbox('Education Level',
                                     ['Below College', 'College', 'Bachelor', 'Master', 'Doctor'])
            gender = st.radio('Gender', ['Male', 'Female'])
        with col3:
            job_role = st.selectbox('Job Role',
                                    ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                     'Manufacturing Director', 'Healthcare Representative',
                                     'Human Resources', 'Manager', 'Sales Representative', 'Research Director'])
            job_level = st.select_slider('Job Level', [1, 2, 3, 4, 5])
            over_time = st.checkbox('Overtime?')

        # Additional inputs
        monthly_income = st.number_input('Monthly Income', min_value=0)
        percent_hike = st.number_input('Percent Salary Hike (%)', min_value=0)

        submit = st.form_submit_button('Predict Attrition')

    if submit:
        # Build dataframe from inputs
        entry = pd.DataFrame({
            'Age': [age],
            'BusinessTravel': [business_travel],
            'DistanceFromHome': [distance],
            'Department': [department],
            'Education': [education],
            'Gender': [gender],
            'JobRole': [job_role],
            'JobLevel': [job_level],
            'OverTime': ['Yes' if over_time else 'No'],
            'MonthlyIncome': [monthly_income],
            'PercentSalaryHike': [percent_hike]
        })

        processed = preprocess_input(entry)
        result = load_model_and_predict(processed)

        # Display prediction
        if result == 1:
            st.error('🚨 High risk of attrition')
        else:
            st.success('✅ Likely to stay')

    # Footer
    year = datetime.date.today().year
    author = 'Rasyid Alfiansyah'
    st.markdown(f"**© {year} {author}**")


if __name__ == '__main__':
    app()
import datetime
import os
import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


def preprocess_input(new_data):
    # Load cleaned dataset and merge for consistent encoding
    base = pd.read_csv('employee_data_cleaned.csv')
    base = base.drop(['EmployeeId', 'Attrition'], axis=1)
    combined = pd.concat([base, new_data], ignore_index=True)

    # Identify feature types
    num_cols = combined.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = combined.select_dtypes(include=['object']).columns

    # Encode categories and scale numericals
    for col in cat_cols:
        combined[col] = LabelEncoder().fit_transform(combined[col])
    combined[num_cols] = MinMaxScaler().fit_transform(combined[num_cols])

    # Return only the last row (the user input)
    return combined.iloc[[-1]]


def load_model_and_predict(features):
    model = joblib.load('best_model_gb.joblib')
    return model.predict(features)[0]


def app():
    st.title('Employee Attrition Predictor — Jaya Jaya Maju')

    # --- Input Section ---
    with st.form(key='user_inputs'):
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=18, max_value=65, value=30)
            business_travel = st.selectbox('Business Travel',
                                           ['Non-Travel', 'Travel Rarely', 'Travel Frequently'])
            distance = st.number_input('Distance From Home (km)', min_value=0)
        with col2:
            department = st.selectbox('Department',
                                      ['Human Resources', 'Research & Development', 'Sales'])
            education = st.selectbox('Education Level',
                                     ['Below College', 'College', 'Bachelor', 'Master', 'Doctor'])
            gender = st.radio('Gender', ['Male', 'Female'])
        with col3:
            job_role = st.selectbox('Job Role',
                                    ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                     'Manufacturing Director', 'Healthcare Representative',
                                     'Human Resources', 'Manager', 'Sales Representative', 'Research Director'])
            job_level = st.select_slider('Job Level', [1, 2, 3, 4, 5])
            over_time = st.checkbox('Overtime?')

        # Additional inputs
        monthly_income = st.number_input('Monthly Income', min_value=0)
        percent_hike = st.number_input('Percent Salary Hike (%)', min_value=0)

        submit = st.form_submit_button('Predict Attrition')

    if submit:
        # Build dataframe from inputs
        entry = pd.DataFrame({
            'Age': [age],
            'BusinessTravel': [business_travel],
            'DistanceFromHome': [distance],
            'Department': [department],
            'Education': [education],
            'Gender': [gender],
            'JobRole': [job_role],
            'JobLevel': [job_level],
            'OverTime': ['Yes' if over_time else 'No'],
            'MonthlyIncome': [monthly_income],
            'PercentSalaryHike': [percent_hike]
        })

        processed = preprocess_input(entry)
        result = load_model_and_predict(processed)

        # Display prediction
        if result == 1:
            st.error('🚨 High risk of attrition')
        else:
            st.success('✅ Likely to stay')

    # Footer
    year = datetime.date.today().year
    author = 'Rasyid Alfiansyah'
    st.markdown(f"**© {year} {author}**")


if __name__ == '__main__':
    app()