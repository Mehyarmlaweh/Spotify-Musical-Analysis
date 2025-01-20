import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    data = pd.read_csv(
        r"C:\Users\14384\Desktop\M2 BDIA\Data Viz\TPS\TP2\Spotify-Musical-Analysis\data\spotify_tracks.csv"
    )
    return data
