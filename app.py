from parser.document_parser import extract_text_from_pdf

text = extract_text_from_pdf("ACORD.pdf")
print(text[:10000])