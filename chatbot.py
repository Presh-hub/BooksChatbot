from books import list_books, list_books_by_level, get_book_summary, search_book

started = False
last_level = None  # 🔥 memory

def chatbot_response(user_input):
    global last_level, started

    user_input = user_input.lower()
    #start screen
    if not started:
        if user_input == "continue":
            started = True
            return "Great! you can now:\n- Type beginner, intermediate, advanced\n- search <book>\n- summary <book>"
        else:
            return "📚 Welcome to Books ChatBot!\nI can help you find books and summaries.\n\nType 'continue' to start"

    if "hello" in user_input:
        return "Hi 👋 I can recommend books, search, and give summaries!"

    elif "beginner" in user_input:
        last_level = "Beginner"
        return "📘 Beginner Books:\n" + "\n".join(list_books_by_level("Beginner"))

    elif "intermediate" in user_input:
        last_level = "Intermediate"
        return "📗 Intermediate Books:\n" + "\n".join(list_books_by_level("Intermediate"))

    elif "advanced" in user_input:
        last_level = "Advanced"
        return "📕 Advanced Books:\n" + "\n".join(list_books_by_level("Advanced"))

    elif "next" in user_input:
        if last_level == "Beginner":
            return "➡️ Move to Intermediate:\n" + "\n".join(list_books_by_level("Intermediate"))
        elif last_level == "Intermediate":
            return "➡️ Move to Advanced:\n" + "\n".join(list_books_by_level("Advanced"))
        else:
            return "Start with beginner books first 📘"

    elif user_input.startswith("summary"):
        return get_book_summary(user_input)

    elif "search" in user_input:
        keyword = user_input.replace("search", "").strip()
        results = search_book(keyword)

        if results:
            return "🔍 Found:\n" + results
        else:
            return "❌ No matching books found."
            
    elif "recommend" in user_input:
        return "🔥 Recommended:\n" + "\n".join(list_books_by_level("Beginner"))

    elif "bye" in user_input:
        return "Goodbye and hope to see you next time👋"

    else:
        return "Try: beginner books, search <name>, next, or summary "
    