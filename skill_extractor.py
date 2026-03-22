from data.skills_db import SKILLS_LIST, SKILL_SYNONYMS

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []

    for skill, synonyms in SKILL_SYNONYMS.items():
        for synonym in synonyms:
            if synonym in text_lower:
                if skill not in found_skills:
                    found_skills.append(skill)
                break

    return found_skills