def calculate_ats_score(
    skills,
    education,
    experience,
    projects
):

    score = 20

    text = (
        skills +
        education +
        experience +
        projects
    ).lower()


    keywords = [
        "python",
        "java",
        "sql",
        "machine learning",
        "artificial intelligence",
        "github",
        "data science",
        "web development",
        "api",
        "cloud",
        "aws",
        "docker",
        "streamlit",
        "project"
    ]


    matched_keywords = []
    missing_keywords = []


    for keyword in keywords:

        if keyword in text:

            score += 5
            matched_keywords.append(keyword)

        else:

            missing_keywords.append(keyword)



    if len(projects) > 50:
        score += 10


    if len(experience) > 50:
        score += 10


    if len(education) > 20:
        score += 10



    if score > 100:
        score = 100



    return (
        score,
        matched_keywords,
        missing_keywords
    )