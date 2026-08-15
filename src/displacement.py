import pandas as pd


def calculate_displacement(initial_data, final_data):

    initial_data = initial_data.set_index("Node")
    final_data = final_data.set_index("Node")

    displacement = pd.DataFrame()

    displacement["X-disp"] = final_data["X"] - initial_data["X"]
    displacement["Y-disp"] = final_data["Y"] - initial_data["Y"]
    displacement["Z-disp"] = final_data["Z"] - initial_data["Z"]

    displacement = displacement.reset_index()

    return displacement