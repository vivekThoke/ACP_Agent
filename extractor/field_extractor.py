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