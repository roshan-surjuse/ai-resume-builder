from fpdf import FPDF


def clean_text(text):
    """
    Remove unsupported characters for PDF
    """
    replacements = {
        "•": "-",
        "–": "-",
        "—": "-",
        "’": "'",
        "“": '"',
        "”": '"'
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


    # Header

    pdf.set_font(
        "Helvetica",
        "B",
        18
    )

    pdf.cell(
        0,
        10,
        clean_text(name),
        ln=True,
        align="C"
    )


    pdf.set_font(
        "Helvetica",
        "B",
        12
    )

    pdf.cell(
        0,
        8,
        clean_text(title),
        ln=True,
        align="C"
    )


    # Contact

    pdf.set_font(
        "Helvetica",
        size=10
    )


    contact = f"{address} | {email} | {phone}"

    pdf.cell(
        0,
        8,
        clean_text(contact),
        ln=True,
        align="C"
    )


    links = f"{linkedin} | {github}"

    pdf.cell(
        0,
        8,
        clean_text(links),
        ln=True,
        align="C"
    )


    pdf.ln(8)



    # Template

    pdf.set_font(
        "Helvetica",
        "B",
        13
    )

    pdf.cell(
        0,
        10,
        clean_text(template.replace("🇺🇸","")
                          .replace("🇨🇦","")
                          .replace("🇬🇧","")
                          .replace("🇮🇳","")
                          .replace("🇦🇪","")),
        ln=True
    )



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
            10,
            heading,
            ln=True
        )


        pdf.set_font(
            "Helvetica",
            size=11
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