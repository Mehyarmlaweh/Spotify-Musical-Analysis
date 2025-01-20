from src.musical_analysis.data_loading import load_data
import pandas as pd

def test_load_data():
    # Test if the data is loaded correctly
    data = load_data()
    
    # Check if the data is not empty
    assert not data.empty, "Data should not be empty"
    
    # Check if specific columns exist
    expected_columns = ["track_name", "artists", "album_name", "track_genre", "popularity"]
    for column in expected_columns:
        assert column in data.columns, f"Column '{column}' is missing in the dataset"


def test_average_popularity_by_genre():
    # Test calculating average popularity by genre
    data = load_data()
    genre_popularity = data.groupby("track_genre")["popularity"].mean().reset_index()
    
    # Check if the result is a DataFrame
    assert isinstance(genre_popularity, pd.DataFrame), "Result should be a DataFrame"
    
    # Check if the DataFrame has the correct columns
    assert list(genre_popularity.columns) == ["track_genre", "popularity"], "Columns should be 'track_genre' and 'popularity'"
    
    # Check if the average popularity values are within the expected range
    assert all(genre_popularity["popularity"].between(0, 100)), "Popularity values should be between 0 and 100"