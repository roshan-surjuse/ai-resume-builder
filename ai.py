def generate_summary(
    name,
    skills,
    education,
    experience
):

    skills_text = skills.replace("-", "").replace("\n", ", ")

    summary = f"""
{name} is a {education} candidate with strong skills in {skills_text}.

The candidate has experience in {experience}.

Strong interest in software development, artificial intelligence,
problem solving, and technology solutions.

Able to learn new technologies and contribute effectively
to professional software projects.
"""

    summary = summary.replace(", .", ".")
    summary = summary.replace(" .", ".")

    return summary.strip()