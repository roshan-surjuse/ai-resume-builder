def calculate_ats_score(skills, education, experience, projects):

    score = 20

    keywords = [
        "python",
        "java",
        "sql",
        "machine learning",
        "artificial intelligence",
        "ai",
        "github",
        "projects",
        "web development",
        "communication",
        "cloud",
        "data science"
    ]


    text = (
        skills +
        education +
        experience +
        projects
    ).lower()


    for keyword in keywords:

        if keyword in text:
            score += 5


    if len(skills) > 50:
        score += 10


    if len(projects) > 50:
        score += 10


    if len(experience) > 50:
        score += 10


    if score > 100:
        score = 100


    return score