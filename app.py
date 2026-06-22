import streamlit as st
import pandas as pd
import joblib

# ======================

# CONFIG

# ======================

st.set_page_config(
page_title="Student Dropout Prediction",
page_icon="🎓",
layout="wide"
)

model = joblib.load("model.pkl")

st.title("🎓 Student Dropout Prediction")

st.markdown("""
This machine learning application predicts a student's academic status based on demographic, academic, financial, and socio-economic factors.

Possible outcomes:
- ⚠️ Dropout
- 🎓 Graduate
  """)

# ======================

# DEMOGRAPHICS

# ======================

with st.expander("👤 Student Demographics", expanded=True):

    col1, col2 = st.columns(2)

    with col1:
        marital_dict = {
            "Single": 1,
            "Married": 2,
            "Widower": 3,
            "Divorced": 4,
            "Facto Union": 5,
            "Legally Separated": 6
        }

        marital_label = st.selectbox(
            "Marital Status",
            options=list(marital_dict.keys())
        )

        marital_status = marital_dict[marital_label]

        nationality_dict = {
            "Portuguese": 1,
            "German": 2,
            "Spanish": 6,
            "Italian": 11,
            "Dutch": 13,
            "English": 14,
            "Lithuanian": 17,
            "Angolan": 21,
            "Cape Verdean": 22,
            "Guinean": 24,
            "Mozambican": 25,
            "Santomean": 26,
            "Turkish": 32,
            "Brazilian": 41,
            "Romanian": 62,
            "Moldovan": 100,
            "Mexican": 101,
            "Ukrainian": 103,
            "Russian": 105,
            "Cuban": 108,
            "Colombian": 109
        }

        nationality_label = st.selectbox(
            "Nationality",
            options=list(nationality_dict.keys())
        )

        nationality = nationality_dict[nationality_label]

        gender_dict = {
        "Female": 0,
        "Male": 1
        }

        gender_label = st.selectbox(
            "Gender",
            options=list(gender_dict.keys())
        )

        gender = gender_dict[gender_label]
        age = st.number_input("Age at Enrollment", min_value=17, value=18)

    with col2:
        yes_no = {
            "No": 0,
            "Yes": 1
        }

        displaced_label = st.selectbox(
            "Displaced",
            options=list(yes_no.keys())
        )

        displaced = yes_no[displaced_label]

        special_needs_label = st.selectbox(
            "Educational Special Needs",
            options=list(yes_no.keys())
        )

        special_needs = yes_no[special_needs_label]

        international_label = st.selectbox(
            "International",
            options=list(yes_no.keys())
        )

        international = yes_no[international_label]

# ======================

# ACADEMIC BACKGROUND

# ======================

with st.expander("🎓 Academic Background"):

    col1, col2 = st.columns(2)

    with col1:
        application_mode_dict = {
            "1st Phase - General Contingent": 1,
            "Ordinance No. 612/93": 2,
            "Azores Island Special Contingent": 5,
            "Other Higher Courses": 7,
            "Ordinance No. 854-B/99": 10,
            "International Student": 15,
            "Madeira Island Special Contingent": 16,
            "2nd Phase - General Contingent": 17,
            "3rd Phase - General Contingent": 18,
            "Different Plan": 26,
            "Other Institution": 27,
            "Over 23 Years Old": 39,
            "Transfer": 42,
            "Change of Course": 43,
            "Technological Specialization Diploma": 44,
            "Change Institution/Course": 51,
            "Short Cycle Diploma": 53,
            "Change Institution/Course (International)": 57
        }

        application_mode_label = st.selectbox(
            "Application Mode",
            options=list(application_mode_dict.keys())
        )

        application_mode = application_mode_dict[application_mode_label]

        application_order = st.slider(
            "Application Order",
            min_value=0,
            max_value=9,
            value=0,
            help="0 = First Choice, 9 = Last Choice"
        )

        course_dict = {
            "Biofuel Production Technologies": 33,
            "Animation and Multimedia Design": 171,
            "Social Service (Evening)": 8014,
            "Agronomy": 9003,
            "Communication Design": 9070,
            "Veterinary Nursing": 9085,
            "Informatics Engineering": 9119,
            "Equinculture": 9130,
            "Management": 9147,
            "Social Service": 9238,
            "Tourism": 9254,
            "Nursing": 9500,
            "Oral Hygiene": 9556,
            "Advertising and Marketing Management": 9670,
            "Journalism and Communication": 9773,
            "Basic Education": 9853,
            "Management (Evening)": 9991
        }

        course_label = st.selectbox(
            "Course",
            options=list(course_dict.keys())
        )

        course = course_dict[course_label]

    with col2:
        daytime_evening = {
            "Evening": 0,
            "Daytime": 1
        }

        attedance_label = st.selectbox(
            "Daytime/Evening Attendance",
            options=list(daytime_evening.keys())
        )

        attendance = daytime_evening[attedance_label]

        previous_qualification_dict = {
            "Secondary Education": 1,
            "Bachelor Degree": 2,
            "Degree": 3,
            "Master": 4,
            "Doctorate": 5,
            "Frequency of Higher Education": 6,
            "12th Year Not Completed": 9,
            "11th Year Not Completed": 10,
            "Other 11th Year Schooling": 12,
            "10th Year Schooling": 14,
            "10th Year Not Completed": 15,
            "Basic Education 3rd Cycle": 19,
            "Basic Education 2nd Cycle": 38,
            "Technological Specialization": 39,
            "Higher Education Degree (1st Cycle)": 40,
            "Professional Higher Technical Course": 42,
            "Master (2nd Cycle)": 43
        }

        previous_qualification_label = st.selectbox(
            "Previous Qualification",
            options=list(previous_qualification_dict.keys())
        )

        previous_qualification = previous_qualification_dict[previous_qualification_label]

        previous_grade = st.number_input(
            "Previous Qualification Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0
        )

        admission_grade = st.number_input(
            "Admission Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0
        )

# ======================

# FAMILY INFORMATION

# ======================

with st.expander("👨‍👩‍👧 Family Information"):

    col1, col2 = st.columns(2)

    with col1:
        mother_qual = st.number_input(
            "Mother Qualification",
            min_value=1,
            value=1
        )

        mother_occ = st.number_input(
            "Mother Occupation",
            min_value=0,
            value=0
        )

    with col2:
        father_qual = st.number_input(
            "Father Qualification",
            min_value=1,
            value=1
        )

        father_occ = st.number_input(
            "Father Occupation",
            min_value=0,
            value=0
        )

# ======================

# FINANCIAL INFORMATION

# ======================

with st.expander("💰 Financial Information"):

    col1, col2 = st.columns(2)

    with col1:
        yes_no = {
            "No": 0,
            "Yes": 1
        }

        debtor_label = st.selectbox(
            "Debtor",
            options=list(yes_no.keys())
        )

        debtor = yes_no[debtor_label]

        scholarship_label = st.selectbox(
            "Scholarship Holder",
            options=list(yes_no.keys())
        )

        scholarship = yes_no[scholarship_label]

    with col2:
        tuition_label = st.selectbox(
            "Tuition Fees Up To Date",
            options=list(yes_no.keys())
        )

        tuition = yes_no[tuition_label]

# ======================

# SEMESTER 1

# ======================

with st.expander("📚 Academic Performance - Semester 1"):

    sem1_credited = st.number_input("Credited", min_value=0)
    sem1_enrolled = st.number_input("Enrolled", min_value=0)
    sem1_eval = st.number_input("Evaluations", min_value=0)
    sem1_approved = st.number_input("Approved", min_value=0)
    sem1_grade = st.number_input("Grade", min_value=0.0, max_value=20.0)
    sem1_without_eval = st.number_input(
        "Without Evaluations",
        min_value=0
    )

# ======================

# SEMESTER 2

# ======================

with st.expander("📖 Academic Performance - Semester 2"):

    sem2_credited = st.number_input("Credited ", min_value=0)
    sem2_enrolled = st.number_input("Enrolled ", min_value=0)
    sem2_eval = st.number_input("Evaluations ", min_value=0)
    sem2_approved = st.number_input("Approved ", min_value=0)
    sem2_grade = st.number_input(
        "Grade ",
        min_value=0.0,
        max_value=20.0
    )
    sem2_without_eval = st.number_input(
        "Without Evaluations ",
        min_value=0
    )

# ======================

# ECONOMIC

# ======================

with st.expander("📈 Economic Indicators"):

    unemployment = st.number_input(
        "Unemployment Rate (%)",
        value=10.0
    )

    inflation = st.number_input(
        "Inflation Rate (%)",
        value=1.0
    )

    gdp = st.number_input(
        "GDP",
        value=0.0
    )

# ======================

# PREDICT

# ======================

if st.button("🔍 Predict Student Status"):

    data = pd.DataFrame([{
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Application_order': application_order,
        'Course': course,
        'Daytime_evening_attendance': attendance,
        'Previous_qualification': previous_qualification,
        'Previous_qualification_grade': previous_grade,
        'Nacionality': nationality,
        'Mothers_qualification': mother_qual,
        'Fathers_qualification': father_qual,
        'Mothers_occupation': mother_occ,
        'Fathers_occupation': father_occ,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Educational_special_needs': special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age,
        'International': international,
        'Curricular_units_1st_sem_credited': sem1_credited,
        'Curricular_units_1st_sem_enrolled': sem1_enrolled,
        'Curricular_units_1st_sem_evaluations': sem1_eval,
        'Curricular_units_1st_sem_approved': sem1_approved,
        'Curricular_units_1st_sem_grade': sem1_grade,
        'Curricular_units_1st_sem_without_evaluations': sem1_without_eval,
        'Curricular_units_2nd_sem_credited': sem2_credited,
        'Curricular_units_2nd_sem_enrolled': sem2_enrolled,
        'Curricular_units_2nd_sem_evaluations': sem2_eval,
        'Curricular_units_2nd_sem_approved': sem2_approved,
        'Curricular_units_2nd_sem_grade': sem2_grade,
        'Curricular_units_2nd_sem_without_evaluations': sem2_without_eval,
        'Unemployment_rate': unemployment,
        'Inflation_rate': inflation,
        'GDP': gdp
    }])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]

    st.subheader("Prediction Result")

    if prediction == "Dropout":
        st.error("⚠️ High Risk of Dropout")
    else:
        st.success("🎓 Likely to Graduate")

    st.write("Prediction:", prediction)

    st.progress(float(max(probability)))

    st.subheader("📊 Class Probabilities")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Dropout", f"{probability[0]*100:.2f}%")

    with col2:
        st.metric("Graduate", f"{probability[1]*100:.2f}%")

    st.subheader("📌 General Dropout Risk Factors")

    st.markdown("""
    Factors that have the strongest influence on dropout risk:

    - 📚 Curricular Units 2nd Semester Approved
    - 📖 Curricular Units 1st Semester Approved
    - 💰 Tuition Fees Up to Date
    - 📝 Curricular Units 2nd Semester Grade
    - 🌍 International Student Status

    These factors were obtained from Logistic Regression feature analysis.
    """)
