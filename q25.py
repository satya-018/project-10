import streamlit as st
from datetime import date

st.set_page_config(page_title="Anamika Birthday Countdown")

st.title("🎂 Birthday Countdown for Anamika Kindo")

# Input fields
title = st.text_input("Enter your title (Miss, Ms., Dr., etc.)")
dob = st.date_input(
    "Select your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if st.button("Check Countdown"):
    today = date.today()

    # Next birthday calculation
    next_birthday = date(today.year, dob.month, dob.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)

    days_left = (next_birthday - today).days

    st.success(
        f"🎉 Congratulations Anamika {title}! "
        f"Your birthday is just {days_left} days away."
    )

    st.balloons()
