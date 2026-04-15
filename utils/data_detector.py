def has_meaningful_data(text: str) -> bool:
    """
    Detect if document contains actual filled data
    """

    lines = text.split("\n")

    meaningful_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.isupper() and len(line.split()) < 5:
            continue

        if any(word in line.lower() for word in ["policy", "address", "phone", "email"]):
            continue

        if any(char.isdigit() for char in line) or len(line.split()) > 3:
            meaningful_lines.append(line)

    return len(meaningful_lines) > 5