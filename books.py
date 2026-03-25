import pandas as pd

def load_books():
    df = pd.read_csv(
        "data/books.csv",
        encoding="latin-1",
        sep=";",
        quotechar='"',
        on_bad_lines='skip',
        low_memory=False
    )

    df = df[["Book-Title", "Book-Author"]].dropna().drop_duplicates()

    # 🔥 Add sequence levels manually
    df["Level"] = ["Beginner", "Intermediate", "Advanced"] * (len(df)//3 + 1)

    return df.head(20)

def list_books():
    df = load_books()

    result = []
    for i in range(len(df)):
        result.append(f"{i+1}. {df.iloc[i]['Book-Title']} by {df.iloc[i]['Book-Author']}")

    return result

    
    