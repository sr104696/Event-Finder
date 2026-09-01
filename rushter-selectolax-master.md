# rushter/selectolax@master

- Files included: 55
- Files skipped: 2
- Total size: 441.7 KB
- Estimated tokens: ~113,067

## Directory Structure

```
├── .github
│   └── workflows
│       ├── make_release.yml
│       └── pythonpackage.yml
├── docs
│   ├── .gitignore
│   ├── conf.py
│   ├── examples.rst
│   ├── index.rst
│   ├── lexbor.rst
│   ├── logo.png
│   ├── logo.svg
│   ├── make.bat
│   ├── Makefile
│   ├── modules.rst
│   ├── parser.rst
│   └── selectolax.rst
├── examples
│   ├── benchmark.py
│   └── simple_example.py
├── selectolax
│   ├── lexbor
│   │   ├── attrs.pxi
│   │   ├── fragment_lookup.pxi
│   │   ├── node_remove.pxi
│   │   ├── node.pxi
│   │   ├── selection.pxi
│   │   └── util.pxi
│   ├── modest
│   │   ├── node.pxi
│   │   ├── selection.pxi
│   │   └── util.pxi
│   ├── __init__.py
│   ├── base.pxi
│   ├── lexbor.pxd
│   ├── lexbor.pyi
│   ├── lexbor.pyx
│   ├── parser.pxd
│   ├── parser.pyi
│   ├── parser.pyx
│   ├── py.typed
│   └── utils.pxi
├── tests
│   ├── __init__.py
│   ├── test_lexbor_fragment.py
│   ├── test_lexbor.py
│   ├── test_nodes.py
│   ├── test_parser.py
│   └── test_utils.py
├── typesafety
│   └── test_lexbor.yaml
├── .dockerignore
├── .gitignore
├── .gitmodules
├── .readthedocs.yaml
├── CHANGES.md
├── Dockerfile
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── requirements_dev.txt
├── ruff.toml
├── setup.cfg
└── setup.py
```

## Code Digest

### `.dockerignore`

```dockerignore
.git
.gitignore
.gitmodules
.idea
.mypy_cache
.pytest_cache
.ruff_cache
.venv
build
dist
__pycache__
*.pyc
*.pyo
*.pyd
*.so
cython_debug
docs/_build

```

### `.github/workflows/make_release.yml`

```yml
name: Build and upload to PyPI

on:
 release:
   types:
     - published


jobs:
  build_wheels:
    name: Build wheels for ${{ matrix.os }}
    runs-on: ${{ matrix.runs-on }}
    strategy:
      matrix:
        include:
          - os: linux-intel
            runs-on: ubuntu-latest
          - os: linux-arm
            runs-on: ubuntu-24.04-arm
          - os: windows-intel
            runs-on: windows-latest
          - os: windows-arm
            runs-on: windows-11-arm
          - os: macos-intel
            runs-on: macos-15-intel
          - os: macos-arm
            runs-on: macos-latest

    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true

      - name: Build wheels
        uses: pypa/cibuildwheel@v3.2.0
        env:
          CIBW_PLATFORM: ${{ matrix.platform || 'auto' }}

      - uses: actions/upload-artifact@v4
        with:
          name: cibw-wheels-${{ matrix.os }}-${{ matrix.platform}}-${{ strategy.job-index }}
          path: ./wheelhouse/*.whl


  build_sdist:
    name: Build source distribution
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true
      - name: Build sdist
        run: |
          pip install -U Cython packaging setuptools wheel
          python setup.py build_ext --inplace --cython
          python setup.py sdist

      - uses: actions/upload-artifact@v4
        with:
          path: dist/*.tar.gz
          retention-days: 1
          name: cibw-sdist

  upload_pypi:
    needs: [build_wheels, build_sdist]
    runs-on: ubuntu-latest
    environment: release
    permissions:
      id-token: write
    if: github.event_name == 'release' && github.event.action == 'published'
    steps:
      - uses: actions/download-artifact@v4
        with:
          pattern: cibw-*
          path: dist
          merge-multiple: true

      - uses: pypa/gh-action-pypi-publish@release/v1

```

### `.github/workflows/pythonpackage.yml`

```yml
name: Python package

on:
  pull_request:
    branches:
      - master
  push:
    branches:
      - master


jobs:
  test:
    strategy:
      max-parallel: 6
      matrix:
        python-version: ["3.11", "3.12", "3.13" ]
        platform: [ubuntu-24.04, macos-latest]
    runs-on: ${{ matrix.platform }}
    timeout-minutes: 6
    steps:
    - uses: actions/checkout@v4
      with:
        submodules: true
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip setuptools
        pip install -r requirements_dev.txt
        USE_LEXBOR=1 python setup.py build_ext --inplace --cython
    - name: Test with pytest
      run: |
        USE_LEXBOR=1 pytest tests
    - name: Test typesafety
      run: |
        pytest typesafety
  lint:
    strategy:
      max-parallel: 6
      matrix:
        python-version: ["3.13" ]
        platform: [ ubuntu-24.04 ]
    runs-on: ${{ matrix.platform }}
    timeout-minutes: 6
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip setuptools
          pip install -r requirements_dev.txt
          python3 -m pip install types-pyinstaller
          USE_LEXBOR=1 python setup.py build_ext --inplace --cython
      - name: Lint using Ruff
        run: ruff check selectolax tests
      - name: Lint Mypy
        run: mypy selectolax tests
      - name: Lint Cython
        run: cython-lint selectolax/

```

### `.gitignore`

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg
.idea

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# pyenv python configuration file
.python-version


selectolax/parser.c
selectolax/lexbor.c

# virtual env
.venv/
venv/

tmp/

```

### `.gitmodules`

```gitmodules
[submodule "modest"]
	path = modest
	url = https://github.com/lexborisov/modest
[submodule "lexbor"]
	path = lexbor
	url = https://github.com/lexbor/lexbor

```

### `.readthedocs.yaml`

```yaml
# Read the Docs configuration file for Sphinx projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the OS, Python version and other tools you might need
build:
  os: ubuntu-lts-latest
  tools:
    python: latest
    # You can also specify other tool versions:
    # nodejs: "20"
    # rust: "1.70"
    # golang: "1.20"
  jobs:
   pre_build:
     - git submodule sync
     - git submodule update --init --recursive
     - pip install -r requirements_dev.txt
     - python setup.py develop

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/conf.py
  # You can configure Sphinx to use a different builder, for instance use the dirhtml builder for simpler URLs
  # builder: "dirhtml"
  # Fail on all warnings to avoid broken references
  # fail_on_warning: true

# Optionally build your docs in additional formats such as PDF and ePub
# formats:
#   - pdf
#   - epub

# Optional but recommended, declare the Python requirements required
# to build your documentation
# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
python:
   install:
     - requirements: requirements_dev.txt

```

### `CHANGES.md`

```md
# selectolax Changelog

# Version 0.4.11

- Add NULL checks for CSS selectors module to prevent crashes
- Fix html5test pretty print serialization mode checks
- Update lexbor

# Version 0.4.10

- Do not destroy nodes when stripping tags
- Allow building selectolax using older lexbor versions (#218)
- Update lexbor. Fixes crashes when parsing HTML (#217).

# Version 0.4.9

- Add an ability to specify tags and namespace for fragmented parser
- Add a new serialization mode when pretty printing: `html5test`
- Allow empty HTML fragments
- Fix attrs access for non-element nodes
- Improve buffer cleanups
- Fix duplicate text when doing `text(deep=True)` on a text node
- Improve text concatenation performance
- Improve attribute handling

# Version 0.4.8

- Add Add `html_pretty`, `inner_html_pretty` methods
- Enable free-threading
- Improve `merge_text_nodes`
- Update lexbor


# Version 0.4.7

- Fix `.text()` and `iter()` for HTML fragments when there are multiple nodes at the root level. Resolves #209.
- Update lexbor. Resolves #212.
- Breaking changes: Empty tags are now serialized to `<div value="">` instead of `<div value>`
  ([Commit 4530fed](https://github.com/lexbor/lexbor/commit/4530fed3f3a2b1c3729f7742be4f56131cb8e086)).
- Improve `unwrap_tags` and `merge_text_nodes`.

# Version 0.4.6

- Fix HTML parsing in fragment parser for `LexborHTMLParser`
- Fix memory leak in fragment parser
- Improve `skip_empty` parameter for text methods
- Add `comment_content` method
- Minor performance optimizations
- Add `create_tag` method to `LexborHTMLParser`
- Fix advanced selector (`.select()`) when attributes are empty.


# Version 0.4.5

  - Broken release. Not published to PyPi.

# Version 0.4.4

- Add `is_fragment` parameter to `LexborHTMLParser` @pygarap

- Add the ability to skip empty text nodes for lexbor backend to `.text`, `.iter`, `.traverse` @pygarap

- Add new properties to lexbor backend: `is_element_node`, `is_text_node`, `is_comment_node`, `is_document_node`.  @pygarap
- Update `lexbor` library


# Version 0.4.3

- Update `lexbor` library
- Fix missing description on PyPi.


# Version 0.4.2

- Broken release. Not published to PyPi.

# Version 0.4.1

- Fix parsing of CSS selectors that contain Unicode characters.

# Version 0.4.0

- Fix incorrect default value in docstrings for strict argument
- Fix incorrect exception handling for `any_css_matches`
- Fix docstring for `css_first` method
- Fix memory leak in `merge_text_nodes` for lexbor backend
- Update lexbor backend
- Add `.inner_html` property. Allows to get and set inner HTML of a node.
- Update various docstrings.
- Optimize performance for`css_first` in lexbor backend
- Fix segfaults when accessing attributes. Resolves #135.
- Add new `.clone` method to lexbor backend. Resolve #117.
- Improve unicode handling for malformed text. Resolves #138.
- Fix segfaults when doing double `.decompose`. Resolves #179.
- Fix sefgaults when doing double `.unwrap`. Resolves #169.
- Fix typo for tag names. Clarify available tag names.

## Version 0.3.34

Released

- Lexbor backend now supports `:lexbor-contains("abc" i)` CSS pseudo-class to match text nodes.

## Version 0.3.33

Released

- Add `merge_text_nodes` to lexbor backend. Fixes #170. @amirshukayev
- Performance improvements in Cython code. @Vizonex

## Version 0.3.32

Released

- Update lexbor. New version of lexbor fixes bugs with CSS selectors.

## Version 0.3.31

Released

- Improve type hints, add docstrings to type hints
- Prevent decomposing of the root node
- Unpin Cython version and make it Optional
- Allow empty attribute values. Fixes #165.

## Version 0.3.30

Released

- Update lexbor
- Expose `SelectolaxError` exception in lexbor.pyi

## Version 0.3.29

Released

- Feat: Add unwrap empty tags functionality. Fixes #159.

## Version 0.3.28

Released

- Fix: Update lexbor and improve HTML serialization speed. Fixes #153.
- Fix: typo in type annotations. Fixes #147.
- Fix: Fix incorrect type annotations for `LexborHTMLParser.__init__`. Fixes #144.

## Version 0.3.27

Released

- Fix: Header detected as head

## Version 0.3.26

Released

- Improve type hints

## Version 0.3.25

Released

- Feat: Add `parse_fragment()` and `create_tag()`
- Add missing typing for `Node.insert_child()`
- Add `Node.parser` to access the `HTMLParser` to which the node belongs

## Version 0.3.24

Released

- Add `Node.insert_child` method to lexbor and modest backends

## Version 0.3.23

Released

- Add Python 3.13 wheels
- Update lexbor

## Version 0.3.21

Released

- ***Breaking change***: `lexbor` backend now includes the root node when querying CSS selectors. Same as `Modest` backend.
- Fix `css_matches` and `any_css_matches` methods for `Modest` backend on some compilers

## Version 0.3.20

Released

- Fixup for 0.3.19 release
- Fix tag order for `lexbor` backend

## Version 0.3.19

Released

- Increase maximum HTML size to 2.4GB

## Version 0.3.18

Released

- Fix memory leak when using CSS selectors, `lexbor` backend

## Version 0.3.17

Released

- Update lexbor
- Add Python 3.12 wheels

## Version 0.3.16

Released

- Make HTML nodes hashable
- Pin Cython version

## Version 0.3.15

Released

- Improve typing. Thanks to @nesb1

## Version 0.3.14

Released

- Fix memory leak for `lexbor` backend

## Version 0.3.13

Released

- Update `lexbor`

## Version 0.3.12

Released

- Update `lexbor`
- Add Python 3.11 wheels

## Version 0.3.11

Released

- Fix out-of-bounds bug for `merge_text_nodes` method.

## Version 0.3.10

Released

This release does not contain any changes.
Due to a typo in the version number ([#70](https://github.com/rushter/selectolax/issues/70)), we need to make a new release.

## Version 0.3.9

Released

- Remove trailing separator when using `text(deep=True, separator='x')`.
- Add a new `merge_text_nodes` method for Modest backend.

## Version 0.3.8

Released

- Fix incorrect text handling when using `text(deep=True)` on a text node.

## Version 0.3.7

Released

- Fix return type of HTMLParser.tags

## Version 0.3.6

Released

- Improve text handling
- Add binary builds for Python 3.10 and ARM on MacOS and Linux

## Version 0.3.5

Released

- Add type annotations

## Version 0.3.4

Released

- Fix `HTMLParser.html`

## Version 0.3.3

Released

- Use `document` for the `HTMLParser.html`, `LexborHTMLParser.html` root properties

## Version 0.3.2

Released

- Fix `selector` method for lexbor
- Improve text extraction for lexbor

## Version 0.3.1

Released

- Fix `setup.py` for Windows

## Version 0.3.0

Released

- Added `lexbor` backend
- Fix cloning for `Modest` backend

## Version 0.2.14

Released

- Added advanced Selector (the `select` method)
- Improved speed of `strip_tags`
- Added `clone` method for the `HtmlParser` object
- Exposed `detect_encoding`, `decode_errors`, `use_meta_tags`, `raw_html` attributes for `HtmlParser`
- Added `sget` method to the `attrs` property

## Version 0.2.13

Released

- Don't throw exception when encoding text as UTF-8 bytes fails ([#40](https://github.com/rushter/selectolax/issues/40)).
- Fix Node.attrs.items() causes ([#39](https://github.com/rushter/selectolax/issues/39)).

## Version 0.2.12

Released

- Build wheels Apple Silicon

## Version 0.2.11

Released

- Fix strip argument is ignored for the root node ([#35](https://github.com/rushter/selectolax/issues/35)).
- Fix CSS parser hangs on a bad CSS selector ([#36](https://github.com/rushter/selectolax/issues/36)).

## Version 0.2.10

Released

- Fix root node property ([#32](https://github.com/rushter/selectolax/issues/32)). The `root` property now points to the html tag.

## Version 0.2.9

Released

- Fix README for PyPI

## Version 0.2.8

Released

- Add wheels for Python 3.9

## Version 0.2.7

Released

- Add `raw_value` attribute for `Node` objects ([#22](https://github.com/rushter/selectolax/issues/22))
- Improve node modification operations

## Version 0.2.6

Released

- Fix dependency on the source `Node` when inserting to or modifying destination `Node`

## Version 0.2.5

Released

- Allow to pass Node instances to `replace_with`, `insert_before` and `insert_after` methods
- Added `insert_before` and `insert_after` methods

## Version 0.2.4

Released

- Set maximum input size to 80MB
- Update modest

## Version 0.2.3

Released

- Rebuild PyPi wheels to support Python 3.8 and manylinux2010

## Version 0.2.2

Released

- Fix node comparison

## Version 0.2.1

Released

- Add optional `include_text` parameter for the `iter` and `traverse` methods

## Version 0.2.0

Released

- Fix `iter()` does not yield text nodes
- Switch from TravisCI to Github Actions
- Build and ship wheels for Windows, MacOS and Linux using Azure Pipelines
- Add `unwrap` and `unwrap_tags` method ([#7](https://github.com/rushter/selectolax/issues/7))
- Add `replace_with` method ([#13](https://github.com/rushter/selectolax/issues/13))
- Add `attrs` property
- Add `traverse` method

```

### `Dockerfile`

```
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements_dev.txt .
RUN pip install --no-cache-dir Cython setuptools wheel && \
    pip install --no-cache-dir -r requirements_dev.txt

COPY . .

RUN python setup.py install

RUN mkdir /test_run && \
    cp test.py *.html /test_run/

WORKDIR /test_run

CMD ["python", "test.py"]

```

### `docs/.gitignore`

```gitignore
/selectolax.rst
/selectolax.*.rst
/modules.rst

```

### `docs/conf.py`

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# selectolax documentation build configuration file, created by
# sphinx-quickstart on Tue Jul  9 22:26:36 2013.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import platform
import sys

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath('../../'))


# Get the project root dir, which is the parent dir of this
cwd = os.getcwd()
project_root = os.path.dirname(cwd)

# Insert the project root dir as the first element in the PYTHONPATH.
# This lets us ensure that the source package is imported, and that its
# version is used.

if platform.system() == "Darwin":
    sys.path.insert(0, project_root)

import selectolax

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "numpydoc",
    "sphinxext.opengraph",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "selectolax"
copyright = "2018-2026, Artem Golubin"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = selectolax.__version__
# The full version, including alpha/beta/rc tags.
release = selectolax.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to
# some non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built
# documents.
# keep_warnings = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "source_repository": "https://github.com/rushter/selectolax",
    "source_branch": "master",
    "source_directory": "docs/",
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as
# html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the
# top of the sidebar.
html_logo = "logo.png"

# The name of an image file (within the static path) to use as favicon
# of the docs.  This file should be a Windows icon file (.ico) being
# 16x16 or 32x32 pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
# html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names
# to template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer.
# Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer.
# Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages
# will contain a <link> tag referring to it.  The value of this option
# must be the base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "selectolaxdoc"

# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ("index", "selectolax.tex", "selectolax Documentation", "Artem Golubin", "manual"),
]

# The name of an image file (relative to this directory) to place at
# the top of the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings
# are parts, not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "selectolax", "selectolax Documentation", ["Artem Golubin"], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "selectolax",
        "selectolax Documentation",
        "Artem Golubin",
        "selectolax",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

numpydoc_show_class_members = False

```

### `docs/examples.rst`

```rst
Examples
========

This page contains simple examples of how to use Selectolax for HTML parsing and manipulation.

.. note::
   All examples use the Lexbor backend (``from selectolax.lexbor import LexborHTMLParser``)
   which provides better performance and features compared to the older Modest backend.

Basic HTML Parsing
------------------

There are 3 ways to create or parse objects in Selectolax:

1. Parse HTML as a full document using ``LexborHTMLParser()``
2. Parse HTML as a fragment using ``LexborHTMLParser(..., is_fragment=True)``
3. Create single node using ``LexborHTMLParser(...).create_node()``

- ``LexborHTMLParser()`` - Returns the HTML tree as parsed by Lexbor, unmodified. The HTML is assumed to be a full document. ``<html>``, ``<head>``, and ``<body>`` tags are added if missing.

- ``LexborHTMLParser(..., is_fragment=True)`` - Intended for HTML fragments/partials.
    Behaves the same way as `DocumentFragment` in browsers.
    Drops ``<html>``, ``<head>``, and ``<body>`` tags if present in the input HTML.
    Use it to parse snippets of HTML that are not complete documents.


.. code-block:: python

    from selectolax.lexbor import LexborHTMLParser

    html = """
    <body>
        <span id="vspan"></span>
        <h1>Welcome to selectolax tutorial</h1>
        <div id="text">
            <p class='p3' style='display:none;'>Excepteur <i>sint</i> occaecat cupidatat non proident</p>
            <p class='p3' vid>Lorem ipsum</p>
        </div>
        <div>
            <p id='stext'>Lorem ipsum dolor sit amet, ea quo modus meliore platonem.</p>
        </div>
    </body>
    """

    fragment = """
    <div>
        <p class="p3">
            Hello there!
        </p>
    </div>
    <script>
        document.querySelector(".p3").addEventListener("click", () => { ... });
    </script>
    """

    # Parse HTML as a full document
    parser = LexborHTMLParser(html)

    # Parse HTML as a fragment
    frag_parser = LexborHTMLParser(html, is_fragment=True)

    # Create a new node for  `parser`.
    node = parser.create_node("div")

CSS Selectors
-------------

Select All Elements with CSS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find all paragraph elements with class 'p3' and examine their properties.

.. code-block:: python

    from selectolax.lexbor import LexborHTMLParser

    html = """
    <body>
        <div id="text">
            <p class='p3' style='display:none;'>Excepteur <i>sint</i> occaecat cupidatat non proident</p>
            <p class='p3' vid>Lorem ipsum</p>
        </div>
        <div>
            <p id='stext'>Lorem ipsum dolor sit amet, ea quo modus meliore platonem.</p>
        </div>
    </body>
    """

    parser = LexborHTMLParser(html)
    selector = "p.p3"

    for node in parser.css(selector):
        print('---------------------')
        print('Node: %s' % node.html)
        print('attributes: %s' % node.attributes)
        print('node text: %s' % node.text(deep=True, separator='', strip=False))
        print('tag: %s' % node.tag)
        print('parent tag: %s' % node.parent.tag)
        if node.last_child:
            print('last child inside current node: %s' % node.last_child.html)
        print('---------------------\n')

**Output:**

.. code-block:: text

    ---------------------
    Node: <p class='p3' style='display:none;'>Excepteur <i>sint</i> occaecat cupidatat non proident</p>
    attributes: {'class': 'p3', 'style': 'display:none;'}
    node text: Excepteur sint occaecat cupidatat non proident
    tag: p
    parent tag: div
    last child inside current node: Excepteur <i>sint</i> occaecat cupidatat non proident
    ---------------------

    ---------------------
    Node: <p class='p3' vid>Lorem ipsum</p>
    attributes: {'class': 'p3', 'vid': ''}
    node text: Lorem ipsum
    tag: p
    parent tag: div
    last child inside current node: Lorem ipsum
    ---------------------

Select First Match
~~~~~~~~~~~~~~~~~~

Get the first matching element using CSS selectors.

.. code-block:: python

    parser = LexborHTMLParser(html)

    # Get first h1 element
    print("H1: %s" % parser.css_first('h1').text())

**Output:**

.. code-block:: text

    H1: Welcome to selectolax tutorial

Default Return Values
~~~~~~~~~~~~~~~~~~~~~

Handle cases where no elements match your selector by providing a default value.

.. code-block:: python

    # Return default value if no matches found
    print("Title: %s" % parser.css_first('title', default='not-found'))

**Output:**

.. code-block:: text

    Title: not-found

Strict Mode
~~~~~~~~~~~

Ensure exactly one match exists, otherwise raise an error.

.. code-block:: python

    # This will raise an error if multiple matches are found
    try:
        result = parser.css_first("p.p3", default='not-found', strict=True)
    except Exception as e:
        print(f"Error: {e}")

**Output:**

.. code-block:: text

    ValueError: Expected 1 match, but found 2 matches

CSS Chaining
~~~~~~~~~~~~

Chain multiple CSS selectors to progressively filter results.

.. code-block:: python

    html = """
    <div id="container">
        <span class="red"></span>
        <span class="green"></span>
        <span class="red"></span>
        <span class="green"></span>
    </div>
    """

    parser = LexborHTMLParser(html)

    # Chain selectors: start with div, then span, then .red
    red_spans = parser.select('div').css("span").css(".red").matches
    print([node.html for node in red_spans])

**Output:**

.. code-block:: text

    ['<span class="red"></span>', '<span class="red"></span>']

HTML manipulation
-----------------

Getting HTML data back
~~~~~~~~~~~~~~~~~~~~~~

You can get HTML data back using `.html` or `.inner_html` properties.
They can be called on any node.

.. code-block:: python

    from selectolax.lexbor import LexborHTMLParser
    html = """
    <div id="main">
      <div>Hi there</div>
      <div id="updated">2021-08-15</div>
     </div>
    """
    parser = LexborHTMLParser(html)
    node = parser.css_first("#main")
    print("Inner html:\n")
    print(node.inner_html)
    print("\nOuter html:\n")
    print(node.html)

**Output:**

.. code-block:: text

    Inner html:

      <div>Hi there</div>
      <div id="updated">2021-08-15</div>

    Outer html:

    <div id="main">
      <div>Hi there</div>
      <div id="updated">2021-08-15</div>
     </div>


Changing HTML
~~~~~~~~~~~~~~

You can also change HTML by setting the `.inner_html` property.

.. code-block:: python

    from selectolax.lexbor import LexborHTMLParser
    html = """
    <div id="main">
      <div>Hi there</div>
     </div>
    """
    parser = LexborHTMLParser(html)
    node = parser.css_first("#main")
    print("Old html:\n")
    print(node.html)

    node.inner_html = "<span>Test</span>"
    print("\nNew html:\n")
    print(node.inner_html)

**Output:**

    Old html:

    <div id="main">
      <div>Hi there</div>
     </div>

    New html:

    <div id="main"><span>Test</span></div>


DOM Navigation
--------------

Parent Elements
~~~~~~~~~~~~~~~

Get parent element in the DOM tree.

.. code-block:: python

    # Print parent of p#stext
    print(parser.css_first('p#stext').parent.html)

**Output:**

.. code-block:: text

    <div>
            <p id='stext'>Lorem ipsum dolor sit amet, ea quo modus meliore platonem.</p>
        </div>

Nested Selectors
~~~~~~~~~~~~~~~~

Chain CSS selectors to find nested elements.

.. code-block:: python

    # Chain CSS selectors
    result = parser.css_first('div#text').css_first('p:nth-child(2)').html
    print(result)

**Output:**

.. code-block:: text

    <p class='p3' vid>Lorem ipsum</p>

Iterating Over Child Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Walk all child nodes of an element.

.. code-block:: python

    for node in parser.css("div#text"):
        for cnode in node.iter():
            print(cnode.tag, cnode.html)

**Output:**

.. code-block:: text

    p <p class="p3" style="display:none;">Excepteur <i>sint</i> occaecat cupidatat non proident</p>
    p <p class="p3" vid>Lorem ipsum</p>

DOM Modification
----------------

Tag Removal
~~~~~~~~~~~

Completely remove elements from the DOM tree.

.. code-block:: python

    parser = LexborHTMLParser(html)

    # Remove all p tags
    for node in parser.tags('p'):
        node.decompose()

    print(parser.body.html)

**Output:**

.. code-block:: text

    <body>
        <span id="vspan"></span>
        <h1>Welcome to selectolax tutorial</h1>
        <div id="text">


        </div>
        <div>

        </div>
    </body>

Tag Unwrapping
~~~~~~~~~~~~~~

Remove tags but preserve their content.

.. code-block:: python

    parser = LexborHTMLParser(html)

    # Remove p and i tags but keep their content
    parser.unwrap_tags(['p', 'i'])
    print(parser.body.html)

**Output:**

.. code-block:: text

    <body>
        <span id="vspan"></span>
        <h1>Welcome to selectolax tutorial</h1>
        <div id="text">
            Excepteur sint occaecat cupidatat non proident
            Lorem ipsum
        </div>
        <div>
            Lorem ipsum dolor sit amet, ea quo modus meliore platonem.
        </div>
    </body>

Attribute Manipulation
~~~~~~~~~~~~~~~~~~~~~~

Add, modify, and remove element attributes.

.. code-block:: python

    parser = LexborHTMLParser(html)
    node = parser.css_first('div#text')

    # Set attributes
    node.attrs['data'] = 'secret data'
    node.attrs['id'] = 'new_id'
    print(node.attributes)

    # Remove attributes
    del node.attrs['id']
    print(node.attributes)
    print(node.html)

**Output:**

.. code-block:: text

    {'id': 'new_id', 'data': 'secret data'}
    {'data': 'secret data'}
    <div data="secret data">
            <p class="p3" style="display:none;">Excepteur <i>sint</i> occaecat cupidatat non proident</p>
            <p class="p3" vid>Lorem ipsum</p>
        </div>

Inserting Nodes
~~~~~~~~~~~~~~~

Insert new content into the DOM at specific positions.

.. code-block:: python

    html = """
    <div id="container">
        <span class="red"></span>
        <span class="green"></span>
        <span class="red"></span>
        <span class="green"></span>
    </div>
    """

    parser = LexborHTMLParser(html)

    # Insert text before an element
    red_node = parser.css_first('.red')
    red_node.insert_before("Hello")

    # Insert HTML nodes
    subtree = LexborHTMLParser("<div>Hi</div>")
    green_node = parser.css_first('.green')
    green_node.insert_before(subtree)

    # Insert before, after, or as child
    car_div = parser.create_node("div")
    car_div.inner_html = "Car"
    green_node.insert_before(car_div)
    green_node.insert_after(car_div)
    green_node.insert_child(car_div)

    print(parser.body.html)

Tree Traversal
--------------

Walk  every node in the DOM tree and extract text content.

.. code-block:: python

    parser = LexborHTMLParser(html)

    # Traverse the entire tree
    for node in parser.root.traverse(include_text=True):
        if node.tag == '-text':
            text = node.text(deep=True).strip()
            if text:
                print(text)
        else:
            print(node.tag)

**Output:**

.. code-block:: text

    html
    head
    body
    div
    p
    Excepteur
    i
    sint
    occaecat cupidatat non proident
    p
    Lorem ipsum
    div
    p
    Lorem ipsum dolor sit amet, ea quo modus meliore platonem.


Common Patterns
---------------

Extract Text Content
~~~~~~~~~~~~~~~~~~~~

Extract text content from HTML elements with various formatting options.

.. code-block:: python

    parser = LexborHTMLParser('<div><p>Hello <b>world</b>!</p></div>')

    # Get text content with different options
    node = parser.css_first('p')

    # Get all text content
    print(node.text())  # "Hello world!"

    # Get text with custom separator
    print(node.text(separator=' | '))  # "Hello | world | !"

    # Get text without stripping whitespace
    print(node.text(strip=False))

**Output:**

.. code-block:: text

    Hello world!
    Hello  | world | !
    Hello world!

Clean HTML
~~~~~~~~~~

Remove potentially dangerous or unwanted HTML elements.

.. code-block:: python

    dirty_html = '''
    <div>
        <p>Good content</p>
        <script>alert('xss')</script>
        <style>body { color: red; }</style>
        <p>More content</p>
    </div>
    '''

    parser = LexborHTMLParser(dirty_html)

    # Remove unwanted tags
    for tag in parser.css('script, style'):
        tag.decompose()

    print(parser.body.html)

**Output:**

.. code-block:: text

    <body><div>
        <p>Good content</p>


        <p>More content</p>
    </div>
    </body>

Extract Links and Images
~~~~~~~~~~~~~~~~~~~~~~~~

Extract all links and images from HTML content.

.. code-block:: python

    html = '''
    <div>
        <a href="https://example.com">Link 1</a>
        <a href="/page2">Link 2</a>
        <img src="image1.jpg" alt="Image 1">
        <img src="image2.png" alt="Image 2">
    </div>
    '''

    parser = LexborHTMLParser(html)

    # Extract all links
    for link in parser.css('a[href]'):
        print(f"Link: {link.text()} -> {link.attrs['href']}")

    # Extract all images
    for img in parser.css('img[src]'):
        print(f"Image: {img.attrs.get('alt', 'No alt')} -> {img.attrs['src']}")

**Output:**

.. code-block:: text

    Link: Link 1 -> https://example.com
    Link: Link 2 -> /page2
    Image: Image 1 -> image1.jpg
    Image: Image 2 -> image2.png


Advanced selectors
------------------

Text Content Filtering
~~~~~~~~~~~~~~~~~~~~~~

Use advanced selectors to filter elements based on their text content.

.. code-block:: python

    html = """
    <script>
     var super_variable = 100;
    </script>
    <script>
     console.log('debug');
    </script>
    """

    parser = LexborHTMLParser(html)

    # Filter script tags containing specific text
    scripts_with_super = parser.select('script').text_contains("super").matches
    print([node.text() for node in scripts_with_super])

**Output:**

.. code-block:: text

    ['\n var super_variable = 100;\n']

CSS Attribute and Pseudo-class Selectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    html = """
    <div>
        <article class="post published" data-id="1">
            <h2>First Post</h2>
            <p>Content of first post</p>
            <div class="meta">
                <span class="author">John</span>
                <span class="date">2023-01-01</span>
            </div>
        </article>
        <article class="post draft" data-id="2">
            <h2>Second Post</h2>
            <p>Content of second post</p>
            <div class="meta">
                <span class="author">Jane</span>
                <span class="date">2023-01-02</span>
            </div>
        </article>
        <aside class="sidebar">
            <div class="widget">
                <h3>Popular Posts</h3>
                <ul>
                    <li><a href="#1">First Post</a></li>
                    <li><a href="#2">Second Post</a></li>
                </ul>
            </div>
        </aside>
    </div>
    """

    parser = LexborHTMLParser(html)

    # Attribute selectors
    published_posts = parser.css('article.post.published')
    print(f"Published posts: {len(published_posts)}")

    # Descendant selectors
    authors = parser.css('article .meta .author')
    for author in authors:
        print(f"Author: {author.text()}")

    # Pseudo-class selectors
    first_article = parser.css('article:first-child')
    if first_article:
        print(f"First article title: {first_article[0].css_first('h2').text()}")

    # Attribute value selectors
    specific_post = parser.css_first('article[data-id="1"]')
    if specific_post:
        print(f"Post ID 1 title: {specific_post.css_first('h2').text()}")

**Output:**

.. code-block:: text

    Published posts: 1
    Author: John
    Author: Jane
    First article title: First Post
    Post ID 1 title: First Post

Text Content Pseudo-class Selectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use lexbor-specific pseudo-classes for case-sensitive and case-insensitive text matching.

.. code-block:: python

    html = '<div><p>hello </p><p id="main">lexbor is AwesOme</p></div>'
    parser = LexborHTMLParser(html)

    # Case-insensitive search
    results_ci = parser.css('p:lexbor-contains("awesome" i)')
    print(f"Case-insensitive results: {len(results_ci)}")

    # Case-sensitive search
    results_cs = parser.css('p:lexbor-contains("AwesOme")')
    print(f"Case-sensitive results: {len(results_cs)}")
    print(f"Matching text: {results_cs[0].text()}")

**Output:**

.. code-block:: text

    Case-insensitive results: 1
    Case-sensitive results: 1
    Matching text: lexbor is AwesOme

Sibling Navigation
------------------

Navigate between sibling elements in the DOM.

.. code-block:: python

    html = """
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact" class="active">Contact</a>
        <a href="/blog">Blog</a>
    </nav>
    """

    parser = LexborHTMLParser(html)
    active_link = parser.css_first("a.active")

    if active_link:
        print(f"Active link: {active_link.text()}")
        # We need to call it twice, because there are text nodes (spaces and new lines) between <a> elements
        if active_link.prev:
            print(f"Previous link: {active_link.prev.prev.text()}")

        if active_link.next:
            print(f"Next link: {active_link.next.next.text()}")

**Output:**

.. code-block:: text

    Active link: Contact
    Previous link: About
    Next link: Blog


Table Parsing
-------------

Parse HTML tables and extract structured data.

.. code-block:: python

    table_html = """
    <table class="data-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>City</th>
                <th>Occupation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Alice Johnson</td>
                <td>28</td>
                <td>New York</td>
                <td>Software Engineer</td>
            </tr>
            <tr>
                <td>Bob Smith</td>
                <td>35</td>
                <td>Los Angeles</td>
                <td>Designer</td>
            </tr>
            <tr>
                <td>Carol Brown</td>
                <td>42</td>
                <td>Chicago</td>
                <td>Manager</td>
            </tr>
        </tbody>
    </table>
    """

    parser = LexborHTMLParser(table_html)

    # Extract headers
    headers = [th.text() for th in parser.css('thead th')]
    print("Headers:", headers)

    # Extract data rows
    rows = []
    for tr in parser.css('tbody tr'):
        row_data = [td.text() for td in tr.css('td')]
        rows.append(row_data)

    # Display as structured data
    for i, row in enumerate(rows):
        print(f"\nRow {i+1}:")
        for header, value in zip(headers, row):
            print(f"  {header}: {value}")

**Output:**

.. code-block:: text

    Headers: ['Name', 'Age', 'City', 'Occupation']

    Row 1:
      Name: Alice Johnson
      Age: 28
      City: New York
      Occupation: Software Engineer

    Row 2:
      Name: Bob Smith
      Age: 35
      City: Los Angeles
      Occupation: Designer

    Row 3:
      Name: Carol Brown
      Age: 42
      City: Chicago
      Occupation: Manager

Form Data Extraction
--------------------

Parse HTML forms and extract input data.

.. code-block:: python

    form_html = """
    <form id="contact-form" method="post" action="/submit">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" value="John Doe" required>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="john@example.com">
        </div>
        <div class="form-group">
            <label for="country">Country:</label>
            <select id="country" name="country">
                <option value="us">United States</option>
                <option value="ca" selected>Canada</option>
                <option value="uk">United Kingdom</option>
            </select>
        </div>
        <div class="form-group">
            <label>
                <input type="checkbox" name="newsletter" checked> Subscribe to newsletter
            </label>
        </div>
        <div class="form-group">
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4">Hello there!</textarea>
        </div>
        <button type="submit">Submit</button>
    </form>
    """

    parser = LexborHTMLParser(form_html)

    # Extract form metadata
    form = parser.css_first('form')
    print(f"Form ID: {form.attrs.get('id')}")
    print(f"Form method: {form.attrs.get('method')}")
    print(f"Form action: {form.attrs.get('action')}")

    # Extract input fields
    print("\nInput fields:")
    for input_field in parser.css('input'):
        field_type = input_field.attrs.get('type', 'text')
        name = input_field.attrs.get('name')
        value = input_field.attrs.get('value', '')
        checked = 'checked' in input_field.attrs

        print(f"  {name} ({field_type}): {value} {'[checked]' if checked else ''}")

    # Extract select options
    print("\nSelect fields:")
    for select in parser.css('select'):
        name = select.attrs.get('name')
        print(f"  {name}:")
        for option in select.css('option'):
            value = option.attrs.get('value')
            text = option.text()
            selected = 'selected' in option.attrs
            print(f"    {value}: {text} {'[selected]' if selected else ''}")

    # Extract textarea
    print("\nTextarea fields:")
    for textarea in parser.css('textarea'):
        name = textarea.attrs.get('name')
        content = textarea.text()
        print(f"  {name}: {content}")

**Output:**

.. code-block:: text

    Form ID: contact-form
    Form method: post
    Form action: /submit

    Input fields:
      name (text): John Doe
      email (email):
      newsletter (checkbox):  [checked]

    Select fields:
      country:
        us: United States
        ca: Canada [selected]
        uk: United Kingdom

    Textarea fields:
      message: Hello there!

```

### `docs/index.rst`

```rst
selectolax
==========

Selectolax is a fast HTML5 parser with CSS selectors, written in Cython,
using [Modest](https://github.com/lexborisov/Modest/) and [Lexbor](https://github.com/lexbor/lexbor) engines.

It supports two backends:

- `Lexbor <https://github.com/lexbor/lexbor>`__ (preferred)
- `Modest <https://github.com/lexborisov/Modest>`__ (first generation of lexbor, **deprecated**)

API
===

.. toctree::
   :maxdepth: 2

   parser
   lexbor
   examples


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

```

### `docs/lexbor.rst`

```rst
selectolax.lexbor module
========================

.. automodule:: selectolax.lexbor

LexborHTMLParser
----------------

.. autoclass:: LexborHTMLParser
    :members:


LexborNode
----------

.. autoclass:: LexborNode
    :members:

Selector
--------

.. autoclass:: LexborSelector
    :members:

```

### `docs/make.bat`

```bat
@ECHO OFF

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set BUILDDIR=_build
set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% .
set I18NSPHINXOPTS=%SPHINXOPTS% .
if NOT "%PAPER%" == "" (
	set ALLSPHINXOPTS=-D latex_paper_size=%PAPER% %ALLSPHINXOPTS%
	set I18NSPHINXOPTS=-D latex_paper_size=%PAPER% %I18NSPHINXOPTS%
)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  html       to make standalone HTML files
	echo.  dirhtml    to make HTML files named index.html in directories
	echo.  singlehtml to make a single large HTML file
	echo.  pickle     to make pickle files
	echo.  json       to make JSON files
	echo.  htmlhelp   to make HTML files and a HTML help project
	echo.  qthelp     to make HTML files and a qthelp project
	echo.  devhelp    to make HTML files and a Devhelp project
	echo.  epub       to make an epub
	echo.  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter
	echo.  text       to make text files
	echo.  man        to make manual pages
	echo.  texinfo    to make Texinfo files
	echo.  gettext    to make PO message catalogs
	echo.  changes    to make an overview over all changed/added/deprecated items
	echo.  xml        to make Docutils-native XML files
	echo.  pseudoxml  to make pseudoxml-XML files for display purposes
	echo.  linkcheck  to check all external links for integrity
	echo.  doctest    to run all doctests embedded in the documentation if enabled
	goto end
)

if "%1" == "clean" (
	for /d %%i in (%BUILDDIR%\*) do rmdir /q /s %%i
	del /q /s %BUILDDIR%\*
	goto end
)


%SPHINXBUILD% 2> nul
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

if "%1" == "html" (
	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%/html
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/html.
	goto end
)

if "%1" == "dirhtml" (
	%SPHINXBUILD% -b dirhtml %ALLSPHINXOPTS% %BUILDDIR%/dirhtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/dirhtml.
	goto end
)

if "%1" == "singlehtml" (
	%SPHINXBUILD% -b singlehtml %ALLSPHINXOPTS% %BUILDDIR%/singlehtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/singlehtml.
	goto end
)

if "%1" == "pickle" (
	%SPHINXBUILD% -b pickle %ALLSPHINXOPTS% %BUILDDIR%/pickle
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can process the pickle files.
	goto end
)

if "%1" == "json" (
	%SPHINXBUILD% -b json %ALLSPHINXOPTS% %BUILDDIR%/json
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can process the JSON files.
	goto end
)

if "%1" == "htmlhelp" (
	%SPHINXBUILD% -b htmlhelp %ALLSPHINXOPTS% %BUILDDIR%/htmlhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can run HTML Help Workshop with the ^
.hhp project file in %BUILDDIR%/htmlhelp.
	goto end
)

if "%1" == "qthelp" (
	%SPHINXBUILD% -b qthelp %ALLSPHINXOPTS% %BUILDDIR%/qthelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can run "qcollectiongenerator" with the ^
.qhcp project file in %BUILDDIR%/qthelp, like this:
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\selectolax.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\selectolax.ghc
	goto end
)

if "%1" == "devhelp" (
	%SPHINXBUILD% -b devhelp %ALLSPHINXOPTS% %BUILDDIR%/devhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished.
	goto end
)

if "%1" == "epub" (
	%SPHINXBUILD% -b epub %ALLSPHINXOPTS% %BUILDDIR%/epub
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The epub file is in %BUILDDIR%/epub.
	goto end
)

if "%1" == "latex" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; the LaTeX files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "latexpdf" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	cd %BUILDDIR%/latex
	make all-pdf
	cd %BUILDDIR%/..
	echo.
	echo.Build finished; the PDF files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "latexpdfja" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	cd %BUILDDIR%/latex
	make all-pdf-ja
	cd %BUILDDIR%/..
	echo.
	echo.Build finished; the PDF files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "text" (
	%SPHINXBUILD% -b text %ALLSPHINXOPTS% %BUILDDIR%/text
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The text files are in %BUILDDIR%/text.
	goto end
)

if "%1" == "man" (
	%SPHINXBUILD% -b man %ALLSPHINXOPTS% %BUILDDIR%/man
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The manual pages are in %BUILDDIR%/man.
	goto end
)

if "%1" == "texinfo" (
	%SPHINXBUILD% -b texinfo %ALLSPHINXOPTS% %BUILDDIR%/texinfo
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The Texinfo files are in %BUILDDIR%/texinfo.
	goto end
)

if "%1" == "gettext" (
	%SPHINXBUILD% -b gettext %I18NSPHINXOPTS% %BUILDDIR%/locale
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The message catalogs are in %BUILDDIR%/locale.
	goto end
)

if "%1" == "changes" (
	%SPHINXBUILD% -b changes %ALLSPHINXOPTS% %BUILDDIR%/changes
	if errorlevel 1 exit /b 1
	echo.
	echo.The overview file is in %BUILDDIR%/changes.
	goto end
)

if "%1" == "linkcheck" (
	%SPHINXBUILD% -b linkcheck %ALLSPHINXOPTS% %BUILDDIR%/linkcheck
	if errorlevel 1 exit /b 1
	echo.
	echo.Link check complete; look for any errors in the above output ^
or in %BUILDDIR%/linkcheck/output.txt.
	goto end
)

if "%1" == "doctest" (
	%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest
	if errorlevel 1 exit /b 1
	echo.
	echo.Testing of doctests in the sources finished, look at the ^
results in %BUILDDIR%/doctest/output.txt.
	goto end
)

if "%1" == "xml" (
	%SPHINXBUILD% -b xml %ALLSPHINXOPTS% %BUILDDIR%/xml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The XML files are in %BUILDDIR%/xml.
	goto end
)

if "%1" == "pseudoxml" (
	%SPHINXBUILD% -b pseudoxml %ALLSPHINXOPTS% %BUILDDIR%/pseudoxml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The pseudo-XML files are in %BUILDDIR%/pseudoxml.
	goto end
)

:end

```

### `docs/Makefile`

```
# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  latexpdfja to make LaTeX files and run them through platex/dvipdfmx"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  xml        to make Docutils-native XML files"
	@echo "  pseudoxml  to make pseudoxml-XML files for display purposes"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/selectolax.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/selectolax.qhc"

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/selectolax"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/selectolax"
	@echo "# devhelp"

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

latexpdfja:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through platex and dvipdfmx..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf-ja
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

texinfo:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make' in that directory to run these through makeinfo" \
	      "(use \`make info' here to do that automatically)."

info:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo "Running Texinfo files through makeinfo..."
	make -C $(BUILDDIR)/texinfo info
	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."

gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

xml:
	$(SPHINXBUILD) -b xml $(ALLSPHINXOPTS) $(BUILDDIR)/xml
	@echo
	@echo "Build finished. The XML files are in $(BUILDDIR)/xml."

pseudoxml:
	$(SPHINXBUILD) -b pseudoxml $(ALLSPHINXOPTS) $(BUILDDIR)/pseudoxml
	@echo
	@echo "Build finished. The pseudo-XML files are in $(BUILDDIR)/pseudoxml."

```

### `docs/modules.rst`

```rst
selectolax
==========

.. toctree::
   :maxdepth: 4

   selectolax

```

### `docs/parser.rst`

```rst
selectolax.parser module
======================================

.. automodule:: selectolax.parser

HtmlParser
----------

.. autoclass:: HTMLParser
    :members:


Node
----

.. autoclass:: Node
    :members:

Selector
--------

.. autoclass:: Selector
    :members:

```

### `docs/selectolax.rst`

```rst
selectolax package
==================

Submodules
----------

selectolax.lexbor module
------------------------

.. automodule:: selectolax.lexbor
   :members:
   :undoc-members:
   :show-inheritance:

selectolax.parser module
------------------------

.. automodule:: selectolax.parser
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: selectolax
   :members:
   :undoc-members:
   :show-inheritance:

```

### `examples/benchmark.py`

```py
# coding:utf-8
"""A simple benchmark that measures speed of lxml and selectolax.

How the benchmark works
-----------------------

For each page, we extract:

1) Title
2) Number of script tag
3) The ``href`` attribute from all links
4) The content of the Meta description tag

"""
import functools
import json
import time

from bs4 import BeautifulSoup
from html5_parser import parse
from lxml.html import fromstring
from selectolax.parser import HTMLParser

from selectolax.lexbor import LexborHTMLParser

bad_urls = []


def bs4_parser(html_content, parser=HTMLParser):
    soup = BeautifulSoup(html_content, 'html.parser')
    title_text = soup.title.string
    assert title_text

    a_hrefs = [a.attrs.get('href', '') for a in soup.find_all('a')]
    assert len(a_hrefs) >= 5, 'href'

    num_script_tags = len(soup.find_all('script'))
    assert num_script_tags > 0, 'script'
    meta_description = soup.find('meta', attrs={"name": "description"})
    if meta_description:
        meta_content = meta_description.get('content')


def selectolax_parser(html_content, parser=HTMLParser):
    tree = parser(html_content)
    title_text = ""
    title_node = tree.css_first('title')
    if title_node:
        title_text = title_node.text()
    assert title_text

    a_hrefs = [a.attrs.get('href', '') for a in tree.css('a[href]')]
    assert len(a_hrefs) >= 5, 'href'

    num_script_tags = len(tree.css('script'))
    assert num_script_tags > 0, 'script'
    meta_description = tree.css_first('meta[name="description"]')
    if meta_description:
        meta_content = meta_description.attrs.sget('content', '')


def lxml_parser(html_content):
    tree = fromstring(html_content)
    title_text = tree.xpath('//title/text()')
    assert title_text, 'title'

    a_hrefs = [a.attrib.get('href', '') for a in tree.xpath('//a[@href]')]
    assert len(a_hrefs) >= 5, 'href'

    num_script_tags = len(tree.xpath('//script'))
    assert num_script_tags > 0, 'script'
    meta_description = tree.xpath('meta[@name="description"]')
    if meta_description:
        meta_content = meta_description[0].attrib.get('content', '')


def html5_parser(html_content):
    tree = parse(html_content)
    title_text = tree.xpath('//title/text()')
    assert title_text, 'title'

    a_hrefs = [a.attrib.get('href', '') for a in tree.xpath('//a[@href]')]
    assert len(a_hrefs) >= 5, 'href'

    num_script_tags = len(tree.xpath('//script'))
    assert num_script_tags > 0, 'script'
    meta_description = tree.xpath('meta[@name="description"]')
    if meta_description:
        meta_content = meta_description[0].attrib.get('content', '')


def _perform_test(pages, parse_func):
    for page in pages:
        parse_func(page['html'])


def main():
    #
    # This file contains 754 main pages from the top internet domains (according to Alexa rank).
    # That translates to 324MB of HTML data.
    # Because of potential copyright infringements, I don't publish it.
    #
    html_pages = [json.loads(page) for page in open('pages/pages.json', 'rt')]
    available_parsers = [
        ('bs4', bs4_parser,),
        ('lxml', lxml_parser,),
        ('html5_parser', html5_parser,),
        ('modest', selectolax_parser,),
        ('lexbor', functools.partial(selectolax_parser, parser=LexborHTMLParser)),
    ]
    for parser_name, parser in available_parsers:
        start = time.time()
        _perform_test(html_pages, parser)
        print('%r: %s' % (parser_name, time.time() - start))


if __name__ == '__main__':
    main()

```

### `examples/simple_example.py`

```py
from selectolax.lexbor import LexborHTMLParser

html = "<div><p id=p1><p id=p2><p id=p3><a>link</a><p id=p4><p id=p5>text<p id=p6></div>"
selector = "div > :nth-child(2n+1):not(:has(a))"

for node in LexborHTMLParser(html).css(selector):
    print(node.attributes, node.text(), node.tag)
    print(node.parent.tag)
    print(node.html)

```

### `LICENSE`

```

MIT License

Copyright (c) 2018-2026, Artem Golubin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

### `Makefile`

```
.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -rf .eggs/
	find . -maxdepth 1 -name '*.egg-info' -exec rm -fr {} +
	find . -maxdepth 1 -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/

lint: ## check style with ruff
	ruff format selectolax tests
	ruff check --fix selectolax tests
	cython-lint selectolax/
	mypy selectolax tests

.PHONY: test
test: ## run tests quickly with the default Python
	pytest tests -s -v

coverage: ## check code coverage quickly with the default Python
	coverage run --source selectolax -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/selectolax.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ selectolax
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: clean ## package and upload a release
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

dev:
	python setup.py build_ext --inplace --cython --lexbor

dev-static: clean-build
	python setup.py build_ext --inplace --cython --static --disable-modest

```

### `MANIFEST.in`

```in
include CONTRIBUTING.rst
include HISTORY.rst
include LICENSE
include README.md
include CHANGES.md

include selectolax/*
include selectolax/lexbor/*
include selectolax/modest/*

include selectolax/lexbor/*.so
exclude selectolax/*.so


recursive-include modest/source *.c *.h
recursive-include modest/include *.h
include modest/*
include modest/include/*
include modest/source/*

recursive-include lexbor/source *.c *.h
include lexbor/*
include lexbor/source/*

recursive-include tests *
recursive-exclude * __pycache__
recursive-exclude * *.py[co]

recursive-include docs *.rst conf.py Makefile make.bat *.jpg *.png *.gif

```

### `pyproject.toml`

```toml
[build-system]
requires = [
    "wheel",
    "Cython",
    "setuptools>=62.4",
]

[project]
name = 'selectolax'
version = '0.4.11'
description = 'A fast HTML5 parser with CSS selectors, written in Cython, using Modest and Lexbor engines.'
readme = 'README.md'
requires-python = '>=3.9,<3.15'
license = 'MIT'
authors = [
    { name = 'Artem Golubin', email = 'me@rushter.com' }
]
dependencies = []

keywords = [
    "selectolax",
    "html",
    "parser",
    "css",
    "fast",
    "lexbor",
    "modest",
]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: OS Independent",
    "Operating System :: Unix",
    "Programming Language :: Cython",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Internet",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing",
    "Topic :: Text Processing :: Markup",
    "Topic :: Text Processing :: Markup :: HTML",
    "Typing :: Typed",
]

[project.urls]
Homepage = "https://github.com/rushter/selectolax"
Repository = "https://github.com/rushter/selectolax"
Documentation = "https://selectolax.readthedocs.io/en/latest/parser.html"
Changelog = "https://github.com/rushter/selectolax/blob/master/CHANGES.md"

[tool.cibuildwheel]
build-frontend = "build"
build-verbosity = 1

[tool.cibuildwheel.linux]
environment = { LDFLAGS = "-Wl,--strip-debug" }

skip = [
    "*-manylinux_i686",
    "*-musllinux_i686",
    "*-win32*",
    "pp*"
]
test-skip = "*-macosx_arm64"

[project.optional-dependencies]
cython = [
    "Cython",
]

[tool.cython-lint]
max-line-length = 120
ignore = ['E221', 'E222', ]

[tool.setuptools.packages.find]
include = ["selectolax*"]

```

### `README.md`

```md
![selectolax logo](docs/logo.png)

---

A fast HTML5 parser with CSS selectors, written in Cython,
using [Modest](https://github.com/lexborisov/Modest/) and [Lexbor](https://github.com/lexbor/lexbor) engines.

---

[![PyPI - Version](https://img.shields.io/pypi/v/selectolax?logo=pypi&label=Pypi&logoColor=fff)](https://pypi.org/project/selectolax)
[![PyPI Total Downloads](https://static.pepy.tech/badge/selectolax)](https://pepy.tech/projects/selectolax)
[![CI](https://img.shields.io/github/actions/workflow/status/rushter/selectolax/pythonpackage.yml?branch=master&logo=githubactions&label=CI)](https://github.com/rushter/selectolax/actions/workflows/pythonpackage.yml?query=branch%3Amaster+event%3Apush)
[![Python Versions](https://img.shields.io/pypi/pyversions/selectolax?logo=python&logoColor=fff&label=Python)](https://pypi.org/project/selectolax)
[![GitHub License](https://img.shields.io/github/license/rushter/selectolax?logo=github&label=License)](https://github.com/rushter/selectolax/blob/master/LICENSE)

---

## Installation

From PyPI using pip:

```bash
pip install selectolax
```

If installation fails due to compilation errors, you may need to install [Cython](https://github.com/cython/cython):

```bash
pip install selectolax[cython]
```

This usually happens when you try to install an outdated version of selectolax on a newer version of Python.

Development version from GitHub:

```bash
git clone --recursive  https://github.com/rushter/selectolax
cd selectolax
pip install -r requirements_dev.txt
python setup.py install
```

How to compile selectolax while developing:

```bash
make clean
make dev
```

## Basic examples

Here are some basic examples to get you started with selectolax:

Parsing HTML and extracting text:

```python
In [1]: from selectolax.lexbor import LexborHTMLParser
   ...:
   ...: html = """
   ...: <h1 id="title" data-updated="20201101">Hi there</h1>
   ...: <div class="post">Lorem Ipsum is simply dummy text of the printing and typesetting industry. </div>
   ...: <div class="post">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
   ...: """
   ...: tree = LexborHTMLParser(html)

In [2]: tree.css_first('h1#title').text()
Out[2]: 'Hi there'

In [3]: tree.css_first('h1#title').attributes
Out[3]: {'id': 'title', 'data-updated': '20201101'}

In [4]: [node.text() for node in tree.css('.post')]
Out[4]:
['Lorem Ipsum is simply dummy text of the printing and typesetting industry. ',
 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.']
```

### Using advanced CSS selectors

```python
In [1]: html = "<div><p id=p1><p id=p2><p id=p3><a>link</a><p id=p4><p id=p5>text<p id=p6></div>"
   ...: selector = "div > :nth-child(2n+1):not(:has(a))"

In [2]: for node in LexborHTMLParser(html).css(selector):
   ...:     print(node.attributes, node.text(), node.tag)
   ...:     print(node.parent.tag)
   ...:     print(node.html)
   ...:
{'id': 'p1'}  p
div
<p id="p1"></p>
{'id': 'p5'} text p
div
<p id="p5">text</p>
```

#### Using `lexbor-contains` CSS pseudo-class to match text

```python
from selectolax.lexbor import LexborHTMLParser
html = "<div><p>hello </p><p id='main'>lexbor is AwesOme</p></div>"
parser = LexborHTMLParser(html)
# Case-insensitive search
results = parser.css('p:lexbor-contains("awesome" i)')
# Case-sensitive search
results = parser.css('p:lexbor-contains("AwesOme")')
assert len(results) == 1
assert results[0].text() == "lexbor is AwesOme"
```

* [More examples](https://selectolax.readthedocs.io/en/latest/examples.html)

### Available backends

Selectolax supports two backends: `Modest` and `Lexbor`. By default, all examples use the `Lexbor` backend.
Most of the features between backends are almost identical, but there are some differences.

As of 2024, the preferred backend is `Lexbor`. The `Modest` backend is still available for compatibility reasons
and the underlying C library that selectolax uses is not maintained anymore.

To use `lexbor`, just import the parser and use it in the similar way to the `HTMLParser`.

```python
In [1]: from selectolax.lexbor import LexborHTMLParser

In [2]: html = """
   ...: <title>Hi there</title>
   ...: <div id="updated">2021-08-15</div>
   ...: """

In [3]: parser = LexborHTMLParser(html)
In [4]: parser.root.css_first("#updated").text()
Out[4]: '2021-08-15'
```

## Simple Benchmark

* Extract title, links, scripts and a meta tag from main pages of top 754 domains. See `examples/benchmark.py` for more information.

| Package                       | Time      |
|-------------------------------|-----------|
| Beautiful Soup (html.parser)  | 61.02 sec.|
| lxml / Beautiful Soup (lxml)  | 9.09 sec. |
| html5_parser                  | 16.10 sec.|
| selectolax (Modest)           | 2.94 sec. |
| selectolax (Lexbor)           | 2.39 sec. |

## Links

* [selectolax API reference and examples](https://selectolax.readthedocs.io/en/latest/index.html)
* [Video introduction to web scraping using selectolax](https://youtu.be/HpRsfpPuUzE)
* [How to Scrape 7k Products with Python using selectolax and httpx](https://www.youtube.com/watch?v=XpGvq755J2U)
* [Modest introduction](https://lexborisov.github.io/Modest/)
* [Modest benchmark](https://lexborisov.github.io/benchmark-html-parsers/)
* [Python benchmark](https://rushter.com/blog/python-fast-html-parser/)
* [Another Python benchmark](https://www.peterbe.com/plog/selectolax-or-pyquery)
* [Universal interface to lxml and selectolax](https://github.com/lorien/domselect)

## License

* Modest engine — [LGPL2.1](https://github.com/lexborisov/Modest/blob/master/LICENSE)
* lexbor engine — [Apache-2.0 license](https://github.com/lexbor/lexbor?tab=Apache-2.0-1-ov-file#readme)
* selectolax - [MIT](https://github.com/rushter/selectolax/blob/master/LICENSE)


## Contributors

Thanks to all the contributors of selectolax!

<a href="https://github.com/rushter/selectolax/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=rushter/selectolax" />
</a>

```

### `requirements_dev.txt`

```txt
pip>=18.0
bumpversion>=0.5.3
wheel>=0.29.0
watchdog>=0.8.3
tox>=2.3.1
coverage>=4.1
Sphinx==8.0.2
numpydoc==1.8.0
pytest>=3.7.2
pytest-runner>=4.2
Cython>=3.0.11
pluggy>=0.7.1
mypy==1.4.1
types-pyinstaller==6.10.0.20240812
furo==2024.8.6
sphinxext-opengraph==0.9.1
sphinx-copybutton==0.5.2
ruff
setuptools>=75.7.0
pytest-mypy-plugins>=3.2,<4.0.0
cython-lint

```

### `ruff.toml`

```toml
[lint.per-file-ignores]
"__init__.py" = ["F401"]
```

### `selectolax/__init__.py`

```py
# -*- coding: utf-8 -*-


__author__ = """Artem Golubin"""
__email__ = "me@rushter.com"
__version__ = "0.4.11"

from . import lexbor, modest, parser

```

### `selectolax/base.pxi`

```pxi

class SelectolaxError(Exception):
    """An exception that indicates error."""
    pass

```

### `selectolax/lexbor.pxd`

```pxd
# cython: freethreading_compatible = True
from libc.stdint cimport uint8_t, uint32_t, uintptr_t

cdef extern from "lexbor/core/core.h" nogil:
    ctypedef uint32_t lxb_codepoint_t
    ctypedef unsigned char lxb_char_t
    ctypedef unsigned int lxb_status_t
    ctypedef enum lexbor_status_t:
        LXB_STATUS_OK = 0x0000
        LXB_STATUS_ERROR = 0x0001
        LXB_STATUS_ERROR_MEMORY_ALLOCATION
        LXB_STATUS_ERROR_OBJECT_IS_NULL
        LXB_STATUS_ERROR_SMALL_BUFFER
        LXB_STATUS_ERROR_INCOMPLETE_OBJECT
        LXB_STATUS_ERROR_NO_FREE_SLOT
        LXB_STATUS_ERROR_TOO_SMALL_SIZE
        LXB_STATUS_ERROR_NOT_EXISTS
        LXB_STATUS_ERROR_WRONG_ARGS
        LXB_STATUS_ERROR_WRONG_STAGE
        LXB_STATUS_ERROR_UNEXPECTED_RESULT
        LXB_STATUS_ERROR_UNEXPECTED_DATA
        LXB_STATUS_ERROR_OVERFLOW
        LXB_STATUS_CONTINUE
        LXB_STATUS_SMALL_BUFFER
        LXB_STATUS_ABORTED
        LXB_STATUS_STOPPED
        LXB_STATUS_NEXT
        LXB_STATUS_STOP

    lexbor_str_t* lexbor_str_destroy(lexbor_str_t *str, lexbor_mraw_t *mraw, bint destroy_obj)

    lexbor_str_t* lexbor_str_create()
    lxb_char_t * lexbor_str_data_noi(lexbor_str_t *str)

cdef extern from "lexbor/core/lexbor.h" nogil:
    ctypedef void *(*lexbor_memory_malloc_f)(size_t size) nogil
    ctypedef void *(*lexbor_memory_realloc_f)(void *dst, size_t size) nogil
    ctypedef void *(*lexbor_memory_calloc_f)(size_t num, size_t size) nogil
    ctypedef void (*lexbor_memory_free_f)(void *dst) nogil
    lxb_status_t lexbor_memory_setup(
        lexbor_memory_malloc_f new_malloc,
        lexbor_memory_realloc_f new_realloc,
        lexbor_memory_calloc_f new_calloc,
        lexbor_memory_free_f new_free
    )


cdef extern from "lexbor/html/html.h" nogil:
    ctypedef unsigned int lxb_html_document_opt_t

    ctypedef struct lxb_html_tokenizer_t
    ctypedef struct lxb_html_form_element_t
    ctypedef struct lxb_html_head_element_t
    ctypedef struct lxb_html_body_element_t
    ctypedef struct lxb_dom_element_t
    ctypedef struct lexbor_mraw_t
    ctypedef struct lexbor_hash_t
    ctypedef struct lxb_dom_document_type_t
    ctypedef void lxb_dom_interface_t
    ctypedef uintptr_t lxb_tag_id_t
    ctypedef uintptr_t lxb_ns_id_t
    ctypedef lxb_dom_interface_t *(*lxb_dom_interface_destroy_f)(lxb_dom_interface_t *intrfc)
    ctypedef lxb_dom_interface_t *(*lxb_dom_interface_create_f)(lxb_dom_document_t *document, lxb_tag_id_t tag_id,
                                                                lxb_ns_id_t ns)

    ctypedef struct lxb_dom_event_target_t:
        void *events

    ctypedef struct lexbor_str_t:
        lxb_char_t *data
        size_t     length

    ctypedef struct lxb_dom_node_t:
        lxb_dom_event_target_t event_target

        uintptr_t              local_name
        uintptr_t              prefix
        uintptr_t              ns

        lxb_dom_document_t     *owner_document

        lxb_dom_node_t         *next
        lxb_dom_node_t         *prev
        lxb_dom_node_t         *parent
        lxb_dom_node_t         *first_child
        lxb_dom_node_t         *last_child
        void                   *user

        lxb_dom_node_type_t    type

    ctypedef struct lxb_dom_document_t:
        lxb_dom_node_t              node

        lxb_dom_document_cmode_t    compat_mode
        lxb_dom_document_dtype_t    type

        lxb_dom_document_type_t *doctype
        lxb_dom_element_t *element

        lxb_dom_interface_create_f  create_interface
        lxb_dom_interface_destroy_f destroy_interface

        lexbor_mraw_t *mraw
        lexbor_mraw_t *text
        lexbor_hash_t *tags
        lexbor_hash_t *attrs
        lexbor_hash_t *prefix
        lexbor_hash_t *ns
        void *parser
        void *user

        bint                        tags_inherited
        bint                        ns_inherited

        bint                        scripting

    ctypedef  struct lxb_html_document_t:
        lxb_dom_document_t dom_document

        void *iframe_srcdoc

        lxb_html_head_element_t *head
        lxb_html_body_element_t *body
        lxb_html_document_ready_state_t ready_state
        lxb_html_document_opt_t         opt

    ctypedef  enum lxb_html_document_ready_state_t:
        LXB_HTML_DOCUMENT_READY_STATE_UNDEF       = 0x00
        LXB_HTML_DOCUMENT_READY_STATE_LOADING     = 0x01
        LXB_HTML_DOCUMENT_READY_STATE_INTERACTIVE = 0x02
        LXB_HTML_DOCUMENT_READY_STATE_COMPLETE    = 0x03

    ctypedef enum lxb_html_parser_state_t:
        LXB_HTML_PARSER_STATE_BEGIN            = 0x00
        LXB_HTML_PARSER_STATE_PROCESS          = 0x01
        LXB_HTML_PARSER_STATE_END              = 0x02
        LXB_HTML_PARSER_STATE_FRAGMENT_PROCESS = 0x03
        LXB_HTML_PARSER_STATE_ERROR            = 0x04

    ctypedef enum lxb_dom_node_type_t:
        LXB_DOM_NODE_TYPE_ELEMENT                = 0x01
        LXB_DOM_NODE_TYPE_ATTRIBUTE              = 0x02
        LXB_DOM_NODE_TYPE_TEXT                   = 0x03
        LXB_DOM_NODE_TYPE_CDATA_SECTION          = 0x04
        LXB_DOM_NODE_TYPE_ENTITY_REFERENCE       = 0x05
        LXB_DOM_NODE_TYPE_ENTITY                 = 0x06
        LXB_DOM_NODE_TYPE_PROCESSING_INSTRUCTION = 0x07
        LXB_DOM_NODE_TYPE_COMMENT                = 0x08
        LXB_DOM_NODE_TYPE_DOCUMENT               = 0x09
        LXB_DOM_NODE_TYPE_DOCUMENT_TYPE          = 0x0A
        LXB_DOM_NODE_TYPE_DOCUMENT_FRAGMENT      = 0x0B
        LXB_DOM_NODE_TYPE_NOTATION               = 0x0C
        LXB_DOM_NODE_TYPE_LAST_ENTRY             = 0x0D

    ctypedef enum lxb_dom_document_cmode_t:
        LXB_DOM_DOCUMENT_CMODE_NO_QUIRKS = 0x00
        LXB_DOM_DOCUMENT_CMODE_QUIRKS = 0x01
        LXB_DOM_DOCUMENT_CMODE_LIMITED_QUIRKS = 0x02

    ctypedef enum lxb_dom_document_dtype_t:
        LXB_DOM_DOCUMENT_DTYPE_UNDEF = 0x00,
        LXB_DOM_DOCUMENT_DTYPE_HTML = 0x01,
        LXB_DOM_DOCUMENT_DTYPE_XML = 0x02

    ctypedef enum lxb_html_serialize_opt_t:
        LXB_HTML_SERIALIZE_OPT_UNDEF = 0x00
        LXB_HTML_SERIALIZE_OPT_SKIP_WS_NODES = 0x01
        LXB_HTML_SERIALIZE_OPT_SKIP_COMMENT = 0x02
        LXB_HTML_SERIALIZE_OPT_RAW = 0x04
        LXB_HTML_SERIALIZE_OPT_WITHOUT_CLOSING = 0x08
        LXB_HTML_SERIALIZE_OPT_TAG_WITH_NS = 0x10
        LXB_HTML_SERIALIZE_OPT_WITHOUT_TEXT_INDENT = 0x20
        LXB_HTML_SERIALIZE_OPT_FULL_DOCTYPE = 0x40

    ctypedef struct lexbor_array_t:
        void **list
        size_t size
        size_t length

    ctypedef struct lexbor_array_obj_t:
        uint8_t *list
        size_t  size
        size_t  length
        size_t  struct_size

    ctypedef struct lxb_html_tree_pending_table_t
    ctypedef bint lxb_html_tree_insertion_mode_f
    ctypedef lxb_status_t lxb_html_tree_append_attr_f

    ctypedef struct lxb_html_tree_t:

        lxb_html_tokenizer_t *tkz_ref

        lxb_html_document_t *document
        lxb_dom_node_t *fragment

        lxb_html_form_element_t *form

        lexbor_array_t *open_elements
        lexbor_array_t *active_formatting
        lexbor_array_obj_t *template_insertion_modes

        lxb_html_tree_pending_table_t *pending_table

        lexbor_array_obj_t *parse_errors

        bint foster_parenting
        bint frameset_ok
        bint scripting

        lxb_html_tree_insertion_mode_f mode
        lxb_html_tree_insertion_mode_f original_mode
        lxb_html_tree_append_attr_f    before_append_attr

        lxb_status_t status

        size_t ref_count

    ctypedef struct lxb_html_parser_t:
        lxb_html_tokenizer_t *tkz
        lxb_html_tree_t *tree
        lxb_html_tree_t *original_tree

        lxb_dom_node_t *root
        lxb_dom_node_t *form

        lxb_html_parser_state_t state
        lxb_status_t status

        size_t  ref_count

    ctypedef struct lxb_html_element_t

    # Functions
    lxb_html_parser_t * lxb_html_parser_create()
    lxb_status_t lxb_html_parser_init(lxb_html_parser_t *parser)
    lxb_html_parser_t * lxb_html_parser_destroy(lxb_html_parser_t *parser)
    lxb_html_document_t * lxb_html_document_create()
    lxb_html_element_t * lxb_html_document_create_element(lxb_html_document_t *document,
                                                          const lxb_char_t *local_name, size_t lname_len,
                                                          void *reserved_for_opt)
    lxb_status_t lxb_html_document_parse(lxb_html_document_t *document, const lxb_char_t *html, size_t size)
    lxb_dom_node_t * lxb_html_parse_fragment_by_tag_id(lxb_html_parser_t *parser,
                                                       lxb_html_document_t *document,
                                                       lxb_tag_id_t tag_id,
                                                       lxb_ns_id_t ns,
                                                       const lxb_char_t *html,
                                                       size_t size)
    lxb_dom_node_t * lxb_html_document_parse_fragment(lxb_html_document_t *document,
                                                      lxb_dom_element_t *element,
                                                      const lxb_char_t *html,
                                                      size_t size)
    lxb_html_body_element_t * lxb_html_document_body_element_noi(lxb_html_document_t *document)
    lxb_html_head_element_t * lxb_html_document_head_element_noi(lxb_html_document_t *document)
    lxb_dom_element_t * lxb_dom_document_element(lxb_dom_document_t *document)

    lxb_status_t lxb_html_serialize_tree_str(lxb_dom_node_t *node, lexbor_str_t *str)
    lxb_status_t lxb_html_serialize_deep_str(lxb_dom_node_t *node, lexbor_str_t *str)
    lxb_status_t lxb_html_serialize_pretty_tree_str(lxb_dom_node_t *node,
                                                    lxb_html_serialize_opt_t opt,
                                                    size_t indent,
                                                    lexbor_str_t *str)
    lxb_status_t lxb_html_serialize_pretty_deep_str(lxb_dom_node_t *node,
                                                    lxb_html_serialize_opt_t opt,
                                                    size_t indent,
                                                    lexbor_str_t *str)
    lxb_html_element_t* lxb_html_element_inner_html_set(lxb_html_element_t *element,
                                                        const lxb_char_t *html, size_t size)

cdef class LexborNode:
    cdef:
        lxb_dom_node_t *node
        public LexborHTMLParser parser
        cdef bint _is_fragment_root

    @staticmethod
    cdef LexborNode new(lxb_dom_node_t *node, LexborHTMLParser parser)
    cdef void set_as_fragment_root(self)
    cdef str _serialize_html(self, lxb_html_serialize_opt_t options, size_t indent, bint pretty)
    cdef str _serialize_inner_html(self, lxb_html_serialize_opt_t options, size_t indent, bint pretty)
    cdef inline LexborNode _get_node(self)


cdef bint is_empty_text_node(lxb_dom_node_t *node)
cdef inline bint _is_whitespace_only(const lxb_char_t *buffer, size_t buffer_length) nogil


cdef class LexborCSSSelector:
    cdef lxb_css_parser_t* parser
    cdef lxb_selectors_t * selectors
    cdef lxb_css_selectors_t * css_selectors
    cdef public list results
    cdef public LexborNode current_node
    cdef int _create_css_parser(self) except -1
    cpdef list find(self, str query, LexborNode node)
    cpdef list find_first(self, str query, LexborNode node)
    cpdef list _find(self, str query, LexborNode node, bint only_first)
    cpdef int any_matches(self, str query, LexborNode node) except -1

cdef class LexborHTMLParser:
    cdef lxb_html_document_t *document
    cdef lxb_dom_node_t *_fragment_wrapper
    cdef lxb_dom_node_t *_fragment_root
    cdef bint _is_fragment
    cdef lxb_tag_id_t _fragment_tag_id
    cdef lxb_ns_id_t _fragment_namespace_id
    cdef public bytes raw_html
    cdef LexborCSSSelector _selector
    cdef inline void _new_html_document(self)
    cdef inline lxb_status_t _parse_html_document(self, char *html, size_t html_len) nogil
    cdef inline lxb_status_t _parse_html_fragment(self, char *html, size_t html_len) nogil
    cdef int _parse_html(self, char *html, size_t html_len) except -1
    cdef object cached_script_texts
    cdef object cached_script_srcs

    @staticmethod
    cdef LexborHTMLParser from_document(lxb_html_document_t * document, bytes raw_html)

cdef extern from "lexbor/dom/dom.h" nogil:
    ctypedef enum lexbor_action_t:
        LEXBOR_ACTION_OK    = 0x00
        LEXBOR_ACTION_STOP  = 0x01
        LEXBOR_ACTION_NEXT  = 0x02

    ctypedef lexbor_action_t (*lxb_dom_node_simple_walker_f)(lxb_dom_node_t *node, void *ctx)

    ctypedef struct lxb_dom_character_data_t:
        lxb_dom_node_t node
        lexbor_str_t   data

    ctypedef struct lxb_dom_text_t:
        lxb_dom_character_data_t char_data

    ctypedef uintptr_t lxb_dom_attr_id_t
    ctypedef struct lxb_dom_collection_t:
        lexbor_array_t     array
        lxb_dom_document_t *document

    ctypedef struct lxb_dom_attr_t:
        lxb_dom_node_t     node

        lxb_dom_attr_id_t  upper_name
        lxb_dom_attr_id_t  qualified_name

        lexbor_str_t *value

        lxb_dom_element_t *owner

        lxb_dom_attr_t *next
        lxb_dom_attr_t *prev

    lxb_dom_collection_t * lxb_dom_collection_make(lxb_dom_document_t *document, size_t start_list_size)
    lxb_char_t * lxb_dom_node_text_content(lxb_dom_node_t *node, size_t *len)
    lxb_status_t lxb_dom_node_text_content_set(lxb_dom_node_t *node, const lxb_char_t *content, size_t len)
    bint lxb_dom_node_is_empty(lxb_dom_node_t *node)
    void lxb_dom_node_remove(lxb_dom_node_t *node)
    void * lxb_dom_document_destroy_text_noi(lxb_dom_document_t *document, lxb_char_t *text)
    lxb_dom_node_t * lxb_dom_document_root(lxb_dom_document_t *document)
    lxb_dom_element_t * lxb_dom_interface_element(lxb_dom_node_t *node)
    lxb_char_t * lxb_dom_element_qualified_name(lxb_dom_element_t *element, size_t *len)
    lxb_dom_node_t * lxb_dom_node_destroy(lxb_dom_node_t *node)
    lxb_dom_node_t * lxb_dom_node_destroy_deep(lxb_dom_node_t *root)
    lxb_dom_attr_t * lxb_dom_element_first_attribute_noi(lxb_dom_element_t *element)

    const lxb_char_t * lxb_dom_attr_local_name_noi(lxb_dom_attr_t *attr, size_t *len)
    const lxb_char_t * lxb_dom_attr_value_noi(lxb_dom_attr_t *attr, size_t *len)

    lxb_dom_attr_t * lxb_dom_element_set_attribute(lxb_dom_element_t *element,
                                                   const lxb_char_t *qualified_name, size_t qn_len,
                                                   const lxb_char_t *value, size_t value_len)
    lxb_status_t lxb_dom_element_remove_attribute(lxb_dom_element_t *element,
                                                  const lxb_char_t *qualified_name, size_t qn_len)
    lxb_dom_attr_t * lxb_dom_element_attr_by_name(lxb_dom_element_t *element,
                                                  const lxb_char_t *qualified_name, size_t length)
    lxb_tag_id_t lxb_dom_node_tag_id_noi(lxb_dom_node_t *node)
    lxb_dom_node_t * lxb_dom_document_import_node(lxb_dom_document_t *doc, lxb_dom_node_t *node, bint deep)
    void lxb_dom_node_insert_after(lxb_dom_node_t *to, lxb_dom_node_t *node)
    lxb_status_t lxb_dom_node_replace_all(lxb_dom_node_t *parent, lxb_dom_node_t *node)
    void lxb_dom_node_insert_child(lxb_dom_node_t *to, lxb_dom_node_t *node)
    void lxb_dom_node_insert_before(lxb_dom_node_t *to, lxb_dom_node_t *node)
    void lxb_dom_node_insert_after(lxb_dom_node_t *to, lxb_dom_node_t *node)
    lxb_dom_text_t * lxb_dom_document_create_text_node(lxb_dom_document_t *document, const lxb_char_t *data, size_t len)
    void lxb_dom_node_simple_walk(lxb_dom_node_t *root, lxb_dom_node_simple_walker_f walker_cb, void *ctx)
    lxb_dom_node_t* lxb_dom_node_clone(lxb_dom_node_t *node, bint deep)


cdef extern from "lexbor/dom/interfaces/element.h" nogil:
    lxb_status_t lxb_dom_elements_by_tag_name(lxb_dom_element_t *root, lxb_dom_collection_t *collection,
                                              const lxb_char_t *qualified_name, size_t len)


cdef extern from "lexbor/dom/interfaces/document.h" nogil:
    lxb_html_document_t * lxb_html_document_destroy(lxb_html_document_t *document)


cdef extern from "lexbor/dom/collection.h" nogil:
    size_t lxb_dom_collection_length_noi(lxb_dom_collection_t *col)

    lxb_dom_element_t * lxb_dom_collection_element_noi(lxb_dom_collection_t *col, size_t idx)
    lxb_dom_collection_t * lxb_dom_collection_destroy(lxb_dom_collection_t *col, bint self_destroy)


cdef extern from "lexbor/css/css.h" nogil:
    ctypedef struct lxb_css_parser_t:
        lxb_css_memory_t* memory
    ctypedef struct lxb_css_syntax_tokenizer_t
    ctypedef struct lxb_css_memory_t

    lxb_css_parser_t * lxb_css_parser_create()
    lxb_status_t lxb_css_parser_init(lxb_css_parser_t *parser, lxb_css_syntax_tokenizer_t *tkz)
    lxb_css_parser_t * lxb_css_parser_destroy(lxb_css_parser_t *parser, bint self_destroy)
    void lxb_css_parser_clean(lxb_css_parser_t *parser)
    lxb_css_memory_t * lxb_css_memory_destroy(lxb_css_memory_t *memory, bint self_destroy)
    void lxb_css_selector_list_destroy_memory(lxb_css_selector_list_t *list)


cdef extern from "lexbor/tag/tag.h" nogil:
    ctypedef struct lxb_tag_data_t:
        lxb_tag_id_t tag_id

    ctypedef enum lxb_tag_id_enum_t:
        LXB_TAG__UNDEF = 0x0000
        LXB_TAG__END_OF_FILE = 0x0001
        LXB_TAG__TEXT = 0x0002
        LXB_TAG__DOCUMENT = 0x0003
        LXB_TAG__EM_COMMENT = 0x0004
        LXB_TAG__EM_DOCTYPE = 0x0005
        LXB_TAG_A = 0x0006
        LXB_TAG_ABBR = 0x0007
        LXB_TAG_ACRONYM = 0x0008
        LXB_TAG_ADDRESS = 0x0009
        LXB_TAG_ALTGLYPH = 0x000a
        LXB_TAG_ALTGLYPHDEF = 0x000b
        LXB_TAG_ALTGLYPHITEM = 0x000c
        LXB_TAG_ANIMATECOLOR = 0x000d
        LXB_TAG_ANIMATEMOTION = 0x000e
        LXB_TAG_ANIMATETRANSFORM = 0x000f
        LXB_TAG_ANNOTATION_XML = 0x0010
        LXB_TAG_APPLET = 0x0011
        LXB_TAG_AREA = 0x0012
        LXB_TAG_ARTICLE = 0x0013
        LXB_TAG_ASIDE = 0x0014
        LXB_TAG_AUDIO = 0x0015
        LXB_TAG_B = 0x0016
        LXB_TAG_BASE = 0x0017
        LXB_TAG_BASEFONT = 0x0018
        LXB_TAG_BDI = 0x0019
        LXB_TAG_BDO = 0x001a
        LXB_TAG_BGSOUND = 0x001b
        LXB_TAG_BIG = 0x001c
        LXB_TAG_BLINK = 0x001d
        LXB_TAG_BLOCKQUOTE = 0x001e
        LXB_TAG_BODY = 0x001f
        LXB_TAG_BR = 0x0020
        LXB_TAG_BUTTON = 0x0021
        LXB_TAG_CANVAS = 0x0022
        LXB_TAG_CAPTION = 0x0023
        LXB_TAG_CENTER = 0x0024
        LXB_TAG_CITE = 0x0025
        LXB_TAG_CLIPPATH = 0x0026
        LXB_TAG_CODE = 0x0027
        LXB_TAG_COL = 0x0028
        LXB_TAG_COLGROUP = 0x0029
        LXB_TAG_DATA = 0x002a
        LXB_TAG_DATALIST = 0x002b
        LXB_TAG_DD = 0x002c
        LXB_TAG_DEL = 0x002d
        LXB_TAG_DESC = 0x002e
        LXB_TAG_DETAILS = 0x002f
        LXB_TAG_DFN = 0x0030
        LXB_TAG_DIALOG = 0x0031
        LXB_TAG_DIR = 0x0032
        LXB_TAG_DIV = 0x0033
        LXB_TAG_DL = 0x0034
        LXB_TAG_DT = 0x0035
        LXB_TAG_EM = 0x0036
        LXB_TAG_EMBED = 0x0037
        LXB_TAG_FEBLEND = 0x0038
        LXB_TAG_FECOLORMATRIX = 0x0039
        LXB_TAG_FECOMPONENTTRANSFER = 0x003a
        LXB_TAG_FECOMPOSITE = 0x003b
        LXB_TAG_FECONVOLVEMATRIX = 0x003c
        LXB_TAG_FEDIFFUSELIGHTING = 0x003d
        LXB_TAG_FEDISPLACEMENTMAP = 0x003e
        LXB_TAG_FEDISTANTLIGHT = 0x003f
        LXB_TAG_FEDROPSHADOW = 0x0040
        LXB_TAG_FEFLOOD = 0x0041
        LXB_TAG_FEFUNCA = 0x0042
        LXB_TAG_FEFUNCB = 0x0043
        LXB_TAG_FEFUNCG = 0x0044
        LXB_TAG_FEFUNCR = 0x0045
        LXB_TAG_FEGAUSSIANBLUR = 0x0046
        LXB_TAG_FEIMAGE = 0x0047
        LXB_TAG_FEMERGE = 0x0048
        LXB_TAG_FEMERGENODE = 0x0049
        LXB_TAG_FEMORPHOLOGY = 0x004a
        LXB_TAG_FEOFFSET = 0x004b
        LXB_TAG_FEPOINTLIGHT = 0x004c
        LXB_TAG_FESPECULARLIGHTING = 0x004d
        LXB_TAG_FESPOTLIGHT = 0x004e
        LXB_TAG_FETILE = 0x004f
        LXB_TAG_FETURBULENCE = 0x0050
        LXB_TAG_FIELDSET = 0x0051
        LXB_TAG_FIGCAPTION = 0x0052
        LXB_TAG_FIGURE = 0x0053
        LXB_TAG_FONT = 0x0054
        LXB_TAG_FOOTER = 0x0055
        LXB_TAG_FOREIGNOBJECT = 0x0056
        LXB_TAG_FORM = 0x0057
        LXB_TAG_FRAME = 0x0058
        LXB_TAG_FRAMESET = 0x0059
        LXB_TAG_GLYPHREF = 0x005a
        LXB_TAG_H1 = 0x005b
        LXB_TAG_H2 = 0x005c
        LXB_TAG_H3 = 0x005d
        LXB_TAG_H4 = 0x005e
        LXB_TAG_H5 = 0x005f
        LXB_TAG_H6 = 0x0060
        LXB_TAG_HEAD = 0x0061
        LXB_TAG_HEADER = 0x0062
        LXB_TAG_HGROUP = 0x0063
        LXB_TAG_HR = 0x0064
        LXB_TAG_HTML = 0x0065
        LXB_TAG_I = 0x0066
        LXB_TAG_IFRAME = 0x0067
        LXB_TAG_IMAGE = 0x0068
        LXB_TAG_IMG = 0x0069
        LXB_TAG_INPUT = 0x006a
        LXB_TAG_INS = 0x006b
        LXB_TAG_ISINDEX = 0x006c
        LXB_TAG_KBD = 0x006d
        LXB_TAG_KEYGEN = 0x006e
        LXB_TAG_LABEL = 0x006f
        LXB_TAG_LEGEND = 0x0070
        LXB_TAG_LI = 0x0071
        LXB_TAG_LINEARGRADIENT = 0x0072
        LXB_TAG_LINK = 0x0073
        LXB_TAG_LISTING = 0x0074
        LXB_TAG_MAIN = 0x0075
        LXB_TAG_MALIGNMARK = 0x0076
        LXB_TAG_MAP = 0x0077
        LXB_TAG_MARK = 0x0078
        LXB_TAG_MARQUEE = 0x0079
        LXB_TAG_MATH = 0x007a
        LXB_TAG_MENU = 0x007b
        LXB_TAG_META = 0x007c
        LXB_TAG_METER = 0x007d
        LXB_TAG_MFENCED = 0x007e
        LXB_TAG_MGLYPH = 0x007f
        LXB_TAG_MI = 0x0080
        LXB_TAG_MN = 0x0081
        LXB_TAG_MO = 0x0082
        LXB_TAG_MS = 0x0083
        LXB_TAG_MTEXT = 0x0084
        LXB_TAG_MULTICOL = 0x0085
        LXB_TAG_NAV = 0x0086
        LXB_TAG_NEXTID = 0x0087
        LXB_TAG_NOBR = 0x0088
        LXB_TAG_NOEMBED = 0x0089
        LXB_TAG_NOFRAMES = 0x008a
        LXB_TAG_NOSCRIPT = 0x008b
        LXB_TAG_OBJECT = 0x008c
        LXB_TAG_OL = 0x008d
        LXB_TAG_OPTGROUP = 0x008e
        LXB_TAG_OPTION = 0x008f
        LXB_TAG_OUTPUT = 0x0090
        LXB_TAG_P = 0x0091
        LXB_TAG_PARAM = 0x0092
        LXB_TAG_PATH = 0x0093
        LXB_TAG_PICTURE = 0x0094
        LXB_TAG_PLAINTEXT = 0x0095
        LXB_TAG_PRE = 0x0096
        LXB_TAG_PROGRESS = 0x0097
        LXB_TAG_Q = 0x0098
        LXB_TAG_RADIALGRADIENT = 0x0099
        LXB_TAG_RB = 0x009a
        LXB_TAG_RP = 0x009b
        LXB_TAG_RT = 0x009c
        LXB_TAG_RTC = 0x009d
        LXB_TAG_RUBY = 0x009e
        LXB_TAG_S = 0x009f
        LXB_TAG_SAMP = 0x00a0
        LXB_TAG_SCRIPT = 0x00a1
        LXB_TAG_SECTION = 0x00a2
        LXB_TAG_SELECT = 0x00a3
        LXB_TAG_SLOT = 0x00a4
        LXB_TAG_SMALL = 0x00a5
        LXB_TAG_SOURCE = 0x00a6
        LXB_TAG_SPACER = 0x00a7
        LXB_TAG_SPAN = 0x00a8
        LXB_TAG_STRIKE = 0x00a9
        LXB_TAG_STRONG = 0x00aa
        LXB_TAG_STYLE = 0x00ab
        LXB_TAG_SUB = 0x00ac
        LXB_TAG_SUMMARY = 0x00ad
        LXB_TAG_SUP = 0x00ae
        LXB_TAG_SVG = 0x00af
        LXB_TAG_TABLE = 0x00b0
        LXB_TAG_TBODY = 0x00b1
        LXB_TAG_TD = 0x00b2
        LXB_TAG_TEMPLATE = 0x00b3
        LXB_TAG_TEXTAREA = 0x00b4
        LXB_TAG_TEXTPATH = 0x00b5
        LXB_TAG_TFOOT = 0x00b6
        LXB_TAG_TH = 0x00b7
        LXB_TAG_THEAD = 0x00b8
        LXB_TAG_TIME = 0x00b9
        LXB_TAG_TITLE = 0x00ba
        LXB_TAG_TR = 0x00bb
        LXB_TAG_TRACK = 0x00bc
        LXB_TAG_TT = 0x00bd
        LXB_TAG_U = 0x00be
        LXB_TAG_UL = 0x00bf
        LXB_TAG_VAR = 0x00c0
        LXB_TAG_VIDEO = 0x00c1
        LXB_TAG_WBR = 0x00c2
        LXB_TAG_XMP = 0x00c3
        LXB_TAG__LAST_ENTRY = 0x00c4

    lxb_tag_id_t lxb_tag_id_by_name_noi(lexbor_hash_t *hash,
                                        const lxb_char_t *name,
                                        size_t len)


cdef extern from "lexbor/ns/ns.h" nogil:
    ctypedef struct lxb_ns_data_t:
        lxb_ns_id_t ns_id

    ctypedef struct lxb_ns_prefix_data_t:
        uintptr_t prefix_id

    ctypedef enum lxb_ns_id_enum_t:
        LXB_NS__UNDEF = 0x00
        LXB_NS__ANY = 0x01
        LXB_NS_HTML = 0x02
        LXB_NS_MATH = 0x03
        LXB_NS_SVG = 0x04
        LXB_NS_XLINK = 0x05
        LXB_NS_XML = 0x06
        LXB_NS_XMLNS = 0x07
        LXB_NS__LAST_ENTRY = 0x08

    const lxb_ns_data_t * lxb_ns_data_by_link(lexbor_hash_t *hash,
                                              const lxb_char_t *name,
                                              size_t length)
    const lxb_ns_prefix_data_t * lxb_ns_prefix_data_by_name(lexbor_hash_t *hash,
                                                            const lxb_char_t *name,
                                                            size_t length)


cdef extern from "lexbor/selectors/selectors.h" nogil:
    ctypedef struct lxb_css_selectors_t

    ctypedef struct lxb_selectors_t
    ctypedef struct lxb_css_selector_list_t
    ctypedef struct lxb_css_selector_specificity_t
    ctypedef lxb_status_t (*lxb_selectors_cb_f)(lxb_dom_node_t *node, lxb_css_selector_specificity_t *spec, void *ctx)
    ctypedef enum lxb_selectors_opt_t:
        LXB_SELECTORS_OPT_DEFAULT = 0x00
        LXB_SELECTORS_OPT_MATCH_ROOT = 1 << 1
        LXB_SELECTORS_OPT_MATCH_FIRST = 1 << 2

    void lxb_selectors_opt_set(lxb_selectors_t *selectors, lxb_selectors_opt_t opt)
    lxb_css_selectors_t * lxb_css_selectors_create()
    lxb_status_t lxb_css_selectors_init(lxb_css_selectors_t *selectors)
    void lxb_css_parser_selectors_set(lxb_css_parser_t *parser, lxb_css_selectors_t *selectors)
    lxb_css_selector_list_t * lxb_css_selectors_parse(lxb_css_parser_t *parser, const lxb_char_t *data, size_t length)
    lxb_css_selectors_t * lxb_css_selectors_destroy(lxb_css_selectors_t *selectors, bint self_destroy)

    lxb_selectors_t * lxb_selectors_create()
    lxb_status_t lxb_selectors_init(lxb_selectors_t *selectors)
    lxb_selectors_t * lxb_selectors_destroy(lxb_selectors_t *selectors, bint self_destroy)
    lxb_status_t lxb_selectors_find(lxb_selectors_t *selectors, lxb_dom_node_t *root,
                                    lxb_css_selector_list_t *list, lxb_selectors_cb_f cb, void *ctx)

```

### `selectolax/lexbor.pyi`

```pyi
from __future__ import annotations

from typing import Any, Iterator, Literal, NoReturn, Optional, TypeVar, overload

DefaultT = TypeVar("DefaultT")

class LexborAttributes:
    """A dict-like object that represents attributes."""

    @staticmethod
    def create(node: LexborAttributes) -> LexborAttributes: ...
    def keys(self) -> Iterator[str]: ...
    def items(self) -> Iterator[tuple[str, str | None]]: ...
    def values(self) -> Iterator[str | None]: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str) -> str | None: ...
    def __setitem__(self, key: str, value: Optional[str]) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __repr__(self) -> str: ...
    @overload
    def get(self, key: str, default: DefaultT) -> DefaultT | str | None: ...
    @overload
    def get(self, key: str, default: None = ...) -> str | None: ...
    @overload
    def sget(self, key: str, default: str | DefaultT) -> str | DefaultT: ...
    @overload
    def sget(self, key: str, default: str = "") -> str: ...

class LexborSelector:
    """An advanced CSS selector that supports additional operations.

    Think of it as a toolkit that mimics some of the features of XPath.

    Please note, this is an experimental feature that can change in the future.
    """

    def __init__(self, node: LexborNode, query: str): ...
    def css(self, query: str) -> NoReturn: ...
    @property
    def matches(self) -> list[LexborNode]:
        """Returns all possible matches"""
        ...

    @property
    def any_matches(self) -> bool:
        """Returns True if there are any matches"""
        ...

    def text_contains(
        self, text: str, deep: bool = True, separator: str = "", strip: bool = False
    ) -> LexborSelector:
        """Filter all current matches given text."""
        ...

    def any_text_contains(
        self, text: str, deep: bool = True, separator: str = "", strip: bool = False
    ) -> bool:
        """Returns True if any node in the current search scope contains specified text"""
        ...

    def attribute_longer_than(
        self, attribute: str, length: int, start: str | None = None
    ) -> LexborSelector:
        """Filter all current matches by attribute length.

        Similar to string-length in XPath.
        """
        ...

    def any_attribute_longer_than(
        self, attribute: str, length: int, start: str | None = None
    ) -> bool:
        """Returns True any href attribute longer than a specified length.

        Similar to string-length in XPath.
        """
        ...

    @property
    def inner_html(self) -> str | None:
        """Return HTML representation of the child nodes.

        Works similar to innerHTML in JavaScript.
        Unlike the `.html` property, does not include the current node.
        Can be used to set HTML as well. See the setter docstring.

        Returns
        -------
        text : str or None
        """
        ...

    @inner_html.setter
    def inner_html(self, html: str):
        """Set inner HTML to the specified HTML.

        Replaces existing data inside the node.
        Works similar to innerHTML in JavaScript.

        Parameters
        ----------
        html : str

        """
        ...

class LexborCSSSelector:
    def __init__(self): ...
    def find(self, query: str, node: LexborNode) -> list[LexborNode]: ...
    def any_matches(self, query: str, node: LexborNode) -> bool: ...

class LexborNode:
    """A class that represents HTML node (element)."""

    parser: LexborHTMLParser

    @property
    def mem_id(self) -> int: ...
    @property
    def child(self) -> LexborNode | None:
        """Alias for the `first_child` property.

        **Deprecated**. Please use `first_child` instead.
        """
        ...

    @property
    def first_child(self) -> LexborNode | None:
        """Return the first child node."""
        ...

    @property
    def parent(self) -> LexborNode | None:
        """Return the parent node."""
        ...

    @property
    def next(self) -> LexborNode | None:
        """Return next node."""
        ...

    @property
    def prev(self) -> LexborNode | None:
        """Return previous node."""
        ...

    @property
    def last_child(self) -> LexborNode | None:
        """Return last child node."""
        ...

    @property
    def html(self) -> str | None:
        """Return HTML representation of the current node including all its child nodes.

        Returns
        -------
        text : str
        """
        ...

    def html_pretty(
        self,
        indent: int = 0,
        skip_ws_nodes: bool = False,
        skip_comment: bool = False,
        raw: bool = False,
        without_closing: bool = False,
        tag_with_ns: bool = False,
        without_text_indent: bool = False,
        full_doctype: bool = False,
        html5test: bool = False,
    ) -> str | None:
        """Return pretty-printed HTML for the current node.

        Parameters
        ----------
        indent : int, optional
            Initial indentation level passed to Lexbor. Defaults to ``0``.
        skip_ws_nodes : bool, optional
            Skip text nodes that contain only whitespace.
        skip_comment : bool, optional
            Exclude HTML comment nodes from the serialized output.
        raw : bool, optional
            Serialize text and attribute values without HTML escaping.
        without_closing : bool, optional
            Omit closing tags for non-void elements.
        tag_with_ns : bool, optional
            Include namespace prefixes in serialized tag names when available.
        without_text_indent : bool, optional
            Disable extra indentation added around text and comment content.
        full_doctype : bool, optional
            Serialize the full document type declaration when a doctype node is present.
        html5test : bool, optional
            Serialize using Lexbor's HTML5 test formatting mode.
        """
        ...

    def __hash__(self) -> int: ...
    def text_lexbor(self) -> str:
        """Returns the text of the node including text of all its child nodes.

        Uses builtin method from lexbor.
        """
        ...

    def text(
        self,
        deep: bool = True,
        separator: str = "",
        strip: bool = False,
        skip_empty: bool = False,
    ) -> str:
        """Return concatenated text from this node.

        Parameters
        ----------
        deep : bool, optional
            When ``True`` (default), include text from all descendant nodes; when
            ``False``, only include direct children.
        separator : str, optional
            String inserted between successive text fragments.
        strip : bool, optional
            If ``True``, apply ``str.strip()`` to each fragment before joining to
            remove surrounding whitespace. Defaults to ``False``.
        skip_empty : bool, optional
            Exclude text nodes whose content is only ASCII whitespace (space,
            tab, newline, form feed or carriage return) when ``True``.
            Defaults to ``False``.

        Returns
        -------
        text : str
            Combined textual content assembled according to the provided options.
        """
        ...

    def css(self, query: str) -> list[LexborNode]:
        """Evaluate CSS selector against current node and its child nodes.

        Matches pattern `query` against HTML tree.
        `CSS selectors reference <https://www.w3schools.com/cssref/css_selectors.asp>`_.

        Special selectors:

         - parser.css('p:lexbor-contains("awesome" i)') -- case-insensitive contains
         - parser.css('p:lexbor-contains("awesome")') -- case-sensitive contains


        Parameters
        ----------
        query : str
            CSS selector (e.g. "div > :nth-child(2n+1):not(:has(a))").

        Returns
        -------
        selector : list of `Node` objects
        """
        ...

    @overload
    def css_first(
        self, query: str, default: Any = ..., strict: Literal[True] = ...
    ) -> LexborNode:
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : bool, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `LexborNode` object
        """
        ...

    @overload
    def css_first(
        self, query: str, default: DefaultT, strict: bool = False
    ) -> LexborNode | DefaultT:
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : bool, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `LexborNode` object
        """
        ...

    @overload
    def css_first(
        self, query: str, default: None = ..., strict: bool = False
    ) -> LexborNode | None:
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : bool, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `LexborNode` object
        """
        ...

    def any_css_matches(self, selectors: tuple[str]) -> bool:
        """Returns True if any of CSS selectors matches a node"""
        ...

    def css_matches(self, selector: str) -> bool:
        """Returns True if CSS selector matches a node."""
        ...

    @property
    def tag_id(self) -> int: ...
    @property
    def tag(self) -> str | None:
        """Return the name of the current tag (e.g. div, p, img).

        For for non-tag nodes, returns the following names:

         * `-text` - text node
         * `-document` - document node
         * `-comment` - comment node

        Returns
        -------
        text : str
        """
        ...

    def decompose(self, recursive: bool = True) -> None:
        """Remove the current node from the tree.

        Parameters
        ----------
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = LexborHTMLParser(html)
        >>> for tag in tree.css('script'):
        >>>     tag.decompose()
        """
        ...

    def strip_tags(self, tags: list[str], recursive: bool = False) -> None:
        """Remove specified tags from the HTML tree.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = LexborHTMLParser('<html><head></head><body><script></script><div>Hello world!</div></body></html>')
        >>> tags = ['head', 'style', 'script', 'xmp', 'iframe', 'noembed', 'noframes']
        >>> tree.strip_tags(tags)
        >>> tree.html
        '<html><body><div>Hello world!</div></body></html>'
        """
        ...

    @property
    def attributes(self) -> dict[str, str | None]:
        """Get all attributes that belong to the current node.

        The value of empty attributes is None.

        Returns
        -------
        attributes : dictionary of all attributes.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div data id='my_id'></div>")
        >>> node = tree.css_first('div')
        >>> node.attributes
        {'data': None, 'id': 'my_id'}
        """
        ...

    @property
    def attrs(self) -> LexborAttributes:
        """A dict-like object that is similar to the ``attributes`` property, but operates directly on the Node data.

        .. warning:: Use ``attributes`` instead, if you don't want to modify Node attributes.

        Returns
        -------
        attributes : Attributes mapping object.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div id='a'></div>")
        >>> node = tree.css_first('div')
        >>> node.attrs
        <div attributes, 1 items>
        >>> node.attrs['id']
        'a'
        >>> node.attrs['foo'] = 'bar'
        >>> del node.attrs['id']
        >>> node.attributes
        {'foo': 'bar'}
        >>> node.attrs['id'] = 'new_id'
        >>> node.html
        '<div foo="bar" id="new_id"></div>'
        """
        ...

    @property
    def id(self) -> str | None:
        """Get the id attribute of the node.

        Returns None if id does not set.

        Returns
        -------
        text : str
        """
        ...

    def iter(
        self, include_text: bool = False, skip_empty: bool = False
    ) -> Iterator[LexborNode]:
        """Iterate over direct children of this node.

        Parameters
        ----------
        include_text : bool, optional
            When ``True``, yield text nodes in addition to element nodes. Defaults
            to ``False``.
        skip_empty : bool, optional
            When ``include_text`` is ``True``, ignore text nodes made up solely
            of ASCII whitespace (space, tab, newline, form feed or carriage
            return). Defaults to ``False``.

        Yields
        ------
        LexborNode
            Child nodes on the same tree level as this node, filtered according
            to the provided options.
        """
        ...

    def unwrap(self, delete_empty: bool = False) -> None:
        """Replace node with whatever is inside this node.

        Does nothing if you perform unwrapping second time on the same node.

        Parameters
        ----------
        delete_empty : bool, default False
            If True, removes empty tags.

        Examples
        --------

        >>>  tree = LexborHTMLParser("<div>Hello <i>world</i>!</div>")
        >>>  tree.css_first('i').unwrap()
        >>>  tree.html
        '<html><head></head><body><div>Hello world!</div></body></html>'

        Note: by default, empty tags are ignored, use "delete_empty" to change this.
        """
        ...

    def unwrap_tags(self, tags: list[str], delete_empty: bool = False) -> None:
        """Unwraps specified tags from the HTML tree.

        Works the same as the ``unwrap`` method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool, default False
            If True, removes empty tags.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.body.unwrap_tags(['i','a'])
        >>> tree.body.html
        '<body><div>Hello world!</div></body>'

        Note: by default, empty tags are ignored, use "delete_empty" to change this.
        """
        ...

    def merge_text_nodes(self) -> None:
        """Iterates over all text nodes and merges all text nodes that are close to each other.

        This is useful for text extraction.
        Use it when you need to strip HTML tags and merge "dangling" text.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div><p><strong>J</strong>ohn</p><p>Doe</p></div>")
        >>> node = tree.css_first('div')
        >>> tree.unwrap_tags(["strong"])
        >>> tree.text(deep=True, separator=" ", strip=True)
        "J ohn Doe" # Text extraction produces an extra space because the strong tag was removed.
        >>> node.merge_text_nodes()
        >>> tree.text(deep=True, separator=" ", strip=True)
        "John Doe"
        """
        ...

    def traverse(
        self, include_text: bool = False, skip_empty: bool = False
    ) -> Iterator[LexborNode]:
        """Depth-first traversal starting at the current node.

        Parameters
        ----------
        include_text : bool, optional
            When ``True``, include text nodes in the traversal sequence. Defaults
            to ``False``.
        skip_empty : bool, optional
            Skip text nodes that contain only ASCII whitespace (space, tab,
            newline, form feed or carriage return) when ``include_text`` is
            ``True``. Defaults to ``False``.

        Yields
        ------
        LexborNode
            Nodes encountered in depth-first order beginning with the current
            node, filtered according to the provided options.
        """
        ...

    def replace_with(self, value: bytes | str | LexborNode) -> None:
        """Replace current Node with specified value.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to replace the Node with.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = LexborHTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.replace_with(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get Laptop</div>'

        >>> html_parser = LexborHTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = LexborHTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.replace_with(html_parser2.body.child)
        '<div>Get <span alt="Laptop"><div>Test</div> <div></div></span></div>'
        """
        ...

    def insert_before(self, value: bytes | str | LexborNode) -> None:
        """Insert a node before the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert before the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = LexborHTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.insert_before(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get Laptop<img src="" alt="Laptop"></div>'

        >>> html_parser = LexborHTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = LexborHTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.insert_before(html_parser2.body.child)
        <div>Get <span alt="Laptop"><div>Test</div><img src="/jpg"> <div></div></span></div>'
        """
        ...

    def insert_after(self, value: bytes | str | LexborNode) -> None:
        """Insert a node after the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert after the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = LexborHTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.insert_after(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get <img src="" alt="Laptop">Laptop</div>'

        >>> html_parser = LexborHTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = LexborHTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.insert_after(html_parser2.body.child)
        <div>Get <span alt="Laptop"><img src="/jpg"><div>Test</div> <div></div></span></div>'
        """
        ...

    def insert_child(self, value: bytes | str | LexborNode) -> None:
        """Insert a node inside (at the end of) the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert inside the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = LexborHTMLParser('<div>Get <img src=""></div>')
        >>> div = tree.css_first('div')
        >>> div.insert_child('Laptop')
        >>> tree.body.child.html
        '<div>Get <img src="">Laptop</div>'

        >>> html_parser = LexborHTMLParser('<div>Get <span alt="Laptop"> <div>Laptop</div> </span></div>')
        >>> html_parser2 = LexborHTMLParser('<div>Test</div>')
        >>> span_node = html_parser.css_first('span')
        >>> span_node.insert_child(html_parser2.body.child)
        <div>Get <span alt="Laptop"> <div>Laptop</div> <div>Test</div> </span></div>'
        """
        ...

    @property
    def raw_value(self) -> NoReturn:
        """Return the raw (unparsed, original) value of a node.

        Currently, works on text nodes only.

        Returns
        -------

        raw_value : bytes

        Examples
        --------

        >>> html_parser = LexborHTMLParser('<div>&#x3C;test&#x3E;</div>')
        >>> selector = html_parser.css_first('div')
        >>> selector.child.html
        '&lt;test&gt;'
        >>> selector.child.raw_value
        b'&#x3C;test&#x3E;'
        """
        ...

    def scripts_contain(self, query: str) -> bool:
        """Returns True if any of the script tags contain specified text.

        Caches script tags on the first call to improve performance.

        Parameters
        ----------
        query : str
            The query to check.
        """
        ...

    def script_srcs_contain(self, queries: tuple[str]) -> bool:
        """Returns True if any of the script SRCs attributes contain on of the specified text.

        Caches values on the first call to improve performance.

        Parameters
        ----------
        queries : tuple of str
        """
        ...

    def remove(self, recursive: bool = True) -> None:
        """An alias for the decompose method."""
        ...

    def select(self, query: str | None = None) -> LexborSelector:
        """Select nodes given a CSS selector.

        Works similarly to the the ``css`` method, but supports chained filtering and extra features.

        Parameters
        ----------
        query : str or None
            The CSS selector to use when searching for nodes.

        Returns
        -------
        selector : The `Selector` class.
        """
        ...

    @property
    def text_content(self) -> str | None:
        """Returns the text of the node if it is a text node.

        Returns None for other nodes.
        Unlike the ``text`` method, does not include child nodes.

        Returns
        -------
        text : str or None.
        """
        ...

    @property
    def comment_content(self) -> str | None:
        """Extract the textual content of an HTML comment node.

        Returns
        -------
        str or None
            Comment text with surrounding whitespace removed, or ``None`` if
            the current node is not a comment or the comment markup cannot be
            parsed.

        Examples
        --------
        >>> parse_fragment("<!-- hello -->")[0].comment_content
        'hello'
        >>> parse_fragment("<div>not a comment</div>")[0].comment_content is None
        True
        """
        ...

    @property
    def inner_html(self) -> str | None:
        """Return HTML representation of the child nodes.

        Works similar to innerHTML in JavaScript.
        Unlike the `.html` property, does not include the current node.
        Can be used to set HTML as well. See the setter docstring.

        Returns
        -------
        text : str or None
        """
        ...

    @inner_html.setter
    def inner_html(self, html: str):
        """Set inner HTML to the specified HTML.

        Replaces existing data inside the node.
        Works similar to innerHTML in JavaScript.

        Parameters
        ----------
        html : str

        """
        ...

    def inner_html_pretty(
        self,
        indent: int = 0,
        skip_ws_nodes: bool = False,
        skip_comment: bool = False,
        raw: bool = False,
        without_closing: bool = False,
        tag_with_ns: bool = False,
        without_text_indent: bool = False,
        full_doctype: bool = False,
        html5test: bool = False,
    ) -> str | None:
        """Return pretty-printed HTML representation of the child nodes.

        Parameters
        ----------
        indent : int, optional
            Initial indentation level passed to Lexbor. Defaults to ``0``.
        skip_ws_nodes : bool, optional
            Skip text nodes that contain only whitespace.
        skip_comment : bool, optional
            Exclude HTML comment nodes from the serialized output.
        raw : bool, optional
            Serialize text and attribute values without HTML escaping.
        without_closing : bool, optional
            Omit closing tags for non-void elements.
        tag_with_ns : bool, optional
            Include namespace prefixes in serialized tag names when available.
        without_text_indent : bool, optional
            Disable extra indentation added around text and comment content.
        full_doctype : bool, optional
            Serialize the full document type declaration when a doctype node is present.
        html5test : bool, optional
            Serialize using Lexbor's HTML5 test formatting mode.
        """
        ...

    def clone(self) -> LexborNode:
        """Clone the current node.

        You can it use to do temporary modifications without affecting the original HTML tree.

        It is tied to the current parser instance.
        Gets destroyed when parser instance is destroyed.
        """
        ...

    @property
    def is_element_node(self) -> bool:
        """Return True if the node represents an element node."""
        ...

    @property
    def is_text_node(self) -> bool:
        """Return True if the node represents a text node."""
        ...

    @property
    def is_comment_node(self) -> bool:
        """Return True if the node represents a comment node."""
        ...

    @property
    def is_document_node(self) -> bool:
        """Return True if the node represents a document node."""
        ...

    @property
    def is_empty_text_node(self) -> bool:
        """Check whether the current node is an empty text node.

        Returns
        -------
        bool
            ``True`` when the node is a text node whose data consists solely of
            ASCII whitespace characters (space, tab, newline, form feed or
            carriage return).
        """
        ...

class LexborHTMLParser:
    """The lexbor HTML parser.

    Use this class to parse raw HTML.

    This parser mimics most of the stuff from ``HTMLParser`` but not inherits it directly.

    Parameters
    ----------

    html : str (unicode) or bytes
    """

    raw_html: bytes

    def __init__(
        self,
        html: str | bytes,
        is_fragment: bool = False,
        fragment_tag: str = "div",
        fragment_namespace: str = "html",
    ) -> None:
        """Create a parser and load HTML.

        Parameters
        ----------
        html : str or bytes
            HTML content to parse.
        is_fragment : bool, optional
            When ``False`` (default), the input is parsed as a full HTML document.
            If the input is only a fragment, the parser still accepts it and inserts any missing required elements,
            (such as `<html>`, `<head>`, and `<body>`) into the tree,
            according to the HTML parsing rules in the HTML Standard.
            This matches how browsers construct the DOM when they load an HTML page.

            When ``True``, the input is parsed as an HTML fragment.
            The parser does not insert any missing required HTML elements.
            Behaves the same way as `DocumentFragment` in browsers.
            When `<html>`, `<head>` or `<body>` are present, ignores them entirely.
            As per the HTML Standard.
        fragment_tag : str, optional
            Context element tag used for fragment parsing. Defaults to ``"div"``.
            Only used when ``is_fragment`` is ``True``.
        fragment_namespace : str, optional
            Context element namespace used for fragment parsing. Defaults to ``"html"``.
            Accepts Lexbor namespace names such as ``"html"``, ``"svg"``, and ``"math"``,
            or a namespace URI recognized by Lexbor. Only used when ``is_fragment`` is ``True``.

        """
        ...

    def __repr__(self) -> str:
        """Return a concise representation of the parsed document.

        Returns
        -------
        str
            A string showing the number of characters in the parsed HTML.
        """
        ...

    @property
    def selector(self) -> LexborCSSSelector:
        """Return a lazily created CSS selector helper.

        Returns
        -------
        LexborCSSSelector
            Selector instance bound to this parser.
        """
        ...

    @property
    def root(self) -> LexborNode | None:
        """Return the document root node.

        Returns
        -------
        LexborNode or None
            Root of the parsed document, or ``None`` if unavailable.
        """
        ...

    @property
    def body(self) -> LexborNode | None:
        """Return document body.

        Returns
        -------
        LexborNode or None
            ``<body>`` element when present, otherwise ``None``.
        """
        ...

    @property
    def head(self) -> LexborNode | None:
        """Return document head.

        Returns
        -------
        LexborNode or None
            ``<head>`` element when present, otherwise ``None``.
        """
        ...

    def tags(self, name: str) -> list[LexborNode]:
        """Return all tags that match the provided name.

        Parameters
        ----------
        name : str
            Tag name to search for (e.g., ``"div"``).

        Returns
        -------
        list of LexborNode
            Matching elements in document order.

        Raises
        ------
        ValueError
            If ``name`` is empty or longer than 100 characters.
        SelectolaxError
            If Lexbor cannot locate the elements.
        """
        ...

    def text(
        self,
        deep: bool = True,
        separator: str = "",
        strip: bool = False,
        skip_empty: bool = False,
    ) -> str:
        """Returns the text of the node including text of all its child nodes.

        Parameters
        ----------
        strip : bool, default False
            If true, calls ``str.strip()`` on each text part to remove extra white spaces.
        separator : str, default ''
            The separator to use when joining text from different nodes.
        deep : bool, default True
            If True, includes text from all child nodes.
        skip_empty : bool, optional
            Exclude text nodes whose content is only ASCII whitespace (space,
            tab, newline, form feed or carriage return) when ``True``.
            Defaults to ``False``.

        Returns
        -------
        text : str
            Combined textual content assembled according to the provided options.
        """
        ...

    @property
    def html(self) -> str | None:
        """Return HTML representation of the page.

        Returns
        -------
        str or None
            Serialized HTML of the current document.
        """
        ...

    def html_pretty(
        self,
        indent: int = 0,
        skip_ws_nodes: bool = False,
        skip_comment: bool = False,
        raw: bool = False,
        without_closing: bool = False,
        tag_with_ns: bool = False,
        without_text_indent: bool = False,
        full_doctype: bool = False,
        html5test: bool = False,
    ) -> str | None:
        """Return pretty-printed HTML representation of the page.

        Parameters
        ----------
        indent : int, optional
            Initial indentation level passed to Lexbor. Defaults to ``0``.
        skip_ws_nodes : bool, optional
            Skip text nodes that contain only whitespace.
        skip_comment : bool, optional
            Exclude HTML comment nodes from the serialized output.
        raw : bool, optional
            Serialize text and attribute values without HTML escaping.
        without_closing : bool, optional
            Omit closing tags for non-void elements.
        tag_with_ns : bool, optional
            Include namespace prefixes in serialized tag names when available.
        without_text_indent : bool, optional
            Disable extra indentation added around text and comment content.
        full_doctype : bool, optional
            Serialize the full document type declaration when a doctype node is present.
        html5test : bool, optional
            Serialize using Lexbor's HTML5 test formatting mode.
        """
        ...

    def css(self, query: str) -> list[LexborNode]:
        """A CSS selector.

        Matches pattern `query` against HTML tree.
        `CSS selectors reference <https://www.w3schools.com/cssref/css_selectors.asp>`_.

        Special selectors:

         - parser.css('p:lexbor-contains("awesome" i)') -- case-insensitive contains
         - parser.css('p:lexbor-contains("awesome")') -- case-sensitive contains

        Parameters
        ----------
        query : str
            CSS selector (e.g. "div > :nth-child(2n+1):not(:has(a))").

        Returns
        -------
        selector : list of `Node` objects
        """
        ...

    @overload
    def css_first(
        self, query: str, default: Any = ..., strict: Literal[True] = ...
    ) -> LexborNode:
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : Any, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `LexborNode` object
        """
        ...

    @overload
    def css_first(
        self, query: str, default: DefaultT, strict: bool = False
    ) -> LexborNode | DefaultT:
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : Any, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `LexborNode` object
        """
        ...

    @overload
    def css_first(
        self, query: str, default: None = ..., strict: bool = False
    ) -> LexborNode | None:
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : Any, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `LexborNode` object
        """
        ...

    def strip_tags(self, tags: list[str], recursive: bool = False) -> None:
        """Remove specified tags from the node.

        Parameters
        ----------
        tags : list of str
            List of tags to remove.
        recursive : bool, default False
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = LexborHTMLParser('<html><head></head><body><script></script><div>Hello world!</div></body></html>')
        >>> tags = ['head', 'style', 'script', 'xmp', 'iframe', 'noembed', 'noframes']
        >>> tree.strip_tags(tags)
        >>> tree.html
        '<html><body><div>Hello world!</div></body></html>'

        Returns
        -------
        None
        """
        ...

    def select(self, query: str | None = None) -> LexborSelector | None:
        """Select nodes given a CSS selector.

        Works similarly to the ``css`` method, but supports chained filtering and extra features.

        Parameters
        ----------
        query : str or None
            The CSS selector to use when searching for nodes.

        Returns
        -------
        LexborSelector or None
            Selector bound to the root node, or ``None`` if the document is empty.
        """
        ...

    def any_css_matches(self, selectors: tuple[str]) -> bool:
        """Return ``True`` if any of the specified CSS selectors match.

        Parameters
        ----------
        selectors : tuple[str]
            CSS selectors to evaluate.

        Returns
        -------
        bool
            ``True`` when at least one selector matches.
        """
        ...

    def scripts_contain(self, query: str) -> bool:
        """Return ``True`` if any script tag contains the given text.

        Caches script tags on the first call to improve performance.

        Parameters
        ----------
        query : str
            Text to search for within script contents.

        Returns
        -------
        bool
            ``True`` when a matching script tag is found.
        """
        ...

    def script_srcs_contain(self, queries: tuple[str]) -> bool:
        """Return ``True`` if any script ``src`` contains one of the strings.

        Caches values on the first call to improve performance.

        Parameters
        ----------
        queries : tuple of str
            Strings to look for inside ``src`` attributes.

        Returns
        -------
        bool
            ``True`` when a matching source value is found.
        """
        ...

    def css_matches(self, selector: str) -> bool:
        """Return ``True`` if the document matches the selector at least once.

        Parameters
        ----------
        selector : str
            CSS selector to test.

        Returns
        -------
        bool
            ``True`` when a match exists.
        """
        ...

    def merge_text_nodes(self) -> None:
        """Iterates over all text nodes and merges all text nodes that are close to each other.

        This is useful for text extraction.
        Use it when you need to strip HTML tags and merge "dangling" text.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div><p><strong>J</strong>ohn</p><p>Doe</p></div>")
        >>> node = tree.css_first('div')
        >>> tree.unwrap_tags(["strong"])
        >>> tree.text(deep=True, separator=" ", strip=True)
        "J ohn Doe" # Text extraction produces an extra space because the strong tag was removed.
        >>> node.merge_text_nodes()
        >>> tree.text(deep=True, separator=" ", strip=True)
        "John Doe"

        Returns
        -------
        None
        """
        ...

    def clone(self) -> LexborHTMLParser:
        """Clone the current document tree.

        You can use it to do temporary modifications without affecting the original HTML tree.
        It is tied to the current parser instance.
        Gets destroyed when the parser instance is destroyed.

        Returns
        -------
        LexborHTMLParser
            A parser instance backed by a deep-copied document.
        """
        ...

    def unwrap_tags(self, tags: list[str], delete_empty: bool = False) -> None:
        """Unwraps specified tags from the HTML tree.

        Works the same as the ``unwrap`` method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool
            Whenever to delete empty tags.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.body.unwrap_tags(['i','a'])
        >>> tree.body.html
        '<body><div>Hello world!</div></body>'

        Returns
        -------
        None
        """
        ...

    @property
    def inner_html(self) -> str:
        """Return HTML representation of the child nodes.

        Works similar to innerHTML in JavaScript.
        Unlike the `.html` property, does not include the current node.
        Can be used to set HTML as well. See the setter docstring.

        Returns
        -------
        text : str | None
        """
        ...

    @inner_html.setter
    def inner_html(self, html: str) -> None:
        """Set inner HTML to the specified HTML.

        Replaces existing data inside the node.
        Works similar to innerHTML in JavaScript.

        Parameters
        ----------
        html : str

        Returns
        -------
        None
        """
        ...

    def inner_html_pretty(
        self,
        indent: int = 0,
        skip_ws_nodes: bool = False,
        skip_comment: bool = False,
        raw: bool = False,
        without_closing: bool = False,
        tag_with_ns: bool = False,
        without_text_indent: bool = False,
        full_doctype: bool = False,
        html5test: bool = False,
    ) -> str | None:
        """Return pretty-printed HTML representation of the child nodes.

        Parameters
        ----------
        indent : int, optional
            Initial indentation level passed to Lexbor. Defaults to ``0``.
        skip_ws_nodes : bool, optional
            Skip text nodes that contain only whitespace.
        skip_comment : bool, optional
            Exclude HTML comment nodes from the serialized output.
        raw : bool, optional
            Serialize text and attribute values without HTML escaping.
        without_closing : bool, optional
            Omit closing tags for non-void elements.
        tag_with_ns : bool, optional
            Include namespace prefixes in serialized tag names when available.
        without_text_indent : bool, optional
            Disable extra indentation added around text and comment content.
        full_doctype : bool, optional
            Serialize the full document type declaration when a doctype node is present.
        html5test : bool, optional
            Serialize using Lexbor's HTML5 test formatting mode.
        """
        ...
    def create_node(self, tag: str) -> LexborNode:
        """Given an HTML tag name, e.g. `"div"`, create a single empty node for that tag,
        e.g. `"<div></div>"`.


        Parameters
        ----------
        tag : str
            Name of the tag to create.

        Returns
        -------
        LexborNode
            Newly created element node.
        Raises
        ------
        SelectolaxError
            If the element cannot be created.

        Examples
        --------
        >>> parser = LexborHTMLParser("<div></div>")
        >>> new_node = parser.create_node("span")
        >>> new_node.tag_name
        'span'
        >>> parser.css_first("div").append_child(new_node)
        >>> parser.html
        '<html><head></head><body><div><span></span></div></body></html>'
        """

def create_tag(tag: str) -> LexborNode:
    """
    Given an HTML tag name, e.g. `"div"`, create a single empty node for that tag,
    e.g. `"<div></div>"`.

    Use `LexborHTMLParser().create_node(..)` if you need to create a node tied to a specific parser instance.
    """
    ...

def parse_fragment(html: str) -> list[LexborNode]:
    """
    Given HTML, parse it into a list of Nodes, such that the nodes
    correspond to the given HTML.

    For contrast, HTMLParser adds `<html>`, `<head>`, and `<body>` tags
    if they are missing. This function does not add these tags.
    """
    ...

class SelectolaxError(Exception):
    """An exception that indicates error."""

    pass

```

### `selectolax/lexbor.pyx`

```pyx
from cpython.bool cimport bool
from cpython.exc cimport PyErr_SetObject
from cpython.mem cimport (
    PyMem_RawCalloc,
    PyMem_RawFree,
    PyMem_RawMalloc,
    PyMem_RawRealloc
)
_ENCODING = 'UTF-8'

include "base.pxi"
include "utils.pxi"
include "lexbor/attrs.pxi"
include "lexbor/node.pxi"
include "lexbor/selection.pxi"
include "lexbor/util.pxi"
include "lexbor/node_remove.pxi"
include "lexbor/fragment_lookup.pxi"

# We don't inherit from HTMLParser here, because it also includes all the C code from Modest.

cdef class LexborHTMLParser:
    """The lexbor HTML parser.

    Use this class to parse raw HTML.

    This parser mimics most of the stuff from ``HTMLParser`` but not inherits it directly.

    Parameters
    ----------

    html : str (unicode) or bytes
    """
    def __init__(
        self,
        html: str | bytes,
        is_fragment: bool = False,
        fragment_tag: str = "div",
        fragment_namespace: str = "html",
    ):
        """Create a parser and load HTML.

        Parameters
        ----------
        html : str or bytes
            HTML content to parse.
        is_fragment : bool, optional
            When ``False`` (default), the input is parsed as a full HTML document.
            If the input is only a fragment, the parser still accepts it and inserts any missing required elements,
            (such as `<html>`, `<head>`, and `<body>`) into the tree,
            according to the HTML parsing rules in the HTML Standard.
            This matches how browsers construct the DOM when they load an HTML page.

            When ``True``, the input is parsed as an HTML fragment.
            The parser does not insert any missing required HTML elements.
            Behaves the same way as `DocumentFragment` in browsers.
            When `<html>`, `<head>` or `<body>` are present, ignores them entirely.
            As per the HTML Standard.
        fragment_tag : str, optional
            Context element tag used for fragment parsing. Defaults to ``"div"``.
            Only used when ``is_fragment`` is ``True``.
        fragment_namespace : str, optional
            Context element namespace used for fragment parsing. Defaults to ``"html"``.
            Accepts Lexbor namespace names such as ``"html"``, ``"svg"``, and ``"math"``,
            or a namespace URI recognized by Lexbor. Only used when ``is_fragment`` is ``True``.

        """
        cdef size_t html_len
        cdef object bytes_html

        self._is_fragment = is_fragment
        self._fragment_wrapper = NULL
        self._fragment_root = NULL
        self._fragment_tag_id = LXB_TAG_DIV
        self._fragment_namespace_id = LXB_NS_HTML
        self._selector = None
        self._new_html_document()
        if self._is_fragment:
            self._fragment_tag_id = _fragment_tag_id_from_string(self.document, fragment_tag)
            self._fragment_namespace_id = _fragment_namespace_id_from_string(self.document, fragment_namespace)
        bytes_html, html_len = preprocess_input(html)
        self._parse_html(bytes_html, html_len)
        self.raw_html = bytes_html

    cdef inline void _new_html_document(self):
        """Initialize a fresh Lexbor HTML document.

        Returns
        -------
        None

        Raises
        ------
        SelectolaxError
            If the underlying Lexbor document cannot be created.
        """
        with nogil:
            self.document = lxb_html_document_create()

        if self.document == NULL:
            PyErr_SetObject(SelectolaxError, "Failed to initialize object for HTML Document.")

    cdef int _parse_html(self, char *html, size_t html_len) except -1:
        """Parse HTML content into the internal document.

        Parameters
        ----------
        html : char *
            Pointer to UTF-8 encoded HTML bytes.
        html_len : size_t
            Length of the HTML buffer.

        Returns
        -------
        int
            ``0`` on success; ``-1`` when parsing fails.

        Raises
        ------
        SelectolaxError
            If Lexbor returns a non-OK status.
        RuntimeError
            If the internal document is ``NULL`` after a successful parse.
        """
        cdef lxb_status_t status

        if self.document == NULL:
            return -1

        with nogil:
            if self._is_fragment:
                status = self._parse_html_fragment(html, html_len)
            else:
                status = self._parse_html_document(html, html_len)

        if status != LXB_STATUS_OK:
            PyErr_SetObject(SelectolaxError, "Can't parse HTML.")
            return -1

        if self.document == NULL:
            PyErr_SetObject(RuntimeError, "document is NULL even after html was parsed correctly")
            return -1
        return 0

    cdef inline lxb_status_t _parse_html_document(self, char *html, size_t html_len) nogil:
        """Parse HTML as a full HTML document.
        If the input is only a fragment, the parser still accepts it and inserts any missing required elements,
        (such as `<html>`, `<head>`, and `<body>`) into the tree,
        according to the HTML parsing rules in the HTML Standard.
        This matches how browsers construct the DOM when they load an HTML page.

        Parameters
        ----------
        html : char *
            Pointer to UTF-8 encoded HTML bytes.
        html_len : size_t
            Length of the HTML buffer.

        Returns
        -------
        lxb_status_t
            Lexbor status code produced by ``lxb_html_document_parse``.
        """
        return lxb_html_document_parse(self.document, <lxb_char_t *> html, html_len)

    cdef inline lxb_status_t _parse_html_fragment(self, char *html, size_t html_len) nogil:
        """Parse HTML as an HTML fragment.
        The parser does not insert any missing required HTML elements.

        Parameters
        ----------
        html : char *
            Pointer to UTF-8 encoded HTML bytes.
        html_len : size_t
            Length of the HTML buffer.

        Returns
        -------
        lxb_status_t
            Lexbor status code; ``LXB_STATUS_OK`` when parsing the fragment succeeded.
        """
        cdef lxb_html_parser_t *parser = NULL
        cdef lxb_dom_node_t *fragment_html_node = NULL
        cdef lxb_status_t status = LXB_STATUS_OK

        parser = lxb_html_parser_create()
        if parser == NULL:
            return LXB_STATUS_ERROR_MEMORY_ALLOCATION

        status = lxb_html_parser_init(parser)
        if status != LXB_STATUS_OK:
            lxb_html_parser_destroy(parser)
            return status

        fragment_html_node = lxb_html_parse_fragment_by_tag_id(
            parser,
            self.document,
            self._fragment_tag_id,
            self._fragment_namespace_id,
            <lxb_char_t *> html,
            html_len
        )
        if fragment_html_node == NULL:
            status = parser.status
            lxb_html_parser_destroy(parser)
            if status == LXB_STATUS_OK:
                return LXB_STATUS_ERROR
            return status

        self._fragment_wrapper = fragment_html_node
        self._fragment_root = fragment_html_node.first_child
        lxb_html_parser_destroy(parser)
        return LXB_STATUS_OK

    def __dealloc__(self):
        """Release the underlying Lexbor HTML document.

        Returns
        -------
        None

        Notes
        -----
        Safe to call multiple times; does nothing if the document is already
        freed.
        """
        if self.document != NULL:
            lxb_html_document_destroy(self.document)

    def __repr__(self):
        """Return a concise representation of the parsed document.

        Returns
        -------
        str
            A string showing the number of characters in the parsed HTML.
        """
        html_len = len(self.root.html if self.root is not None else "")
        return f"<LexborHTMLParser chars='{html_len}'>"

    @property
    def selector(self):
        """Return a lazily created CSS selector helper.

        Returns
        -------
        LexborCSSSelector
            Selector instance bound to this parser.
        """
        if self._selector is None:
            self._selector = LexborCSSSelector()
        return self._selector

    @property
    def root(self):
        """Return the document root node.

        Returns
        -------
        LexborNode or None
            Root of the parsed document, or ``None`` if unavailable.
        """
        if self.document == NULL:
            return None
        cdef LexborNode  node
        cdef lxb_dom_node_t* dom_root
        if self._is_fragment and self._fragment_root != NULL:
            dom_root = self._fragment_root
        else:
            dom_root = lxb_dom_document_root(&self.document.dom_document)
        if dom_root == NULL:
            return None
        node =  LexborNode.new(dom_root, self)
        if self._is_fragment:
            node.set_as_fragment_root()
        return node

    @property
    def body(self):
        """Return document body.

        Returns
        -------
        LexborNode or None
            ``<body>`` element when present, otherwise ``None``.
        """
        cdef lxb_html_body_element_t* body
        body = lxb_html_document_body_element_noi(self.document)
        if body == NULL:
            return None
        return LexborNode.new(<lxb_dom_node_t *> body, self)

    @property
    def head(self):
        """Return document head.

        Returns
        -------
        LexborNode or None
            ``<head>`` element when present, otherwise ``None``.
        """
        cdef lxb_html_head_element_t* head
        head = lxb_html_document_head_element_noi(self.document)
        if head == NULL:
            return None
        return LexborNode.new(<lxb_dom_node_t *> head, self)

    def tags(self, str name):
        """Return all tags that match the provided name.

        Parameters
        ----------
        name : str
            Tag name to search for (e.g., ``"div"``).

        Returns
        -------
        list of LexborNode
            Matching elements in document order.

        Raises
        ------
        ValueError
            If ``name`` is empty or longer than 100 characters.
        SelectolaxError
            If Lexbor cannot locate the elements.
        """

        if not name:
            raise ValueError("Tag name cannot be empty")
        if len(name) > 100:
            raise ValueError("Tag name is too long")

        cdef lxb_dom_collection_t* collection = NULL
        cdef lxb_status_t status
        pybyte_name = name.encode('UTF-8')

        result = list()
        collection = lxb_dom_collection_make(&self.document.dom_document, 128)

        if collection == NULL:
            return result
        status = lxb_dom_elements_by_tag_name(
            <lxb_dom_element_t *> self.document,
            collection,
            <lxb_char_t *> pybyte_name,
            len(pybyte_name)
        )
        if status != 0x0000:
            lxb_dom_collection_destroy(collection, <bint> True)
            raise SelectolaxError("Can't locate elements.")

        for i in range(lxb_dom_collection_length_noi(collection)):
            node = LexborNode.new(
                <lxb_dom_node_t*> lxb_dom_collection_element_noi(collection, i),
                self
            )
            result.append(node)
        lxb_dom_collection_destroy(collection, <bint> True)
        return result

    def text(
        self,
        deep: bool = True,
        separator: str = "",
        strip: bool = False,
        skip_empty: bool = False,
    ) -> str:
        """Returns the text of the node including text of all its child nodes.

        Parameters
        ----------
        strip : bool, default False
            If true, calls ``str.strip()`` on each text part to remove extra white spaces.
        separator : str, default ''
            The separator to use when joining text from different nodes.
        deep : bool, default True
            If True, includes text from all child nodes.
        skip_empty : bool, optional
            Exclude text nodes whose content is only ASCII whitespace (space,
            tab, newline, form feed or carriage return) when ``True``.
            Defaults to ``False``.

        Returns
        -------
        text : str
            Combined textual content assembled according to the provided options.
        """
        if self.root is None:
            return ""
        return self.root.text(deep=deep, separator=separator, strip=strip, skip_empty=skip_empty)

    @property
    def html(self):
        """Return HTML representation of the page.

        Returns
        -------
        str or None
            Serialized HTML of the current document.
        """
        if self.document == NULL:
            return None
        if self._is_fragment:
            if self.root is None:
                return ""
            return self.root.html
        node = LexborNode.new(<lxb_dom_node_t *> &self.document.dom_document, self)
        return node.html

    def html_pretty(
        self,
        Py_ssize_t indent=0,
        bint skip_ws_nodes=False,
        bint skip_comment=False,
        bint raw=False,
        bint without_closing=False,
        bint tag_with_ns=False,
        bint without_text_indent=False,
        bint full_doctype=False,
        bint html5test=False,
    ):
        """Return pretty-printed HTML representation of the page.

        Parameters
        ----------
        indent : int, optional
            Initial indentation level passed to Lexbor. Defaults to ``0``.
        skip_ws_nodes : bool, optional
            Skip text nodes that contain only whitespace.
        skip_comment : bool, optional
            Exclude HTML comment nodes from the serialized output.
        raw : bool, optional
            Serialize text and attribute values without HTML escaping.
        without_closing : bool, optional
            Omit closing tags for non-void elements.
        tag_with_ns : bool, optional
            Include namespace prefixes in serialized tag names when available.
        without_text_indent : bool, optional
            Disable extra indentation added around text and comment content.
        full_doctype : bool, optional
            Serialize the full document type declaration when a doctype node is present.
        html5test : bool, optional
            Serialize using Lexbor's HTML5 test formatting mode.
        """
        cdef lxb_html_serialize_opt_t options
        if self.document == NULL:
            return None
        if indent < 0:
            raise ValueError("indent must be greater than or equal to 0")
        options = _html_pretty_options(
            skip_ws_nodes,
            skip_comment,
            raw,
            without_closing,
            tag_with_ns,
            without_text_indent,
            full_doctype,
            html5test,
        )
        if self._is_fragment:
            if self.root is None:
                return None
            return self.root.html_pretty(
                indent=indent,
                skip_ws_nodes=skip_ws_nodes,
                skip_comment=skip_comment,
                raw=raw,
                without_closing=without_closing,
                tag_with_ns=tag_with_ns,
                without_text_indent=without_text_indent,
                full_doctype=full_doctype,
                html5test=html5test,
            )
        node = LexborNode.new(<lxb_dom_node_t *> &self.document.dom_document, self)
        return node._serialize_html(options, <size_t> indent, True)

    def css(self, str query):
        """A CSS selector.

        Matches pattern `query` against HTML tree.
        `CSS selectors reference <https://www.w3schools.com/cssref/css_selectors.asp>`_.

        Special selectors:

         - parser.css('p:lexbor-contains("awesome" i)') -- case-insensitive contains
         - parser.css('p:lexbor-contains("awesome")') -- case-sensitive contains

        Parameters
        ----------
        query : str
            CSS selector (e.g. "div > :nth-child(2n+1):not(:has(a))").

        Returns
        -------
        selector : list of `Node` objects
        """
        return self.root.css(query)

    def css_first(self, str query, default=None, strict=False):
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : Any, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `LexborNode` object
        """
        return self.root.css_first(query, default, strict)

    def strip_tags(self, list tags, bool recursive = False):
        """Remove specified tags from the node.

        Parameters
        ----------
        tags : list of str
            List of tags to remove.
        recursive : bool, default False
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = LexborHTMLParser('<html><head></head><body><script></script><div>Hello world!</div></body></html>')
        >>> tags = ['head', 'style', 'script', 'xmp', 'iframe', 'noembed', 'noframes']
        >>> tree.strip_tags(tags)
        >>> tree.html
        '<html><body><div>Hello world!</div></body></html>'

        Returns
        -------
        None
        """
        cdef lxb_dom_collection_t* collection = NULL
        cdef lxb_status_t status

        for tag in tags:
            pybyte_name = tag.encode('UTF-8')

            collection = lxb_dom_collection_make(&self.document.dom_document, 128)

            if collection == NULL:
                raise SelectolaxError("Can't initialize DOM collection.")

            status = lxb_dom_elements_by_tag_name(
                <lxb_dom_element_t *> self.document,
                collection,
                <lxb_char_t *> pybyte_name,
                len(pybyte_name)
            )
            if status != 0x0000:
                lxb_dom_collection_destroy(collection, <bint> True)
                raise SelectolaxError("Can't locate elements.")

            for i in range(lxb_dom_collection_length_noi(collection)):
                if recursive:
                    node_remove_deep(<lxb_dom_node_t *> lxb_dom_collection_element_noi(collection, i))
                else:
                    lxb_dom_node_remove(<lxb_dom_node_t *> lxb_dom_collection_element_noi(collection, i))
            lxb_dom_collection_destroy(collection, <bint> True)

    def select(self, query=None):
        """Select nodes given a CSS selector.

        Works similarly to the ``css`` method, but supports chained filtering and extra features.

        Parameters
        ----------
        query : str or None
            The CSS selector to use when searching for nodes.

        Returns
        -------
        LexborSelector or None
            Selector bound to the root node, or ``None`` if the document is empty.
        """
        cdef LexborNode node
        node = self.root
        if node:
            return LexborSelector(node, query)
        return None

    def any_css_matches(self, tuple selectors):
        """Return ``True`` if any of the specified CSS selectors match.

        Parameters
        ----------
        selectors : tuple[str]
            CSS selectors to evaluate.

        Returns
        -------
        bool
            ``True`` when at least one selector matches.
        """
        return self.root.any_css_matches(selectors)

    def scripts_contain(self, str query):
        """Return ``True`` if any script tag contains the given text.

        Caches script tags on the first call to improve performance.

        Parameters
        ----------
        query : str
            Text to search for within script contents.

        Returns
        -------
        bool
            ``True`` when a matching script tag is found.
        """
        return self.root.scripts_contain(query)

    def script_srcs_contain(self, tuple queries):
        """Return ``True`` if any script ``src`` contains one of the strings.

        Caches values on the first call to improve performance.

        Parameters
        ----------
        queries : tuple of str
            Strings to look for inside ``src`` attributes.

        Returns
        -------
        bool
            ``True`` when a matching source value is found.
        """
        return self.root.script_srcs_contain(queries)

    def css_matches(self, str selector):
        """Return ``True`` if the document matches the selector at least once.

        Parameters
        ----------
        selector : str
            CSS selector to test.

        Returns
        -------
        bool
            ``True`` when a match exists.
        """
        return self.root.css_matches(selector)

    def merge_text_nodes(self):
        """Iterates over all text nodes and merges all text nodes that are close to each other.

        This is useful for text extraction.
        Use it when you need to strip HTML tags and merge "dangling" text.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div><p><strong>J</strong>ohn</p><p>Doe</p></div>")
        >>> node = tree.css_first('div')
        >>> tree.unwrap_tags(["strong"])
        >>> tree.text(deep=True, separator=" ", strip=True)
        "J ohn Doe" # Text extraction produces an extra space because the strong tag was removed.
        >>> node.merge_text_nodes()
        >>> tree.text(deep=True, separator=" ", strip=True)
        "John Doe"

        Returns
        -------
        None
        """
        return self.root.merge_text_nodes()

    @staticmethod
    cdef LexborHTMLParser from_document(lxb_html_document_t *document, bytes raw_html):
        """Construct a parser from an existing Lexbor document.

        Parameters
        ----------
        document : lxb_html_document_t *
            Borrowed pointer to an initialized Lexbor HTML document.
        raw_html : bytes
            Original HTML bytes backing the document.

        Returns
        -------
        LexborHTMLParser
            Parser instance wrapping the provided document.
        """
        obj = <LexborHTMLParser> LexborHTMLParser.__new__(LexborHTMLParser)
        obj.document = document
        obj.raw_html = raw_html
        obj.cached_script_texts = None
        obj.cached_script_srcs = None
        obj._is_fragment = False
        obj._fragment_wrapper = NULL
        obj._fragment_root = NULL
        obj._fragment_tag_id = LXB_TAG_DIV
        obj._fragment_namespace_id = LXB_NS_HTML
        obj._selector = None
        return obj

    def clone(self):
        """Clone the current document tree.

        You can use to do temporary modifications without affecting the original HTML tree.
        It is tied to the current parser instance.
        Gets destroyed when the parser instance is destroyed.

        Returns
        -------
        LexborHTMLParser
            A parser instance backed by a deep-copied document.
        """
        cdef lxb_html_document_t* cloned_document
        cdef lxb_dom_node_t* cloned_node
        cdef lxb_dom_node_t* source_node
        cdef lxb_dom_node_t* cloned_root
        cdef LexborHTMLParser cls

        with nogil:
            cloned_document = lxb_html_document_create()

        if cloned_document == NULL:
            raise SelectolaxError("Can't create a new document")

        cloned_document.ready_state = LXB_HTML_DOCUMENT_READY_STATE_COMPLETE

        source_node = lxb_dom_document_root(&self.document.dom_document)
        if self._is_fragment and self._fragment_wrapper != NULL:
            source_node = self._fragment_wrapper

        with nogil:
            cloned_node = lxb_dom_document_import_node(
                &cloned_document.dom_document,
                source_node,
                <bint> True
            )

        if cloned_node == NULL:
            raise SelectolaxError("Can't create a new document")

        with nogil:
            lxb_dom_node_insert_child(<lxb_dom_node_t * > cloned_document, cloned_node)

        cls = LexborHTMLParser.from_document(cloned_document, self.raw_html)
        if self._is_fragment:
            cls._is_fragment = True
            cls._fragment_tag_id = self._fragment_tag_id
            cls._fragment_namespace_id = self._fragment_namespace_id
            cls._fragment_wrapper = cloned_node
            cloned_root = cloned_node
            if cloned_root != NULL:
                cls._fragment_root = cloned_root.first_child
        return cls

    def unwrap_tags(self, list tags, delete_empty = False):
        """Unwraps specified tags from the HTML tree.

        Works the same as the ``unwrap`` method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool
            Whenever to delete empty tags.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.body.unwrap_tags(['i','a'])
        >>> tree.body.html
        '<body><div>Hello world!</div></body>'

        Returns
        -------
        None
        """
        # faster to check if the document is empty which should determine if we have a root
        if self.document != NULL:
            self.root.unwrap_tags(tags, delete_empty=delete_empty)

    @property
    def inner_html(self) -> str:
        """Return HTML representation of the child nodes.

        Works similar to innerHTML in JavaScript.
        Unlike the `.html` property, does not include the current node.
        Can be used to set HTML as well. See the setter docstring.

        Returns
        -------
        text : str | None
        """
        return self.root.inner_html

    @inner_html.setter
    def inner_html(self, str html):
        """Set inner HTML to the specified HTML.

        Replaces existing data inside the node.
        Works similar to innerHTML in JavaScript.

        Parameters
        ----------
        html : str

        Returns
        -------
        None
        """
        self.root.inner_html = html

    def inner_html_pretty(
        self,
        Py_ssize_t indent=0,
        bint skip_ws_nodes=False,
        bint skip_comment=False,
        bint raw=False,
        bint without_closing=False,
        bint tag_with_ns=False,
        bint without_text_indent=False,
        bint full_doctype=False,
        bint html5test=False,
    ):
        """Return pretty-printed HTML representation of the child nodes.

        Parameters
        ----------
        indent : int, optional
            Initial indentation level passed to Lexbor. Defaults to ``0``.
        skip_ws_nodes : bool, optional
            Skip text nodes that contain only whitespace.
        skip_comment : bool, optional
            Exclude HTML comment nodes from the serialized output.
        raw : bool, optional
            Serialize text and attribute values without HTML escaping.
        without_closing : bool, optional
            Omit closing tags for non-void elements.
        tag_with_ns : bool, optional
            Include namespace prefixes in serialized tag names when available.
        without_text_indent : bool, optional
            Disable extra indentation added around text and comment content.
        full_doctype : bool, optional
            Serialize the full document type declaration when a doctype node is present.
        html5test : bool, optional
            Serialize using Lexbor's HTML5 test formatting mode.
        """
        if self.root is None:
            return None
        return self.root.inner_html_pretty(
            indent=indent,
            skip_ws_nodes=skip_ws_nodes,
            skip_comment=skip_comment,
            raw=raw,
            without_closing=without_closing,
            tag_with_ns=tag_with_ns,
            without_text_indent=without_text_indent,
            full_doctype=full_doctype,
            html5test=html5test,
        )

    def create_node(self, str tag):
        """Given an HTML tag name, e.g. `"div"`, create a single empty node for that tag,
        e.g. `"<div></div>"`.

        Parameters
        ----------
        tag : str
            Name of the tag to create.

        Returns
        -------
        LexborNode
            Newly created element node.
        Raises
        ------
        SelectolaxError
            If the element cannot be created.

        Examples
        --------
        >>> parser = LexborHTMLParser("<div></div>")
        >>> new_node = parser.create_node("span")
        >>> new_node.tag_name
        'span'
        >>> parser.css_first("div").append_child(new_node)
        >>> parser.html
        '<html><head></head><body><div><span></span></div></body></html>'
        """
        cdef lxb_html_element_t* element
        cdef lxb_dom_node_t* dom_node
        if not tag:
            raise SelectolaxError("Tag name cannot be empty")
        pybyte_name = tag.encode('UTF-8')

        element = lxb_html_document_create_element(
            self.document,
            <const lxb_char_t *> pybyte_name,
            len(pybyte_name),
            NULL
        )

        if element == NULL:
            raise SelectolaxError(f"Can't create element for tag '{tag}'")

        dom_node = <lxb_dom_node_t *> element

        return LexborNode.new(dom_node, self)

# Putting lexbor on python's heap is better than putting it
# onto C's Heap, because python's Garbage collector can collect
# this memory after use and has the bonus of gaining access to
# mimalloc which python uses under the hood...
if lexbor_memory_setup(
    PyMem_RawMalloc,
    PyMem_RawRealloc,
    PyMem_RawCalloc,
    PyMem_RawFree
) != LXB_STATUS_OK:
    # This will almost never happen due to the code in both the windows and posix versions
    # but if something were to happen this excecption on import should be triggered...
    raise SelectolaxError("Can't initalize allocators from lexbor_memory_setup(...)")

```

### `selectolax/lexbor/attrs.pxi`

```pxi
cimport cython


@cython.final
cdef class LexborAttributes:
    """A dict-like object that represents attributes."""
    cdef lxb_dom_node_t *node
    cdef unicode decode_errors

    @staticmethod
    cdef LexborAttributes create(lxb_dom_node_t *node):
        obj = <LexborAttributes> LexborAttributes.__new__(LexborAttributes)
        obj.node = node
        return obj

    def __iter__(self):
        cdef lxb_dom_attr_t *attr = lxb_dom_element_first_attribute_noi(<lxb_dom_element_t *> self.node)
        cdef size_t str_len = 0
        attributes = dict()

        while attr != NULL:
            key = lxb_dom_attr_local_name_noi(attr, &str_len)
            if key is not NULL:
                yield key.decode(_ENCODING)
            attr = attr.next

    def __setitem__(self, str key, object value):
        value = value
        bytes_key = key.encode(_ENCODING)
        bytes_value = value.encode(_ENCODING) if value else b""
        cdef lxb_dom_attr_t *attr
        cdef lxb_dom_document_t *doc

        if value is None:
            # N.B. This is suboptimal, but there is not API to set empty attributes
            attr = lxb_dom_element_set_attribute(
                <lxb_dom_element_t *> self.node,
                <lxb_char_t *> bytes_key, len(bytes_key),
                NULL, 0
            )
            if attr == NULL:
                raise MemoryError("Failed to set attribute")
            doc = (<lxb_dom_node_t*>attr).owner_document
            lexbor_str_destroy(attr.value, doc.text, 0)
            attr.value = NULL

        elif isinstance(value, str) or isinstance(value, unicode) :
            attr = lxb_dom_element_set_attribute(
                <lxb_dom_element_t *> self.node,
                <lxb_char_t *> bytes_key, len(bytes_key),
                <lxb_char_t *> bytes_value, len(bytes_value),
            )
            if attr == NULL:
                raise MemoryError("Failed to set attribute")
        else:
            raise TypeError("Expected str or unicode, got %s" % type(value))

    def __delitem__(self, key):
        try:
            self.__getitem__(key)
        except KeyError:
            raise KeyError(key)
        bytes_key = key.encode(_ENCODING)
        lxb_dom_element_remove_attribute(
            <lxb_dom_element_t *> self.node,
            <lxb_char_t *> bytes_key, len(bytes_key),
        )

    def __getitem__(self, str key):
        bytes_key = key.encode(_ENCODING)
        cdef lxb_dom_attr_t * attr = lxb_dom_element_attr_by_name(
            <lxb_dom_element_t *> self.node,
            <lxb_char_t *> bytes_key, len(bytes_key)
        )
        cdef size_t str_len = 0
        if attr != NULL:
            value = lxb_dom_attr_value_noi(attr, &str_len)
            return value.decode(_ENCODING) if value else None
        raise KeyError(key)

    def __len__(self):
        return len(list(self.__iter__()))

    def keys(self):
        return self.__iter__()

    def items(self):
        for key in self.__iter__():
            yield key, self[key]

    def values(self):
        for key in self.__iter__():
            yield self[key]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def sget(self, key, default=""):
        """Same as get, but returns empty strings instead of None values for empty attributes."""
        try:
            val = self[key]
            if val is None:
                val = ""
            return val
        except KeyError:
            return default

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __repr__(self):
        cdef lxb_char_t *c_text
        cdef size_t str_len = 0
        c_text = lxb_dom_element_qualified_name(<lxb_dom_element_t *> self.node, &str_len)
        tag_name = c_text.decode(_ENCODING, 'ignore') if c_text != NULL else 'unknown'
        return "<%s attributes, %s items>" % (tag_name, len(self))

```

### `selectolax/lexbor/fragment_lookup.pxi`

```pxi
cdef inline lxb_tag_id_t _fragment_tag_id_from_string(
    lxb_html_document_t *document,
    str fragment_tag,
) except? 0:
    cdef bytes fragment_tag_bytes
    cdef lxb_tag_id_t tag_id

    if not fragment_tag:
        raise ValueError("fragment_tag cannot be empty")

    fragment_tag_bytes = fragment_tag.encode("UTF-8")
    tag_id = lxb_tag_id_by_name_noi(
        document.dom_document.tags,
        <const lxb_char_t *> fragment_tag_bytes,
        len(fragment_tag_bytes),
    )
    if tag_id == LXB_TAG__UNDEF:
        raise ValueError(f"Unknown fragment tag: {fragment_tag!r}")

    return tag_id


cdef inline lxb_ns_id_t _fragment_namespace_id_from_string(
    lxb_html_document_t *document,
    str fragment_namespace,
) except? 0:
    cdef bytes fragment_namespace_bytes
    cdef const lxb_ns_prefix_data_t *prefix_data
    cdef const lxb_ns_data_t *ns_data

    if not fragment_namespace:
        raise ValueError("fragment_namespace cannot be empty")

    fragment_namespace_bytes = fragment_namespace.encode("UTF-8")

    prefix_data = lxb_ns_prefix_data_by_name(
        document.dom_document.ns,
        <const lxb_char_t *> fragment_namespace_bytes,
        len(fragment_namespace_bytes),
    )
    if prefix_data != NULL:
        return <lxb_ns_id_t> prefix_data.prefix_id

    ns_data = lxb_ns_data_by_link(
        document.dom_document.ns,
        <const lxb_char_t *> fragment_namespace_bytes,
        len(fragment_namespace_bytes),
    )
    if ns_data != NULL:
        return ns_data.ns_id

    raise ValueError(f"Unknown fragment namespace: {fragment_namespace!r}")

```

### `selectolax/lexbor/node_remove.pxi`

```pxi

cdef lxb_dom_node_t * node_remove_deep(lxb_dom_node_t* root):
    cdef lxb_dom_node_t *tmp
    cdef lxb_dom_node_t *node = root

    while node != NULL:
        if node.first_child != NULL:
            node = node.first_child
        else:
            while node != root and node.next == NULL:
                tmp = node.parent
                lxb_dom_node_remove(node)
                node = tmp

            if node == root:
                lxb_dom_node_remove(node)
                break

            tmp = node.next
            lxb_dom_node_remove(node)
            node = tmp

    return NULL

cdef bint node_is_removed(lxb_dom_node_t* node):
    if node.parent == NULL and node.next == NULL \
       and node.prev == NULL:
        return 1
    return 0

```

### `selectolax/lexbor/node.pxi`

```pxi
cimport cython
from cpython.exc cimport PyErr_SetNone

import logging

logger = logging.getLogger("selectolax")

_TAG_TO_NAME = {
    0x0005: "-doctype",
    0x0002: "-text",
    0x0004: "-comment",
}
ctypedef fused str_or_LexborNode:
    str
    bytes
    LexborNode

ctypedef fused str_or_bytes:
    str
    bytes

cdef inline bytes to_bytes(str_or_LexborNode value):
    cdef bytes bytes_val
    if isinstance(value, unicode):
        bytes_val = <bytes> value.encode("utf-8")
    elif isinstance(value, bytes):
        bytes_val = <bytes> value
    return bytes_val


@cython.final
cdef class LexborNode:
    """A class that represents HTML node (element)."""

    cdef void set_as_fragment_root(self):
        self._is_fragment_root = 1

    @staticmethod
    cdef LexborNode new(lxb_dom_node_t *node, LexborHTMLParser parser):
        cdef LexborNode lxbnode = LexborNode.__new__(LexborNode)
        lxbnode.node = node
        lxbnode.parser = parser
        lxbnode._is_fragment_root = 0
        return lxbnode

    @property
    def mem_id(self):
        return <size_t> self.node

    @property
    def child(self):
        """Alias for the `first_child` property.

        **Deprecated**. Please use `first_child` instead.
        """
        return self.first_child

    @property
    def first_child(self):
        """Return the first child node."""
        cdef LexborNode node
        if self.node.first_child:
            node = LexborNode.new(<lxb_dom_node_t *> self.node.first_child, self.parser)
            return node
        return None

    @property
    def parent(self):
        """Return the parent node."""
        cdef LexborNode node
        if self.node.parent != NULL:
            node = LexborNode.new(<lxb_dom_node_t *> self.node.parent, self.parser)
            return node
        return None

    @property
    def next(self):
        """Return next node."""
        cdef LexborNode node
        if self.node.next != NULL:
            node = LexborNode.new(<lxb_dom_node_t *> self.node.next, self.parser)
            return node
        return None

    @property
    def prev(self):
        """Return previous node."""
        cdef LexborNode node
        if self.node.prev != NULL:
            node = LexborNode.new(<lxb_dom_node_t *> self.node.prev, self.parser)
            return node
        return None

    @property
    def last_child(self):
        """Return last child node."""
        cdef LexborNode node
        if self.node.last_child != NULL:
            node = LexborNode.new(<lxb_dom_node_t *> self.node.last_child, self.parser)
            return node
        return None

    @property
    def html(self):
        """Return HTML representation of the current node including all its child nodes.

        Returns
        -------
        text : str
        """
        cdef lexbor_str_t *lxb_str
        cdef lxb_status_t status
        lxb_str = lexbor_str_create()
        if self._is_fragment_root:
            status = serialize_fragment(self.node, lxb_str)
            # status = lxb_html_serialize_tree_str(self.node, lxb_str)
        else:
            status = lxb_html_serialize_tree_str(self.node, lxb_str)
        if status == 0:
            html = lxb_str.data.decode(_ENCODING).replace('<-undef>', '')
            lexbor_str_destroy(lxb_str, self.node.owner_document.text, True)
            return html
        lexbor_str_destroy(lxb_str, self.node.owner_document.text, True)
        return None

    cdef inline str _serialize_html(self, lxb_html_serialize_opt_t options, size_t indent, bint pretty):
        cdef lexbor_str_t *lxb_str
        cdef lxb_status_t status

        lxb_str = lexbor_str_create()
        if self._is_fragment_root:
            if pretty:
                status = serialize_fragment_pretty(self.node, lxb_str, options, indent)
            else:
                status = serialize_fragment(self.node, lxb_str)
        else:
            if pretty:
                status = lxb_html_serialize_pretty_tree_str(self.node, options, indent, lxb_str)
            else:
                status = lxb_html_serialize_tree_str(self.node, lxb_str)

        if status == 0:
            html = lxb_str.data.decode(_ENCODING).replace('<-undef>', '')
            lexbor_str_destroy(lxb_str, self.node.owner_document.text, True)
            return html
        lexbor_str_destroy(lxb_str, self.node.owner_document.text, True)
        return None

    cdef inline str _serialize_inner_html(self, lxb_html_serialize_opt_t options, size_t indent, bint pretty):
        cdef lexbor_str_t *lxb_str
        cdef lxb_status_t status

        lxb_str = lexbor_str_create()
        if pretty:
            status = lxb_html_serialize_pretty_deep_str(self.node, options, indent, lxb_str)
        else:
            status = lxb_html_serialize_deep_str(self.node, lxb_str)

        if status == 0 and lxb_str.data:
            html = lxb_str.data.decode(_ENCODING).replace('<-undef>', '')
            lexbor_str_destroy(lxb_str, self.node.owner_document.text, True)
            return html
        lexbor_str_destroy(lxb_str, self.node.owner_document.text, True)
        return None

    def html_pretty(
        self,
        Py_ssize_t indent=0,
        bint skip_ws_nodes=False,
        bint skip_comment=False,
        bint raw=False,
        bint without_closing=False,
        bint tag_with_ns=False,
        bint without_text_indent=False,
        bint full_doctype=False,
        bint html5test=False,
    ):
        """Return pretty-printed HTML for the current node.

        Parameters
        ----------
        indent : int, optional
            Initial indentation level passed to Lexbor. Defaults to ``0``.
        skip_ws_nodes : bool, optional
            Skip text nodes that contain only whitespace.
        skip_comment : bool, optional
            Exclude HTML comment nodes from the serialized output.
        raw : bool, optional
            Serialize text and attribute values without HTML escaping.
        without_closing : bool, optional
            Omit closing tags for non-void elements.
        tag_with_ns : bool, optional
            Include namespace prefixes in serialized tag names when available.
        without_text_indent : bool, optional
            Disable extra indentation added around text and comment content.
        full_doctype : bool, optional
            Serialize the full document type declaration when a doctype node is present.
        html5test : bool, optional
            Serialize using Lexbor's HTML5 test formatting mode.
        """
        cdef lxb_html_serialize_opt_t options
        if indent < 0:
            raise ValueError("indent must be greater than or equal to 0")
        options = _html_pretty_options(
            skip_ws_nodes,
            skip_comment,
            raw,
            without_closing,
            tag_with_ns,
            without_text_indent,
            full_doctype,
            html5test,
        )
        return self._serialize_html(options, <size_t> indent, True)

    def inner_html_pretty(
        self,
        Py_ssize_t indent=0,
        bint skip_ws_nodes=False,
        bint skip_comment=False,
        bint raw=False,
        bint without_closing=False,
        bint tag_with_ns=False,
        bint without_text_indent=False,
        bint full_doctype=False,
        bint html5test=False,
    ):
        """Return pretty-printed HTML representation of the child nodes.

        Parameters
        ----------
        indent : int, optional
            Initial indentation level passed to Lexbor. Defaults to ``0``.
        skip_ws_nodes : bool, optional
            Skip text nodes that contain only whitespace.
        skip_comment : bool, optional
            Exclude HTML comment nodes from the serialized output.
        raw : bool, optional
            Serialize text and attribute values without HTML escaping.
        without_closing : bool, optional
            Omit closing tags for non-void elements.
        tag_with_ns : bool, optional
            Include namespace prefixes in serialized tag names when available.
        without_text_indent : bool, optional
            Disable extra indentation added around text and comment content.
        full_doctype : bool, optional
            Serialize the full document type declaration when a doctype node is present.
        html5test : bool, optional
            Serialize using Lexbor's HTML5 test formatting mode.
        """
        cdef lxb_html_serialize_opt_t options
        if indent < 0:
            raise ValueError("indent must be greater than or equal to 0")
        options = _html_pretty_options(
            skip_ws_nodes,
            skip_comment,
            raw,
            without_closing,
            tag_with_ns,
            without_text_indent,
            full_doctype,
            html5test,
        )
        return self._serialize_inner_html(options, <size_t> indent, True)

    def __hash__(self):
        return self.mem_id

    def text_lexbor(self):
        """Returns the text of the node including text of all its child nodes.

        Uses builtin method from lexbor.
        """

        cdef size_t str_len = 0
        cdef lxb_char_t * text
        text = lxb_dom_node_text_content(self.node, &str_len)
        if <int> str_len == 0:
            raise RuntimeError("Can't extract text")

        unicode_text = text.decode(_ENCODING)
        return unicode_text

    def text(self, bool deep=True, str separator='', bool strip=False, bool skip_empty=False):
        """Return concatenated text from this node.

        Parameters
        ----------
        deep : bool, optional
            When ``True`` (default), include text from all descendant nodes; when
            ``False``, only include direct children.
        separator : str, optional
            String inserted between successive text fragments.
        strip : bool, optional
            If ``True``, apply ``str.strip()`` to each fragment before joining to
            remove surrounding whitespace. Defaults to ``False``.
        skip_empty : bool, optional
            Exclude text nodes whose content is only ASCII whitespace (space,
            tab, newline, form feed or carriage return) when ``True``.
            Defaults to ``False``.

        Returns
        -------
        text : str
            Combined textual content assembled according to the provided options.

        """
        cdef unsigned char * text
        cdef LexborNode start_node = self._get_node()
        cdef lxb_dom_node_t * node = <lxb_dom_node_t *> start_node.node.first_child

        if not deep:
            container = TextContainer(separator, strip)
            if _is_node_type(self.node, LXB_DOM_NODE_TYPE_TEXT):
                text = <unsigned char *> lexbor_str_data_noi(&(<lxb_dom_character_data_t *> self.node).data)
                if text != NULL:
                    if not skip_empty or not self.is_empty_text_node:
                        py_text = text.decode(_ENCODING)
                        container.append(py_text)

            while node != NULL:
                if _is_node_type(node, LXB_DOM_NODE_TYPE_TEXT):
                    text = <unsigned char *> lexbor_str_data_noi(&(<lxb_dom_character_data_t *> node).data)
                    if text != NULL:
                        if not skip_empty or not is_empty_text_node(node):
                            py_text = text.decode(_ENCODING)
                            container.append(py_text)
                node = node.next
            return container.text
        else:
            container = TextContainer(separator, strip)
            if _is_node_type(self.node, LXB_DOM_NODE_TYPE_TEXT):
                text = <unsigned char *> lexbor_str_data_noi(&(<lxb_dom_character_data_t *> self.node).data)
                if text != NULL:
                    if not skip_empty or not self.is_empty_text_node:
                        container.append(text.decode(_ENCODING))

            lxb_dom_node_simple_walk(
                <lxb_dom_node_t *> start_node.node,
                <lxb_dom_node_simple_walker_f> text_callback,
                <void *> container
            )
            return container.text

    cdef inline LexborNode _get_node(self):
        cdef LexborNode node
        if self._is_fragment_root and not _is_node_type(self.node, LXB_DOM_NODE_TYPE_TEXT):
            node = self.parent
        else:
            node = self
        return node

    def css(self, str query):
        """Evaluate CSS selector against current node and its child nodes.

        Matches pattern `query` against HTML tree.
        `CSS selectors reference <https://www.w3schools.com/cssref/css_selectors.asp>`_.

        Special selectors:

         - parser.css('p:lexbor-contains("awesome" i)') -- case-insensitive contains
         - parser.css('p:lexbor-contains("awesome")') -- case-sensitive contains


        Parameters
        ----------
        query : str
            CSS selector (e.g. "div > :nth-child(2n+1):not(:has(a))").

        Returns
        -------
        selector : list of `Node` objects
        """
        return self.parser.selector.find(query, self._get_node())

    def css_first(self, str query, default=None, bool strict=False):
        """Same as `css` but returns only the first match.

        When `strict=False` stops at the first match. Works faster.

        Parameters
        ----------

        query : str
        default : Any, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `LexborNode` object
        """
        if strict:
            results = self.parser.selector.find(query, self._get_node())
        else:
            results = self.parser.selector.find_first(query, self._get_node())
        n_results = len(results)
        if n_results > 0:
            if strict and n_results > 1:
                raise ValueError("Expected 1 match, but found %s matches" % n_results)
            return results[0]
        return default

    def any_css_matches(self, tuple selectors):
        """Returns True if any of CSS selectors matches a node"""
        for selector in selectors:
            if self.parser.selector.any_matches(selector, self):
                return True
        return False

    def css_matches(self, str selector):
        """Returns True if CSS selector matches a node."""
        return bool(self.parser.selector.any_matches(selector, self))

    def __repr__(self):
        return '<LexborNode %s>' % self.tag

    @property
    def tag_id(self):
        cdef lxb_tag_id_t tag_id = lxb_dom_node_tag_id_noi(self.node)
        return tag_id

    @property
    def tag(self):
        """Return the name of the current tag (e.g. div, p, img).

        For for non-tag nodes, returns the following names:

         * `-text` - text node
         * `-document` - document node
         * `-comment` - comment node

        This

        Returns
        -------
        text : str
        """

        cdef lxb_char_t *c_text
        cdef size_t str_len = 0
        if self.tag_id in [LXB_TAG__EM_DOCTYPE, LXB_TAG__TEXT, LXB_TAG__EM_COMMENT]:
            return _TAG_TO_NAME[self.tag_id]
        c_text = lxb_dom_element_qualified_name(<lxb_dom_element_t *> self.node, &str_len)
        text = None
        if c_text:
            text = c_text.decode(_ENCODING)
        return text

    def decompose(self, bool recursive=True):
        """Remove the current node from the tree.

        Parameters
        ----------
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = LexborHTMLParser(html)
        >>> for tag in tree.css('script'):
        >>>     tag.decompose()

        """
        if self.node == <lxb_dom_node_t *> lxb_dom_document_root(&self.parser.document.dom_document):
            raise SelectolaxError("Decomposing the root node is not allowed.")

        if recursive:
            node_remove_deep(<lxb_dom_node_t *> self.node)
        else:
            lxb_dom_node_remove(<lxb_dom_node_t *> self.node)

    def strip_tags(self, list tags, bool recursive = False):
        """Remove specified tags from the HTML tree.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = LexborHTMLParser('<html><head></head><body><script></script><div>Hello world!</div></body></html>')
        >>> tags = ['head', 'style', 'script', 'xmp', 'iframe', 'noembed', 'noframes']
        >>> tree.strip_tags(tags)
        >>> tree.html
        '<html><body><div>Hello world!</div></body></html>'

        """
        cdef LexborNode element
        for tag in tags:
            for element in self.css(tag):
                element.decompose(recursive=recursive)

    @property
    def attributes(self):
        """Get all attributes that belong to the current node.

        The value of empty attributes is None.

        Returns
        -------
        attributes : dictionary of all attributes.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div data id='my_id'></div>")
        >>> node = tree.css_first('div')
        >>> node.attributes
        {'data': None, 'id': 'my_id'}
        """
        cdef lxb_dom_attr_t *attr = lxb_dom_element_first_attribute_noi(<lxb_dom_element_t *> self.node)
        cdef size_t str_len = 0
        attributes = dict()

        if not _is_node_type(self.node, LXB_DOM_NODE_TYPE_ELEMENT):
            return attributes

        while attr != NULL:
            key = lxb_dom_attr_local_name_noi(attr, &str_len)
            value = lxb_dom_attr_value_noi(attr, &str_len)

            if value:
                py_value = value.decode(_ENCODING)
            else:
                py_value = None
            attributes[key.decode(_ENCODING)] = py_value

            attr = attr.next
        return attributes

    @property
    def attrs(self):
        """A dict-like object that is similar to the ``attributes`` property, but operates directly on the Node data.

        .. warning:: Use ``attributes`` instead, if you don't want to modify Node attributes.

        Returns
        -------
        attributes : Attributes mapping object.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div id='a'></div>")
        >>> node = tree.css_first('div')
        >>> node.attrs
        <div attributes, 1 items>
        >>> node.attrs['id']
        'a'
        >>> node.attrs['foo'] = 'bar'
        >>> del node.attrs['id']
        >>> node.attributes
        {'foo': 'bar'}
        >>> node.attrs['id'] = 'new_id'
        >>> node.html
        '<div foo="bar" id="new_id"></div>'
        """
        if not _is_node_type(self.node, LXB_DOM_NODE_TYPE_ELEMENT):
            raise TypeError("attrs is only available for element nodes")
        cdef LexborAttributes attributes = LexborAttributes.create(<lxb_dom_node_t *> self.node)
        return attributes

    @property
    def id(self):
        """Get the id attribute of the node.

        Returns None if id does not set.

        Returns
        -------
        text : str
        """
        cdef char * key = 'id'
        cdef size_t str_len
        cdef lxb_dom_attr_t * attr = lxb_dom_element_attr_by_name(
            <lxb_dom_element_t *> self.node,
            <lxb_char_t *> key, 2
        )
        if attr != NULL:
            value = lxb_dom_attr_value_noi(attr, &str_len)
            return value.decode(_ENCODING) if value else None
        return None

    def iter(self, bool include_text = False, bool skip_empty = False):
        """Iterate over direct children of this node.

        Parameters
        ----------
        include_text : bool, optional
            When ``True``, yield text nodes in addition to element nodes. Defaults
            to ``False``.
        skip_empty : bool, optional
            When ``include_text`` is ``True``, ignore text nodes made up solely
            of ASCII whitespace (space, tab, newline, form feed or carriage
            return). Defaults to ``False``.

        Yields
        ------
        LexborNode
            Child nodes on the same tree level as this node, filtered according
            to the provided options.
        """

        cdef LexborNode start_node = self._get_node()
        cdef lxb_dom_node_t *node = start_node.node.first_child
        cdef LexborNode next_node

        while node != NULL:
            if node.type == LXB_DOM_NODE_TYPE_TEXT and not include_text:
                node = node.next
                continue
            if node.type == LXB_DOM_NODE_TYPE_TEXT and include_text and skip_empty and is_empty_text_node(node):
                node = node.next
                continue

            next_node = LexborNode.new(<lxb_dom_node_t *> node, self.parser)
            yield next_node
            node = node.next

    def __iter__(self):
        return self.iter()

    def __next__(self):
        return self.next

    def unwrap(self, bint delete_empty=False):
        """Replace node with whatever is inside this node.

        Does nothing if you perform unwrapping second time on the same node.

        Parameters
        ----------
        delete_empty : bool, default False
            If True, removes empty tags.

        Examples
        --------

        >>>  tree = LexborHTMLParser("<div>Hello <i>world</i>!</div>")
        >>>  tree.css_first('i').unwrap()
        >>>  tree.html
        '<html><head></head><body><div>Hello world!</div></body></html>'

        Note: by default, empty tags are ignored, use "delete_empty" to change this.
        """
        if self.node.parent == NULL:
            return

        if node_is_removed(<lxb_dom_node_t *> self.node) == 1:
            logger.error("Attempt to unwrap removed node. Does nothing.")
            return

        cdef lxb_dom_node_t * current_node = self.node.first_child
        cdef lxb_dom_node_t * next_node

        if current_node == NULL:
            if delete_empty:
                lxb_dom_node_remove(<lxb_dom_node_t *> self.node)
            return

        while current_node != NULL:
            next_node = current_node.next
            lxb_dom_node_insert_before(self.node, current_node)
            current_node = next_node

        lxb_dom_node_remove(<lxb_dom_node_t *> self.node)

    def unwrap_tags(self, list tags, bint delete_empty = False):
        """Unwraps specified tags from the HTML tree.

        Works the same as the ``unwrap`` method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool, default False
            If True, removes empty tags.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.body.unwrap_tags(['i','a'])
        >>> tree.body.html
        '<body><div>Hello world!</div></body>'

        Note: by default, empty tags are ignored, use "delete_empty" to change this.
        """
        cdef LexborNode element
        for tag in tags:
            if self.node.parent == NULL and not _is_node_type(self.node, LXB_DOM_NODE_TYPE_DOCUMENT):
                break
            for element in self.css(tag):
                element.unwrap(delete_empty)

    def merge_text_nodes(self):
        """Iterates over all text nodes and merges all text nodes that are close to each other.

        This is useful for text extraction.
        Use it when you need to strip HTML tags and merge "dangling" text.

        Examples
        --------

        >>> tree = LexborHTMLParser("<div><p><strong>J</strong>ohn</p><p>Doe</p></div>")
        >>> node = tree.css_first('div')
        >>> tree.unwrap_tags(["strong"])
        >>> tree.text(deep=True, separator=" ", strip=True)
        "J ohn Doe" # Text extraction produces an extra space because the strong tag was removed.
        >>> node.merge_text_nodes()
        >>> tree.text(deep=True, separator=" ", strip=True)
        "John Doe"
        """
        _merge_text_nodes(self.node)

    def traverse(self, bool include_text = False, bool skip_empty = False):
        """Depth-first traversal starting at the current node.

        Parameters
        ----------
        include_text : bool, optional
            When ``True``, include text nodes in the traversal sequence. Defaults
            to ``False``.
        skip_empty : bool, optional
            Skip text nodes that contain only ASCII whitespace (space, tab,
            newline, form feed or carriage return) when ``include_text`` is
            ``True``. Defaults to ``False``.

        Yields
        ------
        LexborNode
            Nodes encountered in depth-first order beginning with the current
            node, filtered according to the provided options.
        """
        cdef lxb_dom_node_t * root = self.node
        cdef lxb_dom_node_t * node = root
        cdef LexborNode lxb_node

        while node != NULL:
            if include_text or node.type != LXB_DOM_NODE_TYPE_TEXT:
                if not skip_empty or not is_empty_text_node(node):
                    lxb_node = LexborNode.new(<lxb_dom_node_t *> node, self.parser)
                    yield lxb_node

            if node.first_child != NULL:
                node = node.first_child
            else:
                while node != root and node.next == NULL:
                    node = node.parent
                if node == root:
                    break
                node = node.next

    def replace_with(self, str_or_LexborNode value):
        """Replace current Node with specified value.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to replace the Node with.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = LexborHTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.replace_with(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get Laptop</div>'

        >>> html_parser = LexborHTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = LexborHTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.replace_with(html_parser2.body.child)
        '<div>Get <span alt="Laptop"><div>Test</div> <div></div></span></div>'
        """
        cdef lxb_dom_node_t * new_node

        if isinstance(value, (str, bytes, unicode)):
            bytes_val = to_bytes(value)
            new_node = <lxb_dom_node_t *> lxb_dom_document_create_text_node(
                &self.parser.document.dom_document,
                <lxb_char_t *> bytes_val, len(bytes_val)
            )
            if new_node == NULL:
                raise SelectolaxError("Can't create a new node")
            lxb_dom_node_insert_before(self.node, new_node)
            lxb_dom_node_remove(<lxb_dom_node_t *> self.node)
        elif isinstance(value, LexborNode):
            new_node = lxb_dom_document_import_node(
                &self.parser.document.dom_document,
                <lxb_dom_node_t *> value.node,
                <bint> True
            )
            if new_node == NULL:
                raise SelectolaxError("Can't create a new node")
            lxb_dom_node_insert_before(self.node, <lxb_dom_node_t *> new_node)
            lxb_dom_node_remove(<lxb_dom_node_t *> self.node)
        else:
            raise SelectolaxError("Expected a string or LexborNode instance, but %s found" % type(value).__name__)

    def insert_before(self, str_or_LexborNode value):
        """
        Insert a node before the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert before the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = LexborHTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.insert_before(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get Laptop<img src="" alt="Laptop"></div>'

        >>> html_parser = LexborHTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = LexborHTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.insert_before(html_parser2.body.child)
        <div>Get <span alt="Laptop"><div>Test</div><img src="/jpg"> <div></div></span></div>'
        """
        cdef lxb_dom_node_t * new_node

        if isinstance(value, (str, bytes, unicode)):
            bytes_val = to_bytes(value)
            new_node = <lxb_dom_node_t *> lxb_dom_document_create_text_node(
                &self.parser.document.dom_document,
                <lxb_char_t *> bytes_val, len(bytes_val)
            )
            if new_node == NULL:
                raise SelectolaxError("Can't create a new node")
            lxb_dom_node_insert_before(self.node, new_node)
        elif isinstance(value, LexborNode):
            new_node = lxb_dom_document_import_node(
                &self.parser.document.dom_document,
                <lxb_dom_node_t *> value.node,
                <bint> True
            )
            if new_node == NULL:
                raise SelectolaxError("Can't create a new node")
            lxb_dom_node_insert_before(self.node, <lxb_dom_node_t *> new_node)
        else:
            raise SelectolaxError("Expected a string or LexborNode instance, but %s found" % type(value).__name__)

    def insert_after(self, str_or_LexborNode value):
        """
        Insert a node after the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert after the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = LexborHTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.insert_after(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get <img src="" alt="Laptop">Laptop</div>'

        >>> html_parser = LexborHTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = LexborHTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.insert_after(html_parser2.body.child)
        <div>Get <span alt="Laptop"><img src="/jpg"><div>Test</div> <div></div></span></div>'
        """
        cdef lxb_dom_node_t * new_node

        if isinstance(value, (str, bytes, unicode)):
            bytes_val = to_bytes(value)
            new_node = <lxb_dom_node_t *> lxb_dom_document_create_text_node(
                &self.parser.document.dom_document,
                <lxb_char_t *> bytes_val, len(bytes_val)
            )
            if new_node == NULL:
                raise SelectolaxError("Can't create a new node")
            lxb_dom_node_insert_after(self.node, new_node)
        elif isinstance(value, LexborNode):
            new_node = lxb_dom_document_import_node(
                &self.parser.document.dom_document,
                <lxb_dom_node_t *> value.node,
                <bint> True
            )
            if new_node == NULL:
                raise SelectolaxError("Can't create a new node")
            lxb_dom_node_insert_after(self.node, <lxb_dom_node_t *> new_node)
        else:
            raise SelectolaxError("Expected a string or LexborNode instance, but %s found" % type(value).__name__)

    def insert_child(self, str_or_LexborNode value):
        """
        Insert a node inside (at the end of) the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert inside the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = LexborHTMLParser('<div>Get <img src=""></div>')
        >>> div = tree.css_first('div')
        >>> div.insert_child('Laptop')
        >>> tree.body.child.html
        '<div>Get <img src="">Laptop</div>'

        >>> html_parser = LexborHTMLParser('<div>Get <span alt="Laptop"> <div>Laptop</div> </span></div>')
        >>> html_parser2 = LexborHTMLParser('<div>Test</div>')
        >>> span_node = html_parser.css_first('span')
        >>> span_node.insert_child(html_parser2.body.child)
        <div>Get <span alt="Laptop"> <div>Laptop</div> <div>Test</div> </span></div>'
        """
        cdef lxb_dom_node_t * new_node

        if isinstance(value, (str, bytes, unicode)):
            bytes_val = to_bytes(value)
            new_node = <lxb_dom_node_t *> lxb_dom_document_create_text_node(
                &self.parser.document.dom_document,
                <lxb_char_t *> bytes_val, len(bytes_val)
            )
            if new_node == NULL:
                raise SelectolaxError("Can't create a new node")
            lxb_dom_node_insert_child(self.node, new_node)
        elif isinstance(value, LexborNode):
            new_node = lxb_dom_document_import_node(
                &self.parser.document.dom_document,
                <lxb_dom_node_t *> value.node,
                <bint> True
            )
            if new_node == NULL:
                raise SelectolaxError("Can't create a new node")
            lxb_dom_node_insert_child(self.node, <lxb_dom_node_t *> new_node)
        else:
            raise SelectolaxError("Expected a string or LexborNode instance, but %s found" % type(value).__name__)

    @property
    def raw_value(self):
        """Return the raw (unparsed, original) value of a node.

        Currently, works on text nodes only.

        Returns
        -------

        raw_value : bytes

        Examples
        --------

        >>> html_parser = LexborHTMLParser('<div>&#x3C;test&#x3E;</div>')
        >>> selector = html_parser.css_first('div')
        >>> selector.child.html
        '&lt;test&gt;'
        >>> selector.child.raw_value
        b'&#x3C;test&#x3E;'
        """
        raise NotImplementedError("This features is not supported by the lexbor backend. Please use Modest backend.")

    def scripts_contain(self, str query):
        """Returns True if any of the script tags contain specified text.

        Caches script tags on the first call to improve performance.

        Parameters
        ----------
        query : str
            The query to check.

        """
        cdef LexborNode node
        if self.parser.cached_script_texts is None:
            nodes = self.parser.selector.find('script', self)
            text_nodes = []
            for node in nodes:
                node_text = node.text(deep=True)
                if node_text:
                    text_nodes.append(node_text)
            self.parser.cached_script_texts = text_nodes

        for text in self.parser.cached_script_texts:
            if query in text:
                return True
        return False

    def script_srcs_contain(self, tuple queries):
        """Returns True if any of the script SRCs attributes contain on of the specified text.

        Caches values on the first call to improve performance.

        Parameters
        ----------
        queries : tuple of str

        """
        cdef LexborNode node
        if self.parser.cached_script_srcs is None:
            nodes = self.parser.selector.find('script', self)
            src_nodes = []
            for node in nodes:
                node_src = node.attrs.get('src')
                if node_src:
                    src_nodes.append(node_src)
            self.parser.cached_script_srcs = src_nodes

        for text in self.parser.cached_script_srcs:
            for query in queries:
                if query in text:
                    return True
        return False

    def remove(self, bool recursive=True):
        """An alias for the decompose method."""
        self.decompose(recursive)

    def select(self, query=None):
        """Select nodes given a CSS selector.

        Works similarly to the the ``css`` method, but supports chained filtering and extra features.

        Parameters
        ----------
        query : str or None
            The CSS selector to use when searching for nodes.

        Returns
        -------
        selector : The `Selector` class.
        """
        return LexborSelector(self._get_node(), query)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.html == other
        if not isinstance(other, LexborNode):
            return False
        return self.html == other.html

    @property
    def text_content(self):
        """Returns the text of the node if it is a text node.

        Returns None for other nodes.
        Unlike the ``text`` method, does not include child nodes.

        Returns
        -------
        text : str or None.
        """
        cdef unsigned char * text
        cdef lxb_dom_node_t * node = <lxb_dom_node_t *> self.node.first_child
        cdef TextContainer container
        if not _is_node_type(self.node, LXB_DOM_NODE_TYPE_TEXT):
            return None

        text = <unsigned char *> lexbor_str_data_noi(&(<lxb_dom_character_data_t *> self.node).data)
        if text != NULL:
            container = TextContainer.new_with_defaults()
            py_text = text.decode(_ENCODING)
            container.append(py_text)
            return container.text
        return None

    @property
    def comment_content(self) -> str | None:
        """Extract the textual content of an HTML comment node.

        Returns
        -------
        str or None
            Comment text with surrounding whitespace removed, or ``None`` if
            the current node is not a comment or the comment markup cannot be
            parsed.

        Examples
        --------
        >>> parse_fragment("<!-- hello -->")[0].comment_content
        'hello'
        >>> parse_fragment("<div>not a comment</div>")[0].comment_content is None
        True
        """
        if not self.is_comment_node:
            return None
        try:
            return extract_html_comment(self.html)
        except (ValueError, AttributeError, IndexError):
            return None

    @property
    def inner_html(self) -> str | None:
        """Return HTML representation of the child nodes.

        Works similar to innerHTML in JavaScript.
        Unlike the `.html` property, does not include the current node.
        Can be used to set HTML as well. See the setter docstring.

        Returns
        -------
        text : str | None
        """

        return self._serialize_inner_html(LXB_HTML_SERIALIZE_OPT_UNDEF, 0, False)

    @inner_html.setter
    def inner_html(self, str html) -> None:
        """Set inner HTML to the specified HTML.

        Replaces existing data inside the node.
        Works similar to innerHTML in JavaScript.

        Parameters
        ----------
        html : str | None

        """
        cdef bytes bytes_val
        bytes_val = <bytes> html.encode("utf-8")
        lxb_html_element_inner_html_set(
            <lxb_html_element_t *> self.node,
            <lxb_char_t *> bytes_val, len(bytes_val)
        )

    def clone(self) -> LexborNode:
        """Clone the current node.

        You can use to do temporary modifications without affecting the original HTML tree.

        It is tied to the current parser instance.
        Gets destroyed when parser instance is destroyed.
        """
        cdef lxb_dom_node_t * node
        node = lxb_dom_node_clone(<lxb_dom_node_t *> self.node, 1)
        return LexborNode.new(node, self.parser)

    @property
    def is_element_node(self) -> bool:
        """Return True if the node represents an element node."""
        return _is_node_type(self.node, LXB_DOM_NODE_TYPE_ELEMENT)

    @property
    def is_text_node(self) -> bool:
        """Return True if the node represents a text node."""
        return _is_node_type(self.node, LXB_DOM_NODE_TYPE_TEXT)

    @property
    def is_comment_node(self) -> bool:
        """Return True if the node represents a comment node."""
        return _is_node_type(self.node, LXB_DOM_NODE_TYPE_COMMENT)

    @property
    def is_document_node(self) -> bool:
        """Return True if the node represents a document node."""
        return _is_node_type(self.node, LXB_DOM_NODE_TYPE_DOCUMENT)

    @property
    def is_empty_text_node(self) -> bool:
        """Check whether the current node is an empty text node.

        Returns
        -------
        bool
            ``True`` when the node is a text node whose character data consists
            only of ASCII whitespace characters (space, tab, newline, form feed
            or carriage return).
        """
        return is_empty_text_node(self.node)


@cython.internal
@cython.final
cdef class TextContainer:
    cdef list _parts
    cdef str separator
    cdef bint strip

    @staticmethod
    cdef TextContainer new_with_defaults():
        cdef TextContainer cls = TextContainer.__new__(TextContainer)
        cls._parts = []
        cls.separator = ''
        cls.strip = False
        return cls

    def __init__(self, str separator = '', bool strip = False):
        self._parts = []
        self.separator = separator
        self.strip = strip

    def append(self, str node_text):
        if self.strip:
            self._parts.append(node_text.strip())
        else:
            self._parts.append(node_text)

    @property
    def text(self):
        return self.separator.join(self._parts)

cdef lexbor_action_t text_callback(lxb_dom_node_t *node, void *ctx):
    cdef unsigned char *text
    cdef lxb_tag_id_t tag_id = lxb_dom_node_tag_id_noi(node)
    if tag_id != LXB_TAG__TEXT:
        return LEXBOR_ACTION_OK

    text = <unsigned char *> lexbor_str_data_noi(&(<lxb_dom_text_t *> node).char_data.data)
    if not text:
        return LEXBOR_ACTION_OK

    try:
        py_str = text.decode(_ENCODING, "replace")

    except Exception as e:
        PyErr_SetNone(e)
        return LEXBOR_ACTION_STOP

    cdef TextContainer cls
    cls = <TextContainer> ctx
    cls.append(py_str)
    return LEXBOR_ACTION_OK

cdef lxb_status_t serialize_fragment(lxb_dom_node_t *node, lexbor_str_t *lxb_str):
    cdef lxb_status_t status
    while node != NULL:
        status = lxb_html_serialize_tree_str(node, lxb_str)
        if status != LXB_STATUS_OK:
            return status
        node = node.next

    return LXB_STATUS_OK


cdef lxb_status_t serialize_fragment_pretty(
    lxb_dom_node_t *node,
    lexbor_str_t *lxb_str,
    lxb_html_serialize_opt_t options,
    size_t indent,
):
    cdef lxb_status_t status
    while node != NULL:
        status = lxb_html_serialize_pretty_tree_str(node, options, indent, lxb_str)
        if status != LXB_STATUS_OK:
            return status
        node = node.next

    return LXB_STATUS_OK


cdef inline lxb_html_serialize_opt_t _html_pretty_options(
    bint skip_ws_nodes,
    bint skip_comment,
    bint raw,
    bint without_closing,
    bint tag_with_ns,
    bint without_text_indent,
    bint full_doctype,
    bint html5test,
):
    cdef lxb_html_serialize_opt_t options = LXB_HTML_SERIALIZE_OPT_UNDEF

    if skip_ws_nodes:
        options = <lxb_html_serialize_opt_t> (options | LXB_HTML_SERIALIZE_OPT_SKIP_WS_NODES)
    if skip_comment:
        options = <lxb_html_serialize_opt_t> (options | LXB_HTML_SERIALIZE_OPT_SKIP_COMMENT)
    if raw:
        options = <lxb_html_serialize_opt_t> (options | LXB_HTML_SERIALIZE_OPT_RAW)
    if without_closing:
        options = <lxb_html_serialize_opt_t> (options | LXB_HTML_SERIALIZE_OPT_WITHOUT_CLOSING)
    if tag_with_ns:
        options = <lxb_html_serialize_opt_t> (options | LXB_HTML_SERIALIZE_OPT_TAG_WITH_NS)
    if without_text_indent:
        options = <lxb_html_serialize_opt_t> (options | LXB_HTML_SERIALIZE_OPT_WITHOUT_TEXT_INDENT)
    if full_doctype:
        options = <lxb_html_serialize_opt_t> (options | LXB_HTML_SERIALIZE_OPT_FULL_DOCTYPE)
    if html5test:
        options = <lxb_html_serialize_opt_t> (options | 0x80)

    return options

cdef inline bint _is_node_type(lxb_dom_node_t *node, lxb_dom_node_type_t expected_type):
    return node != NULL and node.type == expected_type

cdef void _merge_text_nodes(lxb_dom_node_t *root):
    if root == NULL or node_is_removed(root):
        return

    cdef lxb_dom_node_t *node
    cdef lxb_dom_node_t *next_node
    cdef lxb_dom_text_t *new_text_node
    cdef lxb_char_t *left_text
    cdef lxb_char_t *right_text
    cdef size_t left_length, right_length
    cdef bytes combined

    cdef bint changed = 1
    while changed:
        changed = 0
        node = root.first_child
        while node != NULL:
            next_node = node.next
            if node.type == LXB_DOM_NODE_TYPE_TEXT and next_node != NULL and next_node.type == LXB_DOM_NODE_TYPE_TEXT:
                left_text = lxb_dom_node_text_content(node, &left_length)
                right_text = lxb_dom_node_text_content(next_node, &right_length)

                if left_text != NULL and right_text != NULL:
                    combined = (<bytes>left_text[:left_length]) + (<bytes>right_text[:right_length])
                    new_text_node = lxb_dom_document_create_text_node(
                        root.owner_document,
                        <lxb_char_t *>combined,
                        len(combined)
                    )
                    if new_text_node != NULL:
                        lxb_dom_node_insert_before(node, <lxb_dom_node_t *>new_text_node)
                        lxb_dom_node_remove(node)
                        lxb_dom_node_remove(next_node)
                        changed = 1
                        break

            node = next_node

    node = root.first_child
    while node != NULL:
        if node.type == LXB_DOM_NODE_TYPE_ELEMENT and node.first_child:
            _merge_text_nodes(node)
        node = node.next

```

### `selectolax/lexbor/selection.pxi`

```pxi
cimport cython
from cpython.exc cimport PyErr_SetObject
from cpython.list cimport PyList_GET_SIZE


@cython.final
cdef class LexborCSSSelector:

    def __init__(self):
        self._create_css_parser()
        self.results = []
        self.current_node = None

    cdef int _create_css_parser(self) except -1:
        cdef lxb_status_t status

        self.parser = lxb_css_parser_create()
        if self.parser == NULL:
            PyErr_SetObject(SelectolaxError, "Can't create CSS parser.")
            return -1

        status = lxb_css_parser_init(self.parser, NULL)
        if status != LXB_STATUS_OK:
            lxb_css_parser_destroy(self.parser, True)
            self.parser = NULL
            PyErr_SetObject(SelectolaxError, "Can't initialize CSS parser.")
            return -1

        self.css_selectors = lxb_css_selectors_create()
        if self.css_selectors == NULL:
            lxb_css_parser_destroy(self.parser, True)
            self.parser = NULL
            PyErr_SetObject(SelectolaxError, "Can't create CSS selector.")
            return -1

        status = lxb_css_selectors_init(self.css_selectors)
        if status != LXB_STATUS_OK:
            lxb_css_selectors_destroy(self.css_selectors, True)
            self.css_selectors = NULL
            lxb_css_parser_destroy(self.parser, True)
            self.parser = NULL
            PyErr_SetObject(SelectolaxError, "Can't initialize CSS selector.")
            return -1

        lxb_css_parser_selectors_set(self.parser, self.css_selectors)

        self.selectors = lxb_selectors_create()
        if self.selectors == NULL:
            lxb_css_selectors_destroy(self.css_selectors, True)
            self.css_selectors = NULL
            lxb_css_parser_destroy(self.parser, True)
            self.parser = NULL
            PyErr_SetObject(SelectolaxError, "Can't create selector.")
            return -1

        status = lxb_selectors_init(self.selectors)
        if status != LXB_STATUS_OK:
            lxb_selectors_destroy(self.selectors, True)
            self.selectors = NULL
            lxb_css_selectors_destroy(self.css_selectors, True)
            self.css_selectors = NULL
            lxb_css_parser_destroy(self.parser, True)
            self.parser = NULL
            PyErr_SetObject(SelectolaxError, "Can't initialize selector.")
            return -1

        lxb_selectors_opt_set(self.selectors, LXB_SELECTORS_OPT_MATCH_ROOT)
        return 0

    cpdef list find(self, str query, LexborNode node):
        return self._find(query, node, 0)

    cpdef list find_first(self, str query, LexborNode node):
        return self._find(query, node, 1)

    cpdef list _find(self, str query, LexborNode node, bint only_first):
        cdef lxb_css_selector_list_t* selectors
        cdef lxb_char_t* c_selector
        cdef lxb_css_selector_list_t * selectors_list

        if not isinstance(query, str):
            raise TypeError("Query must be a string.")

        bytes_query = query.encode(_ENCODING)
        selectors_list = lxb_css_selectors_parse(self.parser, <lxb_char_t *> bytes_query, <size_t>len(bytes_query))

        if selectors_list == NULL:
            raise SelectolaxError("Can't parse CSS selector.")

        self.current_node = node
        self.results = []
        if only_first:
            status = lxb_selectors_find(self.selectors, node.node, selectors_list,
                                        <lxb_selectors_cb_f>css_finder_callback_first, <void*>self)
        else:
            status = lxb_selectors_find(self.selectors, node.node, selectors_list,
                                        <lxb_selectors_cb_f>css_finder_callback, <void*>self)
        results = list(self.results)
        self.results = []
        self.current_node = None
        lxb_css_selector_list_destroy_memory(selectors_list)
        self.parser.memory = NULL
        return results

    cpdef int any_matches(self, str query, LexborNode node) except -1:
        cdef lxb_css_selector_list_t * selectors
        cdef lxb_char_t * c_selector
        cdef lxb_css_selector_list_t * selectors_list
        cdef int result

        if not isinstance(query, str):
            raise TypeError("Query must be a string.")

        bytes_query = query.encode(_ENCODING)
        selectors_list = lxb_css_selectors_parse(self.parser, <lxb_char_t *> bytes_query, <size_t> len(bytes_query))

        if selectors_list == NULL:
            PyErr_SetObject(SelectolaxError, "Can't parse CSS selector.")
            return -1

        self.results = []
        status = lxb_selectors_find(self.selectors, node.node, selectors_list,
                                    <lxb_selectors_cb_f> css_matcher_callback, <void *> self)
        if status != LXB_STATUS_OK:
            lxb_css_selector_list_destroy_memory(selectors_list)
            self.parser.memory = NULL
            PyErr_SetObject(SelectolaxError, "Can't parse CSS selector.")
            return -1

        result = PyList_GET_SIZE(self.results) > 0
        self.results = []
        lxb_css_selector_list_destroy_memory(selectors_list)
        self.parser.memory = NULL
        return result

    def __dealloc__(self):
        if self.selectors != NULL:
            lxb_selectors_destroy(self.selectors, True)
        if self.parser != NULL:
            lxb_css_parser_destroy(self.parser, True)
        if self.css_selectors != NULL:
            lxb_css_selectors_destroy(self.css_selectors, True)


cdef class LexborSelector:
    """An advanced CSS selector that supports additional operations.

    Think of it as a toolkit that mimics some of the features of XPath.

    Please note, this is an experimental feature that can change in the future.
    """
    cdef LexborNode node
    cdef list nodes

    def __init__(self, LexborNode node, query):
        self.node = node
        self.nodes = self.node.parser.selector.find(query, self.node) if query else [node, ]

    cpdef css(self, str query):
        """Evaluate CSS selector against current scope."""
        raise NotImplementedError("This features is not supported by the lexbor backend. Please use Modest backend.")

    @property
    def matches(self) -> list:
        """Returns all possible matches"""
        return self.nodes

    @property
    def any_matches(self) -> bool:
        """Returns True if there are any matches"""
        return bool(self.nodes)

    def text_contains(self, str text, bool deep=True, str separator='', bool strip=False) -> LexborSelector:
        """Filter all current matches given text."""
        cdef list nodes = []
        for node in self.nodes:
            node_text = node.text(deep=deep, separator=separator, strip=strip)
            if node_text and text in node_text:
                nodes.append(node)
        self.nodes = nodes
        return self

    def any_text_contains(self, str text, bool deep=True, str separator='', bool strip=False) -> bool:
        """Returns True if any node in the current search scope contains specified text"""
        cdef LexborNode node
        for node in self.nodes:
            node_text = node.text(deep=deep, separator=separator, strip=strip)
            if node_text and text in node_text:
                return True
        return False

    def attribute_longer_than(self, str attribute, int length, str start  = None) -> LexborSelector:
        """Filter all current matches by attribute length.

        Similar to `string-length` in XPath.
        """
        cdef list nodes = []
        for node in self.nodes:
            attr = node.attributes.get(attribute)
            if not attr:
                continue
            if attr and start and start in attr:
                attr = attr[attr.find(start) + len(start):]
            if len(attr) > length:
                nodes.append(node)
        self.nodes = nodes
        return self

    def any_attribute_longer_than(self, str attribute, int length, str start  = None) -> bool:
        """Returns True any href attribute longer than a specified length.

        Similar to `string-length` in XPath.
        """
        cdef LexborNode node
        for node in self.nodes:
            attr = node.attributes.get(attribute)
            if attr is None:
                continue
            if start and start in attr:
                attr = attr[attr.find(start) + len(start):]
            if len(attr) > length:
                return True
        return False

    def __bool__(self):
        return bool(self.nodes)


cdef lxb_status_t css_finder_callback(lxb_dom_node_t *node, lxb_css_selector_specificity_t *spec, void *ctx):
    cdef LexborNode lxb_node
    cdef LexborCSSSelector cls
    cls = <LexborCSSSelector> ctx
    lxb_node = LexborNode.new(<lxb_dom_node_t *> node, cls.current_node.parser)
    cls.results.append(lxb_node)
    return LXB_STATUS_OK

cdef lxb_status_t css_finder_callback_first(lxb_dom_node_t *node, lxb_css_selector_specificity_t *spec, void *ctx):
    cdef LexborNode lxb_node
    cdef LexborCSSSelector cls
    cls = <LexborCSSSelector> ctx
    lxb_node = LexborNode.new(<lxb_dom_node_t *> node, cls.current_node.parser)
    cls.results.append(lxb_node)
    return LXB_STATUS_STOP


cdef lxb_status_t css_matcher_callback(lxb_dom_node_t *node, lxb_css_selector_specificity_t *spec, void *ctx):
    cdef LexborNode lxb_node
    cdef LexborCSSSelector cls
    cls = <LexborCSSSelector> ctx
    cls.results.append(True)
    return LXB_STATUS_STOP

```

### `selectolax/lexbor/util.pxi`

```pxi
include "../utils.pxi"

import re


def create_tag(tag: str):
    """
    Given an HTML tag name, e.g. `"div"`, create a single empty node for that tag,
    e.g. `"<div></div>"`.

    Use `LexborHTMLParser().create_node(..)` if you need to create a node tied to a specific parser instance.
    """
    return LexborHTMLParser(f"<{tag}></{tag}>", is_fragment=True).root


def parse_fragment(html: str):
    """
    Given HTML, parse it into a list of Nodes, such that the nodes
    correspond to the given HTML.

    For contrast, HTMLParser adds `<html>`, `<head>`, and `<body>` tags
    if they are missing. This function does not add these tags.
    """
    return do_parse_fragment(html, LexborHTMLParser)


def extract_html_comment(text: str) -> str:
    """Extract the inner content of an HTML comment string.

    Args:
        text: Raw HTML comment, including the ``<!--`` and ``-->`` markers.

    Returns:
        The comment body with surrounding whitespace stripped.

    Raises:
        ValueError: If the input is not a well-formed HTML comment.

    Examples:
        >>> extract_html_comment("<!-- hello -->")
        'hello'
    """
    if match := re.fullmatch(r"\s*<!--\s*(.*?)\s*-->\s*", text, flags=re.DOTALL):
        return match.group(1).strip()
    msg = "Input is not a valid HTML comment"
    raise ValueError(msg)


cdef inline bint is_empty_text_node(lxb_dom_node_t *text_node):
    """
    Check whether a node is a text node made up solely of HTML ASCII whitespace.

    Parameters
    ----------
    text_node : lxb_dom_node_t *
        Pointer to the node that should be inspected.

    Returns
    -------
    bint
        ``True`` if ``text_node`` is a text node whose character data contains
        only space, tab, newline, form feed, or carriage return characters;
        otherwise ``False``.
    """
    if text_node == NULL or text_node.type != LXB_DOM_NODE_TYPE_TEXT:
        return False

    cdef lxb_dom_character_data_t *text_character_data = <lxb_dom_character_data_t *> text_node
    cdef lexbor_str_t *text_buffer = &text_character_data.data
    cdef size_t text_length = text_buffer.length
    cdef lxb_char_t *text_bytes = text_buffer.data

    return _is_whitespace_only(text_bytes, text_length)


cdef inline bint _is_whitespace_only(const lxb_char_t *buffer, size_t buffer_length) nogil:
    """
    Determine whether a byte buffer consists only of HTML ASCII whitespace.

    Parameters
    ----------
    buffer : const lxb_char_t *
        Pointer to the buffer to inspect.
    buffer_length : size_t
        Number of bytes available in ``buffer``.

    Returns
    -------
    bint
        ``True`` if ``buffer`` is ``NULL``, empty, or contains only space
        (0x20), tab (0x09), line feed (0x0A), form feed (0x0C), or carriage
        return (0x0D) bytes; otherwise ``False``.

    Notes
    -----
    Mirrors Lexbor's ``lexbor_utils_whitespace`` macro and stays inline to
    keep the GIL released in hot loops.
    """
    cdef const lxb_char_t *cursor = buffer
    cdef const lxb_char_t *end = buffer + buffer_length
    cdef lxb_char_t current_char

    if buffer == NULL or buffer_length == 0:
        return True

    # Inline whitespace check mirroring lexbor_utils_whitespace(chr, !=, &&)
    while cursor < end:
        current_char = cursor[0]
        if (current_char != ' ' and current_char != '\t' and current_char != '\n'
                and current_char != '\f' and current_char != '\r'):
            return False
        cursor += 1

    return True

```

### `selectolax/modest/node.pxi`

```pxi
cimport cython
from cpython.exc cimport PyErr_NoMemory

from libc.stdlib cimport free
from libc.stdlib cimport malloc
from libc.stdlib cimport realloc
from libc.string cimport memcpy

DEF _STACK_SIZE = 100
DEF _ENCODING = 'UTF-8'


@cython.final
@cython.internal
cdef class Stack:
    def __cinit__(self, size_t capacity=25):
        self.capacity = capacity
        self.top = 0
        self._stack = <myhtml_tree_node_t**> malloc(capacity * sizeof(myhtml_tree_node_t))
        if self._stack == NULL:
            raise MemoryError("Failed to allocate memory for stack")

    def __dealloc__(self):
        free(self._stack)

    cdef bint is_empty(self):
        return self.top <= 0

    cdef int push(self, myhtml_tree_node_t* res) except -1:
        if self.top >= self.capacity:
            if self.resize() < 0:
                return -1
        self._stack[self.top] = res
        self.top += 1

    cdef myhtml_tree_node_t * pop(self):
        self.top = self.top - 1
        return self._stack[self.top]

    cdef int resize(self) except -1:
        self.capacity *= 2
        self._stack = <myhtml_tree_node_t**> realloc(<void*> self._stack, self.capacity * sizeof(myhtml_tree_node_t))
        if self._stack == NULL:
            PyErr_NoMemory()
            return -1
        return 0

cdef class _Attributes:
    """A dict-like object that represents attributes."""
    cdef myhtml_tree_node_t * node
    cdef unicode decode_errors

    @staticmethod
    cdef _Attributes create(myhtml_tree_node_t *node, unicode decode_errors):
        obj = <_Attributes>_Attributes.__new__(_Attributes)
        obj.node = node
        obj.decode_errors = decode_errors
        return obj

    def __iter__(self):
        cdef myhtml_tree_attr_t *attr = myhtml_node_attribute_first(self.node)
        while attr:
            if attr.key.data == NULL:
                attr = attr.next
                continue
            key = attr.key.data.decode(_ENCODING, self.decode_errors)
            attr = attr.next
            yield key

    def __setitem__(self, str key, value):
        value = str(value)
        bytes_key = key.encode(_ENCODING)
        bytes_value = value.encode(_ENCODING)
        myhtml_attribute_remove_by_key(self.node, <char*>bytes_key, len(bytes_key))
        myhtml_attribute_add(self.node, <char*>bytes_key, len(bytes_key), <char*>bytes_value, len(bytes_value),
                             MyENCODING_UTF_8)

    def __delitem__(self, key):
        try:
            self.__getitem__(key)
        except KeyError:
            raise KeyError(key)
        bytes_key = key.encode(_ENCODING)
        myhtml_attribute_remove_by_key(self.node, <char*>bytes_key, len(bytes_key))

    def __getitem__(self, str key):
        bytes_key = key.encode(_ENCODING)
        cdef myhtml_tree_attr_t * attr =  myhtml_attribute_by_key(self.node, <char*>bytes_key, len(bytes_key))
        if attr != NULL:
            if attr.value.data != NULL:
                return attr.value.data.decode(_ENCODING, self.decode_errors)
            elif attr.key.data != NULL:
                return None
        raise KeyError(key)

    def __len__(self):
        return len(list(self.__iter__()))

    def keys(self):
        return self.__iter__()

    def items(self):
        for key in self.__iter__():
            yield key, self[key]

    def values(self):
        for key in self.__iter__():
            yield self[key]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def sget(self, key, default=""):
        """Same as get, but returns empty strings instead of None values for empty attributes."""
        try:
            val = self[key]
            if val is None:
                val = ""
            return val
        except KeyError:
            return default

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __repr__(self):
        cdef const char *c_text
        c_text = myhtml_tag_name_by_id(self.node.tree, self.node.tag_id, NULL)
        tag_name = c_text.decode(_ENCODING, 'ignore') if c_text != NULL else 'unknown'
        return "<%s attributes, %s items>" % (tag_name, len(self))

ctypedef fused str_or_Node:
    str
    bytes
    Node

cdef class Node:
    """A class that represents HTML node (element)."""
    cdef myhtml_tree_node_t *node
    cdef public HTMLParser parser

    @staticmethod
    cdef Node new(myhtml_tree_node_t *node, HTMLParser parser):
        # custom __init__ for C, because __cinit__ doesn't accept C types
        cdef Node cls = Node.__new__(Node)
        cls.node = node
        # Keep reference to the selector object, so myhtml structures will not be garbage collected prematurely
        cls.parser = parser
        return cls

    @property
    def attributes(self):
        """Get all attributes that belong to the current node.

        The value of empty attributes is None.

        Returns
        -------
        attributes : dictionary of all attributes.

        Examples
        --------

        >>> tree = HTMLParser("<div data id='my_id'></div>")
        >>> node = tree.css_first('div')
        >>> node.attributes
        {'data': None, 'id': 'my_id'}
        """
        cdef myhtml_tree_attr_t *attr = myhtml_node_attribute_first(self.node)
        attributes = dict()

        while attr:
            if attr.key.data == NULL:
                attr = attr.next
                continue
            key = attr.key.data.decode(_ENCODING, self.parser.decode_errors)
            if attr.value.data:
                value = attr.value.data.decode(_ENCODING, self.parser.decode_errors)
            else:
                value = None
            attributes[key] = value

            attr = attr.next

        return attributes

    @property
    def attrs(self):
        """A dict-like object that is similar to the ``attributes`` property, but operates directly on the Node data.

        .. warning:: Use ``attributes`` instead, if you don't want to modify Node attributes.

        Returns
        -------
        attributes : Attributes mapping object.

        Examples
        --------

        >>> tree = HTMLParser("<div id='a'></div>")
        >>> node = tree.css_first('div')
        >>> node.attrs
        <div attributes, 1 items>
        >>> node.attrs['id']
        'a'
        >>> node.attrs['foo'] = 'bar'
        >>> del node.attrs['id']
        >>> node.attributes
        {'foo': 'bar'}
        >>> node.attrs['id'] = 'new_id'
        >>> node.html
        '<div foo="bar" id="new_id"></div>'
        """
        cdef _Attributes attributes = _Attributes.create(self.node, self.parser.decode_errors)
        return attributes

    @property
    def mem_id(self):
        """Get the mem_id attribute of the node.

        Returns
        -------
        text : int
        """
        return <size_t> self.node

    @property
    def id(self):
        """Get the id attribute of the node.

        Returns None if id does not set.

        Returns
        -------
        text : str
        """
        cdef char* key = 'id'
        cdef myhtml_tree_attr_t *attr
        attr = myhtml_attribute_by_key(self.node, key, 2)
        return None if attr == NULL else attr.value.data.decode(_ENCODING, self.parser.decode_errors)

    def __hash__(self):
        return self.mem_id

    def text(self, bool deep=True, str separator='', bool strip=False):
        """Returns the text of the node including text of all its child nodes.

        Parameters
        ----------
        strip : bool, default False
            If true, calls ``str.strip()`` on each text part to remove extra white spaces.
        separator : str, default ''
            The separator to use when joining text from different nodes.
        deep : bool, default True
            If True, includes text from all child nodes.

        Returns
        -------
        text : str

        """
        cdef const char* c_text
        cdef myhtml_tree_node_t *node = self.node.child
        cdef list parts = []

        if not deep:
            if self.node.tag_id == MyHTML_TAG__TEXT:
                c_text = myhtml_node_text(self.node, NULL)
                if c_text != NULL:
                    node_text = c_text.decode(_ENCODING, self.parser.decode_errors)
                    parts.append(node_text.strip() if strip else node_text)

            while node != NULL:
                if node.tag_id == MyHTML_TAG__TEXT:
                    c_text = myhtml_node_text(node, NULL)
                    if c_text != NULL:
                        node_text = c_text.decode(_ENCODING, self.parser.decode_errors)
                        parts.append(node_text.strip() if strip else node_text)
                node = node.next
        else:
            self._text_deep(self.node, parts, strip)
        return separator.join(parts)

    cdef inline _text_deep(self, myhtml_tree_node_t *node, list parts, bint strip):
        cdef Stack stack = Stack(_STACK_SIZE)
        cdef myhtml_tree_node_t* current_node = NULL
        cdef const char* c_text

        if node.tag_id == MyHTML_TAG__TEXT:
            c_text = myhtml_node_text(node, NULL)
            if c_text != NULL:
                node_text = c_text.decode(_ENCODING, self.parser.decode_errors)
                parts.append(node_text.strip() if strip else node_text)

        if node.child == NULL:
            return

        stack.push(node.child)

        # Depth-first left-to-right tree traversal
        while not stack.is_empty():
            current_node = stack.pop()

            if current_node != NULL:
                if current_node.tag_id == MyHTML_TAG__TEXT:
                    c_text = myhtml_node_text(current_node, NULL)
                    if c_text != NULL:
                        node_text = c_text.decode(_ENCODING, self.parser.decode_errors)
                        parts.append(node_text.strip() if strip else node_text)

            if current_node.next is not NULL:
                stack.push(current_node.next)

            if current_node.child is not NULL:
                stack.push(current_node.child)

    def iter(self, include_text=False):
        """Iterate over nodes on the current level.

        Parameters
        ----------
        include_text : bool
            If True, includes text nodes as well.

        Yields
        -------
        node
        """

        cdef myhtml_tree_node_t *node = self.node.child
        cdef Node next_node

        while node != NULL:
            if node.tag_id == MyHTML_TAG__TEXT and not include_text:
                node = node.next
                continue

            next_node = Node.new(node, self.parser)
            yield next_node
            node = node.next

    def traverse(self, include_text=False):
        """Iterate over all child and next nodes starting from the current level.

        Parameters
        ----------
        include_text : bool
            If True, includes text nodes as well.

        Yields
        -------
        node
        """
        cdef Stack stack = Stack(_STACK_SIZE)
        cdef myhtml_tree_node_t* current_node = NULL
        cdef Node next_node

        stack.push(self.node)

        while not stack.is_empty():
            current_node = stack.pop()
            if current_node != NULL and not (current_node.tag_id == MyHTML_TAG__TEXT and not include_text):
                next_node = Node.new(current_node, self.parser)
                yield next_node

            if current_node.next is not NULL:
                stack.push(current_node.next)

            if current_node.child is not NULL:
                stack.push(current_node.child)

    @property
    def tag(self):
        """Return the name of the current tag (e.g. div, p, img).

        Returns
        -------
        text : str
        """
        cdef const char *c_text
        c_text = myhtml_tag_name_by_id(self.node.tree, self.node.tag_id, NULL)
        text = None
        if c_text:
            text = c_text.decode(_ENCODING, self.parser.decode_errors)
        return text

    @property
    def child(self):
        """Alias for the `first_child` property.

        **Deprecated**. Please use `first_child` instead.
        """
        cdef Node node
        if self.node.child:
            node = Node.new(self.node.child, self.parser)
            return node
        return None

    @property
    def parent(self):
        """Return the parent node."""
        cdef Node node
        if self.node.parent:
            node = Node.new(self.node.parent, self.parser)
            return node
        return None

    @property
    def next(self):
        """Return next node."""
        cdef Node node
        if self.node.next:
            node = Node.new(self.node.next, self.parser)
            return node
        return None

    @property
    def prev(self):
        """Return previous node."""
        cdef Node node
        if self.node.prev:
            node = Node.new(self.node.prev, self.parser)
            return node
        return None

    @property
    def last_child(self):
        """Return last child node."""
        cdef Node node
        if self.node.last_child:
            node = Node.new(self.node.last_child, self.parser)
            return node
        return None

    @property
    def html(self):
        """Return HTML representation of the current node including all its child nodes.

        Returns
        -------
        text : str
        """
        cdef mycore_string_raw_t c_str
        c_str.data = NULL
        c_str.length = 0
        c_str.size = 0

        cdef mystatus_t status
        status = myhtml_serialization(self.node, &c_str)

        if status == 0 and c_str.data:
            html = c_str.data.decode(_ENCODING).replace('<-undef>', '')
            free(c_str.data)
            return html

        return None

    def css(self, str query):
        """Evaluate CSS selector against current node and its child nodes."""
        return find_nodes(self.parser, self.node, query)

    def any_css_matches(self, tuple selectors):
        """Returns True if any of CSS selectors matches a node"""
        return find_matches(self.parser, self.node, selectors)

    def css_matches(self, str selector):
        """Returns True if CSS selector matches a node."""
        return find_matches(self.parser, self.node, (selector, ))

    def css_first(self, str query, default=None, bool strict=False):
        """Evaluate CSS selector against current node and its child nodes."""
        results = self.css(query)
        n_results = len(results)

        if n_results > 0:

            if strict and n_results > 1:
                raise ValueError("Expected 1 match, but found %s matches" % n_results)

            return results[0]

        return default

    def decompose(self, bool recursive=True):
        """Remove a Node from the tree.

        Parameters
        ----------
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = HTMLParser(html)
        >>> for tag in tree.css('script'):
        >>>     tag.decompose()

        """
        if recursive:
            myhtml_node_delete_recursive(self.node)
        else:
            myhtml_node_delete(self.node)

    def remove(self, bool recursive=True):
        """An alias for the decompose method."""
        self.decompose(recursive)

    def unwrap(self, delete_empty = False):
        """Replace node with whatever is inside this node.

        Parameters
        ----------
        delete_empty : bool, default False
            Whenever to delete empty tags.

        Examples
        --------

        >>>  tree = HTMLParser("<div>Hello <i>world</i>!</div>")
        >>>  tree.css_first('i').unwrap()
        >>>  tree.html
        '<html><head></head><body><div>Hello world!</div></body></html>'

        Note: by default, empty tags are ignored, set "delete_empty" to "True" to change this.
        """
        if self.node.child == NULL:
            if delete_empty:
                myhtml_node_delete(self.node)
            return
        cdef myhtml_tree_node_t* next_node
        cdef myhtml_tree_node_t* current_node

        if self.node.child.next != NULL:
            current_node = self.node.child
            next_node = current_node.next

            while next_node != NULL:
                next_node = current_node.next
                myhtml_node_insert_before(self.node, current_node)
                current_node = next_node
        else:
            myhtml_node_insert_before(self.node, self.node.child)
        myhtml_node_delete(self.node)

    def strip_tags(self, list tags, bool recursive = False):
        """Remove specified tags from the HTML tree.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = HTMLParser('<html><head></head><body><script></script><div>Hello world!</div></body></html>')
        >>> tags = ['head', 'style', 'script', 'xmp', 'iframe', 'noembed', 'noframes']
        >>> tree.strip_tags(tags)
        >>> tree.html
        '<html><body><div>Hello world!</div></body></html>'

        """
        # ensure cython can recast element to a Node so that decompose will be called sooner.
        cdef Node element
        for tag in tags:
            for element in self.css(tag):
                element.decompose(recursive=recursive)

    def unwrap_tags(self, list tags, delete_empty = False):
        """Unwraps specified tags from the HTML tree.

        Works the same as the ``unwrap`` method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool, default False
            Whenever to delete empty tags.

        Examples
        --------

        >>> tree = HTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.body.unwrap_tags(['i','a'])
        >>> tree.body.html
        '<body><div>Hello world!</div></body>'

        Note: by default, empty tags are ignored, set "delete_empty" to "True" to change this.
        """
        cdef Node element
        for tag in tags:
            for element in self.css(tag):
                element.unwrap(delete_empty)

    def replace_with(self, str_or_Node value):
        """Replace current Node with specified value.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to replace the Node with.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = HTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.replace_with(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get Laptop</div>'

        >>> html_parser = HTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = HTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.replace_with(html_parser2.body.child)
        '<div>Get <span alt="Laptop"><div>Test</div> <div></div></span></div>'
        """
        cdef myhtml_tree_node_t *node
        if isinstance(value, (str, bytes, unicode)):
            bytes_val = to_bytes(value)
            node = myhtml_node_create(self.parser.html_tree, MyHTML_TAG__TEXT, MyHTML_NAMESPACE_HTML)
            myhtml_node_text_set(node, <char*> bytes_val, len(bytes_val), MyENCODING_UTF_8)
            myhtml_node_insert_before(self.node, node)
            myhtml_node_delete(self.node)
        elif isinstance(value, Node):
            node = myhtml_node_clone_deep(self.parser.html_tree, <myhtml_tree_node_t *> value.node)
            myhtml_node_insert_before(self.node, node)
            myhtml_node_delete(self.node)
        else:
            raise TypeError("Expected a string or Node instance, but %s found" % type(value).__name__)

    def insert_before(self, str_or_Node value):
        """
        Insert a node before the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert before the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = HTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.insert_before(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get Laptop<img src="" alt="Laptop"></div>'

        >>> html_parser = HTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = HTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.insert_before(html_parser2.body.child)
        <div>Get <span alt="Laptop"><div>Test</div><img src="/jpg"> <div></div></span></div>'
        """
        cdef myhtml_tree_node_t *node
        if isinstance(value, (str, bytes, unicode)):
            bytes_val =  to_bytes(value)
            node = myhtml_node_create(self.parser.html_tree, MyHTML_TAG__TEXT, MyHTML_NAMESPACE_HTML)
            myhtml_node_text_set(node, <char*> bytes_val, len(bytes_val), MyENCODING_UTF_8)
            myhtml_node_insert_before(self.node, node)
        elif isinstance(value, Node):
            node = myhtml_node_clone_deep(self.parser.html_tree, <myhtml_tree_node_t *> value.node)
            myhtml_node_insert_before(self.node, node)
        else:
            raise TypeError("Expected a string or Node instance, but %s found" % type(value).__name__)

    def insert_after(self, str_or_Node value):
        """
        Insert a node after the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert after the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = HTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.insert_after(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get <img src="" alt="Laptop">Laptop</div>'

        >>> html_parser = HTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = HTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.insert_after(html_parser2.body.child)
        <div>Get <span alt="Laptop"><img src="/jpg"><div>Test</div> <div></div></span></div>'
        """
        cdef myhtml_tree_node_t *node
        if isinstance(value, (str, bytes, unicode)):
            bytes_val = to_bytes(value)
            node = myhtml_node_create(self.parser.html_tree, MyHTML_TAG__TEXT, MyHTML_NAMESPACE_HTML)
            myhtml_node_text_set(node, <char*> bytes_val, len(bytes_val), MyENCODING_UTF_8)
            myhtml_node_insert_after(self.node, node)
        elif isinstance(value, Node):
            node = myhtml_node_clone_deep(self.parser.html_tree, <myhtml_tree_node_t *> value.node)
            myhtml_node_insert_after(self.node, node)
        else:
            raise TypeError("Expected a string or Node instance, but %s found" % type(value).__name__)

    def insert_child(self, str_or_Node value):
        """
        Insert a node inside (at the end of) the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert inside the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = HTMLParser('<div>Get <img src=""></div>')
        >>> div = tree.css_first('div')
        >>> div.insert_child('Laptop')
        >>> tree.body.child.html
        '<div>Get <img src="">Laptop</div>'

        >>> html_parser = HTMLParser('<div>Get <span alt="Laptop"> <div>Laptop</div> </span></div>')
        >>> html_parser2 = HTMLParser('<div>Test</div>')
        >>> span_node = html_parser.css_first('span')
        >>> span_node.insert_child(html_parser2.body.child)
        <div>Get <span alt="Laptop"> <div>Laptop</div> <div>Test</div> </span></div>'
        """
        cdef myhtml_tree_node_t *node
        if isinstance(value, (str, bytes, unicode)):
            bytes_val = to_bytes(value)
            node = myhtml_node_create(self.parser.html_tree, MyHTML_TAG__TEXT, MyHTML_NAMESPACE_HTML)
            myhtml_node_text_set(node, <char*> bytes_val, len(bytes_val), MyENCODING_UTF_8)
            myhtml_node_append_child(self.node, node)
        elif isinstance(value, Node):
            node = myhtml_node_clone_deep(self.parser.html_tree, <myhtml_tree_node_t *> value.node)
            myhtml_node_append_child(self.node, node)
        else:
            raise TypeError("Expected a string or Node instance, but %s found" % type(value).__name__)

    def unwrap_tags(self, list tags, delete_empty = False):
        """Unwraps specified tags from the HTML tree.

        Works the same as th ``unwrap`` method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool, default False
            Whenever to delete empty tags.

        Examples
        --------

        >>> tree = HTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.body.unwrap_tags(['i','a'])
        >>> tree.body.html
        '<body><div>Hello world!</div></body>'

        Note: by default, empty tags are ignored, set "delete_empty" to "True" to change this.
        """
        cdef Node element
        for tag in tags:
            for element in self.css(tag):
                element.unwrap(delete_empty)

    @property
    def raw_value(self):
        """Return the raw (unparsed, original) value of a node.

        Currently, works on text nodes only.

        Returns
        -------

        raw_value : bytes

        Examples
        --------

        >>> html_parser = HTMLParser('<div>&#x3C;test&#x3E;</div>')
        >>> selector = html_parser.css_first('div')
        >>> selector.child.html
        '&lt;test&gt;'
        >>> selector.child.raw_value
        b'&#x3C;test&#x3E;'
        """
        cdef int begin = self.node.token.element_begin
        cdef int length = self.node.token.element_length
        if self.node.tag_id != MyHTML_TAG__TEXT:
            raise ValueError("Can't obtain raw value for non-text node.")
        return self.parser.raw_html[begin:begin + length]

    def select(self, query=None):
        """Select nodes given a CSS selector.

        Works similarly to the ``css`` method, but supports chained filtering and extra features.

        Parameters
        ----------
        query : str or None
            The CSS selector to use when searching for nodes.

        Returns
        -------
        selector : The `Selector` class.
        """
        return Selector(self, query)

    def scripts_contain(self, str query):
        """Returns True if any of the script tags contain specified text.

        Caches script tags on the first call to improve performance.

        Parameters
        ----------
        query : str
            The query to check.

        """
        cdef Node node
        if self.parser.cached_script_texts is None:
            nodes = find_nodes(self.parser, self.node, 'script')
            text_nodes = []
            for node in nodes:
                node_text = node.text(deep=True)
                if node_text:
                    text_nodes.append(node_text)
            self.parser.cached_script_texts = text_nodes

        for text in self.parser.cached_script_texts:
            if query in text:
                return True
        return False

    def script_srcs_contain(self, tuple queries):
        """Returns True if any of the script SRCs attributes contain on of the specified text.

        Caches values on the first call to improve performance.

        Parameters
        ----------
        queries : tuple of str

        """
        if self.parser.cached_script_srcs is None:
            nodes = find_nodes(self.parser, self.node, 'script')
            src_nodes = []
            for node in nodes:
                node_src = node.attrs.get('src')
                if node_src:
                    src_nodes.append(node_src)
            self.parser.cached_script_srcs = src_nodes

        for text in self.parser.cached_script_srcs:
            for query in queries:
                if query in text:
                    return True
        return False

    def __repr__(self):
        return '<Node %s>' % self.tag

    def __eq__(self, other):
        if isinstance(other, str):
            return self.html == other
        if not isinstance(other, Node):
            return False
        return self.html == other.html

    @property
    def text_content(self):
        """Returns the text of the node if it is a text node.

        Returns None for other nodes.
        Unlike the ``text`` method, does not include child nodes.

        Returns
        -------
        text : str or None.
        """
        cdef const char* c_text

        if self.node.tag_id == MyHTML_TAG__TEXT:
            c_text = myhtml_node_text(self.node, NULL)
            if c_text != NULL:
                return c_text.decode(_ENCODING, self.parser.decode_errors)
        return None

    def merge_text_nodes(self):
        """Iterates over all text nodes and merges all text nodes that are close to each other.

        This is useful for text extraction.
        Use it when you need to strip HTML tags and merge "dangling" text.

        Examples
        --------

        >>> tree = HTMLParser("<div><p><strong>J</strong>ohn</p><p>Doe</p></div>")
        >>> node = tree.css_first('div')
        >>> tree.unwrap_tags(["strong"])
        >>> tree.text(deep=True, separator=" ", strip=True)
        "J ohn Doe" # Text extraction produces an extra space because the strong tag was removed.
        >>> node.merge_text_nodes()
        >>> tree.text(deep=True, separator=" ", strip=True)
        "John Doe"
        """
        cdef Stack stack = Stack(_STACK_SIZE)
        cdef myhtml_tree_node_t * current_node = NULL
        cdef Node next_node
        cdef const char* left_text
        cdef const char* right_text
        cdef char* final_text
        cdef size_t left_length, right_length, final_length

        stack.push(self.node)

        while not stack.is_empty():
            current_node = stack.pop()

            if (current_node.tag_id == MyHTML_TAG__TEXT and current_node.prev and
                    current_node.prev.tag_id == MyHTML_TAG__TEXT):
                left_text = myhtml_node_text(current_node.prev, &left_length)
                right_text = myhtml_node_text(current_node, &right_length)
                if left_text and right_text:
                    final_length = left_length + right_length
                    final_text = <char *>malloc(final_length + 1)
                    if final_text == NULL:
                        raise MemoryError("Can't allocate memory for a new node.")
                    memcpy(final_text, left_text, left_length)
                    memcpy(final_text + left_length, right_text, right_length + 1)
                    myhtml_node_text_set(current_node, <const char *>final_text, final_length, MyENCODING_UTF_8)
                    myhtml_node_delete(current_node.prev)
                    free(final_text)

            if current_node.next is not NULL:
                stack.push(current_node.next)

            if current_node.child is not NULL:
                stack.push(current_node.child)

cdef inline bytes to_bytes(str_or_Node value):
    cdef bytes bytes_val
    if isinstance(value, unicode):
        bytes_val = <bytes>value.encode("utf-8")
    elif isinstance(value, bytes):
        bytes_val = <bytes>value
    return bytes_val

```

### `selectolax/modest/selection.pxi`

```pxi
cimport cython
from cpython.exc cimport PyErr_SetObject


@cython.final
cdef class CSSSelector:

    cdef char *c_selector
    cdef mycss_entry_t *css_entry
    cdef modest_finder_t *finder
    cdef mycss_selectors_list_t *selectors_list

    def __init__(self, str selector):

        selector_pybyte = selector.encode('UTF-8')
        self.c_selector = selector_pybyte

        # In order to propagate errors these methods should return no value
        self._create_css_parser()
        self._prepare_selector(self.css_entry, self.c_selector, len(self.c_selector))
        self.finder = modest_finder_create_simple()

    cdef myhtml_collection_t* find(self, myhtml_tree_node_t* scope):
        """Find all possible matches."""

        cdef myhtml_collection_t *collection

        collection = NULL
        modest_finder_by_selectors_list(self.finder, scope, self.selectors_list, &collection)

        return collection

    cdef int _create_css_parser(self) except -1:
        cdef mystatus_t status

        cdef mycss_t *mycss = mycss_create()
        status = mycss_init(mycss)

        if status != 0:
            PyErr_SetObject(RuntimeError, "Can't init MyCSS object.")
            return -1

        self.css_entry = mycss_entry_create()
        status = mycss_entry_init(mycss, self.css_entry)

        if status != 0:
            PyErr_SetObject(RuntimeError, "Can't init MyCSS Entry object.")
            return -1
        return 0

    cdef int _prepare_selector(self, mycss_entry_t *css_entry, const char *selector, size_t selector_size) except -1:
        cdef mystatus_t out_status
        self.selectors_list = mycss_selectors_parse(mycss_entry_selectors(css_entry), myencoding_t.MyENCODING_UTF_8,
                                                    selector, selector_size, &out_status)

        if (self.selectors_list == NULL) or (self.selectors_list.flags and MyCSS_SELECTORS_FLAGS_SELECTOR_BAD):
            PyErr_SetObject(ValueError, "Bad CSS Selectors: %s" % self.c_selector.decode('utf-8'))
            return -1
        return 0

    def __dealloc__(self):
        mycss_selectors_list_destroy(mycss_entry_selectors(self.css_entry), self.selectors_list, 1)
        modest_finder_destroy(self.finder, 1)

        cdef mycss_t *mycss = self.css_entry.mycss
        mycss_entry_destroy(self.css_entry, 1)
        mycss_destroy(mycss, 1)


cdef class Selector:
    """An advanced CSS selector that supports additional operations.

    Think of it as a toolkit that mimics some of the features of XPath.

    Please note, this is an experimental feature that can change in the future.
    """
    cdef Node node
    cdef list nodes

    def __init__(self, Node node, str query):
        """custom init, because __cinit__ doesn't accept C types"""
        self.node = node
        self.nodes = find_nodes(node.parser, node.node, query) if query else [node, ]

    cpdef css(self, str query):
        """Evaluate CSS selector against current scope."""
        cdef Node current_node
        nodes = list()
        for node in self.nodes:
            current_node = node
            nodes.extend(find_nodes(self.node.parser, current_node.node, query))
        self.nodes = nodes
        return self

    @property
    def matches(self):
        """Returns all possible matches"""
        return self.nodes

    @property
    def any_matches(self):
        """Returns True if there are any matches"""
        return bool(self.nodes)

    def text_contains(self, str text, bool deep=True, str separator='', bool strip=False):
        """Filter all current matches given text."""
        nodes = []
        cdef Node node
        for node in self.nodes:
            node_text = node.text(deep=deep, separator=separator, strip=strip)
            if node_text and text in node_text:
                nodes.append(node)
        self.nodes = nodes
        return self

    def any_text_contains(self, str text, bool deep=True, str separator='', bool strip=False):
        """Returns True if any node in the current search scope contains specified text"""
        nodes = []
        cdef Node node
        for node in self.nodes:
            node_text = node.text(deep=deep, separator=separator, strip=strip)
            if node_text and text in node_text:
                return True
        return False

    def attribute_longer_than(self, str attribute, int length, str start  = None):
        """Filter all current matches by attribute length.

        Similar to `string-length` in XPath.
        """
        nodes = []
        for node in self.nodes:
            attr = node.attributes.get(attribute)
            if attr is None:
                continue
            if start and start in attr:
                attr = attr[attr.find(start) + len(start):]
            if len(attr) > length:
                nodes.append(node)
        self.nodes = nodes
        return self

    def any_attribute_longer_than(self, str attribute, int length, str start  = None):
        """Returns True any href attribute longer than a specified length.

        Similar to `string-length` in XPath.
        """
        cdef list nodes = []
        cdef Node node
        for node in self.nodes:
            attr = node.attributes.get(attribute)
            if attr is None:
                continue
            if start and start in attr:
                attr = attr[attr.find(start) + len(start):]
            if len(attr) > length:
                return True
        return False

    def __bool__(self):
        return bool(self.nodes)

cdef find_nodes(HTMLParser parser, myhtml_tree_node_t *node, str query):
    cdef myhtml_collection_t *collection
    cdef CSSSelector selector = CSSSelector(query)
    cdef Node n
    cdef list result = []
    collection = selector.find(node)

    if collection == NULL:
        return result

    for i in range(collection.length):
        n = Node.new(collection.list[i], parser)
        result.append(n)
    myhtml_collection_destroy(collection)
    return result


cdef bool find_matches(HTMLParser parser, myhtml_tree_node_t *node, tuple selectors):
    cdef myhtml_collection_t *collection
    cdef CSSSelector selector
    cdef int collection_size
    cdef str query

    for query in selectors:
        selector = CSSSelector(query)
        collection_size = 0
        collection = NULL

        collection = selector.find(node)
        if collection == NULL:
            continue

        collection_size = collection.length
        myhtml_collection_destroy(collection)
        if collection_size > 0:
            return True
    return False

```

### `selectolax/modest/util.pxi`

```pxi
include "../utils.pxi"


def create_tag(tag: str):
    """
    Given an HTML tag name, e.g. `"div"`, create a single empty node for that tag,
    e.g. `"<div></div>"`.
    """
    return do_create_tag(tag, HTMLParser)


def parse_fragment(html: str):
    """
    Given HTML, parse it into a list of Nodes, such that the nodes
    correspond to the given HTML.

    For contrast, HTMLParser adds `<html>`, `<head>`, and `<body>` tags
    if they are missing. This function does not add these tags.
    """
    return do_parse_fragment(html, HTMLParser)

```

### `selectolax/parser.pxd`

```pxd
# cython: freethreading_compatible = True
cdef extern from "myhtml/myhtml.h" nogil:
    ctypedef unsigned int mystatus_t
    ctypedef struct myhtml_t
    ctypedef size_t myhtml_tag_id_t

    ctypedef struct myhtml_tree_t:
        # not completed struct
        myhtml_t* myhtml
        myhtml_tree_node_t*   document
        myhtml_tree_node_t*   node_html

    ctypedef struct mchar_async_t
    ctypedef struct mycore_string_t:
        char*  data
        size_t size
        size_t length

        mchar_async_t *mchar
        size_t node_idx

    ctypedef struct mycore_string_raw_t:
        char*  data
        size_t size
        size_t length

        myhtml_namespace ns

    ctypedef enum myhtml_options:
        MyHTML_OPTIONS_DEFAULT                 = 0x00
        MyHTML_OPTIONS_PARSE_MODE_SINGLE       = 0x01
        MyHTML_OPTIONS_PARSE_MODE_ALL_IN_ONE   = 0x02
        MyHTML_OPTIONS_PARSE_MODE_SEPARATELY   = 0x04

    ctypedef struct myhtml_collection_t:
        myhtml_tree_node_t **list
        size_t size
        size_t length

    ctypedef  struct myhtml_tree_node_t:
        myhtml_tree_node_flags flags

        myhtml_tag_id_t tag_id
        myhtml_namespace ns

        myhtml_tree_node_t* prev
        myhtml_tree_node_t* next
        myhtml_tree_node_t* child
        myhtml_tree_node_t* parent

        myhtml_tree_node_t* last_child

        myhtml_token_node_t* token
        void* data

        myhtml_tree_t* tree

    ctypedef enum myhtml_namespace:
        MyHTML_NAMESPACE_UNDEF      = 0x00
        MyHTML_NAMESPACE_HTML       = 0x01
        MyHTML_NAMESPACE_MATHML     = 0x02
        MyHTML_NAMESPACE_SVG        = 0x03
        MyHTML_NAMESPACE_XLINK      = 0x04
        MyHTML_NAMESPACE_XML        = 0x05
        MyHTML_NAMESPACE_XMLNS      = 0x06
        MyHTML_NAMESPACE_ANY        = 0x07
        MyHTML_NAMESPACE_LAST_ENTRY = 0x07

    ctypedef enum myhtml_tree_node_flags:
        MyHTML_TREE_NODE_UNDEF           = 0
        MyHTML_TREE_NODE_PARSER_INSERTED = 1
        MyHTML_TREE_NODE_BLOCKING        = 2

    ctypedef enum myhtml_token_type:
        MyHTML_TOKEN_TYPE_OPEN             = 0x000
        MyHTML_TOKEN_TYPE_CLOSE            = 0x001
        MyHTML_TOKEN_TYPE_CLOSE_SELF       = 0x002
        MyHTML_TOKEN_TYPE_DONE             = 0x004
        MyHTML_TOKEN_TYPE_WHITESPACE       = 0x008
        MyHTML_TOKEN_TYPE_RCDATA           = 0x010
        MyHTML_TOKEN_TYPE_RAWTEXT          = 0x020
        MyHTML_TOKEN_TYPE_SCRIPT           = 0x040
        MyHTML_TOKEN_TYPE_PLAINTEXT        = 0x080
        MyHTML_TOKEN_TYPE_CDATA            = 0x100
        MyHTML_TOKEN_TYPE_DATA             = 0x200
        MyHTML_TOKEN_TYPE_COMMENT          = 0x400
        MyHTML_TOKEN_TYPE_NULL             = 0x800

    ctypedef enum myhtml_tags:
        MyHTML_TAG__UNDEF              = 0x000
        MyHTML_TAG__TEXT               = 0x001
        MyHTML_TAG__COMMENT            = 0x002
        MyHTML_TAG__DOCTYPE            = 0x003
        MyHTML_TAG_A                   = 0x004
        MyHTML_TAG_ABBR                = 0x005
        MyHTML_TAG_ACRONYM             = 0x006
        MyHTML_TAG_ADDRESS             = 0x007
        MyHTML_TAG_ANNOTATION_XML      = 0x008
        MyHTML_TAG_APPLET              = 0x009
        MyHTML_TAG_AREA                = 0x00a
        MyHTML_TAG_ARTICLE             = 0x00b
        MyHTML_TAG_ASIDE               = 0x00c
        MyHTML_TAG_AUDIO               = 0x00d
        MyHTML_TAG_B                   = 0x00e
        MyHTML_TAG_BASE                = 0x00f
        MyHTML_TAG_BASEFONT            = 0x010
        MyHTML_TAG_BDI                 = 0x011
        MyHTML_TAG_BDO                 = 0x012
        MyHTML_TAG_BGSOUND             = 0x013
        MyHTML_TAG_BIG                 = 0x014
        MyHTML_TAG_BLINK               = 0x015
        MyHTML_TAG_BLOCKQUOTE          = 0x016
        MyHTML_TAG_BODY                = 0x017
        MyHTML_TAG_BR                  = 0x018
        MyHTML_TAG_BUTTON              = 0x019
        MyHTML_TAG_CANVAS              = 0x01a
        MyHTML_TAG_CAPTION             = 0x01b
        MyHTML_TAG_CENTER              = 0x01c
        MyHTML_TAG_CITE                = 0x01d
        MyHTML_TAG_CODE                = 0x01e
        MyHTML_TAG_COL                 = 0x01f
        MyHTML_TAG_COLGROUP            = 0x020
        MyHTML_TAG_COMMAND             = 0x021
        MyHTML_TAG_COMMENT             = 0x022
        MyHTML_TAG_DATALIST            = 0x023
        MyHTML_TAG_DD                  = 0x024
        MyHTML_TAG_DEL                 = 0x025
        MyHTML_TAG_DETAILS             = 0x026
        MyHTML_TAG_DFN                 = 0x027
        MyHTML_TAG_DIALOG              = 0x028
        MyHTML_TAG_DIR                 = 0x029
        MyHTML_TAG_DIV                 = 0x02a
        MyHTML_TAG_DL                  = 0x02b
        MyHTML_TAG_DT                  = 0x02c
        MyHTML_TAG_EM                  = 0x02d
        MyHTML_TAG_EMBED               = 0x02e
        MyHTML_TAG_FIELDSET            = 0x02f
        MyHTML_TAG_FIGCAPTION          = 0x030
        MyHTML_TAG_FIGURE              = 0x031
        MyHTML_TAG_FONT                = 0x032
        MyHTML_TAG_FOOTER              = 0x033
        MyHTML_TAG_FORM                = 0x034
        MyHTML_TAG_FRAME               = 0x035
        MyHTML_TAG_FRAMESET            = 0x036
        MyHTML_TAG_H1                  = 0x037
        MyHTML_TAG_H2                  = 0x038
        MyHTML_TAG_H3                  = 0x039
        MyHTML_TAG_H4                  = 0x03a
        MyHTML_TAG_H5                  = 0x03b
        MyHTML_TAG_H6                  = 0x03c
        MyHTML_TAG_HEAD                = 0x03d
        MyHTML_TAG_HEADER              = 0x03e
        MyHTML_TAG_HGROUP              = 0x03f
        MyHTML_TAG_HR                  = 0x040
        MyHTML_TAG_HTML                = 0x041
        MyHTML_TAG_I                   = 0x042
        MyHTML_TAG_IFRAME              = 0x043
        MyHTML_TAG_IMAGE               = 0x044
        MyHTML_TAG_IMG                 = 0x045
        MyHTML_TAG_INPUT               = 0x046
        MyHTML_TAG_INS                 = 0x047
        MyHTML_TAG_ISINDEX             = 0x048
        MyHTML_TAG_KBD                 = 0x049
        MyHTML_TAG_KEYGEN              = 0x04a
        MyHTML_TAG_LABEL               = 0x04b
        MyHTML_TAG_LEGEND              = 0x04c
        MyHTML_TAG_LI                  = 0x04d
        MyHTML_TAG_LINK                = 0x04e
        MyHTML_TAG_LISTING             = 0x04f
        MyHTML_TAG_MAIN                = 0x050
        MyHTML_TAG_MAP                 = 0x051
        MyHTML_TAG_MARK                = 0x052
        MyHTML_TAG_MARQUEE             = 0x053
        MyHTML_TAG_MENU                = 0x054
        MyHTML_TAG_MENUITEM            = 0x055
        MyHTML_TAG_META                = 0x056
        MyHTML_TAG_METER               = 0x057
        MyHTML_TAG_MTEXT               = 0x058
        MyHTML_TAG_NAV                 = 0x059
        MyHTML_TAG_NOBR                = 0x05a
        MyHTML_TAG_NOEMBED             = 0x05b
        MyHTML_TAG_NOFRAMES            = 0x05c
        MyHTML_TAG_NOSCRIPT            = 0x05d
        MyHTML_TAG_OBJECT              = 0x05e
        MyHTML_TAG_OL                  = 0x05f
        MyHTML_TAG_OPTGROUP            = 0x060
        MyHTML_TAG_OPTION              = 0x061
        MyHTML_TAG_OUTPUT              = 0x062
        MyHTML_TAG_P                   = 0x063
        MyHTML_TAG_PARAM               = 0x064
        MyHTML_TAG_PLAINTEXT           = 0x065
        MyHTML_TAG_PRE                 = 0x066
        MyHTML_TAG_PROGRESS            = 0x067
        MyHTML_TAG_Q                   = 0x068
        MyHTML_TAG_RB                  = 0x069
        MyHTML_TAG_RP                  = 0x06a
        MyHTML_TAG_RT                  = 0x06b
        MyHTML_TAG_RTC                 = 0x06c
        MyHTML_TAG_RUBY                = 0x06d
        MyHTML_TAG_S                   = 0x06e
        MyHTML_TAG_SAMP                = 0x06f
        MyHTML_TAG_SCRIPT              = 0x070
        MyHTML_TAG_SECTION             = 0x071
        MyHTML_TAG_SELECT              = 0x072
        MyHTML_TAG_SMALL               = 0x073
        MyHTML_TAG_SOURCE              = 0x074
        MyHTML_TAG_SPAN                = 0x075
        MyHTML_TAG_STRIKE              = 0x076
        MyHTML_TAG_STRONG              = 0x077
        MyHTML_TAG_STYLE               = 0x078
        MyHTML_TAG_SUB                 = 0x079
        MyHTML_TAG_SUMMARY             = 0x07a
        MyHTML_TAG_SUP                 = 0x07b
        MyHTML_TAG_SVG                 = 0x07c
        MyHTML_TAG_TABLE               = 0x07d
        MyHTML_TAG_TBODY               = 0x07e
        MyHTML_TAG_TD                  = 0x07f
        MyHTML_TAG_TEMPLATE            = 0x080
        MyHTML_TAG_TEXTAREA            = 0x081
        MyHTML_TAG_TFOOT               = 0x082
        MyHTML_TAG_TH                  = 0x083
        MyHTML_TAG_THEAD               = 0x084
        MyHTML_TAG_TIME                = 0x085
        MyHTML_TAG_TITLE               = 0x086
        MyHTML_TAG_TR                  = 0x087
        MyHTML_TAG_TRACK               = 0x088
        MyHTML_TAG_TT                  = 0x089
        MyHTML_TAG_U                   = 0x08a
        MyHTML_TAG_UL                  = 0x08b
        MyHTML_TAG_VAR                 = 0x08c
        MyHTML_TAG_VIDEO               = 0x08d
        MyHTML_TAG_WBR                 = 0x08e
        MyHTML_TAG_XMP                 = 0x08f
        MyHTML_TAG_ALTGLYPH            = 0x090
        MyHTML_TAG_ALTGLYPHDEF         = 0x091
        MyHTML_TAG_ALTGLYPHITEM        = 0x092
        MyHTML_TAG_ANIMATE             = 0x093
        MyHTML_TAG_ANIMATECOLOR        = 0x094
        MyHTML_TAG_ANIMATEMOTION       = 0x095
        MyHTML_TAG_ANIMATETRANSFORM    = 0x096
        MyHTML_TAG_CIRCLE              = 0x097
        MyHTML_TAG_CLIPPATH            = 0x098
        MyHTML_TAG_COLOR_PROFILE       = 0x099
        MyHTML_TAG_CURSOR              = 0x09a
        MyHTML_TAG_DEFS                = 0x09b
        MyHTML_TAG_DESC                = 0x09c
        MyHTML_TAG_ELLIPSE             = 0x09d
        MyHTML_TAG_FEBLEND             = 0x09e
        MyHTML_TAG_FECOLORMATRIX       = 0x09f
        MyHTML_TAG_FECOMPONENTTRANSFER = 0x0a0
        MyHTML_TAG_FECOMPOSITE         = 0x0a1
        MyHTML_TAG_FECONVOLVEMATRIX    = 0x0a2
        MyHTML_TAG_FEDIFFUSELIGHTING   = 0x0a3
        MyHTML_TAG_FEDISPLACEMENTMAP   = 0x0a4
        MyHTML_TAG_FEDISTANTLIGHT      = 0x0a5
        MyHTML_TAG_FEDROPSHADOW        = 0x0a6
        MyHTML_TAG_FEFLOOD             = 0x0a7
        MyHTML_TAG_FEFUNCA             = 0x0a8
        MyHTML_TAG_FEFUNCB             = 0x0a9
        MyHTML_TAG_FEFUNCG             = 0x0aa
        MyHTML_TAG_FEFUNCR             = 0x0ab
        MyHTML_TAG_FEGAUSSIANBLUR      = 0x0ac
        MyHTML_TAG_FEIMAGE             = 0x0ad
        MyHTML_TAG_FEMERGE             = 0x0ae
        MyHTML_TAG_FEMERGENODE         = 0x0af
        MyHTML_TAG_FEMORPHOLOGY        = 0x0b0
        MyHTML_TAG_FEOFFSET            = 0x0b1
        MyHTML_TAG_FEPOINTLIGHT        = 0x0b2
        MyHTML_TAG_FESPECULARLIGHTING  = 0x0b3
        MyHTML_TAG_FESPOTLIGHT         = 0x0b4
        MyHTML_TAG_FETILE              = 0x0b5
        MyHTML_TAG_FETURBULENCE        = 0x0b6
        MyHTML_TAG_FILTER              = 0x0b7
        MyHTML_TAG_FONT_FACE           = 0x0b8
        MyHTML_TAG_FONT_FACE_FORMAT    = 0x0b9
        MyHTML_TAG_FONT_FACE_NAME      = 0x0ba
        MyHTML_TAG_FONT_FACE_SRC       = 0x0bb
        MyHTML_TAG_FONT_FACE_URI       = 0x0bc
        MyHTML_TAG_FOREIGNOBJECT       = 0x0bd
        MyHTML_TAG_G                   = 0x0be
        MyHTML_TAG_GLYPH               = 0x0bf
        MyHTML_TAG_GLYPHREF            = 0x0c0
        MyHTML_TAG_HKERN               = 0x0c1
        MyHTML_TAG_LINE                = 0x0c2
        MyHTML_TAG_LINEARGRADIENT      = 0x0c3
        MyHTML_TAG_MARKER              = 0x0c4
        MyHTML_TAG_MASK                = 0x0c5
        MyHTML_TAG_METADATA            = 0x0c6
        MyHTML_TAG_MISSING_GLYPH       = 0x0c7
        MyHTML_TAG_MPATH               = 0x0c8
        MyHTML_TAG_PATH                = 0x0c9
        MyHTML_TAG_PATTERN             = 0x0ca
        MyHTML_TAG_POLYGON             = 0x0cb
        MyHTML_TAG_POLYLINE            = 0x0cc
        MyHTML_TAG_RADIALGRADIENT      = 0x0cd
        MyHTML_TAG_RECT                = 0x0ce
        MyHTML_TAG_SET                 = 0x0cf
        MyHTML_TAG_STOP                = 0x0d0
        MyHTML_TAG_SWITCH              = 0x0d1
        MyHTML_TAG_SYMBOL              = 0x0d2
        MyHTML_TAG_TEXT                = 0x0d3
        MyHTML_TAG_TEXTPATH            = 0x0d4
        MyHTML_TAG_TREF                = 0x0d5
        MyHTML_TAG_TSPAN               = 0x0d6
        MyHTML_TAG_USE                 = 0x0d7
        MyHTML_TAG_VIEW                = 0x0d8
        MyHTML_TAG_VKERN               = 0x0d9
        MyHTML_TAG_MATH                = 0x0da
        MyHTML_TAG_MACTION             = 0x0db
        MyHTML_TAG_MALIGNGROUP         = 0x0dc
        MyHTML_TAG_MALIGNMARK          = 0x0dd
        MyHTML_TAG_MENCLOSE            = 0x0de
        MyHTML_TAG_MERROR              = 0x0df
        MyHTML_TAG_MFENCED             = 0x0e0
        MyHTML_TAG_MFRAC               = 0x0e1
        MyHTML_TAG_MGLYPH              = 0x0e2
        MyHTML_TAG_MI                  = 0x0e3
        MyHTML_TAG_MLABELEDTR          = 0x0e4
        MyHTML_TAG_MLONGDIV            = 0x0e5
        MyHTML_TAG_MMULTISCRIPTS       = 0x0e6
        MyHTML_TAG_MN                  = 0x0e7
        MyHTML_TAG_MO                  = 0x0e8
        MyHTML_TAG_MOVER               = 0x0e9
        MyHTML_TAG_MPADDED             = 0x0ea
        MyHTML_TAG_MPHANTOM            = 0x0eb
        MyHTML_TAG_MROOT               = 0x0ec
        MyHTML_TAG_MROW                = 0x0ed
        MyHTML_TAG_MS                  = 0x0ee
        MyHTML_TAG_MSCARRIES           = 0x0ef
        MyHTML_TAG_MSCARRY             = 0x0f0
        MyHTML_TAG_MSGROUP             = 0x0f1
        MyHTML_TAG_MSLINE              = 0x0f2
        MyHTML_TAG_MSPACE              = 0x0f3
        MyHTML_TAG_MSQRT               = 0x0f4
        MyHTML_TAG_MSROW               = 0x0f5
        MyHTML_TAG_MSTACK              = 0x0f6
        MyHTML_TAG_MSTYLE              = 0x0f7
        MyHTML_TAG_MSUB                = 0x0f8
        MyHTML_TAG_MSUP                = 0x0f9
        MyHTML_TAG_MSUBSUP             = 0x0fa
        MyHTML_TAG__END_OF_FILE        = 0x0fb
        MyHTML_TAG_FIRST_ENTRY         = MyHTML_TAG__TEXT
        MyHTML_TAG_LAST_ENTRY          = 0x0fc

    ctypedef enum myhtml_tree_parse_flags_t:
        MyHTML_TREE_PARSE_FLAGS_CLEAN = 0x000
        MyHTML_TREE_PARSE_FLAGS_WITHOUT_BUILD_TREE = 0x001
        MyHTML_TREE_PARSE_FLAGS_WITHOUT_PROCESS_TOKEN = 0x003
        MyHTML_TREE_PARSE_FLAGS_SKIP_WHITESPACE_TOKEN = 0x004
        MyHTML_TREE_PARSE_FLAGS_WITHOUT_DOCTYPE_IN_TREE = 0x008

    ctypedef  struct myhtml_token_node_t:
        myhtml_tag_id_t tag_id

        mycore_string_t str

        size_t raw_begin
        size_t raw_length

        size_t element_begin
        size_t element_length

        myhtml_token_attr_t* attr_first
        myhtml_token_attr_t* attr_last

        myhtml_token_type type

    ctypedef struct myhtml_token_attr_t:
        myhtml_token_attr_t* next
        myhtml_token_attr_t* prev

        mycore_string_t key
        mycore_string_t value

        size_t raw_key_begin
        size_t raw_key_length
        size_t raw_value_begin
        size_t raw_value_length

        myhtml_namespace ns

    ctypedef struct myhtml_tree_attr_t:
        myhtml_tree_attr_t* next
        myhtml_tree_attr_t* prev

        mycore_string_t key
        mycore_string_t value

        size_t raw_key_begin
        size_t raw_key_length
        size_t raw_value_begin
        size_t raw_value_length

    myhtml_t * myhtml_create()
    mystatus_t myhtml_init(myhtml_t* myhtml, myhtml_options opt, size_t thread_count, size_t queue_size)
    myhtml_tree_t * myhtml_tree_create()
    mystatus_t myhtml_tree_init(myhtml_tree_t* tree, myhtml_t* myhtml)
    mystatus_t myhtml_parse(myhtml_tree_t* tree, myencoding_t encoding, const char* html, size_t html_size)

    myhtml_tree_attr_t* myhtml_node_attribute_first(myhtml_tree_node_t* node)
    myhtml_tree_attr_t* myhtml_attribute_by_key(myhtml_tree_node_t *node, const char *key, size_t key_len)
    const char* myhtml_node_text(myhtml_tree_node_t *node, size_t *length)
    mycore_string_t * myhtml_node_string(myhtml_tree_node_t *node)
    const char * myhtml_tag_name_by_id(myhtml_tree_t* tree, myhtml_tag_id_t tag_id, size_t *length)

    myhtml_collection_t * myhtml_collection_destroy(myhtml_collection_t *collection)
    myhtml_tree_t * myhtml_tree_destroy(myhtml_tree_t* tree)
    myhtml_t* myhtml_destroy(myhtml_t* myhtml)

    myhtml_tree_node_t* myhtml_tree_get_document(myhtml_tree_t* tree)
    myhtml_tree_node_t* myhtml_tree_get_node_body(myhtml_tree_t* tree)
    myhtml_tree_node_t* myhtml_tree_get_node_head(myhtml_tree_t* tree)

    myhtml_collection_t* myhtml_get_nodes_by_name(myhtml_tree_t* tree, myhtml_collection_t *collection,
                                                  const char* name, size_t length, mystatus_t *status)

    void myhtml_node_delete(myhtml_tree_node_t *node)
    void myhtml_node_delete_recursive(myhtml_tree_node_t *node)
    void myhtml_tree_parse_flags_set(myhtml_tree_t* tree, myhtml_tree_parse_flags_t parse_flags)
    myhtml_tree_node_t * myhtml_node_insert_before(myhtml_tree_node_t *target, myhtml_tree_node_t *node)
    myhtml_tree_node_t * myhtml_node_insert_after(myhtml_tree_node_t *target, myhtml_tree_node_t *node)
    myhtml_tree_node_t * myhtml_node_create(myhtml_tree_t* tree, myhtml_tag_id_t tag_id, myhtml_namespace ns)
    myhtml_tree_node_t * myhtml_node_clone_deep(myhtml_tree_t* dest_tree, myhtml_tree_node_t* src)
    myhtml_tree_node_t * myhtml_node_append_child(myhtml_tree_node_t* target, myhtml_tree_node_t* node)

    mycore_string_t * myhtml_node_text_set(myhtml_tree_node_t *node, const char* text, size_t length,
                                           myencoding_t encoding)
    myhtml_tree_attr_t * myhtml_attribute_by_key(myhtml_tree_node_t *node, const char *key, size_t key_len)
    myhtml_tree_attr_t * myhtml_attribute_remove_by_key(myhtml_tree_node_t *node, const char *key, size_t key_len)
    myhtml_tree_attr_t * myhtml_attribute_add(myhtml_tree_node_t *node, const char *key, size_t key_len,
                                              const char *value, size_t value_len, myencoding_t encoding)

    myhtml_tree_node_t * myhtml_node_insert_to_appropriate_place(myhtml_tree_node_t *target, myhtml_tree_node_t *node)

cdef extern from "myhtml/tree.h" nogil:
    myhtml_tree_node_t * myhtml_tree_node_clone(myhtml_tree_node_t* node)
    myhtml_tree_node_t * myhtml_tree_node_insert_root(myhtml_tree_t* tree, myhtml_token_node_t* token,
                                                      myhtml_namespace ns)
    void myhtml_tree_node_add_child(myhtml_tree_node_t* root, myhtml_tree_node_t* node)

cdef extern from "myhtml/serialization.h" nogil:
    mystatus_t myhtml_serialization(myhtml_tree_node_t* scope_node, mycore_string_raw_t* str)


cdef extern from "myencoding/encoding.h" nogil:
    ctypedef enum myencoding_t:
        MyENCODING_DEFAULT        = 0x00
        # MyENCODING_AUTO           = 0x01  // future
        MyENCODING_NOT_DETERMINED = 0x02
        MyENCODING_UTF_8          = 0x00  # default encoding
        MyENCODING_UTF_16LE       = 0x04
        MyENCODING_UTF_16BE       = 0x05
        MyENCODING_X_USER_DEFINED = 0x06
        MyENCODING_BIG5           = 0x07
        MyENCODING_EUC_JP         = 0x08
        MyENCODING_EUC_KR         = 0x09
        MyENCODING_GB18030        = 0x0a
        MyENCODING_GBK            = 0x0b
        MyENCODING_IBM866         = 0x0c
        MyENCODING_ISO_2022_JP    = 0x0d
        MyENCODING_ISO_8859_10    = 0x0e
        MyENCODING_ISO_8859_13    = 0x0f
        MyENCODING_ISO_8859_14    = 0x10
        MyENCODING_ISO_8859_15    = 0x11
        MyENCODING_ISO_8859_16    = 0x12
        MyENCODING_ISO_8859_2     = 0x13
        MyENCODING_ISO_8859_3     = 0x14
        MyENCODING_ISO_8859_4     = 0x15
        MyENCODING_ISO_8859_5     = 0x16
        MyENCODING_ISO_8859_6     = 0x17
        MyENCODING_ISO_8859_7     = 0x18
        MyENCODING_ISO_8859_8     = 0x19
        MyENCODING_ISO_8859_8_I   = 0x1a
        MyENCODING_KOI8_R         = 0x1b
        MyENCODING_KOI8_U         = 0x1c
        MyENCODING_MACINTOSH      = 0x1d
        MyENCODING_SHIFT_JIS      = 0x1e
        MyENCODING_WINDOWS_1250   = 0x1f
        MyENCODING_WINDOWS_1251   = 0x20
        MyENCODING_WINDOWS_1252   = 0x21
        MyENCODING_WINDOWS_1253   = 0x22
        MyENCODING_WINDOWS_1254   = 0x23
        MyENCODING_WINDOWS_1255   = 0x24
        MyENCODING_WINDOWS_1256   = 0x25
        MyENCODING_WINDOWS_1257   = 0x26
        MyENCODING_WINDOWS_1258   = 0x27
        MyENCODING_WINDOWS_874    = 0x28
        MyENCODING_X_MAC_CYRILLIC = 0x29
        MyENCODING_LAST_ENTRY     = 0x2a

    bint myencoding_detect_bom(const char *text, size_t length, myencoding_t *encoding)
    bint myencoding_detect(const char *text, size_t length, myencoding_t *encoding)
    myencoding_t myencoding_prescan_stream_to_determine_encoding(const char *data, size_t data_size)
    const char* myencoding_name_by_id(myencoding_t encoding, size_t *length)


cdef extern from "mycss/mycss.h" nogil:
    ctypedef struct mycss_entry_t:
        # not completed struct
        mycss_t* mycss

    ctypedef struct mycss_t

    ctypedef struct mycss_selectors_t

    ctypedef struct mycss_selectors_entries_list_t
    ctypedef struct mycss_declaration_entry_t

    ctypedef enum mycss_selectors_flags:
        MyCSS_SELECTORS_FLAGS_UNDEF         = 0x00
        MyCSS_SELECTORS_FLAGS_SELECTOR_BAD  = 0x01
    ctypedef mycss_selectors_flags mycss_selectors_flags_t

    ctypedef struct mycss_selectors_list_t:
        mycss_selectors_entries_list_t* entries_list
        size_t entries_list_length

        mycss_declaration_entry_t* declaration_entry

        mycss_selectors_flags_t flags

        mycss_selectors_list_t* parent
        mycss_selectors_list_t* next
        mycss_selectors_list_t* prev

    # CSS init routines
    mycss_t * mycss_create()
    mystatus_t mycss_init(mycss_t* mycss)
    mycss_entry_t * mycss_entry_create()
    mystatus_t mycss_entry_init(mycss_t* mycss, mycss_entry_t* entry)

    mycss_selectors_list_t * mycss_selectors_parse(mycss_selectors_t* selectors, myencoding_t encoding,
                                                   const char* data, size_t data_size, mystatus_t* out_status)
    mycss_selectors_t * mycss_entry_selectors(mycss_entry_t* entry)

    mycss_selectors_list_t * mycss_selectors_list_destroy(mycss_selectors_t* selectors,
                                                          mycss_selectors_list_t* selectors_list, bint self_destroy)
    mycss_entry_t * mycss_entry_destroy(mycss_entry_t* entry, bint self_destroy)
    mycss_t * mycss_destroy(mycss_t* mycss, bint self_destroy)


cdef extern from "modest/finder/finder.h" nogil:
    ctypedef struct modest_finder_t
    modest_finder_t* modest_finder_create_simple()
    mystatus_t modest_finder_by_selectors_list(modest_finder_t* finder, myhtml_tree_node_t* scope_node,
                                               mycss_selectors_list_t* selector_list, myhtml_collection_t** collection)
    modest_finder_t * modest_finder_destroy(modest_finder_t* finder, bint self_destroy)


cdef class HTMLParser:
    cdef myhtml_tree_t *html_tree
    cdef public bint detect_encoding
    cdef public bint use_meta_tags
    cdef myencoding_t _encoding
    cdef public unicode decode_errors
    cdef public bytes raw_html
    cdef object cached_script_texts
    cdef object cached_script_srcs

    cdef void _detect_encoding(self, char* html, size_t html_len) nogil
    cdef int _parse_html(self, char* html, size_t html_len) except -1

    @staticmethod
    cdef HTMLParser from_tree(
        myhtml_tree_t * tree, bytes raw_html, bint detect_encoding, bint use_meta_tags, str decode_errors,
        myencoding_t encoding
    )


cdef class Stack:
    cdef size_t capacity
    cdef size_t top
    cdef myhtml_tree_node_t ** _stack

    cdef bint is_empty(self)
    cdef int push(self, myhtml_tree_node_t* res) except -1
    cdef myhtml_tree_node_t * pop(self)
    cdef int resize(self) except -1

```

### `selectolax/parser.pyi`

```pyi
from typing import Iterator, Literal, TypeVar, overload

DefaultT = TypeVar("DefaultT")

class _Attributes:
    """A dict-like object that represents attributes."""

    @staticmethod
    def create(node: Node, decode_errors: str) -> _Attributes: ...
    def keys(self) -> Iterator[str]: ...
    def items(self) -> Iterator[tuple[str, str | None]]: ...
    def values(self) -> Iterator[str | None]: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str) -> str | None: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __repr__(self) -> str: ...
    @overload
    def get(self, key: str, default: DefaultT) -> DefaultT | str | None: ...
    @overload
    def get(self, key: str, default: None = ...) -> str | None: ...
    @overload
    def sget(self, key: str, default: str | DefaultT) -> str | DefaultT: ...
    @overload
    def sget(self, key: str, default: str = "") -> str:
        """Same as get, but returns empty strings instead of None values for empty attributes."""
        ...

class Selector:
    """An advanced CSS selector that supports additional operations.

    Think of it as a toolkit that mimics some of the features of XPath.

    Please note, this is an experimental feature that can change in the future."""

    def __init__(self, node: Node, query: str): ...
    def css(self, query: str) -> Node:
        """Evaluate CSS selector against current scope."""
        ...
    @property
    def matches(self) -> list[Node]:
        """Returns all possible selector matches"""
        ...
    @property
    def any_matches(self) -> bool:
        """Returns True if there are any matches"""
        ...
    def text_contains(
        self, text: str, deep: bool = True, separator: str = "", strip: bool = False
    ) -> Selector:
        """Filter all current matches given text."""
        ...
    def any_text_contains(
        self, text: str, deep: bool = True, separator: str = "", strip: bool = False
    ) -> bool:
        """Returns True if any node in the current search scope contains specified text"""
        ...
    def attribute_longer_than(
        self, text: str, length: int, start: str | None = None
    ) -> Selector:
        """Filter all current matches by attribute length.

        Similar to string-length in XPath."""
        ...
    def any_attribute_longer_than(
        self, text: str, length: int, start: str | None = None
    ) -> bool:
        """Returns True any href attribute longer than a specified length.

        Similar to string-length in XPath."""
        ...

class Node:
    """A class that represents HTML node (element)."""

    parser: HTMLParser
    @property
    def attributes(self) -> dict[str, str | None]:
        """Get all attributes that belong to the current node.

        The value of empty attributes is None.

        Returns
        -------
        attributes : dictionary of all attributes.

        Examples
        --------

        >>> tree = HTMLParser("<div data id='my_id'></div>")
        >>> node = tree.css_first('div')
        >>> node.attributes
        {'data': None, 'id': 'my_id'}
        """
        ...
    @property
    def attrs(self) -> _Attributes:
        """A dict-like object that is similar to the ``attributes`` property, but operates directly on the Node data.

        .. warning:: Use ``attributes`` instead, if you don't want to modify Node attributes.

        Returns
        -------
        attributes : Attributes mapping object.

        Examples
        --------

        >>> tree = HTMLParser("<div id='a'></div>")
        >>> node = tree.css_first('div')
        >>> node.attrs
        <div attributes, 1 items>
        >>> node.attrs['id']
        'a'
        >>> node.attrs['foo'] = 'bar'
        >>> del node.attrs['id']
        >>> node.attributes
        {'foo': 'bar'}
        >>> node.attrs['id'] = 'new_id'
        >>> node.html
        '<div foo="bar" id="new_id"></div>'
        """
        ...
    @property
    def id(self) -> str | None:
        """Get the id attribute of the node.

        Returns None if id does not set.

        Returns
        -------
        text : str
        """
        ...

    def mem_id(self) -> int:
        """Get the mem_id attribute of the node.

        Returns
        -------
        text : int
        """
        ...

    def __hash__(self) -> int:
        """Get the hash of this node
        :return: int
        """
        ...
    def text(self, deep: bool = True, separator: str = "", strip: bool = False) -> str:
        """Returns the text of the node including text of all its child nodes.

        Parameters
        ----------
        strip : bool, default False
            If true, calls ``str.strip()`` on each text part to remove extra white spaces.
        separator : str, default ''
            The separator to use when joining text from different nodes.
        deep : bool, default True
            If True, includes text from all child nodes.

        Returns
        -------
        text : str
        """
        ...
    def iter(self, include_text: bool = False) -> Iterator[Node]:
        """Iterate over nodes on the current level.

        Parameters
        ----------
        include_text : bool
            If True, includes text nodes as well.

        Yields
        -------
        node
        """
        ...
    def traverse(self, include_text: bool = False) -> Iterator[Node]:
        """Iterate over all child and next nodes starting from the current level.

        Parameters
        ----------
        include_text : bool
            If True, includes text nodes as well.

        Yields
        -------
        node
        """
        ...
    @property
    def tag(self) -> str:
        """Return the name of the current tag (e.g. div, p, img).

        Returns
        -------
        text : str
        """
        ...
    @property
    def child(self) -> Node | None:
        """Alias for the `first_child` property.

        **Deprecated**. Please use `first_child` instead.
        """
        ...
    @property
    def parent(self) -> Node | None:
        """Return the parent node."""
        ...
    @property
    def next(self) -> Node | None:
        """Return next node."""
        ...
    @property
    def prev(self) -> Node | None:
        """Return previous node."""
        ...
    @property
    def last_child(self) -> Node | None:
        """Return last child node."""
        ...
    @property
    def html(self) -> str | None:
        """Return HTML representation of the current node including all its child nodes.

        Returns
        -------
        text : str
        """
        ...
    def css(self, query: str) -> list[Node]:
        """Evaluate CSS selector against current node and its child nodes."""
        ...
    def any_css_matches(self, selectors: tuple[str]) -> bool:
        """Returns True if any of CSS selectors matches a node"""
        ...
    def css_matches(self, selector: str) -> bool:
        """Returns True if CSS selector matches a node."""
        ...
    @overload
    def css_first(
        self, query: str, default: DefaultT, strict: bool = False
    ) -> Node | DefaultT: ...
    @overload
    def css_first(
        self, query: str, default: None = None, strict: bool = False
    ) -> Node | None | DefaultT:
        """Evaluate CSS selector against current node and its child nodes."""
        ...
    def decompose(self, recursive: bool = True) -> None:
        """Remove a Node from the tree.

        Parameters
        ----------
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = HTMLParser(html)
        >>> for tag in tree.css('script'):
        >>>     tag.decompose()
        """
        ...
    def remove(self, recursive: bool = True) -> None:
        """An alias for the decompose method."""
        ...
    def unwrap(self, delete_empty: bool = False) -> None:
        """Replace node with whatever is inside this node.

        Parameters
        ----------
        delete_empty : bool, default False
            Whenever to delete empty tags.

        Examples
        --------

        >>>  tree = HTMLParser("<div>Hello <i>world</i>!</div>")
        >>>  tree.css_first('i').unwrap()
        >>>  tree.html
        '<html><head></head><body><div>Hello world!</div></body></html>'

        Note: by default, empty tags are ignored, set "delete_empty" to "True" to change this.
        """
        ...
    def strip_tags(self, tags: list[str], recursive: bool = False) -> None:
        """Remove specified tags from the HTML tree.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = HTMLParser('<html><head></head><body><script></script><div>Hello world!</div></body></html>')
        >>> tags = ['head', 'style', 'script', 'xmp', 'iframe', 'noembed', 'noframes']
        >>> tree.strip_tags(tags)
        >>> tree.html
        '<html><body><div>Hello world!</div></body></html>'
        """
        ...
    def unwrap_tags(self, tags: list[str], delete_empty: bool = False) -> None:
        """Unwraps specified tags from the HTML tree.

        Works the same as the unwrap method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool, default False
            Whenever to delete empty tags.

        Examples
        --------

        >>> tree = HTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.body.unwrap_tags(['i','a'])
        >>> tree.body.html
        '<body><div>Hello world!</div></body>'

        Note: by default, empty tags are ignored, set "delete_empty" to "True" to change this.
        """
        ...
    def replace_with(self, value: str | bytes | None) -> None:
        """Replace current Node with specified value.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to replace the Node with.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = HTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.replace_with(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get Laptop</div>'

        >>> html_parser = HTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = HTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.replace_with(html_parser2.body.child)
        '<div>Get <span alt="Laptop"><div>Test</div> <div></div></span></div>'
        """
        ...
    def insert_before(self, value: str | bytes | None) -> None:
        """Insert a node before the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert before the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = HTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.insert_before(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get Laptop<img src="" alt="Laptop"></div>'

        >>> html_parser = HTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = HTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.insert_before(html_parser2.body.child)
        <div>Get <span alt="Laptop"><div>Test</div><img src="/jpg"> <div></div></span></div>'
        """
        ...
    def insert_after(self, value: str | bytes | None) -> None:
        """Insert a node after the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert after the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = HTMLParser('<div>Get <img src="" alt="Laptop"></div>')
        >>> img = tree.css_first('img')
        >>> img.insert_after(img.attributes.get('alt', ''))
        >>> tree.body.child.html
        '<div>Get <img src="" alt="Laptop">Laptop</div>'

        >>> html_parser = HTMLParser('<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>')
        >>> html_parser2 = HTMLParser('<div>Test</div>')
        >>> img_node = html_parser.css_first('img')
        >>> img_node.insert_after(html_parser2.body.child)
        <div>Get <span alt="Laptop"><img src="/jpg"><div>Test</div> <div></div></span></div>'
        """
        ...
    def insert_child(self, value: str | bytes | None) -> None:
        """Insert a node inside (at the end of) the current Node.

        Parameters
        ----------
        value : str, bytes or Node
            The text or Node instance to insert inside the Node.
            When a text string is passed, it's treated as text. All HTML tags will be escaped.
            Convert and pass the ``Node`` object when you want to work with HTML.
            Does not clone the ``Node`` object.
            All future changes to the passed ``Node`` object will also be taken into account.

        Examples
        --------

        >>> tree = HTMLParser('<div>Get <img src=""></div>')
        >>> div = tree.css_first('div')
        >>> div.insert_child('Laptop')
        >>> tree.body.child.html
        '<div>Get <img src="">Laptop</div>'

        >>> html_parser = HTMLParser('<div>Get <span alt="Laptop"> <div>Laptop</div> </span></div>')
        >>> html_parser2 = HTMLParser('<div>Test</div>')
        >>> span_node = html_parser.css_first('span')
        >>> span_node.insert_child(html_parser2.body.child)
        <div>Get <span alt="Laptop"> <div>Laptop</div> <div>Test</div> </span></div>'
        """
        ...
    @property
    def raw_value(self) -> bytes:
        """Return the raw (unparsed, original) value of a node.

        Currently, works on text nodes only.

        Returns
        -------

        raw_value : bytes

        Examples
        --------

        >>> html_parser = HTMLParser('<div>&#x3C;test&#x3E;</div>')
        >>> selector = html_parser.css_first('div')
        >>> selector.child.html
        '&lt;test&gt;'
        >>> selector.child.raw_value
        b'&#x3C;test&#x3E;'
        """
        ...
    def select(self, query: str | None = None) -> Selector:
        """Select nodes given a CSS selector.

        Works similarly to the css method, but supports chained filtering and extra features.

        Parameters
        ----------
        query : str or None
            The CSS selector to use when searching for nodes.

        Returns
        -------
        selector : The `Selector` class.
        """
        ...
    def scripts_contain(self, query: str) -> bool:
        """Returns True if any of the script tags contain specified text.

        Caches script tags on the first call to improve performance.

        Parameters
        ----------
        query : str
            The query to check.
        """
        ...
    def script_srcs_contain(self, queries: tuple[str]) -> bool:
        """Returns True if any of the script SRCs attributes contain on of the specified text.

        Caches values on the first call to improve performance.

        Parameters
        ----------
        queries : tuple of str
        """
        ...
    @property
    def text_content(self) -> str | None:
        """Returns the text of the node if it is a text node.

        Returns None for other nodes.
        Unlike the ``text`` method, does not include child nodes.

        Returns
        -------
        text : str or None.
        """
        ...
    def merge_text_nodes(self):
        """Iterates over all text nodes and merges all text nodes that are close to each other.

        This is useful for text extraction.
        Use it when you need to strip HTML tags and merge "dangling" text.

        Examples
        --------

        >>> tree = HTMLParser("<div><p><strong>J</strong>ohn</p><p>Doe</p></div>")
        >>> node = tree.css_first('div')
        >>> tree.unwrap_tags(["strong"])
        >>> tree.text(deep=True, separator=" ", strip=True)
        "J ohn Doe" # Text extraction produces an extra space because the strong tag was removed.
        >>> node.merge_text_nodes()
        >>> tree.text(deep=True, separator=" ", strip=True)
        "John Doe"
        """
        ...

class HTMLParser:
    """The HTML parser using modest backend.

    This backend is **deprecated**. Please use `lexbor` backend instead.

    Use this class to parse raw HTML.

    Parameters
    ----------

    html : str (unicode) or bytes
    detect_encoding : bool, default True
        If `True` and html type is `bytes` then encoding will be detected automatically.
    use_meta_tags : bool, default True
        Whether to use meta tags in encoding detection process.
    decode_errors : str, default 'ignore'
        Same as in builtin's str.decode, i.e 'strict', 'ignore' or 'replace'.
    """

    def __init__(
        self,
        html: bytes | str,
        detect_encoding: bool = True,
        use_meta_tags: bool = True,
        decode_errors: Literal["strict", "ignore", "replace"] = "ignore",
    ): ...
    def css(self, query: str) -> list[Node]:
        """A CSS selector.

        Matches pattern `query` against HTML tree.
        `CSS selectors reference <https://www.w3schools.com/cssref/css_selectors.asp>`_.

        Parameters
        ----------
        query : str
            CSS selector (e.g. "div > :nth-child(2n+1):not(:has(a))").

        Returns
        -------
        selector : list of `Node` objects
        """
        ...
    @overload
    def css_first(
        self, query: str, default: DefaultT, strict: bool = False
    ) -> Node | DefaultT: ...
    @overload
    def css_first(
        self, query: str, default: None = None, strict: bool = False
    ) -> Node | None | DefaultT:
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : bool, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `Node` object
        """
        ...
    @property
    def input_encoding(self) -> str:
        """Return encoding of the HTML document.

        Returns `unknown` in case the encoding is not determined.
        """
        ...
    @property
    def root(self) -> Node | None:
        """Returns root node."""
        ...
    @property
    def head(self) -> Node | None:
        """Returns head node."""
        ...
    @property
    def body(self) -> Node | None:
        """Returns document body."""
        ...
    def tags(self, name: str) -> list[Node]:
        """Returns a list of tags that match specified name.

        Parameters
        ----------
        name : str (e.g. div)
        """
        ...
    def text(self, deep: bool = True, separator: str = "", strip: bool = False) -> str:
        """Returns the text of the node including text of all its child nodes.

        Parameters
        ----------
        strip : bool, default False
            If true, calls ``str.strip()`` on each text part to remove extra white spaces.
        separator : str, default ''
            The separator to use when joining text from different nodes.
        deep : bool, default True
            If True, includes text from all child nodes.

        Returns
        -------
        text : str
        """
        ...
    def strip_tags(self, tags: list[str], recursive: bool = False) -> None:
        """Remove specified tags from the node.

        Parameters
        ----------
        tags : list of str
            List of tags to remove.
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = HTMLParser('<html><head></head><body><script></script><div>Hello world!</div></body></html>')
        >>> tags = ['head', 'style', 'script', 'xmp', 'iframe', 'noembed', 'noframes']
        >>> tree.strip_tags(tags)
        >>> tree.html
        '<html><body><div>Hello world!</div></body></html>'
        """
        ...
    def unwrap_tags(self, tags: list[str], delete_empty: bool = False) -> None:
        """Unwraps specified tags from the HTML tree.

        Works the same as th unwrap method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool, default False
            If True, removes empty tags.

        Examples
        --------

        >>> tree = HTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.head.unwrap_tags(['i','a'])
        >>> tree.head.html
        '<body><div>Hello world!</div></body>'
        """
        ...
    @property
    def html(self) -> str | None:
        """Return HTML representation of the page."""
        ...
    def select(self, query: str | None = None) -> Selector | None:
        """Select nodes given a CSS selector.

        Works similarly to  the ``css`` method, but supports chained filtering and extra features.

        Parameters
        ----------
        query : str or None
            The CSS selector to use when searching for nodes.

        Returns
        -------
        selector : The `Selector` class.
        """
        ...
    def any_css_matches(self, selectors: tuple[str]) -> bool:
        """Returns True if any of the specified CSS selectors matches a node."""
        ...
    def scripts_contain(self, query: str) -> bool:
        """Returns True if any of the script tags contain specified text.

        Caches script tags on the first call to improve performance.

        Parameters
        ----------
        query : str
            The query to check.
        """
        ...
    def scripts_srcs_contain(self, queries: tuple[str]) -> bool:
        """Returns True if any of the script SRCs attributes contain on of the specified text.

        Caches values on the first call to improve performance.

        Parameters
        ----------
        queries : tuple of str
        """
        ...
    def css_matches(self, selector: str) -> bool: ...
    def clone(self) -> HTMLParser:
        """Clone the current tree."""
        ...
    def merge_text_nodes(self):
        """Iterates over all text nodes and merges all text nodes that are close to each other.

        This is useful for text extraction.
        Use it when you need to strip HTML tags and merge "dangling" text.

        Examples
        --------

        >>> tree = HTMLParser("<div><p><strong>J</strong>ohn</p><p>Doe</p></div>")
        >>> node = tree.css_first('div')
        >>> tree.unwrap_tags(["strong"])
        >>> tree.text(deep=True, separator=" ", strip=True)
        "J ohn Doe" # Text extraction produces an extra space because the strong tag was removed.
        >>> node.merge_text_nodes()
        >>> tree.text(deep=True, separator=" ", strip=True)
        "John Doe"
        """
        ...

def create_tag(tag: str) -> Node:
    """
    Given an HTML tag name, e.g. `"div"`, create a single empty node for that tag,
    e.g. `"<div></div>"`.
    """
    ...

def parse_fragment(html: str) -> list[Node]:
    """
    Given HTML, parse it into a list of Nodes, such that the nodes
    correspond to the given HTML.

    For contrast, HTMLParser adds `<html>`, `<head>`, and `<body>` tags
    if they are missing. This function does not add these tags.
    """
    ...

```

### `selectolax/parser.pyx`

```pyx

from cpython.bool cimport bool
from cpython.exc cimport PyErr_SetObject

include "modest/selection.pxi"
include "modest/node.pxi"
include "modest/util.pxi"
include "utils.pxi"

cdef class HTMLParser:
    """The HTML parser using modest backend.

    This backend is **deprecated**. Please use `lexbor` backend instead.

    Use this class to parse raw HTML.

    Parameters
    ----------

    html : str (unicode) or bytes
    detect_encoding : bool, default True
        If `True` and html type is `bytes` then encoding will be detected automatically.
    use_meta_tags : bool, default True
        Whether to use meta tags in encoding detection process.
    decode_errors : str, default 'ignore'
        Same as in builtin's str.decode, i.e 'strict', 'ignore' or 'replace'.
    """
    def __init__(self, html, detect_encoding=True, use_meta_tags=True, decode_errors = 'ignore'):

        cdef size_t html_len
        cdef char* html_chars

        self.detect_encoding = detect_encoding
        self.use_meta_tags = use_meta_tags
        self.decode_errors = decode_errors
        self._encoding = MyENCODING_UTF_8

        bytes_html, html_len = preprocess_input(html, decode_errors)
        html_chars = <char*> bytes_html

        if detect_encoding and isinstance(html, bytes):
            self._detect_encoding(html_chars, html_len)

        self._parse_html(html_chars, html_len)

        self.raw_html = bytes_html
        self.cached_script_texts = None
        self.cached_script_srcs = None

    def css(self, str query):
        """A CSS selector.

        Matches pattern `query` against HTML tree.
        `CSS selectors reference <https://www.w3schools.com/cssref/css_selectors.asp>`_.

        Parameters
        ----------
        query : str
            CSS selector (e.g. "div > :nth-child(2n+1):not(:has(a))").

        Returns
        -------
        selector : list of `Node` objects

        """

        cdef Node node = Node.new(self.html_tree.node_html, self)
        return node.css(query)

    def css_first(self, str query, default=None, strict=False):
        """Same as `css` but returns only the first match.

        Parameters
        ----------

        query : str
        default : Any, default None
            Default value to return if there is no match.
        strict: bool, default False
            Set to True if you want to check if there is strictly only one match in the document.


        Returns
        -------
        selector : `Node` object

        """

        cdef Node node = Node.new(self.html_tree.node_html, self)
        return node.css_first(query, default, strict)

    cdef void _detect_encoding(self, char* html, size_t html_len) nogil:
        cdef myencoding_t encoding = MyENCODING_DEFAULT

        if self.use_meta_tags:
            encoding = myencoding_prescan_stream_to_determine_encoding(html, html_len)
            if encoding != MyENCODING_DEFAULT and encoding != MyENCODING_NOT_DETERMINED:
                self._encoding = encoding
                return

        if not myencoding_detect_bom(html, html_len, &encoding):
            myencoding_detect(html, html_len, &encoding)

        self._encoding = encoding

    cdef int _parse_html(self, char* html, size_t html_len) except -1:
        cdef myhtml_t* myhtml
        cdef mystatus_t status

        with nogil:
            myhtml = myhtml_create()
            status = myhtml_init(myhtml, MyHTML_OPTIONS_DEFAULT, 1, 0)

        if status != 0:
            PyErr_SetObject(RuntimeError, "Can't init MyHTML object.")
            return -1

        with nogil:
            self.html_tree = myhtml_tree_create()
            status = myhtml_tree_init(self.html_tree, myhtml)

        if status != 0:
            PyErr_SetObject(RuntimeError, "Can't init MyHTML Tree object.")
            return -1

        with nogil:
            status = myhtml_parse(self.html_tree, self._encoding, html, html_len)

        if status != 0:
            PyErr_SetObject(RuntimeError, "Can't parse HTML (status code: %d)" % status)
            return -1

        if self.html_tree.node_html == NULL:
            PyErr_SetObject(RuntimeError, "html_tree is still NULL even after parsing ")
            return -1
        return 0

    @property
    def input_encoding(self):
        """Return encoding of the HTML document.

        Returns `unknown` in case the encoding is not determined.
        """
        cdef const char* encoding
        encoding = myencoding_name_by_id(self._encoding, NULL)

        if encoding != NULL:
            return encoding.decode('utf-8')
        else:
            return 'unknown'

    @property
    def root(self):
        """Returns root node."""
        if self.html_tree and self.html_tree.node_html:
            try:
                return Node.new(self.html_tree.node_html, self)
            except Exception:
                # If Node creation or initialization fails, return None
                return None
        return None

    @property
    def head(self):
        """Returns head node."""
        cdef myhtml_tree_node_t* head
        head = myhtml_tree_get_node_head(self.html_tree)

        if head != NULL:
            return Node.new(head, self)
        return None

    @property
    def body(self):
        """Returns document body."""
        cdef myhtml_tree_node_t* body
        body = myhtml_tree_get_node_body(self.html_tree)

        if body != NULL:
            return Node.new(body, self)
        return None

    def tags(self, str name):
        """Returns a list of tags that match specified name.

        Parameters
        ----------
        name : str (e.g. div)

        """
        # Validate tag name
        if not name:
            raise ValueError("Tag name cannot be empty")
        if len(name) > 100:  # Reasonable limit for tag names
            raise ValueError("Tag name is too long")

        cdef myhtml_collection_t* collection = NULL
        pybyte_name = name.encode('UTF-8')
        cdef mystatus_t status = 0

        result = list()
        collection = myhtml_get_nodes_by_name(self.html_tree, NULL, pybyte_name, len(pybyte_name), &status)

        if collection == NULL:
            return result

        if status == 0:
            for i in range(collection.length):
                node = Node.new(collection.list[i], self)
                result.append(node)

        myhtml_collection_destroy(collection)

        return result

    def text(self, bool deep=True, str separator='', bool strip=False):
        """Returns the text of the node including text of all its child nodes.

        Parameters
        ----------
        strip : bool, default False
            If true, calls ``str.strip()`` on each text part to remove extra white spaces.
        separator : str, default ''
            The separator to use when joining text from different nodes.
        deep : bool, default True
            If True, includes text from all child nodes.

        Returns
        -------
        text : str

        """
        if not self.body:
            return ""
        return self.body.text(deep=deep, separator=separator, strip=strip)

    def strip_tags(self, list tags, bool recursive = False):
        """Remove specified tags from the node.

        Parameters
        ----------
        tags : list of str
            List of tags to remove.
        recursive : bool, default True
            Whenever to delete all its child nodes

        Examples
        --------

        >>> tree = HTMLParser('<html><head></head><body><script></script><div>Hello world!</div></body></html>')
        >>> tags = ['head', 'style', 'script', 'xmp', 'iframe', 'noembed', 'noframes']
        >>> tree.strip_tags(tags)
        >>> tree.html
        '<html><body><div>Hello world!</div></body></html>'

        """
        cdef myhtml_collection_t* collection = NULL

        cdef mystatus_t status = 0

        for tag in tags:
            pybyte_name = tag.encode('UTF-8')
            collection = myhtml_get_nodes_by_name(self.html_tree, NULL, pybyte_name, len(pybyte_name), &status)

            if collection == NULL:
                continue

            if status != 0:
                continue

            for i in range(collection.length):
                if recursive:
                    myhtml_node_delete_recursive(collection.list[i])
                else:
                    myhtml_node_delete(collection.list[i])

            myhtml_collection_destroy(collection)

    def unwrap_tags(self, list tags, delete_empty : bool = False):
        """Unwraps specified tags from the HTML tree.

        Works the same as th `unwrap` method, but applied to a list of tags.

        Parameters
        ----------
        tags : list
            List of tags to remove.
        delete_empty : bool, default False
            If True, removes empty tags.

        Examples
        --------

        >>> tree = HTMLParser("<div><a href="">Hello</a> <i>world</i>!</div>")
        >>> tree.head.unwrap_tags(['i','a'])
        >>> tree.head.html
        '<body><div>Hello world!</div></body>'
        """
        if self.root is not None:
            self.root.unwrap_tags(tags, delete_empty=delete_empty)

    @property
    def html(self):
        """Return HTML representation of the page."""
        cdef Node node
        if self.html_tree != NULL and self.html_tree.document != NULL:
            node = Node.new(self.html_tree.document, self)
            return node.html
        return None

    def select(self, query=None):
        """Select nodes given a CSS selector.

        Works similarly to  the ``css`` method, but supports chained filtering and extra features.

        Parameters
        ----------
        query : str or None
            The CSS selector to use when searching for nodes.

        Returns
        -------
        selector : The `Selector` class.
        """
        cdef Node node
        node = self.root
        if node:
            return Selector(node, query)

    def any_css_matches(self, tuple selectors):
        """Returns True if any of the specified CSS selectors matches a node."""
        return self.root.any_css_matches(selectors)

    def scripts_contain(self, str query):
        """Returns True if any of the script tags contain specified text.

        Caches script tags on the first call to improve performance.

        Parameters
        ----------
        query : str
            The query to check.

        """
        return self.root.scripts_contain(query)

    def script_srcs_contain(self, tuple queries):
        """Returns True if any of the script SRCs attributes contain on of the specified text.

        Caches values on the first call to improve performance.

        Parameters
        ----------
        queries : tuple of str

        """
        return self.root.script_srcs_contain(queries)

    def css_matches(self, str selector):
        return self.root.css_matches(selector)

    def merge_text_nodes(self):
        """Iterates over all text nodes and merges all text nodes that are close to each other.

        This is useful for text extraction.
        Use it when you need to strip HTML tags and merge "dangling" text.

        Examples
        --------

        >>> tree = HTMLParser("<div><p><strong>J</strong>ohn</p><p>Doe</p></div>")
        >>> node = tree.css_first('div')
        >>> tree.unwrap_tags(["strong"])
        >>> tree.text(deep=True, separator=" ", strip=True)
        "J ohn Doe" # Text extraction produces an extra space because the strong tag was removed.
        >>> node.merge_text_nodes()
        >>> tree.text(deep=True, separator=" ", strip=True)
        "John Doe"
        """
        return self.root.merge_text_nodes()

    @staticmethod
    cdef HTMLParser from_tree(
            myhtml_tree_t * tree, bytes raw_html, bint detect_encoding, bint use_meta_tags, str decode_errors,
            myencoding_t encoding
    ):
        obj = <HTMLParser> HTMLParser.__new__(HTMLParser)
        obj.html_tree = tree
        obj.raw_html = raw_html
        obj.detect_encoding = detect_encoding
        obj.use_meta_tags = use_meta_tags
        obj.decode_errors = decode_errors
        obj._encoding = encoding
        obj.cached_script_texts = None
        obj.cached_script_srcs = None
        return obj

    def clone(self):
        """Clone the current tree."""
        cdef myhtml_t* myhtml
        cdef mystatus_t status
        cdef myhtml_tree_t* html_tree
        cdef myhtml_tree_node_t* node
        cdef HTMLParser cls

        with nogil:
            myhtml = myhtml_create()
            status = myhtml_init(myhtml, MyHTML_OPTIONS_DEFAULT, 1, 0)

        if status != 0:
            raise RuntimeError("Can't init MyHTML object.")

        with nogil:
            html_tree = myhtml_tree_create()
            status = myhtml_tree_init(html_tree, myhtml)

        if status != 0:
            raise RuntimeError("Can't init MyHTML Tree object.")

        node = myhtml_node_clone_deep(html_tree, self.html_tree.node_html)
        myhtml_tree_node_add_child(html_tree.document, node)
        html_tree.node_html = node

        cls = HTMLParser.from_tree(
            html_tree,
            self.raw_html,
            self.detect_encoding,
            self.use_meta_tags,
            self.decode_errors,
            self._encoding
        )
        return cls

    def __dealloc__(self):
        cdef myhtml_t* myhtml

        if self.html_tree != NULL:
            myhtml = self.html_tree.myhtml
            myhtml_tree_destroy(self.html_tree)
            self.html_tree = NULL  # Prevent double-free
            if myhtml != NULL:
                myhtml_destroy(myhtml)

    def __repr__(self):
        return '<HTMLParser chars=%s>' % len(self.root.html)

```

### `selectolax/py.typed`

```typed

```

### `selectolax/utils.pxi`

```pxi
from typing import Literal, Optional, Union, Type

MAX_HTML_INPUT_SIZE = 250e+7

ParserCls = Union[Type["HTMLParser"], Type["LexborHTMLParser"]]
Parser = Union["HTMLParser", "LexborHTMLParser"]
FRAGMENT = Literal[
    "document",
    "fragment",
    "head",
    "body",
    "head_and_body",
    "document_no_head",
    "document_no_body",
    "document_no_head_no_body",
]


def preprocess_input(html, decode_errors='ignore'):
    if isinstance(html, (str, unicode)):
        bytes_html = html.encode('UTF-8', errors=decode_errors)
    elif isinstance(html, bytes):
        bytes_html = html
    else:
        raise TypeError("Expected a string, but %s found" % type(html).__name__)
    html_len = len(bytes_html)
    if html_len > MAX_HTML_INPUT_SIZE:
        raise ValueError("The specified HTML input is too large to be processed (%d bytes)" % html_len)
    return bytes_html, html_len


def do_create_tag(tag: str, parser_cls: ParserCls):
    if not tag:
        raise ValueError("Tag name cannot be empty")
    return do_parse_fragment(f"<{tag}></{tag}>", parser_cls)[0]


def get_fragment_type(
    html: str,
    parser_cls: ParserCls,
    tree: Optional[Parser] = None,
) -> FRAGMENT:
    if not tree:
        tree = parser_cls(html)

    import re
    html_re = re.compile(r"<html|<body|<head(?!er)", re.IGNORECASE)

    has_html = False
    has_head = False
    has_body = False
    for match in html_re.finditer(html):
        if match[0] == "<html":
            has_html = True
        elif match[0] == "<head":
            has_head = True
        elif match[0] == "<body":
            has_body = True

        if has_html and has_head and has_body:
            break

    if has_html and has_head and has_body:
        return "document"
    elif has_html and not has_head and has_body:
        return "document_no_head"
    elif has_html and has_head and not has_body:
        return "document_no_body"
    elif has_html and not has_head and not has_body:
        return "document_no_head_no_body"
    elif has_head and not has_body:
        return "head"
    elif not has_head and has_body:
        return "body"
    elif has_head and has_body:
        return "head_and_body"
    else:
        return "fragment"


def do_parse_fragment(html: str, parser_cls: ParserCls):
    """
    Given HTML, parse it into a list of Nodes, such that the nodes
    correspond to the given HTML.

    For contrast, HTMLParser adds `<html>`, `<head>`, and `<body>` tags
    if they are missing. This function does not add these tags.
    """
    html = html.strip()
    tree = parser_cls(html)
    frag_type = get_fragment_type(html, parser_cls, tree)

    if frag_type == "document":
        return [tree.root]
    if frag_type == "document_no_head":
        tree.head.decompose(recursive=True)
        return [tree.root]
    if frag_type == "document_no_body":
        tree.body.decompose(recursive=True)
        return [tree.root]
    if frag_type == "document_no_head_no_body":
        tree.head.decompose(recursive=True)
        tree.body.decompose(recursive=True)
        return [tree.root]
    elif frag_type == "head":
        tree.body.decompose(recursive=True)
        return [tree.head]
    elif frag_type == "body":
        tree.head.decompose(recursive=True)
        return [tree.body]
    elif frag_type == "head_and_body":
        return [tree.head, tree.body]
    else:
        return [
            *tree.head.iter(include_text=True),
            *tree.body.iter(include_text=True),
        ]

```

### `setup.cfg`

```cfg
[bumpversion]
current_version = 0.4.11
commit = True
tag = True

[bumpversion:file:setup.py]
search = version="{current_version}"
replace = version="{new_version}"

[bumpversion:file:selectolax/__init__.py]
search = __version__ = "{current_version}"
replace = __version__ = "{new_version}"

[bumpversion:file:pyproject.toml]
search = version = '{current_version}'
replace = version = '{new_version}'

[pycodestyle]
max-line-length = 120

```

### `setup.py`

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import platform
import logging

import sys
from setuptools import setup, find_packages, Extension


logging.basicConfig(level=logging.INFO)

with io.open("README.md", mode="rt", encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Setup flags
USE_STATIC = False
USE_CYTHON = False
PLATFORM = "windows_nt" if platform.system() == "Windows" else "posix"
INCLUDE_LEXBOR = bool(os.environ.get("USE_LEXBOR", True))
INCLUDE_MODEST = bool(os.environ.get("USE_MODEST", True))

ARCH = platform.architecture()[0]

try:
    from Cython.Build import cythonize

    HAS_CYTHON = True
    USE_CYTHON = True
except ImportError as err:
    HAS_CYTHON = False

if "--static" in sys.argv:
    USE_STATIC = True
    sys.argv.remove("--static")

if "--lexbor" in sys.argv:
    INCLUDE_LEXBOR = True
    sys.argv.remove("--lexbor")

if "--disable-modest" in sys.argv:
    INCLUDE_MODEST = False
    sys.argv.remove("--disable-modest")

if "--cython" in sys.argv:
    if HAS_CYTHON:
        USE_CYTHON = True
    else:
        raise ImportError("No module named 'Cython'")
    sys.argv.remove("--cython")

# If there are no pretranspiled source files
if HAS_CYTHON and not os.path.exists("selectolax/parser.c"):
    USE_CYTHON = True

COMPILER_DIRECTIVES = {
    "language_level": 3,
    "embedsignature": True,
    "annotation_typing": False,
    "emit_code_comments": True,
    "boundscheck": False,
    "wraparound": False,
    "freethreading_compatible": "True",
    "subinterpreters_compatible": "own_gil",
}


def find_modest_files(modest_path="modest/source"):
    c_files = []
    if os.path.exists(modest_path):
        for root, dirs, files in os.walk(modest_path):
            for file in files:
                if file.endswith(".c"):
                    file_path = os.path.join(root, file)

                    # Filter platform specific files
                    if (file_path.find("myport") >= 0) and (
                        not file_path.find(PLATFORM) >= 0
                    ):
                        continue

                    if INCLUDE_LEXBOR:
                        if (file_path.find("ports") >= 0) and (
                            not file_path.find(PLATFORM) >= 0
                        ):
                            continue
                    c_files.append(file_path)
    return c_files


def make_extensions():
    logging.info(f"USE_CYTHON: {USE_CYTHON}")
    logging.info(f"INCLUDE_LEXBOR: {INCLUDE_LEXBOR}")
    logging.info(f"INCLUDE_MODEST: {INCLUDE_MODEST}")
    logging.info(f"USE_STATIC: {USE_STATIC}")

    files_to_compile_lxb = []
    files_to_compile = []
    extra_objects_lxb, extra_objects = [], []

    if USE_CYTHON:
        if INCLUDE_MODEST:
            files_to_compile = [
                "selectolax/parser.pyx",
            ]
        if INCLUDE_LEXBOR:
            files_to_compile_lxb = [
                "selectolax/lexbor.pyx",
            ]
    else:
        if INCLUDE_MODEST:
            files_to_compile = ["selectolax/parser.c"]
        if INCLUDE_LEXBOR:
            files_to_compile_lxb = [
                "selectolax/lexbor.c",
            ]

    if USE_STATIC:
        if INCLUDE_MODEST:
            extra_objects = ["modest/lib/libmodest_static.a"]
        if INCLUDE_LEXBOR:
            extra_objects_lxb = ["lexbor/liblexbor_static.a"]
    else:
        if INCLUDE_MODEST:
            files_to_compile.extend(find_modest_files("modest/source"))
        if INCLUDE_LEXBOR:
            files_to_compile_lxb.extend(find_modest_files("lexbor/source"))

    compile_arguments_lxb = [
        "-DLEXBOR_STATIC",
    ]
    compile_arguments = [
        "-DMODEST_BUILD_OS=%s" % platform.system(),
        "-DMyCORE_OS_%s" % platform.system(),
        "-DMODEST_PORT_NAME=%s" % PLATFORM,
        "-DMyCORE_BUILD_WITHOUT_THREADS=YES",
        "-DMyCORE_BUILD_DEBUG=NO",
    ]

    if PLATFORM == "posix":
        args = [
            "-pedantic",
            "-fPIC",
            "-Wno-unused-variable",
            "-Wno-unused-function",
            "-std=c99",
            "-O0",
            "-g",
        ]
        compile_arguments.extend(args)
        compile_arguments_lxb.extend(args)
    elif PLATFORM == "windows_nt":
        compile_arguments_lxb.extend(
            [
                "-D_WIN64" if ARCH == "64bit" else "-D_WIN32",
            ]
        )

    extensions = []
    if INCLUDE_MODEST:
        extensions.append(
            Extension(
                "selectolax.parser",
                files_to_compile,
                language="c",
                include_dirs=[
                    "modest/include/",
                ],
                extra_objects=extra_objects,
                extra_compile_args=compile_arguments,
            )
        )

    if INCLUDE_LEXBOR:
        extensions.append(
            Extension(
                "selectolax.lexbor",
                files_to_compile_lxb,
                language="c",
                include_dirs=[
                    "lexbor/source/",
                ],
                extra_objects=extra_objects_lxb,
                extra_compile_args=compile_arguments_lxb,
            )
        )
    if USE_CYTHON:
        extensions = cythonize(extensions, compiler_directives=COMPILER_DIRECTIVES)

    return extensions


setup(
    name="selectolax",
    version="0.4.11",
    description="A fast HTML5 parser with CSS selectors, written in Cython, using Modest and Lexbor engines.",
    long_description=readme,
    author="Artem Golubin",
    author_email="me@rushter.com",
    url="https://github.com/rushter/selectolax",
    packages=find_packages(include=["selectolax"]),
    package_data={"selectolax": ["py.typed"]},
    include_package_data=True,
    zip_safe=False,
    ext_modules=make_extensions(),
)

```

### `tests/__init__.py`

```py
# -*- coding: utf-8 -*-

"""Unit test package for selectolax."""

```

### `tests/test_lexbor_fragment.py`

```py
from inspect import cleandoc
import pytest
from selectolax.lexbor import LexborHTMLParser


def clean_doc(text: str) -> str:
    return f"{cleandoc(text)}\n"


def test_fragment_parser_top_level_tags():
    parser = LexborHTMLParser(
        "<div><span>\n \n</span><title>X</title></div>", is_fragment=False
    )
    assert parser is not None and isinstance(parser, LexborHTMLParser)
    assert (
        parser.html
        == "<html><head></head><body><div><span>\n \n</span><title>X</title></div></body></html>"
    )
    assert (
        parser.root.html
        == "<html><head></head><body><div><span>\n \n</span><title>X</title></div></body></html>"
    )
    assert parser.head is not None
    assert parser.body is not None
    parser = LexborHTMLParser(
        "<div><span>\n \n</span><title>X</title></div>", is_fragment=True
    )
    assert parser.html == "<div><span>\n \n</span><title>X</title></div>"
    assert parser.root.html == "<div><span>\n \n</span><title>X</title></div>"
    assert parser.head is None
    assert parser.body is None
    parser = LexborHTMLParser(
        "<html><body><div><span>\n \n</span><title>X</title></div></body></html>",
        is_fragment=True,
    )
    assert parser.html == "<div><span>\n \n</span><title>X</title></div>"


def test_fragment_parser_multiple_nodes_on_the_same_level():
    html = clean_doc("""
          <meta charset="utf-8">
          <meta content="width=device-width,initial-scale=1" name="viewport">
          <title>Title!</title>
          <!-- My crazy comment -->
          <p>Hello <strong>World</strong>!</p>
    """)
    parser = LexborHTMLParser(html, is_fragment=True)
    expected_html = clean_doc("""
          <meta charset="utf-8">
          <meta content="width=device-width,initial-scale=1" name="viewport">
          <title>Title!</title>
          <!-- My crazy comment -->
          <p>Hello <strong>World</strong>!</p>

    """)
    assert parser.html == expected_html


def test_fragment_parser_whole_doc():
    html = """<html lang="en">
            <head><meta charset="utf-8"><title>Title!</title></head>
            <body><p>Lorem <strong>Ipsum</strong>!</p></body>
        </html>"""
    parser = LexborHTMLParser(html, is_fragment=True)
    expected_html = '<meta charset="utf-8"><title>Title!</title>\n            <p>Lorem <strong>Ipsum</strong>!</p>'
    html = parser.html
    assert html is not None
    assert html.strip() == expected_html


@pytest.mark.parametrize(
    "html, expected_html",
    [
        ("<body><div>Test</div></body>", "<div>Test</div>"),
        ("  <div>Lorep Ipsum</div>", "  <div>Lorep Ipsum</div>"),
        ("<div>Lorem</div><div>Ipsum</div>", "<div>Lorem</div><div>Ipsum</div>"),
        ("   \n  <div>Lorem Ipsum</div>  \t  ", "   \n  <div>Lorem Ipsum</div>  \t  "),
        ("<!-- Comment --><div>Content</div>", "<!-- Comment --><div>Content</div>"),
        (
            "<template><p>Inside Template</p></template>",
            "<template><p>Inside Template</p></template>",
        ),
    ],
)
def test_fragment_parser(html, expected_html):
    parser = LexborHTMLParser(html, is_fragment=True)
    assert parser.html == expected_html


def test_insert_node_fragment_parser():
    html = "<div></div>"
    p = LexborHTMLParser(html, is_fragment=True)
    p.root.insert_child("text")
    assert p.html == "<div>text</div>"


def test_insert_before_fragment_parser():
    html = "<div><span></span></div>"
    p = LexborHTMLParser(html, is_fragment=True)
    span = p.root.css_first("span")
    span.insert_before("text")
    assert p.html == "<div>text<span></span></div>"


def test_insert_after_fragment_parser():
    html = "<div><span></span></div>"
    p = LexborHTMLParser(html, is_fragment=True)
    span = p.root.css_first("span")
    span.insert_after("text")
    assert p.html == "<div><span></span>text</div>"


def test_clone_parser_fragment():
    html = "<div><span>Hello</span><p>World</p></div>"
    p = LexborHTMLParser(html, is_fragment=True)
    cloned = p.clone()
    assert cloned.html == p.html
    assert cloned is not p

    cloned.root.css_first("span").insert_child("!")
    assert cloned.html == "<div><span>Hello!</span><p>World</p></div>"
    assert p.html == "<div><span>Hello</span><p>World</p></div>"


def test_clone_node_fragment():
    html = "<div><span>Hello</span><p>World</p></div>"
    p = LexborHTMLParser(html, is_fragment=True)
    span = p.root.css_first("span")
    cloned_span = span.clone()
    assert cloned_span.html == span.html
    assert cloned_span is not span

    cloned_span.insert_child("!")
    assert cloned_span.html == "<span>Hello!</span>"
    assert span.html == "<span>Hello</span>"


def test_fragment_root_html_serialization():
    html = "<div>Hello</div><span>World</span>"
    p = LexborHTMLParser(html, is_fragment=True)
    assert p.root.html == "<div>Hello</div><span>World</span>"
    p.root.insert_child("!")
    assert p.html == "<div>Hello!</div><span>World</span>"


def test_fragment_root_html_pretty_serialization():
    html = "<div><span>Hello</span></div>\n<span>World</span>"
    p = LexborHTMLParser(html, is_fragment=True)
    assert p.root.html_pretty(skip_ws_nodes=True) == clean_doc(
        """
        <div>
          <span>
            "Hello"
          </span>
        </div>
        <span>
          "World"
        </span>
        """
    )
    assert p.html_pretty(skip_ws_nodes=True) == clean_doc(
        """
        <div>
          <span>
            "Hello"
          </span>
        </div>
        <span>
          "World"
        </span>
        """
    )


def test_fragment_node_properties():
    html = "<div>Hello</div><span>World</span>"
    p = LexborHTMLParser(html, is_fragment=True)
    div = p.root
    span = p.root.next

    assert div.is_element_node is True
    assert div.is_text_node is False
    assert div.is_comment_node is False

    assert span.is_element_node is True
    assert span.is_text_node is False
    assert span.is_comment_node is False

    text_node = div.first_child
    assert text_node.is_element_node is False
    assert text_node.is_text_node is True
    assert text_node.is_comment_node is False


def test_fragment_text_extraction():
    html = "<div>Hello <strong>World</strong>!</div>"
    p = LexborHTMLParser(html, is_fragment=True)
    div = p.root.css_first("div")
    assert div.text() == "Hello World!"
    assert div.text(deep=True, separator=" ", strip=True) == "Hello World !"


def test_fragment_traversal():
    html = "<div><span>Hello</span><p>World</p></div>"
    p = LexborHTMLParser(html, is_fragment=True)
    nodes = list(p.root.traverse(include_text=True))
    assert len(nodes) == 5
    assert nodes[0].tag == "div"
    assert nodes[1].tag == "span"
    assert nodes[2].tag == "-text"
    assert nodes[3].tag == "p"
    assert nodes[4].tag == "-text"


def test_fragment_inner_html():
    html = "<div><span>Hello</span><p>World</p></div>"
    p = LexborHTMLParser(html, is_fragment=True)
    div = p.root.css_first("div")
    assert div.inner_html == "<span>Hello</span><p>World</p>"
    div.inner_html = "<em>New</em> content"
    assert div.html == "<div><em>New</em> content</div>"


def test_fragment_node_operations_combined():
    html = "<div><span>Hello</span></div>"
    p = LexborHTMLParser(html, is_fragment=True)
    span = p.root.css_first("span")
    span.replace_with("Replaced")
    assert p.html == "<div>Replaced</div>"

    html2 = "<div><span></span></div>"
    p2 = LexborHTMLParser(html2, is_fragment=True)
    span2 = p2.root.css_first("span")
    span2.insert_before("Before")
    span2.insert_after("After")
    assert p2.html == "<div>Before<span></span>After</div>"


def test_fragment_replace_with_node():
    html = "<div><span>Hello</span></div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    replacement_html = "<em>Replaced</em>"
    replacement_parser = LexborHTMLParser(replacement_html, is_fragment=True)
    span = parser.root.css_first("span")
    span.replace_with(replacement_parser.root)
    assert parser.html == "<div><em>Replaced</em></div>"


def test_fragment_insert_before_node():
    base_html = "<div><span></span></div>"
    base_parser = LexborHTMLParser(base_html, is_fragment=True)
    before_html = "<strong>Before</strong>"
    before_parser = LexborHTMLParser(before_html, is_fragment=True)
    span = base_parser.root.css_first("span")
    span.insert_before(before_parser.root)
    assert base_parser.html == "<div><strong>Before</strong><span></span></div>"


def test_fragment_insert_after_node():
    base_html = "<div><span></span></div>"
    base_parser = LexborHTMLParser(base_html, is_fragment=True)
    after_html = "<em>After</em>"
    after_parser = LexborHTMLParser(after_html, is_fragment=True)
    span = base_parser.root.css_first("span")
    span.insert_after(after_parser.root)
    assert base_parser.html == "<div><span></span><em>After</em></div>"


def test_fragment_insert_child_node():
    base_html = "<div></div>"
    base_parser = LexborHTMLParser(base_html, is_fragment=True)
    child_html = "<p>Child</p>"
    child_parser = LexborHTMLParser(child_html, is_fragment=True)
    div = base_parser.root.css_first("div")
    div.insert_child(child_parser.root)
    assert base_parser.html == "<div><p>Child</p></div>"


def test_fragment_strip_tags():
    html = "<div><script>alert('test')</script><p>Hello</p><style>body { color: red; }</style></div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    parser.root.strip_tags(["script", "style"])
    assert parser.html == "<div><p>Hello</p></div>"


def test_fragment_decompose():
    html = "<div><script>alert('test')</script><p>Hello</p></div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    script = parser.root.css_first("script")
    script.decompose()
    assert parser.html == "<div><p>Hello</p></div>"


@pytest.mark.parametrize(
    "input_html, expected",
    [
        ("<html><body><div>test</div></body></html>", "<div>test</div>"),
        ("<head><title>test</title></head>", "<title>test</title>"),
        ("<body><p>test</p></body>", "<p>test</p>"),
    ],
)
def test_fragment_strips_top_level_tags(input_html, expected):
    parser = LexborHTMLParser(input_html, is_fragment=True)
    assert parser.html == expected


def test_fragment_navigation():
    html = "<div>First</div><span>Second</span><p>Third</p>"
    parser = LexborHTMLParser(html, is_fragment=True)
    div = parser.root
    span = div.next
    p = span.next
    assert div.tag == "div"
    assert span.tag == "span"
    assert p.tag == "p"
    assert div.prev is None
    assert span.prev.tag == "div"
    assert p.prev.tag == "span"
    assert p.next is None
    assert div.first_child.is_text_node
    assert div.last_child.is_text_node
    assert div.first_child.text_content == "First"


def test_fragment_attrs():
    html = "<div id='test' class='foo bar' data-value='123'></div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    div = parser.root
    assert div.attributes == {"id": "test", "class": "foo bar", "data-value": "123"}
    assert div.attrs["id"] == "test"
    div.attrs["new"] = "value"
    assert div.attributes == {
        "id": "test",
        "class": "foo bar",
        "data-value": "123",
        "new": "value",
    }


def test_fragment_child_alias():
    html = "<div><span>content</span></div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    div = parser.root
    assert div.child == div.first_child


def test_fragment_tag_properties():
    html = "<div id='test'>content</div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    div = parser.root
    assert div.tag == "div"
    assert div.tag_id is not None
    assert div.mem_id is not None
    assert div.id == "test"


def test_fragment_parser_accepts_explicit_fragment_context_defaults():
    parser = LexborHTMLParser(
        "<div id='test'>content</div>",
        is_fragment=True,
        fragment_tag="div",
        fragment_namespace="html",
    )
    assert parser.html == '<div id="test">content</div>'


def test_fragment_parser_accepts_namespace_uri():
    parser = LexborHTMLParser(
        "<title>SVG</title>",
        is_fragment=True,
        fragment_tag="svg",
        fragment_namespace="http://www.w3.org/2000/svg",
    )
    assert parser.root.tag == "title"
    assert parser.html == "<title>SVG</title>"


def test_fragment_parser_rejects_unknown_fragment_tag():
    with pytest.raises(ValueError, match="Unknown fragment tag"):
        LexborHTMLParser("<div></div>", is_fragment=True, fragment_tag="not-a-real-tag")


def test_fragment_parser_rejects_unknown_fragment_namespace():
    with pytest.raises(ValueError, match="Unknown fragment namespace"):
        LexborHTMLParser(
            "<div></div>", is_fragment=True, fragment_namespace="not-a-real-namespace"
        )


def test_fragment_unwrap():
    html = "<div><span>Hello</span> world</div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    span = parser.root.css_first("span")
    span.unwrap()
    assert parser.html == "<div>Hello world</div>"


def test_fragment_unwrap_tags():
    html = "<div><i>Hello</i> <b>world</b></div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    parser.root.unwrap_tags(["i", "b"])
    assert parser.html == "<div>Hello world</div>"


def test_fragment_eq():
    html = "<div>test</div>"
    parser1 = LexborHTMLParser(html, is_fragment=True)
    parser2 = LexborHTMLParser(html, is_fragment=True)
    assert parser1.root == parser2.root.html
    assert parser1.root == "<div>test</div>"


def test_fragment_text_content():
    html = "<div>Hello</div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    text_node = parser.root.first_child
    assert text_node.text_content == "Hello"
    assert parser.root.text_content is None


def test_fragment_comment_content():
    html = "<!-- comment -->"
    parser = LexborHTMLParser(html, is_fragment=True)
    comment_node = parser.root
    assert comment_node.comment_content == "comment"


def test_fragment_parser_malformed_html():
    html = "<div><unclosed><span>content"
    parser = LexborHTMLParser(html, is_fragment=True)
    html_result = parser.html
    assert html_result is not None
    assert "content" in html_result


def test_attributes_access_on_non_element():
    html = "<!-- comment --><div>text</div>"
    parser = LexborHTMLParser(html, is_fragment=True)
    root = parser.root
    assert root is not None

    comment_node = root
    assert comment_node.is_comment_node

    attrs = comment_node.attributes
    assert isinstance(attrs, dict)
    assert len(attrs) == 0

    text_node = root.css_first("div").first_child
    assert text_node is not None
    assert text_node.is_text_node

    text_attrs = text_node.attributes
    assert isinstance(text_attrs, dict)
    assert len(text_attrs) == 0


@pytest.mark.parametrize(
    "malformed_html",
    [
        "<div><unclosed><span>content",  # Unclosed tags
        "<div><span></div>",  # Mismatched tags
        "<div><span>content</span",  # Missing closing bracket
        '<div class="unclosed>content</div>',  # Unclosed attribute
        "<div>&invalid_entity;</div>",  # Invalid entity
        "<!-- unclosed comment",  # Unclosed comment
        "<![CDATA[ unclosed cdata",  # Unclosed CDATA
    ],
)
def test_fragment_parsing_malformed_html(malformed_html):
    parser = LexborHTMLParser(malformed_html, is_fragment=True)
    html_result = parser.html
    assert html_result is None or isinstance(html_result, str)


def test_fragment_only_text():
    text_only = "Just plain text"
    parser = LexborHTMLParser(text_only, is_fragment=True)
    html_result = parser.html
    assert html_result is not None
    assert "Just plain text" in html_result


def test_fragment_only_comment():
    comment_only = "<!-- Just a comment -->"
    parser = LexborHTMLParser(comment_only, is_fragment=True)
    html_result = parser.html
    assert html_result is not None
    assert "Just a comment" in html_result


def test_fragment_mixed_content():
    mixed = "Text <!-- comment --> <div>element</div> more text"
    parser = LexborHTMLParser(mixed, is_fragment=True)
    html_result = parser.html
    assert html_result is not None
    assert "Text" in html_result
    assert "element" in html_result


def test_fragment_create_node_basic():
    parser = LexborHTMLParser("<div></div>", is_fragment=True)
    assert parser.root is not None
    new_node = parser.create_node("span")
    assert new_node.tag == "span"
    assert new_node.parent is None

    parser.root.insert_child(new_node)
    expected_html = "<div><span></span></div>"
    assert parser.html == expected_html


def test_fragment_create_node_different_tags():
    parser = LexborHTMLParser("<div></div>", is_fragment=True)
    root = parser.root
    assert root is not None

    tags_to_test = ["p", "span", "div", "h1", "custom-tag"]
    for tag in tags_to_test:
        new_node = parser.create_node(tag)
        assert new_node.tag == tag
        root.insert_child(new_node)

    html = parser.html
    assert html is not None
    for tag in tags_to_test:
        assert f"<{tag}></{tag}>" in html


def test_fragment_create_node_with_attributes():
    parser = LexborHTMLParser("<div></div>", is_fragment=True)
    assert parser.root is not None
    new_node = parser.create_node("a")
    new_node.attrs["href"] = "https://example.com"
    new_node.attrs["class"] = "link"

    parser.root.insert_child(new_node)
    html = parser.html
    assert html is not None
    assert 'href="https://example.com"' in html
    assert 'class="link"' in html


def test_fragment_text_extraction_multiple_nodes():
    html = "<p>1</p><p>2</p>"
    p = LexborHTMLParser(html, is_fragment=True)
    assert p.text(deep=False) == ""
    assert p.text(deep=True, separator=" ", strip=True) == "1 2"


def test_fragment_iter_multiple_nodes():
    html = "<p>1</p><p>2</p>"
    p = LexborHTMLParser(html, is_fragment=True)
    assert len(list(p.root.iter())) == 2


def test_fragment_empty_html():
    html = ""
    tree = LexborHTMLParser(html, is_fragment=True)
    assert tree.html == ""

```

### `tests/test_lexbor.py`

```py
"""Tests for functionality that is only supported by lexbor backend."""

from inspect import cleandoc

import pytest


from selectolax.lexbor import LexborHTMLParser, SelectolaxError, parse_fragment


def clean_doc(text: str) -> str:
    return f"{cleandoc(text)}\n"


def test_reads_inner_html():
    html = """<div id="main"><div>Hi</div><div id="updated">2025-09-27</div></div>"""
    parser = LexborHTMLParser(html)
    actual = parser.css_first("#main").inner_html
    expected = """<div>Hi</div><div id="updated">2025-09-27</div>"""
    assert actual == expected


def test_sets_inner_html():
    html = """<div id="main"><div>Hi</div><div id="updated">2025-09-27</div></div>"""
    parser = LexborHTMLParser(html)
    expected = "<span>Test</span>"
    parser.css_first("#main").inner_html = "<span>Test</span>"
    actual = parser.css_first("#main").inner_html
    assert actual == expected


def test_html_pretty_document():
    parser = LexborHTMLParser("<div><span>Hello</span><!-- note --></div>")
    assert parser.html_pretty() == clean_doc(
        """
        <html>
          <head>
          </head>
          <body>
            <div>
              <span>
                "Hello"
              </span>
              <!--  note  -->
            </div>
          </body>
        </html>
        """
    )


def test_html_pretty_node_with_options():
    parser = LexborHTMLParser("<div><span>Hello</span><!-- note --></div>")
    node = parser.css_first("div")
    assert node.html_pretty(skip_comment=True) == clean_doc(
        """
        <div>
          <span>
            "Hello"
          </span>
        </div>
        """
    )


def test_html_pretty_skip_ws_nodes_option():
    parser = LexborHTMLParser("<div>\n</div><span></span>", is_fragment=True)
    assert parser.html_pretty(skip_ws_nodes=True) == clean_doc(
        """
        <div>
        </div>
        <span>
        </span>
        """
    )


def test_inner_html_pretty_node_with_options():
    parser = LexborHTMLParser("<div><span>Hello</span><!-- note --></div>")
    node = parser.css_first("div")
    assert node.inner_html_pretty(skip_comment=True) == clean_doc(
        """
        <span>
          "Hello"
        </span>
        """
    )


def test_inner_html_pretty_parser():
    parser = LexborHTMLParser("<div><span>Hello</span></div>", is_fragment=True)
    assert parser.inner_html_pretty(skip_ws_nodes=True) == clean_doc(
        """
        <span>
          "Hello"
        </span>
        """
    )


def test_html_pretty_rejects_negative_indent():
    parser = LexborHTMLParser("<div>Hello</div>")
    with pytest.raises(ValueError):
        parser.html_pretty(indent=-1)


def test_inner_html_pretty_rejects_negative_indent():
    parser = LexborHTMLParser("<div>Hello</div>")
    with pytest.raises(ValueError):
        parser.inner_html_pretty(indent=-1)


def test_checking_attributes_does_not_segfault():
    parser = LexborHTMLParser("")
    root_node = parser.root
    assert root_node is not None
    for node in root_node.traverse():
        parent = node.parent
        assert parent is not None
        parent = parent.attributes.get("anything")


def test_node_cloning():
    parser = LexborHTMLParser("<div id='main'>123</div>")
    new_node = parser.css_first("#main").clone()
    new_node.inner_html = "<div>new</div>"
    assert parser.css_first("#main").html != new_node.html
    assert new_node.html == '<div id="main"><div>new</div></div>'


def test_double_unwrap_does_not_segfault():
    html = """<div><div><div></div></div></div>"""
    outer_div = parse_fragment(html)[0]
    some_set = set()

    inner_div = outer_div.child
    assert inner_div is not None
    inner_div.unwrap()
    inner_div.unwrap()
    some_set.add(outer_div.parent)
    some_set.add(outer_div.parent)


def test_unicode_selector_works():
    html = '<span data-original-title="Pneu renforcé"></span>'
    tree = LexborHTMLParser(html)
    node = tree.css_first('span[data-original-title="Pneu renforcé"]')
    assert node.tag == "span"


def test_node_type_helpers():
    html = "<div id='main'>text<!--comment--></div>"
    parser = LexborHTMLParser(html)

    div_node = parser.css_first("#main")
    assert div_node.is_element_node
    assert not div_node.is_text_node

    text_node = div_node.first_child
    assert text_node is not None
    assert text_node.is_text_node
    assert not text_node.is_element_node

    comment_node = div_node.last_child
    assert comment_node is not None
    assert comment_node.is_comment_node
    assert not comment_node.is_text_node

    document_node = parser.root.parent
    assert document_node is not None
    assert document_node.is_document_node
    assert not document_node.is_element_node


def test_text_honors_skip_empty_flag():
    parser = LexborHTMLParser("<div><span>value</span><title>\n   \n</title></div>")
    span = parser.css_first("span")
    assert span is not None
    assert span.text(deep=False, skip_empty=False) == "value"
    assert span.text(deep=False, skip_empty=True) == "value"
    title = parser.css_first("title")
    assert title is not None
    assert title.text(deep=False, skip_empty=False) == "\n   \n"
    assert title.text(deep=False, skip_empty=True) == ""


def test_attrs_reject_non_element_nodes():
    parser = LexborHTMLParser("<div>hello<!--comment--></div>")
    div = parser.css_first("div")
    text_node = div.first_child
    comment_node = div.last_child

    assert text_node is not None
    assert comment_node is not None
    assert text_node.is_text_node
    assert comment_node.is_comment_node

    with pytest.raises(TypeError, match="element nodes"):
        _ = text_node.attrs

    with pytest.raises(TypeError, match="element nodes"):
        _ = comment_node.attrs


def test_text_does_not_duplicate_fragment_root_text_node():
    parser = LexborHTMLParser("hello", is_fragment=True)
    root = parser.root
    assert root is not None
    assert root.is_text_node
    assert root.text(deep=True) == "hello"


def test_iter_includes_text_nodes_when_requested():
    parser = LexborHTMLParser("<div><span>value</span><title>\n   \n</title></div>")
    div = parser.css_first("div")
    children = [node for node in div.iter(include_text=True, skip_empty=True)]
    assert (
        ", ".join(
            node.tag for node in children[0].iter(include_text=True, skip_empty=True)
        )
        == "-text"
    )
    assert (
        ", ".join(
            node.tag for node in children[1].iter(include_text=True, skip_empty=True)
        )
        == ""
    )


def test_traverse_respects_skip_empty_on_text_nodes():
    parser = LexborHTMLParser("<div><span>value</span><title>\n   \n</title></div>")
    div = parser.css_first("div")
    children = [node.tag for node in div.traverse(include_text=True, skip_empty=True)]
    assert ", ".join(children) == "div, span, -text, title"


def test_traverse_with_skip_empty_on_a_full_html_document():
    html = clean_doc(
        """
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width,initial-scale=1">
            <title>Title!</title>
            <!-- My crazy comment -->
          </head>
          <body>
            <p>Hello <strong>World</strong>!</p>
            <div hidden draggable="true" translate="no" contenteditable="true" tabindex="3">
              Div
            </div>
          </body>
        </html>
        """
    )
    parser = LexborHTMLParser(html)
    children = [
        (node.tag, node.text_content)
        for node in parser.root.traverse(include_text=True, skip_empty=False)
    ]
    assert children == [
        ("html", None),
        ("head", None),
        ("-text", "\n    "),
        ("meta", None),
        ("-text", "\n    "),
        ("meta", None),
        ("-text", "\n    "),
        ("title", None),
        ("-text", "Title!"),
        ("-text", "\n    "),
        ("-comment", None),
        ("-text", "\n  "),
        ("-text", "\n  "),
        ("body", None),
        ("-text", "\n    "),
        ("p", None),
        ("-text", "Hello "),
        ("strong", None),
        ("-text", "World"),
        ("-text", "!"),
        ("-text", "\n    "),
        ("div", None),
        ("-text", "\n      Div\n    "),
        ("-text", "\n  \n\n"),
    ]
    children = [
        (node.tag, node.text_content)
        for node in parser.root.traverse(include_text=True, skip_empty=True)
    ]
    assert children == [
        ("html", None),
        ("head", None),
        ("meta", None),
        ("meta", None),
        ("title", None),
        ("-text", "Title!"),
        ("-comment", None),
        ("body", None),
        ("p", None),
        ("-text", "Hello "),
        ("strong", None),
        ("-text", "World"),
        ("-text", "!"),
        ("div", None),
        ("-text", "\n      Div\n    "),
    ]


def test_is_empty_text_node_property():
    parser = LexborHTMLParser("<div><span>\n \n</span><title>X</title></div>")
    text_node = parser.css_first("span").first_child
    assert text_node.text_content == "\n \n"
    assert text_node.is_empty_text_node
    text_node = parser.css_first("title").first_child
    assert text_node.text_content == "X"
    assert not text_node.is_empty_text_node


def test_comment_content_property() -> None:
    parser = LexborHTMLParser("<div><span><!-- hello --></span><title>X</title></div>")
    text_node = parser.css_first("span").first_child
    assert text_node is not None
    assert text_node.is_comment_node
    assert text_node.comment_content == "hello"


def test_selector_text_contains():
    html = """
    <div>
        <p>Hello world</p>
        <p>Goodbye world</p>
        <span>No match here</span>
    </div>
    """
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    selector = root.select("p").text_contains("Hello")
    assert len(selector.matches) == 1
    assert selector.matches[0].text() == "Hello world"
    assert selector.any_matches is True


def test_selector_any_text_contains():
    html = """
    <div>
        <p>Hello world</p>
        <p>Goodbye world</p>
        <span>No match here</span>
    </div>
    """
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    assert root.select("p").any_text_contains("Hello") is True
    assert root.select("p").any_text_contains("world") is True
    assert root.select("p").any_text_contains("nomatch") is False


def test_selector_attribute_longer_than():
    html = """
    <div>
        <a href="short">Link 1</a>
        <a href="http://very-long-url.com/path">Link 2</a>
        <a href="medium">Link 3</a>
    </div>
    """
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    selector = root.select("a").attribute_longer_than("href", 10)
    assert len(selector.matches) == 1
    href = selector.matches[0].attributes["href"]
    assert href is not None
    assert "very-long-url" in href


def test_selector_any_attribute_longer_than():
    html = """
    <div>
        <a href="short">Link 1</a>
        <a href="http://very-long-url.com/path">Link 2</a>
        <a href="medium">Link 3</a>
    </div>
    """
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    assert root.select("a").any_attribute_longer_than("href", 10) is True
    assert root.select("a").any_attribute_longer_than("href", 50) is False


def test_selector_attribute_longer_than_with_start():
    html = """
    <div>
        <a href="http://short.com">Link 1</a>
        <a href="http://very-long-domain-name.com/path">Link 2</a>
        <a href="http://medium.com">Link 3</a>
    </div>
    """
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    selector = root.select("a").attribute_longer_than("href", 15, "http://")
    assert len(selector.matches) == 1
    href = selector.matches[0].attributes["href"]
    assert href is not None
    assert "very-long-domain-name" in href


def test_selector_chaining():
    html = """
    <div>
        <p class="important">Hello world</p>
        <p class="normal">Goodbye world</p>
        <p class="important">Important stuff</p>
        <span class="important">Not a paragraph</span>
    </div>
    """
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    selector = root.select("p").text_contains("world").attribute_longer_than("class", 6)
    assert len(selector.matches) == 1
    assert selector.matches[0].text() == "Hello world"
    assert selector.matches[0].attributes["class"] == "important"


def test_selector_empty_matches():
    html = "<div><p>Hello</p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    selector = root.select("div").text_contains("nomatch")
    assert len(selector.matches) == 0
    assert selector.any_matches is False
    assert bool(selector) is False


def test_attributes_sget():
    html = '<div id="test" class="foo" empty></div>'
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    div = root.css_first("div")
    assert div is not None
    attrs = div.attrs
    assert attrs.sget("id") == "test"
    assert attrs.sget("class") == "foo"
    assert attrs.sget("empty") == ""  # Empty attributes return empty string
    assert attrs.sget("missing", "default") == "default"


def test_attributes_keys_values_items():
    html = '<div id="test" class="foo" data-value="123"></div>'
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    div = root.css_first("div")
    assert div is not None
    attrs = div.attrs

    keys = list(attrs.keys())
    assert "id" in keys
    assert "class" in keys
    assert "data-value" in keys

    values = list(attrs.values())
    assert "test" in values
    assert "foo" in values
    assert "123" in values

    items = dict(attrs.items())
    assert items["id"] == "test"
    assert items["class"] == "foo"
    assert items["data-value"] == "123"


def test_attributes_len_and_contains():
    html = '<div id="test" class="foo"></div>'
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    div = root.css_first("div")
    assert div is not None
    attrs = div.attrs

    assert len(attrs) == 2
    assert "id" in attrs
    assert "class" in attrs
    assert "missing" not in attrs


def test_attributes_get():
    html = '<div id="test" empty></div>'
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    div = root.css_first("div")
    assert div is not None
    attrs = div.attrs

    assert attrs.get("id") == "test"
    assert attrs.get("empty") is None  # Empty attributes return None
    assert attrs.get("missing") is None
    assert attrs.get("missing", "default") == "default"


def test_attributes_modification():
    html = '<div id="original"></div>'
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    div = root.css_first("div")
    assert div is not None
    attrs = div.attrs

    # new attribute
    attrs["new_attr"] = "new_value"
    assert attrs["new_attr"] == "new_value"

    # existing attribute
    attrs["id"] = "modified"
    assert attrs["id"] == "modified"

    # empty attribute
    attrs["empty"] = None
    assert attrs["empty"] is None

    # deleting attribute
    del attrs["id"]
    assert "id" not in attrs

    try:
        del attrs["nonexistent"]
        assert False, "Should have raised KeyError"
    except KeyError:
        pass


def test_node_insert_operations_with_different_types():
    html = '<div><span id="target">target</span></div>'
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    target = root.css_first("#target")
    assert target is not None

    # Test insert_before with string
    target.insert_before("before_text")
    assert "before_text<span" in root.html

    # Test insert_after with bytes
    target.insert_after(b"after_bytes")
    assert "after_bytes</div>" in root.html


def test_node_replace_with_different_types():
    html = '<div><span id="target">old</span></div>'
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    target = root.css_first("#target")
    assert target is not None

    # Test replace_with string
    target.replace_with("replaced")
    assert root.html == "<html><head></head><body><div>replaced</div></body></html>"

    # Test replace_with bytes
    html = '<div><span id="target">old</span></div>'
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    target = root.css_first("#target")
    assert target is not None

    target.replace_with(b"bytes_replaced")
    assert "bytes_replaced" in root.html


def test_node_insert_with_lexbor_node():
    html1 = "<div>content1</div>"
    html2 = "<span>content2</span>"
    parser1 = LexborHTMLParser(html1)
    parser2 = LexborHTMLParser(html2)

    root1 = parser1.root
    root2 = parser2.root
    assert root1 is not None and root2 is not None

    div1 = root1.css_first("div")
    span2 = root2.css_first("span")
    assert div1 is not None and span2 is not None

    # Insert node from another parser
    div1.insert_child(span2)
    assert "<span>content2</span>" in root1.html


def test_node_manipulation_with_fragments():
    html = "<div>First</div><span>Second</span>"
    parser = LexborHTMLParser(html, is_fragment=True)
    root = parser.root
    assert root is not None

    span = root.next
    assert span is not None

    span.insert_before("Before")
    assert parser.html == "<div>First</div>Before<span>Second</span>"

    span.insert_after("After")
    assert parser.html == "<div>First</div>Before<span>Second</span>After"

    span.insert_child("Child")
    assert parser.html == "<div>First</div>Before<span>SecondChild</span>After"


def test_merge_text_nodes_edge_cases():
    html = "<div><p><strong>J</strong>ohn<strong>D</strong>oe</p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    div = root.css_first("div")
    assert div is not None

    # Before unwrapping - text nodes are separated by strong tags
    text_before = div.text(deep=True, separator="")
    assert "JohnDoe" in text_before

    # Unwrap strong tags - this creates adjacent text nodes
    div.unwrap_tags(["strong"])

    # After unwrapping but before merging - text nodes are adjacent
    text_after_unwrap = div.text(deep=True, separator="")
    assert "JohnDoe" in text_after_unwrap

    # After merging - should be the same since they were already adjacent
    div.merge_text_nodes()
    text_after_merge = div.text(deep=True, separator="")
    assert "JohnDoe" in text_after_merge


def test_unwrap_tags_with_nested_elements():
    html = "<div><p><span><em>Text</em></span></p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    div = root.css_first("div")
    assert div is not None

    div.unwrap_tags(["span", "em"])
    html = root.html
    assert html is not None
    assert "<span>" not in html and "<em>" not in html
    assert "Text" in html


def test_unwrap_tags_delete_empty():
    html = "<div><p><span></span><em>Keep</em><i></i></p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    p = root.css_first("p")
    assert p is not None

    p.unwrap_tags(["span", "i"], delete_empty=True)
    html = root.html
    assert html is not None
    assert "<span>" not in html and "<i>" not in html
    assert "<em>Keep</em>" in html


def test_parser_clone_method():
    html = "<div id='original'><p>Original content</p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None

    # Clone the parser
    cloned_parser = parser.clone()
    assert cloned_parser is not parser
    assert cloned_parser.html == parser.html

    # Modify the clone
    cloned_root = cloned_parser.root
    assert cloned_root is not None
    cloned_div = cloned_root.css_first("div")
    assert cloned_div is not None
    cloned_div.attrs["id"] = "modified"

    # Original should be unchanged
    original_div = root.css_first("div")
    assert original_div is not None
    assert original_div.attrs["id"] == "original"

    # Clone should be modified
    assert cloned_div.attrs["id"] == "modified"


def test_parser_select_method_returns_lexbor_selector():
    html = "<div><p>First</p><p>Second</p><p>Third</p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None

    selector = root.select("p")
    assert hasattr(selector, "matches")
    assert hasattr(selector, "any_matches")
    assert hasattr(selector, "text_contains")
    assert len(selector.matches) == 3

    filtered = selector.text_contains("Second")
    assert len(filtered.matches) == 1
    assert filtered.matches[0].text() == "Second"


def test_parser_select_with_no_matches():
    html = "<div><p>Content</p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None

    selector = root.select("span")
    assert len(selector.matches) == 0
    assert selector.any_matches is False
    assert bool(selector) is False


def test_parser_select_with_query():
    html = "<div><p class='important'>Important</p><p>Normal</p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None

    selector = root.select("p.important")
    assert len(selector.matches) == 1
    assert selector.matches[0].text() == "Important"


def test_css_selector_invalid_syntax():
    html = "<div><p>Test</p></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None

    try:
        root.css("[invalid")
    except Exception:
        pass


def test_selector_attribute_longer_than_edge_cases():
    html = "<div><a href='short'>Link1</a><a>Link2</a><a href=''>Link3</a></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None

    selector = root.select("a")
    result = selector.attribute_longer_than("href", 0)
    assert len(result.matches) == 1


def test_node_replace_with_empty():
    html = "<div><span>target</span></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    span = root.css_first("span")
    assert span is not None

    span.replace_with("")
    html_result = root.html
    assert html_result is not None
    assert "<span>" not in html_result
    assert parser.html == "<html><head></head><body><div></div></body></html>"


def test_double_unwrap_prevention():
    html = "<div><span>test</span></div>"
    parser = LexborHTMLParser(html)
    root = parser.root
    assert root is not None
    span = root.css_first("span")
    assert span is not None

    # First unwrap should work
    span.unwrap()

    # Second unwrap should not cause issues (already removed)
    span.unwrap()

    html_result = root.html
    assert html_result is not None
    assert "test" in html_result


def test_clone_complex_modifications():
    html = "<div><p>Original</p><span>Content</span></div>"
    parser = LexborHTMLParser(html)

    p_tag = parser.root.css_first("p")
    assert p_tag is not None
    p_tag.inner_html = "Modified"

    cloned = parser.clone()

    cloned_p = cloned.root.css_first("p")
    assert cloned_p is not None
    cloned_p.decompose()

    original_text = parser.root.text()
    assert "Modified" in original_text

    cloned_text = cloned.root.text()
    assert "Modified" not in cloned_text


def test_create_node_basic():
    parser = LexborHTMLParser("<div></div>")
    new_node = parser.create_node("span")
    assert new_node.tag == "span"
    assert new_node.parent is None

    parser.css_first("div").insert_child(new_node)
    expected_html = "<html><head></head><body><div><span></span></div></body></html>"
    assert parser.html == expected_html


def test_create_node_different_tags():
    parser = LexborHTMLParser("<div></div>")
    root = parser.root
    assert root is not None

    tags_to_test = ["p", "span", "div", "h1", "custom-tag"]
    for tag in tags_to_test:
        new_node = parser.create_node(tag)
        assert new_node.tag == tag
        root.insert_child(new_node)

    html = parser.html
    assert html is not None
    for tag in tags_to_test:
        assert f"<{tag}></{tag}>" in html


def test_create_node_with_attributes():
    parser = LexborHTMLParser("<div></div>")
    new_node = parser.create_node("a")
    new_node.attrs["href"] = "https://example.com"
    new_node.attrs["class"] = "link"

    parser.root.insert_child(new_node)
    html = parser.html
    assert html is not None
    assert 'href="https://example.com"' in html
    assert 'class="link"' in html


def test_create_node_empty_tag_name():
    parser = LexborHTMLParser("<div></div>")
    try:
        parser.create_node("")
        assert False, "Should have raised an exception"
    except SelectolaxError:
        pass


def test_unwrap_tags_segfault_prevention():
    # This scenario used to cause a segmentation fault because the 'span' tag
    # matches the node itself, causing it to be detached. The subsequent
    # search for 'p' would then happen on a detached node.
    html = "<div><span id='repro'><span><p>Text</p></span></span></div>"
    tree = LexborHTMLParser(html)
    node = tree.css_first("#repro")
    assert node is not None

    # Should not segfault
    node.unwrap_tags(["span", "p"])

    assert "Text" in tree.html
    assert '<span id="repro">' not in tree.html


def test_strip_tags_then_text_basic():
    html = "<html><head></head><body><script>evil();</script><p>Hello</p></body></html>"
    parser = LexborHTMLParser(html)
    parser.strip_tags(["script"])
    result = parser.root.text(separator=" ", strip=True)
    assert "Hello" in result
    assert "evil" not in result


def test_strip_tags_then_text_multiple_tags():
    html = (
        "<html><head><style>body{}</style></head><body>"
        "<script>x=1;</script>"
        "<template><div>hidden</div></template>"
        "<p>Visible</p>"
        "</body></html>"
    )
    parser = LexborHTMLParser(html)
    parser.strip_tags(["style", "script", "template"])
    result = parser.root.text(separator=" ", strip=True)
    assert "Visible" in result
    assert "hidden" not in result
    assert "body{}" not in result


def test_strip_tags_then_text_nested_targets():
    html = (
        "<html><body>"
        "<template><script>inner();</script><p>tmpl</p></template>"
        "<script>outer();</script>"
        "<p>Keep this</p>"
        "</body></html>"
    )
    parser = LexborHTMLParser(html)
    parser.strip_tags(["template", "script"])
    result = parser.root.text(separator=" ", strip=True)
    assert "Keep this" in result
    assert "inner" not in result
    assert "outer" not in result


def test_strip_tags_then_text_recursive_flag():
    html = (
        "<html><body>"
        "<div class='rm'><span>child1</span><em>child2</em></div>"
        "<p>Survivor</p>"
        "</body></html>"
    )
    parser = LexborHTMLParser(html)
    parser.strip_tags(["div"], recursive=True)
    result = parser.root.text(separator=" ", strip=True)
    assert "Survivor" in result
    assert "child1" not in result


def test_strip_tags_then_text_many_iterations():
    template = (
        "<html><head><style>.a{{}}</style></head><body>"
        "<script>var x={i};</script>"
        "<p>Content {i}</p>"
        "</body></html>"
    )
    for i in range(50):
        parser = LexborHTMLParser(template.format(i=i))
        parser.strip_tags(["style", "script"])
        text = parser.root.text(separator=" ", strip=True)
        assert f"Content {i}" in text

```

### `tests/test_nodes.py`

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selectolax.parser import HTMLParser
from selectolax.lexbor import LexborHTMLParser, SelectolaxError

"""
We'are testing only our own code.
Many functionality are already tested in the Modest engine, so there is no reason to test every case.
"""

_PARSERS_PARAMETRIZER = (
    "parser",
    (HTMLParser, LexborHTMLParser),
)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_selector(parser):
    html = "<span></span><div><p id='p3'>text</p></div><p></p>"
    selector = "p#p3"

    for node in parser(html).css(selector):
        assert node.text() == "text"
        assert node.tag == "p"
        assert node.parent.tag == "div"
        assert node.parent.next.tag == "p"
        assert node.parent.prev.tag == "span"
        assert node.parent.last_child.attributes["id"] == "p3"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_css_multiple_matches(parser):
    html = "<div></div><div></div><div></div>"
    assert len(parser(html).css("div")) == 3


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_css_matches(parser):
    html = "<div></div><div></div><div></div>"
    assert parser(html).css_matches("div")


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_any_css_matches(parser):
    html = "<div></div><span></span><div></div>"
    assert parser(html).any_css_matches(("h1", "span"))


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_css_one(parser):
    html = "<span></span><div><p class='p3'>text</p><p class='p3'>sd</p></div><p></p>"

    selector = ".s3"
    assert parser(html).css_first(selector) is None

    selector = "p.p3"
    assert parser(html).css_first(selector).text() == "text"

    with pytest.raises(ValueError):
        parser(html).css_first(selector, strict=True)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_text_when_html_is_empty(parser):
    html_parser = parser("")

    assert html_parser.text() == ""


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_css_first_default(parser):
    html = "<span></span><div><p class='p3'>text</p><p class='p3'>sd</p></div><p></p>"
    selector = ".s3"
    assert parser(html).css_first(selector, default="lorem ipsum") == "lorem ipsum"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_id_property(parser):
    html = "<p id='main_text'>text</p>"
    assert parser(html).css_first("p").id == "main_text"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_tag_property(parser):
    html = "<h1>text</h1>"
    assert parser(html).css_first("h1").tag == "h1"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_attributes(parser):
    html = "<div><p id='p3'>text</p></div>"
    selector = "p#p3"
    for node in parser(html).css(selector):
        assert "id" in node.attributes
        assert node.attributes["id"] == "p3"

    html = "<div><p attr>text</p></div>"
    selector = "p#p3"
    for node in HTMLParser(html).css(selector):
        assert "attr" in node.attributes
        assert node.attributes["attr"] is None


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_decompose(parser):
    html = "<body><div><p id='p3'>text</p></div></body>"
    html_parser = parser(html)

    for node in html_parser.tags("p"):
        node.decompose()
    assert html_parser.body.child.html == "<div></div>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_html_property(parser):
    html = "<body>Hi there</body>"
    html_parser = parser(html)
    assert html_parser.body.child.html == "Hi there"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_root_property(parser):
    html = "<body>Hi there</body>"
    html_parser = parser(html)
    assert html_parser.root.html == "<html><head></head><body>Hi there</body></html>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_head_property(parser):
    html = """
    <html lang="en">
        <head><title>rushter.com</title></head>
        <body></body>
    </html>
    """
    html_parser = parser(html)
    assert html_parser.head.html == "<head><title>rushter.com</title></head>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_body_property(parser):
    html = "<body>Hi there</body>"
    html_parser = parser(html)
    assert html_parser.body.html == "<body>Hi there</body>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_strip_tags(parser):
    html = "<body><div></div><script></script></body>"
    html_parser = parser(html)
    html_parser.root.strip_tags(["div", "script"])
    assert html_parser.html == "<html><head></head><body></body></html>"

    with pytest.raises(TypeError):
        html_parser.strip_tags(1)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_malformed_attributes(parser):
    html = '<div> <meta name="description" content="ÐÐ°Ñ"Ð " /></div>'
    html_parser = parser(html)

    for tag in html_parser.tags("meta"):
        assert tag


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_iter_with_text(parser):
    html = """
    <div id="description">
        <h1>Title</h1>
        text
        <div>foo</div>
        <img scr="image.jpg">
    </div>
    """
    html_parser = parser(html)
    expected_tags = ["-text", "h1", "-text", "div", "-text", "img", "-text"]
    actual_tags = [
        node.tag
        for node in html_parser.css_first("#description").iter(include_text=True)
    ]
    assert expected_tags == actual_tags


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_text_deep_gh61(parser):
    html = """<div>this is a test <h1>Heading</h1></div>"""
    output = []
    tree = parser(html)
    for node in tree.root.traverse(include_text=True):
        if node.tag == "-text":
            text = node.text(deep=True)
            if text:
                output.append(text)
    assert output == ["this is a test ", "Heading"]


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_iter_no_text(parser):
    html = """
    <div id="description">
        <h1>Title</h1>
        text
        <div>foo</div>
        <img scr="image.jpg">
    </div>
    """
    html_parser = parser(html)
    expected_tags = ["h1", "div", "img"]
    actual_tags = [
        node.tag
        for node in html_parser.css_first("#description").iter(include_text=False)
    ]
    assert expected_tags == actual_tags


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_node_navigation(parser):
    html = (
        '<div id="parent"><div id="prev"></div><div id="test_node"><h1 id="child">Title</h1>'
        '<div>foo</div><img scr="image.jpg"></div><div id="next"></div></div>'
    )
    html_parser = parser(html)
    main_node = html_parser.css_first("#test_node")
    assert main_node.prev.id == "prev"
    assert main_node.next.id == "next"
    assert main_node.parent.id == "parent"
    assert main_node.child.id == "child"


@pytest.mark.parametrize(
    "html,expected, parser",
    [
        ("<div id='my_node'></div>", "my_node", HTMLParser),
        ("<div></div>", None, HTMLParser),
        ("<div id='my_node'></div>", "my_node", LexborHTMLParser),
        ("<div></div>", None, LexborHTMLParser),
    ],
)
def test_get_node_id(html, expected, parser):
    html_parser = parser(html)
    node = html_parser.css_first("div")
    assert node.id == expected


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_html_attribute_works_for_text(parser):
    html = "<div>foo bar</div>"
    html_parser = parser(html)
    node = html_parser.css_first("div").child
    assert node.html == "foo bar"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_text_node_returns_text(parser):
    html = "<div>foo bar</div>"
    html_parser = parser(html)
    node = html_parser.css_first("div").child
    assert node.text(deep=False) == "foo bar"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_text_node_returns_text_parent(parser):
    html = "<div>foo bar</div>"
    html_parser = parser(html)
    node = html_parser.css_first("div")
    assert node.text(deep=False) == "foo bar"


def test_text_node_returns_text_when_deep():
    html = "<div>foo bar</div>"
    html_parser = HTMLParser(html)
    node = html_parser.css_first("div").child
    assert node.text(deep=True) == "foo bar"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_unwrap(parser):
    html = '<a id="url" href="https://rushter.com/">I linked to <i>rushter.com</i></a>'
    html_parser = parser(html)
    node = html_parser.css_first("i")
    node.unwrap()
    assert (
        html_parser.body.child.html
        == '<a id="url" href="https://rushter.com/">I linked to rushter.com</a>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_unwrap_empty_tag(parser):
    html = '<a id="url" href="https://rushter.com/">I linked to rushter.com<i></i></a>'
    html_parser = parser(html)
    node = html_parser.css_first("i")
    node.unwrap(delete_empty=True)
    assert (
        html_parser.body.child.html
        == '<a id="url" href="https://rushter.com/">I linked to rushter.com</a>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_unwrap_tags(parser):
    html_parser = parser("<div><a href=>Hello</a> <i>world</i>!</div>")
    html_parser.body.unwrap_tags(["i", "a"])
    assert html_parser.body.html == "<body><div>Hello world!</div></body>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_unwrap_empty_tags(parser):
    html_parser = parser("<div><a href=>Hello</a> <i>world</i>!<i></i><a></a></div>")
    html_parser.body.unwrap_tags(["i", "a"], delete_empty=True)
    assert html_parser.body.html == "<body><div>Hello world!</div></body>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_unwraps_multiple_child_nodes(parser):
    html = """
    <div id="test">
        foo <span>bar <i>Lor<span>ems</span></i> I <span class='p3'>dummy <div>text</div></span></span>
    </div>
    """
    html_parser = parser(html)
    html_parser.body.unwrap_tags(["span", "i"])
    assert (
        html_parser.body.child.html
        == '<div id="test">\n        foo bar Lorems I dummy <div>text</div>\n    </div>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_unwraps_multiple_child_nodes_with_empty(parser):
    html = """
    <div id="test">
        foo <span>bar <i>Lor<span>ems</span></i> I <span class='p3'>dummy<span><i></i></span> <div>text</div></span></span>
    </div>
    """
    html_parser = parser(html)
    html_parser.body.unwrap_tags(["span", "i"], delete_empty=True)
    assert (
        html_parser.body.child.html
        == '<div id="test">\n        foo bar Lorems I dummy <div>text</div>\n    </div>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_replace_with(parser):
    html_parser = parser('<div>Get <img src="" alt="Laptop"></div>')
    img = html_parser.css_first("img")
    img.replace_with(img.attributes.get("alt", ""))
    assert html_parser.body.child.html == "<div>Get Laptop</div>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_replace_with_multiple_nodes(parser):
    html_parser = parser(
        '<div>Get <span alt="Laptop"><img src="/jpg"> <div>/div></span></div>'
    )
    img = html_parser.css_first("span")
    img.replace_with(img.attributes.get("alt", ""))
    assert html_parser.body.child.html == "<div>Get Laptop</div>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_node_replace_with(parser):
    html_parser = parser(
        '<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>'
    )
    html_parser2 = parser("<div>Test</div>")
    img_node = html_parser.css_first("img")
    img_node.replace_with(html_parser2.body.child)
    assert (
        html_parser.body.child.html
        == '<div>Get <span alt="Laptop"><div>Test</div> <div></div></span></div>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_replace_with_empty_string(parser):
    html_parser = parser('<div>Get <img src="" alt="Laptop"></div>')
    img = html_parser.css_first("img")
    img.replace_with("")
    assert html_parser.body.child.html == "<div>Get </div>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_replace_with_invalid_value_passed_exception(parser):
    with pytest.raises(TypeError) as excinfo:
        html_parser = parser('<div>Get <img src="" alt="Laptop"></div>')
        img = html_parser.css_first("img")
        img.replace_with(None)
    assert "No matching signature found" in str(excinfo.value)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_insert_before(parser):
    html_parser = parser('<div>Get <img src="" alt="Laptop"></div>')
    img = html_parser.css_first("img")
    img.insert_before(img.attributes.get("alt", ""))
    assert (
        html_parser.body.child.html == '<div>Get Laptop<img src="" alt="Laptop"></div>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_node_insert_before(parser):
    html_parser = parser(
        '<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>'
    )
    html_parser2 = parser("<div>Test</div>")
    img_node = html_parser.css_first("img")
    img_node.insert_before(html_parser2.body.child)
    assert (
        html_parser.body.child.html
        == '<div>Get <span alt="Laptop"><div>Test</div><img src="/jpg"> <div></div></span></div>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_insert_after(parser):
    html_parser = parser('<div>Get <img src="" alt="Laptop"></div>')
    img = html_parser.css_first("img")
    img.insert_after(img.attributes.get("alt", ""))
    assert (
        html_parser.body.child.html == '<div>Get <img src="" alt="Laptop">Laptop</div>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_node_insert_after(parser):
    html_parser = parser(
        '<div>Get <span alt="Laptop"><img src="/jpg"> <div></div></span></div>'
    )
    html_parser2 = parser("<div>Test</div>")
    img_node = html_parser.css_first("img")
    img_node.insert_after(html_parser2.body.child)
    assert (
        html_parser.body.child.html
        == '<div>Get <span alt="Laptop"><img src="/jpg"><div>Test</div> <div></div></span></div>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_insert_child(parser):
    html_parser = parser('<div>Get <img src=""></div>')
    div = html_parser.css_first("div")
    div.insert_child("Laptop")
    assert html_parser.body.child.html == '<div>Get <img src="">Laptop</div>'


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_node_insert_child(parser):
    html_parser = parser('<div>Get <span alt="Laptop"> <div>Laptop</div> </span></div>')
    html_parser2 = parser("<div>Test</div>")
    span_node = html_parser.css_first("span")
    span_node.insert_child(html_parser2.body.child)
    assert (
        html_parser.body.child.html
        == '<div>Get <span alt="Laptop"> <div>Laptop</div> <div>Test</div></span></div>'
    )


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_attrs_adds_attribute(parser):
    html_parser = parser('<div id="id"></div>')
    node = html_parser.css_first("div")
    node.attrs["new_att"] = "new"
    assert node.attributes == {"id": "id", "new_att": "new"}


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_attrs_sets_attribute(parser):
    html_parser = parser('<div id="id"></div>')
    node = html_parser.css_first("div")
    node.attrs["id"] = "new_id"
    assert node.attributes == {"id": "new_id"}


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_attrs_removes_attribute(parser):
    html_parser = parser('<div id="id"></div>')
    node = html_parser.css_first("div")
    del node.attrs["id"]
    assert node.attributes == {}


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_attrs_test_dict_features(parser):
    html_parser = parser('<div id="id" v data-id="foo"></div>')
    node = html_parser.css_first("div")
    node.attrs["new_att"] = "new"
    assert list(node.attrs.keys()) == ["id", "v", "data-id", "new_att"]
    assert list(node.attrs.values()) == ["id", None, "foo", "new"]
    assert len(node.attrs) == 4
    assert node.attrs.get("unknown_field", "default_value") == "default_value"
    assert "id" in node.attrs
    assert "vid" not in node.attrs


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_traverse(parser):
    html = (
        '<div id="parent"><div id="prev"></div><div id="test_node"><h1 id="child">Title</h1>'
        '<div>foo</div><img scr="image.jpg"></div><div id="next"></div></div>'
    )
    html_parser = parser(html)
    actual = [node.tag for node in html_parser.root.traverse()]
    expected = ["html", "head", "body", "div", "div", "div", "h1", "div", "img", "div"]
    assert actual == expected


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_traverse_with_text(parser):
    html = (
        '<div id="parent"><div id="prev"></div><div id="test_node"><h1 id="child">Title</h1>'
        '<div>foo</div><img scr="image.jpg"></div><div id="next"></div></div>'
    )
    html_parser = parser(html)
    actual = [node.tag for node in html_parser.root.traverse(include_text=True)]
    expected = [
        "html",
        "head",
        "body",
        "div",
        "div",
        "div",
        "h1",
        "-text",
        "div",
        "-text",
        "img",
        "div",
    ]
    assert actual == expected


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_node_comparison(parser):
    html = """
        <div>H3ll0</div><div id='tt'><p id='stext'>Lorem ipsum dolor sit amet, ea quo modus meliore platonem.</p></div>
    """
    html_parser = parser(html)
    nodes = [node for node in html_parser.root.traverse(include_text=False)]
    same_node_path_one = nodes[-1].parent
    same_node_path_two = nodes[-2]
    same_node_path_three = html_parser.css_first("#tt")
    assert same_node_path_one == same_node_path_two == same_node_path_three


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_node_comprassion_with_strings(parser):
    html = """<div id="test"></div>"""
    html_parser = parser(html)
    node = html_parser.css_first("#test")
    assert node == '<div id="test"></div>'


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_node_comparison_fails(parser):
    html = """<div id="test"></div>"""
    html_parser = parser(html)
    node = html_parser.css_first("#test")

    assert node is not None
    assert node != 123


def test_raw_value():
    html_parser = HTMLParser("<div>&#x3C;test&#x3E;</div>")
    selector = html_parser.css_first("div")
    assert selector.child.raw_value == b"&#x3C;test&#x3E;"
    assert selector.child.html == "&lt;test&gt;"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_adavanced_selector(parser):
    html_parser = parser("""
    <script>
     var super_value = 100;
    </script>
    """)
    selector = html_parser.select("script").text_contains("super_value")
    assert selector.any_matches


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_script_contain(parser):
    html_parser = parser("""
    <script>
     var super_value = 100;
    </script>
    """)
    assert html_parser.scripts_contain("super_value")


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_hash_nodes(parser):
    tree = parser("""<div><p><strong>J</strong>ohn</p><p>Doe</p></div>""")
    node = tree.css_first("div")
    assert node.mem_id == hash(node)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_srcs_contain(parser):
    html_parser = parser("""<script src="http://google.com/analytics.js"></script>""")
    assert html_parser.script_srcs_contain(("analytics.js",))


@pytest.mark.parametrize("parser", (HTMLParser,))
def test_css_chaining(parser):
    html = """
    <span class="red"></span>
    <div id="container">
        <span class="red"></span>
        <span class="green"></span>
        <span class="red"></span>
        <span class="green"></span>
    </div>
    <span class="red"></span>
    """
    tree = parser(html)
    assert len(tree.select("div").css("span").css(".red").matches) == 2


@pytest.mark.parametrize("parser", (HTMLParser,))
def test_css_chaining_two(parser):
    html = """
    <script  integrity="sha512-DHpNaMnQ8GaECHElNcJkpGhIThksyXA==" type="application/javascript" class="weird_script">
        var counter = 10;
    </script>
    """
    tree = parser(html)
    query = (
        tree.select("script")
        .text_contains("var counter = ")
        .css(".weird_script")
        .attribute_longer_than("integrity", 25)
    )
    assert query


@pytest.mark.parametrize("parser", (HTMLParser, LexborHTMLParser))
def test_content_method(parser):
    html = """
    <div>
        <div id="main">SuperTest</div>
    </div>
    """
    tree = parser(html)
    assert tree.css_first("#main").child.text_content == "SuperTest"
    assert tree.css_first("#main").text_content is None


@pytest.mark.parametrize("parser", (HTMLParser, LexborHTMLParser))
def test_merge_text_nodes(parser):
    html = """<div><p><strong>J</strong>ohn</p><p>Doe</p></div>"""
    tree = parser(html)
    tree.unwrap_tags(["strong"])
    node = tree.css_first("div", strict=True)
    node.merge_text_nodes()
    assert node.html == "<div><p>John</p><p>Doe</p></div>"
    text = tree.text(deep=True, separator=" ", strip=True)
    assert text == "John Doe"


@pytest.mark.parametrize("parser", (HTMLParser, LexborHTMLParser))
def test_merge_text_nodes_complex(parser):
    from textwrap import dedent

    html = dedent("""
        <article>
            <h1><em>H</em>ello <strong>W</strong>orld</h1>
            <div>
                <p>This <span>i</span>s <b>a</b> <i>t</i>est</p>
                <section>
                    <span>Nested</span> <span>text</span> nodes
                    <div>with <em>m</em>ore <strong>nesting</strong> here</div>
                </section>
            </div>
        </article>
    """).strip()
    tree = parser(html)
    tree.unwrap_tags(["em", "strong", "span", "b", "i"])
    root = tree.css_first("article", strict=True)
    root.merge_text_nodes()
    assert root.css_first("h1").text() == "Hello World"
    assert root.css_first("p").text() == "This is a test"
    assert "Nested text nodes" in root.css_first("section").text()
    assert root.css_first("section > div").text() == "with more nesting here"


@pytest.mark.parametrize("parser", (HTMLParser, LexborHTMLParser))
def test_merge_text_nodes_three_plus(parser):
    html = """<div><em>O</em><strong>n</strong><b>e</b> <i>T</i><span>w</span><u>o</u> <small>T</small><big>h</big><mark>r</mark><sub>e</sub><sup>e</sup></div>"""
    tree = parser(html)
    tree.unwrap_tags(
        ["em", "strong", "b", "i", "span", "u", "small", "big", "mark", "sub", "sup"]
    )
    div = tree.css_first("div", strict=True)
    div.merge_text_nodes()
    assert div.text() == "One Two Three"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_css_first_first(parser):
    html = '<h2 class="list-details__item__partial" id="js-partial">(1:1, 0:0, 0:0, 5:3)</h2>'
    selector = "h2.list-details__item__partial"
    find_first = parser(html).css_first(selector)
    assert find_first.css_first(selector) is not None


@pytest.mark.parametrize("parser", (LexborHTMLParser,))
def test_any_css_matches_fails(parser):
    html = """<h1>Test</h1>"""
    tree = parser(html)
    with pytest.raises(SelectolaxError):
        tree.any_css_matches(("##",))


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_text_separator_correctness(parser):
    inner = "".join(f"<span>word{i}</span>" for i in range(50))
    html = f"<div>{inner}</div>"
    tree = parser(html)
    node = tree.css_first("div")

    result = node.text(deep=True, separator=" ")
    parts = result.split(" ")

    assert parts[-1] != "", "Trailing separator found; join() not used correctly"
    assert len(parts) == 50
    for i, part in enumerate(parts):
        assert part == f"word{i}"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_text_strip_and_separator(parser):
    html = "<div><p>  hello  </p><p>  world  </p></div>"
    tree = parser(html)
    node = tree.css_first("div")

    result = node.text(deep=True, separator="|", strip=True)
    assert result == "hello|world"


def test_attribute_longer_than_missing_attribute():
    html = """
    <div>
        <a href="http://very-long-url.example.com/path/to/page">with href</a>
        <a>no href at all</a>
        <a href="short">short href</a>
    </div>
    """
    tree = HTMLParser(html)
    selector = tree.root.select("a").attribute_longer_than("href", 10)
    matches = selector.matches
    assert len(matches) == 1
    assert "very-long-url" in matches[0].attributes["href"]


def test_attribute_longer_than_missing_attribute_with_start():
    html = """
    <div>
        <a href="http://long-domain.example.com/page">with href</a>
        <a>no href</a>
    </div>
    """
    tree = HTMLParser(html)
    selector = tree.root.select("a").attribute_longer_than("href", 15, "http://")
    matches = selector.matches
    assert len(matches) == 1


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_any_attribute_longer_than_missing_attribute(parser):
    html = """
    <div>
        <a href="http://very-long-url.example.com/path/to/page">with href</a>
        <a>no href at all</a>
        <a href="short">short href</a>
    </div>
    """
    tree = parser(html)
    # Must not raise TypeError despite the middle <a> having no href
    assert tree.root.select("a").any_attribute_longer_than("href", 10) is True
    assert tree.root.select("a").any_attribute_longer_than("href", 200) is False


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_any_attribute_longer_than_all_missing(parser):
    html = "<div><a>one</a><a>two</a></div>"
    tree = parser(html)
    assert tree.root.select("a").any_attribute_longer_than("href", 0) is False

```

### `tests/test_parser.py`

```py
import threading
from difflib import SequenceMatcher

import pytest
from selectolax.parser import HTMLParser, Node

from selectolax.lexbor import LexborHTMLParser, LexborNode, SelectolaxError, create_tag

"""
We'are testing only our own code.
Many functionality are already tested in the Modest engine, so there is no reason to test every case.
"""

_PARSERS_PARAMETRIZER = (
    "parser",
    (HTMLParser, LexborHTMLParser),
)


def test_encoding():
    html = "<div><p id=p1><p id=p2><p id=p3><a>link</a><p id=p4><p id=p5>text<p id=p6></div>"
    html = HTMLParser(html)
    assert html.input_encoding == "UTF-8"

    html = b"<div><p id=p1><p id=p2><p id=p3><a>link</a><p id=p4><p id=p5>text<p id=p6></div>"
    html = HTMLParser(html)
    assert html.input_encoding == "UTF-8"

    html = "<div>Привет мир!</div>".encode("cp1251")
    assert HTMLParser(html, detect_encoding=True).input_encoding == "WINDOWS-1251"

    html_utf = '<head><meta charset="WINDOWS-1251"></head>'.encode("utf-8")
    assert (
        HTMLParser(html_utf, detect_encoding=True, use_meta_tags=True).input_encoding
        == "WINDOWS-1251"
    )

    # UTF-16 not ASCII-readable
    html_utf = '<head><meta charset="WINDOWS-1251"></head>'.encode("utf-16le")
    assert (
        HTMLParser(html_utf, detect_encoding=True, use_meta_tags=True).input_encoding
        == "UTF-16LE"
    )

    # Unencodable characters in string, should not throw an exception by default
    html_unencodable = b"<div>Roboto+Condensed</div>".decode("utf-7", errors="ignore")
    assert HTMLParser(html_unencodable).input_encoding == "UTF-8"

    # decode_errrors='strict' should error out
    try:
        HTMLParser(html_unencodable, decode_errors="strict")
        assert False
    except Exception as e:
        assert type(e) is UnicodeEncodeError


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_parser(parser):
    html = parser("")
    assert isinstance(html, parser)

    with pytest.raises(TypeError):
        parser(123)

    with pytest.raises(TypeError):
        parser("asd").css(123)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_malformed_data(parser):
    malformed_inputs = [
        b"\x00\x01\x02\x03",
        "<div><p><span></div>",
        "<" + "a" * 1000 + ">",
    ]

    for malformed_html in malformed_inputs:
        try:
            html_parser = parser(malformed_html)
            # Should not crash, but may return None or empty results
            result = html_parser.html
            assert result is None or isinstance(result, str)
        except (ValueError, RuntimeError, UnicodeDecodeError):
            # These exceptions are acceptable for malformed input
            pass


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_properties(parser):
    html_parser = parser("<div><p>test</p></div>")

    properties_to_test = ["root", "head", "body", "html"]

    for prop_name in properties_to_test:
        getattr(html_parser, prop_name)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_unicode_handling(parser):
    unicode_content = [
        "Hello 世界",
        "🚀🌟💫",
        "Café résumé naïve",
    ]

    for content in unicode_content:
        html = f"<div>{content}</div>"
        try:
            html_parser = parser(html)
            result = html_parser.css_first("div")
            if result:
                extracted_text = result.text()
                assert content in extracted_text
        except UnicodeEncodeError:
            # Some encoding issues might be expected
            pass


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_tag_name_validation(parser):
    """Test that tag name validation works correctly."""
    html_parser = parser("<div></div>")

    # Empty tag name should be rejected
    with pytest.raises(ValueError, match="Tag name cannot be empty"):
        html_parser.tags("")

    # Very long tag names should be rejected
    long_tag_name = "a" * 101  # Exceeds 100 character limit
    with pytest.raises(ValueError, match="Tag name is too long"):
        html_parser.tags(long_tag_name)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_nodes(parser):
    html = (
        '<div><p id="p1"></p><p id="p2"></p><p id="p3"><a>link</a></p>'
        '<p id="p4"></p><p id="p5">text</p><p id="p6"></p></div>'
    )
    htmlp = parser(html)

    assert isinstance(htmlp.root, (Node, LexborNode))
    assert isinstance(htmlp.body, (Node, LexborNode))
    html_output = htmlp.html
    assert len(html_output) >= len(html)
    assert SequenceMatcher(None, html, html_output).ratio() > 0.8


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_root_css(parser):
    tree = parser("test")
    assert len(tree.root.css("data")) == 0


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_strip_tags_from_root(parser):
    html = "<body><div></div><script></script></body>"
    html_parser = parser(html)
    html_parser.root.strip_tags(["div", "script"])
    assert html_parser.html == "<html><head></head><body></body></html>"

    with pytest.raises(TypeError):
        html_parser.strip_tags(1)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_clone(parser):
    html_parser = parser("""<h1>Welcome</h1>""")
    clone = html_parser.clone()
    html_parser.root.css_first("h1").decompose()
    del html_parser
    assert clone.html == "<html><head></head><body><h1>Welcome</h1></body></html>"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_tags(parser):
    html_parser = parser("""
    <div><span><span></span></span></div>
    <div><span></span></div>
    <div><div></div></div>
    <span></span>
    <div></div>
    """)
    assert len(html_parser.tags("div")) == 5


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_preserves_doctype(parser):
    html_parser = parser("""
    <!DOCTYPE html>
    <html>
        <head><title>Test</title></head>
        <body><p>Hello World</p></body>
    </html>
    """)
    assert "<!DOCTYPE html>" in html_parser.html


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_invalid_input_types(parser):
    with pytest.raises(TypeError, match="Expected a string"):
        parser(123)

    with pytest.raises(TypeError, match="Expected a string"):
        parser([])

    with pytest.raises(TypeError, match="Expected a string"):
        parser(None)


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_clone_handling(parser):
    html_parser = parser("<div>test</div>")

    cloned = html_parser.clone()
    assert cloned.html is not None

    assert html_parser.html is not None


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_concurrent_parsing(parser):
    """Test that concurrent parsing doesn't cause race conditions."""
    results = []
    errors = []
    lock = threading.Lock()

    def parse_html(content):
        try:
            html_parser = parser(content)
            result = html_parser.body.text()
            if result:
                with lock:
                    results.append(result)
        except Exception as e:
            with lock:
                errors.append(e)

    threads = []
    test_content = "<div>Content {}</div>"

    for i in range(50):
        content = test_content.format(i)
        t1 = threading.Thread(target=parse_html, args=(content,))
        threads.append(t1)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    assert len(errors) == 0
    assert len(results) == 50


def test_css_selector_error_handling():
    html_parser = LexborHTMLParser("<div class='test'>content</div>")

    # Invalid selector types should raise TypeError
    with pytest.raises(TypeError):
        html_parser.css(123)

    with pytest.raises(TypeError):
        html_parser.css(None)

    invalid_selectors = [
        ":::",
        "[[[",
        "div{color:red}",
        'h3:contains("some substring")',
    ]

    for selector in invalid_selectors:
        try:
            result = html_parser.css(selector)
            # Should return empty list or raise specific exception
            assert isinstance(result, list)
        except SelectolaxError:
            # Specific parsing errors are acceptable
            pass


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_null_pointer_safety(parser):
    """Test that NULL pointer checks prevent crashes."""
    # Test edge cases that might result in NULL pointers
    edge_cases = [
        "",  # Empty HTML
        "<>",  # Empty tag
        "<!>",  # Empty declaration
        "<html></html>",  # Minimal valid HTML
    ]
    properties_to_test = ["root", "head", "body", "html"]
    for html_content in edge_cases:
        html_parser = parser(html_content)

        for prop_name in properties_to_test:
            getattr(html_parser, prop_name)


def test_decompose_root_node():
    html_parser = LexborHTMLParser("<div><p>test</p></div>")
    with pytest.raises(SelectolaxError):
        html_parser.root.decompose()


def test_empty_attribute_lexbor():
    div = create_tag("div")
    div.attrs["hidden"] = None
    assert div.html == '<div hidden=""></div>'


def test_pseudo_class_contains():
    html = "<div><p>hello world</p><p id='main'>AwesOme t3xt</p></div>"
    parser = LexborHTMLParser(html)
    results = parser.css('p:lexbor-contains("awesome" i)')
    assert len(results) == 1
    assert results[0].text() == "AwesOme t3xt"


@pytest.mark.parametrize(*_PARSERS_PARAMETRIZER)
def test_css_matches_returns_bool(parser):
    res = parser("<div>test</div>").css_matches("div")
    assert isinstance(res, bool)
    assert res is True

```

### `tests/test_utils.py`

```py
"""
We'are testing only our own code.
Many functionality are already tested in the Modest engine, so there is no reason to test every case.
"""

from typing import Callable, NamedTuple, Sequence, Type, Union

import pytest
from selectolax.parser import HTMLParser, Node, create_tag, parse_fragment
from selectolax.lexbor import (
    LexborHTMLParser,
    LexborNode,
    create_tag as lexbor_create_tag,
    parse_fragment as lexbor_parse_fragment,
)


class Impl(NamedTuple):
    parser: Union[Type[HTMLParser], Type[LexborHTMLParser]]
    node: Union[Type[Node], Type[LexborNode]]
    tag_fn: Callable[[str], Union[Node, LexborNode]]
    parse_fragment_fn: Callable[[str], Sequence[Union[Node, LexborNode]]]


_IMPL_PARAMETRIZER = (
    "impl",
    (
        Impl(
            parser=HTMLParser,
            node=Node,
            tag_fn=create_tag,
            parse_fragment_fn=parse_fragment,
        ),
        Impl(
            parser=LexborHTMLParser,
            node=LexborNode,
            tag_fn=lexbor_create_tag,
            parse_fragment_fn=lexbor_parse_fragment,
        ),
    ),
)


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_create_tag(impl: Impl):
    node = impl.tag_fn("p")
    assert isinstance(node, impl.node)
    assert node.html == "<p></p>"


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_create_header_tag(impl: Impl):
    node = impl.tag_fn("header")
    assert isinstance(node, impl.node)
    assert node.html == "<header></header>"


# Cases to test parse_fragment():
# - <doctyle> + <html> only
# - HTML with <head>
# - HTML with <body>
# - HTML with <doctype>, <head> and <body>
# - <head> and <body> only without <html>
# - <head> only
# - <body> only
# - <link> and <meta>'s only (as content of <head>)
# - <div>, <script> (as content of <body>)
# - <link> and <div> next to each other (as invalid HTML, but valid fragment)


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_parse_fragment_doctype_html(impl: Impl):
    html = "<!DOCTYPE html><html></html>"
    nodes = impl.parse_fragment_fn(html)
    assert len(nodes) == 1
    assert nodes[0].tag == "html"
    assert nodes[0].html == "<html></html>"
    assert nodes[0].parser.html == "<!DOCTYPE html><html></html>"

    assert len(nodes[0].parser.css("head")) == 0
    assert len(nodes[0].parser.css("body")) == 0


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_parse_fragment_html_with_head(impl: Impl):
    html = '<!DOCTYPE html><html><head><link href="http://"></head></html>'
    nodes = impl.parse_fragment_fn(html)
    assert len(nodes) == 1
    assert nodes[0].tag == "html"
    assert nodes[0].html == '<html><head><link href="http://"></head></html>'
    assert (
        nodes[0].parser.html
        == '<!DOCTYPE html><html><head><link href="http://"></head></html>'
    )

    assert len(nodes[0].parser.css("head")) == 1
    assert len(nodes[0].parser.css("body")) == 0


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_parse_fragment_html_with_body(impl: Impl):
    html = '<!DOCTYPE html><html><body><div><script src="http://"></script></div></body></html>'
    nodes = impl.parse_fragment_fn(html)
    assert len(nodes) == 1
    assert nodes[0].tag == "html"
    assert (
        nodes[0].html
        == '<html><body><div><script src="http://"></script></div></body></html>'
    )
    assert (
        nodes[0].parser.html
        == '<!DOCTYPE html><html><body><div><script src="http://"></script></div></body></html>'
    )

    assert len(nodes[0].parser.css("head")) == 0
    assert len(nodes[0].parser.css("body")) == 1


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_parse_fragment_html_with_head_and_body(impl: Impl):
    html = '<!DOCTYPE html><html><head><link href="http://"></head><body><div><script src="http://"></script></div></body></html>'  # noqa: E501
    nodes = impl.parse_fragment_fn(html)
    assert len(nodes) == 1
    assert nodes[0].tag == "html"
    assert (
        nodes[0].html
        == '<html><head><link href="http://"></head><body><div><script src="http://"></script></div></body></html>'
    )  # noqa: E501
    assert (
        nodes[0].parser.html
        == '<!DOCTYPE html><html><head><link href="http://"></head><body><div><script src="http://"></script></div></body></html>'
    )  # noqa: E501

    assert len(nodes[0].parser.css("head")) == 1
    assert len(nodes[0].parser.css("body")) == 1


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_parse_fragment_head_and_body_no_html(impl: Impl):
    html = '<head><link href="http://"></head><body><div><script src="http://"></script></div></body>'
    nodes = impl.parse_fragment_fn(html)
    assert len(nodes) == 2
    assert nodes[0].tag == "head"
    assert nodes[1].tag == "body"
    assert nodes[0].html == '<head><link href="http://"></head>'
    assert nodes[1].html == '<body><div><script src="http://"></script></div></body>'
    assert (
        nodes[0].parser.html
        == '<html><head><link href="http://"></head><body><div><script src="http://"></script></div></body></html>'
    )  # noqa: E501

    assert len(nodes[0].parser.css("head")) == 1
    assert len(nodes[0].parser.css("body")) == 1


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_parse_fragment_head_no_html(impl: Impl):
    html = '<head><link href="http://"></head>'
    nodes = impl.parse_fragment_fn(html)
    assert len(nodes) == 1
    assert nodes[0].tag == "head"
    assert nodes[0].html == '<head><link href="http://"></head>'
    assert nodes[0].parser.html == '<html><head><link href="http://"></head></html>'

    assert len(nodes[0].parser.css("head")) == 1
    assert len(nodes[0].parser.css("body")) == 0


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_parse_fragment_body_no_html(impl: Impl):
    html = '<body><div><script src="http://"></script></div></body>'
    nodes = impl.parse_fragment_fn(html)
    assert len(nodes) == 1
    assert nodes[0].tag == "body"
    assert nodes[0].html == '<body><div><script src="http://"></script></div></body>'
    assert (
        nodes[0].parser.html
        == '<html><body><div><script src="http://"></script></div></body></html>'
    )

    assert len(nodes[0].parser.css("head")) == 0
    assert len(nodes[0].parser.css("body")) == 1


@pytest.mark.parametrize(*_IMPL_PARAMETRIZER)
def test_parse_fragment_fragment(impl: Impl):
    html = '<link href="http://"><div><script src="http://"></script></div>'
    nodes = impl.parse_fragment_fn(html)
    assert len(nodes) == 2
    assert nodes[0].tag == "link"
    assert nodes[1].tag == "div"
    assert nodes[0].html == '<link href="http://">'
    assert nodes[1].html == '<div><script src="http://"></script></div>'

    # NOTE: Ideally the full HTML would NOT contain `<html>`, `<head>` and `<body>` in this case,
    # but this is technical limitation of the parser.
    # But as long as user serializes fragment nodes by as `Node.html`, they should be fine.
    assert (
        nodes[0].parser.html
        == '<html><head><link href="http://"></head><body><div><script src="http://"></script></div></body></html>'
    )  # noqa: E501
    assert len(nodes[0].parser.css("head")) == 1
    assert len(nodes[0].parser.css("body")) == 1

```

### `typesafety/test_lexbor.yaml`

```yaml
- case: html_parser_css_first_without_default
  parametrized:
    - strict: True
    - strict: False
  main: |
    from selectolax.parser import HTMLParser
    parser = HTMLParser("")
    node = parser.css_first(query="", strict= {{ strict }})
    reveal_type(node) # N: Revealed type is "Union[selectolax.parser.Node, None]"

- case: html_parser_css_first_with_none_default
  parametrized:
    - strict: True
    - strict: False
  main: |
    from selectolax.parser import HTMLParser
    parser = HTMLParser("")
    node = parser.css_first(query="",default=None,strict= {{strict}})
    reveal_type(node) # N: Revealed type is "Union[selectolax.parser.Node, None]"

- case: html_parser_css_first_with_default
  parametrized:
    - strict: True
    - strict: False
  main: |
    from selectolax.parser import HTMLParser
    parser = HTMLParser("")
    node = parser.css_first(query="",default="", strict ={{strict}})
    reveal_type(node) # N: Revealed type is "Union[selectolax.parser.Node, builtins.str]"


- case: lexbor_node_css_first_without_default
  parametrized:
    - strict: True
    - strict: False
  main: |
    from selectolax.parser import HTMLParser
    parser = HTMLParser("")
    node = parser.root
    if node is not None:
      res = node.css_first(query="", strict ={{strict}})
      reveal_type(res) # N: Revealed type is "Union[selectolax.parser.Node, None]"

- case: lexbor_node_css_first_with_none_default
  parametrized:
    - strict: True
    - strict: False
  main: |
    from selectolax.parser import HTMLParser
    parser = HTMLParser("")
    node = parser.root
    if node is not None:
      res = node.css_first(query="",default=None, strict ={{strict}})
      reveal_type(res) # N: Revealed type is "Union[selectolax.parser.Node, None]"

- case: lexbor_node_css_first_with_default
  parametrized:
    - strict: True
    - strict: False
  main: |
    from selectolax.parser import HTMLParser
    parser = HTMLParser("")
    node = parser.root
    if node is not None:
      res = node.css_first(query="",default="", strict ={{strict}})
      reveal_type(res) # N: Revealed type is "Union[selectolax.parser.Node, builtins.str]"
```
