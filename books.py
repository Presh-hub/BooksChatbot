import pandas as pd

def load_books():
    df = pd.read_csv(
        "data/books.csv",
        encoding="latin-1",
        on_bad_lines='skip'   # 🔥 THIS FIXES YOUR ERROR
    )
    return df.head(10)

def list_books():
    df = load_books()

    print(df.columns)  # 🔥 TEMPORARY (to debug)

    result = []

    # Try multiple possible column names
    if "Book-Title" in df.columns:
        titles = df["Book-Title"]
        authors = df["Book-Author"]

    elif "title" in df.columns:
        titles = df["title"]
        authors = df["authors"]

    else:
        return ["Column names not recognized. Check dataset."]

    for i in range(len(titles)):
        result.append(f"{i+1}. {titles.iloc[i]} by {authors.iloc[i]}")

    return result