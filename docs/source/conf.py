# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CapLib'
copyright = '2025, www.caprisktech.com'
author = 'www.caprisktech.com'

version = '0.1'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
extensions.append('sphinx.ext.autodoc')
extensions.append('sphinx.ext.napoleon')

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 2,
    'collapse_navigation': True,
    'titles_only': True
}
html_static_path = ['_static']
html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False

# Disable automatic API documentation generation
autodoc_default_options = {
    'no-auto-toc': True
}

# Add module path
import os
import sys
sys.path.insert(0, os.path.abspath('../../..'))
