from fpdf import FPDF


def clean_text(text):
    if not text:
        return ""

    replacements = {
        "•": "-",
        "–": "-",
        "—": "-",
        "’": "'",
        "“": '"',
        "”": '"',
        "📧": "",
        "📞": "",
        "📍": "",
        "🔗": "",
        "💻": "",
        "🇺": "",
        "🇸": "",
        "🇨": "",
        "🇦": "",
        "🇬": "",
        "🇧": "",
        "🇮": "",
        "🇪": ""
 }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def create_pdf(
    name,
    title,
    email,
    phone,
    address,
    linkedin,
    github,
    skills,
    projects,
    education,
    certifications,
    experience,
    summary,
    template
):

    pdf = FPDF()

    pdf.add_page()

    # Header Name

    pdf.set_font(
        "Helvetica",
        "B",
        20
    )

    pdf.cell(
        0,
        12,
        clean_text(name),
        ln=True,
        align="C"
    )


    # Professional Title

    pdf.set_font(
        "Helvetica",
        "",
        12
    )

    pdf.cell(
        0,
        8,
        clean_text(title),
        ln=True,
        align="C"
    )


    # Contact Line

    pdf.set_font(
        "Helvetica",
        "",
        10
    )

    contact = (
        f"{address} | {email} | {phone}"
    )

    pdf.cell(
        0,
        8,
        clean_text(contact),
        ln=True,
        align="C"
    )


    # Links

    links = (
        f"{linkedin} | {github}"
    )

    pdf.cell(
        0,
        8,
        clean_text(links),
        ln=True,
        align="C"
    )


    pdf.ln(8)



    # Template Name

    pdf.set_font(
        "Helvetica",
        "B",
        13
    )

    clean_template = (
    template
    .replace("🇺🇸", "")
    .replace("🇨🇦", "")
    .replace("🇬🇧", "")
    .replace("🇮🇳", "")
    .replace("🇦🇪", "")
    .strip()
    )


    pdf.cell(
        0,
        10,
        clean_template,
        ln=True
    )

    pdf.ln(5)



    sections = [

        ("Professional Summary", summary),

        ("Technical Skills", skills),

        ("Projects", projects),

        ("Education", education),

        ("Certifications", certifications),

        ("Experience", experience)

    ]



    for heading, content in sections:


        pdf.set_font(
            "Helvetica",
            "B",
            12
        )


        pdf.cell(
            0,
            9,
            heading,
            ln=True
        )


        pdf.set_font(
            "Helvetica",
            "",
            11
        )


        pdf.multi_cell(
            0,
            7,
            clean_text(content)
        )


        pdf.ln(4)



    file = "AI_Professional_Resume.pdf"


    pdf.output(file)


    return file