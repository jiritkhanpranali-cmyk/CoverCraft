def create_prompt(

    name,

    job,

    company,

    skills,

    experience,

    tone,

    job_description="",

    missing_skills=""
):

    return f"""

Write a professional cover letter.

Candidate

Name:
{name}

Applying For:
{job}

Company:
{company}

Skills:
{skills}

Experience:
{experience}

Writing Tone:
{tone}

Job Description:

{job_description}

Missing Skills:

{missing_skills}

Instructions

- Keep between 180 and 220 words.

- Mention relevant experience.

- Align the candidate profile with the job description.

- Do NOT mention missing skills directly.

- End professionally.

"""