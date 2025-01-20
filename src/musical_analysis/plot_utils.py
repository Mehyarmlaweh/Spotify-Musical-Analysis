import base64
import tempfile
import os
import plotly.express as px
import streamlit as st

def save_plot_to_base64(fig):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
            fig.write_image(tmpfile.name, format="png")  
            with open(tmpfile.name, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
            os.unlink(tmpfile.name)  
        return encoded_image
    except Exception as e:
        st.error(f"Error saving plot to Base64: {e}")
        return None