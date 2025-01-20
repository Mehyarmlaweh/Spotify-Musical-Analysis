Getting Started
===============

Installation
------------

To install the Spotify Musical Analysis project, follow these steps:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/your-username/spotify-musical-analysis.git
      cd spotify-musical-analysis

2. Install dependencies using Poetry:

   .. code-block:: bash

      poetry install

3. Run the application:

   .. code-block:: bash

      poetry run streamlit run src/musical_analysis/main.py

Requirements
------------

- Python 3.8+
- Poetry (for dependency management)
- Streamlit (for the web interface)
- Pandas, Plotly, and Boto3 (for data analysis and visualization)