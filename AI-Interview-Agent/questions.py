class QuestionManager:
    def __init__(self):
        self.questions = [
            "What is your greatest strength?",
            "What is your greatest weakness?",
            "Why do you want to work here?",
            "Where do you see yourself in five years?",
            "Describe a challenging situation you faced and how you dealt with it.",
            "Why should we hire you?",
            "What are your salary expectations?",
            "Do you have any questions for us?"
        ]

    def get_random_question(self):
        import random
        return random.choice(self.questions)

    def get_all_questions(self):
        return self.questions

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, question):
        if question in self.questions:
            self.questions.remove(question)