import re

def extract_fields(text: str) -> dict:
    data = {}
    
    # Policy Number
    policy_match = re.search(r"POLICY NUMBER[:\s]*([A-Z0-9-]+)", text)
    data["policy_number"] = policy_match.group(1) if policy_match else None
    
    # Name
    name_match = re.search(r"NAME OF INSURED.*?:\s*(.+)", text)
    data["policyholder_name"] = name_match.group(1) if name_match else None
    
    # Date of Loss
    date_match = re.search(r"DATE OF LOSS.*?:\s*(\d{2}/\d{2}/\d{4})", text)
    data["incident_date"] = date_match.group(1) if date_match else None
    
    # Description
    desc_match = re.search(r"DESCRIPTION OF ACCIDENT.*?:\s*(.+)", text)
    data["description"] = desc_match.group(1) if desc_match else None
    
    # Estimated Damage
    damage_match = re.search(r"ESTIMATE AMOUNT[:\s]*([\d,]+)", text)
    data["estimated_damage"] = int(damage_match.group(1).replace(",", "")) if damage_match else None
    
    return data

# Policy Number
def extract_policy_number(text):
    lines = text.split("\n")

    for i, line in enumerate(lines):
        if "POLICY NUMBER" in line.upper():
            for j in range(i+1, min(i+5, len(lines))):
                candidate = lines[j].strip()

                if candidate and len(candidate) > 5 and not candidate.isalpha():
                    return candidate
    return None

# Policyholder Name
def extract_name(text):
    lines = text.split("\n")

    for i, line in enumerate(lines):
        if "NAME OF INSURED" in line.upper():
            for j in range(i+1, i+5):
                if j < len(lines):
                    val = lines[j].strip()
                    if val and len(val.split()) >= 2:
                        return val
    return None


# Incident Name
def extract_date(text):
    match =  re.search(r"\b\d{2}/\d{2}/\d{4}\b", text)
    return match.group(0) if match else None

