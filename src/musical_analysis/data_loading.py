import pandas as pd
import streamlit as st
from pathlib  import Path


@st.cache_data
def load_data():
    data = pd.read_csv(
        f"""{Path(__file__).parent}/spotify_tracks.csv"""
    )
    return data
