from data.skills_db import DETAILED_ROADMAP, LEARNING_HOURS, COURSE_RECOMMENDATIONS

def generate_roadmap(user_skills, target_career_skills):
    missing_skills = [s for s in target_career_skills if s not in user_skills]
    already_have = [s for s in target_career_skills if s in user_skills]

    roadmap = []
    total_hours = 0

    for skill in missing_skills:
        hours = LEARNING_HOURS.get(skill, 40)
        total_hours += hours
        courses = COURSE_RECOMMENDATIONS.get(skill, ["Search on YouTube", "Check official docs"])
        detailed = DETAILED_ROADMAP.get(skill, None)

        roadmap.append({
            "skill": skill,
            "hours": hours,
            "courses": courses,
            "detailed": detailed
        })

    return {
        "already_have": already_have,
        "missing_skills": missing_skills,
        "roadmap": roadmap,
        "total_hours": total_hours,
        "total_weeks": len(missing_skills) * 3
    }