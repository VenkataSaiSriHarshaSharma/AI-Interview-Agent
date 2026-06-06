from backend.services.gemini_service import generate_content


# =====================================================
# RESUME SCREENING AGENT
# =====================================================

def screen_resume(
    resume_text,
    target_role,
    model
):

    prompt = f"""
You are an expert AI Resume Screening Agent.

Target Role:
{target_role}

Resume Content:
{resume_text}

Analyze the resume and provide ONLY:

1. Candidate Summary (2-3 lines)

2. Key Technical Skills

3. Strengths

4. Missing Skills

5. Resume Match Score (0-100)

6. Final Recommendation
   (SHORTLISTED / CONSIDER / REJECT)

Rules:
- Keep the report concise.
- Maximum 400 words.
- Use bullet points where appropriate.
- Resume Match Score must be a single numeric value.
- Final Recommendation must appear at the end.

Format professionally.
"""

    try:
        return generate_content(prompt)

    except Exception as e:
        return (
            f"Resume Screening Error:\n{str(e)}"
        )


# =====================================================
# COMMUNICATION AGENT
# =====================================================

def evaluate_communication(
    answers,
    model=None
):

    prompt = f"""
You are a Communication Assessment Agent.

Candidate Responses:

{answers}

Evaluate:

1. Communication Score (0-100)

2. Confidence Level

3. Grammar Quality

4. Clarity of Explanation

5. Professionalism

6. Areas of Improvement

Generate a professional report.
"""

    try:

        return generate_content(prompt)

    except Exception as e:

        return (
            f"Communication Analysis Error:\n{str(e)}"
        )


# =====================================================
# SKILL EVALUATION AGENT
# =====================================================

def evaluate_skills(
    resume_text,
    answers,
    model=None
):

    prompt = f"""
You are a Skill Verification Agent.

Resume Content:
{resume_text}

Interview Responses:
{answers}

Compare the skills claimed in the resume
with the skills demonstrated during the interview.

Generate:

1. Demonstrated Skills

2. Claimed Skills

3. Skill Authenticity Score (0-100)

4. Skill Gaps

5. Recommendations
"""

    try:

        return generate_content(prompt)

    except Exception as e:

        return (
            f"Skill Evaluation Error:\n{str(e)}"
        )


# =====================================================
# TECHNICAL INTERVIEW AGENT
# =====================================================

def evaluate_interview(
    candidate_profile,
    answers,
    model=None
):

    prompt = f"""
You are a Senior Technical Interviewer and Hiring Manager.

Candidate Information:
{candidate_profile}

Interview Responses:
{answers}

Analyze the interview thoroughly.

Generate:

# Candidate Evaluation Report

## Technical Score (0-100)

## Communication Score (0-100)

## Problem Solving Score (0-100)

## Candidate Rating
A+
A
B+
B
C

## Hiring Recommendation
SELECT
CONSIDER
REJECT

## Strengths

## Areas for Improvement

## Learning Roadmap

## Final Summary
"""

    try:

        return generate_content(prompt)

    except Exception as e:

        return (
            f"Interview Evaluation Error:\n{str(e)}"
        )


# =====================================================
# HIRING RECOMMENDATION AGENT
# =====================================================

def hiring_recommendation(
    resume_report,
    communication_report,
    skill_report,
    interview_report,
    model=None
):

    prompt = f"""
You are a Hiring Decision Agent.

Resume Report:
{resume_report}

Communication Report:
{communication_report}

Skill Evaluation:
{skill_report}

Interview Evaluation:
{interview_report}

Generate:

1. Final Hiring Status
(SELECT / CONSIDER / REJECT)

2. Confidence Percentage

3. Justification

4. Recruiter Notes

5. Final Recommendation
"""

    try:

        return generate_content(prompt)

    except Exception as e:

        return (
            f"Hiring Recommendation Error:\n{str(e)}"
        )


# =====================================================
# FINAL REPORT AGENT
# =====================================================

def generate_final_report(
    resume_report,
    communication_report,
    skill_report,
    interview_report,
    hiring_report,
    model=None
):

    prompt = f"""
Generate a Final Recruitment Report.

Resume Analysis:
{resume_report}

Communication Analysis:
{communication_report}

Skill Analysis:
{skill_report}

Interview Analysis:
{interview_report}

Hiring Decision:
{hiring_report}

Generate:

1. Candidate Profile Summary

2. Resume Match Score

3. Technical Assessment

4. Communication Assessment

5. Skill Gap Analysis

6. Hiring Recommendation

7. Learning Roadmap

8. Final Recruiter Summary

Format professionally.
"""

    try:

        return generate_content(prompt)

    except Exception as e:

        return (
            f"Final Report Error:\n{str(e)}"
        )