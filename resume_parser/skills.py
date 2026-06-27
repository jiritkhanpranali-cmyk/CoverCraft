from resume_parser.constants import COMMON_SKILLS
from resume_parser.constants import SOFT_SKILLS


def extract_skills(text):

    text=text.lower()

    technical=[]

    soft=[]

    for skill in COMMON_SKILLS:

        if skill.lower() in text:

            technical.append(skill)

    for skill in SOFT_SKILLS:

        if skill.lower() in text:

            soft.append(skill)

    return technical,soft