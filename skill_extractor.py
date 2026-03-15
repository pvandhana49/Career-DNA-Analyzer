import spacy
from data.skills_db import SKILLS_LIST

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILLS_LIST:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills