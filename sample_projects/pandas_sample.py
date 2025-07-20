
import pandas as pd

def load_data():
    df = pd.read_csv('data.csv')
    return df

def summarize(df):
    return df.describe()

def main():
    df = load_data()
    summary = summarize(df)
    print(summary)

if __name__ == "__main__":
    main()
