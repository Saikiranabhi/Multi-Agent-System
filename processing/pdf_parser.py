from pypdf import PdfReader

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    pages_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)

    return "\n".join(pages_text)
