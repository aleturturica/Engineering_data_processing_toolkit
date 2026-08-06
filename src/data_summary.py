def summarize_data(data):

    print("\n----- Data Summary -----")

    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")

    print("\nColumn names:")

    for column in data.columns:
        print(f"- {column}")

    print("\nMissing values:")

    print(data.isnull().sum())