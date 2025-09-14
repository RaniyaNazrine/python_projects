# simple_chatbot.py

def simple_chatbot():
    """
    A simple command-line chatbot that responds to basic greetings and questions.
    The bot will keep running until the user types 'exit' or 'quit'.
    """
    print("Hello! I am a simple chatbot. You can talk to me. Type 'exit' to end our chat.")
    print("-" * 50)  # Print a decorative line

    # Start the main conversation loop
    while True:
        # Get user input and convert it to lowercase for easier matching
        user_input = input("You: ").lower()

        # Check for exit commands
        if user_input == "exit" or user_input == "quit":
            print("Chatbot: Goodbye! It was nice chatting with you.")
            break  # Exit the loop to end the program

        # Simple responses based on keywords in the user's input
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif "your name" in user_input:
            print("Chatbot: You can call me SimpleBot.")
        elif "help" in user_input:
            print("Chatbot: I can answer basic questions. Try asking about my name or how I'm doing.")
        elif "what is python" in user_input:
            print("Chatbot: Python is a high-level, interpreted programming language.")
        else:
            # Default response for unrecognized input
            print("Chatbot: I'm sorry, I don't understand. Could you rephrase that?")

# Run the chatbot function
if __name__ == "__main__":
    simple_chatbot()