import streamlit as st
from reportlab.pdfgen import canvas
from io import BytesIO

def create_pdf(text):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, text)
    p.save()
    buffer.seek(0)
    return buffer

st.title("ReportLab PDF Download Example")

user_text = st.text_input("Enter text to include in the PDF:", "Hello from Streamlit and ReportLab!")

if st.button("Generate and Download PDF"):
    pdf_buffer = create_pdf(user_text)
    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name="reportlab_example.pdf",
        mime="application/pdf"
    )
