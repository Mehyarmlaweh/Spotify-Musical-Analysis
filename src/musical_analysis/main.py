import streamlit as st
from src.musical_analysis.dashboard import dashboard
from src.musical_analysis.home import home


def main():
    # Initialize session state for page navigation
    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Display the appropriate page based on session state
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "dashboard":
        dashboard()


# Run the app
if __name__ == "__main__":
    main()
