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

    print("TITLE =", title)
    print("SUMMARY =", summary[:50])

    pdf = FPDF()

    pdf.add_page()

        # ================= HEADER =================

    pdf.set_draw_color(30, 30, 30)
    pdf.set_line_width(0.8)
    pdf.line(10, 12, 200, 12)

    # Name
    print("PDF NAME:", name)
    print("PDF TITLE:", title)
    print("PDF SUMMARY:", summary[:100])
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 12, clean_text(name), ln=True, align="C")

    # Title

    pdf.set_font("Helvetica", "", 13)

    pdf.cell(
        0,
        8,
        "MSc Computer Science Candidate",
        ln=True,
        align="C"
    )

    # Contact Details
    pdf.set_font("Helvetica", "", 10)

    contact = f"{address} | {email} | {phone}"
    pdf.cell(0, 7, clean_text(contact), ln=True, align="C")

    # Links
    links = f"{linkedin} | {github}"
    pdf.cell(0, 7, clean_text(links), ln=True, align="C")

    pdf.ln(2)

    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    pdf.ln(6)

    # Template Name
    pdf.set_font("Helvetica", "B", 12)

    clean_template = (
        template
        .replace("🇺🇸", "")
        .replace("🇨🇦", "")
        .replace("🇬🇧", "")
        .replace("🇮🇳", "")
        .replace("🇦🇪", "")
        .replace("🤖", "")
        .replace("💻", "")
        .replace("☁", "")
        .replace("🔐", "")
        .replace("📊", "")
        .replace("🌐", "")
        .replace("🎓", "")
        .replace("👨‍💼", "")
        .replace("🚀", "")
        .replace("📚", "")
        .replace("✨", "")
        .replace("🖤", "")
        .replace("📄", "")
        .strip()
    )

    pdf.cell(0, 8, clean_template, ln=True, align="C")

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

        pdf.set_font("Helvetica", "B", 12)

        pdf.set_fill_color(240, 240, 240)

        pdf.cell(
            0,
            9,
            heading.upper(),
            ln=True,
            fill=True
        )

        pdf.ln(1)

        pdf.set_font("Helvetica", "", 11)

        if heading in [
            "Technical Skills",
            "Projects",
            "Certifications"
        ]:

            if "," in str(content):
                items = [
                    item.strip()
                    for item in str(content)
                    .replace("-", "")
                    .split(",")
                ]
            else:
                items = [item.strip() for item in str(content).splitlines()]

            for item in items:

                if item:
                    pdf.set_x(10)

                    pdf.multi_cell(
                        0,
                        7,
                        "- " + clean_text(item).lstrip("- ")
                    )

        else:

            pdf.multi_cell(
                0,
                7,
                clean_text(str(content))
            )

        pdf.ln(4)

    file = "AI_Professional_Resume.pdf"

    pdf.output(file)

    return file