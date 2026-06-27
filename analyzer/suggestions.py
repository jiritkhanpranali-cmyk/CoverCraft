def generate_suggestions(missing_skills):

    suggestions = []


    if missing_skills:

        for skill in missing_skills:

            suggestions.append(
                f"Consider adding {skill} knowledge or projects."
            )


    else:

        suggestions.append(
            "Your resume matches the job requirements well."
        )


    return suggestions