import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

from question_bank import generate_random_questions

from agents import (
    screen_resume,
    evaluate_interview
)

from resume_parser import (
    extract_resume_text
)

# =====================================================
# GEMINI SETUP
# =====================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Multi-Agent Recruitment System",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #1e293b
    );
}

section[data-testid="stSidebar"]{
    background:#020617;
}

h1,h2,h3{
    color:#60a5fa !important;
}

div[data-testid="stMetric"]{
    background:rgba(30,41,59,0.8);
    border-radius:16px;
    padding:20px;
    border:1px solid #334155;
}

div[data-testid="stFileUploader"]{
    background:rgba(30,41,59,0.8);
    border-radius:16px;
    padding:20px;
}

.stTextInput,
.stSelectbox,
.stTextArea{
    border-radius:12px;
}

.stButton > button{
    width:100%;
    border:none;
    border-radius:12px;
    padding:12px;
    font-weight:bold;
    background:linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    );
    color:white;
}

.stButton > button:hover{
    transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🤖 AI Recruitment Platform")

    st.success("✅ Resume Screening Agent")
    st.success("✅ Question Engine")
    st.success("✅ Interview Engine")
    st.success("✅ Evaluation Agent")

    st.markdown("---")

    st.info(
        """
AI Multi-Agent Recruitment System

Version 3.0
"""
    )

# =====================================================
# SESSION STATE
# =====================================================

if "resume_report" not in st.session_state:
    st.session_state.resume_report = None

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "resume_analyzed" not in st.session_state:
    st.session_state.resume_analyzed = False

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

# =====================================================
# HEADER
# =====================================================

col1,col2 = st.columns([5,1])

with col1:

    st.title(
        "🤖 AI Multi-Agent Recruitment System"
    )

    st.caption(
        "AI-Powered Resume Screening • Interview Assessment • Hiring Intelligence"
    )

with col2:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=90
    )

st.markdown("---")

st.markdown("### Recruitment Pipeline")

p1,p2,p3,p4 = st.columns(4)

p1.success("📄 Resume")

if st.session_state.resume_analyzed:
    p2.success("✅ Screened")
else:
    p2.info("⏳ Screening")

if st.session_state.interview_started:
    p3.success("🎤 Interview")
elif st.session_state.interview_completed:
    p3.success("🎤 Completed")
else:
    p3.info("⏳ Waiting")

if st.session_state.evaluation_report:
    p4.success("📊 Evaluated")
else:
    p4.info("⏳ Pending")

st.markdown("---")

# =====================================================
# CANDIDATE DETAILS
# =====================================================

st.markdown("""
## 👤 Candidate Profile

Provide candidate details before starting recruitment analysis.
""")

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
    [
        5,
        10,
        15
    ]
)

# =====================================================
# RESUME UPLOAD
# =====================================================

st.markdown("---")

st.header("📄 Resume Intelligence Engine")

st.caption(
    "Upload PDF or DOCX resumes for AI-powered screening and candidate assessment."
)

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_resume:

    if st.button("📄 Analyze Resume"):

        with st.spinner(
            "Analyzing Resume..."
        ):

            try:

                resume_text = extract_resume_text(
                    uploaded_resume
                )

                report = screen_resume(
                    resume_text,
                    role,
                    model
                )

                st.session_state.resume_text = (
                    resume_text
                )

                st.session_state.resume_report = (
                    report
                )

                st.session_state.resume_analyzed = (
                    True
                )

                st.success(
                    "Resume Analysis Complete"
                )

            except Exception as e:

                st.error(
                    f"Resume Analysis Error: {str(e)}"
                )

if st.session_state.resume_report:

    st.subheader(
        "📑 Resume Screening Report"
    )

    st.markdown(
        st.session_state.resume_report
    )

    st.download_button(
        label="📥 Download Resume Report",
        data=st.session_state.resume_report,
        file_name="Resume_Report.txt",
        mime="text/plain"
    )

# =====================================================
# START INTERVIEW
# =====================================================

st.markdown("---")

if (
    not st.session_state.interview_started
    and not st.session_state.interview_completed
):

    if st.session_state.resume_analyzed:

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

            st.session_state.questions = (
                questions
            )

            st.session_state.answers = []

            st.session_state.question_index = 0

            st.session_state.candidate_profile = {

                "name": candidate_name,
                "role": role,
                "experience": experience,
                "question_count": question_count

            }

            st.session_state.interview_started = (
                True
            )

            st.rerun()

    else:

        st.info(
            "Analyze the resume to unlock the interview."
        )

# =====================================================
# INTERVIEW SECTION
# =====================================================

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

# =====================================================
# INTERVIEW REPORT
# =====================================================

if st.session_state.interview_completed:

    st.success(
        "🎉 Interview Completed"
    )

    st.header(
        "📋 Candidate Dashboard"
    )

if not st.session_state.candidate_profile:

    st.warning(
        "Candidate profile not found. Please start a new interview."
    )

    st.stop()

    col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Role",
    st.session_state.candidate_profile.get(
        "role",
        "N/A"
    )
)

col2.metric(
    "Experience",
    st.session_state.candidate_profile.get(
        "experience",
        "N/A"
    )
)

col3.metric(
    "Questions",
    st.session_state.candidate_profile.get(
        "question_count",
        "N/A"
    )
)

col4.metric(
    "Status",
    "Completed"
)
st.markdown("---")

if st.button(
        "🤖 Generate AI Evaluation"
    ):

        with st.spinner(
            "Generating Evaluation..."
        ):

            report = evaluate_interview(
                st.session_state.candidate_profile,
                st.session_state.answers,
                model
            )

            st.session_state.evaluation_report = (
                report
            )

if st.session_state.evaluation_report:

        st.header(
            "📊 AI Evaluation Report"
        )

        st.markdown(
            st.session_state.evaluation_report
        )

        st.download_button(
            label="📥 Download Interview Report",
            data=st.session_state.evaluation_report,
            file_name="Interview_Report.txt",
            mime="text/plain"
        )

if st.button(
        "🔄 Start New Interview"
    ):

        st.session_state.clear()

        st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Developed by Venkata Sai Sri Harsha Sharma"
)