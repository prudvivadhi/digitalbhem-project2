# Import necessary libraries
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# FAQ database
faq = {
    "What is your name?": "I am a chatbot created to assist you.",
    "How can I help you?": "You can ask me questions about our services.",
    "What is your purpose?": "My purpose is to provide information and answer your queries.",
}

def get_answer(query):
    # Process the user query
    doc = nlp(query.lower())
    
    # Check for a match in the FAQ
    for question in faq.keys():
        if doc.similarity(nlp(question.lower())) > 0.7:
            return faq[question]
    
    return "I'm sorry, I don't understand your question."

def main():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_answer(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()