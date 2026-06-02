import google.generativeai as genai


def evaluate_interview(candidate_profile, answers, model):

    prompt = f"""
You are a Senior Technical Interviewer and Hiring Manager.

Candidate Information:
{candidate_profile}

Interview Responses:
{answers}

Analyze the interview thoroughly.

Generate the report in the following format:

# Candidate Evaluation Report

## Technical Score
Provide a score out of 100.

## Communication Score
Provide a score out of 100.

## Problem Solving Score
Provide a score out of 100.

## Candidate Rating
Assign one:
A+
A
B+
B
C

## Hiring Recommendation
Choose one:
SELECT
CONSIDER
REJECT

## Strengths
Provide 3-5 strengths.

## Areas for Improvement
Provide 3-5 improvement areas.

## Learning Roadmap
Provide a personalized learning plan.

## Final Summary
Provide overall assessment.
"""

    response = model.generate_content(prompt)

    return response.text