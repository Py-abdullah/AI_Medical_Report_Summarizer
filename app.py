import streamlit as st
from pypdf import PdfReader

from summarizer import summarize_medical_report
# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Medical Report Summarizer",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("🩺 AI Medical Report Summarizer")

st.write(
    "Upload a medical report and generate a simplified, "
    "patient-friendly summary using AI."
)
# -----------------------------
# Medical Disclaimer
# -----------------------------

st.warning(
    "This tool is for educational and informational purposes only. "
    "It does not provide a medical diagnosis or replace advice from "
    "a qualified healthcare professional."
)
# -----------------------------
# Language Selection
# -----------------------------

language = st.selectbox(
    "Select Summary Language",
    [
        "English",
        "Urdu",
        "Arabic"
    ]
)

# -----------------------------
# PDF Upload
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf", "txt"]
)

# -----------------------------
# Extract PDF Text
# -----------------------------

def extract_pdf_text(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text
# -----------------------------
# Process File
# -----------------------------

if uploaded_file is not None:

    st.success(
        f"File uploaded: {uploaded_file.name}"
    )

    if st.button("Generate Summary"):

        with st.spinner(
            "Reading and summarizing the medical report..."
        ):

            try:

                # PDF
                if uploaded_file.name.lower().endswith(".pdf"):

                    report_text = extract_pdf_text(
                        uploaded_file
                    )

                # TXT
                else:

                    report_text = uploaded_file.read().decode(
                        "utf-8"
                    )

                # Check extracted text

                if not report_text.strip():

                    st.error(
                        "No readable text was found in the file."
                    )

                else:

                    # Display extracted text

                    with st.expander(
                        "View Extracted Report Text"
                    ):

                        st.write(report_text)


                    # Generate summary

                    summary = summarize_medical_report(
                        report_text,
                        language
                    )


                    # Display result

                    st.subheader(
                        "📋 Patient-Friendly Summary"
                    )

                    st.write(summary)


            except Exception as e:

                st.error(
                    f"An error occurred: {str(e)}"
                )
                