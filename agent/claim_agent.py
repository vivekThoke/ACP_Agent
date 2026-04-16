from extractor.field_extractor import extract_fields
from validator.validator import find_missing_fields
from router.router import route_claim

class ClaimAgent:

    def __init__(self, max_retries=2):
        self.max_retries = max_retries

    def process(self, text: str):
        reasoning_steps = []

        reasoning_steps.append("Starting extraction")

        extracted = extract_fields(text)
        missing = find_missing_fields(extracted)

        reasoning_steps.append(f"Missing fields: {missing}")

        if missing:
            reasoning_steps.append("Proceeding with partial data (no re-call to LLM)")
        else:
            reasoning_steps.append("All fields extracted successfully")

        route, reason = route_claim(extracted, missing)

        return {
            "extractedFields": extracted,
            "missingFields": missing,
            "recommendedRoute": route,
            "reasoning": " | ".join(reasoning_steps) + f" | Final: {reason}"
        }

    def _build_reasoning(self, steps, final_reason):
        return " | ".join(steps) + f" | Final Decision: {final_reason}"