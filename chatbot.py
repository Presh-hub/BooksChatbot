from books import list_books

from books import list_books, load_books

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi 👋 I can recommend books by level: beginner, intermediate, advanced."

    elif "beginner" in user_input:
        df = load_books()
        beginner = df.head(5)
        return "Start with these:\n" + "\n".join(beginner["Book-Title"])

    elif "intermediate" in user_input:
        return "Next step: Data Structures and Algorithms books."

    elif "advanced" in user_input:
        return "Advanced topics: Machine Learning and AI."

    elif "book" in user_input:
        return "Here are some books:\n" + "\n".join(list_books())

    elif "bye" in user_input:
        return "Goodbye 👋"

    else:
        return "Try: beginner books, intermediate, advanced"