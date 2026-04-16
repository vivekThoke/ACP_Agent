import re

def route_claim(data: dict, missing_fields: list):
    description = (data.get("description") or "").lower()
    damage = data.get("estimated_damage")

    # Rule 1: Missing fields
    if missing_fields:
        return "Manual Review", "Missing required fields"

    # Rule 2: Fraud keywords
    fraud_keywords = ["fraud", "staged", "inconsistent"]
    if any(word in description for word in fraud_keywords):
        return "Investigation", "Fraud-related keywords detected"

    # Rule 3: Injury
    if "injury" in description:
        return "Specialist Queue", "Injury-related claim"

    damage_val = parse_amount(damage)
    # Rule 4: Fast track
    if damage_val and damage_val  < 25000:
        return "Fast Track", "Low estimated damage"

    return "Standard Processing", "Default routing"

def parse_amount(value):
    if not value:
        return None
    # remove currency symbols and commas
    cleaned = re.sub(r"[^\d]", "", value)
    return int(cleaned) if cleaned else None