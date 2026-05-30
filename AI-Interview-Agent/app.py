import streamlit as st

from question_bank import generate_random_questions
from agents import evaluate_interview

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="AI Interview Agent",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------
# SIDEBAR
# --------------------------------

with st.sidebar:

    st.title("🤖 AI Interview Platform")

    st.success("Question Engine")
    st.success("Interview Engine")
    st.success("Memory Engine")
    st.success("Evaluation Engine")

# --------------------------------
# SESSION STATE
# --------------------------------

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

# --------------------------------
# HEADER
# --------------------------------

st.title("🤖 AI Interview Agent")

st.subheader(
    "Professional Candidate Assessment Platform"
)

# --------------------------------
# CANDIDATE DETAILS
# --------------------------------

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

# --------------------------------
# START INTERVIEW
# --------------------------------

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

        generated_questions = generate_random_questions(
            role,
            question_count
        )

        st.session_state.candidate_profile = {
            "name": candidate_name,
            "role": role,
            "experience": experience,
            "question_count": question_count
        }

        st.session_state.questions = generated_questions

        st.session_state.interview_started = True

        st.session_state.question_index = 0

        st.session_state.answers = []

        st.session_state.evaluation_report = None

        st.rerun()

# --------------------------------
# INTERVIEW
# --------------------------------

if st.session_state.interview_started:

    total_questions = len(
        st.session_state.questions
    )

    current_index = (
        st.session_state.question_index
    )

    progress = current_index / total_questions

    st.progress(progress)

    current_question = (
        st.session_state.questions[
            current_index
        ]
    )

    st.subheader(
        f"Question {current_index + 1}"
    )

    st.write(current_question)

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
                "question": current_question,
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

# --------------------------------
# REPORT
# --------------------------------

if st.session_state.interview_completed:

    st.success(
        "🎉 Interview Completed"
    )

    st.header(
        "📋 Candidate Summary"
    )
    col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Role",
        st.session_state.candidate_profile["role"]
    )

with col2:

    st.metric(
        "Experience",
        st.session_state.candidate_profile["experience"]
    )

with col3:

    st.metric(
        "Questions",
        st.session_state.candidate_profile["question_count"]
    )

    st.json(
        st.session_state.candidate_profile
    )

    if st.button(
        "Generate Evaluation Report"
    ):

        report = evaluate_interview(
            st.session_state.candidate_profile,
            st.session_state.answers
        )

        st.session_state.evaluation_report = report

    if st.session_state.evaluation_report:

        st.download_button(
    label="📥 Download Report",

    data=st.session_state.evaluation_report,

    file_name="Interview_Report.txt",

    mime="text/plain"
)

        st.markdown(
            st.session_state.evaluation_report
        )

    if st.button(
        "🔄 Start New Interview"
    ):

        st.session_state.clear()

        st.rerun()