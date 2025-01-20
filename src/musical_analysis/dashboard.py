import streamlit as st
import plotly.express as px
from data_loading import load_data
from claude_llm import call_claude_llm

# Spotify Theme Colors
SPOTIFY_GREEN = "#1DB954"
SPOTIFY_BLACK = "#191414"
SPOTIFY_WHITE = "#FFFFFF"


# Apply custom CSS for Spotify theme
def apply_spotify_theme():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {SPOTIFY_BLACK};
            color: {SPOTIFY_WHITE};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {SPOTIFY_GREEN};
        }}
        .stButton>button {{
            background-color: {SPOTIFY_GREEN};
            color: {SPOTIFY_WHITE};
            border-radius: 20px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
        }}
        .stButton>button:hover {{
            background-color: #1ED760;
            color: {SPOTIFY_WHITE};
        }}
        .stSelectbox>div>div {{
            background-color: {SPOTIFY_BLACK};
            color: {SPOTIFY_WHITE};
            border: 1px solid {SPOTIFY_GREEN};
        }}
        .stDataFrame {{
            background-color: {SPOTIFY_BLACK};
            color: {SPOTIFY_WHITE};
        }}
        .stMarkdown {{
            color: {SPOTIFY_WHITE};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def dashboard():
    apply_spotify_theme()  # Apply Spotify theme

    st.title("📊 Music Analysis Dashboard")
    st.markdown("### Which music style maximizes sales for a music production company?")

    # Load data
    data = load_data()

    # 1. Popularity by Genre
    st.header("1. Average Popularity by Genre")
    genre_popularity = data.groupby("track_genre")["popularity"].mean().reset_index()
    genre_popularity = genre_popularity.sort_values(by="popularity", ascending=False)

    # Bar chart for genre popularity
    fig1 = px.bar(
        genre_popularity,
        x="track_genre",
        y="popularity",
        title="Average Popularity by Genre",
        color_discrete_sequence=[SPOTIFY_GREEN],
    )
    st.plotly_chart(fig1)

    # Define the prompt for Claude LLM
    prompt1 = f"""
    Analyze the following data showing the average popularity of music genres:
    {genre_popularity.to_string(index=False)}

    Provide insights on which genres are the most popular and 
    why they might be strong candidates for maximizing sales. 
    Also, suggest potential strategies for music producers 
    based on this data.
    """

    if st.button("Get Insights from Claude LLM (Popularity by Genre)"):
        try:
            output1 = call_claude_llm(prompt1)
            if output1:
                st.markdown("### Insights from Claude LLM (Popularity by Genre)")
                st.write(output1)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    st.markdown("""
    **Insight:**  
    This chart shows the average popularity of music genres. Genres with high popularity (like pop or electronic) are strong candidates for maximizing sales.
    """)

    # 2. Audio Features by Genre
    st.header("2. Audio Features by Genre")
    selected_genre = st.selectbox("Choose a genre", data["track_genre"].unique())
    filtered_data = data[data["track_genre"] == selected_genre]

    st.subheader(f"Audio Features for Genre: {selected_genre}")
    features = ["danceability", "energy", "acousticness", "valence"]
    for feature in features:
        st.write(f"**{feature.capitalize()}**")
        fig2 = px.histogram(
            filtered_data,
            x=feature,
            nbins=20,
            title=f"Distribution of {feature}",
            color_discrete_sequence=[SPOTIFY_GREEN],
        )
        st.plotly_chart(fig2)

        # Define the prompt for Claude LLM
        prompt2 = f"""
        Analyze the following data showing the distribution of {feature} for the genre {selected_genre}:
        {filtered_data[feature].describe().to_string()}

        Provide insights on how this feature influences the genre's popularity and suggest strategies for music producers to leverage this feature.
        """

        # Call Claude LLM and get the response
        if st.button(
            f"Get Insights from Claude LLM ({feature.capitalize()} Distribution)"
        ):
            try:
                output2 = call_claude_llm(prompt2)
                if output2:
                    st.markdown(
                        f"### Insights from Claude LLM ({feature.capitalize()} Distribution)"
                    )
                    st.write(output2)
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # 3. Correlation Between Popularity and Audio Features
    st.header("3. Correlation Between Popularity and Audio Features")
    corr_data = data[
        ["popularity", "danceability", "energy", "acousticness", "valence"]
    ]
    corr_matrix = corr_data.corr()

    # Heatmap for correlation matrix
    fig3 = px.imshow(
        corr_matrix,
        text_auto=True,
        title="Correlation Matrix",
        color_continuous_scale=[SPOTIFY_BLACK, SPOTIFY_GREEN],
    )
    st.plotly_chart(fig3)

    # Define the prompt for Claude LLM
    prompt3 = f"""
    Analyze the following correlation matrix showing the relationships between popularity and audio features (danceability, energy, acousticness, valence):
    {corr_matrix.to_string()}

    Provide insights on which features have the strongest influence on popularity and suggest strategies for music producers to optimize these features.
    """

    # Call Claude LLM and get the response
    if st.button("Get Insights from Claude LLM (Correlation Matrix)"):
        try:
            output3 = call_claude_llm(prompt3)
            if output3:
                st.markdown("### Insights from Claude LLM (Correlation Matrix)")
                st.write(output3)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # 4. Top 10 Most Popular Tracks
    st.header("4. Top 10 Most Popular Tracks")
    top_tracks = data.sort_values(by="popularity", ascending=False).head(10)
    st.write(
        top_tracks[["track_name", "artists", "album_name", "track_genre", "popularity"]]
    )

    st.markdown("""
    **Insight:**  
    This table lists the most popular tracks. By analyzing their features, you can identify recurring trends to guide future productions.
    """)
