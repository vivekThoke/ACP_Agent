def build_extraction_prompt(text: str) -> str:
    return f"""
        You are an insurance claims AI agent.

        IMPORTANT:
        - If the document does NOT contain actual filled values, return all fields as null.
        - DO NOT guess or infer values.

        Extract the following fields.

        Return STRICT JSON only.

        Fields:
        - policy_number
        - policyholder_name
        - incident_date
        - description
        - estimated_damage

        Rules:
        - If value is not explicitly present → return null
        - Do NOT extract labels
        - Do NOT hallucinate

        Document:
        {text}
        
        
        Do NOT guess values
        """