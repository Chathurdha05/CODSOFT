from datetime import datetime

def chatbot():
    """
    A simple rule-based chatbot with predefined responses to user inputs.
    """
    print("Chatbot: Hello! I'm your simple chatbot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip().lower()

        #Exit condition
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        #Rule-based responses
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning perfectly!How about you?")
        elif "i am good" in user_input:
            print("Chatbot: Great! What's your name?")
        elif "my name" in user_input:
            name = user_input.split(" ")[-1] #Extract the last word as the name"
            print(f"Chatbot: Nice to meet you, {name}!")
        elif "what can you do" in user_input:
            print("Chatbot: I can answer your questions, chat with you, or help with basic queries.")
        elif "thank you" in user_input:
            print("Chatbot: You're welcome! Happy to help.")
        elif "time" in user_input:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "what is the weather like" in user_input:
            print("Chatbot: I can't access real-time weather information yet, but I can suggest some weather websites.")
        elif "bored" in user_input:
            print("Chatbot: I can tell you a joke, play a game, or recommend some interesting websites to explore.")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")
            user_input = input("You: ").strip().lower()

#Entry point for the chatbot
if __name__ == "__main__":
    chatbot()

    
    
