# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'C++ Standard Library'
copyright = '2022, M Zaki'
author = 'M Zaki'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'breathe',
    'myst_parser',
    'sphinx_design',
    'sphinxcontrib.plantuml',
    'sphinx.ext.graphviz'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

root_doc = "cxx_pro_std_articles/index"

show_authors = True

# -- Breathe configuration --------------------------------------------------


breathe_default_project = 'cxx_std_articles'

breathe_projects = {
    breathe_default_project : os.path.abspath("doxygen/xml"),
    }

print(os.path.abspath(""))
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'pydata_sphinx_theme'

# The title in the home page
html_title = 'C++ Standard Library'

html_short_title = "std::"

html_baseurl = "/cxx_pro_std_articles/"

# html_logo = None

# html_favicon = None

html_last_updated_fmt = '%b %d, %Y'

# pydata theme options. See pydata theme website for options
html_theme_options = {
    # Add external links
    "external_links" : [
        {
            "url" : "https://en.cppreference.com/w/cpp", 
            "name" : "C++ Reference"
        },
        {
            "url" : "",
            "name" : "" 
        }
    ],
    
    # Add GitHub URL
    "github_url": "https://github.com/zaki-x86",
    
    # Add icons:
    "icon_links" : [
        
    ],
    
    # Add logo 
    "logo" : {
        
    },
    
    "show_toc_level" : 1,
    
    "footer_items": ["copyright", "last-updated"],
    
    # todo! figure out how to add last updated template
    
    # todo! configure google analytics -- when this thing goes live
    # "google_analytics_id": "UA-XXXXXXX",
}

html_sidebars = {
    # todo!
}

html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise interprise
    "github_user": "<zaki-x86>",
    "github_repo": "<https://github.com/zaki-x86/cxx_pro_std_articles>",
    "github_version": "<main>",
    #"doc_path": "<path-from-root-to-your-docs>",
}