def calculate_score(result):

    total = len(result["job"])

    matched = len(result["matched"])

    if total == 0:
        return 0

    return round((matched / total) * 100)