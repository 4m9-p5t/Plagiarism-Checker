import streamlit as st
from plagiarism_detector import detect_plagiarism
from utils.text_utils import extract_text_from_docx, extract_text_from_pdf

st.title("🔍 Pendeteksi Plagiarisme Sederhana")
st.write("Masukkan teks yang ingin Anda periksa plagiarisme:")

input_text = st.text_area("Teks yang ingin diperikasa", height=200)

uploaded_file = st.file_uploader("Upload dokumen referensi (.txt, .docx, .pdf):", type=["txt", "docx", "pdf"])

reference_text = ""

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1]
    
    if file_type == "txt":
        reference_text = uploaded_file.read().decode("utf-8")
    elif file_type == "docx":
        reference_text = extract_text_from_docx(uploaded_file)
    elif file_type == "pdf":
        reference_text = extract_text_from_pdf(uploaded_file)
    else:
        st.error("Format file tidak didukung.")
else:
    try:
        with open("data/reference.txt", "r", encoding="utf-8") as f:
            reference_text = f.read()
    except FileNotFoundError:
        st.warning("Tidak ada file referensi bawaan ditemukan.")
        
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