from data.skills_db import ROADMAP_STEPS

def generate_roadmap(user_skills, target_career_skills):
    missing_skills = [s for s in target_career_skills if s not in user_skills]
    already_have = [s for s in target_career_skills if s in user_skills]

    roadmap = []

    for i, skill in enumerate(missing_skills):
        steps = ROADMAP_STEPS.get(skill, ["Study fundamentals", "Build a project", "Practice daily"])
        roadmap.append({
            "week": i + 1,
            "skill": skill,
            "steps": steps
        })

    return {
        "already_have": already_have,
        "missing_skills": missing_skills,
        "roadmap": roadmap,
        "total_weeks": len(missing_skills)
    }