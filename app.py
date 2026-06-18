import streamlit as st
import pandas as pd
import re
from datetime import date

from database import *
from model import predict_health

# Create database table
create_table()

st.title("🏥 Health Prediction Application")

menu = ["Create", "Read", "Update", "Delete"]

choice = st.sidebar.selectbox("Menu", menu)

# ======================
# CREATE
# ======================

if choice == "Create":

    st.subheader("Add Patient")

    name = st.text_input("Full Name")

    dob = st.date_input("Date Of Birth")

    email = st.text_input("Email Address")

    glucose = st.number_input(
        "Glucose",
        min_value=0.0,
        format="%.2f"
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        min_value=0.0,
        format="%.2f"
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0.0,
        format="%.2f"
    )

    if st.button("Save"):

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not name.strip():
            st.error("Name cannot be empty")

        elif not re.match(email_pattern, email):
            st.error("Invalid Email Address")

        elif dob > date.today():
            st.error("Date of Birth cannot be a future date")

        else:

            # AI Prediction
            remarks = predict_health(
                glucose,
                haemoglobin,
                cholesterol
            )

            # Show AI-generated remarks immediately
            st.write("### 🤖 Remarks (Generated from AI)")
            st.info(remarks)

            # Save to database
            add_patient(
                name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success("Patient Added Successfully!")

# ======================
# READ
# ======================

elif choice == "Read":

    st.subheader("Patient Records")

    data = view_patients()

    if data:

        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Full Name",
                "DOB",
                "Email",
                "Glucose",
                "Haemoglobin",
                "Cholesterol",
                "Remarks"
            ]
        )

        st.dataframe(df, use_container_width=True)

    else:
        st.warning("No records found.")

# ======================
# UPDATE
# ======================

elif choice == "Update":

    st.subheader("Update Patient Remarks")

    patient_id = st.number_input(
        "Patient ID",
        min_value=1,
        step=1
    )

    new_remarks = st.text_input(
        "New Remarks"
    )

    if st.button("Update"):

        update_patient(
            patient_id,
            new_remarks
        )

        st.success("Record Updated Successfully!")

# ======================
# DELETE
# ======================

elif choice == "Delete":

    st.subheader("Delete Patient Record")

    patient_id = st.number_input(
        "Patient ID",
        min_value=1,
        step=1
    )

    if st.button("Delete"):

        delete_patient(patient_id)

        st.success("Record Deleted Successfully!")