from parser.document_parser import extract_text_from_pdf
from extractor.field_extractor import extract_fields
from validator.validator import find_missing_fields
from router.router import route_claim

def process_claim(file_path):
    text = extract_text_from_pdf(file_path)

    extracted = extract_fields(text)
    missing = find_missing_fields(extracted)

    route, reason = route_claim(extracted, missing)

    return {
        "extractedFields": extracted,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }


if __name__ == "__main__":
    result = process_claim("ACORD.pdf")
    print(result)