from parser.document_parser import extract_text_from_pdf


def process_claim(file_path):
    text = extract_text_from_pdf(file_path)
    
    

text = extract_text_from_pdf("ACORD.pdf")
print(text[:10000])