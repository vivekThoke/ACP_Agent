MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "incident_date",
    "description",
    "estimated_damage"
]

def find_missing_fields(data: dict):
    missing = []

    for field in MANDATORY_FIELDS:
        if not data.get(field):
            missing.append(field)

    return missing