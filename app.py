import streamlit as st

from ai import generate_summary
from ats import calculate_ats_score
from pdf_generator import create_pdf


st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Builder")
st.write("Create Professional ATS Friendly Resume")


# Personal Details

st.header("👤 Personal Information")

name = st.text_input("Full Name")

title = st.text_input(
    "Professional Title",
    placeholder="Software Engineer / AI Engineer"
)

email = st.text_input("Email")

phone = st.text_input("Phone Number")

address = st.text_input(
    "Address / Location"
)


linkedin = st.text_input(
    "LinkedIn Profile"
)

github = st.text_input(
    "GitHub Profile"
)


# Resume Content

st.header("💼 Professional Details")


skills = st.text_area(
    "Technical Skills",
    placeholder="Python, Java, SQL, Machine Learning"
)


projects = st.text_area(
    "Projects"
)


education = st.text_area(
    "Education"
)


certifications = st.text_area(
    "Certifications"
)


experience = st.text_area(
    "Experience"
)


# Resume Templates

st.header("🎨 Choose Resume Template")

profile_photo = st.file_uploader(
    "Choose Profile Photo",
    type=["jpg", "jpeg", "png"]
)
template = st.selectbox(
    "Select Template",
    [
        "🇺🇸 USA ATS Resume",
        "🇨🇦 Canada ATS Resume",
        "🇬🇧 UK ATS Resume",
        "🇮🇳 India ATS Resume",
        "🇦🇪 Gulf ATS Resume",

        "Software Engineer Resume",
        "AI Engineer Resume",
        "Data Scientist Resume",
        "Fresh Graduate Resume",
        "Professional Modern Resume"
    ]
)
# Generate Resume Button

if st.button("🚀 Generate Resume"):
    

    st.success("✅ Resume Generated Successfully!")


    # AI Summary

    summary = generate_summary(
        name,
        skills,
        education,
        experience
    )
     
     # ATS Score

    score, matched_keywords, missing_keywords = calculate_ats_score(
        skills,
        education,
        experience,
        projects
    )
    
    st.subheader("✅ Strong Keywords Found")

    st.header("🤖 AI Generated Professional Summary")

    st.write(summary)

    st.header("📊 ATS Resume Score")

    st.progress(score / 100)

    st.write(
        f"Your ATS Score: {score}/100"
    )


    if matched_keywords:
        st.write(", ".join(matched_keywords))
    else:
        st.write("No strong keywords found")


    st.subheader("⚠ Missing Keywords")


    if missing_keywords:
        st.write(", ".join(missing_keywords))
    else:
        st.success("No missing keywords")


    st.subheader("💡 Resume Improvement Tips")

    if len(missing_keywords) > 5:
        st.warning(
            "Add more technical skills and project keywords to improve ATS score."
        )

    else:
        st.success(
            "Your resume keywords are looking good."
        )


    if score >= 90:

        st.success(
        "Excellent ATS Resume!"
     )

    elif score >= 70:

        st.warning(
            "Good Resume. Some improvements possible."
        )

    else:

        st.error(
            "Resume needs improvement."
        )



    # Resume Preview

    st.header("👀 Resume Preview")


    st.subheader(name)

    st.write(title)

    st.markdown(
    f"""
**{name}**

*{title}*

📍 {address} | 📧 {email} | 📞 {phone}

🔗 {linkedin} | 💻 {github}
"""
)


    st.markdown("## 💻 Technical Skills")

    st.write(skills)


    st.markdown("## 🚀 Projects")

    st.write(projects)


    st.markdown("## 🎓 Education")

    st.write(education)


    st.markdown("## 📜 Certifications")

    st.write(certifications)


    st.markdown("## 💼 Experience")

    st.write(experience)



    # Create PDF

    pdf_file = create_pdf(
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
    )


    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Resume PDF",
            data=file,
            file_name="AI_Professional_Resume.pdf",
            mime="application/pdf"
        )
        