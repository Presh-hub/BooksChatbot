import pandas as pd
import json

# SWITCH DATASET 
MODE = "manual"   # change to "kaggle" if needed



# LOAD DATA


def load_books():
    if MODE == "kaggle":
        df = pd.read_csv(
            "data/books.csv",
            encoding="latin-1",
            sep=";",
            quotechar='"',
            on_bad_lines='skip',
            low_memory=False
        )

        df = df[["Book-Title", "Book-Author"]].dropna().drop_duplicates()

        levels = ["Beginner", "Intermediate", "Advanced"]
        df["Level"] = [levels[i % 3] for i in range(len(df))]

        return df.head(20)

    else:
        with open("data/books.json", "r") as file:
            return json.load(file)



# LIST BOOKS


def list_books():
    data = load_books()

    result = []

    if MODE == "kaggle":
        for i in range(len(data)):
            result.append(f"{i+1}. {data.iloc[i]['Book-Title']} by {data.iloc[i]['Book-Author']}")

    else:
        for b in data:
            result.append(f"{b['id']}. {b['title']} by {b['author']}")

    return result



# GET SUMMARY (ONLY JSON)

def get_book_summary(user_input):
    if MODE == "kaggle":
        return "❌ sorry no available summaries."

    books = load_books()

    for b in books:
        if b["title"].lower() in user_input.lower():
            return f"{b['title']}:\n{b['summary']}"

    return "Book not found."