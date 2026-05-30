class InterviewAgent:
    def __init__(self, name):
        self.name = name

    def greet_candidate(self):
        return f"Hello, I'm {self.name}. Let's start the interview."

    def ask_question(self, question):
        return f"{self.name}: {question}"

    def process_response(self, response):
        # Logic to process the candidate's response
        return f"Processing response: {response}"


class TechnicalAgent(InterviewAgent):
    def ask_technical_question(self):
        technical_questions = [
            "What is your experience with Python?",
            "Can you explain the concept of OOP?",
            "How do you handle errors in your code?"
        ]
        return self.ask_question(technical_questions[0])  # Example of asking the first technical question


class HRAgent(InterviewAgent):
    def ask_hr_question(self):
        hr_questions = [
            "Tell me about yourself.",
            "What are your strengths and weaknesses?",
            "Where do you see yourself in five years?"
        ]
        return self.ask_question(hr_questions[0])  # Example of asking the first HR question