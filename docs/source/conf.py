# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Spotify Musical Analysis'
copyright = '2025, Mehyar'
author = 'Mehyar'

# The short X.Y version
version = '1.0'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',  # Automatically generate documentation from docstrings
    'sphinx.ext.viewcode',  # Add links to source code
    'sphinx.ext.napoleon',  # Support for Google-style and NumPy-style docstrings
    'sphinx.ext.githubpages',  # Publish docs to GitHub Pages
    'sphinx.ext.autosummary',  # Generate autosummary files
]

# Add paths to templates
templates_path = ['_templates']

# List of patterns to exclude from documentation
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Use the 'furo' theme for modern and clean documentation
html_theme = 'furo'

# Add paths to static files (e.g., custom CSS or JavaScript)
html_static_path = ['_static']

# Customize the theme
html_theme_options = {
    'navigation_depth': 4,  # Depth of the table of contents in the sidebar
    'collapse_navigation': False,  # Do not collapse the sidebar navigation
    'titles_only': False,  # Show all headings in the sidebar, not just the top-level ones
}

# Add a custom logo
html_logo = '_static/logo.png'  # Replace with the path to your logo file


# -- Options for autodoc -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

# Automatically generate summaries for autodoc
autosummary_generate = True

# Include both class and __init__ docstrings
autoclass_content = 'both'

# -- Options for Napoleon ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html

# Use Google-style docstrings
napoleon_google_docstring = True

# Include private methods in the documentation
napoleon_include_private_with_doc = True

# -- Options for intersphinx -------------------------------------------------
# Link to external documentation (e.g., Python standard library)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}