# Configuration file for the Sphinx documentation builder.
# For a full list of options, see the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # if you need to import your package

project = 'LLM Benchmark Tool'
author = 'Trương Thị Oanh'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'classic'  # or change to 'sphinx_rtd_theme' if installed
html_static_path = ['_static']
language = 'vi'
html_css_files = ['custom.css']