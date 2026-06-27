import streamlit as st

from generator.prompt_builder import create_prompt
from generator.letter_generator import generate_letter
from utils.pdf_export import create_pdf

from resume_parser.parser import extract_resume_text
from resume_parser.extractor import extract_information
from analyzer.matcher import analyze_match
from analyzer.score import calculate_score
from analyzer.suggestions import generate_suggestions
from utils.docx_export import create_docx
from job_assistant.job_matcher import compare_jobs
from job_assistant.recommender import recommend_best

from authentication.auth import (
    create_user,
    login_user
)

from database.database import (
    init_db,
    save_letter,
    get_letters
)
init_db()
# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="CoverCraft",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------------
# LOAD CSS
# ---------------------------------------------------------

with open("assets/style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("📄 CoverCraft")

st.sidebar.markdown("---")

page = st.sidebar.radio(

    "Navigation",

    [

        "🔐 Login",

        "📝 Signup",

        "🏠 Home",

        "📚 History",

        "ℹ About"

    ]

)

if "username" in st.session_state:


    st.sidebar.success(

        f"👤 {st.session_state.username}"

    )


    if st.sidebar.button("Logout"):

        del st.session_state.username

        st.success(
            "Logged out successfully"
        )

        st.rerun()



st.sidebar.info(
"""
CoverCraft v7.0

Powered by

Ollama + Llama 3
"""
)

# =========================================================
# LOGIN
# =========================================================

if page=="🔐 Login":

    st.title("Login")


    username = st.text_input(
        "Username",
        width=400
    )


    password = st.text_input(
        "Password",
        type="password",
        width=400
    )


    if st.button("Login"):


        user = login_user(
            username,
            password
        )


        if user:

            st.session_state.username = username

            st.success(
                "Login successful"
            )

            st.rerun()


        else:

            st.error(
                "Invalid login"
            )
# ==========================================================
# HOME
# ==========================================================
# =========================================================
# SIGNUP
# =========================================================

if page=="📝 Signup":


    st.title("Create Account")


    username = st.text_input(
        "Username",
        width=400
    )


    password = st.text_input(
        "Password",
        type="password",
        width=400
    )



    if st.button("Signup"):


        result = create_user(

            username,

            password

        )


        if result:

            st.success(
                "Account created!"
            )


        else:

            st.error(
                "Username already exists"
            )
if page == "🏠 Home":

    st.title("📄 CoverCraft")

    st.markdown(
        "### Generate Professional Cover Letters"
    )

    st.write("")

    # ---------------------------------------------------------
    # Resume Upload
    # ---------------------------------------------------------

    uploaded_resume = st.file_uploader(
        "📄 Upload Resume (PDF)",
        type=["pdf"]
    )

    extracted = {}
    resume_text = ""

    if uploaded_resume is not None:

        try:

            resume_text = extract_resume_text(uploaded_resume)

            extracted = extract_information(resume_text)

            st.success("✅ Resume uploaded successfully!")

        except Exception as e:

            st.error(f"Unable to read resume.\n\n{e}")

    # ---------------------------------------------------------

    left, right = st.columns([1, 1])

    # ======================================================
    # LEFT COLUMN
    # ======================================================

    with left:

        st.subheader("Candidate Information")

        name = st.text_input(
            "Full Name",
            value=extracted.get("name", "")
        )

        job = st.text_input("Job Role")

        company = st.text_input("Company Name")

        email = st.text_input(
            "Email",
            value=extracted.get("email", "")
        )

        phone = st.text_input(
            "Phone Number",
            value=extracted.get("phone", "")
        )

        github = st.text_input(
            "GitHub",
            value=extracted.get("github", "")
        )

        linkedin = st.text_input(
            "LinkedIn",
            value=extracted.get("linkedin", "")
        )

        skills = st.text_area(
            "Technical Skills",
            value=extracted.get("skills", ""),
            height=120
        )

        soft_skills = st.text_area(
            "Soft Skills",
            value=extracted.get("soft_skills", ""),
            height=90
        )

        experience = st.text_area(
            "Experience",
            value=extracted.get("experience", ""),
            height=140
        )

        education = st.text_area(
            "Education",
            value=extracted.get("education", ""),
            height=120
        )

        projects = st.text_area(
            "Projects",
            value=extracted.get("projects", ""),
            height=120
        )

        certifications = st.text_area(
            "Certifications",
            value=extracted.get("certifications", ""),
            height=120
        )
        st.markdown("---")

        st.subheader("📄 Job Description")

        job_description = st.text_area(
            "Paste Job Description",
           height=220,
           placeholder="Paste the job description here..."
        )
        st.markdown("---")


        st.subheader(
           "Smart Job Assistant"
        )


        job1 = st.text_area(
          "Job 1 Description"
        )


        job2 = st.text_area(
           "Job 2 Description"
        )


        job3 = st.text_area(
           "Job 3 Description"
        )


        compare = st.button(
           "Compare Jobs"
        )

        tone = st.selectbox(
            "Select Tone",
            [
                "Professional",
                "Friendly",
                "Confident"
            ]
        )

        generate = st.button(
            "Generate Cover Letter"
        )

    # ======================================================
    # RIGHT COLUMN
    # ======================================================

    with right:

        st.subheader("Generated Cover Letter")

        preview = st.empty()
        st.markdown("---")

        st.subheader(" Resume Analysis")

        score_placeholder = st.empty()

        matched_placeholder = st.empty()

        missing_placeholder = st.empty()

# ======================================================
# GENERATE
# ======================================================

    if generate:


        if not all([
            name,
            job,
            company,
            skills,
            experience
        ]):


            st.warning(
                "Please fill all required information before generating."
            )

            st.stop()



        prompt = create_prompt(

            name,

            job,

            company,

            skills,

            experience,

            tone

        )


        status = st.empty()


        status.info(
            "⏳ Generating Cover Letter..."
        )


        letter = generate_letter(prompt)


        status.success(
            "✅ Cover Letter Generated Successfully!"
        )    


        # -----------------------------
        # Resume Job Matching Analysis
        # -----------------------------

        analysis = analyze_match(

            resume_text,

            job_description

        )


        score = calculate_score(

            analysis

        )


        # ATS SCORE DISPLAY


        if score >= 85:

           status = "Excellent"


        elif score >= 70:

           status = "Good"


        else:

           status = "Need Improvement 🔴"



        score_placeholder.metric(

           "ATS Resume Score",

            f"{score}%",

            status

        )


        st.progress(

           score / 100

        )


        matched_placeholder.success(

            "Matched Skills:\n\n"

            +

            ", ".join(

                analysis["matched"]

            )

        )


        missing_placeholder.warning(

            "Missing Skills:\n\n"

            +

            ", ".join(

                analysis["missing"]

            )

        )
        suggestions = generate_suggestions(

            analysis["missing"]

        )


        st.subheader(
            "Resume Improvement Suggestions"
        )


        for suggestion in suggestions:

           st.info(
               suggestion
            )



        # -----------------------------
        # Create Prompt
        # -----------------------------


        prompt = create_prompt(

            name,

            job,

            company,

            skills,

            experience,

            tone,

            job_description,

            ", ".join(

                analysis["missing"]

            )

        )



        status = st.empty()


        status.info(

            "⏳ Generating Cover Letter..."

        )


        letter = generate_letter(prompt)

        # SAVE LETTER TO DATABASE

        if "username" in st.session_state:


            save_letter(

                st.session_state.username,

                letter

            )


        st.balloons()

        status.success(
          "✅ Cover Letter Generated Successfully!"
        )
        st.session_state.generate_clicked = False


        preview.text_area(

            "",

            letter,

            height=600

        )



        pdf = create_pdf(letter)

        docx = create_docx(letter)

        with open(pdf, "rb") as file:


            st.download_button(

                "Download PDF",

                file,

                file_name="Cover_Letter.pdf",

                mime="application/pdf"

            )
            with open(docx,"rb") as file:


                st.download_button(

                    "Download DOCX",

                    file,

                    file_name="Cover_Letter.docx",

                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"

             )
            
            if compare:


                jobs = {

                  "Job 1": job1,

                  "Job 2": job2,

                  "Job 3": job3

                }


                results = compare_jobs(

                    resume_text,

                    jobs

                )


                st.subheader(
                     "Job Ranking"
                )


                for result in results:

                  st.write(

                      result["job"],

                      "➡",

                      result["score"],

                      "%"

                    )


                best = recommend_best(results)


                st.success(

                   f"Best Matching Job: {best['job']}"

                )

# ==========================================================
# History
# ==========================================================
if page == "📚 History":


    st.title(
        "Cover Letter History"
    )


    if "username" not in st.session_state:


        st.warning(
            "Please login first."
        )


    else:


        letters = get_letters(

            st.session_state.username

        )


        if not letters:


            st.info(
                "No saved letters found."
            )


        else:


            for index, item in enumerate(letters):


                st.subheader(

                    f"Letter {index+1}"

                )


                st.text_area(

                    "",

                    item[0],

                    height=300

                )
# ==========================================================
# ABOUT
# ==========================================================

if page == "ℹ About":

    st.title("About CoverCraft")

    st.write("""

## CoverCraft

CoverCraft is a professional Cover Letter Generator powered by a Local LLM using Ollama.

### Version 3 Features

✅ Resume Upload

✅ Automatic Resume Parsing

✅ Name Extraction

✅ Email Extraction

✅ Phone Extraction

✅ GitHub Detection

✅ LinkedIn Detection

✅ Technical Skills Detection

✅ Soft Skills Detection

✅ Education Extraction

✅ Projects Extraction

✅ Certifications Extraction

✅ Cover Letter Generation

✅ PDF Export

""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;color:gray;">

© 2026 CoverCraft

Developed by Pranali Jiritkhan ❤️

</div>
""",
unsafe_allow_html=True
)