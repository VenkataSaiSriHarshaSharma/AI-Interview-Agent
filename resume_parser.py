import fitz
import docx
from io import BytesIO


def extract_text_from_pdf(pdf_file):

    text = ""

    pdf_bytes = pdf_file.file.read()

    pdf_document = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    for page in pdf_document:

        text += page.get_text()

    return text


def extract_text_from_docx(docx_file):

    doc_bytes = docx_file.file.read()

    document = docx.Document(
        BytesIO(doc_bytes)
    )

    text = ""

    for para in document.paragraphs:

        text += para.text + "\n"

    return text


def extract_resume_text(uploaded_file):

    filename = uploaded_file.filename.lower()

    if filename.endswith(".pdf"):

        return extract_text_from_pdf(
            uploaded_file
        )

    elif filename.endswith(".docx"):

        return extract_text_from_docx(
            uploaded_file
        )

    return ""