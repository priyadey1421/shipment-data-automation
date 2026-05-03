import pandas as pd

def validate_data(file_path):
    df = pd.read_excel(file_path)
    errors = []

    for index, row in df.iterrows():
        row_errors = []

        if pd.isnull(row['Sender']):
            row_errors.append("Missing Sender")

        if pd.isnull(row['Receiver']):
            row_errors.append("Missing Receiver")

        try:
            pd.to_datetime(row['Invoice_Date'])
        except:
            row_errors.append("Invalid Date")

        if row['Quantity'] <= 0:
            row_errors.append("Invalid Quantity")

        if row['Value'] <= 0:
            row_errors.append("Invalid Value")

        if row_errors:
            errors.append({
                "Row": index + 1,
                "Errors": ", ".join(row_errors)
            })

    pd.DataFrame(errors).to_excel("../output/validation_errors.xlsx", index=False)

validate_data("../data/sample_shipments.xlsx")
