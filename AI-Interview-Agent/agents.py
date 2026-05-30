def evaluate_interview(candidate_profile, answers):

    total_questions = len(answers)

    answered = sum(
        1 for item in answers
        if item["answer"].strip()
    )

    score = (
        answered / total_questions
    ) * 100

    if score >= 90:

        decision = "SELECT"
        rating = "A+"

    elif score >= 80:

        decision = "SELECT"
        rating = "A"

    elif score >= 70:

        decision = "CONSIDER"
        rating = "B+"

    elif score >= 60:

        decision = "CONSIDER"
        rating = "B"

    else:

        decision = "REJECT"
        rating = "C"

    report = f"""
# Candidate Evaluation Report

## Candidate Information

Name:
{candidate_profile['name']}

Role:
{candidate_profile['role']}

Experience:
{candidate_profile['experience']}

## Performance Metrics

Completion Score:
{score:.2f}%

Candidate Rating:
{rating}

Hiring Recommendation:
{decision}

## Strengths

• Completed the interview successfully

• Demonstrated participation

• Attempted all questions

## Areas for Improvement

• Technical depth

• Practical implementation

• Communication clarity

## Learning Roadmap

Week 1:
Core Fundamentals

Week 2:
Problem Solving Practice

Week 3:
Project Implementation

Week 4:
Mock Interviews

## Final Summary

Candidate has completed the assessment successfully.
"""

    return report