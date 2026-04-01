from books import list_books, list_books_by_level, get_book_summary, search_book
import random

started = False
last_level = None  # memory

def suggestions():
    return (
        "\n\n💡 You can try:\n"
        "- 1 → See all books\n"
        "- 2 → Beginner books\n"
        "- 5 python → Search books\n"
        "- 6 think python → Get summary\n"
    )
def fun_tip():
    tips = [
        "📖 Reading daily improves your thinking!",
        "💡 Try beginner books if you're new!",
        "🚀 Consistency is key to learning!",
    ]
    return "\n\n" + random.choice(tips)

def chatbot_response(user_input):
    global last_level, started

    user_input = user_input.lower()

    #start screen
    if not started:
        if user_input == "continue":
            started = True
            return (
                "📚 MENU:\n\n"
                "1. List all books\n"
                "2. Beginner books\n"
                "3. Intermediate books\n"
                "4. Advanced books\n"
                "5. Search book (e.g. 5 python)\n"
                "6. Get summary (e.g. 6 think python)\n"
                "7. Exit\n\n"
                "👉 Type a number (1–7)"
                )
        else:
            return "📖 Welcome to Books ChatBot!\n\nType 'continue' to start"

    # MENU OPTIONS
    if user_input == "1":
        return (
    "📚 Here are all available books:\n\n"
    + "\n".join(list_books())
    + suggestions()
    + fun_tip()
)
    
    elif user_input == "2":
        last_level = "Beginner"
        return (
    "📘 Great choice! Beginner books 👇\n\n"
    + "\n".join(list_books_by_level("Beginner"))
    + suggestions()
    + fun_tip()
)
    elif user_input == "3":
        last_level = "Intermediate"
        return (
    "📗 Intermediate books for you 👇\n\n"
    + "\n".join(list_books_by_level("Intermediate"))
    + suggestions()
    + fun_tip()
)
    elif user_input == "4":
        last_level = "Advanced"
        return (
    "📕 Advanced books 💪\n\n"
    + "\n".join(list_books_by_level("Advanced"))
    + suggestions()
    + fun_tip()
)
    elif user_input.startswith("5"):
        keyword = user_input.replace("5", "").strip()

        if not keyword:
            return "🔍 Please enter a book name (e.g. 5 python)" + suggestions()

        results = search_book(keyword)

        if results:
            return (
                f"🔍 Nice! I found these books for '{keyword}':\n\n"
                + results
                + suggestions()
                + fun_tip()
            )
        else:
            return "❌ No books found. Try another keyword!" + suggestions()
    
    elif user_input.startswith("6"):
        return (
            "📖 Here’s the summary:\n\n"
            + get_book_summary(user_input)
            + suggestions()
            + fun_tip()
        )

    elif user_input == "7":
        return "👋 Thanks for using Books ChatBot!"
        # SMART AUTO RESPONSES
    elif "thanks" in user_input or "thank you" in user_input:
        return "😊 You're welcome! I'm always here to help you find books!"

    elif "help" in user_input:
        return (
        "🤖 I can help you explore books!\n"
        + suggestions()
    )

    elif "hi" in user_input or "hello" in user_input:
        return (
        "👋 Hey there! Ready to discover some great books?\n"
        + suggestions()
    )

    else:
        return "👋 Goodbye! Hope you found a great book 📚"


    