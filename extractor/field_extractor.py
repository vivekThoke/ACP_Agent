import re
from extractor.llm_extractor import extract_with_llm
from utils.data_detector import has_meaningful_data


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


# Description
def extract_description(text):
    lines = text.split("\n")

    for i, line in enumerate(lines):
        if "DESCRIPTION OF ACCIDENT" in line.upper():
            desc = []
            for j in range(i+1, i+10):
                if j < len(lines):
                    desc.append(lines[j].strip())
            return " ".join(desc)

    return None


# Estimated damage
def extract_damage(text):
    lines = text.split("\n")

    for i, line in enumerate(lines):
        if "ESTIMATE AMOUNT" in line.upper():
            for j in range(i+1, i+5):
                if j < len(lines):
                    val = lines[j].replace(",", "").strip()
                    if val.isdigit():
                        return int(val)
    return None


def extract_fields(text):
    has_data = has_meaningful_data(text)

    print("[DEBUG]: Has meaningful data:", has_data)

    if not has_data:
        print("[DEBUG]: Empty form detected. Skipping extraction.")

        return {
            "policy_number": None,
            "policyholder_name": None,
            "incident_date": None,
            "description": None,
            "estimated_damage": None
        }
    
    # data = {
    #     "policy_number": extract_policy_number(text),
    #     "policyholder_name": extract_name(text),
    #     "incident_date": extract_date(text),
    #     "description": extract_description(text),
    #     "estimated_damage": extract_damage(text)
    # }
    
    data = {
        "policy_number": None,
        "policyholder_name": None,
        "incident_date": None,
        "description": None,
        "estimated_damage": None
    }

    if any(v is None for v in data.values()):
        print("[DEBUG] Calling LLM fallback...")
        llm_data = extract_with_llm(text)

        for key in data:
            if not data[key] and key in llm_data:
                data[key] = llm_data[key]

    return data