import pandas as pd

def load_books():
    df = pd.read_csv("data/books.csv", encoding="latin-1")
    return df

def list_books():
    df = load_books()

    # Try to use common column names
    if "title" in df.columns and "authors" in df.columns:
        books = df[["title", "authors"]].head(10)
        result = []
        for i, row in books.iterrows():
            result.append(f"{i+1}. {row['title']} by {row['authors']}")
        return result

    elif "Title" in df.columns and "Author" in df.columns:
        books = df[["Title", "Author"]].head(10)
        result = []
        for i, row in books.iterrows():
            result.append(f"{i+1}. {row['Title']} by {row['Author']}")
        return result

    else:
        return ["Dataset loaded, but expected title/author columns were not found."]