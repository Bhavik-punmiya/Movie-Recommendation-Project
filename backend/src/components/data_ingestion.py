import os
import pandas as pd
import re

class DataCleaning:
    def __init__(self, data_path):
        self.data_path = data_path
        self.cleaned_data_path = os.path.join('../../artifacts', "cleaned_movies.csv")

    def clean_title(self, title):
        title = re.sub("[^a-zA-Z0-9 ]", "", title)
        return title

    def clean_data(self):
        # Reading the dataset
        movies = pd.read_csv(self.data_path)

        # Cleaning the movie titles
        movies["clean_title"] = movies["title"].apply(self.clean_title)

        # Saving the cleaned data to a new CSV file
        movies.to_csv(self.cleaned_data_path, index=False)

        print("Data cleaning and transformation completed.")

if __name__ == "__main__":
    data_cleaning = DataCleaning("../../dataset/movies.csv")
    data_cleaning.clean_data()
