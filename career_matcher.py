from sentence_transformers import SentenceTransformer, util
from data.skills_db import CAREER_PATHS

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_careers(user_skills):
    results = []

    user_profile = "Skills: " + ", ".join(user_skills)
    user_embedding = model.encode(user_profile, convert_to_tensor=True)

    for career_name, career_data in CAREER_PATHS.items():
        career_profile = f"{career_name}. Requires: " + ", ".join(career_data["required_skills"])
        career_embedding = model.encode(career_profile, convert_to_tensor=True)

        similarity = util.cos_sim(user_embedding, career_embedding).item()
        match_percent = round(similarity * 100, 1)

        results.append({
            "career": career_name,
            "match": match_percent,
            "description": career_data["description"],
            "required_skills": career_data["required_skills"],
            "avg_salary": career_data.get("avg_salary", "N/A"),
            "demand": career_data.get("demand", "N/A")
        })

    results.sort(key=lambda x: x["match"], reverse=True)
    return results