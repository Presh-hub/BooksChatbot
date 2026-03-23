from books import list_books

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! I can list books from the dataset."

    elif "book" in user_input or "list" in user_input or "sequence" in user_input:
        return "\n".join(list_books())

    elif "bye" in user_input:
        return "Goodbye!"

    else:
        return "I do not understand. Try asking: show me books"