def check_columns(data, required_columns):

    missing_columns = []

    for column in required_columns:
        if column not in data.columns:
            missing_columns.append(column)

    return missing_columns