from analyzer.keywords import COMMON_KEYWORDS


def analyze_match(resume_text, job_description):

    resume = resume_text.lower()

    jd = job_description.lower()

    resume_skills = []

    job_skills = []

    for skill in COMMON_KEYWORDS:

        if skill.lower() in resume:
            resume_skills.append(skill)

        if skill.lower() in jd:
            job_skills.append(skill)

    matched = list(
        set(resume_skills).intersection(job_skills)
    )

    missing = list(
        set(job_skills) - set(resume_skills)
    )

    return {

        "resume": resume_skills,

        "job": job_skills,

        "matched": matched,

        "missing": missing

    }