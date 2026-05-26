import streamlit as st
import time

st.set_page_config(page_title="Secret Scan")

st.title("🔍 Identity Scanner")

name = st.text_input("Enter your name")

if st.button("Scan"):
    
    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.balloons()

    if name.strip().lower() == "anamika kindo":
        st.success("✅ Match Found!")
        st.write("🌸 Welcome Anamika Kindo")
        st.write("⭐ Rarity Level: 100/100")
        st.write("💎 Status: One of a kind")
        st.write("🚀 Secret Mode Activated")
    else:
        st.warning("User detected.")
        st.write(f"Hello {name}!")
