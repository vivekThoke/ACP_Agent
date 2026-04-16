from parser.document_parser import extract_text_from_pdf
from extractor.field_extractor import extract_fields
from validator.validator import find_missing_fields
from router.router import route_claim
from model.schema import build_response
from agent.claim_agent import ClaimAgent

def process_claim(file_path):
    text = extract_text_from_pdf(file_path)
    
    # agent = ClaimAgent()
    # result = agent.process(text)

    # return result
    extracted = extract_fields(text)
    
    missing = find_missing_fields(extracted)

    route, reason = route_claim(extracted, missing)

    return build_response(extracted, missing, route, reason)


if __name__ == "__main__":
    result = process_claim("ACORD.pdf")
    print(result)