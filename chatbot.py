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

    user_input = user_input.lower().strip()

    # START SCREEN
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
                "👉 Type a number OR text"
            )
        else:
            return "📖 Welcome to Books ChatBot!\n\nType 'continue' to start"

    # OPTION 1 — ALL BOOKS
    elif user_input.startswith("1") or "all books" in user_input:
        return (
            "📚 Here are all available books:\n\n"
            + "\n".join(list_books())
            + suggestions()
            + fun_tip()
        )

    # OPTION 2 — BEGINNER
    elif user_input.startswith("2") or "beginner" in user_input:
        last_level = "Beginner"
        return (
            "📘 Beginner books 👇\n\n"
            + "\n".join(list_books_by_level("Beginner"))
            + suggestions()
            + fun_tip()
        )

    # OPTION 3 — INTERMEDIATE
    elif user_input.startswith("3") or "intermediate" in user_input:
        last_level = "Intermediate"
        return (
            "📗 Intermediate books 👇\n\n"
            + "\n".join(list_books_by_level("Intermediate"))
            + suggestions()
            + fun_tip()
        )

    # OPTION 4 — ADVANCED
    elif user_input.startswith("4") or "advanced" in user_input:
        last_level = "Advanced"
        return (
            "📕 Advanced books 👇\n\n"
            + "\n".join(list_books_by_level("Advanced"))
            + suggestions()
            + fun_tip()
        )

    # OPTION 5 — SEARCH (🔥 IMPROVED)
    elif user_input.startswith("5") or "search" in user_input:
        keyword = user_input.replace("5", "").replace("search", "").strip()

        if not keyword:
            return "🔍 Please enter a book name (e.g. 5 python)" + suggestions()

        results = search_book(keyword)

        if results:
            return (
                f"🔍 I found these books for '{keyword}':\n\n"
                + results
                + suggestions()
                + fun_tip()
            )
        else:
            return "❌ No books found. Try another keyword!" + suggestions()

    # OPTION 6 — SUMMARY (🔥 FIXED)
    elif user_input.startswith("6") or "summary" in user_input:
        return (
            "📖 Here’s the summary:\n\n"
            + get_book_summary(user_input)
            + suggestions()
            + fun_tip()
        )

    # OPTION 7 — EXIT
    elif user_input == "7":
        return "👋 Thanks for using Books ChatBot!"

    # SMART RESPONSES
    elif "thanks" in user_input or "thank you" in user_input:
        return "😊 You're welcome! I'm always here to help!"

    elif "help" in user_input:
        return "🤖 I can help you explore books!\n" + suggestions()

    elif "hi" in user_input or "hello" in user_input:
        return "👋 Hey there! Ready to discover some great books?\n" + suggestions()

    # DEFAULT (🔥 FIXED — NO MORE RANDOM GOODBYE)
    else:
        return "❗ I didn’t understand that. Please try again.\n" + suggestions()