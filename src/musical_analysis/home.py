import streamlit as st

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
        .stMarkdown {{
            color: {SPOTIFY_WHITE};
        }}
        .big-font {{
            font-size: 30px !important;
            font-weight: bold;
            color: {SPOTIFY_GREEN};
        }}
        .intro-text {{
            font-size: 18px;
            color: {SPOTIFY_WHITE};
        }}
        .testimonial {{
            font-style: italic;
            color: {SPOTIFY_WHITE};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def home():
    apply_spotify_theme()  # Apply Spotify theme

    st.title("🎵 Welcome to the Music Analysis App")
    st.markdown(
        '<p class="big-font">🎵 Discover Musical Trends That Maximize Sales 🎵</p>',
        unsafe_allow_html=True,
    )

    # Introduction
    st.markdown(
        """
        <div class="intro-text">
        Welcome to our music analysis application, designed to help producers and professionals in the music industry make informed decisions. With precise data and interactive visualizations, you can identify the most popular and profitable music styles tailored to your target audience.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "👉 Access the Analysis Dashboard",
        key="dashboard_button",
        help="Click to explore the data",
    ):
        st.session_state.page = "dashboard"
        st.rerun()

    # Section "Why use this application?"
    st.markdown("### Why use this application?")
    st.markdown("""
        - **📊 Real-time data:** Access analyses based on the latest trends in the music market.  
        - **🎨 Interactive visualizations:** Explore clear and customizable charts to better understand the data.  
        - **💡 Smart recommendations:** Get suggestions for music styles based on past performances.  
        - **🚀 Easy to use:** An intuitive interface designed for busy professionals.  
        """)

    # Testimonial
    st.markdown("### Testimonial")
    st.markdown(
        """
        <div class="testimonial">
        *"This application has revolutionized how we make decisions. In just a few clicks, we identified the music style that generated the most sales this year!"*  
        – **Alex, Music Producer**
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Engaging visual (example: image or icon)
    st.image(
        r"C:\Users\14384\Desktop\M2 BDIA\Data Viz\TPS\TP2\Spotify-Musical-Analysis\assets\Spotify_icon.png",
        width=100,
    )
