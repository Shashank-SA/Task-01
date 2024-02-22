import re


responses = {
    r'hello|hi|hey': 'Hello!',
    r'how are you': 'I am fine ',
    r'what is your name': 'I am a botty.',
    r'bye|goodbye': 'bye.',
    r'help': 'How acan i help you friend. Please ask .',
    r'\b(?:what|who)\s+is\s+your\s+(?:creator|developer)\b': 'I was developed by a team.',
    r'\b(?:what|who)\s+created\s+you\b': 'I am developed by you.',
    r'\b(?:how\s+do\s+you\s+work|how\s+does\s+it\s+work)\b': 'I work by processing natural language text and generating responses based on patterns and knowledge.',
    r'\b(?:what\s+can\s+you\s+do|capabilities)\b': 'I can answer questions, provide information, and engage in conversations on various topics.',
    r'\b(?:tell\s+me\s+a\s+joke)\b': 'Sure, heres a joke for you: Why was the math book sad? Because it had too many problems!',
    r'\b(?:what\s+is\s+the\s+meaning\s+of\s+life)\b': 'The meaning of life is a deep philosophical question that has been debated for centuries. It varies from person to person.',
    r'\b(?:thank\s+you|thanks)\b': 'Youre welcome! .',
}

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I don't understand that. Please try asking a different question."

# Main loop for the chatbot
print("Chatbot: Hello! I'm a simple chatbot. You can ask me questions or say hello.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
