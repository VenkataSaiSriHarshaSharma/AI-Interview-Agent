import fitz
import docx


def extract_text_from_pdf(pdf_file):

    text = ""

    pdf_document = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in pdf_document:

        text += page.get_text()

    return text


def extract_text_from_docx(docx_file):

    document = docx.Document(docx_file)

    text = ""

    for para in document.paragraphs:

        text += para.text + "\n"

    return text


def extract_resume_text(uploaded_file):

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):

        return extract_text_from_pdf(
            uploaded_file
        )

    elif filename.endswith(".docx"):

        return extract_text_from_docx(
            uploaded_file
        )

    return ""