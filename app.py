import streamlit as st
import base64

st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)


def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

bg = get_base64_image("background.png")

st.markdown("""
<style>

/* ===============================
   BACKGROUND
================================ */

.stApp {

background:

linear-gradient(
rgba(0,15,40,0.45),
rgba(0,15,40,0.45)
),

url("BG_IMAGE");

background-size:cover;

background-position:center;

background-attachment:fixed;

}



/* ===============================
   MAIN PANEL
================================ */

.stMainBlockContainer {

max-width:1000px !important;

margin:auto !important;


background:

rgba(255,255,255,0.05);



border:

1.5px solid rgba(0,255,255,0.45);



border-radius:

25px;



padding:

35px !important;



box-shadow:

0 0 30px rgba(0,255,255,0.25);

}





/* ===============================
   HEADINGS
================================ */

h1,h2,h3,h4 {

color:#00ffff !important;

font-weight:800 !important;

text-shadow:

0 0 10px #00ffff;

}





/* ===============================
   NORMAL TEXT OUTPUT
================================ */


.stMarkdown,
.stMarkdown p,
.stMarkdown li,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {

color:white !important;

font-size:18px !important;

}





/* ===============================
   LABELS
================================ */

.stTextInput label,
.stTextArea label,
.stSelectbox label {

color:white !important;

font-size:18px !important;

font-weight:bold !important;

}





/* ===============================
   INPUT BOXES AQUA GLASS
================================ */


.stTextInput,
.stTextArea,
.stSelectbox {

max-width:720px !important;

margin:auto !important;

margin-bottom:18px !important;

}




div[data-baseweb="input"] > div,
div[data-baseweb="base-input"],
div[data-baseweb="textarea"] {


background:

rgba(0,255,255,0.18) !important;



border:

2px solid rgba(0,255,255,0.75) !important;



border-radius:

14px !important;



box-shadow:

0 0 15px rgba(0,255,255,0.30);


}





/* ===============================
   ONLY INPUT TEXT BLACK
================================ */


div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {


background:

transparent !important;



color:

#000000 !important;



-webkit-text-fill-color:

#000000 !important;



font-size:

19px !important;



font-weight:

600 !important;


}





/* PLACEHOLDER */

input::placeholder,
textarea::placeholder {

color:

rgba(0,0,0,0.55) !important;

}





/* ===============================
   TEXT AREA SIZE
================================ */

div[data-baseweb="input"] input {

height:

48px !important;

}


div[data-baseweb="textarea"] textarea {

min-height:

100px !important;

}





/* ===============================
   BUTTON
================================ */


.stButton button {


background:

linear-gradient(
90deg,
#00ffff,
#0072ff
) !important;



color:white !important;



width:240px;



height:50px;



border-radius:25px;



font-size:18px;



font-weight:bold;



border:none;



box-shadow:

0 0 25px #00ffff;


}





/* ===============================
   ALERT BOX
================================ */


.stAlert {

background:

rgba(0,255,255,0.12) !important;



color:white !important;



border-radius:15px !important;

}





/* ===============================
   RESUME PREVIEW
================================ */


.resume-container {


background:

rgba(0,255,255,0.10);



border:

2px solid rgba(0,255,255,0.60);



border-radius:

20px;



padding:

25px;


}



.resume-container * {

color:white !important;

}





</style>
""".replace("BG_IMAGE", f"data:image/png;base64,{bg}"),
unsafe_allow_html=True)

from ai import generate_summary
from ats import calculate_ats_score
from pdf_generator import create_pdf

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
    "Address / Location",
    placeholder="Amravati, Maharashtra"
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
    
    if score >= 90:

        st.success("🟢 Excellent ATS Resume (90-100)")

    elif score >= 75:

        st.info("🟡 Very Good ATS Resume (75-89)")

    elif score >= 60:

        st.warning("🟠 Average ATS Resume (60-74)")

    else:

        st.error("🔴 ATS Resume Needs Improvement")


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
    st.write("DEBUG BEFORE PDF")
    st.write("TITLE VALUE:", title)
    st.write("SUMMARY VALUE:", summary)

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
        