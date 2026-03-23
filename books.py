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

    # Use correct column names for your dataset
    if "Book-Title" in df.columns and "Book-Author" in df.columns:
        titles = df["Book-Title"]
        authors = df["Book-Author"]

        result = []
        for i in range(len(titles)):
            result.append(f"{i+1}. {titles.iloc[i]} by {authors.iloc[i]}")

        return result

    else:
        return ["Dataset loaded, but expected columns not found."]