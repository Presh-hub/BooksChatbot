from chatbot import chatbot_response

print("Book Sequence ChatBot")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() == "bye":
        break