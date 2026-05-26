import streamlit as st

st.title("Username Modifier")

username = st.text_input("Enter username here:")

if username:
    uppercase_username = username.upper()
    replace_username = uppercase_username.replace("A", "@")

    first_character = replace_username[0]
    last_character = replace_username[-1]

    st.write("Modified username:", replace_username)
    st.write("Length:", len(replace_username))
    st.write("First character:", first_character)
    st.write("Last character:", last_character)
    st.write("Count of @:", replace_username.count("@"))

    if len(replace_username) <= 10:
        st.success("Valid username")
    else:
        st.error("Username is too long")
