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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme
import time

project = 'SunFounder Pironman 5'
copyright = f'{time.localtime().tm_year}, SunFounder'
author = 'www.sunfounder.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_static_path = ['_static']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

#### RTD+

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
    './lang.js', # new
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/ext-language_tools.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/theme-chrome.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
]



# Multi-language

language = 'en' # Before running make html, set the language.
locale_dirs = ['locale/'] # .po files for other languages are placed in the locale/ folder.

gettext_compact = False # Support for generating the contents of the folders inside source/ into other languages.

# language links

rst_epilog = """

.. |link_german_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pironman5/de/latest/" target="_blank">Deutsch Online-Kurs</a>

.. |link_jp_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pironman5/ja/latest/" target="_blank">日本語オンライン教材</a>

.. |link_en_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pironman5/en/latest/" target="_blank">English Online-tutorials</a>

.. |link_fr_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pironman5/fr/latest/" target="_blank">Tutoriels en ligne en français</a>

.. |link_es_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pironman5/es/latest/" target="_blank">Tutoriales en línea en español</a>

.. |link_it_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pironman5/it/latest/" target="_blank">Corsi di italiano online</a>

"""


# open link in a new window

rst_epilog += """

.. |link_rpi_get_start| raw:: html

    <a href="https://www.raspberrypi.com/documentation/computers/getting-started.html" target="_blank">Getting Started with Raspberry Pi</a>

.. |link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.org/software/" target="_blank">Raspberry Pi Imager</a>

.. |link_batocera| raw:: html

    <a href="https://batocera.org/" target="_blank">Batocera.linux</a>


.. |link_batocera_download| raw:: html

    <a href="https://batocera.org/download" target="_blank">Batocera.linux download</a>

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit" target="_blank">here</a>

.. |link_kodi| raw:: html

    <a href="https://kodi.tv/" target="_blank">Kodi</a>
    
.. |link_osmc| raw:: html

    <a href="https://osmc.tv/" target="_blank">OSMC</a>

.. |link_libreelec| raw:: html

    <a href="https://libreelec.tv/" target="_blank">LibreELEC</a>
    
.. |link_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>


.. |link_pironman5| raw:: html

    <a href="https://www.sunfounder.com/products/pironman-5-nvme-m-2-ssd-pcie-mini-pc-case-for-raspberry-pi-5" target="_blank">Pironman 5</a>


.. |link_raspberry_pi_imager| raw:: html

    <a href="https://www.raspberrypi.org/software/" target="_blank">Raspberry Pi Imager</a>

.. |link_putty| raw:: html

    <a href="https://www.putty.org/" target="_blank">PuTTY</a>


"""
