import pandas as pd

def clean_data(file_path):
    df = pd.read_excel(file_path)

    df = df.drop_duplicates()
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    df['Sender'] = df['Sender'].fillna("Unknown")
    df['Receiver'] = df['Receiver'].fillna("Unknown")

    df['Invoice_Date'] = pd.to_datetime(df['Invoice_Date'], errors='coerce')

    df = df[df['Quantity'] > 0]
    df = df[df['Value'] > 0]

    df.to_excel("../output/cleaned_data.xlsx", index=False)

clean_data("../data/sample_shipments.xlsx")
