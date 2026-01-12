from extract_pdf import extract_pdf_pages
from llm_compiler import compile_presentation_json
import json

PDF_PATH = "/home/akshay/Videos/pdf_presentation_compiler/pdfs/xx.pdf"

def main():
    print("Extracting PDF pages...")
    pages = extract_pdf_pages(PDF_PATH)

    print(f"Extracted {len(pages)} pages")

    print("Compiling presentation JSON via LLM...")
    presentation_json = compile_presentation_json(pages)

    with open("presentation_output.json", "w") as f:
        json.dump(presentation_json, f, indent=2)

    print("Done. Output saved to presentation_output.json")

if __name__ == "__main__":
    main()
