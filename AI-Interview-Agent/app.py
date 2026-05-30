from agents import AIInterviewAgent
from questions import QuestionManager

def main():
    # Initialize the AI interview agent
    agent = AIInterviewAgent()
    
    # Initialize the question manager
    question_manager = QuestionManager()
    
    # Start the interview process
    print("Welcome to the AI Interview Agent!")
    questions = question_manager.get_questions()
    
    for question in questions:
        response = agent.ask_question(question)
        agent.process_response(response)
    
    print("Thank you for participating in the interview!")

if __name__ == "__main__":
    main()