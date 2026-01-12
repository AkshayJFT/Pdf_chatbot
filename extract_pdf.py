import fitz  # PyMuPDF

def extract_pdf_pages(pdf_path: str):
    doc = fitz.open(pdf_path)
    pages = []

    for idx, page in enumerate(doc):
        text = page.get_text("text").strip()
        if text:
            pages.append({
                "page_no": idx + 1,
                "text": text
            })

    doc.close()
    return pages



