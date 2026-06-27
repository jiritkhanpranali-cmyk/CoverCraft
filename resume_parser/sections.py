import re


def get_section(text, keywords):

    lower=text.lower()

    start=-1

    for word in keywords:

        index=lower.find(word)

        if index!=-1:

            start=index

            break

    if start==-1:

        return ""

    next_headers=[

        "education",

        "skills",

        "projects",

        "experience",

        "internship",

        "certification",

        "achievements",

        "languages",

        "hobbies"

    ]

    end=len(text)

    for header in next_headers:

        pos=lower.find(header,start+5)

        if pos!=-1 and pos<end:

            end=pos

    return text[start:end]