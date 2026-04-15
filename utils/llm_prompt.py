def build_extraction_prompt(text: str) -> str:
    return f"""
        You are an insurance claims AI agent.

        Extract the following fields from the FNOL document.

        Return STRICT JSON only (no explanation).

        Fields:
        - policy_number
        - policyholder_name
        - incident_date
        - description
        - estimated_damage

        Rules:
        - If not found → return null
        - estimated_damage must be integer
        - Keep description concise

        Document:
        {text}
        
        Do NOT guess values
        """