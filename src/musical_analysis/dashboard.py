import streamlit as st
import pandas as pd
import plotly.express as px
from data_loading import load_data
from plot_utils import save_plot_to_base64
from claude_llm import call_claude_llm

def dashboard():
    st.title("📊 Music Analysis Dashboard")
    st.markdown("### Which music style maximizes sales for a music production company?")
    
    # Load data
    data = load_data()
    
    # 1. Popularity by Genre
    st.header("1. Average Popularity by Genre")
    genre_popularity = data.groupby("track_genre")["popularity"].mean().reset_index()
    genre_popularity = genre_popularity.sort_values(by="popularity", ascending=False)
    
    # Bar chart for genre popularity
    fig1 = px.bar(genre_popularity, x="track_genre", y="popularity", title="Average Popularity by Genre")
    st.plotly_chart(fig1)
    
    # Define the prompt for Claude LLM
    prompt1 = """
    Analyze the bar chart showing the average popularity of music genres. Provide insights on which genres are the most popular and why they might be strong candidates for maximizing sales. Also, suggest potential strategies for music producers based on this data.
    """
    
    if st.button("Get Insights from Claude LLM (Popularity by Genre)"):
        try:
            image_base64_1 = save_plot_to_base64(fig1)
            if image_base64_1:
                output1 = call_claude_llm(image_base64_1, prompt1)
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
        fig2 = px.histogram(filtered_data, x=feature, nbins=20, title=f"Distribution of {feature}")
        st.plotly_chart(fig2)
        
        # Define the prompt for Claude LLM
        prompt2 = f"""
        Analyze the histogram showing the distribution of {feature} for the genre {selected_genre}. Provide insights on how this feature influences the genre's popularity and suggest strategies for music producers to leverage this feature.
        """
        
        # Call Claude LLM and get the response
        if st.button(f"Get Insights from Claude LLM ({feature.capitalize()} Distribution)"):
            try:
                image_base64_2 = save_plot_to_base64(fig2)
                if image_base64_2:
                    output2 = call_claude_llm(image_base64_2, prompt2)
                    if output2:
                        st.markdown(f"### Insights from Claude LLM ({feature.capitalize()} Distribution)")
                        st.write(output2)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
    # 3. Correlation Between Popularity and Audio Features
    st.header("3. Correlation Between Popularity and Audio Features")
    corr_data = data[["popularity", "danceability", "energy", "acousticness", "valence"]]
    corr_matrix = corr_data.corr()
    
    # Heatmap for correlation matrix
    fig3 = px.imshow(corr_matrix, text_auto=True, title="Correlation Matrix")
    st.plotly_chart(fig3)
    
    # Define the prompt for Claude LLM
    prompt3 = """
    Analyze the correlation matrix showing the relationships between popularity and audio features (danceability, energy, acousticness, valence). Provide insights on which features have the strongest influence on popularity and suggest strategies for music producers to optimize these features.
    """
    
    # Call Claude LLM and get the response
    if st.button("Get Insights from Claude LLM (Correlation Matrix)"):
        try:
            image_base64_3 = save_plot_to_base64(fig3)
            if image_base64_3:
                output3 = call_claude_llm(image_base64_3, prompt3)
                if output3:
                    st.markdown("### Insights from Claude LLM (Correlation Matrix)")
                    st.write(output3)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    # 4. Top 10 Most Popular Tracks
    st.header("4. Top 10 Most Popular Tracks")
    top_tracks = data.sort_values(by="popularity", ascending=False).head(10)
    st.write(top_tracks[["track_name", "artists", "album_name", "track_genre", "popularity"]])
    
    st.markdown("""
    **Insight:**  
    This table lists the most popular tracks. By analyzing their features, you can identify recurring trends to guide future productions.
    """)