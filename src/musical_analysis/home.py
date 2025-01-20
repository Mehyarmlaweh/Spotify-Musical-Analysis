import streamlit as st

def home():
    st.title("🎵 Welcome to the Music Analysis App")
    # CSS for improved display
    st.markdown("""
        <style>
        .big-font {
            font-size: 30px !important;
            font-weight: bold;
        }
        .intro-text {
            font-size: 18px;
            color: #4A4A4A;
        }
        .button-style {
            background-color: #FF4B4B;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-align: center;
            font-size: 16px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">🎵 Discover Musical Trends That Maximize Sales 🎵</p>', unsafe_allow_html=True)

    # Introduction
    st.markdown("""
        <div class="intro-text">
        Welcome to our music analysis application, designed to help producers and professionals in the music industry make informed decisions. With precise data and interactive visualizations, you can identify the most popular and profitable music styles tailored to your target audience.
        </div>
        """, unsafe_allow_html=True)

    if st.button("👉 Access the Analysis Dashboard", key="dashboard_button", help="Click to explore the data"):
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
    st.markdown("""
        *"This application has revolutionized how we make decisions. In just a few clicks, we identified the music style that generated the most sales this year!"*  
        – **Alex, Music Producer**
        """)

    # Engaging visual (example: image or icon)
    st.image(r"C:\Users\14384\Desktop\M2 BDIA\Data Viz\TPS\TP2\Spotify-Musical-Analysis\assets\Spotify_icon.png", width=40)