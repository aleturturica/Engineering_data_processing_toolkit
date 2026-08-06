from src.csv_reader import load_csv
from src.data_validation import check_columns
from src.data_summary import summarize_data
from src.config import REQUIRED_COLUMNS


def main():

    data = load_csv("data/input/example.csv")

    missing_columns = check_columns(data, REQUIRED_COLUMNS)

    if len(missing_columns) == 0:
        print("Required columns found.")
    else:
        print("Missing columns:")

        for column in missing_columns:
            print(f"  - {column}")

    summarize_data(data)

if __name__ == "__main__":
    main()