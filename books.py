import pandas as pd

def load_books():
    df = pd.read_csv(
        "data/books.csv",
        encoding="latin-1",
        sep=";",
        quotechar='"',
        on_bad_lines='skip'
    )

    
    df = df[["Book-Title", "Book-Author"]]

    
    df = df.dropna()


    df = df.drop_duplicates()


    df["Book-Title"] = df["Book-Title"].str.strip()
    df["Book-Author"] = df["Book-Author"].str.strip()


    df = df.reset_index(drop=True)

    return df.head(10)

def list_books():
    df = load_books()

    result = []
    for i in range(len(df)):
        result.append(f"{i+1}. {df.iloc[i]['Book-Title']} by {df.iloc[i]['Book-Author']}")

    return result

    
    