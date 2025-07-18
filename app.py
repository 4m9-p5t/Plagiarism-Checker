import streamlit as st
from plagiarism_detector import detect_plagiarism

st.title("🔍 Pendeteksi Plagiarisme Sederhana")
st.write("Masukkan teks yang ingin Anda periksa plagiarisme:")

input_text = st.text_area("Teks yang ingin diperikasa", height=200)

uploaded_file = st.file_uploader("Atau unggah file teks referensi (opsional)", type=["txt"])

if uploaded_file is not None:
    reference_text = uploaded_file.read().decode("utf-8")
else:
    try:
        with open("data/reference.txt", "r", encoding="utf-8") as file:
            reference_text = file.read()
    except FileNotFoundError:
        reference_text = ""
        
if st.button("Periksa Plagiarisme"):
    if input_text.strip() == "":
        st.warning("Masukkan teks yang ingin diperiksa.")
    elif reference_text.strip() == "":
        st.error("Text referensi tidak tersedia.")
    else:
        score = detect_plagiarism(input_text, reference_text)
        percent = round(score * 100, 2)
        st.success(f"✅ Skor plagiarisme: {percent}%")
        if percent > 50:
            st.error("⚠️ Teks ini memiliki tingkat plagiarisme yang tinggi!")
        if percent > 20:
            st.success("⚠️ Teks agak mirip. Silakan lakukan parafrase lebih lanjut.")
        else:
            st.info("✅ Teks ini tampaknya orisinal.")