import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    data = pd.read_csv(
        "spotify_tracks.csv"
    )
    return data
