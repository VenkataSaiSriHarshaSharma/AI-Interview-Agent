# AI Multi-Agent Recruitment System

## Overview

The AI Multi-Agent Recruitment System is an AI-powered hiring platform that automates candidate assessment using Google Gemini and Streamlit.

The system performs:

* Resume Screening
* Skill Evaluation
* Technical Interview Assessment
* Communication Analysis
* Hiring Recommendation
* Candidate Performance Reporting

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* Google Generative AI SDK
* Prompt Engineering
* PyMuPDF
* Python-Docx
* Git
* GitHub

## Features

### Resume Screening Agent

* Resume parsing
* Skill extraction
* Resume match analysis

### Interview Agent

* Dynamic technical questions
* Multiple job roles supported
* Randomized question generation

### Evaluation Agent

* Technical score generation
* Communication assessment
* Problem-solving evaluation

### Hiring Recommendation Agent

* SELECT / CONSIDER / REJECT decision
* Candidate strengths and weaknesses
* Learning roadmap generation

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

## Project Structure

```text
AI-Interview-Agent
│
├── app.py
├── agents.py
├── question_bank.py
├── requirements.txt
├── README.md
└── .env
```

## Future Enhancements

* Resume Upload Support
* Skill Gap Analysis
* PDF Report Generation
* Recruiter Dashboard
* Cloud Deployment

## Author

Venkata Sai Sri Harsha Sharma
