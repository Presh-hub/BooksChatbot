from books import list_books, get_book_summary

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi 👋 I can show books or summaries."

    elif "books" in user_input:
        return "\n".join(list_books())

    elif "summary" in user_input:
        return get_book_summary(user_input)

    elif "bye" in user_input:
        return "Goodbye 👋"

    else:
        return "Try: show books or summary <book name>"