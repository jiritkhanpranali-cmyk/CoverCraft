import re

from resume_parser.skills import extract_skills
from resume_parser.sections import get_section


def extract_information(text):

    info={}

    # ---------------- Name ----------------

    lines=text.split("\n")

    info["name"]=lines[0].strip()

    # ---------------- Email ----------------

    emails=re.findall(

        r'[\w\.-]+@[\w\.-]+\.\w+',

        text

    )

    info["email"]=emails[0] if emails else ""

    # ---------------- Phone ----------------

    phones=re.findall(

        r'\+?\d[\d\s\-]{8,15}',

        text

    )

    info["phone"]=phones[0] if phones else ""

    # ---------------- Links ----------------

    github=re.findall(

        r'https?://github\.com/\S+',

        text

    )

    linkedin=re.findall(

        r'https?://(www\.)?linkedin\.com/\S+',

        text

    )

    info["github"]=github[0] if github else ""

    info["linkedin"]=linkedin[0] if linkedin else ""

    # ---------------- Skills ----------------

    technical,soft=extract_skills(text)

    info["skills"]=", ".join(technical)

    info["soft_skills"]=", ".join(soft)

    # ---------------- Sections ----------------

    info["education"]=get_section(

        text,

        ["education"]

    )

    info["projects"]=get_section(

        text,

        ["projects","project"]

    )

    info["experience"]=get_section(

        text,

        [

            "experience",

            "internship",

            "work experience"

        ]

    )

    info["certifications"]=get_section(

        text,

        [

            "certification",

            "certifications"

        ]

    )

    return info