import streamlit as st

st.set_page_config(page_title="AI Resume Builder")

st.title("AI Resume Builder")

name = st.text_input("Name")
skills = st.text_area("Skills")
education = st.text_area("Education")
experience = st.text_area("Experience")

if st.button("Generate Resume"):
    st.success("Resume Generated Successfully!")
    st.write("### Name")
    st.write(name)
    st.write("### Skills")
    st.write(skills)
    st.write("### Education")
    st.write(education)
    st.write("### Experience")
    st.write(experience)
