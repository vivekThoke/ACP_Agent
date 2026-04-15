from extractor.field_extractor import extract_fields
from validator.validator import find_missing_fields
from router.router import route_claim

class ClaimAgent:

    def __init__(self, max_retries=2):
        self.max_retries = max_retries

    def process(self, text: str):
        attempt = 0
        final_data = None
        reasoning_steps = []

        while attempt <= self.max_retries:
            reasoning_steps.append(f"Attempt {attempt+1}: Extracting fields")

            extracted = extract_fields(text)
            missing = find_missing_fields(extracted)

            reasoning_steps.append(f"Missing fields: {missing}")

            # ✅ Decision 1: If no missing → stop
            if not missing:
                reasoning_steps.append("All fields extracted successfully")
                final_data = extracted
                break

            # ✅ Decision 2: Retry if attempts left
            if attempt < self.max_retries:
                reasoning_steps.append("Retrying extraction using LLM refinement")
                attempt += 1
            else:
                reasoning_steps.append("Max retries reached. Proceeding with available data")
                final_data = extracted
                break

        # 🚦 Routing
        route, reason = route_claim(final_data, missing)

        return {
            "extractedFields": final_data,
            "missingFields": missing,
            "recommendedRoute": route,
            "reasoning": self._build_reasoning(reasoning_steps, reason)
        }

    def _build_reasoning(self, steps, final_reason):
        return " | ".join(steps) + f" | Final Decision: {final_reason}"