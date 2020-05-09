import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input_file_name = "movies.csv"
input_csv_file_path = os.path.join(dir_path, input_file_name)
output_file_name = "film_ratings.csv"
output_csv_file_path = os.path.join(dir_path, output_file_name)

data_frame = pd.read_csv(input_csv_file_path, header=0)

final_data = []

if __name__ == "__main__":
    print("Reading csv file")
    for index, row in data_frame.iterrows():
        final_data.append({"title": row["Title"], "ratings": row["Ratings"]})

    output_data_frame = pd.DataFrame(final_data, columns=["title", "ratings"])
    output_data_frame.to_csv(output_csv_file_path)
