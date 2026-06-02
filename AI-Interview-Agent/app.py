import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

from question_bank import generate_random_questions
from agents import evaluate_interview

# =====================================
# GEMINI SETUP
# =====================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Recruitment Platform",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("🤖 AI Recruitment Platform")

    st.success("✅ Question Engine")
    st.success("✅ Interview Engine")
    st.success("✅ Memory Engine")
    st.success("✅ AI Evaluation Engine")

    st.markdown("---")

    st.info("""
Professional Candidate Assessment System

Version 2.0
""")

# =====================================
# SESSION STATE
# =====================================

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

if "interview_completed" not in st.session_state:
    st.session_state.interview_completed = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "candidate_profile" not in st.session_state:
    st.session_state.candidate_profile = {}

if "evaluation_report" not in st.session_state:
    st.session_state.evaluation_report = None

# =====================================
# HEADER
# =====================================

st.title("🤖 AI Recruitment & Assessment Platform")

st.caption(
    "AI-Powered Candidate Screening System"
)

# =====================================
# CANDIDATE FORM
# =====================================

candidate_name = st.text_input(
    "Candidate Name"
)

role = st.selectbox(
    "Select Role",
    [
        "Java Developer",
        "Python Developer",
        "AI Engineer",
        "Data Analyst",
        "Full Stack Developer",
        "Cyber Security Analyst",
        "Cloud Engineer",
        "DevOps Engineer",
        "Backend Developer",
        "Frontend Developer",
        "Software Engineer",
        "Data Engineer",
        "Business Analyst",
        "QA Engineer",
        "Mobile App Developer"
    ]
)

experience = st.selectbox(
    "Experience Level",
    [
        "Fresher",
        "1-3 Years",
        "3-5 Years",
        "5+ Years"
    ]
)

question_count = st.selectbox(
    "Number of Questions",
    [5, 10, 15]
)

# =====================================
# START INTERVIEW
# =====================================

if (
    not st.session_state.interview_started
    and not st.session_state.interview_completed
):

    if st.button("🚀 Start Interview"):

        if candidate_name.strip() == "":
            st.warning(
                "Please enter candidate name."
            )
            st.stop()

        questions = generate_random_questions(
            role,
            question_count
        )

        st.session_state.questions = questions

        st.session_state.candidate_profile = {
            "name": candidate_name,
            "role": role,
            "experience": experience,
            "question_count": question_count
        }

        st.session_state.answers = []

        st.session_state.question_index = 0

        st.session_state.interview_started = True

        st.rerun()

# =====================================
# INTERVIEW SECTION
# =====================================

if st.session_state.interview_started:

    total_questions = len(
        st.session_state.questions
    )

    current_index = (
        st.session_state.question_index
    )

    progress = current_index / total_questions

    st.progress(progress)

    question = (
        st.session_state.questions[
            current_index
        ]
    )

    st.subheader(
        f"Question {current_index + 1} of {total_questions}"
    )

    st.write(question)

    answer = st.text_area(
        "Your Answer"
    )

    if st.button("Submit & Next"):

        if answer.strip() == "":
            st.warning(
                "Please enter an answer."
            )
            st.stop()

        st.session_state.answers.append(
            {
                "question": question,
                "answer": answer
            }
        )

        st.session_state.question_index += 1

        if (
            st.session_state.question_index
            >= total_questions
        ):

            st.session_state.interview_started = False

            st.session_state.interview_completed = True

        st.rerun()

# =====================================
# REPORT SECTION
# =====================================

if st.session_state.interview_completed:

    st.success(
        "🎉 Interview Completed"
    )

    st.header(
        "📋 Candidate Dashboard"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Role",
        st.session_state.candidate_profile["role"]
    )

    col2.metric(
        "Experience",
        st.session_state.candidate_profile["experience"]
    )

    col3.metric(
        "Questions",
        st.session_state.candidate_profile["question_count"]
    )

    st.markdown("---")

    if st.button(
        "🤖 Generate AI Evaluation"
    ):

        with st.spinner(
            "AI Agent Evaluating Candidate..."
        ):

            report = evaluate_interview(
                st.session_state.candidate_profile,
                st.session_state.answers,
                model
            )

            st.session_state.evaluation_report = report

    if st.session_state.evaluation_report:

        st.header(
            "📊 AI Evaluation Report"
        )

        st.markdown(
            st.session_state.evaluation_report
        )

        st.download_button(
            label="📥 Download Report",
            data=st.session_state.evaluation_report,
            file_name="AI_Interview_Report.txt",
            mime="text/plain"
        )

    if st.button(
        "🔄 Start New Interview"
    ):

        st.session_state.clear()

        st.rerun()

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "Developed by Venkata Sai Sri Harsha Sharma"
)