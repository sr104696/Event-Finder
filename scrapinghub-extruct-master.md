# scrapinghub/extruct@master

- Files included: 162
- Files skipped: 6
- Total size: 593.2 KB
- Estimated tokens: ~151,807

## Directory Structure

```
├── .github
│   ├── workflows
│   │   ├── python-package.yml
│   │   └── python-publish.yml
│   └── dependabot.yml
├── extruct
│   ├── __init__.py
│   ├── __main__.py
│   ├── _extruct.py
│   ├── dublincore.py
│   ├── jsonld.py
│   ├── microformat.py
│   ├── opengraph.py
│   ├── rdfa.py
│   ├── tool.py
│   ├── uniform.py
│   ├── utils.py
│   ├── VERSION
│   ├── w3cmicrodata.py
│   └── xmldom.py
├── tests
│   ├── samples
│   │   ├── custom.invalid
│   │   │   ├── AllocateAction.001.html
│   │   │   ├── AllocateAction.001.jsonld
│   │   │   ├── JoinAction.001.html
│   │   │   ├── JoinAction.001.jsonld
│   │   │   ├── JSONLD_with_control_characters_comment.html
│   │   │   ├── JSONLD_with_control_characters_comment.jsonld
│   │   │   ├── JSONLD_with_control_characters.html
│   │   │   ├── JSONLD_with_control_characters.jsonld
│   │   │   ├── JSONLD_with_JS_comment.html
│   │   │   └── JSONLD_with_JS_comment.jsonld
│   │   ├── misc
│   │   │   ├── dublincore_test.html
│   │   │   ├── dublincore_test.json
│   │   │   ├── expanded_OG_support_test.html
│   │   │   ├── expanded_OG_support_test.json
│   │   │   ├── microformat_flat_test.json
│   │   │   ├── microformat_test.html
│   │   │   ├── microformat_test.json
│   │   │   ├── null_ld_mock.html
│   │   │   ├── null_ld_mock.jsonld
│   │   │   ├── opengraph_flat_test.json
│   │   │   ├── opengraph_ns_product_test.html
│   │   │   ├── opengraph_ns_product_test.json
│   │   │   ├── opengraph_test.html
│   │   │   ├── opengraph_test.json
│   │   │   ├── Portfolio_Niels_Lubberman.html
│   │   │   ├── Portfolio_Niels_Lubberman.json
│   │   │   └── product_microdata.html
│   │   ├── schema.org
│   │   │   ├── CreativeWork_flat_with_node_id.001.json
│   │   │   ├── CreativeWork_flat.001.json
│   │   │   ├── CreativeWork.001.html
│   │   │   ├── CreativeWork.001.json
│   │   │   ├── CreativeWork.001.jsonld
│   │   │   ├── Event.001.html
│   │   │   ├── Event.001.json
│   │   │   ├── Event.002.html
│   │   │   ├── Event.002.json
│   │   │   ├── Event.003.html
│   │   │   ├── Event.003.json
│   │   │   ├── Event.004.html
│   │   │   ├── Event.004.json
│   │   │   ├── Event.008.html
│   │   │   ├── Event.008.json
│   │   │   ├── LocalBusiness.002.html
│   │   │   ├── LocalBusiness.002.json
│   │   │   ├── LocalBusiness.003.html
│   │   │   ├── LocalBusiness.003.json
│   │   │   ├── MusicRecording.001.html
│   │   │   ├── MusicRecording.001.json
│   │   │   ├── product_custom_url_and_node_id.json
│   │   │   ├── product_custom_url.json
│   │   │   ├── product-ref.html
│   │   │   ├── product-ref.json
│   │   │   ├── product.html
│   │   │   ├── product.json
│   │   │   ├── SearchAction.001.html
│   │   │   └── SearchAction.001.json
│   │   ├── schema.org.invalid
│   │   │   ├── AllocateAction.001.html
│   │   │   ├── AllocateAction.001.jsonld
│   │   │   ├── JoinAction.001.html
│   │   │   └── JoinAction.001.jsonld
│   │   ├── songkick
│   │   │   ├── Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015.html
│   │   │   ├── Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015.jsonld
│   │   │   ├── elysianfields_1.html
│   │   │   ├── elysianfields_1.json
│   │   │   ├── elysianfields.html
│   │   │   ├── elysianfields.json
│   │   │   ├── jsonld_empty_item_test.html
│   │   │   ├── jsonld_empty_item_test.jsonld
│   │   │   ├── Maxïmo Park Gigography, Tour History & Past Concerts.html
│   │   │   ├── Maxïmo Park Gigography, Tour History & Past Concerts.jsonld
│   │   │   ├── tovestyrke.html
│   │   │   ├── tovestyrke.json
│   │   │   ├── Years & Years Tickets, Tour Dates 2015 & Concerts.html
│   │   │   └── Years & Years Tickets, Tour Dates 2015 & Concerts.jsonld
│   │   ├── w3c
│   │   │   ├── microdata.4.2.data.html
│   │   │   ├── microdata.4.2.data.json
│   │   │   ├── microdata.4.2.meter.html
│   │   │   ├── microdata.4.2.meter.json
│   │   │   ├── microdata.4.2.strings.html
│   │   │   ├── microdata.4.2.strings.json
│   │   │   ├── microdata.4.2.strings.unclean.html
│   │   │   ├── microdata.4.2.strings.unclean.json
│   │   │   ├── microdata.5.2.flat.json
│   │   │   ├── microdata.5.2.html
│   │   │   ├── microdata.5.2.json
│   │   │   ├── microdata.5.2.withtext.json
│   │   │   ├── microdata.5.3.html
│   │   │   ├── microdata.5.3.json
│   │   │   ├── microdata.5.5.html
│   │   │   ├── microdata.5.5.json
│   │   │   ├── microdata.7.1.flat.json
│   │   │   ├── microdata.7.1.html
│   │   │   ├── microdata.7.1.json
│   │   │   ├── microdata.object.html
│   │   │   └── microdata.object.json
│   │   ├── w3crdfa
│   │   │   ├── w3c.rdf11primer.example014.expanded.json
│   │   │   ├── w3c.rdf11primer.example014.html
│   │   │   ├── w3c.rdfalite.example003.expanded.json
│   │   │   ├── w3c.rdfalite.example003.html
│   │   │   ├── w3c.rdfalite.example004.expanded.json
│   │   │   ├── w3c.rdfalite.example004.html
│   │   │   ├── w3c.rdfalite.example005.expanded.json
│   │   │   ├── w3c.rdfalite.example005.html
│   │   │   ├── w3c.rdfaprimer.example005.expanded.json
│   │   │   ├── w3c.rdfaprimer.example005.html
│   │   │   ├── w3c.rdfaprimer.example006.expanded.json
│   │   │   ├── w3c.rdfaprimer.example006.html
│   │   │   ├── w3c.rdfaprimer.example007.expanded.json
│   │   │   ├── w3c.rdfaprimer.example007.html
│   │   │   ├── w3c.rdfaprimer.example008.expanded.json
│   │   │   ├── w3c.rdfaprimer.example008.html
│   │   │   ├── w3c.rdfaprimer.example009.expanded.json
│   │   │   ├── w3c.rdfaprimer.example009.html
│   │   │   ├── w3c.rdfaprimer.example010.expanded.json
│   │   │   ├── w3c.rdfaprimer.example010.html
│   │   │   ├── w3c.rdfaprimer.example011.expanded.json
│   │   │   ├── w3c.rdfaprimer.example011.html
│   │   │   ├── w3c.rdfaprimer.example015.expanded.json
│   │   │   └── w3c.rdfaprimer.example015.html
│   │   ├── websites
│   │   │   ├── microdata-with-description.html
│   │   │   └── microdata-with-description.json
│   │   └── wikipedia
│   │       ├── xhtml+rdfa.expanded.json
│   │       └── xhtml+rdfa.html
│   ├── __init__.py
│   ├── test_dublincore.py
│   ├── test_extruct_uniform.py
│   ├── test_extruct.py
│   ├── test_jsonld.py
│   ├── test_microdata.py
│   ├── test_microformat.py
│   ├── test_opengraph.py
│   ├── test_rdfa.py
│   ├── test_tool.py
│   └── test_uniform.py
├── .coveragerc
├── .git-blame-ignore-revs
├── .gitattributes
├── .gitignore
├── .isort.cfg
├── .pre-commit-config.yaml
├── AUTHORS
├── HISTORY.rst
├── LICENSE
├── pyproject.toml
├── pytest.ini
├── README.rst
├── requirements-dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
└── tox.ini
```

## Code Digest

### `.coveragerc`

```coveragerc
[run]
branch = true
source = extruct
omit = extruct/service.py

```

### `.git-blame-ignore-revs`

```git-blame-ignore-revs
# Contains commits to be ignored due to linting

# https://github.com/scrapinghub/extruct/pull/201
c52cdf2a0caaeaaa0bee978b9d06451c93b7e8be
f6c235fa8a7513f21cb3381bfa429674cc566781
f2fc2231706905de1b818fae2040ef61ed2c4418

```

### `.gitattributes`

```gitattributes
tests/samples/** linguist-vendored

```

### `.github/dependabot.yml`

```yml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
    groups:
      github-actions:
        patterns:
          - "*"

```

### `.github/workflows/python-package.yml`

```yml
# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: tox

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  test:

    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements-dev.txt
    - name: tox
      run: |
        tox -e `python -c "import sys; print('py' + ''.join(sys.version.split('.')[:2]))"`
    - name: Upload coverage report
      uses: codecov/codecov-action@v5
      with:
        token: ${{ secrets.CODECOV_TOKEN }}

  check:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ['3.12']
        tox-job: ["linters"]

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements-dev.txt
    - name: tox
      run: |
        tox -e ${{ matrix.tox-job }}

```

### `.github/workflows/python-publish.yml`

```yml
# This workflows will upload a Python Package using Twine when a release is created
# For more information see: https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions#publishing-to-package-registries

name: publish

on:
  push:
    tags:
      - "v*"

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install setuptools wheel twine
    - name: Build and publish
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
      run: |
        python setup.py sdist bdist_wheel
        twine upload dist/*

```

### `.gitignore`

```gitignore
# Python
*.pyc
*.pyo
/build/
/dist/
*.egg-info

# Mac OS
*.DS_Store

# IDE
/.idea/

.cache/
.tox/
.pytest_cache/
.coverage

```

### `.isort.cfg`

```cfg
[settings]
profile=black

```

### `.pre-commit-config.yaml`

```yaml
repos:
  - hooks:
      - id: black
    repo: https://github.com/psf/black-pre-commit-mirror
    rev: 24.4.2
  - hooks:
      - id: isort
    repo: https://github.com/PyCQA/isort
    rev: 5.13.2
  - hooks:
    - id: mypy
      additional_dependencies: [types-requests, types-mock, lxml-stubs]
    repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
  - hooks:
    - id: pyupgrade
    repo: https://github.com/asottile/pyupgrade
    rev: v3.15.2

```

### `AUTHORS`

```
Authors
=======

* Paul Trembeth <paul@scrapingub.com>
* Andres Moreira <andres@scrapinghub.com>
* Elias Dorneles <elias@scrapinghub.com>

```

### `extruct/__init__.py`

```py
from ._extruct import SYNTAXES, extract
from .jsonld import JsonLdExtractor
from .microformat import MicroformatExtractor
from .opengraph import OpenGraphExtractor
from .rdfa import RDFaExtractor
from .w3cmicrodata import MicrodataExtractor
from .xmldom import XmlDomHTMLParser

```

### `extruct/__main__.py`

```py
from extruct.tool import main

if __name__ == "__main__":
    print(main())

```

### `extruct/_extruct.py`

```py
from __future__ import annotations

import logging
import warnings
from typing import Any, Callable

from lxml.html import HtmlElement

from extruct.dublincore import DublinCoreExtractor
from extruct.jsonld import JsonLdExtractor
from extruct.microformat import MicroformatExtractor
from extruct.opengraph import OpenGraphExtractor
from extruct.rdfa import RDFaExtractor
from extruct.uniform import _udublincore, _umicrodata_microformat, _uopengraph
from extruct.utils import parse_html, parse_xmldom_html
from extruct.w3cmicrodata import MicrodataExtractor

logger = logging.getLogger(__name__)
SYNTAXES = ["microdata", "opengraph", "json-ld", "microformat", "rdfa", "dublincore"]


def extract(
    htmlstring_or_tree: str | bytes | HtmlElement,
    base_url: str | None = None,
    encoding: str = "UTF-8",
    syntaxes: list[str] = SYNTAXES,
    errors: str = "strict",
    uniform: bool = False,
    return_html_node: bool = False,
    schema_context: str = "http://schema.org",
    with_og_array: bool = False,
    url: str | None = None,  # deprecated
) -> dict[str, list[dict[str, Any]]]:
    """
    htmlstring: string with valid html document;
    base_url: base url of the html document
    encoding: encoding of the html document
    syntaxes: list of syntaxes to extract, default SYNTAXES
    errors: set to 'log' to log the exceptions, 'ignore' to ignore them
            or 'strict'(default) to raise them
    uniform: if True uniform output format of all syntaxes to a list of dicts.
             Returned dicts structure:
             {'@context': 'http://example.com',
              '@type': 'example_type',
              /* All other the properties in keys here */
              }
    return_html_node: if True, it includes into the result a HTML node of
                      respective embedded metadata under 'htmlNode' key.
                      The feature is supported only by microdata syntax.
                      Each node is of `lxml.etree.Element` type.
    schema_context: schema's context for current page"""
    if base_url is None and url is not None:
        warnings.warn(
            '"url" argument is deprecated, please use "base_url"',
            DeprecationWarning,
            stacklevel=2,
        )
        base_url = url
    if not (isinstance(syntaxes, list) and all(v in SYNTAXES for v in syntaxes)):
        raise ValueError(
            "syntaxes must be a list with any or all (default) of"
            "these values: {}".format(SYNTAXES)
        )
    if errors not in ["log", "ignore", "strict"]:
        raise ValueError(
            'Invalid error command, valid values are either "log"'
            ', "ignore" or "strict"'
        )
    if isinstance(htmlstring_or_tree, (str, bytes)):
        parser = parse_xmldom_html if "rdfa" in syntaxes else parse_html
        try:
            tree = parser(htmlstring_or_tree, encoding=encoding)
        except Exception as e:
            if errors == "ignore":
                return {}
            if errors == "log":
                logger.exception("Failed to parse html, raises {}".format(e))
                return {}
            if errors == "strict":
                raise
    else:
        if "microformat" in syntaxes:
            raise ValueError(
                "'microformat' syntax requires a string, not a parsed tree. "
                "Consider adjusting the 'syntaxes' argument to exclude it, "
                "or passing an HTML string or bytes."
            )
        tree = htmlstring_or_tree
    processors = []
    if "microdata" in syntaxes:
        processors.append(
            (
                "microdata",
                MicrodataExtractor(add_html_node=return_html_node).extract_items,
                tree,
            )
        )
    if "json-ld" in syntaxes:
        processors.append(
            (
                "json-ld",
                JsonLdExtractor().extract_items,
                tree,
            )
        )
    if "opengraph" in syntaxes:
        processors.append(("opengraph", OpenGraphExtractor().extract_items, tree))
    if "microformat" in syntaxes:
        processors.append(
            ("microformat", MicroformatExtractor().extract_items, htmlstring_or_tree)
        )
    if "rdfa" in syntaxes:
        processors.append(
            (
                "rdfa",
                RDFaExtractor().extract_items,
                tree,
            )
        )
    if "dublincore" in syntaxes:
        processors.append(
            (
                "dublincore",
                DublinCoreExtractor().extract_items,
                tree,
            )
        )
    output: dict[str, list[dict[str, Any]]] = {}
    for syntax, extract, document in processors:
        try:
            output[syntax] = list(extract(document, base_url=base_url))
        except Exception as e:
            if errors == "log":
                logger.exception("Failed to extract {}, raises {}".format(syntax, e))
            if errors == "ignore":
                pass
            if errors == "strict":
                raise
    if uniform:
        uniform_processors: list[
            tuple[str, Callable[..., Any], list[Any], str | None]
        ] = []
        if "microdata" in syntaxes:
            uniform_processors.append(
                (
                    "microdata",
                    _umicrodata_microformat,
                    output["microdata"],
                    schema_context,
                )
            )
        if "microformat" in syntaxes:
            uniform_processors.append(
                (
                    "microformat",
                    _umicrodata_microformat,
                    output["microformat"],
                    "http://microformats.org/wiki/",
                )
            )
        if "opengraph" in syntaxes:
            uniform_processors.append(
                (
                    "opengraph",
                    _uopengraph,
                    output["opengraph"],
                    None,
                )
            )
        if "dublincore" in syntaxes:
            uniform_processors.append(
                (
                    "dublincore",
                    _udublincore,
                    output["dublincore"],
                    None,
                )
            )

        for syntax, uniform_fn, raw, schema_ctx in uniform_processors:
            try:
                if syntax == "opengraph":
                    output[syntax] = uniform_fn(raw, with_og_array=with_og_array)
                elif syntax == "dublincore":
                    output[syntax] = uniform_fn(raw)
                else:
                    output[syntax] = uniform_fn(raw, schema_ctx)
            except Exception as e:
                if errors == "ignore":
                    output[syntax] = []
                if errors == "log":
                    output[syntax] = []
                    logger.exception(
                        "Failed to uniform extracted for {}, raises {}".format(
                            syntax, e
                        )
                    )
                if errors == "strict":
                    raise

    return output

```

### `extruct/dublincore.py`

```py
# mypy: disallow_untyped_defs=False
import re

from w3lib.html import strip_html5_whitespace

from extruct.utils import parse_html

_DC_ELEMENTS = (
    {  # Defined according DCMES(DCM Version 1.1): http://dublincore.org/documents/dces/
        "contributor": "http://purl.org/dc/elements/1.1/contributor",
        "coverage": "http://purl.org/dc/elements/1.1/coverage",
        "creator": "http://purl.org/dc/elements/1.1/creator",
        "date": "http://purl.org/dc/elements/1.1/date",
        "description": "http://purl.org/dc/elements/1.1/description",
        "format": "http://purl.org/dc/elements/1.1/format",
        "identifier": "http://purl.org/dc/elements/1.1/identifier",
        "language": "http://purl.org/dc/elements/1.1/language",
        "publisher": "http://purl.org/dc/elements/1.1/publisher",
        "relation": "http://purl.org/dc/elements/1.1/relation",
        "rights": "http://purl.org/dc/elements/1.1/rights",
        "source": "http://purl.org/dc/elements/1.1/source",
        "subject": "http://purl.org/dc/elements/1.1/subject",
        "title": "http://purl.org/dc/elements/1.1/title",
        "type": "http://purl.org/dc/elements/1.1/type",
    }
)

_DC_TERMS = {  # Defined according: http://dublincore.org/documents/2008/01/14/dcmi-terms/
    "abstract": "http://purl.org/dc/terms/abstract",
    "description": "http://purl.org/dc/terms/description",
    "accessrights": "http://purl.org/dc/terms/accessRights",
    "rights": "http://purl.org/dc/terms/rights",
    "rightsstatement": "http://purl.org/dc/terms/RightsStatement",
    "accrualmethod": "http://purl.org/dc/terms/accrualMethod",
    "collection": "http://purl.org/dc/terms/Collection",
    "methodOfaccrual": "http://purl.org/dc/terms/MethodOfAccrual",
    "accrualperiodicity": "http://purl.org/dc/terms/accrualPeriodicity",
    "frequency": "http://purl.org/dc/terms/Frequency",
    "accrualpolicy": "http://purl.org/dc/terms/accrualPolicy",
    "policy": "http://purl.org/dc/terms/Policy",
    "alternative": "http://purl.org/dc/terms/alternative",
    "title": "http://purl.org/dc/terms/title",
    "audience": "http://purl.org/dc/terms/audience",
    "agentclass": "http://purl.org/dc/terms/AgentClass",
    "available": "http://purl.org/dc/terms/available",
    "date": "http://purl.org/dc/terms/date",
    "bibliographiccitation": "http://purl.org/dc/terms/bibliographicCitation",
    "identifier": "http://purl.org/dc/terms/identifier",
    "bibliographicresource": "http://purl.org/dc/terms/BibliographicResource",
    "conformsto": "http://purl.org/dc/terms/conformsTo",
    "relation": "http://purl.org/dc/terms/relation",
    "standard": "http://purl.org/dc/terms/Standard",
    "contributor": "http://purl.org/dc/terms/contributor",
    "agent": "http://purl.org/dc/terms/Agent",
    "coverage": "http://purl.org/dc/terms/coverage",
    "locationperiodorjurisdiction": "http://purl.org/dc/terms/LocationPeriodOrJurisdiction",
    "created": "http://purl.org/dc/terms/created",
    "creator": "http://purl.org/dc/terms/creator",
    "dateaccepted": "http://purl.org/dc/terms/dateAccepted",
    "datecopyrighted": "http://purl.org/dc/terms/dateCopyrighted",
    "datesubmitted": "http://purl.org/dc/terms/dateSubmitted",
    "educationlevel": "http://purl.org/dc/terms/educationLevel",
    "extent": "http://purl.org/dc/terms/extent",
    "format": "http://purl.org/dc/terms/format",
    "sizeorduration": "http://purl.org/dc/terms/SizeOrDuration",
    "mediatypeorextent": "http://purl.org/dc/terms/MediaTypeOrExtent",
    "hasformat": "http://purl.org/dc/terms/hasFormat",
    "haspart": "http://purl.org/dc/terms/hasPart",
    "hasversion": "http://purl.org/dc/terms/hasVersion",
    "instructionalmethod": "http://purl.org/dc/terms/instructionalMethod",
    "methodofinstruction": "http://purl.org/dc/terms/MethodOfInstruction",
    "isformatof": "http://purl.org/dc/terms/isFormatOf",
    "ispartof": "http://purl.org/dc/terms/isPartOf",
    "isreferencedby": "http://purl.org/dc/terms/isReferencedBy",
    "isreplacedby": "http://purl.org/dc/terms/isReplacedBy",
    "isrequiredby": "http://purl.org/dc/terms/isRequiredBy",
    "issued": "http://purl.org/dc/terms/issued",
    "isversionof": "http://purl.org/dc/terms/isVersionOf",
    "language": "http://purl.org/dc/terms/language",
    "linguisticsystem": "http://purl.org/dc/terms/LinguisticSystem",
    "license": "http://purl.org/dc/terms/license",
    "licensedocument": "http://purl.org/dc/terms/LicenseDocument",
    "mediator": "http://purl.org/dc/terms/mediator",
    "medium": "http://purl.org/dc/terms/medium",
    "physicalresource": "http://purl.org/dc/terms/PhysicalResource",
    "physicalmedium": "http://purl.org/dc/terms/PhysicalMedium",
    "modified": "http://purl.org/dc/terms/modified",
    "provenance": "http://purl.org/dc/terms/provenance",
    "provenancestatement": "http://purl.org/dc/terms/ProvenanceStatement",
    "publisher": "http://purl.org/dc/terms/publisher",
    "references": "http://purl.org/dc/terms/references",
    "replaces": "http://purl.org/dc/terms/replaces",
    "requires": "http://purl.org/dc/terms/requires",
    "rightsholder": "http://purl.org/dc/terms/rightsHolder",
    "source": "http://purl.org/dc/terms/source",
    "spatial": "http://purl.org/dc/terms/spatial",
    "location": "http://purl.org/dc/terms/Location",
    "subject": "http://purl.org/dc/terms/subject",
    "tableofcontents": "http://purl.org/dc/terms/tableOfContents",
    "temporal": "http://purl.org/dc/terms/temporal",
    "periodoftime": "http://purl.org/dc/terms/PeriodOfTime",
    "type": "http://purl.org/dc/terms/type",
    "valid": "http://purl.org/dc/terms/valid",
}

_URL_NAMESPACES = ["http://purl.org/dc/terms/", "http://purl.org/dc/elements/1.1/"]


def get_lower_attrib(name):
    # get attribute to compare against _DC_TERMS or _DC_ELEMENTS
    return re.sub(r".*\.", "", name).lower()


class DublinCoreExtractor:
    """DublinCore extractor following extruct API."""

    def extract(self, htmlstring, base_url=None, encoding="UTF-8"):
        tree = parse_html(htmlstring, encoding=encoding)
        return list(self.extract_items(tree, base_url=base_url))

    def extract_items(self, document, base_url=None):
        elements = []
        terms = []

        def attrib_to_dict(attribs):
            # convert _attrib type to dict
            return dict(attribs.items())

        def populate_results(node, main_attrib):
            # fill list with DC Elements or DC Terms
            node_attrib = node.attrib
            if main_attrib not in node_attrib:
                return

            name = node.attrib[main_attrib]
            lower_name = get_lower_attrib(name)
            if lower_name in _DC_ELEMENTS:
                node.attrib.update({"URI": _DC_ELEMENTS[lower_name]})
                elements.append(attrib_to_dict(node.attrib))

            elif lower_name in _DC_TERMS:
                node.attrib.update({"URI": _DC_TERMS[lower_name]})
                terms.append(attrib_to_dict(node.attrib))

        namespaces_nodes = document.xpath('//link[contains(@rel,"schema")]')
        namespaces = {}
        for i in namespaces_nodes:
            url = strip_html5_whitespace(i.attrib["href"])
            if url in _URL_NAMESPACES:
                namespaces.update({re.sub(r"schema\.", "", i.attrib["rel"]): url})

        list_meta_node = document.xpath("//meta")
        for meta_node in list_meta_node:
            populate_results(meta_node, "name")

        list_link_node = document.xpath("//link")
        for link_node in list_link_node:
            populate_results(link_node, "rel")

        yield {"namespaces": namespaces, "elements": elements, "terms": terms}

```

### `extruct/jsonld.py`

```py
# mypy: disallow_untyped_defs=False
"""
JSON-LD extractor
"""

import json
import re

import jstyleson
import lxml.etree

from extruct.utils import parse_html

HTML_OR_JS_COMMENTLINE = re.compile(r"^\s*(//.*|<!--.*-->)")


class JsonLdExtractor:
    _xp_jsonld = lxml.etree.XPath(
        'descendant-or-self::script[@type="application/ld+json"]'
    )

    def extract(self, htmlstring, base_url=None, encoding="UTF-8"):
        tree = parse_html(htmlstring, encoding=encoding)
        return self.extract_items(tree, base_url=base_url)

    def extract_items(self, document, base_url=None):
        return [
            item
            for items in map(self._extract_items, self._xp_jsonld(document))  # type: ignore[arg-type]
            if items
            for item in items
            if item
        ]

    def _extract_items(self, node):
        script = node.xpath("string()").strip()
        if not script:
            return
        try:
            # TODO: `strict=False` can be configurable if needed
            data = json.loads(script, strict=False)
        except ValueError:
            # sometimes JSON-decoding errors are due to leading HTML or JavaScript comments
            data = jstyleson.loads(HTML_OR_JS_COMMENTLINE.sub("", script), strict=False)
        if isinstance(data, list):
            yield from data
        elif isinstance(data, dict):
            yield data

```

### `extruct/microformat.py`

```py
# mypy: disallow_untyped_defs=False
import mf2py


class MicroformatExtractor:
    def extract(self, htmlstring, base_url=None, encoding="UTF-8"):
        return list(self.extract_items(htmlstring, base_url=base_url))

    def extract_items(self, html, base_url=None):
        yield from mf2py.parse(html, html_parser="lxml", url=base_url)["items"]

```

### `extruct/opengraph.py`

```py
# mypy: disallow_untyped_defs=False
import re

from extruct.utils import parse_html

_PREFIX_PATTERN = re.compile(r"\s*(\w+):\s*([^\s]+)")
_OG_NAMESPACES = {
    "og": "http://ogp.me/ns#",
    "music": "http://ogp.me/ns/music#",
    "video": "http://ogp.me/ns/video#",
    "article": "http://ogp.me/ns/article#",
    "book": "http://ogp.me/ns/book#",
    "profile": "http://ogp.me/ns/profile#",
    # non-standard but seen in the wild
    "product": "http://ogp.me/ns/product#",  # ~10% of product pages with OG
}


class OpenGraphExtractor:
    """OpenGraph extractor following extruct API."""

    def extract(self, htmlstring, base_url=None, encoding="UTF-8"):
        tree = parse_html(htmlstring, encoding=encoding)
        return list(self.extract_items(tree, base_url=base_url))

    def extract_items(self, document, base_url=None):
        # OpenGraph defines a web page as a single rich object.
        for head in document.xpath("//head"):
            html_elems = document.head.xpath("parent::html")
            namespaces = self.get_namespaces(html_elems[0]) if html_elems else {}
            namespaces.update(self.get_namespaces(head))
            props = []
            for el in head.xpath("meta[@property and @content]"):
                prop = el.attrib["property"]
                val = el.attrib["content"]
                ns = prop.partition(":")[0]
                if ns in _OG_NAMESPACES:
                    namespaces[ns] = _OG_NAMESPACES[ns]
                if ns in namespaces:
                    props.append((prop, val))
            if props:
                yield {"namespace": namespaces, "properties": props}

    def get_namespaces(self, element):
        return dict(_PREFIX_PATTERN.findall(element.attrib.get("prefix", "")))

```

### `extruct/rdfa.py`

```py
# mypy: disallow_untyped_defs=False
"""
RDFa extractor

Based on pyrdfa3 and rdflib
"""
import json
import logging
import re
from collections import defaultdict

rdflib_logger = logging.getLogger("rdflib")
rdflib_logger.setLevel(logging.ERROR)

from pyRdfa import Options
from pyRdfa import pyRdfa as PyRdfa
from pyRdfa.initialcontext import initial_context
from rdflib import Graph
from rdflib import logger as rdflib_logger  # type: ignore[no-redef]

from extruct.utils import parse_xmldom_html

# silence rdflib INFO logs
rdflib_logger.setLevel(logging.ERROR)

initial_context["http://www.w3.org/2011/rdfa-context/rdfa-1.1"].ns.update(
    {
        "twitter": "https://dev.twitter.com/cards#",
        "fb": "http://ogp.me/ns/fb#",
        "og": "http://ogp.me/ns#",
        "music": "http://ogp.me/ns/music#",
        "video": "http://ogp.me/ns/video#",
        "article": "http://ogp.me/ns/article#",
        "book": "http://ogp.me/ns/book#",
        "profile": "http://ogp.me/ns/profile#",
    }
)


class RDFaExtractor:
    def _replaceNS(self, prop, html_element, head_element):
        """Expand namespace to match with returned json (e.g.: og -> 'http://ogp.me/ns#')"""

        # context namespaces taken from pyrdfa3
        # https://github.com/RDFLib/PyRDFa/blob/master/pyRdfa/initialcontext.py
        context = {
            "owl": "http://www.w3.org/2002/07/owl#",
            "gr": "http://purl.org/goodrelations/v1#",
            "ctag": "http://commontag.org/ns#",
            "cc": "http://creativecommons.org/ns#",
            "grddl": "http://www.w3.org/2003/g/data-view#",
            "rif": "http://www.w3.org/2007/rif#",
            "sioc": "http://rdfs.org/sioc/ns#",
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "xml": "http://www.w3.org/XML/1998/namespace",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "rev": "http://purl.org/stuff/rev#",
            "rdfa": "http://www.w3.org/ns/rdfa#",
            "dc": "http://purl.org/dc/terms/",
            "foaf": "http://xmlns.com/foaf/0.1/",
            "void": "http://rdfs.org/ns/void#",
            "ical": "http://www.w3.org/2002/12/cal/icaltzd#",
            "vcard": "http://www.w3.org/2006/vcard/ns#",
            "wdrs": "http://www.w3.org/2007/05/powder-s#",
            "og": "http://ogp.me/ns#",
            "wdr": "http://www.w3.org/2007/05/powder#",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "xhv": "http://www.w3.org/1999/xhtml/vocab#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "v": "http://rdf.data-vocabulary.org/#",
            "skosxl": "http://www.w3.org/2008/05/skos-xl#",
            "schema": "http://schema.org/",
        }

        # if bad property
        if ":" not in prop:
            return prop

        # if property has no prefix
        if "http://" in prop:
            return prop

        prefix = prop.split(":")[0]

        match = None
        if head_element.get("prefix"):
            match = re.search(prefix + r": [^\s]+", head_element.get("prefix"))

        # if namespace taken from prefix attribute in head tag
        if match:
            ns = match.group().split(": ")[1]
            return ns + prop.split(":")[1]

        # if namespace taken from xmlns attribute in html tag
        if ("xmlns:" + prefix) in html_element.keys():
            return html_element.get("xmlns:" + prefix) + prop.split(":")[1]

        # if namespace present in initial context
        if prefix in context:
            return context[prefix] + prop.split(":")[1]

        return prop

    def _sort(self, unordered, ordered):
        """Sort the rdfa tags in jsonld string"""
        idx_for_value = dict(
            reversed([(value, idx) for idx, value in enumerate(ordered)])
        )
        unordered.sort(
            key=lambda props: idx_for_value.get(props.get("@value"), len(ordered))
        )

    def _fix_order(self, jsonld_string, document):
        """
        Fix order of rdfa tags in jsonld string
        by checking the appearance order in the HTML
        """
        json_objects = json.loads(jsonld_string)

        html, head = document.xpath("/html"), document.xpath("//head")
        if not html or not head:
            return json_objects
        html_element, head_element = html[0], head[0]

        # Stores the values or each property in appearance order
        values_for_property = defaultdict(list)

        for meta_tag in head_element.xpath("meta[@property]"):
            expanded_property = self._replaceNS(
                meta_tag.attrib["property"], html_element, head_element
            )
            values_for_property[expanded_property].append(meta_tag.get("content"))

        for json_object in json_objects:
            keys = json_object.keys()

            for key in keys:
                if type(json_object[key]) is list and len(json_object[key]) > 1:
                    self._sort(json_object[key], values_for_property[key])

        return json_objects

    def extract(self, htmlstring, base_url=None, encoding="UTF-8", expanded=True):
        tree = parse_xmldom_html(htmlstring, encoding=encoding)
        return self.extract_items(tree, base_url=base_url, expanded=expanded)

    def extract_items(self, document, base_url=None, expanded=True):
        options = Options(
            output_processor_graph=True,
            embedded_rdf=False,
            space_preserve=True,
            vocab_expansion=False,
            vocab_cache=False,
            vocab_cache_report=False,
            refresh_vocab_cache=False,
            check_lite=False,
        )
        g = PyRdfa(options, base=base_url).graph_from_DOM(
            document, graph=Graph(), pgraph=Graph()
        )
        jsonld_string = g.serialize(format="json-ld", auto_compact=not expanded)

        # rdflib may return either bytes or strings
        if isinstance(jsonld_string, bytes):
            jsonld_string = jsonld_string.decode("utf-8")

        try:
            # hack to fix the ordering of multi-value properties (see issue 116)
            # it should be disabled once PyRDFA fixes itself
            return self._fix_order(jsonld_string, document)
        except:
            return json.loads(jsonld_string)

```

### `extruct/tool.py`

```py
from __future__ import annotations

import argparse
import json
from typing import Any

import requests

import extruct
from extruct import SYNTAXES


def metadata_from_url(
    url: str,
    syntaxes: list[str] = SYNTAXES,
    uniform: bool = False,
    schema_context: str = "http://schema.org",
    errors: str = "strict",
) -> dict[str, Any]:
    resp = requests.get(url, timeout=30)
    result: dict[str, Any] = {
        "url": url,
        "status": "{} {}".format(resp.status_code, resp.reason),
    }
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        return result
    result.update(
        extruct.extract(
            resp.content,
            base_url=url,  # FIXME: use base url
            syntaxes=syntaxes,
            uniform=uniform,
            schema_context=schema_context,
            errors=errors,
        )
    )
    return result


def main(args: Any | None = None) -> Any:
    parser = argparse.ArgumentParser(prog="extruct", description=__doc__)
    arg = parser.add_argument
    arg("url", help="The target URL")
    arg(
        "--syntaxes",
        nargs="+",
        choices=SYNTAXES,
        default=SYNTAXES,
        help="List of syntaxes to extract. Valid values any or all (default):"
        "microdata, opengraph, microformat json-ld, rdfa."
        "Example: --syntaxes microdata opengraph json-ld",
    )
    arg(
        "--uniform",
        default=False,
        help="""If True uniform output format of all syntaxes to a list of dicts.
                Returned dicts structure:
                {'@context': 'http://example.com',
                 '@type': 'example_type',
                 /* All other the properties in keys here */
                 }""",
    )
    arg(
        "--schema_context",
        default="http://schema.org",
        help="schema's context for current page",
    )
    arg(
        "--errors",
        default="log",
        choices=["strict", "log", "ignore"],
        help="errors: set to 'log'(default) to log the exceptions, 'ignore' to ignore"
        " them or 'strict' to raise them",
    )
    args = parser.parse_args(args)
    metadata = metadata_from_url(
        args.url, args.syntaxes, args.uniform, args.schema_context, args.errors
    )
    return json.dumps(metadata, indent=2, sort_keys=True)

```

### `extruct/uniform.py`

```py
# mypy: disallow_untyped_defs=False
import copy
from typing import Any
from urllib.parse import urljoin, urlparse

from extruct.dublincore import get_lower_attrib


def _uopengraph(extracted, with_og_array=False):
    out = []
    for obj in extracted:
        # In order of appearance in the page
        properties = list(obj["properties"])
        flattened: dict[Any, Any] = {}

        for k, v in properties:
            if k not in flattened.keys():
                flattened[k] = v
            elif v and v.strip():
                # If og_array isn't required add first non empty value
                if not with_og_array:
                    if not flattened[k] or not flattened[k].strip():
                        flattened[k] = v
                else:
                    if isinstance(flattened[k], list):
                        flattened[k].append(v)
                    elif flattened[k] and flattened[k].strip():
                        flattened[k] = [flattened[k], v]
                    else:
                        flattened[k] = v

        t = flattened.pop("og:type", None)
        if t:
            flattened["@type"] = t
        flattened["@context"] = obj["namespace"]
        out.append(flattened)
    return out


def _umicrodata_microformat(extracted, schema_context):
    res = []
    if isinstance(extracted, list):
        for obj in extracted:
            res.append(flatten_dict(obj, schema_context, True))
    elif isinstance(extracted, dict):
        res.append(flatten_dict(extracted, schema_context, False))
    return res


def _udublincore(extracted):
    out = []
    extracted_cpy = copy.deepcopy(extracted)
    for obj in extracted_cpy:
        context = obj.pop("namespaces", None)
        obj["@context"] = context
        elements = obj["elements"]
        for element in elements:
            for key, value in element.items():
                if get_lower_attrib(value) == "type":
                    obj["@type"] = element["content"]
                    obj["elements"].remove(element)
                    break
        out.append(obj)
    return out


def _flatten(element, schema_context):
    if isinstance(element, dict):
        element = flatten_dict(element, schema_context, False)
    elif isinstance(element, list):
        element = [
            flatten_dict(o, schema_context, False) if isinstance(o, dict) else o
            for o in element
        ]
    return element


def flatten_dict(d, schema_context, add_context):
    out = dict(d)
    typ = out.pop("type", None)
    if not typ:
        return d

    if isinstance(typ, list):
        out["@type"] = typ
        context = schema_context
    else:
        context, typ = infer_context(typ, schema_context)
        out["@type"] = typ

    if add_context:
        out["@context"] = context

    props = out.pop("properties", {})
    for field, value in props.items():
        value = _flatten(value, schema_context)
        out[field] = value

    children = out.pop("children", [])
    if children:
        out["children"] = []
    for child in children:
        child = _flatten(child, schema_context)
        out["children"].append(child)
    return out


def infer_context(typ, context="http://schema.org"):
    parsed_context = urlparse(typ)
    if parsed_context.netloc:
        base = "".join([parsed_context.scheme, "://", parsed_context.netloc])
        if parsed_context.path and parsed_context.fragment:
            context = urljoin(base, parsed_context.path)
            typ = parsed_context.fragment.strip("/")
        elif parsed_context.path:
            context = base
            typ = parsed_context.path.strip("/")
    return context, typ

```

### `extruct/utils.py`

```py
# mypy: disallow_untyped_defs=False
import lxml.html

from extruct.xmldom import XmlDomHTMLParser


def parse_html(html, encoding):
    """Parse HTML using lxml.html.HTMLParser, return a tree"""
    parser = lxml.html.HTMLParser(encoding=encoding)
    return lxml.html.fromstring(html, parser=parser)


def parse_xmldom_html(html, encoding):
    """Parse HTML using XmlDomHTMLParser, return a tree"""
    parser = XmlDomHTMLParser(encoding=encoding)
    return lxml.html.fromstring(html, parser=parser)

```

### `extruct/VERSION`

```
0.18.0

```

### `extruct/w3cmicrodata.py`

```py
# mypy: disallow_untyped_defs=False
"""
HTML Microdata parser

Piece of code extracted form:
* http://blog.scrapinghub.com/2014/06/18/extracting-schema-org-microdata-using-scrapy-selectors-and-xpath/

Ported to lxml
follows http://www.w3.org/TR/microdata/#json

"""

from __future__ import annotations

import collections
from functools import partial
from typing import Any, Set
from urllib.parse import urljoin

import html_text
import lxml.etree
from lxml.html.clean import Cleaner
from w3lib.html import strip_html5_whitespace

from extruct.utils import parse_html

# Cleaner which is similar to html_text cleaner, but is less aggressive
cleaner = Cleaner(
    scripts=True,
    javascript=False,  # onclick attributes are fine
    comments=True,
    style=True,
    links=True,
    meta=True,
    page_structure=False,  # <title> may be nice to have
    processing_instructions=True,
    embedded=False,  # keep embedded content
    frames=False,  # keep frames
    forms=False,  # keep forms
    annoying_tags=False,
    remove_unknown_tags=False,
    safe_attrs_only=False,
)


class LxmlMicrodataExtractor:
    # iterate in document order (used below for fast get_docid)
    _xp_item = lxml.etree.XPath("descendant-or-self::*[@itemscope]")
    _xp_prop = lxml.etree.XPath(
        """set:difference(
            .//*[@itemprop],
            .//*[@itemscope]//*[@itemprop])""",
        namespaces={"set": "http://exslt.org/sets"},
    )
    _xp_clean_text = lxml.etree.XPath(
        "descendant-or-self::*[not(self::script or self::style)]/text()"
    )

    def __init__(
        self, nested=True, strict=False, add_text_content=False, add_html_node=False
    ):
        self.nested = nested
        self.strict = strict
        self.add_text_content = add_text_content
        self.add_html_node = add_html_node

    def extract(self, htmlstring, base_url=None, encoding="UTF-8"):
        tree = parse_html(htmlstring, encoding=encoding)
        return self.extract_items(tree, base_url)

    def extract_items(self, document, base_url):
        itemids = self._build_itemids(document)
        items_seen: set[Any] = set()
        return [
            item
            for item in (
                self._extract_item(
                    it, items_seen=items_seen, base_url=base_url, itemids=itemids
                )
                for it in self._xp_item(document)  # type: ignore[union-attr]
            )
            if item
        ]

    def get_docid(self, node, itemids):
        return itemids[node]

    def _build_itemids(self, document):
        """Build itemids for a fast get_docid implementation. Use document order."""
        root = document.getroottree().getroot()
        return {node: idx + 1 for idx, node in enumerate(self._xp_item(root))}  # type: ignore[arg-type]

    def _extract_item(self, node, items_seen, base_url, itemids):
        itemid = self.get_docid(node, itemids)

        if self.nested:
            if itemid in items_seen:
                return
            items_seen.add(itemid)

        item = {}
        if not self.nested:
            item["iid"] = itemid
        types = node.get("itemtype", "").split()
        if types:
            if not self.strict and len(types) == 1:
                item["type"] = types[0]
            else:
                item["type"] = types

            nodeid = node.get("itemid")
            if nodeid:
                item["id"] = nodeid.strip()

        properties = collections.defaultdict(list)
        for name, value in self._extract_properties(
            node, items_seen=items_seen, base_url=base_url, itemids=itemids
        ):
            properties[name].append(value)

        # process item references
        refs = node.get("itemref", "").split()
        if refs:
            for refid in refs:
                for name, value in self._extract_property_refs(
                    node,
                    refid,
                    items_seen=items_seen,
                    base_url=base_url,
                    itemids=itemids,
                ):
                    properties[name].append(value)

        props = []
        for name, values in properties.items():
            if not self.strict and len(values) == 1:
                props.append((name, values[0]))
            else:
                props.append((name, values))
        if props:
            item["properties"] = dict(props)
        else:
            # item without properties; let's use the node itself
            item["value"] = self._extract_property_value(
                node,
                force=True,
                items_seen=items_seen,
                base_url=base_url,
                itemids=itemids,
            )

        # below are not in the specs, but can be handy
        if self.add_text_content:
            textContent = self._extract_textContent(node)
            if textContent:
                item["textContent"] = textContent
        if self.add_html_node:
            item["htmlNode"] = node

        return item

    def _extract_properties(self, node, items_seen, base_url, itemids):
        for prop in self._xp_prop(node):  # type: ignore[union-attr]
            yield from self._extract_property(
                prop, items_seen=items_seen, base_url=base_url, itemids=itemids
            )

    def _extract_property_refs(self, node, refid, items_seen, base_url, itemids):
        ref_node = node.xpath("id($refid)[1]", refid=refid)
        if not ref_node:
            return
        ref_node = ref_node[0]
        extract_fn = partial(
            self._extract_property,
            items_seen=items_seen,
            base_url=base_url,
            itemids=itemids,
        )
        if "itemprop" in ref_node.keys() and "itemscope" in ref_node.keys():
            # An full item will be extracted from the node, no need to look
            # for individual properties in child nodes
            yield from extract_fn(ref_node)
        else:
            base_parent_scope = ref_node.xpath("ancestor-or-self::*[@itemscope][1]")
            for prop in ref_node.xpath("descendant-or-self::*[@itemprop]"):
                parent_scope = prop.xpath("ancestor::*[@itemscope][1]")
                # Skip properties defined in a different scope than the ref_node
                if parent_scope == base_parent_scope:
                    yield from extract_fn(prop)

    def _extract_property(self, node, items_seen, base_url, itemids):
        props = node.get("itemprop").split()
        value = self._extract_property_value(
            node, items_seen=items_seen, base_url=base_url, itemids=itemids
        )
        return [(p, value) for p in props]

    def _extract_property_value(self, node, items_seen, base_url, itemids, force=False):
        # http://www.w3.org/TR/microdata/#values
        if not force and node.get("itemscope") is not None:
            if self.nested:
                return self._extract_item(
                    node, items_seen=items_seen, base_url=base_url, itemids=itemids
                )
            else:
                return {"iid_ref": self.get_docid(node, itemids)}

        elif node.tag == "meta":
            return node.get("content", "")

        elif node.tag in (
            "audio",
            "embed",
            "iframe",
            "img",
            "source",
            "track",
            "video",
        ):
            return urljoin(base_url, strip_html5_whitespace(node.get("src", "")))

        elif node.tag in ("a", "area", "link"):
            return urljoin(base_url, strip_html5_whitespace(node.get("href", "")))

        elif node.tag in ("object",):
            return urljoin(base_url, strip_html5_whitespace(node.get("data", "")))

        elif node.tag in ("data", "meter"):
            return node.get("value", "")

        elif node.tag in ("time",):
            return node.get("datetime", "")

        # not in W3C specs but used in schema.org examples
        elif node.get("content"):
            return node.get("content")

        # https://schema.org/docs/actions.html#part-4
        elif (itemprop := node.get("itemprop")) and (
            itemprop.endswith("-input") or itemprop.endswith("-output")
        ):
            result = {}
            if "required" in node.attrib:
                result["valueRequired"] = True
            if name := node.get("name"):
                result["valueName"] = name
            return result

        else:
            return self._extract_textContent(node)

    def _extract_textContent(self, node):
        clean_node = cleaner.clean_html(node)
        return html_text.etree_to_text(clean_node)


MicrodataExtractor = LxmlMicrodataExtractor

```

### `extruct/xmldom.py`

```py
# mypy: disallow_untyped_defs=False
from __future__ import annotations

from copy import copy, deepcopy
from xml.dom import Node
from xml.dom.minidom import Attr, NamedNodeMap

from lxml.etree import ElementBase, XPath, _ElementUnicodeResult, tostring
from lxml.html import HtmlElementClassLookup, HTMLParser

try:
    from lxml.etree import _ElementStringResult
except ImportError:

    class _ElementStringResult(bytes):  # type: ignore[no-redef]
        """
        _ElementStringResult is removed in lxml >= 5.1.1,
        so we define it here for compatibility.
        """

        def getparent(self):
            return self._parent  # type: ignore[attr-defined]


class DomElementUnicodeResult:
    CDATA_SECTION_NODE = Node.CDATA_SECTION_NODE
    ELEMENT_NODE = Node.ELEMENT_NODE
    TEXT_NODE = Node.TEXT_NODE

    def __init__(self, text):
        self.text = text
        self.nodeType = Node.TEXT_NODE

    @property
    def data(self):
        if isinstance(self.text, _ElementUnicodeResult):
            return self.text
        else:
            raise RuntimeError


class DomTextNode:
    CDATA_SECTION_NODE = Node.CDATA_SECTION_NODE
    ELEMENT_NODE = Node.ELEMENT_NODE
    TEXT_NODE = Node.TEXT_NODE

    def __init__(self, text):
        self.data = text
        self.nodeType = Node.TEXT_NODE


def lxmlDomNodeType(node):
    if isinstance(node, ElementBase):
        return Node.ELEMENT_NODE

    elif isinstance(node, (_ElementStringResult, _ElementUnicodeResult)):
        if node.is_attribute:
            return Node.ATTRIBUTE_NODE
        else:
            return Node.TEXT_NODE
    else:
        return Node.NOTATION_NODE


class DomHtmlMixin:
    CDATA_SECTION_NODE = Node.CDATA_SECTION_NODE
    ELEMENT_NODE = Node.ELEMENT_NODE
    TEXT_NODE = Node.TEXT_NODE

    _xp_childrennodes = XPath("child::node()")

    @property
    def documentElement(self):
        return self.getroottree().getroot()  # type: ignore[attr-defined]

    @property
    def nodeType(self):
        return Node.ELEMENT_NODE

    @property
    def nodeName(self):
        # FIXME: this is a simplification
        return self.tag  # type: ignore[attr-defined]

    @property
    def tagName(self):
        return self.tag  # type: ignore[attr-defined]

    @property
    def localName(self):
        return self.xpath("local-name(.)")  # type: ignore[attr-defined]

    def hasAttribute(self, name):
        return name in self.attrib  # type: ignore[attr-defined]

    def getAttribute(self, name):
        return self.get(name)  # type: ignore[attr-defined]

    def setAttribute(self, name, value):
        self.set(name, value)  # type: ignore[attr-defined]

    def cloneNode(self, deep):
        return deepcopy(self) if deep else copy(self)

    @property
    def attributes(self):
        attrs = {}
        for name, value in self.attrib.items():  # type: ignore[attr-defined]
            a = Attr(name)
            a.value = value
            attrs[name] = a
        return NamedNodeMap(attrs, {}, self)

    @property
    def parentNode(self):
        return self.getparent()  # type: ignore[attr-defined]

    @property
    def childNodes_xpath(self):
        for n in self._xp_childrennodes(self):  # type: ignore[union-attr,arg-type]

            if isinstance(n, ElementBase):
                yield n

            elif isinstance(n, (_ElementStringResult, _ElementUnicodeResult)):

                if isinstance(n, _ElementUnicodeResult):
                    n = DomElementUnicodeResult(n)
                else:
                    n.nodeType = Node.TEXT_NODE  # type: ignore[attr-defined]
                    n.data = n  # type: ignore[attr-defined]
                yield n

    @property
    def childNodes(self):
        if self.text:  # type: ignore[attr-defined]
            yield DomTextNode(self.text)  # type: ignore[attr-defined]
        for n in self.iterchildren():  # type: ignore[attr-defined]
            yield n
            if n.tail:
                yield DomTextNode(n.tail)

    def getElementsByTagName(self, name):
        return self.iterdescendants(name)  # type: ignore[attr-defined]

    def getElementById(self, i):
        return self.get_element_by_id(i)  # type: ignore[attr-defined]

    @property
    def data(self):
        if isinstance(self, (_ElementStringResult, _ElementUnicodeResult)):
            return self
        else:
            raise RuntimeError

    def toxml(self, encoding=None):
        return tostring(self, encoding=encoding if encoding is not None else "unicode")  # type: ignore[call-overload]


class DomHtmlElementClassLookup(HtmlElementClassLookup):
    def __init__(self):
        super().__init__()
        self._lookups = {}

    def lookup(self, node_type, document, namespace, name):
        k = (node_type, document, namespace, name)
        t = self._lookups.get(k)
        if t is None:
            cur = super().lookup(node_type, document, namespace, name)
            newtype = type("Dom" + cur.__name__, (cur, DomHtmlMixin), {})
            self._lookups[k] = newtype
            return newtype
        else:
            return t


class XmlDomHTMLParser(HTMLParser):
    """An HTML parser that is configured to return XmlDomHtmlElement
    objects, compatible with xml.dom API
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        parser_lookup = DomHtmlElementClassLookup()
        self.set_element_class_lookup(parser_lookup)

```

### `HISTORY.rst`

```rst
=======
History
=======

v0.18.0 (2024-11-08)
--------------------

* Addded support for the ``valueRequired`` and ``valueName`` fields of `action
  I/O <https://schema.org/docs/actions.html#part-4>`_ to the microdata parser.

v0.17.0 (2024-05-29)
--------------------

* Added support for Python 3.12 (PR #218)
* Added support for lxml >= 5.2.0 (PR #217, #234)
* Cleaned up and modernized the code (PR #214, #219, #220, #222, #223, #224,
  #225, #226, #227)
* Improved the pre-commit and CI configuration (PR #226, #233)

v0.16.0 (2023-07-07)
--------------------

* identical with v0.15

v0.15.0 (2023-07-07)
--------------------

* Allow extruct to receive a parsed tree, instead of
  an HTML string (PR #206)
* Added support for Python 3.10 and 3.11
* Removed support for Python 3.7 (PR #206)
* Code auto-formatted with black & isort

v0.14.0 (2022-10-25)
--------------------

* Removed support for Python 2.7 and 3.5 (PR #200)
* Removed rdflib-jsonld dependency (PR #188)
* Fixed typo in dublincore definitions (PR #190)
* Fixed linguist stats (which language is used) (PR #180)

v0.13.0 (2021-07-26)
--------------------

* Support for rdflib 6.0.0 (PR #177)
* Fix for when jsonld is null (PR #56)
* Documentation fixe (PR #173)

v0.12.0 (2020-12-28)
--------------------

* Support for rdflib 5.0.0 and up.
  When upgrading, we recommend switching to latest versions of
  rdflib, mf2py, rdflib-jsonld and pyrdfa3. (PR #161)
* Support for Python 3.8 and 3.9
* Show full README on PyPI (PR #162)
* README rendering fixed and tested (PR #170)
* Using github actions instead of Travis CI

v0.11.0 (2020-11-23)
--------------------

* support Dublin Core Metadata (DC-HTML-2003) (PR #101)
* support the non-standard ``product`` Open Graph namespace (PR #152)
* move release documentation to the wiki (PR #150)

v0.10.0 (2020-09-01)
--------------------

* support open graph arrays via ``with_og_array=True`` (PR #138)
* support "expanded" Open Graph metadata based on og:type (PR #140)
* parse JSON with JS comments for json-ld (PR #137)
* preserve order for duplicated properties for RDFa (PR #139)
* improve microdata parser performance with large number of items (PR #148)
* spelling fixes (PR #145)

v0.9.0 (2020-04-20)
-------------------

* REST API ``extruct.service`` removed
* ``rdflib`` dependency restrited to <5.0.0, as parsers used by extruct
  were removed in 5.0.0

v0.8.0 (2019-10-07)
-------------------
* Python 3.4 support is dropped;
* in case of duplicate OpenGraph definitions (e.g. multiple ``og:image``),
  empty results are de-prioritized now, to do the same as Facebook;
* text content of microdata attributes is now extracted using html-text
  library, which fixes badly extracted text in some cases
  (words glued together, etc.)

v0.7.3 (2019-06-10)
-------------------

* In case of duplicate OpenGraph definitions (e.g. multiple ``og:image``),
  extruct now keeps the first one, not the last one,
  to do the same as Facebook.

v0.7.2 (2019-02-14)
-------------------

* Cover all possible exception cases dealt by ``extruct()`` ``errors``
  attribute for values ``strict``, ``log`` and ``ignore``
* avoid including ``itemprop`` from child ``itemscope`` when using
  ``itemref`` for microdata
* proper processing order for ``itemref`` for microdata

v0.7.1 (2018-11-02)
-------------------

* json-ld parsing issue is fixed;
* deprecation warning for ``url`` argument points to caller code;
* better Python 3.7 support (fixed warnings, setup running 3.7 tests on CI).

v0.7.0 (2018-08-23)
-------------------

In this release OpenGraph parsing is improved:

* known OpenGraph namespaces (og, music, video,
  article, book, profile) work without an explicitly defined prefix;
* prefix is extracted both from ``<head>`` and ``<html>`` element attributes,
  not only from ``<head>``;
* prefix parsing is more permissive.

Other changes:

* pypi version badge is added to the README;
* html parsing code is cleaned up.

v0.6.0 (2018-08-09)
-------------------

* JSON-LD parsing is less strict now: control characters are allowed.

v0.5.0 (2018-06-08)
-------------------

* Add OpenGraph and Microformat extractors.
* Add argument ``syntaxes`` to ``extract`` and command line function, it allows to
  select which syntaxes to extract.
* Add argument ``uniform`` to ``extract`` and command line function, if True it maps
  the output of Microdata, OpenGraph, Microformat and Json-ld to the same template.
* Add argument ``errors``  to ``extract`` and command line function, it allows to
  define if errors should be raised, logged or ignored.
* Fix RDFa memory leak, now RDfaExtractor resets ``_lookups`` after each
  extraction.
* Fixed regex pattern in ``JsonLdExtractor`` to avoid removing comments from
  within valid JSON.
* In ``w3microdata`` strip whitespaces, newlines, etc from urls extracted from
  html nodes.
* ``base_url`` substitutes ``url`` in ``MicroformatExtractor``, ``JsonLdExtractor``,
  ``OpenGraphExtractor``, ``RDFaExtractor``  and ``MicrodataExtractor``
* individual extractors accept ``base_url`` instead of ``url``, unused keyword
  arguments are removed.
* In ``w3microdata.extract_items`` ``items_seen`` and ``url`` are no longer 
  class variables but are passed as arguments.
* In ``w3microdata`` the following functions are now private:
  ``extract_item``, ``extract_property_value``, ``extract_textContent``,
  ``_extract_property``, ``_extract_properties``, ``_extract_property_refs``
  and ``_extract_textContent``.
* In ``w3microdata`` ``_extract_properties``, ``_extract_property_refs``, 
  ``_extract_property``, ``_extract_property_value`` and ``_extract_item``
  now need ``items_seen`` and ``url`` to be passed as arguments.
* Add argument ``return_html_node`` to ``extract``, it allows to return HTML
  node with the result of metadata extraction. It is supported only by
  microdata syntax.

Warning: backward-incompatible change:

* ``base_url`` is used instead of ``url`` in ``extruct.extract``, ``url`` is 
  still supported by deprecated.
* In ``extruct.extract`` default ``base_url`` is now ``None`` to avoid wrong 
  results with ``urljoin``.




v0.4.0 (2017-06-20)
-------------------

* New ``extruct`` command line tool to fetch a page and extract its metadata.
  Works either via ``extruct`` directly or ``python -m extruct``.
* Accept leading HTML comment in JSON-LD payload.
* rdflib log messages were silenced to avoid the noise when importing extruct.


v0.3.1 (2017-06-07)
-------------------

* Fix dependencies and support RDFa by default (hence depend on rdflib by default).
* Update README with all-in-one extractor examples.

v0.3.0 (2017-06-07)
-------------------

* All extractors have an ``.extract_items()`` method, taking an lxml-parsed
  document as input, if you want to reuse one you already have.
* Add generic extraction: use ``extruct.extract()`` to call all extractors
  at once.

v0.3.0a2 (2017-02-01)
---------------------

Warning: backward-incompatible change:

* ``.extract()`` methods now return a list of Python dicts (the items)
  instead of a dict with an "items" key having this list as value.

v0.3.0a1 (2016-12-15)
---------------------

* Use rdflib's pyRdfa directly instead of pyRdfa3 code copy.


v0.3.0a0 (2016-12-02)
---------------------

* (Very) Experimental support for RDFa extraction using rdflib+lxml


v0.2.0 (2016-09-26)
-------------------

* Web service response content-type set to 'application/json'
* Web service Python 3 compatibility
* Code coverage reports
* Fix extraction of ``<object>`` "data" URL with microdata
* Handle textContent mixed with ``<script>`` and ``<style>`` tags
* Add JSON-LD extraction example to README
* Tests added for non-nested microdata output
* Tests added for text content option
* Tests added for "meter" and "data" attributes


v0.1.0 (2015-10-26)
-------------------

* First release on PyPI.

```

### `LICENSE`

```
Copyright (c) Scrapinghub
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. Neither the name of extruct nor the names of its contributors may be used
       to endorse or promote products derived from this software without
       specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```

### `pyproject.toml`

```toml
[tool.mypy]
show_column_numbers = true

disallow_untyped_defs=true
disallow_incomplete_defs=true
check_untyped_defs=true

warn_redundant_casts=true
warn_unused_ignores=true
warn_return_any=true

strict_equality=true

[[tool.mypy.overrides]]
module = [
    'mf2py.*',
    'pyRdfa.*',
    'rdflib.*',
    'jstyleson.*',
    'urlparse.*',
    'html_text.*',
]
ignore_missing_imports=true

```

### `pytest.ini`

```ini
[pytest]
filterwarnings =
    ; https://github.com/RDFLib/pyrdfa3/issues/31
    ignore:the imp module is deprecated:DeprecationWarning
    ignore:the imp module is deprecated:PendingDeprecationWarning
    ; https://github.com/html5lib/html5lib-python/issues/402
    ; https://bugs.launchpad.net/beautifulsoup/+bug/1847592
    ignore:Using or importing the ABCs:DeprecationWarning

```

### `README.rst`

```rst
=======
extruct
=======

.. image:: https://github.com/scrapinghub/extruct/workflows/build/badge.svg?branch=master
    :target: https://github.com/scrapinghub/extruct/actions
    :alt: Build Status

.. image:: https://img.shields.io/codecov/c/github/scrapinghub/extruct/master.svg?maxAge=2592000
    :target: https://codecov.io/gh/scrapinghub/extruct
    :alt: Coverage report

.. image:: https://img.shields.io/pypi/v/extruct.svg
   :target: https://pypi.python.org/pypi/extruct
   :alt: PyPI Version


*extruct* is a library for extracting embedded metadata from HTML markup.

Currently, *extruct* supports:

- `W3C's HTML Microdata`_
- `embedded JSON-LD`_
- `Microformat`_ via `mf2py`_
- `Facebook's Open Graph`_
- (experimental) `RDFa`_ via `rdflib`_
- `Dublin Core Metadata (DC-HTML-2003)`_

.. _W3C's HTML Microdata: http://www.w3.org/TR/microdata/
.. _embedded JSON-LD: http://www.w3.org/TR/json-ld/#embedding-json-ld-in-html-documents
.. _RDFa: https://www.w3.org/TR/html-rdfa/
.. _rdflib: https://pypi.python.org/pypi/rdflib/
.. _Microformat: http://microformats.org/wiki/Main_Page
.. _mf2py: https://github.com/microformats/mf2py
.. _Facebook's Open Graph: http://ogp.me/
.. _Dublin Core Metadata (DC-HTML-2003): https://www.dublincore.org/specifications/dublin-core/dcq-html/2003-11-30/

The microdata algorithm is a revisit of `this Scrapinghub blog post`_ showing how to use EXSLT extensions.

.. _this Scrapinghub blog post: http://blog.scrapinghub.com/2014/06/18/extracting-schema-org-microdata-using-scrapy-selectors-and-xpath/


Installation
------------

::

    pip install extruct


Usage
-----

All-in-one extraction
+++++++++++++++++++++

The simplest example how to use extruct is to call
``extruct.extract(htmlstring, base_url=base_url)``
with some HTML string and an optional base URL.

Let's try this on a webpage that uses all the syntaxes supported (RDFa with `ogp`_).

First fetch the HTML using python-requests and then feed the response body to ``extruct``::

  >>> import extruct
  >>> import requests
  >>> import pprint
  >>> from w3lib.html import get_base_url
  >>>
  >>> pp = pprint.PrettyPrinter(indent=2)
  >>> r = requests.get('https://www.optimizesmart.com/how-to-use-open-graph-protocol/')
  >>> base_url = get_base_url(r.text, r.url)
  >>> data = extruct.extract(r.text, base_url=base_url)
  >>>
  >>> pp.pprint(data)
  { 'dublincore': [ { 'elements': [ { 'URI': 'http://purl.org/dc/elements/1.1/description',
                                        'content': 'What is Open Graph Protocol '
                                                   'and why you need it? Learn to '
                                                   'implement Open Graph Protocol '
                                                   'for Facebook on your website. '
                                                   'Open Graph Protocol Meta Tags.',
                                        'name': 'description'}],
                        'namespaces': {},
                        'terms': []}],

  'json-ld': [ { '@context': 'https://schema.org',
                   '@id': '#organization',
                   '@type': 'Organization',
                   'logo': 'https://www.optimizesmart.com/wp-content/uploads/2016/03/optimize-smart-Twitter-logo.jpg',
                   'name': 'Optimize Smart',
                   'sameAs': [ 'https://www.facebook.com/optimizesmart/',
                               'https://uk.linkedin.com/in/analyticsnerd',
                               'https://www.youtube.com/user/optimizesmart',
                               'https://twitter.com/analyticsnerd'],
                   'url': 'https://www.optimizesmart.com/'}],
    'microdata': [ { 'properties': {'headline': ''},
                     'type': 'http://schema.org/WPHeader'}],
    'microformat': [ { 'children': [ { 'properties': { 'category': [ 'specialized-tracking'],
                                                       'name': [ 'Open Graph '
                                                                 'Protocol for '
                                                                 'Facebook '
                                                                 'explained with '
                                                                 'examples\n'
                                                                 '\n'
                                                                 'Specialized '
                                                                 'Tracking\n'
                                                                 '\n'
                                                                 '\n'
                                                                 (...)
                                                                 'Follow '
                                                                 '@analyticsnerd\n'
                                                                 '!function(d,s,id){var '
                                                                 "js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, "
                                                                 "'script', "
                                                                 "'twitter-wjs');"]},
                                       'type': ['h-entry']}],
                       'properties': { 'name': [ 'Open Graph Protocol for '
                                                 'Facebook explained with '
                                                 'examples\n'
                                                 (...)
                                                 'Follow @analyticsnerd\n'
                                                 '!function(d,s,id){var '
                                                 "js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, "
                                                 "'script', 'twitter-wjs');"]},
                       'type': ['h-feed']}],
    'opengraph': [ { 'namespace': {'og': 'http://ogp.me/ns#'},
                     'properties': [ ('og:locale', 'en_US'),
                                     ('og:type', 'article'),
                                     ( 'og:title',
                                       'Open Graph Protocol for Facebook '
                                       'explained with examples'),
                                     ( 'og:description',
                                       'What is Open Graph Protocol and why you '
                                       'need it? Learn to implement Open Graph '
                                       'Protocol for Facebook on your website. '
                                       'Open Graph Protocol Meta Tags.'),
                                     ( 'og:url',
                                       'https://www.optimizesmart.com/how-to-use-open-graph-protocol/'),
                                     ('og:site_name', 'Optimize Smart'),
                                     ( 'og:updated_time',
                                       '2018-03-09T16:26:35+00:00'),
                                     ( 'og:image',
                                       'https://www.optimizesmart.com/wp-content/uploads/2010/07/open-graph-protocol.jpg'),
                                     ( 'og:image:secure_url',
                                       'https://www.optimizesmart.com/wp-content/uploads/2010/07/open-graph-protocol.jpg')]}],
    'rdfa': [ { '@id': 'https://www.optimizesmart.com/how-to-use-open-graph-protocol/#header',
                'http://www.w3.org/1999/xhtml/vocab#role': [ { '@id': 'http://www.w3.org/1999/xhtml/vocab#banner'}]},
              { '@id': 'https://www.optimizesmart.com/how-to-use-open-graph-protocol/',
                'article:modified_time': [ { '@value': '2018-03-09T16:26:35+00:00'}],
                'article:published_time': [ { '@value': '2010-07-02T18:57:23+00:00'}],
                'article:publisher': [ { '@value': 'https://www.facebook.com/optimizesmart/'}],
                'article:section': [{'@value': 'Specialized Tracking'}],
                'http://ogp.me/ns#description': [ { '@value': 'What is Open '
                                                              'Graph Protocol '
                                                              'and why you need '
                                                              'it? Learn to '
                                                              'implement Open '
                                                              'Graph Protocol '
                                                              'for Facebook on '
                                                              'your website. '
                                                              'Open Graph '
                                                              'Protocol Meta '
                                                              'Tags.'}],
                'http://ogp.me/ns#image': [ { '@value': 'https://www.optimizesmart.com/wp-content/uploads/2010/07/open-graph-protocol.jpg'}],
                'http://ogp.me/ns#image:secure_url': [ { '@value': 'https://www.optimizesmart.com/wp-content/uploads/2010/07/open-graph-protocol.jpg'}],
                'http://ogp.me/ns#locale': [{'@value': 'en_US'}],
                'http://ogp.me/ns#site_name': [{'@value': 'Optimize Smart'}],
                'http://ogp.me/ns#title': [ { '@value': 'Open Graph Protocol for '
                                                        'Facebook explained with '
                                                        'examples'}],
                'http://ogp.me/ns#type': [{'@value': 'article'}],
                'http://ogp.me/ns#updated_time': [ { '@value': '2018-03-09T16:26:35+00:00'}],
                'http://ogp.me/ns#url': [ { '@value': 'https://www.optimizesmart.com/how-to-use-open-graph-protocol/'}],
                'https://api.w.org/': [ { '@id': 'https://www.optimizesmart.com/wp-json/'}]}]}

Select syntaxes
+++++++++++++++
It is possible to select which syntaxes to extract by passing a list with the desired ones to extract. Valid values: 'microdata', 'json-ld', 'opengraph', 'microformat', 'rdfa' and 'dublincore'. If no list is passed all syntaxes will be extracted and returned::

  >>> r = requests.get('http://www.songkick.com/artists/236156-elysian-fields')
  >>> base_url = get_base_url(r.text, r.url)
  >>> data = extruct.extract(r.text, base_url, syntaxes=['microdata', 'opengraph', 'rdfa'])
  >>>
  >>> pp.pprint(data)
  { 'microdata': [],
    'opengraph': [ { 'namespace': { 'concerts': 'http://ogp.me/ns/fb/songkick-concerts#',
                                    'fb': 'http://www.facebook.com/2008/fbml',
                                    'og': 'http://ogp.me/ns#'},
                     'properties': [ ('fb:app_id', '308540029359'),
                                     ('og:site_name', 'Songkick'),
                                     ('og:type', 'songkick-concerts:artist'),
                                     ('og:title', 'Elysian Fields'),
                                     ( 'og:description',
                                       'Find out when Elysian Fields is next '
                                       'playing live near you. List of all '
                                       'Elysian Fields tour dates and concerts.'),
                                     ( 'og:url',
                                       'https://www.songkick.com/artists/236156-elysian-fields'),
                                     ( 'og:image',
                                       'http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg')]}],
    'rdfa': [ { '@id': 'https://www.songkick.com/artists/236156-elysian-fields',
                'al:ios:app_name': [{'@value': 'Songkick Concerts'}],
                'al:ios:app_store_id': [{'@value': '438690886'}],
                'al:ios:url': [ { '@value': 'songkick://artists/236156-elysian-fields'}],
                'http://ogp.me/ns#description': [ { '@value': 'Find out when '
                                                              'Elysian Fields is '
                                                              'next playing live '
                                                              'near you. List of '
                                                              'all Elysian '
                                                              'Fields tour dates '
                                                              'and concerts.'}],
                'http://ogp.me/ns#image': [ { '@value': 'http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg'}],
                'http://ogp.me/ns#site_name': [{'@value': 'Songkick'}],
                'http://ogp.me/ns#title': [{'@value': 'Elysian Fields'}],
                'http://ogp.me/ns#type': [{'@value': 'songkick-concerts:artist'}],
                'http://ogp.me/ns#url': [ { '@value': 'https://www.songkick.com/artists/236156-elysian-fields'}],
                'http://www.facebook.com/2008/fbmlapp_id': [ { '@value': '308540029359'}]}]}

Alternatively, if you already parsed the HTML before calling extruct, you can use the tree instead of the HTML string: ::

  >>> # using the request from the previous example
  >>> base_url = get_base_url(r.text, r.url)
  >>> from extruct.utils import parse_html
  >>> tree = parse_html(r.text)
  >>> data = extruct.extract(tree, base_url, syntaxes=['microdata', 'opengraph', 'rdfa'])

Microformat format doesn't support the HTML tree, so you need to use a HTML string.

Uniform
+++++++
Another option is to uniform the output of microformat, opengraph, microdata, dublincore and json-ld syntaxes to the following structure: ::

    {'@context': 'http://example.com',
                 '@type': 'example_type',
                 /* All other the properties in keys here */
                 }

To do so set ``uniform=True`` when calling ``extract``, it's false by default for backward compatibility. Here the same example as before but with uniform set to True: ::

  >>> r = requests.get('http://www.songkick.com/artists/236156-elysian-fields')
  >>> base_url = get_base_url(r.text, r.url)
  >>> data = extruct.extract(r.text, base_url, syntaxes=['microdata', 'opengraph', 'rdfa'], uniform=True)
  >>>
  >>> pp.pprint(data)
  { 'microdata': [],
    'opengraph': [ { '@context': { 'concerts': 'http://ogp.me/ns/fb/songkick-concerts#',
                                 'fb': 'http://www.facebook.com/2008/fbml',
                                 'og': 'http://ogp.me/ns#'},
                   '@type': 'songkick-concerts:artist',
                   'fb:app_id': '308540029359',
                   'og:description': 'Find out when Elysian Fields is next '
                                     'playing live near you. List of all '
                                     'Elysian Fields tour dates and concerts.',
                   'og:image': 'http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg',
                   'og:site_name': 'Songkick',
                   'og:title': 'Elysian Fields',
                   'og:url': 'https://www.songkick.com/artists/236156-elysian-fields'}],
    'rdfa': [ { '@id': 'https://www.songkick.com/artists/236156-elysian-fields',
                'al:ios:app_name': [{'@value': 'Songkick Concerts'}],
                'al:ios:app_store_id': [{'@value': '438690886'}],
                'al:ios:url': [ { '@value': 'songkick://artists/236156-elysian-fields'}],
                'http://ogp.me/ns#description': [ { '@value': 'Find out when '
                                                              'Elysian Fields is '
                                                              'next playing live '
                                                              'near you. List of '
                                                              'all Elysian '
                                                              'Fields tour dates '
                                                              'and concerts.'}],
                'http://ogp.me/ns#image': [ { '@value': 'http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg'}],
                'http://ogp.me/ns#site_name': [{'@value': 'Songkick'}],
                'http://ogp.me/ns#title': [{'@value': 'Elysian Fields'}],
                'http://ogp.me/ns#type': [{'@value': 'songkick-concerts:artist'}],
                'http://ogp.me/ns#url': [ { '@value': 'https://www.songkick.com/artists/236156-elysian-fields'}],
                'http://www.facebook.com/2008/fbmlapp_id': [ { '@value': '308540029359'}]}]}

NB rdfa structure is not uniformed yet.

Returning HTML node
+++++++++++++++++++

It is also possible to get references to HTML node for every extracted metadata item.
The feature is supported only by microdata syntax.

To use that, just set the ``return_html_node`` option of ``extract`` method to ``True``.
As the result, an additional key "nodeHtml" will be included in the result for every
item. Each node is of ``lxml.etree.Element`` type: ::

  >>> r = requests.get('http://www.rugpadcorner.com/shop/no-muv/')
  >>> base_url = get_base_url(r.text, r.url)
  >>> data = extruct.extract(r.text, base_url, syntaxes=['microdata'], return_html_node=True)
  >>>
  >>> pp.pprint(data)
  { 'microdata': [ { 'htmlNode': <Element div at 0x7f10f8e6d3b8>,
                     'properties': { 'description': 'KEEP RUGS FLAT ON CARPET!\n'
                                                    'Not your thin sticky pad, '
                                                    'No-Muv is truly the best!',
                                     'image': ['', ''],
                                     'name': ['No-Muv', 'No-Muv'],
                                     'offers': [ { 'htmlNode': <Element div at 0x7f10f8e6d138>,
                                                   'properties': { 'availability': 'http://schema.org/InStock',
                                                                   'price': 'Price:  '
                                                                            '$45'},
                                                   'type': 'http://schema.org/Offer'},
                                                 { 'htmlNode': <Element div at 0x7f10f8e60f48>,
                                                   'properties': { 'availability': 'http://schema.org/InStock',
                                                                   'price': '(Select '
                                                                            'Size/Shape '
                                                                            'for '
                                                                            'Pricing)'},
                                                   'type': 'http://schema.org/Offer'}],
                                     'ratingValue': ['5.00', '5.00']},
                     'type': 'http://schema.org/Product'}]}

Single extractors
-----------------

You can also use each extractor individually. See below.

Microdata extraction
++++++++++++++++++++
::

  >>> import pprint
  >>> pp = pprint.PrettyPrinter(indent=2)
  >>>
  >>> from extruct.w3cmicrodata import MicrodataExtractor
  >>>
  >>> # example from http://www.w3.org/TR/microdata/#associating-names-with-items
  >>> html = """<!DOCTYPE HTML>
  ... <html>
  ...  <head>
  ...   <title>Photo gallery</title>
  ...  </head>
  ...  <body>
  ...   <h1>My photos</h1>
  ...   <figure itemscope itemtype="http://n.whatwg.org/work" itemref="licenses">
  ...    <img itemprop="work" src="images/house.jpeg" alt="A white house, boarded up, sits in a forest.">
  ...    <figcaption itemprop="title">The house I found.</figcaption>
  ...   </figure>
  ...   <figure itemscope itemtype="http://n.whatwg.org/work" itemref="licenses">
  ...    <img itemprop="work" src="images/mailbox.jpeg" alt="Outside the house is a mailbox. It has a leaflet inside.">
  ...    <figcaption itemprop="title">The mailbox.</figcaption>
  ...   </figure>
  ...   <footer>
  ...    <p id="licenses">All images licensed under the <a itemprop="license"
  ...    href="http://www.opensource.org/licenses/mit-license.php">MIT
  ...    license</a>.</p>
  ...   </footer>
  ...  </body>
  ... </html>"""
  >>>
  >>> mde = MicrodataExtractor()
  >>> data = mde.extract(html)
  >>> pp.pprint(data)
  [{'properties': {'license': 'http://www.opensource.org/licenses/mit-license.php',
                   'title': 'The house I found.',
                   'work': 'http://www.example.com/images/house.jpeg'},
    'type': 'http://n.whatwg.org/work'},
   {'properties': {'license': 'http://www.opensource.org/licenses/mit-license.php',
                   'title': 'The mailbox.',
                   'work': 'http://www.example.com/images/mailbox.jpeg'},
    'type': 'http://n.whatwg.org/work'}]

JSON-LD extraction
++++++++++++++++++
::

  >>> import pprint
  >>> pp = pprint.PrettyPrinter(indent=2)
  >>>
  >>> from extruct.jsonld import JsonLdExtractor
  >>>
  >>> html = """<!DOCTYPE HTML>
  ... <html>
  ...  <head>
  ...   <title>Some Person Page</title>
  ...  </head>
  ...  <body>
  ...   <h1>This guys</h1>
  ...     <script type="application/ld+json">
  ...     {
  ...       "@context": "http://schema.org",
  ...       "@type": "Person",
  ...       "name": "John Doe",
  ...       "jobTitle": "Graduate research assistant",
  ...       "affiliation": "University of Dreams",
  ...       "additionalName": "Johnny",
  ...       "url": "http://www.example.com",
  ...       "address": {
  ...         "@type": "PostalAddress",
  ...         "streetAddress": "1234 Peach Drive",
  ...         "addressLocality": "Wonderland",
  ...         "addressRegion": "Georgia"
  ...       }
  ...     }
  ...     </script>
  ...  </body>
  ... </html>"""
  >>>
  >>> jslde = JsonLdExtractor()
  >>>
  >>> data = jslde.extract(html)
  >>> pp.pprint(data)
  [{'@context': 'http://schema.org',
    '@type': 'Person',
    'additionalName': 'Johnny',
    'address': {'@type': 'PostalAddress',
                'addressLocality': 'Wonderland',
                'addressRegion': 'Georgia',
                'streetAddress': '1234 Peach Drive'},
    'affiliation': 'University of Dreams',
    'jobTitle': 'Graduate research assistant',
    'name': 'John Doe',
    'url': 'http://www.example.com'}]


RDFa extraction (experimental)
++++++++++++++++++++++++++++++

::

  >>> import pprint
  >>> pp = pprint.PrettyPrinter(indent=2)
  >>> from extruct.rdfa import RDFaExtractor  # you can ignore the warning about html5lib not being available
  INFO:rdflib:RDFLib Version: 4.2.1
  /home/paul/.virtualenvs/extruct.wheel.test/lib/python3.5/site-packages/rdflib/plugins/parsers/structureddata.py:30: UserWarning: html5lib not found! RDFa and Microdata parsers will not be available.
    'parsers will not be available.')
  >>>
  >>> html = """<html>
  ...  <head>
  ...    ...
  ...  </head>
  ...  <body prefix="dc: http://purl.org/dc/terms/ schema: http://schema.org/">
  ...    <div resource="/alice/posts/trouble_with_bob" typeof="schema:BlogPosting">
  ...       <h2 property="dc:title">The trouble with Bob</h2>
  ...       ...
  ...       <h3 property="dc:creator schema:creator" resource="#me">Alice</h3>
  ...       <div property="schema:articleBody">
  ...         <p>The trouble with Bob is that he takes much better photos than I do:</p>
  ...       </div>
  ...      ...
  ...    </div>
  ...  </body>
  ... </html>
  ... """
  >>>
  >>> rdfae = RDFaExtractor()
  >>> pp.pprint(rdfae.extract(html, base_url='http://www.example.com/index.html'))
  [{'@id': 'http://www.example.com/alice/posts/trouble_with_bob',
    '@type': ['http://schema.org/BlogPosting'],
    'http://purl.org/dc/terms/creator': [{'@id': 'http://www.example.com/index.html#me'}],
    'http://purl.org/dc/terms/title': [{'@value': 'The trouble with Bob'}],
    'http://schema.org/articleBody': [{'@value': '\n'
                                                 '        The trouble with Bob '
                                                 'is that he takes much better '
                                                 'photos than I do:\n'
                                                 '      '}],
    'http://schema.org/creator': [{'@id': 'http://www.example.com/index.html#me'}]}]

You'll get a list of expanded JSON-LD nodes.


Open Graph extraction
++++++++++++++++++++++++++++++

::

  >>> import pprint
  >>> pp = pprint.PrettyPrinter(indent=2)
  >>>
  >>> from extruct.opengraph import OpenGraphExtractor
  >>>
  >>> html = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  ... <html xmlns="https://www.w3.org/1999/xhtml" xmlns:og="https://ogp.me/ns#" xmlns:fb="https://www.facebook.com/2008/fbml">
  ...  <head>
  ...   <title>Himanshu's Open Graph Protocol</title>
  ...   <meta http-equiv="Content-Type" content="text/html;charset=WINDOWS-1252" />
  ...   <meta http-equiv="Content-Language" content="en-us" />
  ...   <link rel="stylesheet" type="text/css" href="event-education.css" />
  ...   <meta name="verify-v1" content="so4y/3aLT7/7bUUB9f6iVXN0tv8upRwaccek7JKB1gs=" >
  ...   <meta property="og:title" content="Himanshu's Open Graph Protocol"/>
  ...   <meta property="og:type" content="article"/>
  ...   <meta property="og:url" content="https://www.eventeducation.com/test.php"/>
  ...   <meta property="og:image" content="https://www.eventeducation.com/images/982336_wedding_dayandouan_th.jpg"/>
  ...   <meta property="fb:admins" content="himanshu160"/>
  ...   <meta property="og:site_name" content="Event Education"/>
  ...   <meta property="og:description" content="Event Education provides free courses on event planning and management to event professionals worldwide."/>
  ...  </head>
  ...  <body>
  ...   <div id="fb-root"></div>
  ...   <script>(function(d, s, id) {
  ...               var js, fjs = d.getElementsByTagName(s)[0];
  ...               if (d.getElementById(id)) return;
  ...                  js = d.createElement(s); js.id = id;
  ...                  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=501839739845103";
  ...                  fjs.parentNode.insertBefore(js, fjs);
  ...                  }(document, 'script', 'facebook-jssdk'));</script>
  ...  </body>
  ... </html>"""
  >>>
  >>> opengraphe = OpenGraphExtractor()
  >>> pp.pprint(opengraphe.extract(html))
  [{"namespace": {
        "og": "http://ogp.me/ns#"
    },
    "properties": [
        [
            "og:title",
            "Himanshu's Open Graph Protocol"
        ],
        [
            "og:type",
            "article"
        ],
        [
            "og:url",
            "https://www.eventeducation.com/test.php"
        ],
        [
            "og:image",
            "https://www.eventeducation.com/images/982336_wedding_dayandouan_th.jpg"
        ],
        [
            "og:site_name",
            "Event Education"
        ],
        [
            "og:description",
            "Event Education provides free courses on event planning and management to event professionals worldwide."
        ]
      ]
   }]


Microformat extraction
++++++++++++++++++++++++++++++

::

  >>> import pprint
  >>> pp = pprint.PrettyPrinter(indent=2)
  >>>
  >>> from extruct.microformat import MicroformatExtractor
  >>>
  >>> html = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  ... <html xmlns="https://www.w3.org/1999/xhtml" xmlns:og="https://ogp.me/ns#" xmlns:fb="https://www.facebook.com/2008/fbml">
  ...  <head>
  ...   <title>Himanshu's Open Graph Protocol</title>
  ...   <meta http-equiv="Content-Type" content="text/html;charset=WINDOWS-1252" />
  ...   <meta http-equiv="Content-Language" content="en-us" />
  ...   <link rel="stylesheet" type="text/css" href="event-education.css" />
  ...   <meta name="verify-v1" content="so4y/3aLT7/7bUUB9f6iVXN0tv8upRwaccek7JKB1gs=" >
  ...   <meta property="og:title" content="Himanshu's Open Graph Protocol"/>
  ...   <article class="h-entry">
  ...    <h1 class="p-name">Microformats are amazing</h1>
  ...    <p>Published by <a class="p-author h-card" href="http://example.com">W. Developer</a>
  ...       on <time class="dt-published" datetime="2013-06-13 12:00:00">13<sup>th</sup> June 2013</time></p>
  ...    <p class="p-summary">In which I extoll the virtues of using microformats.</p>
  ...    <div class="e-content">
  ...     <p>Blah blah blah</p>
  ...    </div>
  ...   </article>
  ...  </head>
  ...  <body></body>
  ... </html>"""
  >>>
  >>> microformate = MicroformatExtractor()
  >>> data = microformate.extract(html)
  >>> pp.pprint(data)
  [{"type": [
        "h-entry"
    ],
    "properties": {
        "name": [
            "Microformats are amazing"
        ],
        "author": [
            {
                "type": [
                    "h-card"
                ],
                "properties": {
                    "name": [
                        "W. Developer"
                    ],
                    "url": [
                        "http://example.com"
                    ]
                },
                "value": "W. Developer"
            }
        ],
        "published": [
            "2013-06-13 12:00:00"
        ],
        "summary": [
            "In which I extoll the virtues of using microformats."
        ],
        "content": [
            {
                "html": "\n<p>Blah blah blah</p>\n",
                "value": "\nBlah blah blah\n"
            }
        ]
      }
   }]

DublinCore extraction
++++++++++++++++++++++++++++++
::

    >>> import pprint
    >>> pp = pprint.PrettyPrinter(indent=2)
    >>> from extruct.dublincore import DublinCoreExtractor
    >>> html = '''<head profile="http://dublincore.org/documents/dcq-html/">
    ... <title>Expressing Dublin Core in HTML/XHTML meta and link elements</title>
    ... <link rel="schema.DC" href="http://purl.org/dc/elements/1.1/" />
    ... <link rel="schema.DCTERMS" href="http://purl.org/dc/terms/" />
    ...
    ...
    ... <meta name="DC.title" lang="en" content="Expressing Dublin Core
    ... in HTML/XHTML meta and link elements" />
    ... <meta name="DC.creator" content="Andy Powell, UKOLN, University of Bath" />
    ... <meta name="DCTERMS.issued" scheme="DCTERMS.W3CDTF" content="2003-11-01" />
    ... <meta name="DC.identifier" scheme="DCTERMS.URI"
    ... content="http://dublincore.org/documents/dcq-html/" />
    ... <link rel="DCTERMS.replaces" hreflang="en"
    ... href="http://dublincore.org/documents/2000/08/15/dcq-html/" />
    ... <meta name="DCTERMS.abstract" content="This document describes how
    ... qualified Dublin Core metadata can be encoded
    ... in HTML/XHTML &lt;meta&gt; elements" />
    ... <meta name="DC.format" scheme="DCTERMS.IMT" content="text/html" />
    ... <meta name="DC.type" scheme="DCTERMS.DCMIType" content="Text" />
    ... <meta name="DC.Date.modified" content="2001-07-18" />
    ... <meta name="DCTERMS.modified" content="2001-07-18" />'''
    >>> dublinlde = DublinCoreExtractor()
    >>> data = dublinlde.extract(html)
    >>> pp.pprint(data)
    [ { 'elements': [ { 'URI': 'http://purl.org/dc/elements/1.1/title',
                        'content': 'Expressing Dublin Core\n'
                                   'in HTML/XHTML meta and link elements',
                        'lang': 'en',
                        'name': 'DC.title'},
                      { 'URI': 'http://purl.org/dc/elements/1.1/creator',
                        'content': 'Andy Powell, UKOLN, University of Bath',
                        'name': 'DC.creator'},
                      { 'URI': 'http://purl.org/dc/elements/1.1/identifier',
                        'content': 'http://dublincore.org/documents/dcq-html/',
                        'name': 'DC.identifier',
                        'scheme': 'DCTERMS.URI'},
                      { 'URI': 'http://purl.org/dc/elements/1.1/format',
                        'content': 'text/html',
                        'name': 'DC.format',
                        'scheme': 'DCTERMS.IMT'},
                      { 'URI': 'http://purl.org/dc/elements/1.1/type',
                        'content': 'Text',
                        'name': 'DC.type',
                        'scheme': 'DCTERMS.DCMIType'}],
        'namespaces': { 'DC': 'http://purl.org/dc/elements/1.1/',
                        'DCTERMS': 'http://purl.org/dc/terms/'},
        'terms': [ { 'URI': 'http://purl.org/dc/terms/issued',
                     'content': '2003-11-01',
                     'name': 'DCTERMS.issued',
                     'scheme': 'DCTERMS.W3CDTF'},
                   { 'URI': 'http://purl.org/dc/terms/abstract',
                     'content': 'This document describes how\n'
                                'qualified Dublin Core metadata can be encoded\n'
                                'in HTML/XHTML <meta> elements',
                     'name': 'DCTERMS.abstract'},
                   { 'URI': 'http://purl.org/dc/terms/modified',
                     'content': '2001-07-18',
                     'name': 'DC.Date.modified'},
                   { 'URI': 'http://purl.org/dc/terms/modified',
                     'content': '2001-07-18',
                     'name': 'DCTERMS.modified'},
                   { 'URI': 'http://purl.org/dc/terms/replaces',
                     'href': 'http://dublincore.org/documents/2000/08/15/dcq-html/',
                     'hreflang': 'en',
                     'rel': 'DCTERMS.replaces'}]}]



Command Line Tool
-----------------

*extruct* provides a command line tool that allows you to fetch a page and
extract the metadata from it directly from the command line.

Dependencies
++++++++++++

The command line tool depends on ``requests``, which is not installed by default
when you install **extruct**. In order to use the command line tool, you can
install **extruct** with the `cli` extra requirements::

    pip install 'extruct[cli]'


Usage
+++++

::

    extruct "http://example.com"

Downloads "http://example.com" and outputs the Microdata, JSON-LD and RDFa, Open Graph
and Microformat metadata to `stdout`.

Supported Parameters
++++++++++++++++++++

By default, the command line tool will try to extract all the supported
metadata formats from the page (currently Microdata, JSON-LD, RDFa, Open Graph
and Microformat). If you want to restrict the output to just one or a subset of
those, you can pass their individual names collected in a list through 'syntaxes' argument.

For example, this command extracts only Microdata and JSON-LD metadata from
"http://example.com"::

    extruct "http://example.com" --syntaxes microdata json-ld

NB syntaxes names passed must correspond to these: microdata, json-ld, rdfa, opengraph, microformat

Development version
-------------------

::

    mkvirtualenv extruct
    pip install -r requirements-dev.txt


Tests
-----

Run tests in current environment::

    py.test tests


Use tox_ to run tests with different Python versions::

    tox


.. _tox: https://testrun.org/tox/latest/
.. _ogp: https://ogp.me/

```

### `requirements-dev.txt`

```txt
# project requirements for development, install them using following command:
# pip install -r requirements-dev.txt

-r requirements.txt

tox
bumpversion

pytest
pytest-cov
readme_renderer
mock
black
pre-commit

```

### `requirements.txt`

```txt
# project requirements, install them using following command:
# pip install -r requirements.txt
lxml
lxml-html-clean
requests
rdflib>=6.0.0
pyrdfa3
mf2py>=1.1.0
w3lib
html-text
jstyleson

```

### `setup.cfg`

```cfg
[bumpversion]
current_version = 0.18.0
commit = True
tag = True

[bumpversion:file:extruct/VERSION]

[wheel]
universal = 1

```

### `setup.py`

```py
# mypy: disallow_untyped_defs=False
import os

from setuptools import find_packages, setup


def get_readme():
    path = os.path.join(os.path.dirname(__file__), "README.rst")
    with open(path) as f:
        return f.read().strip()


def get_version():
    path = os.path.join(os.path.dirname(__file__), "extruct", "VERSION")
    with open(path) as f:
        return f.read().strip()


setup(
    name="extruct",
    version=get_version(),
    description="Extract embedded metadata from HTML markup",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Scrapinghub",
    author_email="info@scrapinghub.com",
    maintainer="Scrapinghub",
    maintainer_email="info@scrapinghub.com",
    url="https://github.com/scrapinghub/extruct",
    entry_points={
        "console_scripts": {
            "extruct = extruct.tool:main",
        }
    },
    packages=find_packages(
        exclude=[
            "tests",
        ]
    ),
    package_data={"extruct": ["VERSION"]},
    python_requires=">=3.8",
    install_requires=[
        "lxml",
        "lxml-html-clean",
        "rdflib>=6.0.0",
        "pyrdfa3",
        "mf2py",
        "w3lib",
        "html-text>=0.5.1",
        "jstyleson",
    ],
    extras_require={
        "cli": [
            "requests",
        ],
    },
    keywords="extruct",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)

```

### `tests/__init__.py`

```py
# mypy: disallow_untyped_defs=False
import json
import os

tests_datadir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "samples")


def get_testdata(*paths):
    """Return test data"""
    path = os.path.join(tests_datadir, *paths)
    with open(path, "rb") as f_in:
        return f_in.read()


def jsonize_dict(d):
    return json.loads(json.dumps(d))


def replace_node_ref_with_node_id(item):
    if isinstance(item, list):
        for i in item:
            replace_node_ref_with_node_id(i)
    if isinstance(item, dict):
        for key in list(item):
            val = item[key]
            if key == "htmlNode":
                item["_nodeId_"] = val.get("id")
                del item[key]
            else:
                replace_node_ref_with_node_id(val)

```

### `tests/samples/custom.invalid/AllocateAction.001.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- AllocateAction</title>
</head>

<body>
<script type="application/ld+json">
  // John allocated 5 hours to exercise.
{
  "@context": "http://schema.org",
  "@type": "AllocateAction",
  "agent": {
    "@type": "Person",
    "name": "John"
  },
  "object": {
    "@type": "Duration",
    "name": "5 hours"
  },
  "purpose": {
    "@type": "ExercisePlan",
    "name": "John's weight loss plan"
  },
	"rendered_js": "// John allocated 5 hours to exercise."
}
</script>
</body>

</html>

```

### `tests/samples/custom.invalid/AllocateAction.001.jsonld`

```jsonld
[
    {
      "@context": "http://schema.org",
      "@type": "AllocateAction",
      "agent": {
        "@type": "Person",
        "name": "John"
      },
      "object": {
        "@type": "Duration",
        "name": "5 hours"
      },
      "purpose": {
        "@type": "ExercisePlan",
        "name": "John's weight loss plan"
      },
      "rendered_js": "// John allocated 5 hours to exercise."
    }
]

```

### `tests/samples/custom.invalid/JoinAction.001.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- JoinAction</title>
</head>

<body>
<script type="application/ld+json">
<!-- John joined the festival. -->
{
  "@context": "http://schema.org",
  "@type": "JoinAction",
  "agent": {
    "@type": "Person",
    "name": "John"
  },
  "event": {
    "@type": "Festival",
    "name": "Woodstock"
  },
	"rendered_html": "<!-- John joined the festival. --><b>some text</b>"
}
</script>
</body>

</html>

```

### `tests/samples/custom.invalid/JoinAction.001.jsonld`

```jsonld
[
    {
        "@type": "JoinAction",
        "@context": "http://schema.org",
        "agent": {"name": "John", "@type": "Person"},
        "event": {"name": "Woodstock", "@type": "Festival"},
        "rendered_html": "<!-- John joined the festival. --><b>some text</b>"
    }
]

```

### `tests/samples/custom.invalid/JSONLD_with_control_characters_comment.html`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <script type="application/ld+json">
    {
        "data": "<!-- John joined the festival. --><b>some
        text</b>"
    }
    </script>
</head>

<body></body>

</html>

```

### `tests/samples/custom.invalid/JSONLD_with_control_characters_comment.jsonld`

```jsonld
[
    {
        "data": "<!-- John joined the festival. --><b>some\n        text</b>"
    }
]

```

### `tests/samples/custom.invalid/JSONLD_with_control_characters.html`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <script type="application/ld+json">
    {
        "data": "line 1
        line 2
        line 3
"
    }
    </script>
</head>

<body></body>

</html>
```

### `tests/samples/custom.invalid/JSONLD_with_control_characters.jsonld`

```jsonld
[
    {
        "data": "line 1\n        line 2\n        line 3\n"
    }
]
```

### `tests/samples/custom.invalid/JSONLD_with_JS_comment.html`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <script type="application/ld+json">

	{
		"@context": "http://schema.org",
		"@type": "NewsArticle",
		"thumbnailUrl": "https://uc.udn.com.tw/photo/2019/11/11/99/7053890.jpg",
		"keywords": "",
		"url": "https://money.udn.com/money/story/5635/4158094",
		"mainEntityOfPage": "https://money.udn.com/money/story/5635/4158094",
		"headline": "讓AI挑出感興趣 SparkAmplify精準行銷當紅",
		"articleSection": "商情", // category
		//"interactionCount": ""
	}
		
    </script>
</head>

<body></body>

</html>
```

### `tests/samples/custom.invalid/JSONLD_with_JS_comment.jsonld`

```jsonld
[
	{
		"@context": "http://schema.org",
		"@type": "NewsArticle",
		"thumbnailUrl": "https://uc.udn.com.tw/photo/2019/11/11/99/7053890.jpg",
		"keywords": "",
		"url": "https://money.udn.com/money/story/5635/4158094",
		"mainEntityOfPage": "https://money.udn.com/money/story/5635/4158094",
		"headline": "讓AI挑出感興趣 SparkAmplify精準行銷當紅",
		"articleSection": "商情"
	}
]
```

### `tests/samples/misc/dublincore_test.html`

```html
<head profile="http://dublincore.org/documents/dcq-html/">
<title>Expressing Dublin Core in HTML/XHTML meta and link elements</title>
<link rel="schema.DC" href="http://purl.org/dc/elements/1.1/" />
<link rel="schema.DCTERMS" href="http://purl.org/dc/terms/" />


<meta name="DC.title" lang="en" content="Expressing Dublin Core
in HTML/XHTML meta and link elements" />
<meta name="DC.creator" content="Andy Powell, UKOLN, University of Bath" />
<meta name="DCTERMS.issued" scheme="DCTERMS.W3CDTF" content="2003-11-01" />
<meta name="DC.identifier" scheme="DCTERMS.URI"
content="http://dublincore.org/documents/dcq-html/" />
<link rel="DCTERMS.replaces" hreflang="en"
href="http://dublincore.org/documents/2000/08/15/dcq-html/" />
<meta name="DCTERMS.abstract" content="This document describes how
qualified Dublin Core metadata can be encoded
in HTML/XHTML &lt;meta&gt; elements" />
<meta name="DC.format" scheme="DCTERMS.IMT" content="text/html" />
<meta name="DC.type" scheme="DCTERMS.DCMIType" content="Text" />
<meta name="DC.Date.modified" content="2001-07-18" />
<meta name="DCTERMS.modified" content="2001-07-18" />
```

### `tests/samples/misc/dublincore_test.json`

```json
[
  {
    "namespaces": {
      "DC": "http://purl.org/dc/elements/1.1/",
      "DCTERMS": "http://purl.org/dc/terms/"
    },
  "elements": [
    {"name": "DC.title", "lang": "en", "content": "Expressing Dublin Core\nin HTML/XHTML meta and link elements", "URI": "http://purl.org/dc/elements/1.1/title"},
    {"name": "DC.creator", "content": "Andy Powell, UKOLN, University of Bath", "URI": "http://purl.org/dc/elements/1.1/creator"},
    {"name": "DC.identifier", "scheme": "DCTERMS.URI", "content": "http://dublincore.org/documents/dcq-html/", "URI": "http://purl.org/dc/elements/1.1/identifier"},
    {"name": "DC.format", "scheme": "DCTERMS.IMT", "content": "text/html", "URI": "http://purl.org/dc/elements/1.1/format"},
    {"name": "DC.type", "scheme": "DCTERMS.DCMIType", "content": "Text", "URI": "http://purl.org/dc/elements/1.1/type"}
  ],
  "terms": [
    {"name": "DCTERMS.issued", "scheme": "DCTERMS.W3CDTF", "content": "2003-11-01", "URI": "http://purl.org/dc/terms/issued"},
    {"name": "DCTERMS.abstract", "content": "This document describes how\nqualified Dublin Core metadata can be encoded\nin HTML/XHTML <meta> elements", "URI": "http://purl.org/dc/terms/abstract"},
    {"name": "DC.Date.modified", "content": "2001-07-18", "URI": "http://purl.org/dc/terms/modified"},
    {"name": "DCTERMS.modified", "content": "2001-07-18", "URI": "http://purl.org/dc/terms/modified"},
    {"rel": "DCTERMS.replaces", "hreflang": "en", "href": "http://dublincore.org/documents/2000/08/15/dcq-html/", "URI": "http://purl.org/dc/terms/replaces"}
  ]
  }
]

```

### `tests/samples/misc/expanded_OG_support_test.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="https://www.w3.org/1999/xhtml" xmlns:og="https://ogp.me/ns#" xmlns:fb="https://www.facebook.com/2008/fbml">
	<head>
		<title>Himanshu's Open Graph Protocol</title>
		<meta http-equiv="Content-Type" content="text/html;charset=WINDOWS-1252" />
	   	<meta http-equiv="Content-Language" content="en-us" />
	   	<link rel="stylesheet" type="text/css" href="event-education.css" />
	   	<meta name="verify-v1" content="so4y/3aLT7/7bUUB9f6iVXN0tv8upRwaccek7JKB1gs=" >
	   	<meta property="og:image" content="https://www.eventeducation.com/images/982336_wedding_dayandouan_th.jpg"/>
   		<meta property="fb:admins" content="himanshu160"/>
   		<meta property="og:site_name" content="Event Education"/>

   		<meta property="og:url" content="http://www.nytimes.com/2016/12/15/arts/music/from-steet-theater-to-wagner-on-the-opera-stage.html" />
		<meta property="og:type" content="article" />
		<meta property="og:title" content="From Street Theater to Wagner on the Opera Stage" />
		<meta property="og:description" content="which he set in Bangladesh instead of Norway. The production opens in Madrid on Saturday." />
		<meta property="article:published" itemprop="datePublished" content="2016-12-15T05:55:55-05:00" />
		<meta property="article:modified" itemprop="dateModified" content="2016-12-15T06:19:30-05:00" />
		<meta property="article:section" itemprop="articleSection" content="Music" />
		<meta property="article:section-taxonomy-id" itemprop="articleSection" content="C5BFA7D5-359C-427B-90E6-6B7245A6CDD8" />
		<meta property="article:section_url" content="http://www.nytimes.com/section/arts" />
		<meta property="article:top-level-section" content="arts" />
		<meta property="fb:app_id" content="9869919170" />
		<meta property="music:duration" content="60" />
		<meta property="video:tag" content="Exhilerating" />
		<meta property="book:release_date" content="2016-12-15T06:19:30-05:00" />
		<meta property="profile:first_name" content="John" />
		<meta property="profile:last_name" content="Lennon" />
  	</head>
  	<body>
   		<div id="fb-root"></div>
   			<script>(function(d, s, id) {
               var js, fjs = d.getElementsByTagName(s)[0];
               if (d.getElementById(id)) return;
                  js = d.createElement(s); js.id = id;
                  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=501839739845103";
                  fjs.parentNode.insertBefore(js, fjs);
                  }(document, 'script', 'facebook-jssdk'));</script>
	</body>
</html>
```

### `tests/samples/misc/expanded_OG_support_test.json`

```json
[
  {
    "https://ogp.me/ns#url": [
      {
        "@value": "http://www.nytimes.com/2016/12/15/arts/music/from-steet-theater-to-wagner-on-the-opera-stage.html"
      }
    ], 
    "http://ogp.me/ns/profile#first_name": [
      {
        "@value": "John"
      }
    ], 
    "https://ogp.me/ns#type": [
      {
        "@value": "article"
      }
    ], 
    "http://ogp.me/ns/article#section": [
      {
        "@value": "Music"
      }
    ], 
    "http://ogp.me/ns/music#duration": [
      {
        "@value": "60"
      }
    ], 
    "http://ogp.me/ns/article#modified": [
      {
        "@value": "2016-12-15T06:19:30-05:00"
      }
    ], 
    "http://ogp.me/ns/video#tag": [
      {
        "@value": "Exhilerating"
      }
    ], 
    "https://ogp.me/ns#site_name": [
      {
        "@value": "Event Education"
      }
    ], 
    "http://ogp.me/ns/profile#last_name": [
      {
        "@value": "Lennon"
      }
    ], 
    "https://www.facebook.com/2008/fbmladmins": [
      {
        "@value": "himanshu160"
      }
    ], 
    "http://ogp.me/ns/article#section_url": [
      {
        "@value": "http://www.nytimes.com/section/arts"
      }
    ], 
    "https://ogp.me/ns#title": [
      {
        "@value": "From Street Theater to Wagner on the Opera Stage"
      }
    ], 
    "https://www.facebook.com/2008/fbmlapp_id": [
      {
        "@value": "9869919170"
      }
    ], 
    "https://ogp.me/ns#image": [
      {
        "@value": "https://www.eventeducation.com/images/982336_wedding_dayandouan_th.jpg"
      }
    ], 
    "http://ogp.me/ns/book#release_date": [
      {
        "@value": "2016-12-15T06:19:30-05:00"
      }
    ], 
    "http://ogp.me/ns/article#section-taxonomy-id": [
      {
        "@value": "C5BFA7D5-359C-427B-90E6-6B7245A6CDD8"
      }
    ], 
    "http://ogp.me/ns/article#published": [
      {
        "@value": "2016-12-15T05:55:55-05:00"
      }
    ], 
    "https://ogp.me/ns#description": [
      {
        "@value": "which he set in Bangladesh instead of Norway. The production opens in Madrid on Saturday."
      }
    ], 
    "@id": "http://www.example.com/index.html", 
    "http://ogp.me/ns/article#top-level-section": [
      {
        "@value": "arts"
      }
    ]
  }
]
```

### `tests/samples/misc/microformat_flat_test.json`

```json
[
    {
        "@type": [
            "h-hidden-phone",
            "h-hidden-tablet"
        ],
        "name": [
            ""
        ],
        "@context": "http://microformats.org/wiki/"
    },
    {
        "@type": [
            "h-hidden-phone"
        ],
        "@context": "http://microformats.org/wiki/",
        "children": [
            {
                "@type": [
                    "h-hidden-phone",
                    "h-hidden-tablet"
                ],
                "name": [
                    ""
                ]
            },
            {
                "@type": [
                    "h-hidden-phone"
                ],
                "name": [
                    "aJ Styles FastLane 2018 15 x 17 Framed Plaque w/ Ring Canvas"
                ],
                "photo": [
                    {
                        "alt": "aJ Styles FastLane 2018 15 x 17 Framed Plaque w/ Ring Canvas",
                        "value": "/on/demandware.static/-/Sites-main/default/dwa3227ee6/images/small/CN1148.jpg"
                    }
                ]
            }
        ]
    },
    {
        "name": [
            "Microformats are amazing"
        ],
        "@context": "http://microformats.org/wiki/",
        "@type": [
            "h-entry"
        ],
        "summary": [
            "In which I extoll the virtues of using microformats."
        ],
        "author": [
            {
                "@type": [
                    "h-card"
                ],
                "url": [
                    "http://example.com"
                ],
                "name": [
                    "W. Developer"
                ],
                "value": "W. Developer"
            }
        ],
        "content": [
            {
                "html": "<p>Blah blah blah</p>",
                "value": "Blah blah blah"
            }
        ],
        "published": [
            "2013-06-13 12:00:00"
        ]
    }
]

```

### `tests/samples/misc/microformat_test.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="https://www.w3.org/1999/xhtml" xmlns:og="https://ogp.me/ns#" xmlns:fb="https://www.facebook.com/2008/fbml">
<head>
<title>Himanshu's Open Graph Protocol</title>
<meta http-equiv="Content-Type" content="text/html;charset=WINDOWS-1252" />
<meta http-equiv="Content-Language" content="en-us" />
<link rel="stylesheet" type="text/css" href="event-education.css" />
<meta name="verify-v1" content="so4y/3aLT7/7bUUB9f6iVXN0tv8upRwaccek7JKB1gs=" >
<meta property="og:title" content="Himanshu's Open Graph Protocol"/>
<div class="h-hidden-tablet h-hidden-phone"></div>
	<div class="js-sticky-order b-header-pdp_sticky h-hidden-phone">
		<div class="g-grid-container">
			<div class="g-grid-row">
				<div class="g-grid-col-1 h-hidden-tablet h-hidden-phone"></div>
				<div class="g-grid-col-1 g-grid-col-2-tablet h-hidden-phone">
					<img src="/on/demandware.static/-/Sites-main/default/dwa3227ee6/images/small/CN1148.jpg" alt="aJ Styles FastLane 2018 15 x 17 Framed Plaque w/ Ring Canvas" />
				</div>
			</div>
		</div>
	</div>
<article class="h-entry">
  <h1 class="p-name">Microformats are amazing</h1>
  <p>Published by <a class="p-author h-card" href="http://example.com">W. Developer</a>
     on <time class="dt-published" datetime="2013-06-13 12:00:00">13<sup>th</sup> June 2013</time></p>
 
  <p class="p-summary">In which I extoll the virtues of using microformats.</p>
 
  <div class="e-content">
    <p>Blah blah blah</p>
  </div>
</article>

</head>

<body>

<div id="fb-root"></div>
<script>(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=501839739845103";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
.
.
.
</body>
</html>
```

### `tests/samples/misc/microformat_test.json`

```json
[
    {
        "properties": {
            "name": [
                ""
            ]
        },
        "type": [
            "h-hidden-phone",
            "h-hidden-tablet"
        ]
    },
    {
        "properties": {},
        "children": [
            {
                "properties": {
                    "name": [
                        ""
                    ]
                },
                "type": [
                    "h-hidden-phone",
                    "h-hidden-tablet"
                ]
            },
            {
                "properties": {
                    "photo": [
                        {
                            "alt": "aJ Styles FastLane 2018 15 x 17 Framed Plaque w/ Ring Canvas",
                            "value": "/on/demandware.static/-/Sites-main/default/dwa3227ee6/images/small/CN1148.jpg"

                        }
                    ],
                    "name": [
                        "aJ Styles FastLane 2018 15 x 17 Framed Plaque w/ Ring Canvas"
                    ]
                },
                "type": [
                    "h-hidden-phone"
                ]
            }
        ],
        "type": [
            "h-hidden-phone"
        ]
    },
    {
        "properties": {
            "author": [
                {
                    "properties": {
                        "url": [
                            "http://example.com"
                        ],
                        "name": [
                            "W. Developer"
                        ]
                    },
                    "value": "W. Developer",
                    "type": [
                        "h-card"
                    ]
                }
            ],
            "name": [
                "Microformats are amazing"
            ],
            "content": [
                {
                    "value": "Blah blah blah",
                    "html": "<p>Blah blah blah</p>"
                }
            ],
            "published": [
                "2013-06-13 12:00:00"
            ],
            "summary": [
                "In which I extoll the virtues of using microformats."
            ]
        },
        "type": [
            "h-entry"
        ]
    }
]

```

### `tests/samples/misc/null_ld_mock.html`

```html
<script type="application/ld+json">null</script><script type="application/ld+json">null</script><script type="application/ld+json">null</script><script type="application/ld+json">{"\u0040context":"http:\/\/schema.org","\u0040type":"LocalBusiness","name":"Some Name Goes Here","address":{"\u0040type":"PostalAddress","streetAddress":"123 Munroe Hwy","addressLocality":"Tacoma, Georgia","addressRegion":"Georgia","postalCode":"52342"},"aggregateRating":{"\u0040type":"AggregateRating","ratingValue":5,"ratingCount":280}}</script><script type="application/ld+json">null</script><script type="application/ld+json">null</script><script type="application/ld+json">{"\u0040context":"http:\/\/schema.org","\u0040type":"Review","name":"","reviewBody":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"}</script><script type="application/ld+json">null</script><script type="application/ld+json">null</script><script type="application/ld+json">null</script><script type="application/ld+json">null</script><script type="application/ld+json">null</script>
```

### `tests/samples/misc/null_ld_mock.jsonld`

```jsonld
[
  {
    "@context": "http://schema.org",
    "address": {
      "addressLocality": "Tacoma, Georgia",
      "addressRegion": "Georgia",
      "streetAddress": "123 Munroe Hwy",
      "postalCode": "52342",
      "@type": "PostalAddress"
    },
    "aggregateRating": {
      "ratingCount": 280,
      "@type": "AggregateRating",
      "ratingValue": 5
    },
    "@type": "LocalBusiness",
    "name": "Some Name Goes Here"
  },
  {
    "@context": "http://schema.org",
    "reviewBody": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?",
    "@type": "Review",
    "name": ""
  }
]
```

### `tests/samples/misc/opengraph_flat_test.json`

```json
[
    {
      "og:title": "Himanshu's Open Graph Protocol",
      "og:url": "https://www.eventeducation.com/test.php",
      "og:image": "https://www.eventeducation.com/images/982336_wedding_dayandouan_th.jpg",
      "og:site_name": "Event Education",
      "og:description": "Event Education provides free courses on event planning and management to event professionals worldwide.",
      "article:publisher": "http://www.facebook.com/PUBLISHER",
      "article:author": "http://facebook.com/AUTHOR",
      "article:published_time": "2012-04-04T19:50:00-07:00",
      "article:modified_time": "2016-12-13T12:35:52-07:00",
      "@type": "article",
      "@context": {
        "og": "http://ogp.me/ns#",
        "article": "http://ogp.me/ns/article#"
      }
    }
  ]
```

### `tests/samples/misc/opengraph_ns_product_test.json`

```json
[
    {
        "namespace": {
            "og": "http://ogp.me/ns#",
            "product": "http://ogp.me/ns/product#"
        },
        "properties": [
            [
                "og:type",
                "product.item"
            ],
            [
                "og:url",
                "https://www.fye.com/better-off-dead-exclusive-blu-ray-steelbook-fye.000000032429335302.html"
            ],
            [
                "og:title",
                "Better Off Dead [Exclusive Blu-ray Steelbook] - New on Blu-ray Disc | FYE"
            ],
            [
                "og:description",
                "Better Off Dead [Exclusive Blu-ray Steelbook] - 1980's classic starring John Cusack"
            ],
            [
                "og:image",
                "https://www.fye.com/dw/image/v2/BBNF_PRD/on/demandware.static/-/Sites-fye-master/default/dw74ad83df/fye/000/000000/fye.000000032429335302_0.jpg?sw=272"
            ],
            [
                "product:condition",
                "new"
            ],
            [
                "product:availability",
                "in stock"
            ],
            [
                "product:price:amount",
                "17.99"
            ],
            [
                "product:price:currency",
                "USD"
            ],
            [
                "product:retailer_item_id",
                "fye.000000032429335302"
            ],
            [
                "product:gtin",
                "32429335302"
            ]
        ]
    }
]

```

### `tests/samples/misc/opengraph_test.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="https://www.w3.org/1999/xhtml" xmlns:og="https://ogp.me/ns#" xmlns:fb="https://www.facebook.com/2008/fbml">
<head>
<title>Himanshu's Open Graph Protocol</title>
<meta http-equiv="Content-Type" content="text/html;charset=WINDOWS-1252" />
<meta http-equiv="Content-Language" content="en-us" />
<link rel="stylesheet" type="text/css" href="event-education.css" />
<meta name="verify-v1" content="so4y/3aLT7/7bUUB9f6iVXN0tv8upRwaccek7JKB1gs=" >
<meta property="og:title" content="Himanshu's Open Graph Protocol"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="https://www.eventeducation.com/test.php"/>
<meta property="og:image" content="https://www.eventeducation.com/images/982336_wedding_dayandouan_th.jpg"/>
<meta property="fb:admins" content="himanshu160"/>
<meta property="og:site_name" content="Event Education"/>
<meta property="og:description" content="Event Education provides free courses on event planning and management to event professionals worldwide."/>
<meta property="article:publisher" content="http://www.facebook.com/PUBLISHER" />
<meta property="article:author" content="http://facebook.com/AUTHOR" />
<meta property="article:published_time" content="2012-04-04T19:50:00-07:00" />
<meta property="article:modified_time" content="2016-12-13T12:35:52-07:00" />

</head>

<body>

<div id="fb-root"></div>
<script>(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=501839739845103";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
.
.
.
</body>
</html>

```

### `tests/samples/misc/opengraph_test.json`

```json
[
    {
        "namespace": {
            "og": "http://ogp.me/ns#",
            "article": "http://ogp.me/ns/article#"
        },
        "properties": [
            [
                "og:title",
                "Himanshu's Open Graph Protocol"
            ],
            [
                "og:type",
                "article"
            ],
            [
                "og:url",
                "https://www.eventeducation.com/test.php"
            ],
            [
                "og:image",
                "https://www.eventeducation.com/images/982336_wedding_dayandouan_th.jpg"
            ],
            [
                "og:site_name",
                "Event Education"
            ],
            [
                "og:description",
                "Event Education provides free courses on event planning and management to event professionals worldwide."
            ],
            [
                "article:publisher",
                "http://www.facebook.com/PUBLISHER"
            ],
            [
                "article:author",
                "http://facebook.com/AUTHOR"
            ],
            [
                "article:published_time",
                "2012-04-04T19:50:00-07:00"
            ],
            [
                "article:modified_time",
                "2016-12-13T12:35:52-07:00"
            ]
        ]
    }
]
```

### `tests/samples/misc/Portfolio_Niels_Lubberman.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML+RDFa 1.0//EN"
  "http://www.w3.org/MarkUp/DTD/xhtml-rdfa-1.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" version="XHTML+RDFa 1.0" dir="ltr"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:dc="http://purl.org/dc/terms/"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:og="http://ogp.me/ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:sioc="http://rdfs.org/sioc/ns#"
  xmlns:sioct="http://rdfs.org/sioc/types#"
  xmlns:skos="http://www.w3.org/2004/02/skos/core#"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema#">

<head profile="http://www.w3.org/1999/xhtml/vocab">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="Generator" content="Drupal 7 (http://drupal.org)" />
<link rel="alternate" type="application/rss+xml" title="Front page feed" href="http://nielslubberman.nl/drupal/?q=rss.xml" />
<link rel="shortcut icon" href="http://nielslubberman.nl/drupal/misc/favicon.ico" type="image/vnd.microsoft.icon" />
  <title>Portfolio Niels Lubberman</title>
  <style type="text/css" media="all">
@import url("http://nielslubberman.nl/drupal/modules/system/system.base.css?ophers");
@import url("http://nielslubberman.nl/drupal/modules/system/system.menus.css?ophers");
@import url("http://nielslubberman.nl/drupal/modules/system/system.messages.css?ophers");
@import url("http://nielslubberman.nl/drupal/modules/system/system.theme.css?ophers");
</style>
<style type="text/css" media="all">
@import url("http://nielslubberman.nl/drupal/modules/comment/comment.css?ophers");
@import url("http://nielslubberman.nl/drupal/modules/field/theme/field.css?ophers");
@import url("http://nielslubberman.nl/drupal/modules/node/node.css?ophers");
@import url("http://nielslubberman.nl/drupal/modules/search/search.css?ophers");
@import url("http://nielslubberman.nl/drupal/modules/user/user.css?ophers");
@import url("http://nielslubberman.nl/drupal/sites/all/modules/views/css/views.css?ophers");
</style>
<style type="text/css" media="all">
@import url("http://nielslubberman.nl/drupal/sites/all/modules/colorbox/styles/stockholmsyndrome/colorbox_style.css?ophers");
@import url("http://nielslubberman.nl/drupal/sites/all/modules/ctools/css/ctools.css?ophers");
</style>
<style type="text/css" media="all">
@import url("http://nielslubberman.nl/drupal/sites/all/themes/slideboard/css/slideboard.css?ophers");
</style>
  <script type="text/javascript" src="http://nielslubberman.nl/drupal/misc/jquery.js?v=1.4.4"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/misc/jquery.once.js?v=1.2"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/misc/drupal.js?ophers"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/libraries/colorbox/jquery.colorbox-min.js?ophers"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/modules/colorbox/js/colorbox.js?ophers"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/modules/colorbox/styles/stockholmsyndrome/colorbox_style.js?ophers"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/modules/google_analytics/googleanalytics.js?ophers"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
(function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create", "UA-29644360-2", {"cookieDomain":"auto"});ga("set", "anonymizeIp", true);ga("send", "pageview");
//--><!]]>
</script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/themes/slideboard/scripts/jquery.localscroll-1.2.7-min.js?ophers"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/themes/slideboard/scripts/jquery.parallax-1.1.3.js?ophers"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/themes/slideboard/scripts/jquery.scrollTo-1.4.2-min.js?ophers"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/themes/slideboard/scripts/jquery-scrolltofixed-min.js?ophers"></script>
<script type="text/javascript" src="http://nielslubberman.nl/drupal/sites/all/themes/slideboard/scripts/java_test_file.js?ophers"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
jQuery.extend(Drupal.settings, {"basePath":"\/drupal\/","pathPrefix":"","ajaxPageState":{"theme":"slideboard","theme_token":"O1ESK1AJ7OZncFtmVn4txgL6uMK4gLhSHmob9aqQoOY","js":{"misc\/jquery.js":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"sites\/all\/libraries\/colorbox\/jquery.colorbox-min.js":1,"sites\/all\/modules\/colorbox\/js\/colorbox.js":1,"sites\/all\/modules\/colorbox\/styles\/stockholmsyndrome\/colorbox_style.js":1,"sites\/all\/modules\/google_analytics\/googleanalytics.js":1,"0":1,"sites\/all\/themes\/slideboard\/scripts\/jquery.localscroll-1.2.7-min.js":1,"sites\/all\/themes\/slideboard\/scripts\/jquery.parallax-1.1.3.js":1,"sites\/all\/themes\/slideboard\/scripts\/jquery.scrollTo-1.4.2-min.js":1,"sites\/all\/themes\/slideboard\/scripts\/jquery-scrolltofixed-min.js":1,"sites\/all\/themes\/slideboard\/scripts\/java_test_file.js":1},"css":{"modules\/system\/system.base.css":1,"modules\/system\/system.menus.css":1,"modules\/system\/system.messages.css":1,"modules\/system\/system.theme.css":1,"modules\/comment\/comment.css":1,"modules\/field\/theme\/field.css":1,"modules\/node\/node.css":1,"modules\/search\/search.css":1,"modules\/user\/user.css":1,"sites\/all\/modules\/views\/css\/views.css":1,"sites\/all\/modules\/colorbox\/styles\/stockholmsyndrome\/colorbox_style.css":1,"sites\/all\/modules\/ctools\/css\/ctools.css":1,"sites\/all\/themes\/slideboard\/css\/slideboard.css":1}},"colorbox":{"opacity":"0.85","current":"{current} of {total}","previous":"\u00ab Prev","next":"Next \u00bb","close":"Close","maxWidth":"98%","maxHeight":"98%","fixed":true,"mobiledetect":true,"mobiledevicewidth":"480px"},"googleanalytics":{"trackOutbound":1,"trackMailto":1,"trackDownload":1,"trackDownloadExtensions":"7z|aac|arc|arj|asf|asx|avi|bin|csv|doc(x|m)?|dot(x|m)?|exe|flv|gif|gz|gzip|hqx|jar|jpe?g|js|mp(2|3|4|e?g)|mov(ie)?|msi|msp|pdf|phps|png|ppt(x|m)?|pot(x|m)?|pps(x|m)?|ppam|sld(x|m)?|thmx|qtm?|ra(m|r)?|sea|sit|tar|tgz|torrent|txt|wav|wma|wmv|wpd|xls(x|m|b)?|xlt(x|m)|xlam|xml|z|zip","trackColorbox":1}});
//--><!]]>
</script>
</head>
<body class="html front not-logged-in no-sidebars page-frontpage" >
  <div id="skip-link">
    <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
  </div>
    
	<div id="intro">
		
        			<div id="highlights">
				  <div class="region region-headlines">
    <div id="block-views-headlines-block-block" class="block block-views">

    
  <div class="content">
    <div class="view view-headlines-block view-id-headlines_block view-display-id-block view-dom-id-cd449804aa55c7e447cb71938d84aabc">
        
  
  
      <div class="view-content">
      <table class="views-view-grid cols-3">
  
  <tbody>
          <tr class="row-1 row-first row-last">
                  <td class="col-1 col-first">
            
<div class="highlight-box">
	<h1>LinkedIn</h1>					
	<p><div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even" property="content:encoded"><p>Voeg mij nu toe aan uw professionele netwerk op LinkedIn.</p>
</div></div></div><div class="field field-name-field-sticker field-type-image field-label-hidden"><div class="field-items"><div class="field-item even"><a href="https://www.linkedin.com/pub/niels-lubberman/4a/645/a30" target="_blank"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/images/headlines/headline_linkedin.png" width="121" height="119" alt="" /></a></div></div></div></p>
</div>
          </td>
                  <td class="col-2">
            
<div class="highlight-box">
	<h1>Een Nieuwe Website</h1>					
	<p><div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even" property="content:encoded"><p>Op deze vernieuwde website kunt u enkele van mijn projecten vinden, tevens kunt u lessen downloaden die ik heb gemaakt.</p>
</div></div></div></p>
</div>
          </td>
                  <td class="col-3 col-last">
            
<div class="highlight-box">
	<h1>Download mijn CV</h1>					
	<p><div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even" property="content:encoded"><p>Met behulp van de pijl hieronder kunt u mijn CV downloaden.</p>
</div></div></div><div class="field field-name-field-sticker field-type-image field-label-hidden"><div class="field-items"><div class="field-item even"><a href="http://www.nielslubberman.nl/drupal/sites/default/files/files/lessons/CV Niels Lubberman 2016.pdf" target="_blank"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/images/headlines/headline_download.png" width="120" height="119" alt="" /></a></div></div></div></p>
</div>
          </td>
              </tr>
      </tbody>
</table>
    </div>
  
  
  
  
  
  
</div>  </div>
</div>
  </div>
			</div>
				
	</div> <!--#intro-->

	<div id="nav-bar" class="sticky-navigation">
		<ul class="links"><li class="menu-198 first active"><a href="/drupal/#intro" title="" class="active">Home</a></li>
<li class="menu-911 active"><a href="/drupal/#second" title="" class="active">Lessen</a></li>
<li class="menu-912 active"><a href="/drupal/#stop-project" title="" class="active">Projecten</a></li>
<li class="menu-913 last active"><a href="/drupal/#footer" title="" class="active">Contact</a></li>
</ul>	</div> <!--#navigatie-bar-->
	
	<div id="second">
		<div class="container">
			<div id="lessons">
			
				<div id="logo-bckgrnd">
					<div id="logo-container">
						<img src="http://nielslubberman.nl/drupal/sites/all/themes/slideboard/logo.png" alt="Home">
					</div>
				</div>
								
				<br><br>
				
									<div class="message-container">
						  <div class="region region-newsflash">
    <div id="block-views-news-block" class="block block-views">

    
  <div class="content">
    <div class="view view-news view-id-news view-display-id-block view-dom-id-1122bc77a3c263464260e30e9ff346cd">
        
  
  
      <div class="view-content">
      <table class="views-view-grid cols-4">
  
  <tbody>
          <tr class="row-1 row-first row-last">
                  <td class="col-1 col-first">
              
  <div>        <h1>Nieuwe les - Heksenjacht!</h1>  </div>  
  <div>        <div><p>Kijk snel naar de nieuwe les over heksenprocessen. Veel mensen denken dat heksenjacht een typische middeleeuwse bezigheid was. Maar dit klopt toch echt niet. De meeste processen komen uit de 16de en 17de eeuw. In een tijd dat men juist kritischer ging nadenken over geloof, de wereld en de mens.</p>
</div>  </div>          </td>
              </tr>
      </tbody>
</table>
    </div>
  
  
  
  
  
  
</div>  </div>
</div>
  </div>
					</div>										
				
				<hr>

				  <div class="region region-content">
    <div id="block-system-main" class="block block-system">

    
  <div class="content">
    <div class="view view-frontpage view-id-frontpage view-display-id-page view-dom-id-ba067791ba266de80269b3540885d817">
        
  
  
      <div class="view-content">
      <table class="views-view-grid cols-4">
  
  <tbody>
          <tr class="row-1 row-first row-last">
                  <td class="col-1 col-first">
            

<div class="teaser-content-block">
	<div class="inner-teaser-block">
		<a href="/drupal/?q=node/19">De Skill Tree</a>		<p><p>Bij het voorbereiden van lessenseries denk ik veel na over de vraag hoe we meer rekening kunnen houden met de onderlinge verschillen tussen leerlingen en hoe we de motivatie van leerlingen positief kunnen beïnvloeden. Op basis van deze twee doelen ben ik begonnen met het experimenteren met een Skill Tree. Het idee is om leerlingen een instrument mee te geven, waarmee ze hun eigen leren kunnen meten en observeren. </p>
</p>
	</div>	
	<div class="return-slip">
		<span>
			<span>May 2017</span> | 
			<span>Reacties 0</span> | 
			<a href="/drupal/?q=taxonomy/term/1" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Geschiedenis</a>															
			
			<div class="return-slip-button">
				<a class="btnReadMore" href="/drupal/?q=node/19">Lees verder</a>
			</div>
		</span>
	</div>
</div>

          </td>
                  <td class="col-2">
            

<div class="teaser-content-block">
	<div class="inner-teaser-block">
		<a href="/drupal/?q=node/17">Heksenjacht!</a>		<p><p>Onbegrip over de acties van mensen in het verleden is een vrij veel voorkomend fenomeen bij leerlingen. Het is ook moeilijk om je in te leven in mensen die op een hele andere manier in het leven hebben gestaan dan zijzelf. Dat is ook de reden waarom we in de geschiedenisles vaak stilstaan bij standplaatsgebondenheid. </p>
</p>
	</div>	
	<div class="return-slip">
		<span>
			<span>Jan 2017</span> | 
			<span>Reacties 0</span> | 
			<a href="/drupal/?q=taxonomy/term/1" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Geschiedenis</a>															
			
			<div class="return-slip-button">
				<a class="btnReadMore" href="/drupal/?q=node/17">Lees verder</a>
			</div>
		</span>
	</div>
</div>

          </td>
                  <td class="col-3">
            

<div class="teaser-content-block">
	<div class="inner-teaser-block">
		<a href="/drupal/?q=node/16">Memento Mori</a>		<p><p>Hoe kan het dat we vandaag de dag andere waarden van belang vinden dan mensen uit andere tijden? Binnen deze les gaan leerlingen kijken naar het leven van een horige boer uit de tijd van Monniken en Ridders.</p>
</p>
	</div>	
	<div class="return-slip">
		<span>
			<span>May 2016</span> | 
			<span>Reacties 0</span> | 
			<a href="/drupal/?q=taxonomy/term/1" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Geschiedenis</a>															
			
			<div class="return-slip-button">
				<a class="btnReadMore" href="/drupal/?q=node/16">Lees verder</a>
			</div>
		</span>
	</div>
</div>

          </td>
                  <td class="col-4 col-last">
            

<div class="teaser-content-block">
	<div class="inner-teaser-block">
		<a href="/drupal/?q=node/15">In der Fuehrer&#039;s face</a>		<p><p>In de Eerste en Tweede Wereldoorlog hebben beide partijen propaganda ingezet. Het is belangrijk om leerlingen duidelijk te maken wat propaganda is. Propaganda is namelijk niet altijd even makkelijk te herkennen. Daarnaast is er altijd de vraag of propaganda gebruikt mag worden voor de “goede” zaak. In deze les gaan leerlingen deze vragen bestuderen aan de hand van een Disney filmpje.</p>
</p>
	</div>	
	<div class="return-slip">
		<span>
			<span>Apr 2016</span> | 
			<span>Reacties 0</span> | 
			<a href="/drupal/?q=taxonomy/term/1" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Geschiedenis</a>															
			
			<div class="return-slip-button">
				<a class="btnReadMore" href="/drupal/?q=node/15">Lees verder</a>
			</div>
		</span>
	</div>
</div>

          </td>
              </tr>
      </tbody>
</table>
    </div>
  
  
  
  
  
  
</div>  </div>
</div>
  </div>
	
				<div style="clear: both;"></div>

			</div>
		</div>
	</div> <!--#second-->
	
	<div id="third">
		<div id="project-bar">
		
			<div id="stop-project"><br><br><br></div>
			<nav>
				<ul>		
					  <div class="region region-project-menu">
    <div id="block-views-project-menu-block" class="block block-views">

    
  <div class="content">
    <div class="view view-project-menu view-id-project_menu view-display-id-block view-dom-id-78b6ea9b308e07e656bdea9871355bcd">
        
  
  
      <div class="view-content">
      <table class="views-view-grid cols-4">
  
  <tbody>
          <tr >
                  <td >
            
	<li><a href="#" class="style-project-items"><div><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/images/projects/grey_img_4.png" width="160" height="161" alt="" /></div></a>
		<ul>
			<li class="top"></li>
			<li class="bottom">
				<h2><span class="field-content">RU Secure</span></h2>
				<p><div>Dit project heb ik uitgevoerd in opdracht van de afdeling Biologische Veiligheid, Straling en Milieu van de Radboud Universiteit. Doel was om de bestaande cursus Veiligheid te voorzien van een nieuwe lay-out. </div></p>

				<div class="bottom-button-holder">
					<a id="btn-12" class="btnReadMore btnProject">Lees verder</a>
				</div>								
			</li>								
		</ul>
	</li>          </td>
                  <td >
            
	<li><a href="#" class="style-project-items"><div><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/images/projects/grey_img_3.png" width="160" height="161" alt="" /></div></a>
		<ul>
			<li class="top"></li>
			<li class="bottom">
				<h2><span class="field-content">Belangrijke Spelers uit de Computer geschiedenis</span></h2>
				<p><div>Vanuit de Informatica- en Mediawijsheid sectie werd er gevraagd om enkele posters om het lokaal aan te kleden. Als thema werd er gekozen om personen af te beelden die een belangrijke bijdrage hebben geleverd aan de ontwikkeling van de informatie- en communicatietechnologie. </div></p>

				<div class="bottom-button-holder">
					<a id="btn-11" class="btnReadMore btnProject">Lees verder</a>
				</div>								
			</li>								
		</ul>
	</li>          </td>
                  <td >
            
	<li><a href="#" class="style-project-items"><div><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/images/projects/grey_img_2.png" width="160" height="161" alt="" /></div></a>
		<ul>
			<li class="top"></li>
			<li class="bottom">
				<h2><span class="field-content">Natie en Racisme</span></h2>
				<p><div>Een project voor een werkcollege van de Radboud Universiteit over aspecten van de Politieke Geschiedenis.
</div></p>

				<div class="bottom-button-holder">
					<a id="btn-10" class="btnReadMore btnProject">Lees verder</a>
				</div>								
			</li>								
		</ul>
	</li>          </td>
                  <td >
            
	<li><a href="#" class="style-project-items"><div><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/images/projects/grey_img_1.png" width="160" height="161" alt="" /></div></a>
		<ul>
			<li class="top"></li>
			<li class="bottom">
				<h2><span class="field-content">Donau-Zwarte zeekanaal</span></h2>
				<p><div>Tijdens mijn studie heb ik een kort onderzoek gedaan naar het Donau-Zwarte zeekanaal. Dit kanaal, dat symbool stond voor de communistische droom, was een megalomaan project van de Roemeense dictator Ceauςescu en zijn voorganger Gheorghiu-Dej.</div></p>

				<div class="bottom-button-holder">
					<a id="btn-9" class="btnReadMore btnProject">Lees verder</a>
				</div>								
			</li>								
		</ul>
	</li>          </td>
              </tr>
      </tbody>
</table>
    </div>
  
  
  
  
  
  
</div>  </div>
</div>
  </div>
	
				</ul>
			</nav>
		</div>
		
		<div id="project-main">
			  <div class="region region-project-showroom">
    <div id="block-views-project-showroom-block" class="block block-views">

    
  <div class="content">
    <div class="view view-project-showroom view-id-project_showroom view-display-id-block view-dom-id-70b3d797535124cb4342f13f01c565a3">
        
  
  
      <div class="view-content">
      <table class="views-view-grid cols-4">
  
  <tbody>
          <tr class="row-1 row-first row-last">
                  <td class="col-1 col-first">
            

	<div class="project-content" id="project-content-btn-12">
		<div class="project-content-text">		
			<div class="project-content-image">
				<div class="field-content"><a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/pro_ru_secure.png" title="RU Secure" class="colorbox" data-colorbox-gallery="gallery-node-12-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;RU Secure&quot;, &quot;alt&quot;: &quot;Het nieuwe uitlerlijk van de veiligheidscursus van de Radboud Universiteit.&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_ru_secure.png?itok=2-xDWirb&amp;sc=67c0f518676aaf034a9215a0ec7e9e1e" width="100" height="100" alt="Het nieuwe uitlerlijk van de veiligheidscursus van de Radboud Universiteit." title="RU Secure" /></a></div>	
			</div>			

			<h2><span class="field-content">RU Secure</span></h2>
				<div><p>Bij deze opdrachten kwamen meerdere problemen kijken die elk om hun eigen oplossing vroegen. In plaats van te werken met behulp van <em>Adobe Photoshop</em> en <em>Illustrator</em> moest ik kiezen voor een programma waarin mensen die minder vaardig met een computer zijn ook hun weg kunnen vinden. Uiteindelijk viel de keuze op <em>Microsoft PowerPoint</em> omdat dit programma gebruiksvriendelijk is.<br /><br />
Onderdelen van de cursus moesten worden aangevuld, delen van de tekst heb ik geredigeerd en daarnaast heb ik delen vertaald naar het Engels. Het geheel moest vervolgens ingevoegd worden in een <em>Blackboard</em> omgeving.</p>
</div>										
		</div>			
	</div> <!-- End Project -->          </td>
                  <td class="col-2">
            

	<div class="project-content" id="project-content-btn-11">
		<div class="project-content-text">		
			<div class="project-content-image">
				<div class="field-content"><a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/pro_poster_jobs.png" title="Steve Jobs, de man achter Apple" class="colorbox" data-colorbox-gallery="gallery-node-11-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;Steve Jobs, de man achter Apple&quot;, &quot;alt&quot;: &quot;&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_jobs.png?itok=QUE2ZKFT&amp;sc=259cbe26e2b9c2489443d05fdcd3f824" width="100" height="100" alt="" title="Steve Jobs, de man achter Apple" /></a>  <a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/pro_poster_gates.png" title="Bill Gates, de oprichter van Microsoft" class="colorbox" data-colorbox-gallery="gallery-node-11-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;Bill Gates, de oprichter van Microsoft&quot;, &quot;alt&quot;: &quot;&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_gates.png?itok=sIwGJEG3&amp;sc=259cbe26e2b9c2489443d05fdcd3f824" width="100" height="100" alt="" title="Bill Gates, de oprichter van Microsoft" /></a>  <a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/pro_poster_turing.png" title="Alan Turing, vader van de moderne computer" class="colorbox" data-colorbox-gallery="gallery-node-11-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;Alan Turing, vader van de moderne computer&quot;, &quot;alt&quot;: &quot;&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_turing.png?itok=anlTc5N6&amp;sc=259cbe26e2b9c2489443d05fdcd3f824" width="100" height="100" alt="" title="Alan Turing, vader van de moderne computer" /></a>  <a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/pro_poster_tim_berners_lee.png" title="Tim Berners-Lee, architect van het Web" class="colorbox" data-colorbox-gallery="gallery-node-11-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;Tim Berners-Lee, architect van het Web&quot;, &quot;alt&quot;: &quot;&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_tim_berners_lee.png?itok=DghJBlqt&amp;sc=259cbe26e2b9c2489443d05fdcd3f824" width="100" height="100" alt="" title="Tim Berners-Lee, architect van het Web" /></a></div>	
			</div>			

			<h2><span class="field-content">Belangrijke Spelers uit de Computer geschiedenis</span></h2>
				<div><p>De keuze voor <em>Bill Gates</em> en <em>Steven Jobs</em> was logisch omdat dit personen zijn die naast hun bijdrage, ook een grote bekendheid genieten bij onze leerlingen. De andere twee personen zijn minder bekend. <em>Alan Turing</em> stond met zijn ideeën aan de basis van de moderne computer zoals we hem nu kennen. Tijdens de Tweede Wereldoorlog werkte hij voor de Britse regering en was hij verantwoordelijk voor het kraken van de geheime codes van de Duitsers. De laatste persoon is <em>Tim Berners-Lee</em>, de persoon die aan het begin staat van het <em>World Wide Web</em>. Hij is verantwoordelijk voor de infrastructuur en de protocollen die het mogelijk maken dat u momenteel deze webpagina kunt bezoeken.</p>
</div>										
		</div>			
	</div> <!-- End Project -->          </td>
                  <td class="col-3">
            

	<div class="project-content" id="project-content-btn-10">
		<div class="project-content-text">		
			<div class="project-content-image">
				<div class="field-content"><a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/pro_asppolgs_final.png" title="Natie en rascisme" class="colorbox" data-colorbox-gallery="gallery-node-10-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;Natie en rascisme&quot;, &quot;alt&quot;: &quot;&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_asppolgs_final.png?itok=apZpSYdS&amp;sc=7ade4b4c9baeea7a86bad48589f9649d" width="100" height="100" alt="" title="Natie en rascisme" /></a></div>	
			</div>			

			<h2><span class="field-content">Natie en Racisme</span></h2>
				<div><p>Op de <strong>Radboud Universiteit</strong> heb ik het vak <em>Aspecten van de Politieke Geschiedenis</em> gevolgd. Doel van dit vak was in de grote ideologische stromingen van de negentiende en twintigste eeuw te onderzoeken en duiden. Binnen dit vak kregen de studenten de opdracht om een poster te maken om een deel van de stof te visualiseren. In deze poster moesten wij de denkbeelden van een historisch figuur weergeven.<br /><br />
Ik ben aan de slag gegaan met een tekstfragment uit <em>Mein Kampf</em>, het boek waarin Adolf Hitler zijn ideeën uit de doeken deed. Binnen de poster geef ik enkele centrale begrippen weer die betrekking hebben op <strong>nationalisme</strong> en <strong>racisme</strong>. Ook in het kleurgebruik heb ik getracht de symboliek van de Nazi’s terug te laten komen. Zo gebruik ik voornamelijk rood en zwart, de kleuren die voor de Nationaalsocialisten bloed en bodem representeerde. Daarnaast is er een schema weergegeven dat gebruikt werd om de indeling Duitser en Jood te visualiseren.</p>
</div>										
		</div>			
	</div> <!-- End Project -->          </td>
                  <td class="col-4 col-last">
            

	<div class="project-content" id="project-content-btn-9">
		<div class="project-content-text">		
			<div class="project-content-image">
				<div class="field-content"><a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/1979%20Nicolae%20si%20Nicu%20Ceausescu%20la%20Canal.JPG" title="Inspectie bezoek van Ceaușescu" class="colorbox" data-colorbox-gallery="gallery-node-9-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;Inspectie bezoek van Ceaușescu&quot;, &quot;alt&quot;: &quot;&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/1979%20Nicolae%20si%20Nicu%20Ceausescu%20la%20Canal.JPG?itok=CYcBbx1w&amp;sc=3e5afd5e3e8746f6db8fb6f52a325372" width="100" height="100" alt="" title="Inspectie bezoek van Ceaușescu" /></a>  <a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/pro_kanaal.jpg" title="Propaganda tekening die ik heb verwerkt in de poster" class="colorbox" data-colorbox-gallery="gallery-node-9-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;Propaganda tekening die ik heb verwerkt in de poster&quot;, &quot;alt&quot;: &quot;&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_kanaal.jpg?itok=cV8u1cxa&amp;sc=b496d2d94d76a056d4e6efde1cfb2abe" width="100" height="100" alt="" title="Propaganda tekening die ik heb verwerkt in de poster" /></a>  <a href="http://nielslubberman.nl/drupal/sites/default/files/projects/pictures/pro_poster_roemenie.png" title="Poster gemaak in Illustrator" class="colorbox" data-colorbox-gallery="gallery-node-9-ny8GlDLGYQ4" data-cbox-img-attrs="{&quot;title&quot;: &quot;Poster gemaak in Illustrator&quot;, &quot;alt&quot;: &quot;&quot;}"><img typeof="foaf:Image" src="http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_roemenie.png?itok=pScuIyeN&amp;sc=363eea0a2ddd62c554241fc1fed1f3bc" width="100" height="100" alt="" title="Poster gemaak in Illustrator" /></a></div>	
			</div>			

			<h2><span class="field-content">Donau-Zwarte zeekanaal</span></h2>
				<div><p>In het kader van het vak <em>Staatsutopieën</em> heb ik en kort onderzoek gedaan naar het Donau-Zwarte zeekanaal. Dit kanaal, dat symbool stond voor de communistische droom, was een megalomaan project van de Roemeense dictator Nicolae Ceaușescu en zijn voorganger Gheorghe Gheorghiu-Dej.<br /><br />
De poster laat enkele thema’s zien die centraal staan bij de ideologie achter dit project. De kleur blauw staat voor de naam die het regime aan het kanaal gaf; de blauwe snelweg. Het rood in de poster representeert het communisme. In het wapen van de communistische republiek Roemenië staan verwijzingen naar de natuur en het landschap, maar ook naar de industriële voortuitgang in de vorm van een boortoren. De communistische leiders die verbonden waren met het project zijn eveneens terug te vinden. De titel van de poster, <em>Canalul Mortii</em>, was de bijnaam die de inwoners van Roemenië aan het kanaal gaven, in het Nederlands is dit te vertalen als <em>Kanaal van de dood</em>.</p>
</div>										
		</div>			
	</div> <!-- End Project -->          </td>
              </tr>
      </tbody>
</table>
    </div>
  
  
  
  
  
  
</div>  </div>
</div>
  </div>
		</div>	
	</div> <!--#third-->	
	
	<div id="footer">
		  <div class="region region-footer">
    <div id="block-block-1" class="block block-block">

    
  <div class="content">
    <div id="footer">
<div id="contact">
<div class="header-bckgrnd"></div>
<div class="story">
<h1>Contact</h1>
<p>Heeft u vragen of wilt u meer weten neem dan contact met mij op. U kunt mij natuurlijk mailen, daarnaast ben ik te vinden op LinkedIn, Youtube en u kunt ook mijn C.V. op deze website downloaden.</p>
<p><br /></p>
<div id="contact-img-container">
<a href="" title="E-Mail"><img src="../drupal/sites/default/files/images/contact/imgMail.png" height="60" width="60" /></a><a href="" title="Twitter"><img src="../drupal/sites/default/files/images/contact/imgTwitter.png" height="60" width="60" /></a><a href="" title="YouTube"><img src="../drupal/sites/default/files/images/contact/imgYouTube.png" height="60" width="60" /></a>
</div>
</div>
<!--.story--></div>
<!-- End #contact --></div>
<!-- End #footer -->  </div>
</div>
  </div>
	</div> <!-- End #footer -->

  </body>
</html>

```

### `tests/samples/misc/Portfolio_Niels_Lubberman.json`

```json
[
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_jobs.png?itok=QUE2ZKFT&sc=259cbe26e2b9c2489443d05fdcd3f824"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_kanaal.jpg?itok=cV8u1cxa&sc=b496d2d94d76a056d4e6efde1cfb2abe"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_asppolgs_final.png?itok=apZpSYdS&sc=7ade4b4c9baeea7a86bad48589f9649d"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_tim_berners_lee.png?itok=DghJBlqt&sc=259cbe26e2b9c2489443d05fdcd3f824"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_roemenie.png?itok=pScuIyeN&sc=363eea0a2ddd62c554241fc1fed1f3bc"
  },
  {
    "http://www.w3.org/1999/xhtml/vocab#icon": [
      {
        "@id": "http://nielslubberman.nl/drupal/misc/favicon.ico"
      }
    ],
    "http://purl.org/rss/1.0/modules/content/encoded": [
      {
        "@value": "<p xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:content=\"http://purl.org/rss/1.0/modules/content/\" xmlns:dc=\"http://purl.org/dc/terms/\" xmlns:foaf=\"http://xmlns.com/foaf/0.1/\" xmlns:og=\"http://ogp.me/ns#\" xmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\" xmlns:sioc=\"http://rdfs.org/sioc/ns#\" xmlns:sioct=\"http://rdfs.org/sioc/types#\" xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\">Op deze vernieuwde website kunt u enkele van mijn projecten vinden, tevens kunt u lessen downloaden die ik heb gemaakt.</p>\n\n",
        "@type": "http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral"
      },
      {
        "@value": "<p xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:content=\"http://purl.org/rss/1.0/modules/content/\" xmlns:dc=\"http://purl.org/dc/terms/\" xmlns:foaf=\"http://xmlns.com/foaf/0.1/\" xmlns:og=\"http://ogp.me/ns#\" xmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\" xmlns:sioc=\"http://rdfs.org/sioc/ns#\" xmlns:sioct=\"http://rdfs.org/sioc/types#\" xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\">Voeg mij nu toe aan uw professionele netwerk op LinkedIn.</p>\n\n",
        "@type": "http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral"
      },
      {
        "@value": "<p xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:content=\"http://purl.org/rss/1.0/modules/content/\" xmlns:dc=\"http://purl.org/dc/terms/\" xmlns:foaf=\"http://xmlns.com/foaf/0.1/\" xmlns:og=\"http://ogp.me/ns#\" xmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\" xmlns:sioc=\"http://rdfs.org/sioc/ns#\" xmlns:sioct=\"http://rdfs.org/sioc/types#\" xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\">Met behulp van de pijl hieronder kunt u mijn CV downloaden.</p>\n\n",
        "@type": "http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral"
      }
    ],
    "http://www.w3.org/1999/xhtml/vocab#alternate": [
      {
        "@id": "http://nielslubberman.nl/drupal/?q=rss.xml"
      }
    ],
    "@id": "http://nielslubberman.nl/drupal/"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/images/headlines/headline_linkedin.png"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/images/headlines/headline_download.png"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_turing.png?itok=anlTc5N6&sc=259cbe26e2b9c2489443d05fdcd3f824"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_ru_secure.png?itok=2-xDWirb&sc=67c0f518676aaf034a9215a0ec7e9e1e"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/1979%20Nicolae%20si%20Nicu%20Ceausescu%20la%20Canal.JPG?itok=CYcBbx1w&sc=3e5afd5e3e8746f6db8fb6f52a325372"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/images/projects/grey_img_1.png"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/styles/smallcrop/public/projects/pictures/pro_poster_gates.png?itok=sIwGJEG3&sc=259cbe26e2b9c2489443d05fdcd3f824"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/images/projects/grey_img_3.png"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/images/projects/grey_img_2.png"
  },
  {
    "http://www.w3.org/2004/02/skos/core#prefLabel": [
      {
        "@language": "en",
        "@value": "Geschiedenis"
      }
    ],
    "http://www.w3.org/2000/01/rdf-schema#label": [
      {
        "@language": "en",
        "@value": "Geschiedenis"
      }
    ],
    "@type": ["http://www.w3.org/2004/02/skos/core#Concept"],
    "@id": "http://nielslubberman.nl/drupal/?q=taxonomy/term/1"
  },
  {
    "@type": ["http://xmlns.com/foaf/0.1/Image"],
    "@id": "http://nielslubberman.nl/drupal/sites/default/files/images/projects/grey_img_4.png"
  }
]


```

### `tests/samples/misc/product_microdata.html`

```html
<div itemscope itemtype="http://schema.org/Product">
  <span itemprop="brand">ACME</span>
  <span itemprop="name">Executive Anvil</span>
  <img itemprop="image" src="anvil_executive.jpg" alt="Executive Anvil logo" />
  <span itemprop="description">Sleeker than ACME's Classic Anvil, the
    Executive Anvil is perfect for the business traveler
    looking for something to drop from a height.
  </span>
  Product #: <span itemprop="mpn">925872</span>
  <span itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating">
    <span itemprop="ratingValue">4.4</span> stars, based on <span itemprop="reviewCount">89
      </span> reviews
  </span>

  <span itemprop="offers" itemscope itemtype="http://schema.org/Offer">
    Regular price: $179.99
    <meta itemprop="priceCurrency" content="USD" />
    $<span itemprop="price">119.99</span>
    (Sale ends <time itemprop="priceValidUntil" datetime="2020-11-05">
      5 November!</time>)
    Available from: <span itemprop="seller" itemscope itemtype="http://schema.org/Organization">
                      <span itemprop="name">Executive Objects</span>
                    </span>
    Condition: <link itemprop="itemCondition" href="http://schema.org/UsedCondition"/>Previously owned,
      in excellent condition
    <link itemprop="availability" href="http://schema.org/InStock"/>In stock! Order now!
  </span>
</div>

```

### `tests/samples/schema.org.invalid/AllocateAction.001.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- AllocateAction</title>
</head>

<body>
<script type="application/ld+json">
  // John allocated 5 hours to exercise.
{
  "@context": "http://schema.org",
  "@type": "AllocateAction",
  "agent": {
    "@type": "Person",
    "name": "John"
  },
  "object": {
    "@type": "Duration",
    "name": "5 hours"
  },
  "purpose": {
    "@type": "ExercisePlan",
    "name": "John's weight loss plan"
  }
}
</script>
</body>

</html>

```

### `tests/samples/schema.org.invalid/AllocateAction.001.jsonld`

```jsonld
[
    {
      "@context": "http://schema.org",
      "@type": "AllocateAction",
      "agent": {
        "@type": "Person",
        "name": "John"
      },
      "object": {
        "@type": "Duration",
        "name": "5 hours"
      },
      "purpose": {
        "@type": "ExercisePlan",
        "name": "John's weight loss plan"
      }
    }
]

```

### `tests/samples/schema.org.invalid/JoinAction.001.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- JoinAction</title>
</head>

<body>
<script type="application/ld+json">
<!-- John joined the festival. -->
{
  "@context": "http://schema.org",
  "@type": "JoinAction",
  "agent": {
    "@type": "Person",
    "name": "John"
  },
  "event": {
    "@type": "Festival",
    "name": "Woodstock"
  }
}
</script>
</body>

</html>

```

### `tests/samples/schema.org.invalid/JoinAction.001.jsonld`

```jsonld
[
    {
        "@type": "JoinAction",
        "@context": "http://schema.org",
        "agent": {"name": "John", "@type": "Person"},
        "event": {"name": "Woodstock", "@type": "Festival"}
    }
]

```

### `tests/samples/schema.org/CreativeWork_flat_with_node_id.001.json`

```json
{
  "microdata": [
    {
      "_nodeId_": "book1",
      "@type": "Book",
      "@context": "http://schema.org",
      "id": "http://worldcat.org/entity/work/id/2292573321",
      "name": "Rouge et le noir",
      "inLanguage": "fr",
      "workTranslation": {
        "_nodeId_": "creativeWork1",
        "@type": "CreativeWork",
        "id": "http://worldcat.org/entity/work/id/460647",
        "value": "Red and Black : A New Translation, Backgrounds and Sources, Criticism"
        }
      },
    {
      "_nodeId_": "author1",
      "@type": "Person",
      "@context": "http://schema.org",
      "id": "http://viaf.org/viaf/17823",
      "value": "Stendhal"
    },
    {
      "_nodeId_": "book2",
      "@type": "Book",
      "@context": "http://schema.org",
      "id": "http://worldcat.org/entity/work/id/460647",
      "name": "Red and Black : A New Translation, Backgrounds and Sources, Criticism",
      "author": {
        "_nodeId_": "author2",
        "@type": "Person",
        "id": "http://viaf.org/viaf/17823",
        "value": "Stendhal"
      },
      "inLanguage": "en",
      "about": "Psychological fiction, French",
      "translationOfWork": {
        "_nodeId_": "creativeWork2",
        "@type": "CreativeWork",
        "id": "http://worldcat.org/entity/work/id/2292573321",
        "value": "Rouge et le noir"
        }
      },
    {
      "_nodeId_": "translator2",
      "@type": "Person",
      "@context": "http://schema.org",
      "id": "http://viaf.org/viaf/8453420",
      "value": "Robert Martin Adams"
    }
  ],
  "json-ld": [
    {
      "@context": "http://schema.org",
      "@type": "WebPage",
      "breadcrumb": "Books > Literature & Fiction > Classics",
      "mainEntity": {
        "@type": "Book",
        "author": "/author/jd_salinger.html",
        "bookFormat": "http://schema.org/Paperback",
        "datePublished": "1991-05-01",
        "image": "catcher-in-the-rye-book-cover.jpg",
        "inLanguage": "English",
        "isbn": "0316769487",
        "name": "The Catcher in the Rye",
        "numberOfPages": "224",
        "offers": {
          "@type": "Offer",
          "availability": "http://schema.org/InStock",
          "price": "6.99",
          "priceCurrency": "USD"
        },
        "publisher": "Little, Brown, and Company",
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4",
          "reviewCount": "3077"
        },
        "review": [
          {
            "@type": "Review",
            "author": "John Doe",
            "datePublished": "2006-05-04",
            "name": "A masterpiece of literature",
            "reviewBody": "I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.",
            "reviewRating": {
              "@type": "Rating",
              "ratingValue": "5"
            }
          },
          {
            "@type": "Review",
            "author": "Bob Smith",
            "datePublished": "2006-06-15",
            "name": "A good read.",
            "reviewBody": "Catcher in the Rye is a fun book. It's a good book to read.",
            "reviewRating": "4"
          }
        ]
      }
    }
  ],
  "opengraph": [],
  "microformat": [],
  "rdfa": []
}

```

### `tests/samples/schema.org/CreativeWork_flat.001.json`

```json
{
  "microdata": [
    {
      "@type": "Book",
      "@context": "http://schema.org",
      "id": "http://worldcat.org/entity/work/id/2292573321",
      "name": "Rouge et le noir",
      "inLanguage": "fr",
      "workTranslation": {
        "@type": "CreativeWork",
        "id": "http://worldcat.org/entity/work/id/460647",
        "value": "Red and Black : A New Translation, Backgrounds and Sources, Criticism"
        }
      },
    {
      "@type": "Person",
      "@context": "http://schema.org",
      "id": "http://viaf.org/viaf/17823",
      "value": "Stendhal"
    },
    {
      "@type": "Book",
      "@context": "http://schema.org",
      "id": "http://worldcat.org/entity/work/id/460647",
      "name": "Red and Black : A New Translation, Backgrounds and Sources, Criticism",
      "author": {
        "@type": "Person",
        "id": "http://viaf.org/viaf/17823",
        "value": "Stendhal"
      },
      "inLanguage": "en",
      "about": "Psychological fiction, French",
      "translationOfWork": {
        "@type": "CreativeWork",
        "id": "http://worldcat.org/entity/work/id/2292573321",
        "value": "Rouge et le noir"
        }
      },
    {
      "@type": "Person",
      "@context": "http://schema.org",
      "id": "http://viaf.org/viaf/8453420",
      "value": "Robert Martin Adams"
    }
  ],
  "json-ld": [
    {
      "@context": "http://schema.org",
      "@type": "WebPage",
      "breadcrumb": "Books > Literature & Fiction > Classics",
      "mainEntity": {
        "@type": "Book",
        "author": "/author/jd_salinger.html",
        "bookFormat": "http://schema.org/Paperback",
        "datePublished": "1991-05-01",
        "image": "catcher-in-the-rye-book-cover.jpg",
        "inLanguage": "English",
        "isbn": "0316769487",
        "name": "The Catcher in the Rye",
        "numberOfPages": "224",
        "offers": {
          "@type": "Offer",
          "availability": "http://schema.org/InStock",
          "price": "6.99",
          "priceCurrency": "USD"
        },
        "publisher": "Little, Brown, and Company",
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4",
          "reviewCount": "3077"
        },
        "review": [
          {
            "@type": "Review",
            "author": "John Doe",
            "datePublished": "2006-05-04",
            "name": "A masterpiece of literature",
            "reviewBody": "I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.",
            "reviewRating": {
              "@type": "Rating",
              "ratingValue": "5"
            }
          },
          {
            "@type": "Review",
            "author": "Bob Smith",
            "datePublished": "2006-06-15",
            "name": "A good read.",
            "reviewBody": "Catcher in the Rye is a fun book. It's a good book to read.",
            "reviewRating": "4"
          }
        ]
      }
    }
  ],
  "opengraph": [],
  "microformat": [],
  "rdfa": []
}

```

### `tests/samples/schema.org/CreativeWork.001.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "WebPage",
  "breadcrumb": "Books > Literature & Fiction > Classics",
  "mainEntity":{
          "@type": "Book",
          "author": "/author/jd_salinger.html",
          "bookFormat": "http://schema.org/Paperback",
          "datePublished": "1991-05-01",
          "image": "catcher-in-the-rye-book-cover.jpg",
          "inLanguage": "English",
          "isbn": "0316769487",
          "name": "The Catcher in the Rye",
          "numberOfPages": "224",
          "offers": {
            "@type": "Offer",
            "availability": "http://schema.org/InStock",
            "price": "6.99",
            "priceCurrency": "USD"
          },
          "publisher": "Little, Brown, and Company",
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4",
            "reviewCount": "3077"
          },
          "review": [
            {
              "@type": "Review",
              "author": "John Doe",
              "datePublished": "2006-05-04",
              "name": "A masterpiece of literature",
              "reviewBody": "I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.",
              "reviewRating": {
            "@type": "Rating",
            "ratingValue": "5"
           }
            },
            {
              "@type": "Review",
              "author": "Bob Smith",
              "datePublished": "2006-06-15",
              "name": "A good read.",
              "reviewBody": "Catcher in the Rye is a fun book. It's a good book to read.",
              "reviewRating": "4"
            }
          ]
        }
}
</script>
<div>
<div id="book1" itemscope itemtype="http://schema.org/Book" itemid="http://worldcat.org/entity/work/id/2292573321">
        <h1><span itemprop="name">Rouge et le noir</span></h1>
    <div>Author: <span id="author1" property="itemprop" itemscope itemtype="http://schema.org/Person" itemid="http://viaf.org/viaf/17823">Stendhal</span></div>
        <div>Language: <span itemprop="inLanguage" content="fr">French</span></div>
        <div>Has Translation: <span id="creativeWork1" itemprop="workTranslation" itemscope itemtype="http://schema.org/CreativeWork" itemid="http://worldcat.org/entity/work/id/460647">Red and Black : A New Translation, Backgrounds and Sources, Criticism</span></div>
</div>
<div id="book2" itemscope itemtype="http://schema.org/Book" itemid="http://worldcat.org/entity/work/id/460647">
    <h1><span itemprop="name">Red and Black : A New Translation, Backgrounds and Sources, Criticism</span></h1>
    <div>Author: <span id="author2" itemprop="author" itemscope itemtype="http://schema.org/Person" itemid="http://viaf.org/viaf/17823">Stendhal</span></div>
        <div>Language: <span itemprop="inLanguage" content="en">English</span></div>
        <div>Subject: <span itemprop="about">Psychological fiction, French</span></div>
        <div>Translation of: <span id="creativeWork2" itemprop="translationOfWork" itemscope itemtype="http://schema.org/CreativeWork" itemid="http://worldcat.org/entity/work/id/2292573321">Rouge et le noir</span></div>
        <div>Translator: <span id="translator2" property="itemprop" itemscope itemtype="http://schema.org/Person" itemid="http://viaf.org/viaf/8453420">Robert Martin Adams</span></div>
</div>
</div>
</body>

</html>

```

### `tests/samples/schema.org/CreativeWork.001.json`

```json
[
 {"id": "http://worldcat.org/entity/work/id/2292573321",
  "properties": {"inLanguage": "fr",
                 "name": "Rouge et le noir",
                 "workTranslation": {"id": "http://worldcat.org/entity/work/id/460647",
                                     "type": "http://schema.org/CreativeWork",
                                     "value": "Red and Black : A New Translation, Backgrounds and Sources, Criticism"}},
  "type": "http://schema.org/Book"},
 {"id": "http://viaf.org/viaf/17823",
  "type": "http://schema.org/Person",
  "value": "Stendhal"},
 {"id": "http://worldcat.org/entity/work/id/460647",
  "properties": {"about": "Psychological fiction, French",
                 "author": {"id": "http://viaf.org/viaf/17823",
                            "type": "http://schema.org/Person",
                            "value": "Stendhal"},
                 "inLanguage": "en",
                 "name": "Red and Black : A New Translation, Backgrounds and Sources, Criticism",
                 "translationOfWork": {"id": "http://worldcat.org/entity/work/id/2292573321",
                                       "type": "http://schema.org/CreativeWork",
                                       "value": "Rouge et le noir"}},
  "type": "http://schema.org/Book"},
 {"id": "http://viaf.org/viaf/8453420",
  "type": "http://schema.org/Person",
  "value": "Robert Martin Adams"}
]

```

### `tests/samples/schema.org/CreativeWork.001.jsonld`

```jsonld
[
    {
      "@context": "http://schema.org",
      "@type": "WebPage",
      "breadcrumb": "Books > Literature & Fiction > Classics",
      "mainEntity":{
              "@type": "Book",
              "author": "/author/jd_salinger.html",
              "bookFormat": "http://schema.org/Paperback",
              "datePublished": "1991-05-01",
              "image": "catcher-in-the-rye-book-cover.jpg",
              "inLanguage": "English",
              "isbn": "0316769487",
              "name": "The Catcher in the Rye",
              "numberOfPages": "224",
              "offers": {
                "@type": "Offer",
                "availability": "http://schema.org/InStock",
                "price": "6.99",
                "priceCurrency": "USD"
              },
              "publisher": "Little, Brown, and Company",
              "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4",
                "reviewCount": "3077"
              },
              "review": [
                {
                  "@type": "Review",
                  "author": "John Doe",
                  "datePublished": "2006-05-04",
                  "name": "A masterpiece of literature",
                  "reviewBody": "I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.",
                  "reviewRating": {
                "@type": "Rating",
                "ratingValue": "5"
               }
                },
                {
                  "@type": "Review",
                  "author": "Bob Smith",
                  "datePublished": "2006-06-15",
                  "name": "A good read.",
                  "reviewBody": "Catcher in the Rye is a fun book. It's a good book to read.",
                  "reviewRating": "4"
                }
              ]
            }
    }
]

```

### `tests/samples/schema.org/Event.001.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>

<div itemscope itemtype="http://schema.org/Event">
  <a itemprop="url" href="nba-miami-philidelphia-game3.html">
  NBA Eastern Conference First Round Playoff Tickets:
  <span itemprop="name"> Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </span>
  </a>
  <meta itemprop="startDate" content="2016-04-21T20:00">
    Thu, 04/21/16
    8:00 p.m.
  <div itemprop="location" itemscope itemtype="http://schema.org/Place">
    <a itemprop="url" href="wells-fargo-center.html">
    Wells Fargo Center
    </a>
    <div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
      <span itemprop="addressLocality">Philadelphia</span>,
      <span itemprop="addressRegion">PA</span>
    </div>
  </div>
  <div itemprop="offers" itemscope itemtype="http://schema.org/AggregateOffer">
    Priced from: <span itemprop="lowPrice">$35</span>
    <span itemprop="offerCount">1938</span> tickets left
  </div>
</div>

</body>

</html>

```

### `tests/samples/schema.org/Event.001.json`

```json
[{"properties": {"location": {"properties": {"address": {"properties": {"addressLocality": "Philadelphia",
                                                                        "addressRegion": "PA"},
                                                         "type": "http://schema.org/PostalAddress"},
                                             "url": "wells-fargo-center.html"},
                              "type": "http://schema.org/Place"},
                 "name": "Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1)",
                 "offers": {"properties": {"lowPrice": "$35",
                                           "offerCount": "1938"},
                            "type": "http://schema.org/AggregateOffer"},
                 "startDate": "2016-04-21T20:00",
                 "url": "nba-miami-philidelphia-game3.html"},
  "type": "http://schema.org/Event"}]

```

### `tests/samples/schema.org/Event.002.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>

<div itemscope itemtype="http://schema.org/MusicGroup">
<h1 itemprop="name">Foo Fighters</h1>
<div itemprop="video" itemscope itemtype="http://schema.org/VideoObject">
  <h2>Video: <span itemprop="name">Interview with the Foo Fighters</span></h2>
  <meta itemprop="duration" content="T1M33S" />
  <meta itemprop="thumbnail" content="foo-fighters-interview-thumb.jpg" />
  <object ...>
    <param ...>
    <embed type="application/x-shockwave-flash" ...>
  </object>
  <span itemprop="description">Catch this exclusive interview with
    Dave Grohl and the Foo Fighters about their new album, Rope.</span>
</div>
<h2>Songs</h2>
<div itemprop="track" itemscope itemtype="http://schema.org/MusicRecording">
  <span itemprop="name">Rope</span>
  <meta itemprop="url" content ="foo-fighters-rope.html">
  Length: <meta itemprop="duration" content="PT4M5S">4:05 -
  14300 plays
  <div itemprop="interactionCount" itemscope itemtype="http://schema.org/InteractionCounter">
    <meta itemprop="interactionType" content="http://schema.org/ListenAction" />
    <meta itemprop="userInteractionCount" content="14300" />
  </div>
  <a href="foo-fighters-rope-play.html" itemprop="audio">Play</a>
  <a href="foo-fighters-rope-buy.html" itemprop="offers">Buy</a>
  From album: <a href="foo-fighters-wasting-light.html"
    itemprop="inAlbum">Wasting Light</a>
</div>
<div itemprop="track" itemscope itemtype="http://schema.org/MusicRecording">
  <span itemprop="name">Everlong</span>
  <meta itemprop="url" content ="foo-fighters-everlong.html">
  Length: <meta itemprop="duration" content="PT6M33S">6:33 -
  11700 plays
  <div itemprop="interactionCount" itemscope itemtype="http://schema.org/InteractionCounter">
    <meta itemprop="interactionType" content="http://schema.org/ListenAction" />
    <meta itemprop="userInteractionCount" content="11700" />
  </div>
  <a href="foo-fighters-everlong-play.html" itemprop="audio">Play</a>
  <a href="foo-fighters-everlong-buy.html" itemprop="offers">Buy</a>
  From album: <a href="foo-fighters-color-and-shape.html"
    itemprop="inAlbum">The Color And The Shape</a>
</div>
<h2>Upcoming shows</h2>
<div itemprop="event" itemscope itemtype="http://schema.org/Event">
  <a href="foo-fighters-may20-fedexforum" itemprop="url">
    <span itemprop="name">FedExForum</span>
  </a>
  <span itemprop="location">Memphis, TN, US</span>
  <meta itemprop="startDate" content="2011-05-20">May 20
  <a href="ticketmaster.com/foofighters/may20-2011" itemprop="offers">Buy tickets</a>
</div>
<div itemprop="event" itemscope itemtype="http://schema.org/Event">
  <a href="foo-fighters-may23-midamericacenter" itemprop="url">
    <span itemprop="name">Mid America Center</span>
  </a>
  <span itemprop="location">Council Bluffs, IA, US</span>
  <meta itemprop="startDate" content="2011-05-23">May 23
  <a href="ticketmaster.com/foofighters/may23-2011" itemprop="offers">Buy tickets</a>
</div>
<h2><a href="foo-fighters-photos">28 Photos</a></h2>
<a href="foofighters-1.jpg" itemprop="image"><img
alt="Thumbnail and linked photo of Foo Fighters band"
src="foofighters-thumb1.jpg" /></a>
<a href="foofighters-2.jpg" itemprop="image"><img
alt="Thumbnail and linked photo of Foo Fighters band"
src="foofighters-thumb2.jpg" /></a>
<a href="foofighters-3.jpg" itemprop="image"><img
alt="Thumbnail and linked photo of Foo Fighters band"
src="foofighters-thumb3.jpg" /></a>
<h2>Comments:</h2>
Excited about seeing them in concert next week. -Lawrence , Jan 23
I dig their latest single. -Mary, Jan 19
<div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
  <meta itemprop="interactionType" content="http://schema.org/CommentAction" />
  <meta itemprop="userInteractionCount" content="18" />
</div>
Showing 1-2 of 18 comments. <a href="foofighters-comments">More</a>
</div>

</body>

</html>

```

### `tests/samples/schema.org/Event.002.json`

```json
[{"properties": {"event": [{"properties": {"location": "Memphis, TN, US",
                                           "name": "FedExForum",
                                           "offers": "ticketmaster.com/foofighters/may20-2011",
                                           "startDate": "2011-05-20",
                                           "url": "foo-fighters-may20-fedexforum"},
                            "type": "http://schema.org/Event"},
                           {"properties": {"location": "Council Bluffs, IA, US",
                                           "name": "Mid America Center",
                                           "offers": "ticketmaster.com/foofighters/may23-2011",
                                           "startDate": "2011-05-23",
                                           "url": "foo-fighters-may23-midamericacenter"},
                            "type": "http://schema.org/Event"}],
                 "image": ["foofighters-1.jpg",
                           "foofighters-2.jpg",
                           "foofighters-3.jpg"],
                 "interactionStatistic": {"properties": {"interactionType": "http://schema.org/CommentAction",
                                                         "userInteractionCount": "18"},
                                          "type": "http://schema.org/InteractionCounter"},
                 "name": "Foo Fighters",
                 "track": [{"properties": {"audio": "foo-fighters-rope-play.html",
                                           "duration": "PT4M5S",
                                           "inAlbum": "foo-fighters-wasting-light.html",
                                           "interactionCount": {"properties": {"interactionType": "http://schema.org/ListenAction",
                                                                               "userInteractionCount": "14300"},
                                                                "type": "http://schema.org/InteractionCounter"},
                                           "name": "Rope",
                                           "offers": "foo-fighters-rope-buy.html",
                                           "url": "foo-fighters-rope.html"},
                            "type": "http://schema.org/MusicRecording"},
                           {"properties": {"audio": "foo-fighters-everlong-play.html",
                                           "duration": "PT6M33S",
                                           "inAlbum": "foo-fighters-color-and-shape.html",
                                           "interactionCount": {"properties": {"interactionType": "http://schema.org/ListenAction",
                                                                               "userInteractionCount": "11700"},
                                                                "type": "http://schema.org/InteractionCounter"},
                                           "name": "Everlong",
                                           "offers": "foo-fighters-everlong-buy.html",
                                           "url": "foo-fighters-everlong.html"},
                            "type": "http://schema.org/MusicRecording"}],
                 "video": {"properties": {"description": "Catch this exclusive interview with Dave Grohl and the Foo Fighters about their new album, Rope.",
                                           "duration": "T1M33S",
                                           "name": "Interview with the Foo Fighters",
                                           "thumbnail": "foo-fighters-interview-thumb.jpg"},
                            "type": "http://schema.org/VideoObject"}},
   "type": "http://schema.org/MusicGroup"}]

```

### `tests/samples/schema.org/Event.003.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>

<div class="event-wrapper" itemscope itemtype="http://schema.org/Event">
  <div class="event-date" itemprop="startDate" content="2013-09-14T21:30">Sat Sep 14</div>
  <div class="event-title" itemprop="name">Typhoon with Radiation City</div>
  <div class="event-venue" itemprop="location" itemscope itemtype="http://schema.org/Place">
    <span itemprop="name">The Hi-Dive</span>
    <div class="address" itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
      <span itemprop="streetAddress">7 S. Broadway</span><br>
      <span itemprop="addressLocality">Denver</span>,
      <span itemprop="addressRegion">CO</span>
      <span itemprop="postalCode">80209</span>
    </div>
  </div>
  <div class="event-time">9:30 PM</div>
 <span itemprop="offers" itemscope itemtype="http://schema.org/Offer">
  <div class="event-price" itemprop="price" content="13.00">$13.00</div>
  <span itemprop="priceCurrency" content="USD" />
  <a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>
 </span>
</div>

</body>

</html>

```

### `tests/samples/schema.org/Event.003.json`

```json
[
 {"properties": {"location": {"properties": {"address": {"properties": {"addressLocality": "Denver",
                                                                        "addressRegion": "CO",
                                                                        "postalCode": "80209",
                                                                        "streetAddress": "7 S. Broadway"},
                                                         "type": "http://schema.org/PostalAddress"},
                                             "name": "The Hi-Dive"},
                              "type": "http://schema.org/Place"},
                 "name": "Typhoon with Radiation City",
                 "offers": {"properties": {"price": "13.00",
                                           "priceCurrency": "USD",
                                           "url": "http://www.ticketfly.com/purchase/309433"},
                            "type": "http://schema.org/Offer"},
                 "startDate": "2013-09-14T21:30"},
  "type": "http://schema.org/Event"}
]

```

### `tests/samples/schema.org/Event.004.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>

<div class="event-wrapper" itemscope itemtype="http://schema.org/Event">
  <div class="event-date" itemprop="startDate" content="2013-09-14T21:30">Sat Sep 14</div>
  <div class="event-title" itemprop="name">CANCELLED - Typhoon with Radiation City</div>
  <meta itemprop="eventStatus" content="http://schema.org/EventCancelled">
  <div class="event-venue" itemprop="location" itemscope itemtype="http://schema.org/Place">
    <span itemprop="name">The Hi-Dive</span>
    <div class="address" itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
      <span itemprop="streetAddress">7 S. Broadway</span><br>
      <span itemprop="addressLocality">Denver</span>,
      <span itemprop="addressRegion">CO</span>
      <span itemprop="postalCode">80209</span>
    </div>
  </div>
  <div class="event-time">9:30 PM</div>
 <span itemprop="offers" itemscope itemtype="http://schema.org/Offer">
  <div class="event-price" itemprop="price" content="13.00">$13.00</div>
  <span itemprop="priceCurrency" content="USD" />
  <a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a>
 </span>
</div>

</body>

</html>

```

### `tests/samples/schema.org/Event.004.json`

```json
[
 {"properties": {"eventStatus": "http://schema.org/EventCancelled",
                  "location": {"properties": {"address": {"properties": {"addressLocality": "Denver",
                                                                         "addressRegion": "CO",
                                                                         "postalCode": "80209",
                                                                         "streetAddress": "7 S. Broadway"},
                                                          "type": "http://schema.org/PostalAddress"},
                                              "name": "The Hi-Dive"},
                               "type": "http://schema.org/Place"},
                  "name": "CANCELLED - Typhoon with Radiation City",
                  "offers": {"properties": {"price": "13.00",
                                            "priceCurrency": "USD",
                                            "url": "http://www.ticketfly.com/purchase/309433"},
                             "type": "http://schema.org/Offer"},
                  "startDate": "2013-09-14T21:30"},
   "type": "http://schema.org/Event"}
]


```

### `tests/samples/schema.org/Event.008.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>

<div itemscope="" itemtype="http://schema.org/TheaterEvent">
  <span itemprop="name">Julius Caesar at Shakespeare's Globe</span>
  <div itemprop="location" itemscope="" itemtype="http://schema.org/PerformingArtsTheater">
    <meta itemprop="name" content="Shakespeare's Globe"/>
    <link itemprop="sameAs" href="http://www.shakespearesglobe.com/"/>
    <meta itemprop="address" content="London, UK"/>
  </div>
  <div itemprop="offers" itemscope="" itemtype="http://schema.org/Offer">
    <link itemprop="url" href="/examples/ticket/0012301230123"/>
  </div>
  <span itemprop="startDate" content="2014-10-01T19:30">Wed 01 October 2014 19:30</span>
  <div itemprop="workPerformed" itemscope="" itemtype="http://schema.org/CreativeWork">
    <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Julius_Caesar_(play)"/>
    <link itemprop="sameAs" href="http://worldcat.org/entity/work/id/1807288036"/>
    <div itemprop="creator" itemscope="" itemtype="http://schema.org/Person">
       <meta itemprop="name" content="William Shakespeare"/>
       <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/William_Shakespeare"/>
    </div>
  </div>
</div>

</body>

</html>

```

### `tests/samples/schema.org/Event.008.json`

```json
[{"properties": {"location": {"properties": {"address": "London, UK",
                                             "name": "Shakespeare's Globe",
                                             "sameAs": "http://www.shakespearesglobe.com/"},
                              "type": "http://schema.org/PerformingArtsTheater"},
                 "name": "Julius Caesar at Shakespeare's Globe",
                 "offers": {"properties": {"url": "/examples/ticket/0012301230123"},
                            "type": "http://schema.org/Offer"},
                 "startDate": "2014-10-01T19:30",
                 "workPerformed": {"properties": {"creator": {"properties": {"name": "William Shakespeare",
                                                                             "sameAs": "http://en.wikipedia.org/wiki/William_Shakespeare"},
                                                              "type": "http://schema.org/Person"},
                                                  "sameAs": ["http://en.wikipedia.org/wiki/Julius_Caesar_(play)",
                                                             "http://worldcat.org/entity/work/id/1807288036"]},
                                   "type": "http://schema.org/CreativeWork"}},
  "type": "http://schema.org/TheaterEvent"}]


```

### `tests/samples/schema.org/LocalBusiness.002.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>

<div itemscope itemtype="http://schema.org/Restaurant">
  <span itemprop="name">GreatFood</span>
  <div itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating">
    <span itemprop="ratingValue">4</span> stars -
    based on <span itemprop="reviewCount">250</span> reviews
  </div>
  <div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
    <span itemprop="streetAddress">1901 Lemur Ave</span>
    <span itemprop="addressLocality">Sunnyvale</span>,
    <span itemprop="addressRegion">CA</span> <span itemprop="postalCode">94086</span>
  </div>
  <span itemprop="telephone">(408) 714-1489</span>
  <a itemprop="url" href="http://www.dishdash.com">www.greatfood.com</a>
  Hours:
  <meta itemprop="openingHours" content="Mo-Sa 11:00-14:30">Mon-Sat 11am - 2:30pm
  <meta itemprop="openingHours" content="Mo-Th 17:00-21:30">Mon-Thu 5pm - 9:30pm
  <meta itemprop="openingHours" content="Fr-Sa 17:00-22:00">Fri-Sat 5pm - 10:00pm
  Categories:
  <span itemprop="servesCuisine">
    Middle Eastern
  </span>,
  <span itemprop="servesCuisine">
    Mediterranean
  </span>
  Price Range: <span itemprop="priceRange">$$</span>
  Takes Reservations: Yes
</div>

</body>

</html>

```

### `tests/samples/schema.org/LocalBusiness.002.json`

```json
[{"properties": {"address": {"properties": {"addressLocality": "Sunnyvale",
                                            "addressRegion": "CA",
                                            "postalCode": "94086",
                                            "streetAddress": "1901 Lemur Ave"},
                             "type": "http://schema.org/PostalAddress"},
                 "aggregateRating": {"properties": {"ratingValue": "4",
                                                    "reviewCount": "250"},
                                     "type": "http://schema.org/AggregateRating"},
                 "name": "GreatFood",
                 "openingHours": ["Mo-Sa 11:00-14:30",
                                  "Mo-Th 17:00-21:30",
                                  "Fr-Sa 17:00-22:00"],
                 "priceRange": "$$",
                 "servesCuisine": ["Middle Eastern",
                                   "Mediterranean"],
                 "telephone": "(408) 714-1489",
                 "url": "http://www.dishdash.com"},
  "type": "http://schema.org/Restaurant"}]

```

### `tests/samples/schema.org/LocalBusiness.003.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>

<div itemscope itemtype="http://schema.org/Invoice">
  <h1 itemprop="description">New furnace and installation</h1>
  <div itemprop="broker" itemscope itemtype="http://schema.org/LocalBusiness">
    <b itemprop="name">ACME Home Heating</b>
  </div>
  <div itemprop="customer" itemscope itemtype="http://schema.org/Person">
    <b itemprop="name">Jane Doe</b>
  </div>
  <span itemprop="paymentDueDate">2015-01-30</span>
  <div itemprop="minimumPaymentDue" itemscope itemtype="http://schema.org/PriceSpecification">
    <span itemprop="price">0.00</span>
    <span itemprop="priceCurrency">USD</span>
  </div>
  <div itemprop="totalPaymentDue" itemscope itemtype="http://schema.org/PriceSpecification">
    <span itemprop="price">0.00</span>
    <span itemprop="priceCurrency">USD</span>
  </div>
  <meta itemprop="paymentStatus" content="http://schema.org/PaymentComplete" />
  <div itemprop="referencesOrder" itemscope itemtype="http://schema.org/Order">
    <span itemprop="description">furnace</span>
    <span itemprop="orderDate">2014-12-01</span>
    <span itemprop="orderNumber">123ABC</span>
    <div itemprop="orderedItem" itemscope itemtype="http://schema.org/Product">
      <span itemprop="name">ACME Furnace 3000</span>
      <meta itemprop="productId" content="ABC123" />
    </div>
  </div>
  <div itemprop="referencesOrder" itemscope itemtype="http://schema.org/Order">
    <span itemprop="description">furnace installation</span>
    <span itemprop="orderDate">2014-12-02</span>
    <div itemprop="orderedItem" itemscope itemtype="http://schema.org/Service">
      <span itemprop="description">furnace installation</span>
    </div>
  </div>
</div>

</body>

</html>

```

### `tests/samples/schema.org/LocalBusiness.003.json`

```json
[{"properties": {"broker": {"properties": {"name": "ACME Home Heating"},
                            "type": "http://schema.org/LocalBusiness"},
                 "customer": {"properties": {"name": "Jane Doe"},
                              "type": "http://schema.org/Person"},
                 "description": "New furnace and installation",
                 "minimumPaymentDue": {"properties": {"price": "0.00",
                                                      "priceCurrency": "USD"},
                                       "type": "http://schema.org/PriceSpecification"},
                 "paymentDueDate": "2015-01-30",
                 "paymentStatus": "http://schema.org/PaymentComplete",
                 "referencesOrder": [{"properties": {"description": "furnace",
                                                     "orderDate": "2014-12-01",
                                                     "orderNumber": "123ABC",
                                                     "orderedItem": {"properties": {"name": "ACME Furnace 3000",
                                                                                    "productId": "ABC123"},
                                                                     "type": "http://schema.org/Product"}},
                                      "type": "http://schema.org/Order"},
                                     {"properties": {"description": "furnace installation",
                                                     "orderDate": "2014-12-02",
                                                     "orderedItem": {"properties": {"description": "furnace installation"},
                                                                     "type": "http://schema.org/Service"}},
                                      "type": "http://schema.org/Order"}],
                 "totalPaymentDue": {"properties": {"price": "0.00",
                                                    "priceCurrency": "USD"},
                                     "type": "http://schema.org/PriceSpecification"}},
  "type": "http://schema.org/Invoice"}]

```

### `tests/samples/schema.org/MusicRecording.001.html`

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>schmea.org -- Creative Work</title>
</head>

<body>

<div itemscope itemtype="http://schema.org/MusicGroup">
<h1 itemprop="name">Foo Fighters</h1>
<div itemprop="video" itemscope itemtype="http://schema.org/VideoObject">
  <h2>Video: <span itemprop="name">Interview with the Foo Fighters</span></h2>
  <meta itemprop="duration" content="T1M33S" />
  <meta itemprop="thumbnail" content="foo-fighters-interview-thumb.jpg" />
  <object ...>
    <param ...>
    <embed type="application/x-shockwave-flash" ...>
  </object>
  <span itemprop="description">Catch this exclusive interview with
    Dave Grohl and the Foo Fighters about their new album, Rope.</span>
</div>
<h2>Songs</h2>
<div itemprop="track" itemscope itemtype="http://schema.org/MusicRecording">
  <span itemprop="name">Rope</span>
  <meta itemprop="url" content ="foo-fighters-rope.html">
  Length: <meta itemprop="duration" content="PT4M5S">4:05 -
  14300 plays
  <div itemprop="interactionCount" itemscope itemtype="http://schema.org/InteractionCounter">
    <meta itemprop="interactionType" content="http://schema.org/ListenAction" />
    <meta itemprop="userInteractionCount" content="14300" />
  </div>
  <a href="foo-fighters-rope-play.html" itemprop="audio">Play</a>
  <a href="foo-fighters-rope-buy.html" itemprop="offers">Buy</a>
  From album: <a href="foo-fighters-wasting-light.html"
    itemprop="inAlbum">Wasting Light</a>
</div>
<div itemprop="track" itemscope itemtype="http://schema.org/MusicRecording">
  <span itemprop="name">Everlong</span>
  <meta itemprop="url" content ="foo-fighters-everlong.html">
  Length: <meta itemprop="duration" content="PT6M33S">6:33 -
  11700 plays
  <div itemprop="interactionCount" itemscope itemtype="http://schema.org/InteractionCounter">
    <meta itemprop="interactionType" content="http://schema.org/ListenAction" />
    <meta itemprop="userInteractionCount" content="11700" />
  </div>
  <a href="foo-fighters-everlong-play.html" itemprop="audio">Play</a>
  <a href="foo-fighters-everlong-buy.html" itemprop="offers">Buy</a>
  From album: <a href="foo-fighters-color-and-shape.html"
    itemprop="inAlbum">The Color And The Shape</a>
</div>
<h2>Upcoming shows</h2>
<div itemprop="event" itemscope itemtype="http://schema.org/Event">
  <a href="foo-fighters-may20-fedexforum" itemprop="url">
    <span itemprop="name">FedExForum</span>
  </a>
  <span itemprop="location">Memphis, TN, US</span>
  <meta itemprop="startDate" content="2011-05-20">May 20
  <a href="ticketmaster.com/foofighters/may20-2011" itemprop="offers">Buy tickets</a>
</div>
<div itemprop="event" itemscope itemtype="http://schema.org/Event">
  <a href="foo-fighters-may23-midamericacenter" itemprop="url">
    <span itemprop="name">Mid America Center</span>
  </a>
  <span itemprop="location">Council Bluffs, IA, US</span>
  <meta itemprop="startDate" content="2011-05-23">May 23
  <a href="ticketmaster.com/foofighters/may23-2011" itemprop="offers">Buy tickets</a>
</div>
<h2><a href="foo-fighters-photos">28 Photos</a></h2>
<a href="foofighters-1.jpg" itemprop="image"><img
alt="Thumbnail and linked photo of Foo Fighters band"
src="foofighters-thumb1.jpg" /></a>
<a href="foofighters-2.jpg" itemprop="image"><img
alt="Thumbnail and linked photo of Foo Fighters band"
src="foofighters-thumb2.jpg" /></a>
<a href="foofighters-3.jpg" itemprop="image"><img
alt="Thumbnail and linked photo of Foo Fighters band"
src="foofighters-thumb3.jpg" /></a>
<h2>Comments:</h2>
Excited about seeing them in concert next week. -Lawrence , Jan 23
I dig their latest single. -Mary, Jan 19
<div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
  <meta itemprop="interactionType" content="http://schema.org/CommentAction" />
  <meta itemprop="userInteractionCount" content="18" />
</div>
Showing 1-2 of 18 comments. <a href="foofighters-comments">More</a>
</div>

</body>

</html>

```

### `tests/samples/schema.org/MusicRecording.001.json`

```json
[{"properties": {"event": [{"properties": {"location": "Memphis, TN, US",
                                           "name": "FedExForum",
                                           "offers": "ticketmaster.com/foofighters/may20-2011",
                                           "startDate": "2011-05-20",
                                           "url": "foo-fighters-may20-fedexforum"},
                            "type": "http://schema.org/Event"},
                           {"properties": {"location": "Council Bluffs, IA, US",
                                           "name": "Mid America Center",
                                           "offers": "ticketmaster.com/foofighters/may23-2011",
                                           "startDate": "2011-05-23",
                                           "url": "foo-fighters-may23-midamericacenter"},
                            "type": "http://schema.org/Event"}],
                 "image": ["foofighters-1.jpg",
                           "foofighters-2.jpg",
                           "foofighters-3.jpg"],
                 "interactionStatistic": {"properties": {"interactionType": "http://schema.org/CommentAction",
                                                         "userInteractionCount": "18"},
                                          "type": "http://schema.org/InteractionCounter"},
                 "name": "Foo Fighters",
                 "track": [{"properties": {"audio": "foo-fighters-rope-play.html",
                                           "duration": "PT4M5S",
                                           "inAlbum": "foo-fighters-wasting-light.html",
                                           "interactionCount": {"properties": {"interactionType": "http://schema.org/ListenAction",
                                                                               "userInteractionCount": "14300"},
                                                                "type": "http://schema.org/InteractionCounter"},
                                           "name": "Rope",
                                           "offers": "foo-fighters-rope-buy.html",
                                           "url": "foo-fighters-rope.html"},
                            "type": "http://schema.org/MusicRecording"},
                           {"properties": {"audio": "foo-fighters-everlong-play.html",
                                           "duration": "PT6M33S",
                                           "inAlbum": "foo-fighters-color-and-shape.html",
                                           "interactionCount": {"properties": {"interactionType": "http://schema.org/ListenAction",
                                                                               "userInteractionCount": "11700"},
                                                                "type": "http://schema.org/InteractionCounter"},
                                           "name": "Everlong",
                                           "offers": "foo-fighters-everlong-buy.html",
                                           "url": "foo-fighters-everlong.html"},
                            "type": "http://schema.org/MusicRecording"}],
                 "video": {"properties": {"description": "Catch this exclusive interview with Dave Grohl and the Foo Fighters about their new album, Rope.",
                                          "duration": "T1M33S",
                                          "name": "Interview with the Foo Fighters",
                                          "thumbnail": "foo-fighters-interview-thumb.jpg"},
                           "type": "http://schema.org/VideoObject"}},
  "type": "http://schema.org/MusicGroup"}]

```

### `tests/samples/schema.org/product_custom_url_and_node_id.json`

```json
[{"type": "http://schema.org/Product",
  "_nodeId_": "product",
  "properties": {"brand": "ACME",
                 "name": "Executive Anvil",
                 "image": "http://some-example.com/anvil_executive.jpg",
                 "description": "Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.",
                 "mpn": "925872",
                 "aggregateRating": {"type": "http://schema.org/AggregateRating",
                                     "_nodeId_": "aggregateRating",
                                     "properties": {"ratingValue": "4.4",
                                     "reviewCount": "89"}},
                 "offers": {"type": "http://schema.org/Offer",
                            "_nodeId_": "offer",
                            "properties": {"priceCurrency": "USD",
                                           "price": "119.99",
                                           "priceValidUntil": "2020-11-05",
                                           "seller": {"type": "http://schema.org/Organization",
                                                      "_nodeId_": "organization",
                                                      "properties":{"name": "Executive Objects"}},
                            "itemCondition": "http://schema.org/UsedCondition",
                            "availability": "http://schema.org/InStock"}}
                  }
  }]
```

### `tests/samples/schema.org/product_custom_url.json`

```json
[{"type": "http://schema.org/Product",
  "properties": {"brand": "ACME",
                 "name": "Executive Anvil",
                 "image": "http://some-example.com/anvil_executive.jpg",
                 "description": "Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.",
                 "mpn": "925872",
                 "aggregateRating": {"type": "http://schema.org/AggregateRating",
                                     "properties": {"ratingValue": "4.4",
                                     "reviewCount": "89"}},
                 "offers": {"type": "http://schema.org/Offer",
                            "properties": {"priceCurrency": "USD",
                                           "price": "119.99",
                                           "priceValidUntil": "2020-11-05",
                                           "seller": {"type": "http://schema.org/Organization",
                                                      "properties":{"name": "Executive Objects"}},
                            "itemCondition": "http://schema.org/UsedCondition",
                            "availability": "http://schema.org/InStock"}}
                  }
  }]
```

### `tests/samples/schema.org/product-ref.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>Photo gallery</title>
 </head>
 <body>

  <div id="product" itemscope itemtype="http://schema.org/Product" itemref="referenced-product more-properties related_products non-existing-ref">
    <span itemprop="brand">ACME</span>
    <span itemprop="name">Executive Anvil</span>
    <img itemprop="image" src=" anvil_executive.jpg" alt="Executive Anvil logo"/>
    <span itemprop="description">Sleeker than ACME's Classic Anvil, the
      Executive Anvil is perfect for the business traveler
      looking for something to drop from a height.
    </span>
    Product #: <span itemprop="mpn">925872</span>
    <span id="aggregateRating" itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating">
      <span itemprop="ratingValue">4.4</span> stars, based on <span itemprop="reviewCount">89
        </span> reviews
    </span>

    <span id="offer" itemprop="offers" itemscope itemtype="http://schema.org/Offer">
      Regular price: $179.99
      <meta itemprop="priceCurrency" content="USD" />
      $<span itemprop="price">119.99 </span>
      (Sale ends <time itemprop="priceValidUntil" datetime="2020-11-05">
        5 November!</time>)
      Available from: <span id="organization" itemprop="seller" itemscope itemtype="http://schema.org/Organization">
                        <span itemprop="name">Executive Objects</span>
                      </span>
      Condition: <link itemprop="itemCondition" href="http://schema.org/UsedCondition"/>Previously owned,
        in excellent condition
      <link itemprop="availability" href="  http://schema.org/InStock"/>In stock! Order now!
    </span>
  </div>
  <div id="referenced-product" itemscope itemtype="http://schema.org/Product" itemprop="referenced_product">
    <span itemprop="name">REFERENCED PRODUCT</span>
    <img itemprop="image" src="img-ref.jpg">
  </div>
  <div id="more-properties" itemscope itemtype="http://schema.org/Product">
    <span itemprop="prop3">REFERENCED TO INCLUDE PROPERTIES AND ALSO INDIVIDUAL PRODUCT</span>
    <img itemprop="image" src="img-2.jpg">
  </div>
  <div id="related_products">
    <div itemscope itemtype="http://schema.org/Product" itemprop="related_products">
      <span itemprop="name">REL PROD 1</span>
      <img itemprop="image" src="rel-prod-1.jpg">
    </div>
    <div itemscope itemtype="http://schema.org/Product" itemprop="related_products">
      <span itemprop="name">REL PROD 2</span>
      <img itemprop="image" src="rel-prod-2.jpg">
    </div>
   </div>
 </body>
</html>
```

### `tests/samples/schema.org/product-ref.json`

```json
[
    {
        "type": "http://schema.org/Product",
        "properties": {
            "referenced_product": {
                "type": "http://schema.org/Product",
                "properties": {
                    "name": "REFERENCED PRODUCT",
                    "image": "img-ref.jpg"
                }
            },
            "prop3": "REFERENCED TO INCLUDE PROPERTIES AND ALSO INDIVIDUAL PRODUCT",
            "image": [
                "anvil_executive.jpg",
                "img-2.jpg"
            ],
            "related_products": [
                {
                    "type": "http://schema.org/Product",
                    "properties": {
                        "name": "REL PROD 1",
                        "image": "rel-prod-1.jpg"
                    }
                },
                {
                    "type": "http://schema.org/Product",
                    "properties": {
                        "name": "REL PROD 2",
                        "image": "rel-prod-2.jpg"
                    }
                }
            ],
            "brand": "ACME",
            "name": "Executive Anvil",
            "description": "Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.",
            "mpn": "925872",
            "aggregateRating": {
                "type": "http://schema.org/AggregateRating",
                "properties": {
                    "ratingValue": "4.4",
                    "reviewCount": "89"
                }
            },
            "offers": {
                "type": "http://schema.org/Offer",
                "properties": {
                    "priceCurrency": "USD",
                    "price": "119.99",
                    "priceValidUntil": "2020-11-05",
                    "seller": {
                        "type": "http://schema.org/Organization",
                        "properties": {
                            "name": "Executive Objects"
                        }
                    },
                    "itemCondition": "http://schema.org/UsedCondition",
                    "availability": "http://schema.org/InStock"
                }
            }
        }
    },
    {
        "type": "http://schema.org/Product",
        "properties": {
            "prop3": "REFERENCED TO INCLUDE PROPERTIES AND ALSO INDIVIDUAL PRODUCT",
            "image": "img-2.jpg"
        }
    }
]
```

### `tests/samples/schema.org/product.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>Photo gallery</title>
 </head>
 <body>

  <div id="product" itemscope itemtype="http://schema.org/Product">
    <span itemprop="brand">ACME</span>
    <span itemprop="name">Executive Anvil</span>
    <img itemprop="image" src=" anvil_executive.jpg
    " alt="Executive Anvil logo" />
    <span itemprop="description">Sleeker than ACME's Classic Anvil, the
      Executive Anvil is perfect for the business traveler
      looking for something to drop from a height.
    </span>
    Product #: <span itemprop="mpn">925872</span>
    <span id="aggregateRating" itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating">
      <span itemprop="ratingValue">4.4</span> stars, based on <span itemprop="reviewCount">89
        </span> reviews
    </span>

    <span id="offer" itemprop="offers" itemscope itemtype="http://schema.org/Offer">
      Regular price: $179.99
      <meta itemprop="priceCurrency" content="USD" />
      $<span itemprop="price">119.99 </span>
      (Sale ends <time itemprop="priceValidUntil" datetime="2020-11-05">
        5 November!</time>)
      Available from: <span id="organization" itemprop="seller" itemscope itemtype="http://schema.org/Organization">
                        <span itemprop="name">Executive Objects</span>
                      </span>
      Condition: <link itemprop="itemCondition" href="http://schema.org/UsedCondition"/>Previously owned,
        in excellent condition
      <link itemprop="availability" href="  http://schema.org/InStock"/>In stock! Order now!
    </span>
  </div>
 </body>
</html>
```

### `tests/samples/schema.org/product.json`

```json
[{"type": "http://schema.org/Product",
  "properties": {"brand": "ACME",
                 "name": "Executive Anvil",
                 "image": "anvil_executive.jpg",
                 "description": "Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.",
                 "mpn": "925872",
                 "aggregateRating": {"type": "http://schema.org/AggregateRating",
                                     "properties": {"ratingValue": "4.4",
                                     "reviewCount": "89"}},
                 "offers": {"type": "http://schema.org/Offer",
                            "properties": {"priceCurrency": "USD",
                                           "price": "119.99",
                                           "priceValidUntil": "2020-11-05",
                                           "seller": {"type": "http://schema.org/Organization",
                                                      "properties":{"name": "Executive Objects"}},
                            "itemCondition": "http://schema.org/UsedCondition",
                            "availability": "http://schema.org/InStock"}}
                  }
  }]
```

### `tests/samples/schema.org/SearchAction.001.html`

```html
<div itemscope itemtype="https://schema.org/WebSite">
  <meta itemprop="url" content="https://www.example.com/"/>
  <form itemprop="potentialAction" itemscope itemtype="https://schema.org/SearchAction">
    <meta itemprop="target" content="https://query.example.com/search?q={search_term_string}"/>
    <input itemprop="query-input" type="text" name="search_term_string" required/>
    <input type="submit"/>
  </form>
</div>

```

### `tests/samples/schema.org/SearchAction.001.json`

```json
[{"type": "https://schema.org/WebSite", "properties": {"url": "https://www.example.com/", "potentialAction": {"type": "https://schema.org/SearchAction", "properties": {"target": "https://query.example.com/search?q={search_term_string}", "query-input": {"valueRequired": true, "valueName": "search_term_string"}}}}}]
```

### `tests/samples/songkick/Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015.html`

```html
<!DOCTYPE html>
<html lang="en" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml">
  <head>
    <link rel="stylesheet" type="text/css" href="//assets.sk-static.com/assets/concert-c8626a8.css">
    <script type="text/javascript">
  SK = typeof(SK) == 'undefined' ? {} : SK;
  SK_ASSET_HOST = "//assets.sk-static.com";
  SK_DYNAMIC_ASSET_HOST = "http://images.sk-static.com";
  CX_EXPERIMENT_ID = "";
  CX_VARIATION_ID = -2;
</script>

    
    <title>Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015 – Songkick</title>
    <link href="//images.sk-static.com/images/media/profile_images/artists/236156/col3" rel="image_src">
    <link rel="shortcut icon" type="image/x-icon" href="//assets.sk-static.com/images/favicon.ico" />
    <link href="//assets.sk-static.com/images/apple-touch-icon.png" rel="apple-touch-icon">
    <link href="//assets.sk-static.com/images/apple-touch-icon.png" rel="apple-touch-icon-precomposed">
    <meta name="robots" content="all">
    <link href="http://www.songkick.com/concerts/25248299-elysian-fields-at-owl-music-parlor" rel="canonical">
        <meta property="al:ios:url" content="songkick://events/25248299-elysian-fields-at-owl-music-parlor">
    <meta property="al:ios:app_store_id" content="438690886">
    <meta property="al:ios:app_name" content="Songkick Concerts">
    <link rel="alternate" href="android-app://com.songkick/http/www.songkick.com/concerts/25248299-elysian-fields-at-owl-music-parlor">
    <meta name="description" content="Buy tickets for Elysian Fields’s upcoming concert at The Owl Music Parlor in Brooklyn on 31 Oct 2015.">
    <meta property="fb:app_id" content="308540029359">
    <meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0, width=device-width">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta property="og:site_name" content="Songkick">
<meta property="og:type" content="songkick-concerts:concert">
<meta property="og:title" content="Elysian Fields at The Owl Music Parlor (31 Oct 15)">
<meta property="og:description" content="Buy tickets for Elysian Fields’s upcoming concert at The Owl Music Parlor in Brooklyn on 31 Oct 2015.">
<meta property="og:url" content="http://www.songkick.com/concerts/25248299-elysian-fields-at-owl-music-parlor">
<meta property="og:image" content="//images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg">
<meta property="og:locality" content="Brooklyn">
<meta property="og:region" content="NY">
<meta property="og:country-name" content="US">
<meta property="og:street-address" content="497 Rogers Ave">
<meta property="og:postal-code" content="11225">
<meta property="og:latitude" content="40.660109">
<meta property="og:longitude" content="-73.953193">
    <script type="text/javascript">
      (function() {
        var _fbq = window._fbq || (window._fbq = []);
        if (!_fbq.loaded) {
          var fbds = document.createElement('script');
          fbds.async = true;
          fbds.src = '//connect.facebook.net/en_US/fbds.js';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(fbds, s);
          _fbq.loaded = true;
        }
        _fbq.push(['addPixelId', '583609881778767']);
      })();
      window._fbq = window._fbq || [];
      window._fbq.push(['track', 'PixelInitialized', {}]);
    </script>
  </head>
  <body>
    <div id="fb-root"></div>
    <noscript><img height="1" width="1" alt="" style="display:none" src="https://www.facebook.com/tr?id=583609881778767&amp;ev=PixelInitialized" /></noscript>

    
    

    <div class="navigation">
        <div class="navigation-large-screen">
  <ul class="nav-bar">
    <li class="sub-nav">
      <ul>
        <li class="logo"><a href="/" data-analytics-category="navigation" data-analytics-label="logo"><img src="//assets.sk-static.com/assets/nw/furniture/songkick-logo-ac43b7a.svg" height="26" width="90" alt="songkick"></a>
        </li><li class="metro-area menu hover-for-touch">
          <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area" title="Agen concerts">Agen concerts</a>
          <div class="menu-content empty-menu">
            <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="popular_tickets"><span>Popular tickets in Agen</span></a>
            <a class="repeat" href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area">Agen concerts</a>
              <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area_see_all">See all Agen concerts</a> <a class="change-location" data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">(Change&nbsp;location)</a><br><br>
              <a data-analytics-category="navigation" data-analytics-label="metro_area_today" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=10%2F26%2F2015&amp;filters%5BminDate%5D=10%2F26%2F2015#date-filter-form">Today ·</a> <a data-analytics-category="navigation" data-analytics-label="metro_area_7days" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=11%2F02%2F2015&amp;filters%5BminDate%5D=10%2F26%2F2015#date-filter-form">Next 7 days ·</a> <a data-analytics-category="navigation" data-analytics-label="metro_area_month" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=11%2F26%2F2015&amp;filters%5BminDate%5D=10%2F26%2F2015#date-filter-form">Next 30 days</a>
          </div>
        </li>
        <li class="artists menu hover-for-touch">
            <a href="/leaderboards/popular_artists" data-analytics-category="navigation" data-analytics-label="artists">Artists</a>
          <div class="menu-content">
              <ul class="artists-navigation">
<li class="col"><a href="/leaderboards/popular_artists" data-analytics-category="navigation" data-analytics-label="popular_artists">Most popular artists worldwide</a></li>
  <li class="col"><a href="/leaderboards/trending_artists" data-analytics-category="navigation" data-analytics-label="trending_artists">Trending artists worldwide</a></li>
</ul>
<div class="listing">
    <ul class="col popular-artists">
        <li>
          <a href="/artists/197928-coldplay" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/197928/avatar" width="35" height="35" class="artist-profile-image artist" alt="Coldplay live">
            <span class="name">Coldplay</span>
          </a>
        </li>
        <li>
          <a href="/artists/313388-u2" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/313388/avatar" width="35" height="35" class="artist-profile-image artist" alt="U2 live">
            <span class="name">U2</span>
          </a>
        </li>
        <li>
          <a href="/artists/139648-rihanna" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/139648/avatar" width="35" height="35" class="artist-profile-image artist" alt="Rihanna live">
            <span class="name">Rihanna</span>
          </a>
        </li>
        <li>
          <a href="/artists/182968-eminem" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/182968/avatar" width="35" height="35" class="artist-profile-image artist" alt="Eminem live">
            <span class="name">Eminem</span>
          </a>
        </li>
        <li>
          <a href="/artists/1134363-katy-perry" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/1134363/avatar" width="35" height="35" class="artist-profile-image artist" alt="Katy Perry live">
            <span class="name">Katy Perry</span>
          </a>
        </li>
        <li>
          <a href="/artists/537914-adele" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/537914/avatar" width="35" height="35" class="artist-profile-image artist" alt="Adele live">
            <span class="name">Adele</span>
          </a>
        </li>
        <li>
          <a href="/artists/181875-maroon-5" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/181875/avatar" width="35" height="35" class="artist-profile-image artist" alt="Maroon 5 live">
            <span class="name">Maroon 5</span>
          </a>
        </li>
        <li>
          <a href="/artists/552177-kanye-west" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/552177/avatar" width="35" height="35" class="artist-profile-image artist" alt="Kanye West live">
            <span class="name">Kanye West</span>
          </a>
        </li>
        <li>
          <a href="/artists/974908-lady-gaga" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/974908/avatar" width="35" height="35" class="artist-profile-image artist" alt="Lady Gaga live">
            <span class="name">Lady Gaga</span>
          </a>
        </li>
        <li>
          <a href="/artists/468146-red-hot-chili-peppers" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/468146/avatar" width="35" height="35" class="artist-profile-image artist" alt="Red Hot Chili Peppers live">
            <span class="name">Red Hot Chili Peppers</span>
          </a>
        </li>
    </ul>
    <ul class="col popular-artists">
        <li>
          <a href="/artists/8438813-i-love-makonnen" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/8438813/avatar" width="35" height="35" class="artist-profile-image artist" alt="I Love Makonnen live">
            <span class="name">I Love Makonnen</span>
          </a>
        </li>
        <li>
          <a href="/artists/186546-ghost" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/186546/avatar" width="35" height="35" class="artist-profile-image artist" alt="Ghost live">
            <span class="name">Ghost</span>
          </a>
        </li>
        <li>
          <a href="/artists/8568579-alessia-cara" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/8568579/avatar" width="35" height="35" class="artist-profile-image artist" alt="Alessia Cara live">
            <span class="name">Alessia Cara</span>
          </a>
        </li>
        <li>
          <a href="/artists/8508053-post-malone" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/8508053/avatar" width="35" height="35" class="artist-profile-image artist" alt="Post Malone live">
            <span class="name">Post Malone</span>
          </a>
        </li>
        <li>
          <a href="/artists/8386078-sam-feldt" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/8386078/avatar" width="35" height="35" class="artist-profile-image artist" alt="Sam Feldt live">
            <span class="name">Sam Feldt</span>
          </a>
        </li>
    </ul>
</div>

            <div class="tourbox-cta">
              Get your tour dates seen by one billion fans: <a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=visitor" class="sign-up-as-an-artist" data-analytics-category="navigation" data-analytics-label="sign_up_tourbox">Sign up as an artist</a>
            </div>
          </div>
        </li>
        <li class="location">
          <a data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">Change&nbsp;location</a>
        </li>
      </ul>
    <li class="sub-nav">
      <ul>
        <li class="search">
          <form name="search" class="navigation-search-form" data-analytics-category="navigation" data-analytics-label="search" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="hidden" name="type" value="initial">
  <input name="query" type="search" value="" class="text navigation-search" placeholder="Enter artist / concert / venue"><button class="search-button" name="commit" type="submit"><img src="//assets.sk-static.com/assets/nw/components/navigation-large-screen/search-5510d8d.svg" height="15" width="14" alt="search" class="navigation-submit"></button>
</form>
        </li>
        <li class="login-signup">
          <a href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew&amp;cancel_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor" rel="nofollow" class="signup-link" data-signup-source="Everything else" data-analytics-category="navigation" data-analytics-label="sign_up">Sign up</a> <small>or</small> <a href="https://accounts.songkick.com/session/new?source_product=skweb&amp;success_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor&amp;cancel_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor" rel="nofollow" data-analytics-category="navigation" data-analytics-label="log_in">Log in</a>
        </li>
      </ul>
    </li>
  </ul>
</div>

        <div class="global-navigation">
  <ul id='global-navigation-list'>
    <li class="nav-icon"><a href="#nav-icon-toggle"><img src="//assets.sk-static.com/assets/nw/components/navigation/profile-menu-icon-b6e2b51.png" width="26" height="19" alt="Show navigation"></a></li>
    <li id="nav-icon-toggle" class="nav"></li>
    <li class="signup"><a href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew&amp;cancel_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor" rel="nofollow" class="signup-link" data-signup-source="Everything else" data-analytics-category="navigation" data-analytics-label="sign_up" data-auto-signup-redirect-url="https://itunes.apple.com/us/app/apple-store/id438690886?ct=%3A&amp;mt=8&amp;pt=307660">Sign up</a></li>
    <li><a href="https://accounts.songkick.com/session/new?source_product=skweb&amp;success_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor&amp;cancel_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor" rel="nofollow" data-analytics-category="navigation_small_screen" data-analytics-label="log_in">Log in</a></li>
  </ul>
  <a href="/" id="logo" data-analytics-category="navigation_small_screen" data-analytics-label="logo"><img src="//assets.sk-static.com/assets/nw/components/navigation/header-logo-ff8507a.png" alt="Songkick" width="124" height="32"></a>
</div>
<div class="local-navigation">
  <ul>
    <li class="nav-icon"><a href="#home"><img src="//assets.sk-static.com/assets/nw/components/navigation/local-navigation/navigation-icon-2eeeafe.png" width="22" height="15" alt="Show navigation"></a></li><li class="nav-icon search-nav"><label><a href="#search"><img src="//assets.sk-static.com/assets/nw/components/navigation/local-navigation/search-5cac59e.png" height="20" width="20" alt="search"></a></label></li>
    <li class="site-search" id="search">
      <form name="search" class="navigation-search-form" data-analytics-category="navigation" data-analytics-label="search" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="hidden" name="type" value="initial">
  <input name="query" type="search" value="" class="text navigation-search" placeholder="Enter artist / concert / venue"><button class="search-button" name="commit" type="submit"><img src="//assets.sk-static.com/assets/nw/components/navigation-large-screen/search-5510d8d.svg" height="15" width="14" alt="search" class="navigation-submit"></button>
</form>
    </li>
    <li class="home nav" id="home">
      <a data-analytics-category="navigation" data-analytics-label="home" href="/">Home</a>
    </li><li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="metro_area" href="/metro_areas/94426-france-agen">Agen concerts</a>
    </li><li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">Change&nbsp;location</a>
    </li><li>
      <a href="/leaderboards/popular_artists" data-analytics-catigory="navigation" data-analytics-label="popular_artists">Popular artists</a>
    </li>
  </ul>
</div>

      
    </div>


    

<div>
  <div class="event-header pull">
    
    
<div class="component brief">
  <div class="profile-picture-and-actions">

    <div class="profile-picture-wrapper">
      <img class="profile-picture event" src="//images.sk-static.com/images/media/profile_images/artists/236156/card_avatar" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="185">
    </div>

    <div class="event-moderation-actions">
      <div class="flag-event">
        <a href="mailto:support@songkick.com?subject=Event%20Data:%20/concerts/25248299-elysian-fields-at-owl-music-parlor"
           data-analytics-category="event_brief"
           data-analytics-label="flag_event">
          Flag a problem
        </a>
      </div>
    </div>
  </div>

  <div class="date-and-name">
    

    <h5>
      Saturday 31 October 2015
    </h5>
  </div>

  <h1 class="summary">
    <span><a data-analytics-category="event_brief" data-analytics-label="headliners" href="/artists/236156-elysian-fields">Elysian Fields</a></span>
  </h1>

  <div class="location">
    <span class="name"><a data-analytics-category="event_brief" data-analytics-label="venue_name" href="/venues/3134004-owl-music-parlor">The Owl Music Parlor</a>,</span>
      <span>Brooklyn, NY, US</span>

      <span class="venue-info-link"><a href="/venues/3134004-owl-music-parlor" data-analytics-category="event_brief" data-analytics-label="venue_info">(map)</a></span>
  </div>

  <div class="line-up">
    Line-up:
      <span class="headliner">
        <a data-analytics-category="event_brief" data-analytics-label="line_up_artist" href="/artists/236156-elysian-fields">Elysian Fields</a></span>
  </div>

      <div class="join-cta"><a href="http://www.songkick.com/signup" data-analytics-category="event_brief" data-analytics-label="join_songkick">Join Songkick</a> to track this concert and we'll remind you when it's coming up.</div>

    <div class="actions">
      <div class="attendance">
  <form class="attendance auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;Track event&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;Track event&lt;/span&gt;" data-subject-upcoming="true" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="PCTrPhtpasyAcI4rSHXzRi+CnG/qdUVV3DfVh1GlHEl3Xv0LWr2XAwIgcrjc6zr00GuXh5EUe2kJhCE1DOoMRA==" />
    <input type="hidden" name="relationship_type" value="tracking">
    <input type="hidden" name="subject_id" value="25248299">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/concerts/25248299-elysian-fields-at-owl-music-parlor">
    <input type="hidden" name="auto_signup_redirect_url" value="">
    <button type="submit" class="tracking attendance-action" value="Track event"><span class="icon"></span><span class="button-text">Track event</span></button>
</form>  <form class="attendance auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I’m going&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I’m going&lt;/span&gt;" data-subject-upcoming="true" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="tMAsowmtCBlHGKgPJ5Y7nK6YBpYiuaXDzonTvC9Dxhz/ujqWSHn11sVIVJyzCPIuUXENflnYm/8bOicOcgzWEQ==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="25248299">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/concerts/25248299-elysian-fields-at-owl-music-parlor">
    <input type="hidden" name="auto_signup_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I’m going"><span class="icon"></span><span class="button-text">I’m going</span></button>
</form></div>

    </div>

</div>

  </div>

  <div class="page pull">
    <div class="primary col">
      <div id="tickets" class="component tickets-table tickets">
  <h2>Buy tickets</h2>
    <p class="no-face-value">
      We don’t know about tickets yet.
        Check the <a target="_blank" rel="nofollow" data-analytics-category="tickets_component" data-analytics-label="venue_link" href="http://www.theowl.nyc">venue website</a> for more info.
    </p>
</div>

        <div class="component event-hotness">
    <div class="hotness-container">
        <div class="venue-type">
          <span class="hotness-title">Venue type</span>
          <span class="hotness-data">Club (65 capacity)</span>
        </div>
    </div>
  </div>

      
      
      <div class="component venue-info">
  <h2>Venue</h2>
  <div class="venue-info-map">
    <a href="http://maps.google.com/maps?ll=40.660109,-73.953193&amp;q=40.660109,-73.953193&amp;z=15" target="_blank">
      <img src="//maps.googleapis.com/maps/api/staticmap?center=40.660109%2C-73.953193&amp;zoom=15&amp;size=620x260&amp;sensor=false&amp;markers=color%3A0xf80046%7C40.660109%2C-73.953193&amp;key=AIzaSyCrwff0AtTbdgLZ6Qi0iGF_rQs0B4LE8RA" height="260" width="620" alt="Map for The Owl Music Parlor">
    </a>
  </div>
  <div class="venue-info-details">
    <a class="url" href="/venues/3134004-owl-music-parlor">The Owl Music Parlor</a>
    <p class="venue-hcard">
  <span>
      <span>497 Rogers Ave</span>
      <span>11225</span>
    <span>Brooklyn, NY, US</span>
  </span>
    <span>(718) 774-0042</span>
    <span><a class="url" target="_blank" href="http://www.theowl.nyc">www.theowl.nyc</a></span>
</p>

    <a href="/venues/3134004-owl-music-parlor">6 upcoming concerts</a>
    <span class="capacity">Capacity: 65</span>
  </div>
</div>

      
      <div class="component additional-details">
  <h2>Additional details</h2>
  <div class="additional-details-container">
      <p>Doors open: 19:30</p>
  </div>
</div>

      <div class="component event-social">
  <h2>Share this concert</h2>
  <ul>
    <li><a href="https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor%3Futm_campaign%3Devent-page%26utm_content%3DZD0yNDU3MzIy%26utm_medium%3Dshared%26utm_source%3Dfacebook" class="facebook-share button social-sharing facebook" data-analytics-category="social_share" data-analytics-label="facebook" title="Share on Facebook"><span class="icon"></span><span class="button-text">Share</span></a></li>
    <li><a href="https://twitter.com/share?url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor%3Futm_campaign%3Devent-page%26utm_content%3DZD0yNDU3MzIy%26utm_medium%3Dshared%26utm_source%3Dtwitter&amp;via=songkick" class="tweet twitter button social-sharing" data-analytics-category="social_share" data-analytics-label="twitter"  title="Share on twiter"><span class="icon"></span><span class="button-text">Tweet</span></a></li>
    <li><a href="https://plus.google.com/share?url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F25248299-elysian-fields-at-owl-music-parlor%3Futm_campaign%3Devent-page%26utm_content%3DZD0yNDU3MzIy%26utm_medium%3Dshared%26utm_source%3Dgoogleplus" class="googleplus button social-sharing googleplus" data-analytics-category="social_share" data-analytics-label="google" title="Share on Google+"><span class="icon"></span><span class="button-text">Share</span></a></li>
  </ul>
</div>

      
      <div class="component expanded-lineup-details">
  <h2>Line-up details</h2>
  <ul>
    <li class="headliner">
      <div class="artist-image">
        <a href="/artists/236156-elysian-fields">
          <img src="//images.sk-static.com/images/media/profile_images/artists/236156/large_avatar" class="artist" alt="Elysian Fields live" />
        </a>
      </div>
      <div class="artist-info">
        <div class="headliner-label">HEADLINER</div>
        <div class="main-details">
          <span><a href="/artists/236156-elysian-fields">Elysian Fields</a></span>
          <a href="/artists/236156-elysian-fields">7 upcoming events</a>
        </div>
        <div class="last-performance artist-details">
          <p><strong>Last time in New York:</strong> 12 months ago</p>
        </div>
      </div>
    </li>
  </ul>
</div>

      
      
      <div class="component media-summary">

    <div class="media-group posters">
  <h2>Posters (1)</h2>
  <ul class="media-set posters inview" data-url="/concerts/25248299-elysian-fields-at-owl-music-parlor/posters" data-per-page="8" data-total="1">
    <li>
      <div class="media-element">
  <a href="/posters/16882157" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20151024-185802-067024.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="220">
  </a>
</div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#posters" data-analytics-category="media_summary" data-analytics-label="see_all_posters">
      See all posters (1)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_posters_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_posters_next">
    </button>
  </nav>
</div>

    <div class="media-group videos">
  <h2>Videos (2)</h2>
    <div class="video-standfirst">
      <span class="icon-expand">
        <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
      </span>
      <iframe width="480" height="295" src="//www.youtube.com/embed/Us26gmtuf38"></iframe>
    </div>
  <ul class="media-set videos inview" data-url="/concerts/25248299-elysian-fields-at-owl-music-parlor/videos" data-per-page="4" data-total="2">
    <li>
      <div class="media-element">
  <a href="/videos/16882242" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/Us26gmtuf38" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/Us26gmtuf38/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>
<div class="media-element">
  <a href="/videos/16586497" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/A5pjB65_JCQ" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/A5pjB65_JCQ/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#videos" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="see_all_videos">
      See all videos (2)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_videos_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_videos_next">
    </button>
  </nav>
</div>

    <div class="media-group">
  <h2>Photos (2)</h2>
  <ul class="media-set images inview" data-url="/concerts/25248299-elysian-fields-at-owl-music-parlor/images" data-per-page="12" data-total="2">
    <li>
      <div class="media-element media-element-square">
  <a class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="photo" href="/images/16586462">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="217" style="margin-top: -108px; margin-left: -110px;
            min-height: 140px;" src="http://images.sk-static.com/images/media/img/col3/20150925-054405-780997.jpg" />
</a></div>
<div class="media-element media-element-square">
  <a class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="photo" href="/images/1027156">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="164" style="margin-top: -82px; margin-left: -110px;
            min-height: 140px;" src="http://images.sk-static.com/images/media/img/col3/20100330-103600-169450.jpg" />
</a></div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#images" data-analytics-category="media_summary" data-analytics-label="see_all_photos">
      See all photos (2)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_photos_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_photos_next">
    </button>
  </nav>
</div>

</div>


    </div><div class="secondary col">
      <div class="component related-events">
  <div class="related-events-content">
    <h5>More events for Elysian Fields</h5>
    <ol>
        <li>
          <a data-analytics-category="related_events_for_headliner_in_radius" data-analytics-label="parent_headliner_id_236156__metro_area_id_7644" href="/concerts/25248289-elysian-fields-at-owl-music-parlor">
          <div class="date-wrap">
            <span class="day">Thu</span>
            <span class="date">29</span>
            <span class="month">Oct</span>
          </div>
          <span class="event-title"><strong>Elysian Fields</strong>
          The Owl Music Parlor, Brooklyn</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events_for_headliner_in_radius" data-analytics-label="parent_headliner_id_236156__metro_area_id_7644" href="/concerts/25071324-elysian-fields-at-le-poisson-rouge">
          <div class="date-wrap">
            <span class="day">Sat</span>
            <span class="date">07</span>
            <span class="month">Nov</span>
          </div>
          <span class="event-title"><strong>Elysian Fields</strong>
          Le Poisson Rouge, New York</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events_for_headliner_in_radius" data-analytics-label="parent_headliner_id_236156__metro_area_id_7644" href="/concerts/25248324-elysian-fields-at-owl-music-parlor">
          <div class="date-wrap">
            <span class="day">Thu</span>
            <span class="date">12</span>
            <span class="month">Nov</span>
          </div>
          <span class="event-title"><strong>Elysian Fields</strong>
          The Owl Music Parlor, Brooklyn</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events_for_headliner_in_radius" data-analytics-label="parent_headliner_id_236156__metro_area_id_7644" href="/concerts/25248374-elysian-fields-at-owl-music-parlor">
          <div class="date-wrap">
            <span class="day">Sat</span>
            <span class="date">14</span>
            <span class="month">Nov</span>
          </div>
          <span class="event-title"><strong>Elysian Fields</strong>
          The Owl Music Parlor, Brooklyn</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events_for_headliner_in_radius" data-analytics-label="parent_headliner_id_236156__metro_area_id_7644" href="/concerts/25248384-elysian-fields-at-owl-music-parlor">
          <div class="date-wrap">
            <span class="day">Thu</span>
            <span class="date">19</span>
            <span class="month">Nov</span>
          </div>
          <span class="event-title"><strong>Elysian Fields</strong>
          The Owl Music Parlor, Brooklyn</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events_for_headliner_in_radius" data-analytics-label="parent_headliner_id_236156__metro_area_id_7644" href="/concerts/25248389-elysian-fields-at-owl-music-parlor">
          <div class="date-wrap">
            <span class="day">Sat</span>
            <span class="date">21</span>
            <span class="month">Nov</span>
          </div>
          <span class="event-title"><strong>Elysian Fields</strong>
          The Owl Music Parlor, Brooklyn</span>
</a>        </li>
    </ol>
  </div>
</div>

      
      
        
    </div>
  </div>
</div>
<div class="microformat">
  <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/25248299-elysian-fields-at-owl-music-parlor?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Brooklyn","addressCountry":"US","addressRegion":"NY","streetAddress":"497 Rogers Ave","postalCode":"11225"},"name":"The Owl Music Parlor","sameAs":"http://www.theowl.nyc","geo":{"@type":"GeoCoordinates","latitude":40.660109,"longitude":-73.953193}},"startDate":"2015-10-31T19:30:00-0400","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
</div>



    <div class="footer-container">
      <div id="footer" class="footer">
  <ul>
    <li><a href="/blog" rel="nofollow">Blog</a></li>
    <li><a href="/info/about" rel="nofollow">About us</a></li>
    <li><a href="/info/jobs" rel="nofollow">Jobs</a></li>
    <li><a href="/developer"><abbr>API</abbr> &amp; Partners</a></li>
    <li><a href="https://tourbox.songkick.com">Tourbox for artists</a></li>
  </ul>

  <ul>
    <li><a href="http://support.songkick.com/">Help &amp; FAQ</a></li>
    <li><a href="/info/guidelines" rel="nofollow">Community guidelines</a></li>
    <li><a href="/press" rel="nofollow">Press</a></li>
    <li><a href="/info/terms" rel="nofollow">Terms of use</a></li>
    <li><a href="/info/privacy" rel="nofollow">Privacy policy</a></li>
    <li><a href="/info/security" rel="nofollow">Security</a></li>
  </ul>
  <div class="tourbox-cta">
    <p>Get your tour dates seen by one billion fans:</p><a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=visitor" class="sign-up-as-an-artist" data-analytics-category="navigation" data-analytics-label="sign_up_tourbox">Sign up as an artist</a>
  </div>


  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/leaderboards/popular_artists">Most popular charts</a></li>
  </ul>
  <div class="social-container">
    <ul class="social-icons">
      <li>
        <a href="https://twitter.com/songkick">
          <img src="//assets.sk-static.com/assets/nw/furniture/icons/twitter-161f1e4.png" width="22" height="18" alt="Twitter">
          &nbsp;<span>Follow us.</span>
        </a>
      </li>
    </ul>
    <ul class="social-icons">
      <li>
        <a href="http://www.facebook.com/songkickconcerts">
          <img src="//assets.sk-static.com/assets/nw/furniture/icons/facebook-08359b5.png" width="18" height="18" alt="Facebook">
          &nbsp;<span>Like us.</span>
        </a>
      </li>
    </ul>
    <ul class="social-icons">
      <li>
          &nbsp;<span>But we really hope you love us.</span>
      </li>
    </ul>
  </div>
</div>

    </div>
    <script type="text/javascript" src="//assets.sk-static.com/assets/manifests-21cdd8f.js"></script><script type="text/javascript" src="//assets.sk-static.com/assets/app-2fa9bef.js"></script>

  <script type="text/javascript" src="//assets.sk-static.com/assets/event_page-68ba480.js"></script>
  <script type="text/javascript">
    Songkick.EventBus.bind('app:initialize', function() {
      Songkick.EventBus.trigger('ui:event_page_upcoming:view', {tickets_label: "venue_link_only"});
    });
  </script>



<script type="text/javascript">
  /* <![CDATA[ */
  var google_conversion_id = 964669843;
  var google_custom_params = window.google_tag_params;
  var google_remarketing_only = true;
  /* ]]> */
</script>
<script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js">
</script>
<noscript>
  <div style="display:inline;">
  <img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/964669843/?value=0&amp;guid=ON&amp;script=0"/>
  </div>
</noscript>

<script src="//platform.twitter.com/oct.js" type="text/javascript"></script>
<script type="text/javascript">twttr.conversion.trackPid('l6neh', { tw_sale_amount: 0, tw_order_quantity: 0 });</script>
<noscript>
  <img height="1" width="1" style="display:none;" alt="" src="https://analytics.twitter.com/i/adsct?txn_id=l6neh&amp;p_id=Twitter&amp;tw_sale_amount=0&amp;tw_order_quantity=0" />
  <img height="1" width="1" style="display:none;" alt="" src="//t.co/i/adsct?txn_id=l6neh&amp;p_id=Twitter&amp;tw_sale_amount=0&amp;tw_order_quantity=0" />
</noscript>

<script type="text/javascript">
  SK.logged_in_user = {
    id:null,
    analyticsUserType: 'visitor'
  };

  JS.require("FB", 'jQuery', function() {
    Songkick.Facebook.init(
      "308540029359",
      ["email", "public_profile", "user_friends", "user_likes", "user_actions.music"],
      ["email", "public_profile", "user_friends", "user_likes", "user_actions.music", "publish_actions"],
      {events: Songkick.EventBus}
    );
  });
  var features = {};
  Songkick.EventBus.trigger('app:initialize', {events: Songkick.EventBus, features: features});
  Songkick.EventBus.trigger('ui:auto-signup:initialize', {events: Songkick.EventBus, externalSignupUrl: null});
</script>

    
    
    
  </body>
</html>

```

### `tests/samples/songkick/Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015.jsonld`

```jsonld
[
      {
        "@context": "http://schema.org",
        "@type": "MusicEvent",
        "name": "Elysian Fields",
        "url": "http://www.songkick.com\/concerts\/25248299-elysian-fields-at-owl-music-parlor?utm_medium=organic&utm_source=microformat",
        "location": {
          "@type": "Place",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Brooklyn",
            "addressCountry": "US",
            "addressRegion": "NY",
            "streetAddress": "497 Rogers Ave",
            "postalCode": "11225"
          },
          "name": "The Owl Music Parlor",
          "sameAs": "http://www.theowl.nyc",
          "geo": {
            "@type": "GeoCoordinates",
            "latitude": 40.660109,
            "longitude": -73.953193
          }
        },
        "startDate": "2015-10-31T19:30:00-0400",
        "performer": [
          {
            "@type": "MusicGroup",
            "name": "Elysian Fields",
            "sameAs": "http://www.songkick.com\/artists\/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
          }
        ]
      }
]

```

### `tests/samples/songkick/elysianfields_1.html`

```html
<!DOCTYPE html>
<html lang="en" xmlns:test1="http://example.org/test1#" xmlns:fb="http://www.facebook.com/2008/fbml">
  <head prefix="test2: http://example.org/test2# fb: http://www.facebook.com/2008/fbml songkick-concerts: http://ogp.me/ns/fb/songkick-concerts#">
    <link rel="stylesheet" type="text/css" href="//assets.sk-static.com/assets/artist-8005aab.css">
    <script type="text/javascript">
  SK = typeof(SK) == 'undefined' ? {} : SK;
  SK_ASSET_HOST = "//assets.sk-static.com";
  SK_DYNAMIC_ASSET_HOST = "http://images.sk-static.com";
  CX_EXPERIMENT_ID = "";
  CX_VARIATION_ID = -2;
</script>

    <title>Elysian Fields Tickets, Tour Dates 2017 &amp; Concerts – Songkick</title>
    <link href="//images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg" rel="image_src">
    <link rel="shortcut icon" type="image/x-icon" href="//assets.sk-static.com/images/favicon.ico" />
    <link href="//assets.sk-static.com/images/apple-touch-icon.png" rel="apple-touch-icon">
    <link href="//assets.sk-static.com/images/apple-touch-icon.png" rel="apple-touch-icon-precomposed">
    <meta name="robots" content="all">
    <link href="http://www.songkick.com/artists/236156-elysian-fields" rel="canonical">
        <meta property="al:ios:url" content="songkick://artists/236156-elysian-fields">
    <meta property="al:ios:app_store_id" content="438690886">
    <meta property="al:ios:app_name" content="Songkick Concerts">
    <meta name="description" content="Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017.">
    <meta property="fb:app_id" content="308540029359">
    <meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0, width=device-width">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta property="og:site_name" content="Songkick">
    <meta property="og:type" content="songkick-concerts:artist">
    <meta property="og:title" content="Elysian Fields">
    <meta property="og:description" content="Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017.">
    <meta property="og:url" content="http://www.songkick.com/artists/236156-elysian-fields">
    <meta property="og:image" content="http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg">
    <meta property="http://ogp.me/ns#image" content="http://images.sk-static.com/SECONDARY_IMAGE.jpg">
    <meta property="test1:image" content="http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg">
    <meta property="test1:image" content="http://images.sk-static.com/SECONDARY_IMAGE.jpg">
    <meta property="test1:image" content="http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg">
    <meta property="test2:image" content="http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg">
    <meta property="test2:image" content="http://images.sk-static.com/SECONDARY_IMAGE.jpg">
    <meta property="og" content="BAD PROPERTY">
  </head>
  <body>
    <script>
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
  document,'script','//connect.facebook.net/en_US/fbevents.js');
  fbq('init', '583609881778767');
  fbq('track', 'PageView');
</script>
<noscript>
  <img height="1" width="1" alt="" style="display:none" src="https://www.facebook.com/tr?id=583609881778767&amp;ev=PageView&amp;noscript=1" />
</noscript>

    <div id="fb-root"></div>

    
    
    <div class="track-alert js-track-alert ">
  <div class="track-alert-inner">
    This event has been added to your <a data-analytics-category="navigation_your_plans" data-analytics-label="feedback_your_plans" href="/calendar?filter=attendance">Plans</a>.
    <a class="track-alert-dismiss js-track-alert-dismiss">Close</a>
  </div>
</div>


    <div class="navigation">
        <div class="navigation-large-screen">
  <ul class="nav-bar">
    <li class="sub-nav">
      <ul>
        <li class="logo"><a href="/" data-analytics-category="navigation" data-analytics-label="logo"><img src="//assets.sk-static.com/assets/nw/furniture/songkick-logo-ac43b7a.svg" height="26" width="90" alt="songkick"></a>
        </li><li class="metro-area menu hover-for-touch">
          <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area" title="Agen concerts">Agen concerts</a>
          <div class="menu-content empty-menu">
            <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="popular_tickets"><span>Popular tickets in Agen</span></a>
            <a class="repeat" href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area">Agen concerts</a>
              <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area_see_all">See all Agen concerts</a> <a class="change-location" data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">(Change&nbsp;location)</a><br><br>
              <a data-analytics-category="navigation" data-analytics-label="metro_area_today" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=06%2F06%2F2017&amp;filters%5BminDate%5D=06%2F06%2F2017#date-filter-form">Today ·</a> <a data-analytics-category="navigation" data-analytics-label="metro_area_7days" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=06%2F13%2F2017&amp;filters%5BminDate%5D=06%2F06%2F2017#date-filter-form">Next 7 days ·</a> <a data-analytics-category="navigation" data-analytics-label="metro_area_month" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=07%2F06%2F2017&amp;filters%5BminDate%5D=06%2F06%2F2017#date-filter-form">Next 30 days</a>
          </div>
        </li>
        <li class="artists menu hover-for-touch">
            <a href="/leaderboards/popular_artists" data-analytics-category="navigation" data-analytics-label="artists">Artists</a>
          <div class="menu-content">
              <ul class="artists-navigation">
<li class="col"><a href="/leaderboards/popular_artists" data-analytics-category="navigation" data-analytics-label="popular_artists">Most popular artists worldwide</a></li>
  <li class="col"><a href="/leaderboards/trending_artists" data-analytics-category="navigation" data-analytics-label="trending_artists">Trending artists worldwide</a></li>
</ul>
<div class="listing">
    <ul class="col popular-artists">
        <li>
          <a href="/artists/197928-coldplay" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/197928/avatar" width="35" height="35" class="artist-profile-image artist" alt="Coldplay live">
            <span class="name">Coldplay</span>
          </a>
        </li>
        <li>
          <a href="/artists/313388-u2" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/313388/avatar" width="35" height="35" class="artist-profile-image artist" alt="U2 live">
            <span class="name">U2</span>
          </a>
        </li>
        <li>
          <a href="/artists/139648-rihanna" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/139648/avatar" width="35" height="35" class="artist-profile-image artist" alt="Rihanna live">
            <span class="name">Rihanna</span>
          </a>
        </li>
        <li>
          <a href="/artists/182968-eminem" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/182968/avatar" width="35" height="35" class="artist-profile-image artist" alt="Eminem live">
            <span class="name">Eminem</span>
          </a>
        </li>
        <li>
          <a href="/artists/537914-adele" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/537914/avatar" width="35" height="35" class="artist-profile-image artist" alt="Adele live">
            <span class="name">Adele</span>
          </a>
        </li>
        <li>
          <a href="/artists/181875-maroon-5" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/181875/avatar" width="35" height="35" class="artist-profile-image artist" alt="Maroon 5 live">
            <span class="name">Maroon 5</span>
          </a>
        </li>
        <li>
          <a href="/artists/556955-drake" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/556955/avatar" width="35" height="35" class="artist-profile-image artist" alt="Drake live">
            <span class="name">Drake</span>
          </a>
        </li>
        <li>
          <a href="/artists/552177-kanye-west" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/552177/avatar" width="35" height="35" class="artist-profile-image artist" alt="Kanye West live">
            <span class="name">Kanye West</span>
          </a>
        </li>
        <li>
          <a href="/artists/1134363-katy-perry" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/1134363/avatar" width="35" height="35" class="artist-profile-image artist" alt="Katy Perry live">
            <span class="name">Katy Perry</span>
          </a>
        </li>
        <li>
          <a href="/artists/941964-bruno-mars" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/941964/avatar" width="35" height="35" class="artist-profile-image artist" alt="Bruno Mars live">
            <span class="name">Bruno Mars</span>
          </a>
        </li>
    </ul>
    <ul class="col popular-artists">
        <li>
          <a href="/artists/9063689-starley" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/9063689/avatar" width="35" height="35" class="artist-profile-image artist" alt="Starley live">
            <span class="name">Starley</span>
          </a>
        </li>
        <li>
          <a href="/artists/8997064-xxxtentacion" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/8997064/avatar" width="35" height="35" class="artist-profile-image artist" alt="XXXTentacion live">
            <span class="name">XXXTentacion</span>
          </a>
        </li>
        <li>
          <a href="/artists/9031399-ozuna" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/9031399/avatar" width="35" height="35" class="artist-profile-image artist" alt="Ozuna live">
            <span class="name">Ozuna</span>
          </a>
        </li>
        <li>
          <a href="/artists/894756-khalid" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/894756/avatar" width="35" height="35" class="artist-profile-image artist" alt="Khalid live">
            <span class="name">Khalid</span>
          </a>
        </li>
        <li>
          <a href="/artists/241457-nav" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/241457/avatar" width="35" height="35" class="artist-profile-image artist" alt="NAV live">
            <span class="name">NAV</span>
          </a>
        </li>
    </ul>
</div>

            <div class="tourbox-cta">
              Get your tour dates seen by one billion fans: <a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=visitor" class="sign-up-as-an-artist" data-analytics-category="navigation" data-analytics-label="sign_up_tourbox">Sign up as an artist</a>
            </div>
          </div>
        </li>
        <li class="location">
          <a data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">Change&nbsp;location</a>
        </li>
      </ul>
    <li class="sub-nav">
      <ul>
        <li class="search">
          <form name="search" class="navigation-search-form" data-analytics-category="navigation" data-analytics-label="search" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="hidden" name="type" value="initial">
  <input name="query" type="search" value="" class="text navigation-search" placeholder="Enter artist / concert / venue"><button class="search-button" name="commit" type="submit"><img src="//assets.sk-static.com/assets/nw/components/navigation-large-screen/search-5510d8d.svg" height="15" width="14" alt="search" class="navigation-submit"></button>
</form>
        </li>
        <li class="login-signup">
          <a href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fartists%2F236156-elysian-fields&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" class="signup-link" data-signup-source="Everything else" data-analytics-category="navigation" data-analytics-label="sign_up">Sign up</a> <small>or</small> <a href="https://accounts.songkick.com/session/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fartists%2F236156-elysian-fields&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" data-analytics-category="navigation" data-analytics-label="log_in">Log in</a>
        </li>
      </ul>
    </li>
  </ul>
</div>

        <div class="global-navigation">
  <ul id='global-navigation-list'>
    <li class="nav-icon"><a href="#nav-icon-toggle"><img src="//assets.sk-static.com/assets/nw/components/navigation/profile-menu-icon-b6e2b51.png" width="26" height="19" alt="Show navigation"></a></li>
    <li id="nav-icon-toggle" class="nav"></li>
    <li class="signup"><a href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fartists%2F236156-elysian-fields&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" class="signup-link" data-signup-source="Everything else" data-analytics-category="navigation" data-analytics-label="sign_up" data-auto-signup-redirect-url="https://itunes.apple.com/us/app/apple-store/id438690886?ct=%3A&amp;mt=8&amp;pt=307660">Sign up</a></li>
    <li><a href="https://accounts.songkick.com/session/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fartists%2F236156-elysian-fields&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" data-analytics-category="navigation_small_screen" data-analytics-label="log_in">Log in</a></li>
  </ul>
  <a href="/" id="logo" data-analytics-category="navigation_small_screen" data-analytics-label="logo"><img src="//assets.sk-static.com/assets/nw/components/navigation/header-logo-ff8507a.png" alt="Songkick" width="124" height="32"></a>
</div>
<div class="local-navigation">
  <ul>
    <li class="nav-icon"><a href="#home"><img src="//assets.sk-static.com/assets/nw/components/navigation/local-navigation/navigation-icon-2eeeafe.png" width="22" height="15" alt="Show navigation"></a></li><li class="nav-icon search-nav"><label><a href="#search"><img src="//assets.sk-static.com/assets/nw/components/navigation/local-navigation/search-5cac59e.png" height="20" width="20" alt="search"></a></label></li>
    <li class="site-search" id="search">
      <form name="search" class="navigation-search-form" data-analytics-category="navigation" data-analytics-label="search" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="hidden" name="type" value="initial">
  <input name="query" type="search" value="" class="text navigation-search" placeholder="Enter artist / concert / venue"><button class="search-button" name="commit" type="submit"><img src="//assets.sk-static.com/assets/nw/components/navigation-large-screen/search-5510d8d.svg" height="15" width="14" alt="search" class="navigation-submit"></button>
</form>
    </li>
    <li class="home nav" id="home">
      <a data-analytics-category="navigation" data-analytics-label="home" href="/">Home</a>
    </li><li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="metro_area" href="/metro_areas/94426-france-agen">Agen concerts</a>
    </li><li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">Change&nbsp;location</a>
    </li><li>
      <a href="/leaderboards/popular_artists" data-analytics-catigory="navigation" data-analytics-label="popular_artists">Popular artists</a>
    </li>
  </ul>
</div>

    </div>

      <div class="artist-header">
      <div class="row component brief">

  <div class="col-8 primary">
    <h1 class="h0">Elysian Fields
    </h1>


    <ul>
          <li class="ontour">On tour: <strong>yes</strong></li>


              <li class="no-event-nearby">Elysian Fields is not playing near you. <a href="/artists/236156-elysian-fields/calendar">View all concerts</a></li>
                <li class="change-location">Agen, France <a href="/session/filter_metro_area?success_url=/artists/236156-elysian-fields">Change location</a></li>
    </ul>

    <div class="signup-cta-container">
      <h4>Be the first to know when they tour near you.</h4>

        <p>5,555 fans get concert alerts for this artist.</p>

      <div class="track-artist">
        <div class="tracking">
  <form data-analytics-category="signup_cta" data-analytics-action="artist:no_local:cta_button" data-analytics-label="236156" data-tracking-text="Yes, please notify me" data-stop-tracking-text="Yes, please notify me" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="O8P3WbKBJnc0/j6cQhZ/nPUqu84tZgd4v3uyieEk6f3BoAlwbhANhneKX/zd7wh3f4I51Nv5mUiziuHpoNzRHg==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="236156">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist signup-cta" value="Yes, please notify me">Yes, please notify me</button>
</form></div>

      </div>

      <div class="app-store-buttons">
        <a href="https://itunes.apple.com/us/app/apple-store/id438690886?ct=skweb%3Aartist%3Ano_local%3Aapp_store_bt&amp;mt=8&amp;pt=307660" class="app-store-button" data-analytics-category="signup_cta" data-analytics-action="artist:no_local:app_store_bt" data-analytics-label="236156">
          <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/app-store-icon-e56abf8.svg" alt="Available on the App Store" class="store-button">
        </a>
        <a href="https://play.google.com/store/apps/details?id=com.songkick&amp;referrer=utm_campaign%3Dartist%253Ano_local%253Aapp_store_bt%26utm_medium%3D%26utm_source%3Dskweb" class="google-play-button" data-analytics-category="signup_cta" data-analytics-action="artist:no_local:app_store_bt" data-analytics-label="236156">
          <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/play-store-icon-79aae3f.svg" alt="Available on the Play Store" class="store-button">
        </a>
      </div>
    </div>
  </div>

  <div class="col-4 profile-picture-wrap">
    <a href="/images/1027156" class="media-link" rel="nofollow" data-analytics-category="artist_brief" data-analytics-label="profile_image">
    <span class="on-tour">On tour</span>
    <img alt="Elysian Fields live" width="300" height="300" class="artist artist-profile-image" src="//images.sk-static.com/images/media/profile_images/artists/236156/huge_avatar" /></a>
  </div>

</div>

  </div>

  <div class="container">
    <div class="row">
      <div class="col-8 primary">
        
        
        <div class="component events-summary" id="calendar-summary">
  <h2 class="calendar">Upcoming concerts (1)</h2>
  <ul class="event-listings artist-focus">
         <li class="with-date">
           <strong>
            <time datetime="2017-06-10T19:30:00-0400">Saturday 10 June 2017</time>
           </strong>
         </li>

    <li title="Saturday 10 June 2017">
      <time datetime="2017-06-10T19:30:00-0400"></time>


      <p class="artists summary">
        <a href="/concerts/30173984-elysian-fields-at-owl-music-parlor">
          <span>
            <strong>Elysian Fields</strong>
              
          </span>
        </a>
      </p>

      <p class="location">
          <span class="venue-name"><a href="/venues/3134004-owl-music-parlor">The Owl Music Parlor</a></span>,
        <span>
          <span>
            Brooklyn, NY, US
          </span>
            <span class="street-address">497 Rogers Ave</span>
        </span>
      </p>

        <a href="/concerts/30173984-elysian-fields-at-owl-music-parlor">
          <span class="button buy-tickets">Buy&nbsp;tickets</span>
        </a>

      <div class="attendance">
  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;Track event&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;Track event&lt;/span&gt;" data-subject-upcoming="true" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="767qnpwQlkgUuKODLZYcRasCLB+PPGMobmUkzZ3dPKYVzRS3QIG9uVfMwuOyb2uuIaquBXmj/RhilHet3CUERQ==" />
    <input type="hidden" name="relationship_type" value="tracking">
    <input type="hidden" name="subject_id" value="30173984">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="tracking attendance-action" value="Track event"><span class="icon"></span><span class="button-text">Track event</span></button>
</form>  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I’m going&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I’m going&lt;/span&gt;" data-subject-upcoming="true" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="bHa1xBgq7RsVINQWP5oljmiqKYvbXRFTKSAOICT/mzuWFUvtxLvG6lZUtXagY1Jl4gKrkS3Cj2Ml0V1AZQej2A==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="30173984">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I’m going"><span class="icon"></span><span class="button-text">I’m going</span></button>
</form></div>

          <div class="attendance-tray">
    <h6>Don’t miss out.</h6>
    <p>Track this event and we’ll remind you when it’s coming up.</p>
  </div>


      <div class="microformat">
        <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/30173984-elysian-fields-at-owl-music-parlor?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Brooklyn","addressCountry":"US","addressRegion":"NY","streetAddress":"497 Rogers Ave","postalCode":"11225"},"name":"The Owl Music Parlor","sameAs":"http://www.theowl.nyc","geo":{"@type":"GeoCoordinates","latitude":40.660109,"longitude":-73.953193}},"startDate":"2017-06-10T19:30:00-0400","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
      </div>
    </li>
</ul>

</div>

        
        
        
        <div class="component media-summary">

    <div class="media-group videos">
  <h2>Videos (5)</h2>
    <div class="video-standfirst">
      <span class="icon-expand">
        <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
      </span>
      <iframe width="480" height="295" src="//www.youtube.com/embed/eLEhs86urK4"></iframe>
    </div>
  <ul class="media-set videos inview" data-url="/artists/236156-elysian-fields/videos" data-per-page="4" data-total="5">
    <li>
      <div class="media-element">
  <a href="/videos/22325526" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/eLEhs86urK4" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/eLEhs86urK4/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>
<div class="media-element">
  <a href="/videos/20966736" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/Tv-yeHo_1vQ" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/Tv-yeHo_1vQ/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>
<div class="media-element">
  <a href="/videos/19297127" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/3WiS3ZOAtXE" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/3WiS3ZOAtXE/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>
<div class="media-element">
  <a href="/videos/16882242" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/Us26gmtuf38" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/Us26gmtuf38/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#videos" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="see_all_videos">
      See all videos (5)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_videos_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_videos_next">
    </button>
  </nav>
</div>

    <div class="media-group">
  <h2>Photos (3)</h2>
  <ul class="media-set images inview" data-url="/artists/236156-elysian-fields/images" data-per-page="12" data-total="3">
    <li>
      <div class="media-element media-element-square">
  <a class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="photo" href="/images/19297137">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="163" style="margin-top: -81px; margin-left: -110px;
            min-height: 140px;" src="http://images.sk-static.com/images/media/img/col3/20160514-193706-150385.jpg" />
</a></div>
<div class="media-element media-element-square">
  <a class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="photo" href="/images/16586462">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="217" style="margin-top: -108px; margin-left: -110px;
            min-height: 140px;" src="http://images.sk-static.com/images/media/img/col3/20150925-054405-780997.jpg" />
</a></div>
<div class="media-element media-element-square">
  <a class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="photo" href="/images/1027156">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="164" style="margin-top: -82px; margin-left: -110px;
            min-height: 140px;" src="http://images.sk-static.com/images/media/img/col3/20100330-103600-169450.jpg" />
</a></div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#images" data-analytics-category="media_summary" data-analytics-label="see_all_photos">
      See all photos (3)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_photos_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_photos_next">
    </button>
  </nav>
</div>

    <div class="media-group posters">
  <h2>Posters (8)</h2>
  <ul class="media-set posters inview" data-url="/artists/236156-elysian-fields/posters" data-per-page="8" data-total="8">
    <li>
      <div class="media-element">
  <a href="/posters/19867181" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20160630-152543-052433.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="335">
  </a>
</div>
<div class="media-element">
  <a href="/posters/19297192" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20160514-194215-603498.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="139">
  </a>
</div>
<div class="media-element">
  <a href="/posters/16882227" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20151024-190306-422584.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="142">
  </a>
</div>
<div class="media-element">
  <a href="/posters/16882157" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20151024-185802-067024.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="220">
  </a>
</div>
<div class="media-element">
  <a href="/posters/16881532" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20151024-175107-333162.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="284">
  </a>
</div>
<div class="media-element">
  <a href="/posters/8207099" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20130330-164629-584505.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="330">
  </a>
</div>
<div class="media-element">
  <a href="/posters/7693414" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20130131-161630-788528.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="329">
  </a>
</div>
<div class="media-element">
  <a href="/posters/4271263" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20111011-050815-789254.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="330">
  </a>
</div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#posters" data-analytics-category="media_summary" data-analytics-label="see_all_posters">
      See all posters (8)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_posters_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_posters_next">
    </button>
  </nav>
</div>

</div>

          <div class="component events-summary" id="gigography-summary">
  <h2 class="calendar">Past concerts (321) <small><a rel="nofollow" href="/artists/236156-elysian-fields/gigography">See all</a></small></h2>
  <ul class="event-listings artist-focus">
         <li class="with-date">
           <strong>
            <time datetime="2017-04-26T20:00:00-0700">Wednesday 26 April 2017</time>
           </strong>
         </li>

    <li title="Wednesday 26 April 2017">
      <time datetime="2017-04-26T20:00:00-0700"></time>


      <p class="artists summary">
        <a href="/concerts/29673614-elysian-fields-at-hotel-utah-saloon" rel="nofollow">
          <span>
            <strong>Elysian Fields</strong>
              with Chocolate Genius Inc.
          </span>
        </a>
      </p>

      <p class="location">
          <span class="venue-name"><a href="/venues/328-hotel-utah-saloon">Hotel Utah Saloon</a></span>,
        <span>
          <span>
            San Francisco, CA, US
          </span>
            <span class="street-address">500 Fourth Street</span>
        </span>
      </p>


      <div class="attendance was-there">
  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="h1csHSIgrRXIoaF9kVWNd/k2iPlsml9Ch0fLOpVn/E59NNI0/rGG5IvVwB0OrPqcc54K45oFwXKLtpha1J/ErQ==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="29673614">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I was there"><span class="icon"></span><span class="button-text">I was there</span></button>
</form></div>

        

      <div class="microformat">
        <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/29673614-elysian-fields-at-hotel-utah-saloon?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"San Francisco","addressCountry":"US","addressRegion":"CA","streetAddress":"500 Fourth Street","postalCode":"94107"},"name":"Hotel Utah Saloon","sameAs":"http://www.hotelutah.com/","geo":{"@type":"GeoCoordinates","latitude":37.7795638,"longitude":-122.398023}},"startDate":"2017-04-26T20:00:00-0700","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Chocolate Genius Inc.","sameAs":"http://www.songkick.com/artists/1009602-chocolate-genius-inc?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
      </div>
    </li>
         <li class="with-date">
           <strong>
            <time datetime="2016-10-29T21:00:00+0200">Saturday 29 October 2016</time>
           </strong>
         </li>

    <li title="Saturday 29 October 2016">
      <time datetime="2016-10-29T21:00:00+0200"></time>


      <p class="artists summary">
        <a href="/concerts/27626524-elysian-fields-at-le-vip" rel="nofollow">
          <span>
            <strong>Elysian Fields</strong>
              
          </span>
        </a>
      </p>

      <p class="location">
          <span class="venue-name"><a href="/venues/1972419-le-vip">Le VIP</a></span>,
        <span>
          <span>
            Saint-Nazaire, France
          </span>
            <span class="street-address">Boulevard de la Légion d&#39;Honneur - Base Sous Marine - Alvéole 14</span>
        </span>
      </p>


      <div class="attendance was-there">
  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="BVbd+XsRf1lrCbQdNn49hdNM2MUB/Nfo3vvWnidfqAX/NSPQp4BUqCh91X2ph0puWeRa3/djSdjSCoX+ZqeQ5g==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="27626524">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I was there"><span class="icon"></span><span class="button-text">I was there</span></button>
</form></div>


      <div class="microformat">
        <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/27626524-elysian-fields-at-le-vip?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Saint-Nazaire","addressCountry":"France","streetAddress":"Boulevard de la Légion d'Honneur - Base Sous Marine - Alvéole 14","postalCode":"44600"},"name":"Le VIP","sameAs":"http://www.vip.les-escales.com","geo":{"@type":"GeoCoordinates","latitude":47.2734979,"longitude":-2.213848}},"startDate":"2016-10-29T21:00:00+0200","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Troy Von Balthazar","sameAs":"http://www.songkick.com/artists/355304-troy-von-balthazar?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
      </div>
    </li>
         <li class="with-date">
           <strong>
            <time datetime="2016-10-27T20:30:00+0200">Thursday 27 October 2016</time>
           </strong>
         </li>

    <li title="Thursday 27 October 2016">
      <time datetime="2016-10-27T20:30:00+0200"></time>


      <p class="artists summary">
        <a href="/concerts/26734634-elysian-fields-at-le-rocher-de-palmer" rel="nofollow">
          <span>
            <strong>Elysian Fields</strong>
              
          </span>
        </a>
      </p>

      <p class="location">
          <span class="venue-name"><a href="/venues/1080416-le-rocher-de-palmer">Le Rocher De Palmer</a></span>,
        <span>
          <span>
            Cenon, France
          </span>
            <span class="street-address">1 rue Aristide Briand</span>
        </span>
      </p>


      <div class="attendance was-there">
  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="+rMMR0nsxQghwbSbUlSvmPU98KzNXvUXPmPKG8I5ftgA0PJulX3u+WK11fvNrdhzf5VytjvBaycykpl7g8FGOw==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="26734634">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I was there"><span class="icon"></span><span class="button-text">I was there</span></button>
</form></div>


      <div class="microformat">
        <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/26734634-elysian-fields-at-le-rocher-de-palmer?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Cenon","addressCountry":"France","streetAddress":"1 rue Aristide Briand","postalCode":"33152"},"name":"Le Rocher De Palmer","sameAs":"http://lerocherdepalmer.fr/","geo":{"@type":"GeoCoordinates","latitude":44.8624327,"longitude":-0.5237826}},"startDate":"2016-10-27T20:30:00+0200","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Ernst Reijseger","sameAs":"http://www.songkick.com/artists/13128-ernst-reijseger?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Troy Von Balthazar","sameAs":"http://www.songkick.com/artists/355304-troy-von-balthazar?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Rachid Taha","sameAs":"http://www.songkick.com/artists/100389-rachid-taha?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Vaudou Game","sameAs":"http://www.songkick.com/artists/8195583-vaudou-game?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
      </div>
    </li>
</ul>

  <p class="see-all">
    <a rel="nofollow" href="/artists/236156-elysian-fields/gigography">See all past concerts (321)</a>
  </p>
</div>

      </div>

      <div class="col-4 secondary">
        <div class="component artist-touring-stats">
  <ul>

      <li class="stat">
        <p class="name">Next 1 concert:</p>
        <ul class="info">
            <li><a href="/concerts/30173984-elysian-fields-at-owl-music-parlor">Brooklyn, NY, US</a></li>
        </ul>
      </li>

      <li class="stat">
          <p class="name">Next concert:</p>
          <div class="info next-event next-event-soon">this week</div>
      </li>



      <li class="stat">
        <p class="name">Concerts played in 2017:</p>
        <div class="info">2 concerts</div>
      </li>

        <li class="stat">
          <p class="name">Touring history</p>
          <table class="touring-activity">
                            <tr>
              <td class="touring-year" title="2 concerts">
                  <a href="/artists/236156-elysian-fields/calendar" class="currently-touring">2017</a>
              </td>
              <td class="touring-bar-container" title="2 concerts">
                  <a href="/artists/236156-elysian-fields/calendar" class="currently-touring"><span class="touring-bar" style="width:10%;"></span></a>
              </td>
            </tr>
                            <tr>
              <td class="touring-year" title="20 concerts">
                  2016
              </td>
              <td class="touring-bar-container" title="20 concerts">
                  <span class="touring-bar" style="width:100%;"></span>
              </td>
            </tr>
                            <tr>
              <td class="touring-year" title="8 concerts">
                  2015
              </td>
              <td class="touring-bar-container" title="8 concerts">
                  <span class="touring-bar" style="width:40%;"></span>
              </td>
            </tr>
                            <tr>
              <td class="touring-year" title="18 concerts">
                  2014
              </td>
              <td class="touring-bar-container" title="18 concerts">
                  <span class="touring-bar" style="width:90%;"></span>
              </td>
            </tr>
                            <tr>
              <td class="touring-year" title="7 concerts">
                  2013
              </td>
              <td class="touring-bar-container" title="7 concerts">
                  <span class="touring-bar" style="width:35%;"></span>
              </td>
            </tr>
          </table>
        </li>
      <li class="stat">
        <p class="name">Most played:</p>
        <div class="info">
          <ul>
            <li title="New York">
              <a href="/metro_areas/7644-us-new-york" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">New York</span>
              </a> (113)
            </li>
            <li title="Paris">
              <a href="/metro_areas/28909-france-paris" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">Paris</span>
              </a> (31)
            </li>
            <li title="Los Angeles">
              <a href="/metro_areas/17835-us-los-angeles" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">Los Angeles</span>
              </a> (13)
            </li>
            <li title="Lyon">
              <a href="/metro_areas/28889-france-lyon" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">Lyon</span>
              </a> (9)
            </li>
            <li title="Brussels">
              <a href="/metro_areas/26854-belgium-brussels" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">Brussels</span>
              </a> (9)
            </li>
          </ul>
        </div>
      </li>

    <li class="stat">
      <p class="name">Appears most with:</p>
      <div class="info">
        <ul>
          <li title="Sex Mob"><a href="/artists/23541-sex-mob" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Sex Mob</span></a> (3)
          </li>
          <li title="Chicago Underground Duo"><a href="/artists/329761-chicago-underground-duo" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Chicago Underground Duo</span></a> (2)
          </li>
          <li title="Francoiz Breut"><a href="/artists/35985-francoiz-breut" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Francoiz Breut</span></a> (2)
          </li>
          <li title="Luna"><a href="/artists/110737-luna" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Luna</span></a> (2)
          </li>
          <li title="Vinicius Cantuaria"><a href="/artists/490294-vinicius-cantuaria" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Vinicius Cantuaria</span></a> (2)
          </li>
        </ul>
      </div>
    </li>

    <li class="stat">
      <p class="name">Distance travelled:</p>
      <div class="info distance-travelled">296,302 <span>miles</span></div>
    </li>
  </ul>
</div>

        <div class="component related-artists">
  <h5>Similar artists</h5>
  <ul>
      <li>
        <a class="artist-info" href="/artists/2560701-yeti-lane" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/2560701/avatar" class="artist-profile-image artist" width="40" height="40" alt="Yeti Lane live" title="Yeti Lane live">

  <span class="artist-details">
    <span class="artist-name">Yeti Lane</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="2560701" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="R+2ymE5gkq6NN9l1TC2dqkPIWj1a7qnkPvyXk9N0ANe9jkyxkvG5X85DuBXT1OpByWDYJ6xxN9QyDcTzkow4NA==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="2560701">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/1960171-mesparrow" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/1960171/avatar" class="artist-profile-image artist" width="40" height="40" alt="Mesparrow live" title="Mesparrow live">

  <span class="artist-details">
    <span class="artist-name">Mesparrow</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="1960171" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="4oU+oupOcSf9IK4uINnR4FhHUzm8G2BXxayONRZYZMYY5sCLNt9a1r5Uz06/IKYL0u/RI0qE/mfJXd1VV6BcJQ==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="1960171">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/157342-hburns" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/157342/avatar" class="artist-profile-image artist" width="40" height="40" alt="H-Burns live" title="H-Burns live">

  <span class="artist-details">
    <span class="artist-name">H-Burns</span>
    <span>2 concerts</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="157342" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="iljCm2Ke9JLWBt8hltnYP8LyQv+zvRMWLh7A5pKPeP1wOzyyvg/fY5VyvkEJIK/USFrA5UUijSYi75OG03dAHg==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="157342">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/365992-shannon-wright" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/365992/avatar" class="artist-profile-image artist" width="40" height="40" alt="Shannon Wright live" title="Shannon Wright live">

  <span class="artist-details">
    <span class="artist-name">Shannon Wright</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="365992" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="K4HPBO4gfMhCDWH85vLB5sKZh7iJBXW3VF2LlicgKiPR4jEtMrFXOQF5AJx5C7YNSDEFon+a64dYrNj2ZtgSwA==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="365992">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/202740-mademoiselle-k" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/202740/avatar" class="artist-profile-image artist" width="40" height="40" alt="Mademoiselle K live" title="Mademoiselle K live">

  <span class="artist-details">
    <span class="artist-name">Mademoiselle K</span>
    <span>2 concerts</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="202740" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Gdqwy47uK7Wdb0eQIDq2SH5LjfYjnBjF1LgjlgxDbp3juU7iUn8ARN4bJvC/w8Gj9OMP7NUDhvXYSXD2TbtWfg==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="202740">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/345688-assassin" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/345688/avatar" class="artist-profile-image artist" width="40" height="40" alt="Assassin live" title="Assassin live">

  <span class="artist-details">
    <span class="artist-name">Assassin</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="345688" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="BRnavOm7wrDoU5Q9qRUjJumCcKKDofaTRhjOLLtR1B7/eiSVNSrpQasn9V027FTNYyryuHU+aKNK6Z1M+qns/Q==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="345688">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/1055166-cheveu" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/1055166/avatar" class="artist-profile-image artist" width="40" height="40" alt="Cheveu live" title="Cheveu live">

  <span class="artist-details">
    <span class="artist-name">Cheveu</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="1055166" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="OP3uHX5YfKYQH4uzVbuLJXyjcd/kAIH3A/LS6Sdf31bCnhA0oslXV1Nr6tPKQvzO9gvzxRKfH8cPA4GJZqfntQ==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="1055166">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/133699-rubin-steiner" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/133699/avatar" class="artist-profile-image artist" width="40" height="40" alt="Rubin Steiner live" title="Rubin Steiner live">

  <span class="artist-details">
    <span class="artist-name">Rubin Steiner</span>
    <span>2 concerts</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="133699" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Qax/XLiJW7wbfv8IZIxE/e3nSqAozIiGYu2seOWUntO7z4F1ZBhwTVgKnmj7dTMWZ0/Iut5TFrZuHP8YpGymMA==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="133699">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/375620-casey" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/375620/avatar" class="artist-profile-image artist" width="40" height="40" alt="Casey live" title="Casey live">

  <span class="artist-details">
    <span class="artist-name">Casey</span>
    <span>2 concerts</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="375620" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Ym6TCRtKtRbGnAtK0nmOSxqKqlWpSzUXebWp2sbT38WYDW0gx9ue54XoaipNgPmgkCIoT1/Uqyd1RPq6hyvnJg==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="375620">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/492042-peter-von-poehl" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/492042/avatar" class="artist-profile-image artist" width="40" height="40" alt="Peter Von Poehl live" title="Peter Von Poehl live">

  <span class="artist-details">
    <span class="artist-name">Peter Von Poehl</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="492042" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="W3W9mHIiN5uLRaE5QVPeoLjT4NLkpBe49lnDVoPBIDqhFkOxrrMcasgxwFneqqlLMntiyBI7iYj6qJA2wjkY2Q==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="492042">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
  </ul>
</div>


      </div>
    </div>
  </div>
  <div class="microformat">
    <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicGroup","name":"Elysian Fields","url":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat","image":"https://images.sk-static.com/images/media/profile_images/artists/236156/card_avatar","logo":"https://images.sk-static.com/images/media/profile_images/artists/236156/card_avatar","interactionCount":"5555 UserLikes"}]</script>
  </div>



    <div class="footer-container">
      <div id="footer" class="container footer">
  <div class="row">
    <div class="col-3">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/info/about" rel="nofollow">About us</a></li>
        <li><a href="/partner">Partner with us</a></li>
        <li><a href="/blog" rel="nofollow">Blog</a></li>
        <li><a href="/jobs" rel="nofollow">Jobs</a></li>
        <li><a href="http://support.songkick.com/">Help &amp; FAQ</a></li>
        <li><a href="/leaderboards/popular_artists">Most popular charts</a></li>
      </ul>
    </div>
    <div class="col-3">
      <ul>
        <li><a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=tourboxforartists">Tourbox for artists</a></li>
        <li><a href="/developer"><abbr>API</abbr> information</a></li>
        <li><a href="/info/guidelines" rel="nofollow">Community guidelines</a></li>
        <li><a href="/info/terms" rel="nofollow">Terms of use</a></li>
        <li><a href="/info/privacy" rel="nofollow">Privacy policy</a></li>
        <li><a href="/info/security" rel="nofollow">Security</a></li>
      </ul>
    </div>
    <div class="col-6">
      <div class="tourbox-cta">
        <p>Get your tour dates seen by one billion fans:</p>
        <a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=visitor" class="sign-up-as-an-artist" data-analytics-category="navigation" data-analytics-label="sign_up_tourbox">Sign up as an artist</a>
      </div>
      <div class="social-container">
        <ul class="social-icons">
          <li>
            <a href="https://twitter.com/songkick">
              <img src="//assets.sk-static.com/assets/nw/furniture/icons/twitter-161f1e4.png" width="22" height="18" alt="Twitter">
              &nbsp;<span>Follow us.</span>
            </a>
          </li>
          <li>
            <a href="http://www.facebook.com/songkick">
              <img src="//assets.sk-static.com/assets/nw/furniture/icons/facebook-08359b5.png" width="18" height="18" alt="Facebook">
              &nbsp;<span>Like us.</span>
            </a>
          </li>
          <li>
            <span>But we really hope you love us.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>

    </div>
    <script type="text/javascript" src="//assets.sk-static.com/assets/manifests-1f4433a.js"></script><script type="text/javascript" src="//assets.sk-static.com/assets/app-60e1f1b.js"></script>

    <script type="text/javascript">
      setTimeout(function(){var a=document.createElement("script");
      var b=document.getElementsByTagName("script")[0];
      a.src=document.location.protocol+"//dnn506yrbagrg.cloudfront.net/pages/scripts/0013/4464.js?"+Math.floor(new Date().getTime()/3600000);
      a.async=true;a.type="text/javascript";b.parentNode.insertBefore(a,b)}, 1);
    </script>

  <script type="text/javascript">
    Songkick.EventBus.bind('app:initialize', function() {
      JS.require('jQuery', function() {

        $.cookie('exp_showed_offtour_artist_modal', true, { path: '/'});

        $(document).on('click', 'a.ticket-vendor', function(e) {
          Songkick.EventBus.trigger('ui:click', { category: 'tmp_growth_team_ticket_vendor',
          action: 'logged_out_click',
          label: $(this).data('event-id').toString(),
          value: $(this).data('analytics-value')});
        });
      });
    });
      Songkick.EventBus.bind('app:initialize', function(config) {
        JS.require('jQuery.ui', function() {
          var modal = new Songkick.Component.Modal({
            analytics_category: 'signup_cta',
            analytics_label: '236156',
            analytics_action_prefix: 'artist:no_local:modal',
            cookie_key: 'off-tour-no-local-events-artist-cta',
            modal_class: 'off-tour-no-local-events-artist-cta-container',
            component: '<div class="top-area">  <button class="close-widget close">    <img src="/images/nw/components/vendor-click-signup-cta/close.svg" alt="Close" height="12" width="12">  </button>    <img width="60" height="60" class="artist artist-profile-image" src="//images.sk-static.com/images/media/profile_images/artists/236156/large_avatar" alt="Large avatar" />  <p class="artist-name">Elysian Fields</p>    <p class="upcoming-concerts-status">No concerts near you (Agen, France). </p></div><div class="bottom-area">  <h2 class="be-the-first-to-know">Be the first to know about tickets in the future</h2>  <div class="buttons">    <div class="tracking">  <form data-analytics-category="signup_cta" data-analytics-action="artist:no_local:modal:cta_button" data-analytics-label="236156" data-tracking-text="Yes, please notify me" data-stop-tracking-text="Yes, please notify me" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="NLcfiQwkTtHSLb/vns8y/vUXTGekKmpTNONX//6IfzzO1OGg0LVlIJFZ3o8BNkUVf7/OfVK19GM4EgSfv3BH3w==" />    <input type="hidden" name="relationship_type" value="concerts">    <input type="hidden" name="subject_id" value="236156">    <input type="hidden" name="subject_type" value="Artist">    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">    <input type="hidden" name="app_store_redirect_url" value="">    <button type="submit" class="artist signup-cta" value="Yes, please notify me">Yes, please notify me</button></form></div>  </div>  <p class="artist-trackings">5,555 fans get concert alerts for this artist.</p>  <a class="close-message">I don’t want to hear about tickets</a></div>'
          });
          modal.show(modal);
        });
      });
      Songkick.EventBus.bind('app:initialize', function(config) {
        JS.require('jQuery.ui', function() {
          var modal = new Songkick.Component.Modal({
            analytics_category: 'signup_cta',
            analytics_label: '236156',
            analytics_action_prefix: 'artist:post_tv_click',
            cookie_key: 'vendor-click-cta',
            modal_class: 'vendor-signup-cta-container',
            component: '<div class="top-area">  <button class="close-widget close">    <img src="/images/nw/components/vendor-click-signup-cta/close.svg" alt="Close" height="12" width="12">  </button>    <img alt="Elysian Fields live" width="70" height="70" class="artist artist-profile-image" src="//images.sk-static.com/images/media/profile_images/artists/236156/large_avatar" />  <h2>Still searching for Elysian Fields tickets?</h2>  <p class="be-the-first-to-know">Be the first to know about tickets in the future.</p>  <p class="artist-trackings">5,555 other fans want alerts for this artist.</p></div><div class="bottom-area">  <div class="buttons">    <div class="tracking">  <form data-analytics-category="signup_cta" data-analytics-action="artist:post_tv_click:cta_button" data-analytics-label="236156" data-tracking-text="Yes, please notify me" data-stop-tracking-text="Yes, please notify me" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="JFufWp6unu56RbHkt2Gf2wpGKKqeta/CW+M3NeXnAD3eOGFzQj+1Hzkx0IQomOgwgO6qsGgqMfJXEmRVpB843g==" />    <input type="hidden" name="relationship_type" value="concerts">    <input type="hidden" name="subject_id" value="236156">    <input type="hidden" name="subject_type" value="Artist">    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">    <input type="hidden" name="app_store_redirect_url" value="">    <button type="submit" class="artist signup-cta" value="Yes, please notify me">Yes, please notify me</button></form></div>    <a href="https://itunes.apple.com/us/app/apple-store/id438690886?ct=skweb%3Aartist%3Apost_tv_click%3Aapp_store_bt&amp;mt=8&amp;pt=307660" class="app-store-button" data-analytics-category="signup_cta" data-analytics-action="artist:post_tv_click:app_store_bt" data-analytics-label="236156">      <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/app-store-icon-e56abf8.svg" alt="Available on the App Store" class="store-button">    </a>    <a href="https://play.google.com/store/apps/details?id=com.songkick&amp;referrer=utm_campaign%3Dartist%253Apost_tv_click%253Aapp_store_bt%26utm_medium%3D%26utm_source%3Dskweb" class="google-play-button" data-analytics-category="signup_cta" data-analytics-action="artist:post_tv_click:app_store_bt" data-analytics-label="236156">      <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/play-store-icon-79aae3f.svg" alt="Available on the Play Store" class="store-button">    </a>  </div>  <a class="close-message">I don’t want to hear about tickets</a></div>'
          });
          $('body').on('click', 'a.ticket-vendor.third-party',
            function(e) { modal.show(modal);});
        });
      });
  </script>


<script type="text/javascript">
  Songkick.EventBus.bind('app:initialize', function() {
    Songkick.EventBus.trigger('ui:view', {"category":"artist_page","action":"view_on_tour","label":"no_local_events"});
  });
</script>

<script type="text/javascript">
  /* <![CDATA[ */
  var google_conversion_id = 964669843;
  var google_custom_params = window.google_tag_params;
  var google_remarketing_only = true;
  /* ]]> */
</script>
<script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js">
</script>
<noscript>
  <div style="display:inline;">
  <img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/964669843/?value=0&amp;guid=ON&amp;script=0"/>
  </div>
</noscript>

<script type="text/javascript">
  JS.require("twttr", function() {
    twttr.conversion.trackPid('l6neh', { tw_sale_amount: 0, tw_order_quantity: 0 });
  });
</script>
<noscript>
  <img height="1" width="1" style="display:none;" alt="" src="https://analytics.twitter.com/i/adsct?txn_id=l6neh&amp;p_id=Twitter&amp;tw_sale_amount=0&amp;tw_order_quantity=0" />
  <img height="1" width="1" style="display:none;" alt="" src="//t.co/i/adsct?txn_id=l6neh&amp;p_id=Twitter&amp;tw_sale_amount=0&amp;tw_order_quantity=0" />
</noscript>

<script type="text/javascript">
  SK.logged_in_user = {
    id:null,
    analyticsUserType: 'visitor'
  };

  JS.require("FB", 'jQuery', function() {
    Songkick.Facebook.init(
      "308540029359",
      ["email", "public_profile", "user_friends", "user_likes", "user_actions.music"],
      ["email", "public_profile", "user_friends", "user_likes", "user_actions.music", "publish_actions"],
      {events: Songkick.EventBus}
    );
  });
  var features = {};
  Songkick.EventBus.trigger('app:initialize', {
    events: Songkick.EventBus,
    features: features,
    promoteNativeApp: false,
    mobileSignupRedirectUrl: '',
    mobileAnalyticsEnabled: false,
  });
</script>

    
    <script>
  (function(f,b){
    var c;
    f.hj=f.hj||function(){(f.hj.q=f.hj.q||[]).push(arguments)};
    f._hjSettings={hjid:38507, hjsv:4};
    c=b.createElement("script");c.async=1;
    c.src="//static.hotjar.com/c/hotjar-"+f._hjSettings.hjid+".js?sv="+f._hjSettings.hjsv;
    b.getElementsByTagName("head")[0].appendChild(c); 
  })(window,document);
</script>


  </body>
</html>

```

### `tests/samples/songkick/elysianfields_1.json`

```json
{
    "microdata": [],
    "json-ld": [
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/concerts/30173984-elysian-fields-at-owl-music-parlor?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Brooklyn",
                    "addressCountry": "US",
                    "addressRegion": "NY",
                    "streetAddress": "497 Rogers Ave",
                    "postalCode": "11225"
                },
                "name": "The Owl Music Parlor",
                "sameAs": "http://www.theowl.nyc",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 40.660109,
                    "longitude": -73.953193
                }
            },
            "startDate": "2017-06-10T19:30:00-0400",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Elysian Fields",
                    "sameAs": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
                }
            ]
        },
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/concerts/29673614-elysian-fields-at-hotel-utah-saloon?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "San Francisco",
                    "addressCountry": "US",
                    "addressRegion": "CA",
                    "streetAddress": "500 Fourth Street",
                    "postalCode": "94107"
                },
                "name": "Hotel Utah Saloon",
                "sameAs": "http://www.hotelutah.com/",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 37.7795638,
                    "longitude": -122.398023
                }
            },
            "startDate": "2017-04-26T20:00:00-0700",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Elysian Fields",
                    "sameAs": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Chocolate Genius Inc.",
                    "sameAs": "http://www.songkick.com/artists/1009602-chocolate-genius-inc?utm_medium=organic&utm_source=microformat"
                }
            ]
        },
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/concerts/27626524-elysian-fields-at-le-vip?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Saint-Nazaire",
                    "addressCountry": "France",
                    "streetAddress": "Boulevard de la L\u00e9gion d'Honneur - Base Sous Marine - Alv\u00e9ole 14",
                    "postalCode": "44600"
                },
                "name": "Le VIP",
                "sameAs": "http://www.vip.les-escales.com",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 47.2734979,
                    "longitude": -2.213848
                }
            },
            "startDate": "2016-10-29T21:00:00+0200",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Elysian Fields",
                    "sameAs": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Troy Von Balthazar",
                    "sameAs": "http://www.songkick.com/artists/355304-troy-von-balthazar?utm_medium=organic&utm_source=microformat"
                }
            ]
        },
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/concerts/26734634-elysian-fields-at-le-rocher-de-palmer?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Cenon",
                    "addressCountry": "France",
                    "streetAddress": "1 rue Aristide Briand",
                    "postalCode": "33152"
                },
                "name": "Le Rocher De Palmer",
                "sameAs": "http://lerocherdepalmer.fr/",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 44.8624327,
                    "longitude": -0.5237826
                }
            },
            "startDate": "2016-10-27T20:30:00+0200",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Elysian Fields",
                    "sameAs": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Ernst Reijseger",
                    "sameAs": "http://www.songkick.com/artists/13128-ernst-reijseger?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Troy Von Balthazar",
                    "sameAs": "http://www.songkick.com/artists/355304-troy-von-balthazar?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Rachid Taha",
                    "sameAs": "http://www.songkick.com/artists/100389-rachid-taha?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Vaudou Game",
                    "sameAs": "http://www.songkick.com/artists/8195583-vaudou-game?utm_medium=organic&utm_source=microformat"
                }
            ]
        },
        {
            "@context": "http://schema.org",
            "@type": "MusicGroup",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat",
            "image": "https://images.sk-static.com/images/media/profile_images/artists/236156/card_avatar",
            "logo": "https://images.sk-static.com/images/media/profile_images/artists/236156/card_avatar",
            "interactionCount": "5555 UserLikes"
        }
    ],
    "opengraph": [
        {
            "namespace": {
                "og": "http://ogp.me/ns#",
                "fb": "http://www.facebook.com/2008/fbml",
                "concerts": "http://ogp.me/ns/fb/songkick-concerts#",
                "test1": "http://example.org/test1#",
                "test2": "http://example.org/test2#"
            },
            "properties": [
                [
                    "fb:app_id",
                    "308540029359"
                ],
                [
                    "og:site_name",
                    "Songkick"
                ],
                [
                    "og:type",
                    "songkick-concerts:artist"
                ],
                [
                    "og:title",
                    "Elysian Fields"
                ],
                [
                    "og:description",
                    "Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017."
                ],
                [
                    "og:url",
                    "http://www.songkick.com/artists/236156-elysian-fields"
                ],
                [
                    "og:image",
                    "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg"
                ],
                [
                    "og:image",
                    "http://images.sk-static.com/SECONDARY_IMAGE.jpg"
                ],
                [
                    "test1:image",
                    "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg"
                ],
                [
                    "test1:image",
                    "http://images.sk-static.com/SECONDARY_IMAGE.jpg"
                ],
                [
                    "test2:image",
                    "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg"
                ],
                [
                    "test2:image",
                    "http://images.sk-static.com/SECONDARY_IMAGE.jpg"
                ]
            ]
        }
    ],
    "microformat": [],
    "rdfa": [
        {
            "@id": "http://www.songkick.com/artists/236156-elysian-fields",
            "al:ios:app_name": [
                {
                    "@value": "Songkick Concerts"
                }
            ],
            "al:ios:app_store_id": [
                {
                    "@value": "438690886"
                }
            ],
            "al:ios:url": [
                {
                    "@value": "songkick://artists/236156-elysian-fields"
                }
            ],
            "http://example.org/test1#image": [ 
                { 
                    "@value": "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg"
                },
                { 
                    "@value": "http://images.sk-static.com/SECONDARY_IMAGE.jpg"
                }
            ],
            "http://example.org/test2#image": [ 
                { 
                    "@value": "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg"
                },
                { 
                    "@value": "http://images.sk-static.com/SECONDARY_IMAGE.jpg"
                }
            ],
            "http://ogp.me/ns#description": [
                {
                    "@value": "Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017."
                }
            ],
            "http://ogp.me/ns#image": [
                {
                    "@value": "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg"
                },
                {
                    "@value": "http://images.sk-static.com/SECONDARY_IMAGE.jpg"
                }
            ],
            "http://ogp.me/ns#site_name": [
                {
                    "@value": "Songkick"
                }
            ],
            "http://ogp.me/ns#title": [
                {
                    "@value": "Elysian Fields"
                }
            ],
            "http://ogp.me/ns#type": [
                {
                    "@value": "songkick-concerts:artist"
                }
            ],
            "http://ogp.me/ns#url": [
                {
                    "@value": "http://www.songkick.com/artists/236156-elysian-fields"
                }
            ],
            "http://www.facebook.com/2008/fbmlapp_id": [
                {
                    "@value": "308540029359"
                }
            ]
        }
    ]
}

```

### `tests/samples/songkick/elysianfields.html`

```html
<!DOCTYPE html>
<html lang="en" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml">
  <head prefix="og: http://ogp.me/ns# fb: http://www.facebook.com/2008/fbml songkick-concerts: http://ogp.me/ns/fb/songkick-concerts#">
    <link rel="stylesheet" type="text/css" href="//assets.sk-static.com/assets/artist-8005aab.css">
    <script type="text/javascript">
  SK = typeof(SK) == 'undefined' ? {} : SK;
  SK_ASSET_HOST = "//assets.sk-static.com";
  SK_DYNAMIC_ASSET_HOST = "http://images.sk-static.com";
  CX_EXPERIMENT_ID = "";
  CX_VARIATION_ID = -2;
</script>

    <title>Elysian Fields Tickets, Tour Dates 2017 &amp; Concerts – Songkick</title>
    <link href="//images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg" rel="image_src">
    <link rel="shortcut icon" type="image/x-icon" href="//assets.sk-static.com/images/favicon.ico" />
    <link href="//assets.sk-static.com/images/apple-touch-icon.png" rel="apple-touch-icon">
    <link href="//assets.sk-static.com/images/apple-touch-icon.png" rel="apple-touch-icon-precomposed">
    <meta name="robots" content="all">
    <link href="http://www.songkick.com/artists/236156-elysian-fields" rel="canonical">
        <meta property="al:ios:url" content="songkick://artists/236156-elysian-fields">
    <meta property="al:ios:app_store_id" content="438690886">
    <meta property="al:ios:app_name" content="Songkick Concerts">
    <meta name="description" content="Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017.">
    <meta property="fb:app_id" content="308540029359">
    <meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0, width=device-width">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta property="og:site_name" content="Songkick">
    <meta property="og:type" content="songkick-concerts:artist">
    <meta property="og:title" content="Elysian Fields">
    <meta property="og:description" content="Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017.">
    <meta property="og:url" content="http://www.songkick.com/artists/236156-elysian-fields">
    <meta property="og:image" content="http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg">
    <meta property="og:image" content="http://images.sk-static.com/SECONDARY_IMAGE.jpg">
  </head>
  <body>
    <script>
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
  document,'script','//connect.facebook.net/en_US/fbevents.js');
  fbq('init', '583609881778767');
  fbq('track', 'PageView');
</script>
<noscript>
  <img height="1" width="1" alt="" style="display:none" src="https://www.facebook.com/tr?id=583609881778767&amp;ev=PageView&amp;noscript=1" />
</noscript>

    <div id="fb-root"></div>

    
    
    <div class="track-alert js-track-alert ">
  <div class="track-alert-inner">
    This event has been added to your <a data-analytics-category="navigation_your_plans" data-analytics-label="feedback_your_plans" href="/calendar?filter=attendance">Plans</a>.
    <a class="track-alert-dismiss js-track-alert-dismiss">Close</a>
  </div>
</div>


    <div class="navigation">
        <div class="navigation-large-screen">
  <ul class="nav-bar">
    <li class="sub-nav">
      <ul>
        <li class="logo"><a href="/" data-analytics-category="navigation" data-analytics-label="logo"><img src="//assets.sk-static.com/assets/nw/furniture/songkick-logo-ac43b7a.svg" height="26" width="90" alt="songkick"></a>
        </li><li class="metro-area menu hover-for-touch">
          <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area" title="Agen concerts">Agen concerts</a>
          <div class="menu-content empty-menu">
            <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="popular_tickets"><span>Popular tickets in Agen</span></a>
            <a class="repeat" href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area">Agen concerts</a>
              <a href="/metro_areas/94426-france-agen" data-analytics-category="navigation" data-analytics-label="metro_area_see_all">See all Agen concerts</a> <a class="change-location" data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">(Change&nbsp;location)</a><br><br>
              <a data-analytics-category="navigation" data-analytics-label="metro_area_today" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=06%2F06%2F2017&amp;filters%5BminDate%5D=06%2F06%2F2017#date-filter-form">Today ·</a> <a data-analytics-category="navigation" data-analytics-label="metro_area_7days" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=06%2F13%2F2017&amp;filters%5BminDate%5D=06%2F06%2F2017#date-filter-form">Next 7 days ·</a> <a data-analytics-category="navigation" data-analytics-label="metro_area_month" href="/metro_areas/94426-france-agen?filters%5BmaxDate%5D=07%2F06%2F2017&amp;filters%5BminDate%5D=06%2F06%2F2017#date-filter-form">Next 30 days</a>
          </div>
        </li>
        <li class="artists menu hover-for-touch">
            <a href="/leaderboards/popular_artists" data-analytics-category="navigation" data-analytics-label="artists">Artists</a>
          <div class="menu-content">
              <ul class="artists-navigation">
<li class="col"><a href="/leaderboards/popular_artists" data-analytics-category="navigation" data-analytics-label="popular_artists">Most popular artists worldwide</a></li>
  <li class="col"><a href="/leaderboards/trending_artists" data-analytics-category="navigation" data-analytics-label="trending_artists">Trending artists worldwide</a></li>
</ul>
<div class="listing">
    <ul class="col popular-artists">
        <li>
          <a href="/artists/197928-coldplay" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/197928/avatar" width="35" height="35" class="artist-profile-image artist" alt="Coldplay live">
            <span class="name">Coldplay</span>
          </a>
        </li>
        <li>
          <a href="/artists/313388-u2" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/313388/avatar" width="35" height="35" class="artist-profile-image artist" alt="U2 live">
            <span class="name">U2</span>
          </a>
        </li>
        <li>
          <a href="/artists/139648-rihanna" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/139648/avatar" width="35" height="35" class="artist-profile-image artist" alt="Rihanna live">
            <span class="name">Rihanna</span>
          </a>
        </li>
        <li>
          <a href="/artists/182968-eminem" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/182968/avatar" width="35" height="35" class="artist-profile-image artist" alt="Eminem live">
            <span class="name">Eminem</span>
          </a>
        </li>
        <li>
          <a href="/artists/537914-adele" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/537914/avatar" width="35" height="35" class="artist-profile-image artist" alt="Adele live">
            <span class="name">Adele</span>
          </a>
        </li>
        <li>
          <a href="/artists/181875-maroon-5" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/181875/avatar" width="35" height="35" class="artist-profile-image artist" alt="Maroon 5 live">
            <span class="name">Maroon 5</span>
          </a>
        </li>
        <li>
          <a href="/artists/556955-drake" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/556955/avatar" width="35" height="35" class="artist-profile-image artist" alt="Drake live">
            <span class="name">Drake</span>
          </a>
        </li>
        <li>
          <a href="/artists/552177-kanye-west" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/552177/avatar" width="35" height="35" class="artist-profile-image artist" alt="Kanye West live">
            <span class="name">Kanye West</span>
          </a>
        </li>
        <li>
          <a href="/artists/1134363-katy-perry" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/1134363/avatar" width="35" height="35" class="artist-profile-image artist" alt="Katy Perry live">
            <span class="name">Katy Perry</span>
          </a>
        </li>
        <li>
          <a href="/artists/941964-bruno-mars" data-analytics-category="navigation" data-analytics-label="artists_popular_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/941964/avatar" width="35" height="35" class="artist-profile-image artist" alt="Bruno Mars live">
            <span class="name">Bruno Mars</span>
          </a>
        </li>
    </ul>
    <ul class="col popular-artists">
        <li>
          <a href="/artists/9063689-starley" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/9063689/avatar" width="35" height="35" class="artist-profile-image artist" alt="Starley live">
            <span class="name">Starley</span>
          </a>
        </li>
        <li>
          <a href="/artists/8997064-xxxtentacion" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/8997064/avatar" width="35" height="35" class="artist-profile-image artist" alt="XXXTentacion live">
            <span class="name">XXXTentacion</span>
          </a>
        </li>
        <li>
          <a href="/artists/9031399-ozuna" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/9031399/avatar" width="35" height="35" class="artist-profile-image artist" alt="Ozuna live">
            <span class="name">Ozuna</span>
          </a>
        </li>
        <li>
          <a href="/artists/894756-khalid" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/894756/avatar" width="35" height="35" class="artist-profile-image artist" alt="Khalid live">
            <span class="name">Khalid</span>
          </a>
        </li>
        <li>
          <a href="/artists/241457-nav" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
            <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/241457/avatar" width="35" height="35" class="artist-profile-image artist" alt="NAV live">
            <span class="name">NAV</span>
          </a>
        </li>
    </ul>
</div>

            <div class="tourbox-cta">
              Get your tour dates seen by one billion fans: <a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=visitor" class="sign-up-as-an-artist" data-analytics-category="navigation" data-analytics-label="sign_up_tourbox">Sign up as an artist</a>
            </div>
          </div>
        </li>
        <li class="location">
          <a data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">Change&nbsp;location</a>
        </li>
      </ul>
    <li class="sub-nav">
      <ul>
        <li class="search">
          <form name="search" class="navigation-search-form" data-analytics-category="navigation" data-analytics-label="search" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="hidden" name="type" value="initial">
  <input name="query" type="search" value="" class="text navigation-search" placeholder="Enter artist / concert / venue"><button class="search-button" name="commit" type="submit"><img src="//assets.sk-static.com/assets/nw/components/navigation-large-screen/search-5510d8d.svg" height="15" width="14" alt="search" class="navigation-submit"></button>
</form>
        </li>
        <li class="login-signup">
          <a href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fartists%2F236156-elysian-fields&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" class="signup-link" data-signup-source="Everything else" data-analytics-category="navigation" data-analytics-label="sign_up">Sign up</a> <small>or</small> <a href="https://accounts.songkick.com/session/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fartists%2F236156-elysian-fields&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" data-analytics-category="navigation" data-analytics-label="log_in">Log in</a>
        </li>
      </ul>
    </li>
  </ul>
</div>

        <div class="global-navigation">
  <ul id='global-navigation-list'>
    <li class="nav-icon"><a href="#nav-icon-toggle"><img src="//assets.sk-static.com/assets/nw/components/navigation/profile-menu-icon-b6e2b51.png" width="26" height="19" alt="Show navigation"></a></li>
    <li id="nav-icon-toggle" class="nav"></li>
    <li class="signup"><a href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fartists%2F236156-elysian-fields&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" class="signup-link" data-signup-source="Everything else" data-analytics-category="navigation" data-analytics-label="sign_up" data-auto-signup-redirect-url="https://itunes.apple.com/us/app/apple-store/id438690886?ct=%3A&amp;mt=8&amp;pt=307660">Sign up</a></li>
    <li><a href="https://accounts.songkick.com/session/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fartists%2F236156-elysian-fields&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" data-analytics-category="navigation_small_screen" data-analytics-label="log_in">Log in</a></li>
  </ul>
  <a href="/" id="logo" data-analytics-category="navigation_small_screen" data-analytics-label="logo"><img src="//assets.sk-static.com/assets/nw/components/navigation/header-logo-ff8507a.png" alt="Songkick" width="124" height="32"></a>
</div>
<div class="local-navigation">
  <ul>
    <li class="nav-icon"><a href="#home"><img src="//assets.sk-static.com/assets/nw/components/navigation/local-navigation/navigation-icon-2eeeafe.png" width="22" height="15" alt="Show navigation"></a></li><li class="nav-icon search-nav"><label><a href="#search"><img src="//assets.sk-static.com/assets/nw/components/navigation/local-navigation/search-5cac59e.png" height="20" width="20" alt="search"></a></label></li>
    <li class="site-search" id="search">
      <form name="search" class="navigation-search-form" data-analytics-category="navigation" data-analytics-label="search" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="hidden" name="type" value="initial">
  <input name="query" type="search" value="" class="text navigation-search" placeholder="Enter artist / concert / venue"><button class="search-button" name="commit" type="submit"><img src="//assets.sk-static.com/assets/nw/components/navigation-large-screen/search-5510d8d.svg" height="15" width="14" alt="search" class="navigation-submit"></button>
</form>
    </li>
    <li class="home nav" id="home">
      <a data-analytics-category="navigation" data-analytics-label="home" href="/">Home</a>
    </li><li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="metro_area" href="/metro_areas/94426-france-agen">Agen concerts</a>
    </li><li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">Change&nbsp;location</a>
    </li><li>
      <a href="/leaderboards/popular_artists" data-analytics-catigory="navigation" data-analytics-label="popular_artists">Popular artists</a>
    </li>
  </ul>
</div>

    </div>

      <div class="artist-header">
      <div class="row component brief">

  <div class="col-8 primary">
    <h1 class="h0">Elysian Fields
    </h1>


    <ul>
          <li class="ontour">On tour: <strong>yes</strong></li>


              <li class="no-event-nearby">Elysian Fields is not playing near you. <a href="/artists/236156-elysian-fields/calendar">View all concerts</a></li>
                <li class="change-location">Agen, France <a href="/session/filter_metro_area?success_url=/artists/236156-elysian-fields">Change location</a></li>
    </ul>

    <div class="signup-cta-container">
      <h4>Be the first to know when they tour near you.</h4>

        <p>5,555 fans get concert alerts for this artist.</p>

      <div class="track-artist">
        <div class="tracking">
  <form data-analytics-category="signup_cta" data-analytics-action="artist:no_local:cta_button" data-analytics-label="236156" data-tracking-text="Yes, please notify me" data-stop-tracking-text="Yes, please notify me" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="O8P3WbKBJnc0/j6cQhZ/nPUqu84tZgd4v3uyieEk6f3BoAlwbhANhneKX/zd7wh3f4I51Nv5mUiziuHpoNzRHg==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="236156">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist signup-cta" value="Yes, please notify me">Yes, please notify me</button>
</form></div>

      </div>

      <div class="app-store-buttons">
        <a href="https://itunes.apple.com/us/app/apple-store/id438690886?ct=skweb%3Aartist%3Ano_local%3Aapp_store_bt&amp;mt=8&amp;pt=307660" class="app-store-button" data-analytics-category="signup_cta" data-analytics-action="artist:no_local:app_store_bt" data-analytics-label="236156">
          <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/app-store-icon-e56abf8.svg" alt="Available on the App Store" class="store-button">
        </a>
        <a href="https://play.google.com/store/apps/details?id=com.songkick&amp;referrer=utm_campaign%3Dartist%253Ano_local%253Aapp_store_bt%26utm_medium%3D%26utm_source%3Dskweb" class="google-play-button" data-analytics-category="signup_cta" data-analytics-action="artist:no_local:app_store_bt" data-analytics-label="236156">
          <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/play-store-icon-79aae3f.svg" alt="Available on the Play Store" class="store-button">
        </a>
      </div>
    </div>
  </div>

  <div class="col-4 profile-picture-wrap">
    <a href="/images/1027156" class="media-link" rel="nofollow" data-analytics-category="artist_brief" data-analytics-label="profile_image">
    <span class="on-tour">On tour</span>
    <img alt="Elysian Fields live" width="300" height="300" class="artist artist-profile-image" src="//images.sk-static.com/images/media/profile_images/artists/236156/huge_avatar" /></a>
  </div>

</div>

  </div>

  <div class="container">
    <div class="row">
      <div class="col-8 primary">
        
        
        <div class="component events-summary" id="calendar-summary">
  <h2 class="calendar">Upcoming concerts (1)</h2>
  <ul class="event-listings artist-focus">
         <li class="with-date">
           <strong>
            <time datetime="2017-06-10T19:30:00-0400">Saturday 10 June 2017</time>
           </strong>
         </li>

    <li title="Saturday 10 June 2017">
      <time datetime="2017-06-10T19:30:00-0400"></time>


      <p class="artists summary">
        <a href="/concerts/30173984-elysian-fields-at-owl-music-parlor">
          <span>
            <strong>Elysian Fields</strong>
              
          </span>
        </a>
      </p>

      <p class="location">
          <span class="venue-name"><a href="/venues/3134004-owl-music-parlor">The Owl Music Parlor</a></span>,
        <span>
          <span>
            Brooklyn, NY, US
          </span>
            <span class="street-address">497 Rogers Ave</span>
        </span>
      </p>

        <a href="/concerts/30173984-elysian-fields-at-owl-music-parlor">
          <span class="button buy-tickets">Buy&nbsp;tickets</span>
        </a>

      <div class="attendance">
  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;Track event&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;Track event&lt;/span&gt;" data-subject-upcoming="true" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="767qnpwQlkgUuKODLZYcRasCLB+PPGMobmUkzZ3dPKYVzRS3QIG9uVfMwuOyb2uuIaquBXmj/RhilHet3CUERQ==" />
    <input type="hidden" name="relationship_type" value="tracking">
    <input type="hidden" name="subject_id" value="30173984">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="tracking attendance-action" value="Track event"><span class="icon"></span><span class="button-text">Track event</span></button>
</form>  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I’m going&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I’m going&lt;/span&gt;" data-subject-upcoming="true" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="bHa1xBgq7RsVINQWP5oljmiqKYvbXRFTKSAOICT/mzuWFUvtxLvG6lZUtXagY1Jl4gKrkS3Cj2Ml0V1AZQej2A==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="30173984">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I’m going"><span class="icon"></span><span class="button-text">I’m going</span></button>
</form></div>

          <div class="attendance-tray">
    <h6>Don’t miss out.</h6>
    <p>Track this event and we’ll remind you when it’s coming up.</p>
  </div>


      <div class="microformat">
        <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/30173984-elysian-fields-at-owl-music-parlor?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Brooklyn","addressCountry":"US","addressRegion":"NY","streetAddress":"497 Rogers Ave","postalCode":"11225"},"name":"The Owl Music Parlor","sameAs":"http://www.theowl.nyc","geo":{"@type":"GeoCoordinates","latitude":40.660109,"longitude":-73.953193}},"startDate":"2017-06-10T19:30:00-0400","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
      </div>
    </li>
</ul>

</div>

        
        
        
        <div class="component media-summary">

    <div class="media-group videos">
  <h2>Videos (5)</h2>
    <div class="video-standfirst">
      <span class="icon-expand">
        <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
      </span>
      <iframe width="480" height="295" src="//www.youtube.com/embed/eLEhs86urK4"></iframe>
    </div>
  <ul class="media-set videos inview" data-url="/artists/236156-elysian-fields/videos" data-per-page="4" data-total="5">
    <li>
      <div class="media-element">
  <a href="/videos/22325526" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/eLEhs86urK4" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/eLEhs86urK4/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>
<div class="media-element">
  <a href="/videos/20966736" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/Tv-yeHo_1vQ" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/Tv-yeHo_1vQ/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>
<div class="media-element">
  <a href="/videos/19297127" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/3WiS3ZOAtXE" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/3WiS3ZOAtXE/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>
<div class="media-element">
  <a href="/videos/16882242" class="media-link" rel="nofollow" data-embed-path="//www.youtube.com/embed/Us26gmtuf38" data-analytics-category="media_summary" data-analytics-label="video">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>
    <span class="icon-play">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-play.svg" alt="expand" height="18" width="18">
    </span>

    <img src="//i2.ytimg.com/vi/Us26gmtuf38/0.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="215" height="105">
  </a>
</div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#videos" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="see_all_videos">
      See all videos (5)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_videos_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_videos_next">
    </button>
  </nav>
</div>

    <div class="media-group">
  <h2>Photos (3)</h2>
  <ul class="media-set images inview" data-url="/artists/236156-elysian-fields/images" data-per-page="12" data-total="3">
    <li>
      <div class="media-element media-element-square">
  <a class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="photo" href="/images/19297137">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="163" style="margin-top: -81px; margin-left: -110px;
            min-height: 140px;" src="http://images.sk-static.com/images/media/img/col3/20160514-193706-150385.jpg" />
</a></div>
<div class="media-element media-element-square">
  <a class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="photo" href="/images/16586462">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="217" style="margin-top: -108px; margin-left: -110px;
            min-height: 140px;" src="http://images.sk-static.com/images/media/img/col3/20150925-054405-780997.jpg" />
</a></div>
<div class="media-element media-element-square">
  <a class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="photo" href="/images/1027156">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="164" style="margin-top: -82px; margin-left: -110px;
            min-height: 140px;" src="http://images.sk-static.com/images/media/img/col3/20100330-103600-169450.jpg" />
</a></div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#images" data-analytics-category="media_summary" data-analytics-label="see_all_photos">
      See all photos (3)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_photos_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_photos_next">
    </button>
  </nav>
</div>

    <div class="media-group posters">
  <h2>Posters (8)</h2>
  <ul class="media-set posters inview" data-url="/artists/236156-elysian-fields/posters" data-per-page="8" data-total="8">
    <li>
      <div class="media-element">
  <a href="/posters/19867181" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20160630-152543-052433.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="335">
  </a>
</div>
<div class="media-element">
  <a href="/posters/19297192" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20160514-194215-603498.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="139">
  </a>
</div>
<div class="media-element">
  <a href="/posters/16882227" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20151024-190306-422584.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="142">
  </a>
</div>
<div class="media-element">
  <a href="/posters/16882157" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20151024-185802-067024.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="220">
  </a>
</div>
<div class="media-element">
  <a href="/posters/16881532" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20151024-175107-333162.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="284">
  </a>
</div>
<div class="media-element">
  <a href="/posters/8207099" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20130330-164629-584505.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="330">
  </a>
</div>
<div class="media-element">
  <a href="/posters/7693414" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20130131-161630-788528.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="329">
  </a>
</div>
<div class="media-element">
  <a href="/posters/4271263" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20111011-050815-789254.jpg" class="media-img" alt="Elysian Fields live" title="Elysian Fields live" width="220" height="330">
  </a>
</div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#posters" data-analytics-category="media_summary" data-analytics-label="see_all_posters">
      See all posters (8)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_posters_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_posters_next">
    </button>
  </nav>
</div>

</div>

          <div class="component events-summary" id="gigography-summary">
  <h2 class="calendar">Past concerts (321) <small><a rel="nofollow" href="/artists/236156-elysian-fields/gigography">See all</a></small></h2>
  <ul class="event-listings artist-focus">
         <li class="with-date">
           <strong>
            <time datetime="2017-04-26T20:00:00-0700">Wednesday 26 April 2017</time>
           </strong>
         </li>

    <li title="Wednesday 26 April 2017">
      <time datetime="2017-04-26T20:00:00-0700"></time>


      <p class="artists summary">
        <a href="/concerts/29673614-elysian-fields-at-hotel-utah-saloon" rel="nofollow">
          <span>
            <strong>Elysian Fields</strong>
              with Chocolate Genius Inc.
          </span>
        </a>
      </p>

      <p class="location">
          <span class="venue-name"><a href="/venues/328-hotel-utah-saloon">Hotel Utah Saloon</a></span>,
        <span>
          <span>
            San Francisco, CA, US
          </span>
            <span class="street-address">500 Fourth Street</span>
        </span>
      </p>


      <div class="attendance was-there">
  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="h1csHSIgrRXIoaF9kVWNd/k2iPlsml9Ch0fLOpVn/E59NNI0/rGG5IvVwB0OrPqcc54K45oFwXKLtpha1J/ErQ==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="29673614">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I was there"><span class="icon"></span><span class="button-text">I was there</span></button>
</form></div>

        

      <div class="microformat">
        <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/29673614-elysian-fields-at-hotel-utah-saloon?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"San Francisco","addressCountry":"US","addressRegion":"CA","streetAddress":"500 Fourth Street","postalCode":"94107"},"name":"Hotel Utah Saloon","sameAs":"http://www.hotelutah.com/","geo":{"@type":"GeoCoordinates","latitude":37.7795638,"longitude":-122.398023}},"startDate":"2017-04-26T20:00:00-0700","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Chocolate Genius Inc.","sameAs":"http://www.songkick.com/artists/1009602-chocolate-genius-inc?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
      </div>
    </li>
         <li class="with-date">
           <strong>
            <time datetime="2016-10-29T21:00:00+0200">Saturday 29 October 2016</time>
           </strong>
         </li>

    <li title="Saturday 29 October 2016">
      <time datetime="2016-10-29T21:00:00+0200"></time>


      <p class="artists summary">
        <a href="/concerts/27626524-elysian-fields-at-le-vip" rel="nofollow">
          <span>
            <strong>Elysian Fields</strong>
              
          </span>
        </a>
      </p>

      <p class="location">
          <span class="venue-name"><a href="/venues/1972419-le-vip">Le VIP</a></span>,
        <span>
          <span>
            Saint-Nazaire, France
          </span>
            <span class="street-address">Boulevard de la Légion d&#39;Honneur - Base Sous Marine - Alvéole 14</span>
        </span>
      </p>


      <div class="attendance was-there">
  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="BVbd+XsRf1lrCbQdNn49hdNM2MUB/Nfo3vvWnidfqAX/NSPQp4BUqCh91X2ph0puWeRa3/djSdjSCoX+ZqeQ5g==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="27626524">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I was there"><span class="icon"></span><span class="button-text">I was there</span></button>
</form></div>


      <div class="microformat">
        <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/27626524-elysian-fields-at-le-vip?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Saint-Nazaire","addressCountry":"France","streetAddress":"Boulevard de la Légion d'Honneur - Base Sous Marine - Alvéole 14","postalCode":"44600"},"name":"Le VIP","sameAs":"http://www.vip.les-escales.com","geo":{"@type":"GeoCoordinates","latitude":47.2734979,"longitude":-2.213848}},"startDate":"2016-10-29T21:00:00+0200","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Troy Von Balthazar","sameAs":"http://www.songkick.com/artists/355304-troy-von-balthazar?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
      </div>
    </li>
         <li class="with-date">
           <strong>
            <time datetime="2016-10-27T20:30:00+0200">Thursday 27 October 2016</time>
           </strong>
         </li>

    <li title="Thursday 27 October 2016">
      <time datetime="2016-10-27T20:30:00+0200"></time>


      <p class="artists summary">
        <a href="/concerts/26734634-elysian-fields-at-le-rocher-de-palmer" rel="nofollow">
          <span>
            <strong>Elysian Fields</strong>
              
          </span>
        </a>
      </p>

      <p class="location">
          <span class="venue-name"><a href="/venues/1080416-le-rocher-de-palmer">Le Rocher De Palmer</a></span>,
        <span>
          <span>
            Cenon, France
          </span>
            <span class="street-address">1 rue Aristide Briand</span>
        </span>
      </p>


      <div class="attendance was-there">
  <form class="attendance app-store-redirect auto-signup" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="+rMMR0nsxQghwbSbUlSvmPU98KzNXvUXPmPKG8I5ftgA0PJulX3u+WK11fvNrdhzf5VytjvBaycykpl7g8FGOw==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="26734634">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I was there"><span class="icon"></span><span class="button-text">I was there</span></button>
</form></div>


      <div class="microformat">
        <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Elysian Fields","url":"http://www.songkick.com/concerts/26734634-elysian-fields-at-le-rocher-de-palmer?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Cenon","addressCountry":"France","streetAddress":"1 rue Aristide Briand","postalCode":"33152"},"name":"Le Rocher De Palmer","sameAs":"http://lerocherdepalmer.fr/","geo":{"@type":"GeoCoordinates","latitude":44.8624327,"longitude":-0.5237826}},"startDate":"2016-10-27T20:30:00+0200","performer":[{"@type":"MusicGroup","name":"Elysian Fields","sameAs":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Ernst Reijseger","sameAs":"http://www.songkick.com/artists/13128-ernst-reijseger?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Troy Von Balthazar","sameAs":"http://www.songkick.com/artists/355304-troy-von-balthazar?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Rachid Taha","sameAs":"http://www.songkick.com/artists/100389-rachid-taha?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Vaudou Game","sameAs":"http://www.songkick.com/artists/8195583-vaudou-game?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
      </div>
    </li>
</ul>

  <p class="see-all">
    <a rel="nofollow" href="/artists/236156-elysian-fields/gigography">See all past concerts (321)</a>
  </p>
</div>

      </div>

      <div class="col-4 secondary">
        <div class="component artist-touring-stats">
  <ul>

      <li class="stat">
        <p class="name">Next 1 concert:</p>
        <ul class="info">
            <li><a href="/concerts/30173984-elysian-fields-at-owl-music-parlor">Brooklyn, NY, US</a></li>
        </ul>
      </li>

      <li class="stat">
          <p class="name">Next concert:</p>
          <div class="info next-event next-event-soon">this week</div>
      </li>



      <li class="stat">
        <p class="name">Concerts played in 2017:</p>
        <div class="info">2 concerts</div>
      </li>

        <li class="stat">
          <p class="name">Touring history</p>
          <table class="touring-activity">
                            <tr>
              <td class="touring-year" title="2 concerts">
                  <a href="/artists/236156-elysian-fields/calendar" class="currently-touring">2017</a>
              </td>
              <td class="touring-bar-container" title="2 concerts">
                  <a href="/artists/236156-elysian-fields/calendar" class="currently-touring"><span class="touring-bar" style="width:10%;"></span></a>
              </td>
            </tr>
                            <tr>
              <td class="touring-year" title="20 concerts">
                  2016
              </td>
              <td class="touring-bar-container" title="20 concerts">
                  <span class="touring-bar" style="width:100%;"></span>
              </td>
            </tr>
                            <tr>
              <td class="touring-year" title="8 concerts">
                  2015
              </td>
              <td class="touring-bar-container" title="8 concerts">
                  <span class="touring-bar" style="width:40%;"></span>
              </td>
            </tr>
                            <tr>
              <td class="touring-year" title="18 concerts">
                  2014
              </td>
              <td class="touring-bar-container" title="18 concerts">
                  <span class="touring-bar" style="width:90%;"></span>
              </td>
            </tr>
                            <tr>
              <td class="touring-year" title="7 concerts">
                  2013
              </td>
              <td class="touring-bar-container" title="7 concerts">
                  <span class="touring-bar" style="width:35%;"></span>
              </td>
            </tr>
          </table>
        </li>
      <li class="stat">
        <p class="name">Most played:</p>
        <div class="info">
          <ul>
            <li title="New York">
              <a href="/metro_areas/7644-us-new-york" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">New York</span>
              </a> (113)
            </li>
            <li title="Paris">
              <a href="/metro_areas/28909-france-paris" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">Paris</span>
              </a> (31)
            </li>
            <li title="Los Angeles">
              <a href="/metro_areas/17835-us-los-angeles" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">Los Angeles</span>
              </a> (13)
            </li>
            <li title="Lyon">
              <a href="/metro_areas/28889-france-lyon" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">Lyon</span>
              </a> (9)
            </li>
            <li title="Brussels">
              <a href="/metro_areas/26854-belgium-brussels" data-analytics-category="touring_stats" data-analytics-label="most_played_cities">
                <span class="truncated-long">Brussels</span>
              </a> (9)
            </li>
          </ul>
        </div>
      </li>

    <li class="stat">
      <p class="name">Appears most with:</p>
      <div class="info">
        <ul>
          <li title="Sex Mob"><a href="/artists/23541-sex-mob" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Sex Mob</span></a> (3)
          </li>
          <li title="Chicago Underground Duo"><a href="/artists/329761-chicago-underground-duo" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Chicago Underground Duo</span></a> (2)
          </li>
          <li title="Francoiz Breut"><a href="/artists/35985-francoiz-breut" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Francoiz Breut</span></a> (2)
          </li>
          <li title="Luna"><a href="/artists/110737-luna" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Luna</span></a> (2)
          </li>
          <li title="Vinicius Cantuaria"><a href="/artists/490294-vinicius-cantuaria" data-analytics-category="touring_stats" data-analytics-label="appears_most_with">
            <span class="truncated-long">Vinicius Cantuaria</span></a> (2)
          </li>
        </ul>
      </div>
    </li>

    <li class="stat">
      <p class="name">Distance travelled:</p>
      <div class="info distance-travelled">296,302 <span>miles</span></div>
    </li>
  </ul>
</div>

        <div class="component related-artists">
  <h5>Similar artists</h5>
  <ul>
      <li>
        <a class="artist-info" href="/artists/2560701-yeti-lane" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/2560701/avatar" class="artist-profile-image artist" width="40" height="40" alt="Yeti Lane live" title="Yeti Lane live">

  <span class="artist-details">
    <span class="artist-name">Yeti Lane</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="2560701" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="R+2ymE5gkq6NN9l1TC2dqkPIWj1a7qnkPvyXk9N0ANe9jkyxkvG5X85DuBXT1OpByWDYJ6xxN9QyDcTzkow4NA==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="2560701">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/1960171-mesparrow" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/1960171/avatar" class="artist-profile-image artist" width="40" height="40" alt="Mesparrow live" title="Mesparrow live">

  <span class="artist-details">
    <span class="artist-name">Mesparrow</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="1960171" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="4oU+oupOcSf9IK4uINnR4FhHUzm8G2BXxayONRZYZMYY5sCLNt9a1r5Uz06/IKYL0u/RI0qE/mfJXd1VV6BcJQ==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="1960171">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/157342-hburns" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/157342/avatar" class="artist-profile-image artist" width="40" height="40" alt="H-Burns live" title="H-Burns live">

  <span class="artist-details">
    <span class="artist-name">H-Burns</span>
    <span>2 concerts</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="157342" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="iljCm2Ke9JLWBt8hltnYP8LyQv+zvRMWLh7A5pKPeP1wOzyyvg/fY5VyvkEJIK/USFrA5UUijSYi75OG03dAHg==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="157342">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/365992-shannon-wright" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/365992/avatar" class="artist-profile-image artist" width="40" height="40" alt="Shannon Wright live" title="Shannon Wright live">

  <span class="artist-details">
    <span class="artist-name">Shannon Wright</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="365992" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="K4HPBO4gfMhCDWH85vLB5sKZh7iJBXW3VF2LlicgKiPR4jEtMrFXOQF5AJx5C7YNSDEFon+a64dYrNj2ZtgSwA==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="365992">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/202740-mademoiselle-k" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/202740/avatar" class="artist-profile-image artist" width="40" height="40" alt="Mademoiselle K live" title="Mademoiselle K live">

  <span class="artist-details">
    <span class="artist-name">Mademoiselle K</span>
    <span>2 concerts</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="202740" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Gdqwy47uK7Wdb0eQIDq2SH5LjfYjnBjF1LgjlgxDbp3juU7iUn8ARN4bJvC/w8Gj9OMP7NUDhvXYSXD2TbtWfg==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="202740">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/345688-assassin" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/345688/avatar" class="artist-profile-image artist" width="40" height="40" alt="Assassin live" title="Assassin live">

  <span class="artist-details">
    <span class="artist-name">Assassin</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="345688" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="BRnavOm7wrDoU5Q9qRUjJumCcKKDofaTRhjOLLtR1B7/eiSVNSrpQasn9V027FTNYyryuHU+aKNK6Z1M+qns/Q==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="345688">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/1055166-cheveu" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/1055166/avatar" class="artist-profile-image artist" width="40" height="40" alt="Cheveu live" title="Cheveu live">

  <span class="artist-details">
    <span class="artist-name">Cheveu</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="1055166" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="OP3uHX5YfKYQH4uzVbuLJXyjcd/kAIH3A/LS6Sdf31bCnhA0oslXV1Nr6tPKQvzO9gvzxRKfH8cPA4GJZqfntQ==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="1055166">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/133699-rubin-steiner" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/133699/avatar" class="artist-profile-image artist" width="40" height="40" alt="Rubin Steiner live" title="Rubin Steiner live">

  <span class="artist-details">
    <span class="artist-name">Rubin Steiner</span>
    <span>2 concerts</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="133699" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Qax/XLiJW7wbfv8IZIxE/e3nSqAozIiGYu2seOWUntO7z4F1ZBhwTVgKnmj7dTMWZ0/Iut5TFrZuHP8YpGymMA==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="133699">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/375620-casey" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/375620/avatar" class="artist-profile-image artist" width="40" height="40" alt="Casey live" title="Casey live">

  <span class="artist-details">
    <span class="artist-name">Casey</span>
    <span>2 concerts</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="375620" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Ym6TCRtKtRbGnAtK0nmOSxqKqlWpSzUXebWp2sbT38WYDW0gx9ue54XoaipNgPmgkCIoT1/Uqyd1RPq6hyvnJg==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="375620">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
      <li>
        <a class="artist-info" href="/artists/492042-peter-von-poehl" data-analytics-category="artist_info_with_upcoming_count" data-analytics-label="related_artists">
  <img src="//images.sk-static.com/images/media/profile_images/artists/492042/avatar" class="artist-profile-image artist" width="40" height="40" alt="Peter Von Poehl live" title="Peter Von Poehl live">

  <span class="artist-details">
    <span class="artist-name">Peter Von Poehl</span>
    <span>1 concert</span>
  </span>
</a>

        <div class="tracking">
  <form data-analytics-category="track_artist_button" data-analytics-action="track" data-analytics-label="492042" data-tracking-text="Track artist" data-stop-tracking-text="Stop tracking" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="W3W9mHIiN5uLRaE5QVPeoLjT4NLkpBe49lnDVoPBIDqhFkOxrrMcasgxwFneqqlLMntiyBI7iYj6qJA2wjkY2Q==" />
    <input type="hidden" name="relationship_type" value="concerts">
    <input type="hidden" name="subject_id" value="492042">
    <input type="hidden" name="subject_type" value="Artist">
    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="artist track" value="Track artist">Track artist</button>
</form></div>

      </li>
  </ul>
</div>


      </div>
    </div>
  </div>
  <div class="microformat">
    <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicGroup","name":"Elysian Fields","url":"http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic\u0026utm_source=microformat","image":"https://images.sk-static.com/images/media/profile_images/artists/236156/card_avatar","logo":"https://images.sk-static.com/images/media/profile_images/artists/236156/card_avatar","interactionCount":"5555 UserLikes"}]</script>
  </div>



    <div class="footer-container">
      <div id="footer" class="container footer">
  <div class="row">
    <div class="col-3">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/info/about" rel="nofollow">About us</a></li>
        <li><a href="/partner">Partner with us</a></li>
        <li><a href="/blog" rel="nofollow">Blog</a></li>
        <li><a href="/jobs" rel="nofollow">Jobs</a></li>
        <li><a href="http://support.songkick.com/">Help &amp; FAQ</a></li>
        <li><a href="/leaderboards/popular_artists">Most popular charts</a></li>
      </ul>
    </div>
    <div class="col-3">
      <ul>
        <li><a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=tourboxforartists">Tourbox for artists</a></li>
        <li><a href="/developer"><abbr>API</abbr> information</a></li>
        <li><a href="/info/guidelines" rel="nofollow">Community guidelines</a></li>
        <li><a href="/info/terms" rel="nofollow">Terms of use</a></li>
        <li><a href="/info/privacy" rel="nofollow">Privacy policy</a></li>
        <li><a href="/info/security" rel="nofollow">Security</a></li>
      </ul>
    </div>
    <div class="col-6">
      <div class="tourbox-cta">
        <p>Get your tour dates seen by one billion fans:</p>
        <a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=visitor" class="sign-up-as-an-artist" data-analytics-category="navigation" data-analytics-label="sign_up_tourbox">Sign up as an artist</a>
      </div>
      <div class="social-container">
        <ul class="social-icons">
          <li>
            <a href="https://twitter.com/songkick">
              <img src="//assets.sk-static.com/assets/nw/furniture/icons/twitter-161f1e4.png" width="22" height="18" alt="Twitter">
              &nbsp;<span>Follow us.</span>
            </a>
          </li>
          <li>
            <a href="http://www.facebook.com/songkick">
              <img src="//assets.sk-static.com/assets/nw/furniture/icons/facebook-08359b5.png" width="18" height="18" alt="Facebook">
              &nbsp;<span>Like us.</span>
            </a>
          </li>
          <li>
            <span>But we really hope you love us.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>

    </div>
    <script type="text/javascript" src="//assets.sk-static.com/assets/manifests-1f4433a.js"></script><script type="text/javascript" src="//assets.sk-static.com/assets/app-60e1f1b.js"></script>

    <script type="text/javascript">
      setTimeout(function(){var a=document.createElement("script");
      var b=document.getElementsByTagName("script")[0];
      a.src=document.location.protocol+"//dnn506yrbagrg.cloudfront.net/pages/scripts/0013/4464.js?"+Math.floor(new Date().getTime()/3600000);
      a.async=true;a.type="text/javascript";b.parentNode.insertBefore(a,b)}, 1);
    </script>

  <script type="text/javascript">
    Songkick.EventBus.bind('app:initialize', function() {
      JS.require('jQuery', function() {

        $.cookie('exp_showed_offtour_artist_modal', true, { path: '/'});

        $(document).on('click', 'a.ticket-vendor', function(e) {
          Songkick.EventBus.trigger('ui:click', { category: 'tmp_growth_team_ticket_vendor',
          action: 'logged_out_click',
          label: $(this).data('event-id').toString(),
          value: $(this).data('analytics-value')});
        });
      });
    });
      Songkick.EventBus.bind('app:initialize', function(config) {
        JS.require('jQuery.ui', function() {
          var modal = new Songkick.Component.Modal({
            analytics_category: 'signup_cta',
            analytics_label: '236156',
            analytics_action_prefix: 'artist:no_local:modal',
            cookie_key: 'off-tour-no-local-events-artist-cta',
            modal_class: 'off-tour-no-local-events-artist-cta-container',
            component: '<div class="top-area">  <button class="close-widget close">    <img src="/images/nw/components/vendor-click-signup-cta/close.svg" alt="Close" height="12" width="12">  </button>    <img width="60" height="60" class="artist artist-profile-image" src="//images.sk-static.com/images/media/profile_images/artists/236156/large_avatar" alt="Large avatar" />  <p class="artist-name">Elysian Fields</p>    <p class="upcoming-concerts-status">No concerts near you (Agen, France). </p></div><div class="bottom-area">  <h2 class="be-the-first-to-know">Be the first to know about tickets in the future</h2>  <div class="buttons">    <div class="tracking">  <form data-analytics-category="signup_cta" data-analytics-action="artist:no_local:modal:cta_button" data-analytics-label="236156" data-tracking-text="Yes, please notify me" data-stop-tracking-text="Yes, please notify me" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="NLcfiQwkTtHSLb/vns8y/vUXTGekKmpTNONX//6IfzzO1OGg0LVlIJFZ3o8BNkUVf7/OfVK19GM4EgSfv3BH3w==" />    <input type="hidden" name="relationship_type" value="concerts">    <input type="hidden" name="subject_id" value="236156">    <input type="hidden" name="subject_type" value="Artist">    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">    <input type="hidden" name="app_store_redirect_url" value="">    <button type="submit" class="artist signup-cta" value="Yes, please notify me">Yes, please notify me</button></form></div>  </div>  <p class="artist-trackings">5,555 fans get concert alerts for this artist.</p>  <a class="close-message">I don’t want to hear about tickets</a></div>'
          });
          modal.show(modal);
        });
      });
      Songkick.EventBus.bind('app:initialize', function(config) {
        JS.require('jQuery.ui', function() {
          var modal = new Songkick.Component.Modal({
            analytics_category: 'signup_cta',
            analytics_label: '236156',
            analytics_action_prefix: 'artist:post_tv_click',
            cookie_key: 'vendor-click-cta',
            modal_class: 'vendor-signup-cta-container',
            component: '<div class="top-area">  <button class="close-widget close">    <img src="/images/nw/components/vendor-click-signup-cta/close.svg" alt="Close" height="12" width="12">  </button>    <img alt="Elysian Fields live" width="70" height="70" class="artist artist-profile-image" src="//images.sk-static.com/images/media/profile_images/artists/236156/large_avatar" />  <h2>Still searching for Elysian Fields tickets?</h2>  <p class="be-the-first-to-know">Be the first to know about tickets in the future.</p>  <p class="artist-trackings">5,555 other fans want alerts for this artist.</p></div><div class="bottom-area">  <div class="buttons">    <div class="tracking">  <form data-analytics-category="signup_cta" data-analytics-action="artist:post_tv_click:cta_button" data-analytics-label="236156" data-tracking-text="Yes, please notify me" data-stop-tracking-text="Yes, please notify me" class="app-store-redirect auto-signup" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="JFufWp6unu56RbHkt2Gf2wpGKKqeta/CW+M3NeXnAD3eOGFzQj+1Hzkx0IQomOgwgO6qsGgqMfJXEmRVpB843g==" />    <input type="hidden" name="relationship_type" value="concerts">    <input type="hidden" name="subject_id" value="236156">    <input type="hidden" name="subject_type" value="Artist">    <input type="hidden" name="success_url" value="/artists/236156-elysian-fields">    <input type="hidden" name="app_store_redirect_url" value="">    <button type="submit" class="artist signup-cta" value="Yes, please notify me">Yes, please notify me</button></form></div>    <a href="https://itunes.apple.com/us/app/apple-store/id438690886?ct=skweb%3Aartist%3Apost_tv_click%3Aapp_store_bt&amp;mt=8&amp;pt=307660" class="app-store-button" data-analytics-category="signup_cta" data-analytics-action="artist:post_tv_click:app_store_bt" data-analytics-label="236156">      <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/app-store-icon-e56abf8.svg" alt="Available on the App Store" class="store-button">    </a>    <a href="https://play.google.com/store/apps/details?id=com.songkick&amp;referrer=utm_campaign%3Dartist%253Apost_tv_click%253Aapp_store_bt%26utm_medium%3D%26utm_source%3Dskweb" class="google-play-button" data-analytics-category="signup_cta" data-analytics-action="artist:post_tv_click:app_store_bt" data-analytics-label="236156">      <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/play-store-icon-79aae3f.svg" alt="Available on the Play Store" class="store-button">    </a>  </div>  <a class="close-message">I don’t want to hear about tickets</a></div>'
          });
          $('body').on('click', 'a.ticket-vendor.third-party',
            function(e) { modal.show(modal);});
        });
      });
  </script>


<script type="text/javascript">
  Songkick.EventBus.bind('app:initialize', function() {
    Songkick.EventBus.trigger('ui:view', {"category":"artist_page","action":"view_on_tour","label":"no_local_events"});
  });
</script>

<script type="text/javascript">
  /* <![CDATA[ */
  var google_conversion_id = 964669843;
  var google_custom_params = window.google_tag_params;
  var google_remarketing_only = true;
  /* ]]> */
</script>
<script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js">
</script>
<noscript>
  <div style="display:inline;">
  <img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/964669843/?value=0&amp;guid=ON&amp;script=0"/>
  </div>
</noscript>

<script type="text/javascript">
  JS.require("twttr", function() {
    twttr.conversion.trackPid('l6neh', { tw_sale_amount: 0, tw_order_quantity: 0 });
  });
</script>
<noscript>
  <img height="1" width="1" style="display:none;" alt="" src="https://analytics.twitter.com/i/adsct?txn_id=l6neh&amp;p_id=Twitter&amp;tw_sale_amount=0&amp;tw_order_quantity=0" />
  <img height="1" width="1" style="display:none;" alt="" src="//t.co/i/adsct?txn_id=l6neh&amp;p_id=Twitter&amp;tw_sale_amount=0&amp;tw_order_quantity=0" />
</noscript>

<script type="text/javascript">
  SK.logged_in_user = {
    id:null,
    analyticsUserType: 'visitor'
  };

  JS.require("FB", 'jQuery', function() {
    Songkick.Facebook.init(
      "308540029359",
      ["email", "public_profile", "user_friends", "user_likes", "user_actions.music"],
      ["email", "public_profile", "user_friends", "user_likes", "user_actions.music", "publish_actions"],
      {events: Songkick.EventBus}
    );
  });
  var features = {};
  Songkick.EventBus.trigger('app:initialize', {
    events: Songkick.EventBus,
    features: features,
    promoteNativeApp: false,
    mobileSignupRedirectUrl: '',
    mobileAnalyticsEnabled: false,
  });
</script>

    
    <script>
  (function(f,b){
    var c;
    f.hj=f.hj||function(){(f.hj.q=f.hj.q||[]).push(arguments)};
    f._hjSettings={hjid:38507, hjsv:4};
    c=b.createElement("script");c.async=1;
    c.src="//static.hotjar.com/c/hotjar-"+f._hjSettings.hjid+".js?sv="+f._hjSettings.hjsv;
    b.getElementsByTagName("head")[0].appendChild(c); 
  })(window,document);
</script>


  </body>
</html>

```

### `tests/samples/songkick/elysianfields.json`

```json
{
    "microdata": [],
    "json-ld": [
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/concerts/30173984-elysian-fields-at-owl-music-parlor?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Brooklyn",
                    "addressCountry": "US",
                    "addressRegion": "NY",
                    "streetAddress": "497 Rogers Ave",
                    "postalCode": "11225"
                },
                "name": "The Owl Music Parlor",
                "sameAs": "http://www.theowl.nyc",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 40.660109,
                    "longitude": -73.953193
                }
            },
            "startDate": "2017-06-10T19:30:00-0400",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Elysian Fields",
                    "sameAs": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
                }
            ]
        },
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/concerts/29673614-elysian-fields-at-hotel-utah-saloon?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "San Francisco",
                    "addressCountry": "US",
                    "addressRegion": "CA",
                    "streetAddress": "500 Fourth Street",
                    "postalCode": "94107"
                },
                "name": "Hotel Utah Saloon",
                "sameAs": "http://www.hotelutah.com/",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 37.7795638,
                    "longitude": -122.398023
                }
            },
            "startDate": "2017-04-26T20:00:00-0700",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Elysian Fields",
                    "sameAs": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Chocolate Genius Inc.",
                    "sameAs": "http://www.songkick.com/artists/1009602-chocolate-genius-inc?utm_medium=organic&utm_source=microformat"
                }
            ]
        },
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/concerts/27626524-elysian-fields-at-le-vip?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Saint-Nazaire",
                    "addressCountry": "France",
                    "streetAddress": "Boulevard de la L\u00e9gion d'Honneur - Base Sous Marine - Alv\u00e9ole 14",
                    "postalCode": "44600"
                },
                "name": "Le VIP",
                "sameAs": "http://www.vip.les-escales.com",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 47.2734979,
                    "longitude": -2.213848
                }
            },
            "startDate": "2016-10-29T21:00:00+0200",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Elysian Fields",
                    "sameAs": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Troy Von Balthazar",
                    "sameAs": "http://www.songkick.com/artists/355304-troy-von-balthazar?utm_medium=organic&utm_source=microformat"
                }
            ]
        },
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/concerts/26734634-elysian-fields-at-le-rocher-de-palmer?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Cenon",
                    "addressCountry": "France",
                    "streetAddress": "1 rue Aristide Briand",
                    "postalCode": "33152"
                },
                "name": "Le Rocher De Palmer",
                "sameAs": "http://lerocherdepalmer.fr/",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 44.8624327,
                    "longitude": -0.5237826
                }
            },
            "startDate": "2016-10-27T20:30:00+0200",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Elysian Fields",
                    "sameAs": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Ernst Reijseger",
                    "sameAs": "http://www.songkick.com/artists/13128-ernst-reijseger?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Troy Von Balthazar",
                    "sameAs": "http://www.songkick.com/artists/355304-troy-von-balthazar?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Rachid Taha",
                    "sameAs": "http://www.songkick.com/artists/100389-rachid-taha?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Vaudou Game",
                    "sameAs": "http://www.songkick.com/artists/8195583-vaudou-game?utm_medium=organic&utm_source=microformat"
                }
            ]
        },
        {
            "@context": "http://schema.org",
            "@type": "MusicGroup",
            "name": "Elysian Fields",
            "url": "http://www.songkick.com/artists/236156-elysian-fields?utm_medium=organic&utm_source=microformat",
            "image": "https://images.sk-static.com/images/media/profile_images/artists/236156/card_avatar",
            "logo": "https://images.sk-static.com/images/media/profile_images/artists/236156/card_avatar",
            "interactionCount": "5555 UserLikes"
        }
    ],
    "opengraph": [
        {
            "namespace": {
                "og": "http://ogp.me/ns#",
                "fb": "http://www.facebook.com/2008/fbml",
                "concerts": "http://ogp.me/ns/fb/songkick-concerts#"
            },
            "properties": [
                [
                    "fb:app_id",
                    "308540029359"
                ],
                [
                    "og:site_name",
                    "Songkick"
                ],
                [
                    "og:type",
                    "songkick-concerts:artist"
                ],
                [
                    "og:title",
                    "Elysian Fields"
                ],
                [
                    "og:description",
                    "Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017."
                ],
                [
                    "og:url",
                    "http://www.songkick.com/artists/236156-elysian-fields"
                ],
                [
                    "og:image",
                    "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg"
                ],
                [
                    "og:image",
                    "http://images.sk-static.com/SECONDARY_IMAGE.jpg"
                ]
            ]
        }
    ],
    "microformat": [],
    "rdfa": [
        {
            "@id": "http://www.songkick.com/artists/236156-elysian-fields",
            "al:ios:app_name": [
                {
                    "@value": "Songkick Concerts"
                }
            ],
            "al:ios:app_store_id": [
                {
                    "@value": "438690886"
                }
            ],
            "al:ios:url": [
                {
                    "@value": "songkick://artists/236156-elysian-fields"
                }
            ],
            "http://ogp.me/ns#description": [
                {
                    "@value": "Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017."
                }
            ],
            "http://ogp.me/ns#image": [
                {
                    "@value": "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg"
                },
                {
                    "@value": "http://images.sk-static.com/SECONDARY_IMAGE.jpg"
                }
            ],
            "http://ogp.me/ns#site_name": [
                {
                    "@value": "Songkick"
                }
            ],
            "http://ogp.me/ns#title": [
                {
                    "@value": "Elysian Fields"
                }
            ],
            "http://ogp.me/ns#type": [
                {
                    "@value": "songkick-concerts:artist"
                }
            ],
            "http://ogp.me/ns#url": [
                {
                    "@value": "http://www.songkick.com/artists/236156-elysian-fields"
                }
            ],
            "http://www.facebook.com/2008/fbmlapp_id": [
                {
                    "@value": "308540029359"
                }
            ]
        }
    ],
    "dublincore": [
        {
            "namespaces": {
            },
            "elements": [
                {
                    "name": "description",
                    "content": "Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017.",
                    "URI": "http://purl.org/dc/elements/1.1/description"
                }
            ],
            "terms": [
            ]
        }
    ]
}

```

### `tests/samples/songkick/jsonld_empty_item_test.jsonld`

```jsonld
[
  {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "url": "https://www.tasteofhome.com/recipes/chicken-goat-cheese-skillet/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "url": "https://www.tasteofhome.com/recipes/cheesy-cauliflower-breadsticks/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "url": "https://www.tasteofhome.com/recipes/herbed-balsamic-chicken/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "url": "https://www.tasteofhome.com/recipes/garlic-dill-deviled-eggs/"
      },
      {
        "@type": "ListItem",
        "position": 5,
        "url": "https://www.tasteofhome.com/recipes/zucchini-crusted-pizza/"
      },
      {
        "@type": "ListItem",
        "position": 6,
        "url": "https://www.tasteofhome.com/recipes/creamy-dijon-chicken/"
      },
      {
        "@type": "ListItem",
        "position": 7,
        "url": "https://www.tasteofhome.com/recipes/naked-fish-tacos/"
      },
      {
        "@type": "ListItem",
        "position": 8,
        "url": "https://www.tasteofhome.com/recipes/denver-omelet-salad/"
      },
      {
        "@type": "ListItem",
        "position": 9,
        "url": "https://www.tasteofhome.com/recipes/balsamic-zucchini-saute/"
      },
      {
        "@type": "ListItem",
        "position": 10,
        "url": "https://www.tasteofhome.com/recipes/blackened-tilapia-with-zucchini-noodles/"
      },
      {
        "@type": "ListItem",
        "position": 11,
        "url": "https://www.tasteofhome.com/recipes/deviled-egg-spread/"
      },
      {
        "@type": "ListItem",
        "position": 12,
        "url": "https://www.tasteofhome.com/recipes/asparagus-mushroom-frittata/"
      },
      {
        "@type": "ListItem",
        "position": 13,
        "url": "https://www.tasteofhome.com/recipes/blue-cheese-pork-medallions/"
      },
      {
        "@type": "ListItem",
        "position": 14,
        "url": "https://www.tasteofhome.com/recipes/asparagus-cheese-frittata/"
      },
      {
        "@type": "ListItem",
        "position": 15,
        "url": "https://www.tasteofhome.com/recipes/oktoberfest-brats-with-mustard-sauce/"
      },
      {
        "@type": "ListItem",
        "position": 16,
        "url": "https://www.tasteofhome.com/recipes/shrimp-avocado-salad/"
      },
      {
        "@type": "ListItem",
        "position": 17,
        "url": "https://www.tasteofhome.com/recipes/sage-rubbed-salmon/"
      },
      {
        "@type": "ListItem",
        "position": 18,
        "url": "https://www.tasteofhome.com/recipes/cilantro-lime-shrimp/"
      },
      {
        "@type": "ListItem",
        "position": 19,
        "url": "https://www.tasteofhome.com/recipes/parmesan-roasted-broccoli/"
      },
      {
        "@type": "ListItem",
        "position": 20,
        "url": "https://www.tasteofhome.com/recipes/smoky-cauliflower-bites/"
      },
      {
        "@type": "ListItem",
        "position": 21,
        "url": "https://www.tasteofhome.com/recipes/avocado-crab-boats/"
      },
      {
        "@type": "ListItem",
        "position": 22,
        "url": "https://www.tasteofhome.com/recipes/parmesan-chicken/"
      },
      {
        "@type": "ListItem",
        "position": 23,
        "url": "https://www.tasteofhome.com/recipes/roasted-parmesan-carrots/"
      },
      {
        "@type": "ListItem",
        "position": 24,
        "url": "https://www.tasteofhome.com/recipes/coconut-curry-cauliflower-soup/"
      },
      {
        "@type": "ListItem",
        "position": 25,
        "url": "https://www.tasteofhome.com/recipes/brussels-sprouts-with-garlic-goat-cheese/"
      },
      {
        "@type": "ListItem",
        "position": 26,
        "url": "https://www.tasteofhome.com/recipes/juicy-delicious-mixed-spice-burgers/"
      },
      {
        "@type": "ListItem",
        "position": 27,
        "url": "https://www.tasteofhome.com/recipes/parmesan-asparagus/"
      },
      {
        "@type": "ListItem",
        "position": 28,
        "url": "https://www.tasteofhome.com/recipes/roasted-herb-lemon-cauliflower/"
      },
      {
        "@type": "ListItem",
        "position": 29,
        "url": "https://www.tasteofhome.com/recipes/shakshuka/"
      },
      {
        "@type": "ListItem",
        "position": 30,
        "url": "https://www.tasteofhome.com/recipes/mexican-cabbage-roll-soup/"
      },
      {
        "@type": "ListItem",
        "position": 31,
        "url": "https://www.tasteofhome.com/recipes/radish-carrot-cilantro-salad/"
      },
      {
        "@type": "ListItem",
        "position": 32,
        "url": "https://www.tasteofhome.com/recipes/vidalia-onion-swiss-dip/"
      },
      {
        "@type": "ListItem",
        "position": 33,
        "url": "https://www.tasteofhome.com/recipes/citrus-salmon-en-papillote/"
      },
      {
        "@type": "ListItem",
        "position": 34,
        "url": "https://www.tasteofhome.com/recipes/hot-chipotle-spinach-and-artichoke-dip-with-lime/"
      },
      {
        "@type": "ListItem",
        "position": 35,
        "url": "https://www.tasteofhome.com/recipes/grilled-ribeyes-with-greek-relish/"
      },
      {
        "@type": "ListItem",
        "position": 36,
        "url": "https://www.tasteofhome.com/recipes/asparagus-squash-red-pepper-saute/"
      },
      {
        "@type": "ListItem",
        "position": 37,
        "url": "https://www.tasteofhome.com/recipes/pressure-cooker-beef-brisket-in-beer/"
      },
      {
        "@type": "ListItem",
        "position": 38,
        "url": "https://www.tasteofhome.com/recipes/sausage-cobb-salad-lettuce-wraps/"
      },
      {
        "@type": "ListItem",
        "position": 39,
        "url": "https://www.tasteofhome.com/recipes/garlic-asiago-cauliflower-rice/"
      },
      {
        "@type": "ListItem",
        "position": 40,
        "url": "https://www.tasteofhome.com/recipes/cod-and-asparagus-bake/"
      },
      {
        "@type": "ListItem",
        "position": 41,
        "url": "https://www.tasteofhome.com/recipes/sauteed-squash-with-tomatoes-onions/"
      },
      {
        "@type": "ListItem",
        "position": 42,
        "url": "https://www.tasteofhome.com/recipes/roasted-cauliflower-with-tahini-yogurt-sauce/"
      },
      {
        "@type": "ListItem",
        "position": 43,
        "url": "https://www.tasteofhome.com/recipes/cajun-sirloin-with-mushroom-leek-sauce/"
      },
      {
        "@type": "ListItem",
        "position": 44,
        "url": "https://www.tasteofhome.com/recipes/chicken-and-broccoli-with-dill-sauce/"
      },
      {
        "@type": "ListItem",
        "position": 45,
        "url": "https://www.tasteofhome.com/recipes/pancetta-and-mushroom-stuffed-chicken-breast/"
      },
      {
        "@type": "ListItem",
        "position": 46,
        "url": "https://www.tasteofhome.com/recipes/leeks-au-gratin/"
      },
      {
        "@type": "ListItem",
        "position": 47,
        "url": "https://www.tasteofhome.com/recipes/moroccan-cauliflower-and-almond-soup/"
      },
      {
        "@type": "ListItem",
        "position": 48,
        "url": "https://www.tasteofhome.com/recipes/chicken-nicoise-salad/"
      },
      {
        "@type": "ListItem",
        "position": 49,
        "url": "https://www.tasteofhome.com/recipes/shrimp-scampi-spinach-salad/"
      },
      {
        "@type": "ListItem",
        "position": 50,
        "url": "https://www.tasteofhome.com/recipes/spicy-thai-coconut-chicken-soup/"
      },
      {
        "@type": "ListItem",
        "position": 51,
        "url": "https://www.tasteofhome.com/recipes/better-brussels-sprouts/"
      },
      {
        "@type": "ListItem",
        "position": 52,
        "url": "https://www.tasteofhome.com/recipes/shiitake-and-manchego-scramble/"
      },
      {
        "@type": "ListItem",
        "position": 53,
        "url": "https://www.tasteofhome.com/recipes/slow-cooker-marinated-mushrooms/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "53 Keto Diet Recipes",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://www.tasteofhome.com/collection/keto-diet-recipes/view-all/"
    },
    "description": "These keto recipes will satisfy your low carb diet needs (some are more strict than others!).",
    "datePublished": "2018-09-11",
    "dateModified": "2018-10-05",
    "author": [
      {
        "@type": "Person",
        "name": "Rashanda Cobbins"
      }
    ],
    "image": {
      "@type": "ImageObject",
      "url": "https://www.tasteofhome.com/wp-content/uploads/2017/09/Chicken-Goat-Cheese-Skillet_EXPS_SDAM17_136810_B12_08_4b.jpg",
      "height": 1200,
      "width": 1200
    },
    "publisher": {
      "@type": "Organization",
      "name": "Taste of Home",
      "logo": {
        "@type": "ImageObject",
        "url": "https://cdn1.tmbi.com/TOH/Images/toh-logo-red.gif",
        "width": 335,
        "height": 60
      }
    }
  }
]
```

### `tests/samples/songkick/tovestyrke.html`

```html
<!DOCTYPE html>
<html lang="en" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml">
  <head prefix="og: http://ogp.me/ns# fb: http://www.facebook.com/2008/fbml songkick-concerts: http://ogp.me/ns/fb/songkick-concerts#">
    <link rel="stylesheet" type="text/css" href="//assets.sk-static.com/assets/concert-0be23fe.css">
    <script type="text/javascript">
  SK = typeof(SK) == 'undefined' ? {} : SK;
  SK_ASSET_HOST = "//assets.sk-static.com";
  SK_DYNAMIC_ASSET_HOST = "https://images.sk-static.com";
  CX_EXPERIMENT_ID = "";
  CX_VARIATION_ID = -2;
</script>

    <title>Tove Styrke London, Hoxton Square Bar &amp; Kitchen, 12 Jun 2017 – Songkick</title>
    <link href="//images.sk-static.com/images/media/profile_images/artists/3407026/col3" rel="image_src">
    <link rel="shortcut icon" type="image/x-icon" href="//assets.sk-static.com/images/favicon.ico" />
    <link href="//assets.sk-static.com/images/apple-touch-icon.png" rel="apple-touch-icon">
    <link href="//assets.sk-static.com/images/apple-touch-icon.png" rel="apple-touch-icon-precomposed">
    <meta name="robots" content="noindex, nofollow">
    <link href="https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen" rel="canonical">
        <meta property="al:ios:url" content="songkick://events/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen">
    <meta property="al:ios:app_store_id" content="438690886">
    <meta property="al:ios:app_name" content="Songkick Concerts">
    <link rel="alternate" href="android-app://com.songkick/http/www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen">
    <meta name="description" content="Past concert. Tove Styrke concert with Geowulf at Hoxton Square Bar &amp; Kitchen in London on 12 Jun 2017.">
    <meta property="fb:app_id" content="308540029359">
    <meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0, width=device-width">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta property="og:site_name" content="Songkick">
    <meta property="og:type" content="songkick-concerts:concert">
    <meta property="og:title" content="Tove Styrke at Hoxton Square Bar &amp; Kitchen (12 Jun 2017)">
    <meta property="og:description" content="Past concert. Tove Styrke concert at Hoxton Square Bar &amp; Kitchen in London on 12 Jun 2017.">
    <meta property="og:url" content="https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen">
    <meta property="og:image" content="http://images.sk-static.com/images/media/img/col6/20170515-103345-171924.jpg">
    <meta property="og:locality" content="London">
    <meta property="og:country-name" content="UK">
    <meta property="og:street-address" content="2-4 Hoxton Square">
    <meta property="og:postal-code" content="N1 6NU">
    <meta property="og:latitude" content="51.527476">
    <meta property="og:longitude" content="-0.081657">
  </head>
  <body>

      <a href="/jobs?utm_source=skweb_job_ad">
  <div class="songkick-job-ad">
    Psst, we’re hiring! Check out our <b>jobs page</b>.
  </div>
</a>


    
    <script>
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
  document,'script','//connect.facebook.net/en_US/fbevents.js');
  fbq('init', '583609881778767');
  fbq('track', 'PageView');
</script>
<noscript>
  <img height="1" width="1" alt="" style="display:none" src="https://www.facebook.com/tr?id=583609881778767&amp;ev=PageView&amp;noscript=1" />
</noscript>

    <div id="fb-root"></div>

    
    
    <div class="track-alert js-track-alert ">
  <div class="track-alert-inner">
    This event has been added to your <a data-analytics-category="navigation_your_plans" data-analytics-label="feedback_your_plans" href="/calendar?filter=attendance">Plans</a>.
    <a class="track-alert-dismiss js-track-alert-dismiss">Close</a>
  </div>
</div>


    <div class="navigation">
        <div class="navigation-large-screen">
  <ul class="nav-bar">
    <li class="sub-nav">
      <ul>
        <li class="logo"><a href="/" data-analytics-category="navigation" data-analytics-label="logo"><img src="//assets.sk-static.com/assets/nw/furniture/songkick-logo-ac43b7a.svg" height="26" width="90" alt="songkick"></a>
        </li><li class="nav-item metro-area menu hover-for-touch">
          <a href="/metro_areas/24426-uk-london" data-analytics-category="navigation" data-analytics-label="metro_area" title="London concerts">London concerts</a>
          <div class="menu-content">
            <a href="/metro_areas/24426-uk-london" data-analytics-category="navigation" data-analytics-label="popular_tickets"><span>Popular tickets in London</span></a>
            <a class="repeat" href="/metro_areas/24426-uk-london" data-analytics-category="navigation" data-analytics-label="metro_area">London concerts</a>
              <ul class="listing">
                <li class="event">
                  <a href="/concerts/33118744-beach-house-at-troxy" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/273059/avatar" width="35" height="35" class="artist-profile-image artist" alt="Beach House live">
                  <span class="col"><span class="name">Beach House</span><br>
                    <span class="venue">Troxy</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/33217894-migos-at-o2-academy-brixton" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/7222459/avatar" width="35" height="35" class="artist-profile-image artist" alt="Migos live">
                  <span class="col"><span class="name">Migos</span><br>
                    <span class="venue">O2 Academy Brixton</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/33152939-tallest-man-on-earth-at-union-chapel" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/319682/avatar" width="35" height="35" class="artist-profile-image artist" alt="The Tallest Man On Earth live">
                  <span class="col"><span class="name">The Tallest Man On Earth</span><br>
                    <span class="venue">Union Chapel</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/33045794-decemberists-at-eventim-apollo" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/355198/avatar" width="35" height="35" class="artist-profile-image artist" alt="The Decemberists live">
                  <span class="col"><span class="name">The Decemberists</span><br>
                    <span class="venue">Eventim Apollo</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/33040414-fatboy-slim-at-queen-elizabeth-olympic-park" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/371111/avatar" width="35" height="35" class="artist-profile-image artist" alt="Fatboy Slim live">
                  <span class="col"><span class="name">Fatboy Slim</span><br>
                    <span class="venue">Queen Elizabeth Olympic Park</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/33080469-dangelo-at-o2-academy-brixton" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/210179/avatar" width="35" height="35" class="artist-profile-image artist" alt="D&#39;Angelo live">
                  <span class="col"><span class="name">D&#39;Angelo</span><br>
                    <span class="venue">O2 Academy Brixton</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/33116489-editors-at-o2-academy-brixton" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/306990/avatar" width="35" height="35" class="artist-profile-image artist" alt="Editors live">
                  <span class="col"><span class="name">Editors</span><br>
                    <span class="venue">O2 Academy Brixton</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/33235899-van-morrison-at-subterania" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/156780/avatar" width="35" height="35" class="artist-profile-image artist" alt="Van Morrison live">
                  <span class="col"><span class="name">Van Morrison</span><br>
                    <span class="venue">Subterania</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/32975209-5-seconds-of-summer-at-heaven" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/5642214/avatar" width="35" height="35" class="artist-profile-image artist" alt="5 Seconds of Summer live">
                  <span class="col"><span class="name">5 Seconds of Summer</span><br>
                    <span class="venue">Heaven</span>
                </span></a></li>
                <li class="event">
                  <a href="/concerts/33101819-joey-defrancesco-at-subterania" class="col" data-analytics-category="navigation" data-analytics-label="metro_area_popular_ticket">
                  <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/58719/avatar" width="35" height="35" class="artist-profile-image artist" alt="Joey DeFrancesco live">
                  <span class="col"><span class="name">Joey DeFrancesco</span><br>
                    <span class="venue">Subterania</span>
                </span></a></li>
              </ul>
              <a href="/metro_areas/24426-uk-london" data-analytics-category="navigation" data-analytics-label="metro_area_see_all">See all London concerts</a> <a class="change-location" data-analytics-category="navigation-megadropdown" data-analytics-label="change_location" href="/session/filter_metro_area">(Change&nbsp;location)</a><br><br>
              <a data-analytics-category="navigation" data-analytics-label="metro_area_today" href="/metro_areas/24426-uk-london?filters%5BmaxDate%5D=03%2F19%2F2018&amp;filters%5BminDate%5D=03%2F19%2F2018#date-filter-form">Today ·</a> <a data-analytics-category="navigation" data-analytics-label="metro_area_7days" href="/metro_areas/24426-uk-london?filters%5BmaxDate%5D=03%2F26%2F2018&amp;filters%5BminDate%5D=03%2F19%2F2018#date-filter-form">Next 7 days ·</a> <a data-analytics-category="navigation" data-analytics-label="metro_area_month" href="/metro_areas/24426-uk-london?filters%5BmaxDate%5D=04%2F19%2F2018&amp;filters%5BminDate%5D=03%2F19%2F2018#date-filter-form">Next 30 days</a>
          </div>
        </li>
        <li class="nav-item artists menu hover-for-touch">
            <a href="/metro_areas/24426-uk-london#popular-artists-in-metro-area" data-analytics-category="navigation" data-analytics-label="artists">Artists</a>
          <div class="menu-content">
                <ul class="artists-navigation">
  <li class="col"><a href="/metro_areas/24426-uk-london#popular-artists-in-metro-area" data-analytics-category="navigation" data-analytics-label="popular_artists_metro_area">Popular artists in London</a></li>
    <li class="col"><a href="/leaderboards/trending_artists" data-analytics-category="navigation" data-analytics-label="trending_artists">Trending artists worldwide</a></li>
  </ul>
  <div class="listing">
      <ul class="col popular-artists">
          <li>
            <a href="/artists/8596524-j-hus" data-analytics-category="navigation" data-analytics-label="artists_popular_artist_metro_area">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/8596524/avatar" width="35" height="35" class="artist-profile-image artist" alt="J Hus live.">
              <span class="name">J Hus</span>
            </a>
          </li>
          <li>
            <a href="/artists/592367-donaeo" data-analytics-category="navigation" data-analytics-label="artists_popular_artist_metro_area">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/592367/avatar" width="35" height="35" class="artist-profile-image artist" alt="Donae&#39;o live.">
              <span class="name">Donae&#39;o</span>
            </a>
          </li>
          <li>
            <a href="/artists/185297-chip" data-analytics-category="navigation" data-analytics-label="artists_popular_artist_metro_area">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/185297/avatar" width="35" height="35" class="artist-profile-image artist" alt="CHIP live.">
              <span class="name">CHIP</span>
            </a>
          </li>
          <li>
            <a href="/artists/19637-lethal-bizzle" data-analytics-category="navigation" data-analytics-label="artists_popular_artist_metro_area">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/19637/avatar" width="35" height="35" class="artist-profile-image artist" alt="Lethal Bizzle live.">
              <span class="name">Lethal Bizzle</span>
            </a>
          </li>
          <li>
            <a href="/artists/426367-jme" data-analytics-category="navigation" data-analytics-label="artists_popular_artist_metro_area">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/426367/avatar" width="35" height="35" class="artist-profile-image artist" alt="JME live.">
              <span class="name">JME</span>
            </a>
          </li>
      </ul>
      <ul class="col popular-artists">
          <li>
            <a href="/artists/225939-supreme-ntm" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/225939/avatar" width="35" height="35" class="artist-profile-image artist" alt="Suprême NTM live.">
              <span class="name">Suprême NTM</span>
            </a>
          </li>
          <li>
            <a href="/artists/9406319-blocboy-jb" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/9406319/avatar" width="35" height="35" class="artist-profile-image artist" alt="Blocboy JB live.">
              <span class="name">Blocboy JB</span>
            </a>
          </li>
          <li>
            <a href="/artists/9258534-bazzi" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/9258534/avatar" width="35" height="35" class="artist-profile-image artist" alt="Bazzi live.">
              <span class="name">Bazzi</span>
            </a>
          </li>
          <li>
            <a href="/artists/9144289-sob-x-rbe" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/9144289/avatar" width="35" height="35" class="artist-profile-image artist" alt="SOB x RBE live.">
              <span class="name">SOB x RBE</span>
            </a>
          </li>
          <li>
            <a href="/artists/9235649-lil-skies" data-analytics-category="navigation" data-analytics-label="artists_trending_artist">
              <img src="//assets.sk-static.com/assets/default_images/thumb/default-artist-ba18a04.png" data-src="//images.sk-static.com/images/media/profile_images/artists/9235649/avatar" width="35" height="35" class="artist-profile-image artist" alt="lil skies live.">
              <span class="name">lil skies</span>
            </a>
          </li>
      </ul>
  </div>

            <div class="tourbox-cta">
              Get your tour dates seen by one billion fans: <a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=visitor" class="sign-up-as-an-artist" data-analytics-category="navigation" data-analytics-label="sign_up_tourbox">Sign up as an artist</a>
            </div>
          </div>
        </li>
        <li class="nav-item about-us">
          <a data-analytics-category="navigation" data-analytics-label="about_us" href="/info/about?utm_source=songkick.com&amp;utm_medium=referral&amp;utm_campaign=aboutpagetopnav">About&nbsp;us</a>
        </li>
        <li class="location">
          <a data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">Change&nbsp;location</a>
        </li>
      </ul>
    <li class="sub-nav">
      <ul>
        <li class="search">
          <form name="search" class="navigation-search-form" data-analytics-category="navigation" data-analytics-label="search" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="hidden" name="type" value="initial">
  <input name="query" type="search" value="" class="text navigation-search" placeholder="Find concerts for any artist or city"><button class="search-button" name="commit" type="submit"><img src="//assets.sk-static.com/assets/nw/components/navigation-large-screen/search-5510d8d.svg" height="15" width="14" alt="search" class="navigation-submit"></button>
</form>
        </li>
        <li class="login-signup">
          <a href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F30166884-tove-styrke-at-hoxton-square-bar-and-kitchen&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" class="signup-link" data-signup-source="Everything else" data-analytics-category="navigation" data-analytics-label="sign_up">Sign up</a> <a href="https://accounts.songkick.com/session/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F30166884-tove-styrke-at-hoxton-square-bar-and-kitchen&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" rel="nofollow" class="login-link" data-analytics-category="navigation" data-analytics-label="log_in">Log in</a>
        </li>
      </ul>
    </li>
  </ul>
</div>

        <div class="local-navigation">
  <a href="/" id="logo" data-analytics-category="navigation_small_screen" data-analytics-label="logo"><img src="//assets.sk-static.com/assets/nw/components/navigation/header-logo-ff8507a.png" alt="Songkick" width="124" height="32"></a>
  <ul>
    <li class="nav-icon main-menu"><a href="#home"><img src="//assets.sk-static.com/assets/nw/components/navigation/local-navigation/navigation-icon-2eeeafe.png" width="22" height="15" alt="Show navigation"></a></li>
    <li class="nav-icon search-nav"><label><a href="#search"><img src="//assets.sk-static.com/assets/nw/components/navigation/local-navigation/search-5cac59e.png" height="20" width="20" alt="search"></a></label></li>
    <li class="site-search" id="search">
      <form name="search" class="navigation-search-form" data-analytics-category="navigation" data-analytics-label="search" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="hidden" name="type" value="initial">
  <input name="query" type="search" value="" class="text navigation-search" placeholder="Find concerts for any artist or city"><button class="search-button" name="commit" type="submit"><img src="//assets.sk-static.com/assets/nw/components/navigation-large-screen/search-5510d8d.svg" height="15" width="14" alt="search" class="navigation-submit"></button>
</form>
    </li>
    <li class="home nav" id="home">
      <a data-analytics-category="navigation" data-analytics-label="home" href="/">Home</a>
    </li><li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="metro_area" href="/metro_areas/24426-uk-london">London concerts</a>
    </li><li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="change_location" href="/session/filter_metro_area">Change&nbsp;location</a>
    </li><li>
      <a href="/leaderboards/popular_artists" data-analytics-catigory="navigation" data-analytics-label="popular_artists">Popular artists</a>
    </li>
    <li class="nav">
      <a data-analytics-category="navigation" data-analytics-label="about_us" href="/info/about?utm_source=songkick.com&amp;utm_medium=referral&amp;utm_campaign=aboutpagetopnav">About&nbsp;us</a>
    </li>
    <li class="login">
      <a href="https://accounts.songkick.com/session/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F30166884-tove-styrke-at-hoxton-square-bar-and-kitchen&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew" data-analytics_category="navigation" data-analytics_label="log_in">
        <img src="//assets.sk-static.com/assets/nw/components/navigation/user-cff5cca.svg" height="14" alt="Log in"> Log in to your account
      </a>
    </li>
    <li class="signup">
      <a data-analytics-category="navigation" data-analytics-label="sign_up" href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;login_success_url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F30166884-tove-styrke-at-hoxton-square-bar-and-kitchen&amp;signup_success_url=https%3A%2F%2Fwww.songkick.com%2Ftaste_imports%2Fnew">Sign&nbsp;up</a>
    </li>
  </ul>
</div>

    </div>

      <div class="component see-all-events-for-headliner">
  <p><a href="/artists/3407026-tove-styrke" data-analytics-category="navigation" data-analytics-label="event_strip_see_all"><img src="//assets.sk-static.com/images/nw/components/see-all-events-for-headliner/left-arrow.svg" alt="20" height="20" width="20">See all <span class="artist-name">Tove Styrke</span> concerts</a></p>
</div>


<div class="event-header">
  
  
  <div class="row component brief past">

    <div class="col-8">
      <div class="date-and-name">
        <strong class="item-state-tag past-concert">Past concert</strong>

        <p>Monday 12 June 2017</p>
      </div>

      <h1 class="h0 summary">
        <span><a data-analytics-category="event_brief" data-analytics-label="headliners" href="/artists/3407026-tove-styrke">Tove Styrke</a></span>
      </h1>

      <div class="location">
        <span class="name"><a data-analytics-category="event_brief" data-analytics-label="venue_name" href="/venues/8280-hoxton-square-bar-and-kitchen">Hoxton Square Bar &amp; Kitchen</a>,</span>
          <span>London, UK</span>

      </div>

        <div class="line-up">
          Line-up:
            <span class="headliner">
              <a data-analytics-category="event_brief" data-analytics-label="line_up_artist" href="/artists/3407026-tove-styrke">Tove Styrke</a></span>, 
            <span >
              <a data-analytics-category="event_brief" data-analytics-label="line_up_artist" href="/artists/8882079-geowulf">Geowulf</a></span>
        </div>

        <div class="join-cta">
          <a href="https://accounts.songkick.com/signup/new?source_product=skweb&amp;event_id=30166884&amp;attendance_type=tracking" data-analytics-category="event_brief" data-analytics-label="join_songkick">Join Songkick</a>
            to track concerts and get alerts when tickets go on sale.
        </div>

        <div class="actions">
          <div class="attendance was-there">
  <form class="attendance app-store-redirect" data-stop-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" data-tracking-text="&lt;span class=&quot;icon&quot;&gt;&lt;/span&gt;&lt;span class=&quot;button-text&quot;&gt;I was there&lt;/span&gt;" data-analytics-category="signup_cta" data-analytics-label="30166884" data-analytics-action="i_was_there:cta_button" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="23YsegSadvKT0mSmVBfWk7m/Y2nNbeEsMy+TPgmVmmdjspIZ1cz3eN0a0XOTfZDd4DFvbFOogE+kDU7GL0FHwA==" />
    <input type="hidden" name="relationship_type" value="im_going">
    <input type="hidden" name="subject_id" value="30166884">
    <input type="hidden" name="subject_type" value="Event">
    <input type="hidden" name="success_url" value="/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen">
    <input type="hidden" name="app_store_redirect_url" value="">
    <button type="submit" class="im-going attendance-action" value="I was there"><span class="icon"></span><span class="button-text">I was there</span></button>
</form></div>

        </div>

    </div>

    <div class="col-4">
      <div class="profile-picture-and-actions">

        <div class="profile-picture-wrapper">
          <img class="profile-picture event" src="//images.sk-static.com/images/media/profile_images/artists/3407026/huge_avatar" alt="Tove Styrke live" title="Tove Styrke live" width="300" height="300">
        </div>

        <div class="event-moderation">
          <div class="flag-event">
            <a href="http://flagproblem.songkick.com/customer/portal/emails/new"
               target="_blank"
               data-analytics-category="event_brief"
               data-analytics-label="flag_event">
              Flag a problem
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>

<div class="container">
  <div class="row">
    <div class="col-8 primary">
      
      
      
      
      
      <div class="component venue-info">
  <h2>Venue</h2>
  <div class="venue-info-details">
    <a class="url" href="/venues/8280-hoxton-square-bar-and-kitchen">Hoxton Square Bar &amp; Kitchen</a>
    <p class="venue-hcard">
  <span>
      <span>2-4 Hoxton Square</span>
      <span>N1 6NU</span>
    <span>London, UK</span>
  </span>
    <span>+44 (0)20 7613 0709</span>
    <span><a class="url" target="_blank" href="http://www.hoxtonsquarebar.com" rel="nofollow">www.hoxtonsquarebar.com</a></span>
</p>

    <a href="/venues/8280-hoxton-square-bar-and-kitchen">27 upcoming concerts</a>
    <span class="capacity">Capacity: 250</span>
  </div>
</div>

      <div class="component similar-artists-events carousel">
  <h2>Similar artists with upcoming concerts</h2>
  <div class="carousel-list" data-per-page-count="4">
    <div class="carousel-item">
      <a class="artist-image" data-analytics-category="similar_artists_events" data-analytics-label="parent_artist_id_3407026" href="/concerts/33011184-super-duper-at-high-watt">
        <img src="//images.sk-static.com/images/media/profile_images/artists/919618/large_avatar" alt="Super Duper at High Watt (14 Apr 18) with Pink Slip and Jon Santana" class="artist" height="140" width="140">
</a>
      <div class="carousel-item-name">
          <a class="event-details" data-analytics-category="similar_artists_events" data-analytics-label="parent_artist_id_3407026" href="/artists/919618-super-duper">Super Duper</a>
      </div>

      <div class="carousel-item-details">
        <a data-analytics-category="similar_artists_events" data-analytics-label="parent_artist_id_3407026" href="/concerts/33011184-super-duper-at-high-watt">
          Sat 14 Apr 2018<br>

            <span class="event-details">High Watt</span>
          <span class="event-details">Nashville, TN, US</span>
</a>      </div>
    </div>
</div>

</div>

      <div class="component additional-details">
  <h2>Additional details</h2>
  <div class="additional-details-container">
      <p>Doors open: 20:00</p>
      <p>** THIS SHOW IS NOW SOLD OUT **</p>

<p>Facebook Event: www.facebook.com/events/1252411554870762</p>
  </div>
</div>

      <div class="component event-social">
  <h2>Share this concert</h2>
  <ul>
    <li><a href="https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen?utm_campaign=event-page&amp;utm_content=ZD0yNDU4MTk3&amp;utm_medium=shared&amp;utm_source=facebook" class="facebook-share button social-sharing facebook" data-analytics-category="social_share" data-analytics-label="facebook" title="Share on Facebook"><span class="icon"></span><span class="button-text">Share</span></a></li>
    <li><a href="https://twitter.com/share?url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F30166884-tove-styrke-at-hoxton-square-bar-and-kitchen%3Futm_campaign%3Devent-page%26utm_content%3DZD0yNDU4MTk3%26utm_medium%3Dshared%26utm_source%3Dtwitter&amp;via=songkick" class="tweet twitter button social-sharing" data-analytics-category="social_share" data-analytics-label="twitter"  title="Share on twiter"><span class="icon"></span><span class="button-text">Tweet</span></a></li>
    <li><a href="https://plus.google.com/share?url=https%3A%2F%2Fwww.songkick.com%2Fconcerts%2F30166884-tove-styrke-at-hoxton-square-bar-and-kitchen%3Futm_campaign%3Devent-page%26utm_content%3DZD0yNDU4MTk3%26utm_medium%3Dshared%26utm_source%3Dgoogleplus" class="googleplus button social-sharing googleplus" data-analytics-category="social_share" data-analytics-label="google" title="Share on Google+"><span class="icon"></span><span class="button-text">Share</span></a></li>
  </ul>
</div>

      
      
      
      
      <div class="component media-summary">

    
    
    <div class="media-group posters">
  <h2>Posters (1)</h2>
  <ul class="media-set posters inview" data-url="/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen/posters" data-per-page="8" data-total="1">
    <li>
      <div class="media-element">
  <a href="/posters/24535657" class="media-link" rel="nofollow" data-analytics-category="media_summary" data-analytics-label="poster">
    <span class="icon-expand">
      <img src="//assets.sk-static.com/images/nw/components/media-summary/icon-expand.svg" alt="expand" height="12" width="12">
    </span>

    <img src="//images.sk-static.com/images/media/img/col3/20170516-113736-663514.jpg" class="media-img" alt="Tove Styrke live" title="Tove Styrke live" width="220" height="311">
  </a>
</div>

    </li>
  </ul>

  <nav class="media-nav">
    <p class="browse"><a href="#posters" data-analytics-category="media_summary" data-analytics-label="see_all_posters">
      See all posters (1)
    </a></p>

    <button class="paginate paginate-prev" data-analytics-category="media_summary" data-analytics-label="paginate_posters_prev">
    </button>

    <button class="paginate paginate-next" data-analytics-category="media_summary" data-analytics-label="paginate_posters_next">
    </button>
  </nav>
</div>

</div>


    </div><div class="col-4 secondary">
      
      <div class="component related-events">
  <div class="related-events-content">
    <h5>Related upcoming events</h5>
    <ol>
        <li>
          <a data-analytics-category="related_events" data-analytics-label="parent_event_id_30166884" href="/concerts/30122844-mo-at-o2-academy-brixton">
          Wednesday 04 April 2018
          <span class="event-title"><strong>MØ</strong>
          O2 Academy Brixton, London</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events" data-analytics-label="parent_event_id_30166884" href="/concerts/32104889-misterwives-at-scala">
          Thursday 12 April 2018
          <span class="event-title"><strong>Misterwives</strong>
          Scala, London</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events" data-analytics-label="parent_event_id_30166884" href="/concerts/32576639-borns-at-koko">
          Thursday 17 May 2018
          <span class="event-title"><strong>BØRNS</strong>
          KOKO, London</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events" data-analytics-label="parent_event_id_30166884" href="/concerts/32006229-taylor-swift-at-wembley-stadium">
          Friday 22 June 2018
          <span class="event-title"><strong>Taylor Swift</strong>
          Wembley Stadium, London</span>
</a>        </li>
        <li>
          <a data-analytics-category="related_events" data-analytics-label="parent_event_id_30166884" href="/concerts/32086614-taylor-swift-at-wembley-stadium">
          Saturday 23 June 2018
          <span class="event-title"><strong>Taylor Swift</strong>
          Wembley Stadium, London</span>
</a>        </li>
    </ol>
  </div>
</div>

      <div class="component attendance-listing im-going">
  <h5>19 people were there</h5>
  <ul>
    <li>
      <a href="/users/moogmusic" title="moogmusic" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/3818446/medium_avatar" width="31" height="31" alt="moogmusic’s profile image" title="moogmusic’s profile image">
        <span><strong>moogmusic</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/izzywhizzy8" title="izzywhizzy8" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/12157983/medium_avatar" width="31" height="31" alt="izzywhizzy8’s profile image" title="izzywhizzy8’s profile image">
        <span><strong>izzywhizzy8</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/newtonateapples" title="newtonateapples" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/14054853/medium_avatar" width="31" height="31" alt="newtonateapples’s profile image" title="newtonateapples’s profile image">
        <span><strong>newtonateapples</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/electronicrumors" title="electronicrumors" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/23113209/medium_avatar" width="31" height="31" alt="electronicrumors’s profile image" title="electronicrumors’s profile image">
        <span><strong>electronicrumors</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/lara-turner" title="lara-turner" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/33657998/medium_avatar" width="31" height="31" alt="lara-turner’s profile image" title="lara-turner’s profile image">
        <span><strong>lara-turner</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/le2374" title="le2374" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/50955834/medium_avatar" width="31" height="31" alt="le2374’s profile image" title="le2374’s profile image">
        <span><strong>le2374</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/Gavlaar5" title="Gavlaar5" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/106522654/medium_avatar" width="31" height="31" alt="Gavlaar5’s profile image" title="Gavlaar5’s profile image">
        <span><strong>Gavlaar5</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/pia-jeanette-mariana" title="pia-jeanette-mariana" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/117177754/medium_avatar" width="31" height="31" alt="pia-jeanette-mariana’s profile image" title="pia-jeanette-mariana’s profile image">
        <span><strong>pia-jeanette-mariana</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/sam-spence" title="sam-spence" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/117526989/medium_avatar" width="31" height="31" alt="sam-spence’s profile image" title="sam-spence’s profile image">
        <span><strong>sam-spence</strong></span>
      </a>
    </li>
    <li>
      <a href="/users/leah-charlotte-mason" title="leah-charlotte-mason" rel="nofollow">
        <img class="profile-picture photo user" src="//images.sk-static.com/images/media/profile_images/users/117623519/medium_avatar" width="31" height="31" alt="leah-charlotte-mason’s profile image" title="leah-charlotte-mason’s profile image">
        <span><strong>leah-charlotte-mason</strong></span>
      </a>
    </li>
  </ul>
</div>

      <div class="event-moderation-actions">
  <div class="flag-event">
    <a href="http://flagproblem.songkick.com/customer/portal/emails/new"
       target="_blank"
       data-analytics-category="event_brief"
       data-analytics-label="flag_event">
      Flag a problem
    </a>
  </div>
</div>

    </div>
  </div>
</div>

<div class="microformat">
  <script type="application/ld+json">[{"@context":"http://schema.org","@type":"MusicEvent","name":"Tove Styrke","url":"https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"London","addressCountry":"UK","streetAddress":"2-4 Hoxton Square","postalCode":"N1 6NU"},"name":"Hoxton Square Bar \u0026 Kitchen","sameAs":"http://www.hoxtonsquarebar.com","geo":{"@type":"GeoCoordinates","latitude":51.527476,"longitude":-0.081657}},"startDate":"2017-06-12T20:00:00+0100","performer":[{"@type":"MusicGroup","name":"Tove Styrke","sameAs":"https://www.songkick.com/artists/3407026-tove-styrke?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Geowulf","sameAs":"https://www.songkick.com/artists/8882079-geowulf?utm_medium=organic\u0026utm_source=microformat"}]}]</script>
</div>




    <div class="footer-container">
      <div id="footer" class="container footer">
  <div class="row">
    <div class="col-3">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/info/about" rel="nofollow">About us</a></li>
        <li><a href="/blog" rel="nofollow">Blog</a></li>
        <li><a href="/jobs" rel="nofollow">Jobs</a></li>
        <li><a href="http://support.songkick.com/">Help &amp; FAQ</a></li>
        <li><a href="/leaderboards/popular_artists">Most popular charts</a></li>
      </ul>
    </div>
    <div class="col-3">
      <ul>
        <li><a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=tourboxforartists">Tourbox for artists</a></li>
        <li><a href="/developer"><abbr>API</abbr> information</a></li>
        <li><a href="/info/guidelines" rel="nofollow">Community guidelines</a></li>
        <li><a href="/info/terms" rel="nofollow">Terms of use</a></li>
        <li><a href="/info/privacy" rel="nofollow">Privacy policy</a></li>
        <li><a href="/info/security" rel="nofollow">Security</a></li>
      </ul>
    </div>
    <div class="col-6">
      <div class="tourbox-cta">
        <p>Get your tour dates seen everywhere.</p>
        <a href="//tourbox.songkick.com/?utm_medium=referral&amp;utm_source=songkick.com&amp;utm_campaign=visitor" class="sign-up-as-an-artist" data-analytics-category="navigation" data-analytics-label="sign_up_tourbox">Sign up as an artist</a>
      </div>
      <div class="social-container">
        <ul class="social-icons">
          <li>
            <a href="https://twitter.com/songkick">
              <img src="//assets.sk-static.com/assets/nw/furniture/icons/twitter-161f1e4.png" width="22" height="18" alt="Twitter">
              &nbsp;<span>Follow us.</span>
            </a>
          </li>
          <li>
            <a href="http://www.facebook.com/songkick">
              <img src="//assets.sk-static.com/assets/nw/furniture/icons/facebook-08359b5.png" width="18" height="18" alt="Facebook">
              &nbsp;<span>Like us.</span>
            </a>
          </li>
          <li>
            <span>But we really hope you love us.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>

    </div>
    <script type="text/javascript" src="//assets.sk-static.com/assets/manifests-1f4433a.js"></script><script type="text/javascript" src="//assets.sk-static.com/assets/app-242c373.js"></script>

  <script type="text/javascript" src="//assets.sk-static.com/assets/event_page-d99195f.js"></script>
  <script type="text/javascript">
      Songkick.EventBus.bind('app:initialize', function() {
        Songkick.EventBus.trigger('ui:event_page_past:view', {});
      });

    Songkick.EventBus.bind('app:initialize', function() {
      JS.require('jQuery', function() {
        $(document).on('click', 'a.buy-ticket-row', function(e) {
          Songkick.EventBus.trigger('ui:click', {
            category: 'tmp_growth_team_ticket_vendor',
            action: 'logged_out_click',
            label: '30166884',
            value: $(this).data('analytics-value')
          });
        });
      });
    });

      Songkick.EventBus.bind('app:initialize', function(config) {
        JS.require('jQuery.ui', function() {
          var modal = new Songkick.Component.Modal({
            analytics_category: 'signup_cta',
            analytics_label: '30166884',
            analytics_action_prefix: 'event:post_tv_click',
            cookie_key: 'vendor-click-cta',
            modal_class: 'vendor-signup-cta-container',
            component: '<div class="top-area">  <button class="close-widget close">    <img src="//assets.sk-static.com/assets/nw/components/vendor-click-signup-cta/close-b0c6998.svg" alt="Close" height="12" width="12">  </button>    <img alt="Tove Styrke live." width="70" height="70" class="artist artist-profile-image" src="//images.sk-static.com/images/media/profile_images/artists/3407026/large_avatar" />  <h2>Still searching for Tove Styrke tickets?</h2>  <p class="be-the-first-to-know">Be the first to know about tickets in the future.</p>  <p class="artist-trackings">43,284 other fans want alerts for this artist.</p></div><div class="bottom-area">  <div class="buttons">    <div class="tracking">  <form data-analytics-category="signup_cta" data-analytics-action="event:post_tv_click:cta_button" data-analytics-label="30166884" data-tracking-text="Yes, please notify me" data-stop-tracking-text="Yes, please notify me" class="app-store-redirect" action="/trackings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="3gR1/HgTCp7rIRefo9PQbWM80rJTHvg7VqadWttDQzpmwMufqUWLFKXpokpkuZYjOrLet83bmVjBhECi/ZeenQ==" />    <input type="hidden" name="relationship_type" value="concerts">    <input type="hidden" name="tracking_context" value="vendor">    <input type="hidden" name="subject_id" value="3407026">    <input type="hidden" name="subject_type" value="Artist">    <input type="hidden" name="success_url" value="/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen">    <input type="hidden" name="app_store_redirect_url" value="">    <button type="submit" class="artist signup-cta" value="Yes, please notify me">Yes, please notify me</button></form></div>    <a href="https://itunes.apple.com/us/app/apple-store/id438690886?ct=skweb%3Aevent%3Apost_tv_click%3Aapp_store_bt&amp;mt=8&amp;pt=307660" class="app-store-button" data-analytics-category="signup_cta" data-analytics-action="event:post_tv_click:app_store_bt" data-analytics-label="30166884">      <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/app-store-icon-e56abf8.svg" alt="Available on the App Store" class="store-button">    </a>    <a href="https://play.google.com/store/apps/details?id=com.songkick&amp;referrer=utm_campaign%3Devent%253Apost_tv_click%253Aapp_store_bt%26utm_medium%3D%26utm_source%3Dskweb" class="google-play-button" data-analytics-category="signup_cta" data-analytics-action="event:post_tv_click:app_store_bt" data-analytics-label="30166884">      <img src="//assets.sk-static.com/assets/nw/components/artist-off-tour-mobile/play-store-icon-79aae3f.svg" alt="Available on the Play Store" class="store-button">    </a>  </div>  <a class="close-message">I don’t want to hear about tickets</a></div>'
          });
          $('body').on('click', '.buy-ticket-row.third-party',
            function(e) { modal.show(modal);});
        });
      });
  </script>



<script type="text/javascript">
  /* <![CDATA[ */
  var google_conversion_id = 964669843;
  var google_custom_params = window.google_tag_params;
  var google_remarketing_only = true;
  /* ]]> */
</script>
<script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js">
</script>
<noscript>
  <div style="display:inline;">
  <img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/964669843/?value=0&amp;guid=ON&amp;script=0"/>
  </div>
</noscript>

<script type="text/javascript">
  SK.logged_in_user = {
    id:null,
    analyticsUserType: 'visitor'
  };

  JS.require("FB", 'jQuery', function() {
    Songkick.Facebook.init(
      "308540029359",
      ["email", "public_profile", "user_friends", "user_likes", "user_actions.music"],
      ["email", "public_profile", "user_friends", "user_likes", "user_actions.music", "publish_actions"],
      {events: Songkick.EventBus}
    );
  });
  var features = {};
  Songkick.EventBus.trigger('app:initialize', {
    events: Songkick.EventBus,
    features: features,
    promoteNativeApp: false,
    mobileSignupRedirectUrl: '',
    mobileAnalyticsEnabled: false,
  });
</script>

    
    
    
  <!-- start Mixpanel -->
  <script type="text/javascript">
    (function(e,a){if(!a.__SV){var b=window;try{var c,l,i,j=b.location,g=j.hash;c=function(a,b){return(l=a.match(RegExp(b+"=([^&]*)")))?l[1]:null};g&&c(g,"state")&&(i=JSON.parse(decodeURIComponent(c(g,"state"))),"mpeditor"===i.action&&(b.sessionStorage.setItem("_mpcehash",g),history.replaceState(i.desiredHash||"",e.title,j.pathname+j.search)))}catch(m){}var k,h;window.mixpanel=a;a._i=[];a.init=function(b,c,f){function e(b,a){var c=a.split(".");2==c.length&&(b=b[c[0]],a=c[1]);b[a]=function(){b.push([a].concat(Array.prototype.slice.call(arguments,
    0)))}}var d=a;"undefined"!==typeof f?d=a[f]=[]:f="mixpanel";d.people=d.people||[];d.toString=function(b){var a="mixpanel";"mixpanel"!==f&&(a+="."+f);b||(a+=" (stub)");return a};d.people.toString=function(){return d.toString(1)+".people (stub)"};k="disable time_event track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config reset people.set people.set_once people.increment people.append people.union people.track_charge people.clear_charges people.delete_user".split(" ");
    for(h=0;h<k.length;h++)e(d,k[h]);a._i.push([b,c,f])};a.__SV=1.2;b=e.createElement("script");b.type="text/javascript";b.async=!0;b.src="undefined"!==typeof MIXPANEL_CUSTOM_LIB_URL?MIXPANEL_CUSTOM_LIB_URL:"file:"===e.location.protocol&&"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//)?"https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js":"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";c=e.getElementsByTagName("script")[0];c.parentNode.insertBefore(b,c)}})(document,window.mixpanel||[]);

    mixpanel.init("854b86dd364733860c702c3f38c2cb56");
    mixpanel.identify("99e78efe-0000-4000-8000-0000851fbeaf");
    Songkick.EventBus.trigger('app:mixpanel:ready');
  </script>
  <!-- end Mixpanel -->


  </body>
</html>

```

### `tests/samples/songkick/tovestyrke.json`

```json
{
    "url": "https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen",
    "status": "200 OK",
    "microdata": [],
    "json-ld": [
        {
            "@context": "http://schema.org",
            "@type": "MusicEvent",
            "name": "Tove Styrke",
            "url": "https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen?utm_medium=organic&utm_source=microformat",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "London",
                    "addressCountry": "UK",
                    "streetAddress": "2-4 Hoxton Square",
                    "postalCode": "N1 6NU"
                },
                "name": "Hoxton Square Bar & Kitchen",
                "sameAs": "http://www.hoxtonsquarebar.com",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.527476,
                    "longitude": -0.081657
                }
            },
            "startDate": "2017-06-12T20:00:00+0100",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Tove Styrke",
                    "sameAs": "https://www.songkick.com/artists/3407026-tove-styrke?utm_medium=organic&utm_source=microformat"
                },
                {
                    "@type": "MusicGroup",
                    "name": "Geowulf",
                    "sameAs": "https://www.songkick.com/artists/8882079-geowulf?utm_medium=organic&utm_source=microformat"
                }
            ]
        }
    ],
    "rdfa": [
        {
            "@id": "https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen",
            "al:ios:app_name": [
                {
                    "@value": "Songkick Concerts"
                }
            ],
            "al:ios:app_store_id": [
                {
                    "@value": "438690886"
                }
            ],
            "al:ios:url": [
                {
                    "@value": "songkick://events/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen"
                }
            ],
            "http://ogp.me/ns#country-name": [
                {
                    "@value": "UK"
                }
            ],
            "http://ogp.me/ns#description": [
                {
                    "@value": "Past concert. Tove Styrke concert at Hoxton Square Bar & Kitchen in London on 12 Jun 2017."
                }
            ],
            "http://ogp.me/ns#image": [
                {
                    "@value": "http://images.sk-static.com/images/media/img/col6/20170515-103345-171924.jpg"
                }
            ],
            "http://ogp.me/ns#latitude": [
                {
                    "@value": "51.527476"
                }
            ],
            "http://ogp.me/ns#locality": [
                {
                    "@value": "London"
                }
            ],
            "http://ogp.me/ns#longitude": [
                {
                    "@value": "-0.081657"
                }
            ],
            "http://ogp.me/ns#postal-code": [
                {
                    "@value": "N1 6NU"
                }
            ],
            "http://ogp.me/ns#site_name": [
                {
                    "@value": "Songkick"
                }
            ],
            "http://ogp.me/ns#street-address": [
                {
                    "@value": "2-4 Hoxton Square"
                }
            ],
            "http://ogp.me/ns#title": [
                {
                    "@value": "Tove Styrke at Hoxton Square Bar & Kitchen (12 Jun 2017)"
                }
            ],
            "http://ogp.me/ns#type": [
                {
                    "@value": "songkick-concerts:concert"
                }
            ],
            "http://ogp.me/ns#url": [
                {
                    "@value": "https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen"
                }
            ],
            "http://www.facebook.com/2008/fbmlapp_id": [
                {
                    "@value": "308540029359"
                }
            ]
        }
    ],
    "opengraph": [
        {
            "namespace": {
                "og": "http://ogp.me/ns#",
                "fb": "http://www.facebook.com/2008/fbml",
                "concerts": "http://ogp.me/ns/fb/songkick-concerts#"
            },
            "properties": [
                [
                    "fb:app_id",
                    "308540029359"
                ],
                [
                    "og:site_name",
                    "Songkick"
                ],
                [
                    "og:type",
                    "songkick-concerts:concert"
                ],
                [
                    "og:title",
                    "Tove Styrke at Hoxton Square Bar & Kitchen (12 Jun 2017)"
                ],
                [
                    "og:description",
                    "Past concert. Tove Styrke concert at Hoxton Square Bar & Kitchen in London on 12 Jun 2017."
                ],
                [
                    "og:url",
                    "https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen"
                ],
                [
                    "og:image",
                    "http://images.sk-static.com/images/media/img/col6/20170515-103345-171924.jpg"
                ],
                [
                    "og:locality",
                    "London"
                ],
                [
                    "og:country-name",
                    "UK"
                ],
                [
                    "og:street-address",
                    "2-4 Hoxton Square"
                ],
                [
                    "og:postal-code",
                    "N1 6NU"
                ],
                [
                    "og:latitude",
                    "51.527476"
                ],
                [
                    "og:longitude",
                    "-0.081657"
                ]
            ]
        }
    ],
    "microformat": [],
    "dublincore": [
         {
             "namespaces": {},
             "elements": [
                 {
                     "name": "description",
                     "content": "Past concert. Tove Styrke concert with Geowulf at Hoxton Square Bar & Kitchen in London on 12 Jun 2017.",
                     "URI": "http://purl.org/dc/elements/1.1/description"
                 }
             ],
             "terms": [
             ]
         }
    ]
}
```

### `tests/samples/songkick/Years & Years Tickets, Tour Dates 2015 & Concerts.jsonld`

```jsonld
{
    "items": [
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/23948294-years-and-years-at-cliffs-pavillion?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Westcliff-on-sea","addressCountry":"UK","streetAddress":null,"postalCode":null},"name":"Cliffs Pavillion","sameAs":null,"geo":{"@type":"GeoCoordinates","latitude":51.535879,"longitude":0.696966}},"startDate":"2015-10-26T19:00:00+0000","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Shamir","sameAs":"http://www.songkick.com/artists/8335223-shamir?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/23948034-years-and-years-at-o2-academy-brixton?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"London","addressCountry":"UK","streetAddress":"211 Stockwell Road","postalCode":"SW9 9SL"},"name":"O2 Academy Brixton","sameAs":"http://www.o2academybrixton.co.uk/","geo":{"@type":"GeoCoordinates","latitude":51.4651204,"longitude":-0.1148897}},"startDate":"2015-10-27T19:00:00+0000","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Tove Styrke","sameAs":"http://www.songkick.com/artists/3407026-tove-styrke?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/23948009-years-and-years-at-o2-academy-brixton?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"London","addressCountry":"UK","streetAddress":"211 Stockwell Road","postalCode":"SW9 9SL"},"name":"O2 Academy Brixton","sameAs":"http://www.o2academybrixton.co.uk/","geo":{"@type":"GeoCoordinates","latitude":51.4651204,"longitude":-0.1148897}},"startDate":"2015-10-28T19:00:00+0000","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Shamir","sameAs":"http://www.songkick.com/artists/8335223-shamir?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/24491249-rita-ora-at-sse-arena-wembley?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"London","addressCountry":"UK","streetAddress":"Arena Square, Engineers Way","postalCode":"HA9 0AA"},"name":"SSE Arena, Wembley","sameAs":"http://www.wembley.co.uk/","geo":{"@type":"GeoCoordinates","latitude":51.5586053,"longitude":-0.2803252}},"startDate":"2015-10-29T19:30:00+0000","performer":[{"@type":"MusicGroup","name":"Rita Ora","sameAs":"http://www.songkick.com/artists/2312757-rita-ora?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Jason Derülo","sameAs":"http://www.songkick.com/artists/1055942-jason-derulo?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Jess Glynne","sameAs":"http://www.songkick.com/artists/4130211-jess-glynne?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Rudimental","sameAs":"http://www.songkick.com/artists/553588-rudimental?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Sigma","sameAs":"http://www.songkick.com/artists/147560-sigma?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Blonde","sameAs":"http://www.songkick.com/artists/878235-blonde?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Little Mix","sameAs":"http://www.songkick.com/artists/5427893-little-mix?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Krept \u0026 Konan","sameAs":"http://www.songkick.com/artists/3933961-krept-and-konan?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/24852229-years-and-years-at-victoria-warehouse?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Manchester","addressCountry":"UK","streetAddress":"Trafford Wharf Road","postalCode":"M17 1AB"},"name":"Victoria Warehouse","sameAs":null,"geo":{"@type":"GeoCoordinates","latitude":53.4690599,"longitude":-2.2989514}},"startDate":"2015-10-31T18:00:00+0000","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Wolf Alice","sameAs":"http://www.songkick.com/artists/4126816-wolf-alice?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"James Bay","sameAs":"http://www.songkick.com/artists/3741276-james-bay?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Little Simz","sameAs":"http://www.songkick.com/artists/6418354-little-simz?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Nothing But Thieves","sameAs":"http://www.songkick.com/artists/4441173-nothing-but-thieves?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/festivals/1397964-vevo-halloween/id/24846654-vevo-halloween-2015?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Manchester","addressCountry":"UK","streetAddress":"Trafford Wharf Road","postalCode":"M17 1AB"},"name":"Victoria Warehouse","sameAs":null,"geo":{"@type":"GeoCoordinates","latitude":53.4690599,"longitude":-2.2989514}},"startDate":"2015-10-31","performer":[{"@type":"MusicGroup","name":"James Bay","sameAs":"http://www.songkick.com/artists/3741276-james-bay?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Wolf Alice","sameAs":"http://www.songkick.com/artists/4126816-wolf-alice?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Nothing But Thieves","sameAs":"http://www.songkick.com/artists/4441173-nothing-but-thieves?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Little Simz","sameAs":"http://www.songkick.com/artists/6418354-little-simz?utm_medium=organic\u0026utm_source=microformat"}],"endDate":"2015-10-31"}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/23969779-years-and-years-at-mandela-hall?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Belfast","addressCountry":"UK","streetAddress":"75-87 University Road","postalCode":"BT7 1NF"},"name":"Mandela Hall","sameAs":null,"geo":{"@type":"GeoCoordinates","latitude":54.5860497,"longitude":-5.9292773}},"startDate":"2015-11-04T19:30:00+0000","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/24411724-years-and-years-at-olympia-theatre?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Dublin","addressCountry":"Ireland","streetAddress":"72 Dame Street","postalCode":"Dublin 2"},"name":"Olympia Theatre","sameAs":"http://www.olympia.ie/","geo":{"@type":"GeoCoordinates","latitude":53.3442216,"longitude":-6.2635249}},"startDate":"2015-11-05T19:00:00+0000","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/24236219-years-and-years-at-olympia-theatre?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Dublin","addressCountry":"Ireland","streetAddress":"72 Dame Street","postalCode":"Dublin 2"},"name":"Olympia Theatre","sameAs":"http://www.olympia.ie/","geo":{"@type":"GeoCoordinates","latitude":53.3442216,"longitude":-6.2635249}},"startDate":"2015-11-06T19:30:00+0000","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/24790629-years-and-years-at-casino-de-paris?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Paris","addressCountry":"France","streetAddress":"16, Rue De Clichy","postalCode":"75009"},"name":"Casino De Paris","sameAs":null,"geo":{"@type":"GeoCoordinates","latitude":48.8783356,"longitude":2.330072}},"startDate":"2015-11-16T19:30:00+0100","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/23948254-years-and-years-at-brighton-centre?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Brighton","addressCountry":"UK","streetAddress":"Kings Road","postalCode":"BN1 2GR"},"name":"Brighton Centre","sameAs":"http://www.brightoncentre.co.uk/scripts/default.htm","geo":{"@type":"GeoCoordinates","latitude":50.8212812,"longitude":-0.1488263}},"startDate":"2015-10-24T19:00:00+0100","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Shamir","sameAs":"http://www.songkick.com/artists/8335223-shamir?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/23948234-years-and-years-at-great-hall-cardiff-university?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Cardiff","addressCountry":"UK","streetAddress":"Park Place","postalCode":"CF10 3QN"},"name":"Great Hall, Cardiff University","sameAs":null,"geo":{"@type":"GeoCoordinates","latitude":51.4876847,"longitude":-3.1790238}},"startDate":"2015-10-22T19:00:00+0100","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Shamir","sameAs":"http://www.songkick.com/artists/8335223-shamir?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicEvent","name":"Years \u0026 Years","url":"http://www.songkick.com/concerts/23938624-years-and-years-at-o2-academy-bristol?utm_medium=organic\u0026utm_source=microformat","location":{"@type":"Place","address":{"@type":"PostalAddress","addressLocality":"Bristol","addressCountry":"UK","streetAddress":"Frogmore Street","postalCode":"BS1 5NA"},"name":"O2 Academy Bristol","sameAs":"http://www.o2academybristol.co.uk","geo":{"@type":"GeoCoordinates","latitude":51.4538978,"longitude":-2.6003513}},"startDate":"2015-10-21T19:00:00+0100","performer":[{"@type":"MusicGroup","name":"Years \u0026 Years","sameAs":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat"},{"@type":"MusicGroup","name":"Shamir","sameAs":"http://www.songkick.com/artists/8335223-shamir?utm_medium=organic\u0026utm_source=microformat"}]}],
        [{"@context":"http://schema.org","@type":"MusicGroup","name":"Years \u0026 Years","url":"http://www.songkick.com/artists/3976856-years-and-years?utm_medium=organic\u0026utm_source=microformat","image":"https://images.sk-static.com/images/media/profile_images/artists/3976856/card_avatar","logo":"https://images.sk-static.com/images/media/profile_images/artists/3976856/card_avatar","interactionCount":"54441 UserLikes","description":"Years \u0026 Years exploded onto London’s pop scene in 2010 and haven’t let up since. Their sound holds true to many of the familiar constructs of 80s synth pop, but much of their charm comes from their snappy yet original take on british electronic R\u0026B.","review":{"@type":"Review","reviewBody":"\"Thanks for coming out so early this morning, there's so many of you\", applauds Olly Alexander, the hipster-looking frontman of Years \u0026 Years. For a 1pm set on the final day of Bestvial, the electro/pop three piece who formed in 2010 drew a sizable growing crowd to the Big Top for their impressive set. While the rest of my friends stayed back at the camp nursing hangovers, I braved it alone, heading to the set by myself, and I'm so glad I did.\nOlly who is also an actor (he appeared in the final series of Skins as Jakob and also features in new film The Riot Club) and script writer, proved to be formidable frontman - quite the man of many talents. Live, his voice is a combination of Justin Timberlake's R\u0026B crooning and The Weeknd aka Abel Tesafye's soulful ‘What You Need’ haunting tones. Add some infectious, perfect for a summer festival, synth and bass lines courtesy of band members Michael Goldsworthy and Emre Turkmen and you've got pretty much the perfect mix.\nCurrent single 'Take Shelter' received an early but impressive outing, with most of the crowd singing along happily. A daring move, but it proves that Y\u0026Y have plenty more pop hits in waiting ready to smash the chart. One of these pop-hits-in-waiting is the especially brilliant 'Real', with its slinky electronic synth beat gliding along an infectious chorus; hand claps included.\nLater, the tempo is slowed down during ‘Eyes Shut, which sees Olly sit down at a piano where he is able to showcase his impressive vocal range. Wearing an oversized Stussy t-shirt and skinny jeans, while Michael wears a loudly printed flowery shirt, they are a boy band technically, but as far away from manufactured “pop”. so to speak, as possible.\nThey close with an as yet untitled, but perfect new single, which will undoubtedly send them further up the charts upon its release. By the time they tour with Clean Bandit in October, Years and Years will be close enough to household names satus!","author":"benjolley1"}}]
    ]
}

```

### `tests/samples/w3c/microdata.4.2.data.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>data element example</title>
 </head>
 <body>
  <h1 itemscope>
   <data itemprop="product-id" value="9678AOU879">The Instigator 2000</data>
  </h1>
 </body>
</html>

```

### `tests/samples/w3c/microdata.4.2.data.json`

```json
[
    {"properties": {"product-id": ["9678AOU879"]}}
]

```

### `tests/samples/w3c/microdata.4.2.meter.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>meter element example</title>
 </head>
 <body>
  <div itemscope itemtype="http://schema.org/Product">
   <span itemprop="name">Panasonic White 60L Refrigerator</span>
   <img src="panasonic-fridge-60l-white.jpg" alt="">
    <div itemprop="aggregateRating"
         itemscope itemtype="http://schema.org/AggregateRating">
     <meter itemprop="ratingValue" min=0 value=3.5 max=5>Rated 3.5/5</meter>
     (based on <span itemprop="reviewCount">11</span> customer reviews)
    </div>
  </div>
 </body>
</html>

```

### `tests/samples/w3c/microdata.4.2.meter.json`

```json
[
    {"properties": {"aggregateRating": [{"properties": {"ratingValue": ["3.5"],
                                                                   "reviewCount": ["11"]},
                                                    "type": ["http://schema.org/AggregateRating"]}],
                    "name": ["Panasonic White 60L Refrigerator"]},
                    "type": ["http://schema.org/Product"]
    }
]

```

### `tests/samples/w3c/microdata.4.2.strings.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>data element example</title>
 </head>
 <body>
  <div itemscope>
   <p>My name is <span itemprop="name">Neil</span>.</p>
   <p>My band is called <span itemprop="band">Four Parts Water</span>.</p>
   <p>I am <span itemprop="nationality">British</span>.</p>
  </div>
 </body>
</html>

```

### `tests/samples/w3c/microdata.4.2.strings.json`

```json
[
    {"properties": {"band": ["Four Parts Water"],
                    "name": ["Neil"],
                    "nationality": ["British"]}}
]

```

### `tests/samples/w3c/microdata.4.2.strings.unclean.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>data element example</title>
 </head>
 <body>
  <div itemscope>
   <p>My name is <span itemprop="name">Neil<style type="text/css">
body {
  color:red;
}
</style></span>.</p>
   <p>My band is called <span itemprop="band">Four Parts Water</span>.</p>
   <p>I am <span itemprop="nationality"><script>
      function count_rabbits() {
        for(var i=1; i<=3; i++) {
          alert("Rabbit "+i+" out of the hat!");
        }
      }
    </script>British</span>.</p>
  </div>
 </body>
</html>

```

### `tests/samples/w3c/microdata.4.2.strings.unclean.json`

```json
[
    {"properties": {"band": ["Four Parts Water"],
                    "name": ["Neil"],
                    "nationality": ["British"]}}
]

```

### `tests/samples/w3c/microdata.5.2.flat.json`

```json
[{"iid": 1,
  "properties": {"digital": ["Delta"],
                 "name": ["Tank Locomotive (DB 80)"],
                 "product-code": ["33041"],
                 "scale": ["HO"]},
  "type": ["http://md.example.com/loco",
           "http://md.example.com/lighting"]},
 {"iid": 2,
  "properties": {"name": ["Turnout Lantern Kit"],
                 "product-code": ["74470"],
                 "scale": ["HO"],
                 "track-type": ["C"]},
  "type": ["http://md.example.com/track",
           "http://md.example.com/lighting"]},
 {"iid": 3,
  "properties": {"name": ["Express Train Passenger Car (DB Am 203)"],
                 "product-code": ["8710"],
                 "scale": ["Z"]},
  "type": ["http://md.example.com/passengers"]}]

```

### `tests/samples/w3c/microdata.5.2.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>Photo gallery</title>
 </head>
 <body>

<dl itemscope itemtype="http://md.example.com/loco
                        http://md.example.com/lighting">
 <dt>Name:
 <dd itemprop="name">Tank Locomotive (DB 80)
 <dt>Product code:
 <dd itemprop="product-code">33041
 <dt>Scale:
 <dd itemprop="scale">HO
 <dt>Digital:
 <dd itemprop="digital">Delta
</dl>

<dl itemscope itemtype="http://md.example.com/track
                       http://md.example.com/lighting">
 <dt>Name:
 <dd itemprop="name">Turnout Lantern Kit
 <dt>Product code:
 <dd itemprop="product-code">74470
 <dt>Purpose:
 <dd>For retrofitting 2 <span itemprop="track-type">C</span> Track
 turnouts. <meta itemprop="scale" content="HO">
</dl>

<dl itemscope itemtype="http://md.example.com/passengers">
 <dt>Name:
 <dd itemprop="name">Express Train Passenger Car (DB Am 203)
 <dt>Product code:
 <dd itemprop="product-code">8710
 <dt>Scale:
 <dd itemprop="scale">Z
</dl>

  </footer>
 </body>
</html>

```

### `tests/samples/w3c/microdata.5.2.json`

```json
[{"properties": {"digital": ["Delta"],
                 "name": ["Tank Locomotive (DB 80)"],
                 "product-code": ["33041"],
                 "scale": ["HO"]},
  "type": ["http://md.example.com/loco",
           "http://md.example.com/lighting"]},
 {"properties": {"name": ["Turnout Lantern Kit"],
                 "product-code": ["74470"],
                 "scale": ["HO"],
                 "track-type": ["C"]},
  "type": ["http://md.example.com/track",
           "http://md.example.com/lighting"]},
 {"properties": {"name": ["Express Train Passenger Car (DB Am 203)"],
                 "product-code": ["8710"],
                 "scale": ["Z"]},
  "type": ["http://md.example.com/passengers"]}]

```

### `tests/samples/w3c/microdata.5.2.withtext.json`

```json
[{"properties": {"digital": "Delta",
                 "name": "Tank Locomotive (DB 80)",
                 "product-code": "33041",
                 "scale": "HO"},
  "textContent": "Name:\nTank Locomotive (DB 80)\nProduct code:\n33041\nScale:\nHO\nDigital:\nDelta",
  "type": ["http://md.example.com/loco",
           "http://md.example.com/lighting"]},
 {"properties": {"name": "Turnout Lantern Kit",
                 "product-code": "74470",
                 "scale": "HO",
                 "track-type": "C"},
  "textContent": "Name:\nTurnout Lantern Kit\nProduct code:\n74470\nPurpose:\nFor retrofitting 2 C Track turnouts.",
  "type": ["http://md.example.com/track",
           "http://md.example.com/lighting"]},
 {"properties": {"name": "Express Train Passenger Car (DB Am 203)",
                 "product-code": "8710",
                 "scale": "Z"},
  "textContent": "Name:\nExpress Train Passenger Car (DB Am 203)\nProduct code:\n8710\nScale:\nZ",
  "type": "http://md.example.com/passengers"}]

```

### `tests/samples/w3c/microdata.5.3.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>Photo gallery</title>
 </head>
 <body>

<div itemscope>
 <p itemprop="a">1</p>
 <p itemprop="a">2</p>
 <p itemprop="b">test</p>
</div>

<div itemscope>
 <p itemprop="b">test</p>
 <p itemprop="a">1</p>
 <p itemprop="a">2</p>
</div>

<div itemscope>
 <p itemprop="a">1</p>
 <p itemprop="b">test</p>
 <p itemprop="a">2</p>
</div>

<div id="x">
 <p itemprop="a">1</p>
</div>
<div itemscope itemref="x">
 <p itemprop="b">test</p>
 <p itemprop="a">2</p>
</div>

  </footer>
 </body>
</html>

```

### `tests/samples/w3c/microdata.5.3.json`

```json
[
 {"properties": {"a": ["1", "2"], "b": ["test"]}},
 {"properties": {"a": ["1", "2"], "b": ["test"]}},
 {"properties": {"a": ["1", "2"], "b": ["test"]}},
 {"properties": {"a": ["2", "1"], "b": ["test"]}}
]


```

### `tests/samples/w3c/microdata.5.5.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>Photo gallery</title>
 </head>
 <body>
  <h1>My photos</h1>
  <figure itemscope itemtype="http://n.whatwg.org/work" itemref="licenses">
   <img itemprop="work" src="images/house.jpeg" alt="A white house, boarded up, sits in a forest.">
   <figcaption itemprop="title">The house I found.</figcaption>
  </figure>
  <figure itemscope itemtype="http://n.whatwg.org/work" itemref="licenses">
   <img itemprop="work" src="images/mailbox.jpeg" alt="Outside the house is a mailbox. It has a leaflet inside.">
   <figcaption itemprop="title">The mailbox.</figcaption>
  </figure>
  <footer>
   <p id="licenses">All images licensed under the <a itemprop="license"
   href="http://www.opensource.org/licenses/mit-license.php">MIT
   license</a>.</p>
  </footer>
 </body>
</html>

```

### `tests/samples/w3c/microdata.5.5.json`

```json
[{"properties": {"title": ["The house I found."],
                 "work": ["images/house.jpeg"],
                 "license": ["http://www.opensource.org/licenses/mit-license.php"]},
  "type": ["http://n.whatwg.org/work"]},
 {"properties": {"title": ["The mailbox."],
                 "work": ["images/mailbox.jpeg"],
                 "license": ["http://www.opensource.org/licenses/mit-license.php"]},
  "type": ["http://n.whatwg.org/work"]}]

```

### `tests/samples/w3c/microdata.7.1.flat.json`

```json
[
    {
      "iid": 1,
      "type": [ "http://schema.org/BlogPosting" ],
      "properties": {
        "comment": [ { "iid_ref": 2 }, { "iid_ref": 4 } ],
        "datePublished": [ "2013-08-29" ],
        "headline": [ "Progress report" ],
        "url": [ "http://blog.example.com/progress-report?comments=0" ]
      }
    },
    {
      "iid": 2,
      "type": [ "http://schema.org/UserComments" ],
      "properties": {
        "commentTime": [ "2013-08-29" ],
        "creator": [ { "iid_ref": 3 } ],
        "url": [ "http://blog.example.com/progress-report#c1" ]
      }
    },
    {
      "iid": 3,
      "type": [ "http://schema.org/Person" ],
      "properties": {
        "name": [ "Greg" ]
      }
    },
    {
      "iid": 4,
      "type": [ "http://schema.org/UserComments" ],
      "properties": { "commentTime": [ "2013-08-29" ],
        "creator": [ { "iid_ref": 5 } ],
        "url": [ "http://blog.example.com/progress-report#c2" ]
      }
    },
    {
      "iid": 5,
      "type": [ "http://schema.org/Person" ],
      "properties": {
        "name": [ "Charlotte" ]
      }
    }
]

```

### `tests/samples/w3c/microdata.7.1.html`

```html
<!DOCTYPE HTML>
<title>My Blog</title>
<article itemscope itemtype="http://schema.org/BlogPosting">
 <header>
  <h1 itemprop="headline">Progress report</h1>
  <p><time itemprop="datePublished" datetime="2013-08-29">today</time></p>
  <link itemprop="url" href="?comments=0">
 </header>
 <p>All in all, he's doing well with his swim lessons. The biggest thing was he had trouble
 putting his head in, but we got it down.</p>
 <section>
  <h1>Comments</h1>
  <article itemprop="comment" itemscope itemtype="http://schema.org/UserComments" id="c1">
   <link itemprop="url" href="#c1">
   <footer>
    <p>Posted by: <span itemprop="creator" itemscope itemtype="http://schema.org/Person">
     <span itemprop="name">Greg</span>
    </span></p>
    <p><time itemprop="commentTime" datetime="2013-08-29">15 minutes ago</time></p>
   </footer>
   <p>Ha!</p>
  </article>
  <article itemprop="comment" itemscope itemtype="http://schema.org/UserComments" id="c2">
   <link itemprop="url" href="#c2">
   <footer>
    <p>Posted by: <span itemprop="creator" itemscope itemtype="http://schema.org/Person">
     <span itemprop="name">Charlotte</span>
    </span></p>
    <p><time itemprop="commentTime" datetime="2013-08-29">5 minutes ago</time></p>
   </footer>
   <p>When you say "we got it down"...</p>
  </article>
 </section>
</article>

```

### `tests/samples/w3c/microdata.7.1.json`

```json
[
    {
      "type": [ "http://schema.org/BlogPosting" ],
      "properties": {
        "headline": [ "Progress report" ],
        "datePublished": [ "2013-08-29" ],
        "url": [ "http://blog.example.com/progress-report?comments=0" ],
        "comment": [
          {
            "type": [ "http://schema.org/UserComments" ],
            "properties": {
              "url": [ "http://blog.example.com/progress-report#c1" ],
              "creator": [
                {
                  "type": [ "http://schema.org/Person" ],
                  "properties": {
                    "name": [ "Greg" ]
                  }
                }
              ],
              "commentTime": [ "2013-08-29" ]
            }
          },
          {
            "type": [ "http://schema.org/UserComments" ],
            "properties": {
              "url": [ "http://blog.example.com/progress-report#c2" ],
              "creator": [
                {
                  "type": [ "http://schema.org/Person" ],
                  "properties": {
                    "name": [ "Charlotte" ]
                  }
                }
              ],
              "commentTime": [ "2013-08-29" ]
            }
          }
        ]
      }
    }
]

```

### `tests/samples/w3c/microdata.object.html`

```html
<!DOCTYPE HTML>
<html>
 <head>
  <title>object element example</title>
 </head>
 <body>

  <div itemscope="" itemtype="http://schema.org/Thing">
    <object itemprop="object" data="foo"></object>
  </div>

 </body>
</html>

```

### `tests/samples/w3c/microdata.object.json`

```json
[
{"properties": {"object": ["http://www.example.com/microdata/foo"]},
 "type": ["http://schema.org/Thing"]}
]

```

### `tests/samples/w3crdfa/w3c.rdf11primer.example014.expanded.json`

```json
[
  {
    "@id": "http://data.europeana.eu/item/04802/243FA8618938F4117025F17A8B813C5F9AA4D619",
    "http://purl.org/dc/terms/subject": [
      {
        "@id": "http://www.wikidata.org/entity/Q12418"
      }
    ]
  },
  {
    "@id": "http://example.org/bob#me",
    "@type": [
      "http://xmlns.com/foaf/0.1/Person"
    ],
    "http://schema.org/birthDate": [
      {
        "@type": "http://www.w3.org/2001/XMLSchema#date",
        "@value": "1990-07-04"
      }
    ],
    "http://xmlns.com/foaf/0.1/knows": [
      {
        "@id": "http://example.org/alice#me"
      }
    ],
    "http://xmlns.com/foaf/0.1/topic_interest": [
      {
        "@id": "http://www.wikidata.org/entity/Q12418"
      }
    ]
  },
  {
    "@id": "http://www.wikidata.org/entity/Q12418",
    "http://purl.org/dc/terms/creator": [
      {
        "@id": "http://dbpedia.org/resource/Leonardo_da_Vinci"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "Mona Lisa"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdf11primer.example014.html`

```html
<body prefix="foaf: http://xmlns.com/foaf/0.1/
                 schema: http://schema.org/
                 dcterms: http://purl.org/dc/terms/">
  <div resource="http://example.org/bob#me" typeof="foaf:Person">
    <p>
      Bob knows <a property="foaf:knows" href="http://example.org/alice#me">Alice</a>
      and was born on the <time property="schema:birthDate" datatype="xsd:date">1990-07-04</time>.
    </p>
    <p>
      Bob is interested in <span property="foaf:topic_interest"
      resource="http://www.wikidata.org/entity/Q12418">the Mona Lisa</span>.
    </p>
  </div>
  <div resource="http://www.wikidata.org/entity/Q12418">
    <p>
      The <span property="dcterms:title">Mona Lisa</span> was painted by
      <a property="dcterms:creator" href="http://dbpedia.org/resource/Leonardo_da_Vinci">Leonardo da Vinci</a>
      and is the subject of the video
      <a href="http://data.europeana.eu/item/04802/243FA8618938F4117025F17A8B813C5F9AA4D619">'La Joconde à Washington'</a>.
    </p>
  </div>
  <div resource="http://data.europeana.eu/item/04802/243FA8618938F4117025F17A8B813C5F9AA4D619">
      <link property="dcterms:subject" href="http://www.wikidata.org/entity/Q12418"/>
  </div>
</body>

```

### `tests/samples/w3crdfa/w3c.rdfalite.example003.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://schema.org/"
      }
    ]
  },
  {
    "@id": "_:000001",
    "@type": [
      "http://schema.org/Person"
    ],
    "http://schema.org/name": [
      {
        "@value": "Manu Sporny"
      }
    ],
    "http://schema.org/telephone": [
      {
        "@value": "1-800-555-0199"
      }
    ],
    "http://schema.org/url": [
      {
        "@id": "http://manu.sporny.org/"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfalite.example003.html`

```html
<p vocab="http://schema.org/" typeof="Person">
   My name is
   <span property="name">Manu Sporny</span>
   and you can give me a ring via
   <span property="telephone">1-800-555-0199</span>
   or visit
   <a property="url" href="http://manu.sporny.org/">my homepage</a>.
</p>

```

### `tests/samples/w3crdfa/w3c.rdfalite.example004.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://schema.org/"
      }
    ]
  },
  {
    "@id": "http://www.example.com/index.html#manu",
    "@type": [
      "http://schema.org/Person"
    ],
    "http://schema.org/image": [
      {
        "@id": "http://manu.sporny.org/images/manu.png"
      }
    ],
    "http://schema.org/name": [
      {
        "@value": "Manu Sporny"
      }
    ],
    "http://schema.org/telephone": [
      {
        "@value": "1-800-555-0199"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfalite.example004.html`

```html
<p vocab="http://schema.org/" resource="#manu" typeof="Person">
   My name is
   <span property="name">Manu Sporny</span>
   and you can give me a ring via
   <span property="telephone">1-800-555-0199</span>.
   <img property="image" src="http://manu.sporny.org/images/manu.png" />
</p>

```

### `tests/samples/w3crdfa/w3c.rdfalite.example005.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html#manu",
    "@type": [
      "http://schema.org/Person"
    ],
    "http://open.vocab.org/terms/preferredAnimal": [
      {
        "@value": "Liger"
      }
    ],
    "http://schema.org/image": [
      {
        "@id": "http://manu.sporny.org/images/manu.png"
      }
    ],
    "http://schema.org/name": [
      {
        "@value": "Manu Sporny"
      }
    ],
    "http://schema.org/telephone": [
      {
        "@value": "1-800-555-0199"
      }
    ]
  },
  {
    "@id": "http://www.example.com/index.html",
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://schema.org/"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfalite.example005.html`

```html
<p vocab="http://schema.org/" prefix="ov: http://open.vocab.org/terms/" resource="#manu" typeof="Person">
   My name is
   <span property="name">Manu Sporny</span>
   and you can give me a ring via
   <span property="telephone">1-800-555-0199</span>.
   <img property="image" src="http://manu.sporny.org/images/manu.png" />
   My favorite animal is the <span property="ov:preferredAnimal">Liger</span>.
</p>

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example005.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://purl.org/dc/terms/created": [
      {
        "@value": "2011-09-10"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "The Trouble with Bob"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example005.html`

```html
<html>
<head>
  ...
</head>
<body>
  ...
  <h2 property="http://purl.org/dc/terms/title">The Trouble with Bob</h2>
  <p>Date: <span property="http://purl.org/dc/terms/created">2011-09-10</span></p>
  ...
</body>

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example006.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://purl.org/dc/terms/created": [
      {
        "@value": "2011-09-10"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "The Trouble with Bob"
      }
    ],
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://purl.org/dc/terms/"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example006.html`

```html
<html>
<head>
  <meta charset="utf-8" />
  <title>Example</title>
</head>
<body vocab="http://purl.org/dc/terms/">
  ...
  <h2 property="title">The Trouble with Bob</h2>
  <p>Date: <span property="created">2011-09-10</span></p>
  ...
</body>
</html>

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example007.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://purl.org/dc/terms/created": [
      {
        "@value": "2011-09-10"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "The Trouble with Bob"
      }
    ],
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://purl.org/dc/terms/"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example007.html`

```html
<html>
<head>
  <meta charset="utf-8" />
  <title>Example</title>
</head>
<body vocab="http://purl.org/dc/terms/">
  ...
  <h2 property="title">The Trouble with Bob</h2>
  <p>Date: <span property="http://purl.org/dc/terms/created">2011-09-10</span></p>
  ...
</body>

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example008.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://creativecommons.org/ns#license": [
      {
        "@id": "http://creativecommons.org/licenses/by/3.0/"
      }
    ],
    "http://purl.org/dc/terms/created": [
      {
        "@value": "2011-09-10"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "The Trouble with Bob"
      }
    ],
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://purl.org/dc/terms/"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example008.html`

```html
<html>
<body vocab="http://purl.org/dc/terms/">
  ...
  <h2 property="title">The Trouble with Bob</h2>
  <p>Date: <span property="created">2011-09-10</span></p>
  ...
  <p>All content on this site is licensed under
   <a property="http://creativecommons.org/ns#license" href="http://creativecommons.org/licenses/by/3.0/">
     a Creative Commons License</a>. ©2011 Alice Birpemswick.</p>
</body>
</html>

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example009.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://creativecommons.org/ns#license": [
      {
        "@id": "http://creativecommons.org/licenses/by/3.0/"
      }
    ],
    "http://purl.org/dc/terms/created": [
      {
        "@value": "2011-09-10"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "The Trouble with Bob"
      }
    ],
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://purl.org/dc/terms/"
      },
      {
        "@id": "http://creativecommons.org/ns#"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example009.html`

```html
<html>
<body vocab="http://purl.org/dc/terms/">
  ...
  <h2 property="title">The Trouble with Bob</h2>
  <p>Date: <span property="created">2011-09-10</span></p>
  ...
  <p vocab="http://creativecommons.org/ns#">All content on this site is licensed under
    <a property="license" href="http://creativecommons.org/licenses/by/3.0/">
      a Creative Commons License</a>. ©2011 Alice Birpemswick.</p>
</body>
</html>

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example010.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/alice/posts/trouble_with_bob",
    "http://purl.org/dc/terms/created": [
      {
        "@value": "2011-09-10"
      }
    ],
    "http://purl.org/dc/terms/creator": [
      {
        "@value": "Alice"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "The trouble with Bob"
      }
    ]
  },
  {
    "@id": "http://www.example.com/alice/posts/jos_barbecue",
    "http://purl.org/dc/terms/created": [
      {
        "@value": "2011-09-14"
      }
    ],
    "http://purl.org/dc/terms/creator": [
      {
        "@value": "Eve"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "Jo's Barbecue"
      }
    ]
  },
  {
    "@id": "http://www.example.com/index.html",
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://purl.org/dc/terms/"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example010.html`

```html
<body vocab="http://purl.org/dc/terms/">
   ...
   <div resource="/alice/posts/trouble_with_bob">
      <h2 property="title">The trouble with Bob</h2>
      <p>Date: <span property="created">2011-09-10</span></p>
      <h3 property="creator">Alice</h3>
      ...
   </div>
   ...
   <div resource="/alice/posts/jos_barbecue">
      <h2 property="title">Jo's Barbecue</h2>
      <p>Date: <span property="created">2011-09-14</span></p>
      <h3 property="creator">Eve</h3>
      ...
   </div>
   ...
</body>

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example011.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/alice/posts/trouble_with_bob",
    "http://purl.org/dc/terms/title": [
      {
        "@value": "The trouble with Bob"
      }
    ]
  },
  {
    "@id": "http://www.example.com/alice/posts/jos_barbecue",
    "http://purl.org/dc/terms/created": [
      {
        "@value": "2011-09-14"
      }
    ],
    "http://purl.org/dc/terms/creator": [
      {
        "@value": "Eve"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "Jo's Barbecue"
      }
    ]
  },
  {
    "@id": "http://example.com/bob/photos/sunset.jpg",
    "http://purl.org/dc/terms/creator": [
      {
        "@value": "Bob"
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@value": "Beautiful Sunset"
      }
    ]
  },
  {
    "@id": "http://www.example.com/index.html",
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://purl.org/dc/terms/"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example011.html`

```html
<body vocab="http://purl.org/dc/terms/">
   ...
  <div resource="/alice/posts/trouble_with_bob">
      <h2 property="title">The trouble with Bob</h2>
      ...
      The trouble with Bob is that he takes much better photos than I do:
      ...
      <div resource="http://example.com/bob/photos/sunset.jpg">
        <img src="http://example.com/bob/photos/sunset.jpg" />
        <span property="title">Beautiful Sunset</span>
        by <span property="creator">Bob</span>.
      </div>
   </div>
   ...
   <div resource="/alice/posts/jos_barbecue">
      <h2 property="title">Jo's Barbecue</h2>
      <p>Date: <span property="created">2011-09-14</span></p>
      <h3 property="creator">Eve</h3>
      ...
   </div>
   ...
</body>

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example015.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://www.w3.org/ns/rdfa#usesVocabulary": [
      {
        "@id": "http://xmlns.com/foaf/0.1/"
      }
    ]
  },
  {
    "@id": "_:000001",
    "@type": [
      "http://xmlns.com/foaf/0.1/Person"
    ],
    "http://xmlns.com/foaf/0.1/mbox": [
      {
        "@id": "mailto:alice@example.com"
      }
    ],
    "http://xmlns.com/foaf/0.1/name": [
      {
        "@value": "Alice Birpemswick"
      }
    ],
    "http://xmlns.com/foaf/0.1/phone": [
      {
        "@id": "tel:+1-617-555-7332"
      }
    ]
  }
]

```

### `tests/samples/w3crdfa/w3c.rdfaprimer.example015.html`

```html
<div vocab="http://xmlns.com/foaf/0.1/" typeof="Person">
  <p>
    <span property="name">Alice Birpemswick</span>,
    Email: <a property="mbox" href="mailto:alice@example.com">alice@example.com</a>,
    Phone: <a property="phone" href="tel:+1-617-555-7332">+1 617.555.7332</a>
  </p>
</div>

```

### `tests/samples/websites/microdata-with-description.json`

```json
[
 {
  "type": "http://schema.org/Product",
  "properties": {
   "name": "Johnsons 4 Fleas Cats & Kittens Tablets",
   "brand": "Johnsons",
   "offers": [
    {
     "type": "http://schema.org/AggregateOffer",
     "properties": {
      "offercount": "2",
      "priceCurrency": "GBP",
      "lowPrice": "5.29",
      "highPrice": "9.56"
     }
    },
    {
     "type": "http://schema.org/Offer",
     "properties": {
      "name": "Johnsons 4 Fleas Cats & Kittens Tablets 6 Treatment Pack",
      "sku": "CS20858_1",
      "price": "9.56",
      "priceCurrency": "GBP",
      "availability": "http://schema.org/InStock",
      "itemCondition": "http://schema.org/NewCondition"
     }
    },
    {
     "type": "http://schema.org/Offer",
     "properties": {
      "name": "Johnsons 4 Fleas Cats & Kittens Tablets 3 Treatment Pack",
      "sku": "CS20858_2",
      "price": "5.29",
      "priceCurrency": "GBP",
      "availability": "http://schema.org/InStock",
      "itemCondition": "http://schema.org/NewCondition"
     }
    }
   ],
   "image": "https://res.cloudinary.com/monsterpetsupplies/image/upload/f_auto,c_pad,w_500,h_500,q_75/q_100/v1481710164/cat_kitten_flea_tabs_3_eaunpi.jpg",
   "description": "Johnsons 4 Fleas Cats & Kittens - 3 Treatment Pack, 6 Treatment Pack\n\nFor use with Cats and Kittens over 4 weeks of age between 1 and 11kg.\nJohnson's 4fleas tablets are an easy to use oral treatment to kill adult fleas found on your pet.\nEffects on the fleas may be seen as soon as 15 minutes after administration.\nBetween 95 - 100% of fleas will be killed off in the first six hours, but ALL adult fleas will be gone after a day.\nThese tablets can be given directly to the mouth or may be mixed in a small portion f our pet's favourite food and given immediately. Administer a single tablet on an day when fleas are seen on your pet. Repeat on any subsequent day as necessary. Do not give more than one treatment per day.\nYou may notice your pet scratching more than usual for the first half hour after administration; this is completely normal and caused by the fleas reacting to Johnson's 4Fleas tablets.\nWhile highly effective by themselves, 4Fleas is great when used as part of a programme to eliminate fleas and their larvae from both pets and their surroundings."
  }
 }
]
```

### `tests/samples/wikipedia/xhtml+rdfa.expanded.json`

```json
[
  {
    "@id": "http://www.example.com/index.html",
    "http://www.w3.org/2000/01/rdf-schema#seeAlso": [
      {
        "@id": "http://www.example.com/about.htm"
      }
    ],
    "http://www.w3.org/2000/10/swap/pim/contact#address": [
      {
        "@id": "_:000001"
      }
    ],
    "http://xmlns.com/foaf/0.1/name": [
      {
        "@language": "en",
        "@value": "Jerry Smith"
      }
    ],
    "http://xmlns.com/foaf/0.1/phone": [
      {
        "@id": "tel:+6112345678"
      }
    ],
    "http://xmlns.com/foaf/0.1/primaryTopic": [
      {
        "@id": "http://www.example.com/metadata/foaf.rdf"
      }
    ]
  },
  {
    "@id": "_:000001",
    "http://www.w3.org/2000/01/rdf-schema#seeAlso": [
      {
        "@id": "http://dbpedia.org/resource/Adelaide"
      }
    ],
    "http://www.w3.org/2000/10/swap/pim/contact#city": [
      {
        "@language": "en",
        "@value": "Adelaide"
      }
    ]
  }
]

```

### `tests/samples/wikipedia/xhtml+rdfa.html`

```html
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML+RDFa 1.1//EN"
        "http://www.w3.org/MarkUp/DTD/xhtml-rdfa-2.dtd">
<html version="XHTML+RDFa 1.1" xmlns="http://www.w3.org/1999/xhtml"
      xmlns:contact="http://www.w3.org/2000/10/swap/pim/contact#"
      xmlns:foaf="http://xmlns.com/foaf/0.1/"
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
      xml:lang="en"
      lang="en">
<head>
    <title>XHTML+RDFa example</title>
    <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta name="content-language" content="en" />
    <meta name="robots" content="index, follow" />
    <link rel="schema.DC" href="http://purl.org/dc/elements/1.1/" />
    <link rel="schema.DCTERMS" href="http://purl.org/dc/terms/" />
    <link rel="alternate" type="application/rss+xml" title="Feed channel of XHTML+RDFa example page" href="http://www.example.com/rss.xml" />
    <meta name="DC.title" content="XHTML+RDFa example" />
    <meta name="DC.subject" content="XHTML+RDFa, semantic web" />
    <meta name="DC.description" content="Example for Extensible Hypertext Markup Language + Resource Description Framework – in – attributes." />
    <meta name="DC.format" content="application/xhtml+xml" />
    <meta name="DC.language" content="en" />
    <link rel="shortcut icon" href="favicon.ico" />
    <link  rel="stylesheet" type="text/css" href="main.css" title="main styles" />
    <link rel="foaf:primaryTopic" type="application/rdf+xml" title="FOAF" href="http://www.example.com/metadata/foaf.rdf" />
    <script type="text/javascript" src="js/click.js"></script>
</head>
<body>
<div class="content">
    <p>
        <span property="foaf:name">Jerry Smith</span><br />
        <i>Senior developer, QA</i><br />
        <a title="More about me" rel="rdfs:seeAlso" href="about.htm">More...</a>
    </p>
    <p rel="contact:address">
        93 Rose Ave <br />
        <a property="contact:city" rel="rdfs:seeAlso" title="Adelaide on Wikipedia" resource="http://dbpedia.org/resource/Adelaide"
           href="http://en.wikipedia.org/wiki/Adelaide">Adelaide</a>
    </p>
    <p>
        <span rel="foaf:phone" resource="tel:+6112345678">+61 12/345-678</span>
    </p>
</div>
</body>
</html>

```

### `tests/test_dublincore.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest

from extruct.dublincore import DublinCoreExtractor
from tests import get_testdata, jsonize_dict


class TestDublincore(unittest.TestCase):

    maxDiff = None

    def test_dublincore(self):
        body = get_testdata("misc", "dublincore_test.html")
        expected = json.loads(
            get_testdata("misc", "dublincore_test.json").decode("UTF-8")
        )

        dublincorext = DublinCoreExtractor()
        data = dublincorext.extract(body)
        self.assertEqual(jsonize_dict(data), expected)

```

### `tests/test_extruct_uniform.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest

import extruct
from extruct.utils import parse_html
from tests import get_testdata, jsonize_dict, replace_node_ref_with_node_id


class TestFlatten(unittest.TestCase):

    maxDiff = None

    def test_microdata(self):
        body, tree, expected = self._testdata_html_and_tree(
            "schema.org",
            "CreativeWork.001.html",
            "CreativeWork_flat.001.json",
        )
        syntax = "microdata"
        data = extruct.extract(body, uniform=True, syntaxes=[syntax])
        self.assertEqual(jsonize_dict(data[syntax]), expected[syntax])

        data = extruct.extract(tree, uniform=True, syntaxes=[syntax])
        self.assertEqual(jsonize_dict(data[syntax]), expected[syntax])

    def test_opengraph(self):
        body, tree, expected = self._testdata_html_and_tree(
            "misc",
            "opengraph_test.html",
            "opengraph_flat_test.json",
        )
        syntax = "opengraph"
        data = extruct.extract(body, uniform=True, syntaxes=[syntax])
        self.assertEqual(jsonize_dict(data[syntax]), expected)

        data = extruct.extract(tree, uniform=True, syntaxes=[syntax])
        self.assertEqual(jsonize_dict(data[syntax]), expected)

    def test_microdata_with_returning_node(self):
        body, tree, expected = self._testdata_html_and_tree(
            "schema.org",
            "CreativeWork.001.html",
            "CreativeWork_flat_with_node_id.001.json",
        )
        syntax = "microdata"
        data = extruct.extract(
            body, uniform=True, return_html_node=True, syntaxes=[syntax]
        )
        replace_node_ref_with_node_id(data[syntax])
        self.assertEqual(jsonize_dict(data[syntax]), expected[syntax])

        data = extruct.extract(
            tree, uniform=True, return_html_node=True, syntaxes=[syntax]
        )
        replace_node_ref_with_node_id(data[syntax])
        self.assertEqual(jsonize_dict(data[syntax]), expected[syntax])

    def test_microformat(self):
        body = get_testdata("misc", "microformat_test.html")
        expected = json.loads(
            get_testdata("misc", "microformat_flat_test.json").decode("UTF-8")
        )
        data = extruct.extract(body, uniform=True, syntaxes=["microformat"])
        self.assertEqual(jsonize_dict(data["microformat"]), expected)

    def _testdata_html_and_tree(self, root, path1, path2):
        body = get_testdata(root, path1)
        tree = parse_html(body, encoding="UTF-8")
        expected = json.loads(get_testdata(root, path2).decode("UTF-8"))
        return body, tree, expected

```

### `tests/test_extruct.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest

import pytest

import extruct
from extruct.utils import parse_html
from tests import get_testdata, jsonize_dict, replace_node_ref_with_node_id


class TestGeneric(unittest.TestCase):

    maxDiff = None

    def test_all(self):
        body = get_testdata("songkick", "elysianfields.html")
        expected = json.loads(
            get_testdata("songkick", "elysianfields.json").decode("UTF-8")
        )
        data = extruct.extract(
            body, base_url="http://www.songkick.com/artists/236156-elysian-fields"
        )

        self.assertEqual(jsonize_dict(data), expected)

    def test_rdfa_is_preserving_order(self):
        # See https://github.com/scrapinghub/extruct/issues/116
        body = get_testdata("songkick", "elysianfields_1.html")
        expected = json.loads(
            get_testdata("songkick", "elysianfields_1.json").decode("UTF-8")
        )
        data = extruct.extract(
            body, base_url="http://www.songkick.com/artists/236156-elysian-fields"
        )
        self.assertEqual(jsonize_dict(data)["rdfa"], expected["rdfa"])

    def test_microdata_custom_url(self):
        body, expected = self._microdata_custom_url("product_custom_url.json")
        tree = parse_html(body, encoding="UTF-8")
        data = extruct.extract(
            tree, base_url="http://some-example.com", syntaxes=["microdata"]
        )
        self.assertEqual(data, expected)

    def test_microdata_with_returning_node(self):
        body, expected = self._microdata_custom_url(
            "product_custom_url_and_node_id.json"
        )
        data = extruct.extract(
            body,
            base_url="http://some-example.com",
            syntaxes=["microdata"],
            return_html_node=True,
        )
        replace_node_ref_with_node_id(data)
        self.assertEqual(data, expected)

    def test_deprecated_url(self):
        body, expected = self._microdata_custom_url("product_custom_url.json")
        with pytest.warns(DeprecationWarning):
            data = extruct.extract(
                body, url="http://some-example.com", syntaxes=["microdata"]
            )
        self.assertEqual(data, expected)

    def test_extra_kwargs(self):
        body, _ = self._microdata_custom_url("product_custom_url.json")
        with self.assertRaises(TypeError):
            extruct.extract(body, foo="bar")  # type: ignore[call-arg]

    def _microdata_custom_url(self, test_file):
        body = get_testdata("schema.org", "product.html")
        expected = {
            "microdata": json.loads(
                get_testdata("schema.org", test_file).decode("UTF-8")
            )
        }
        return body, expected

    def test_errors(self):
        body = ""

        # raise exceptions
        with self.assertRaises(Exception):
            data = extruct.extract(body)

        # ignore exceptions
        data = extruct.extract(body, errors="ignore")
        assert data == {}

        # ignore exceptions
        data = extruct.extract(body, errors="log")
        assert data == {}

```

### `tests/test_jsonld.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest

from extruct.jsonld import JsonLdExtractor
from tests import get_testdata


class TestJsonLD(unittest.TestCase):
    def test_schemaorg_CreativeWork(self):
        self.assertJsonLdCorrect(folder="schema.org", page="CreativeWork.001")

    def test_songkick(self):
        self.assertJsonLdCorrect(
            folder="songkick",
            page="Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015",
        )

    def test_jsonld_empty_item(self):
        self.assertJsonLdCorrect(folder="songkick", page="jsonld_empty_item_test")

    def test_jsonld_with_comments(self):
        for page in ["JoinAction.001", "AllocateAction.001"]:
            self.assertJsonLdCorrect(folder="schema.org.invalid", page=page)

        for page in ["JoinAction.001", "AllocateAction.001"]:
            self.assertJsonLdCorrect(folder="custom.invalid", page=page)

    def test_jsonld_with_control_characters(self):
        self.assertJsonLdCorrect(
            folder="custom.invalid", page="JSONLD_with_control_characters"
        )

    def test_jsonld_with_control_characters_comment(self):
        self.assertJsonLdCorrect(
            folder="custom.invalid", page="JSONLD_with_control_characters_comment"
        )

    def test_jsonld_with_json_including_js_comment(self):
        self.assertJsonLdCorrect(folder="custom.invalid", page="JSONLD_with_JS_comment")

    def assertJsonLdCorrect(self, folder, page):
        body, expected = self._get_body_expected(folder, page)
        self._check_jsonld(body, expected)

    def _get_body_expected(self, folder, page):
        body = get_testdata(folder, "{}.html".format(page))
        expected = get_testdata(folder, "{}.jsonld".format(page))
        return body, json.loads(expected.decode("utf8"))

    def _check_jsonld(self, body, expected):
        jsonlde = JsonLdExtractor()
        data = jsonlde.extract(body)
        self.assertEqual(data, expected)

    def test_null(self):
        page = "null_ld_mock"
        body = get_testdata("misc", "{}.html".format(page))
        expected = json.loads(
            get_testdata("misc", "{}.jsonld".format(page)).decode("UTF-8")
        )

        jsonlde = JsonLdExtractor()
        data = jsonlde.extract(body)
        self.assertEqual(data, expected)

    def test_empty_jsonld_script(self):
        jsonlde = JsonLdExtractor()
        body = '<script type="application/ld+json">   \n\n  </script>'
        data = jsonlde.extract(body)
        self.assertEqual(data, [])

```

### `tests/test_microdata.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest

from extruct.w3cmicrodata import MicrodataExtractor
from tests import get_testdata


class TestMicrodata(unittest.TestCase):

    maxDiff = None

    def _test_schemaorg(self, schema, indexes=None):
        indexes = indexes or [1]
        for i in indexes:
            body = get_testdata("schema.org", f"{schema}.{i:03d}.html")
            expected = json.loads(
                get_testdata("schema.org", f"{schema}.{i:03d}.json").decode()
            )
            mde = MicrodataExtractor()
            data = mde.extract(body)
            self.assertEqual(data, expected)

    def test_schemaorg_CreativeWork(self):
        for i in [1]:
            body = get_testdata("schema.org", "CreativeWork.{:03d}.html".format(i))
            expected = json.loads(
                get_testdata("schema.org", "CreativeWork.{:03d}.json".format(i)).decode(
                    "UTF-8"
                )
            )

            mde = MicrodataExtractor()
            data = mde.extract(body)
            self.assertEqual(data, expected)

    def test_schemaorg_LocalBusiness(self):
        for i in [2, 3]:
            body = get_testdata("schema.org", "LocalBusiness.{:03d}.html".format(i))
            expected = json.loads(
                get_testdata(
                    "schema.org", "LocalBusiness.{:03d}.json".format(i)
                ).decode("UTF-8")
            )

            mde = MicrodataExtractor()
            data = mde.extract(body)
            self.assertEqual(data, expected)

    def test_schemaorg_MusicRecording(self):
        for i in [1]:
            body = get_testdata("schema.org", "MusicRecording.{:03d}.html".format(i))
            expected = json.loads(
                get_testdata(
                    "schema.org", "MusicRecording.{:03d}.json".format(i)
                ).decode("UTF-8")
            )

            mde = MicrodataExtractor()
            data = mde.extract(body)
            self.assertEqual(data, expected)

    def test_schemaorg_Event(self):
        for i in [1, 2, 3, 4, 8]:
            body = get_testdata("schema.org", "Event.{:03d}.html".format(i))
            expected = json.loads(
                get_testdata("schema.org", "Event.{:03d}.json".format(i)).decode(
                    "UTF-8"
                )
            )

            mde = MicrodataExtractor()
            data = mde.extract(body)

            self.assertEqual(data, expected)

    def test_schemaorg_SearchAction(self):
        self._test_schemaorg("SearchAction")

    def test_w3c_textContent_values(self):
        body = get_testdata("w3c", "microdata.4.2.strings.html")
        expected = json.loads(
            get_testdata("w3c", "microdata.4.2.strings.json").decode("UTF-8")
        )

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_w3c_textContent_values_unclean(self):
        body = get_testdata("w3c", "microdata.4.2.strings.unclean.html")
        expected = json.loads(
            get_testdata("w3c", "microdata.4.2.strings.unclean.json").decode("UTF-8")
        )

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_w3c_5_2(self):
        body = get_testdata("w3c", "microdata.5.2.html")
        expected = json.loads(get_testdata("w3c", "microdata.5.2.json").decode("UTF-8"))

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_w3c_5_3(self):
        body = get_testdata("w3c", "microdata.5.3.html")
        expected = json.loads(get_testdata("w3c", "microdata.5.3.json").decode("UTF-8"))

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_w3c_5_5(self):
        body = get_testdata("w3c", "microdata.5.5.html")
        expected = json.loads(get_testdata("w3c", "microdata.5.5.json").decode("UTF-8"))

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_w3c_7_1(self):
        body = get_testdata("w3c", "microdata.7.1.html")
        expected = json.loads(get_testdata("w3c", "microdata.7.1.json").decode("UTF-8"))

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body, "http://blog.example.com/progress-report")
        self.assertEqual(data, expected)

    def test_w3c_meter_element(self):
        body = get_testdata("w3c", "microdata.4.2.meter.html")
        expected = json.loads(
            get_testdata("w3c", "microdata.4.2.meter.json").decode("UTF-8")
        )

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_w3c_data_element(self):
        body = get_testdata("w3c", "microdata.4.2.data.html")
        expected = json.loads(
            get_testdata("w3c", "microdata.4.2.data.json").decode("UTF-8")
        )

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_w3c_object_element(self):
        body = get_testdata("w3c", "microdata.object.html")
        expected = json.loads(
            get_testdata("w3c", "microdata.object.json").decode("UTF-8")
        )

        mde = MicrodataExtractor(strict=True)
        data = mde.extract(body, "http://www.example.com/microdata/test")
        self.assertEqual(data, expected)


class TestMicrodataFlat(unittest.TestCase):

    maxDiff = None

    def test_w3c_5_2(self):
        body = get_testdata("w3c", "microdata.5.2.html")
        expected = json.loads(
            get_testdata("w3c", "microdata.5.2.flat.json").decode("UTF-8")
        )

        mde = MicrodataExtractor(nested=False, strict=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_w3c_7_1(self):
        body = get_testdata("w3c", "microdata.7.1.html")
        expected = json.loads(
            get_testdata("w3c", "microdata.7.1.flat.json").decode("UTF-8")
        )

        mde = MicrodataExtractor(nested=False, strict=True)
        data = mde.extract(body, "http://blog.example.com/progress-report")
        self.assertEqual(data, expected)


class TestMicrodataWithText(unittest.TestCase):

    maxDiff = None

    def test_w3c_5_2(self):
        body = get_testdata("w3c", "microdata.5.2.html")
        expected = json.loads(
            get_testdata("w3c", "microdata.5.2.withtext.json").decode("UTF-8")
        )

        mde = MicrodataExtractor(add_text_content=True)
        data = mde.extract(body)
        self.assertEqual(data, expected)


class TestUrlJoin(unittest.TestCase):

    maxDiff = None

    def test_join_none(self):
        body = get_testdata("schema.org", "product.html")
        expected = json.loads(
            get_testdata("schema.org", "product.json").decode("UTF-8")
        )

        mde = MicrodataExtractor()
        data = mde.extract(body)
        self.assertEqual(data, expected)

    def test_join_custom_url(self):
        body = get_testdata("schema.org", "product.html")
        expected = json.loads(
            get_testdata("schema.org", "product_custom_url.json").decode("UTF-8")
        )

        mde = MicrodataExtractor()
        data = mde.extract(body, base_url="http://some-example.com")
        self.assertEqual(data, expected)


class TestItemref(unittest.TestCase):

    maxDiff = None

    def test_join_none(self):
        body = get_testdata("schema.org", "product-ref.html")
        expected = json.loads(
            get_testdata("schema.org", "product-ref.json").decode("UTF-8")
        )

        mde = MicrodataExtractor()
        data = mde.extract(body)
        self.assertEqual(data, expected)


class TestMicrodataWithDescription(unittest.TestCase):
    maxDiff = None

    def test_if_punctuations_in_description_are_correctly_formatted(self):
        body = get_testdata("websites", "microdata-with-description.html")
        expected = json.loads(
            get_testdata("websites", "microdata-with-description.json").decode("UTF-8")
        )

        mde = MicrodataExtractor()
        data = mde.extract(body)

        self.assertEqual(data, expected)

```

### `tests/test_microformat.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest

from extruct.microformat import MicroformatExtractor
from tests import get_testdata, jsonize_dict


class TestMicroformat(unittest.TestCase):

    maxDiff = None

    def test_microformat(self):
        body = get_testdata("misc", "microformat_test.html")
        expected = json.loads(
            get_testdata("misc", "microformat_test.json").decode("UTF-8")
        )

        opengraphe = MicroformatExtractor()
        data = opengraphe.extract(body)
        self.assertEqual(jsonize_dict(data), expected)

```

### `tests/test_opengraph.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest

from extruct.opengraph import OpenGraphExtractor
from tests import get_testdata, jsonize_dict


class TestOpengraph(unittest.TestCase):

    maxDiff = None

    def _test_opengraph(self, name):
        body = get_testdata("misc", name + ".html")
        expected = json.loads(get_testdata("misc", name + ".json").decode("UTF-8"))

        opengraphe = OpenGraphExtractor()
        data = opengraphe.extract(body)
        self.assertEqual(jsonize_dict(data), expected)

    def test_opengraph(self):
        self._test_opengraph("opengraph_test")

    def test_opengraph_ns_product(self):
        self._test_opengraph("opengraph_ns_product_test")

```

### `tests/test_rdfa.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest
from pprint import pformat

from lxml.etree import XML, canonicalize

from extruct.rdfa import RDFaExtractor
from tests import get_testdata


def tupleize(d):
    if isinstance(d, list):
        return sorted(tupleize(e) for e in d)
    if isinstance(d, dict):
        # Workaround: canonicalize XML so that attribute re-ordering is ignored
        # See: https://github.com/scrapinghub/extruct/pull/161
        if d.get("@type") == "http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral":
            d["@value"] = canonicalize(XML(d["@value"]))
        return sorted((k, tupleize(v)) for k, v in d.items())
    return d


class TestRDFa(unittest.TestCase):

    maxDiff = None

    def assertJsonLDEqual(self, a, b, normalize_bnode_ids=True):
        sa = json.dumps(
            a, indent=2, separators=(",", ": "), sort_keys=True, ensure_ascii=True
        )
        sb = json.dumps(
            b, indent=2, separators=(",", ": "), sort_keys=True, ensure_ascii=True
        )
        if normalize_bnode_ids:
            sa = self.normalize_bnode_ids(sa)
            sb = self.normalize_bnode_ids(sb)
        self.assertEqual(tupleize(json.loads(sa)), tupleize(json.loads(sb)))

    def normalize_bnode_ids(self, jsld):
        import re

        bnode_ids = set(re.findall(r'"_:(\w+)"', jsld))
        for i, bnid in enumerate(bnode_ids, start=1):
            jsld = jsld.replace(bnid, "%06d" % i)
        return jsld

    def prettify(self, a, normalize_bnode_ids=True):
        output = json.dumps(
            a, indent=2, separators=(",", ": "), sort_keys=True, ensure_ascii=True
        )
        if normalize_bnode_ids:
            output = self.normalize_bnode_ids(output)
        return output

    def test_w3c_rdfalite(self):
        for i in [3, 4, 5]:
            fileprefix = "w3c.rdfalite.example{:03d}".format(i)
            body = get_testdata("w3crdfa", fileprefix + ".html")
            expected = json.loads(
                get_testdata("w3crdfa", fileprefix + ".expanded.json").decode("UTF-8")
            )

            rdfae = RDFaExtractor()
            data = rdfae.extract(body, base_url="http://www.example.com/index.html")
            self.assertJsonLDEqual(data, expected)

    def test_w3c_rdf11primer(self):
        for i in [14]:
            fileprefix = "w3c.rdf11primer.example{:03d}".format(i)
            body = get_testdata("w3crdfa", fileprefix + ".html")
            expected = json.loads(
                get_testdata("w3crdfa", fileprefix + ".expanded.json").decode("UTF-8")
            )

            rdfae = RDFaExtractor()
            data = rdfae.extract(body, base_url="http://www.example.com/index.html")
            self.assertJsonLDEqual(data, expected)

    def test_w3c_rdfaprimer(self):
        for i in [5, 6, 7, 8, 9, 10, 11, 15]:
            fileprefix = "w3c.rdfaprimer.example{:03d}".format(i)
            print(fileprefix)
            body = get_testdata("w3crdfa", fileprefix + ".html")
            expected = json.loads(
                get_testdata("w3crdfa", fileprefix + ".expanded.json").decode("UTF-8")
            )

            rdfae = RDFaExtractor()
            data = rdfae.extract(body, base_url="http://www.example.com/index.html")
            self.assertJsonLDEqual(data, expected)

            # This is for testing that the fix to issue 116 does not affect
            # severely rdfa output even in a presence of a bug in the code
            def mocked_fix_order(x, y, z):
                raise Exception()

            rdfae._fix_order = mocked_fix_order  # type: ignore[assignment]
            data = rdfae.extract(body, base_url="http://www.example.com/index.html")
            self.assertJsonLDEqual(data, expected)

    def test_wikipedia_xhtml_rdfa(self):
        fileprefix = "xhtml+rdfa"
        body = get_testdata("wikipedia", fileprefix + ".html")
        expected = json.loads(
            get_testdata("wikipedia", fileprefix + ".expanded.json").decode("UTF-8")
        )

        rdfae = RDFaExtractor()
        data = rdfae.extract(body, base_url="http://www.example.com/index.html")

        self.assertJsonLDEqual(data, expected)

    def test_wikipedia_xhtml_rdfa_no_prefix(self):
        body = get_testdata("misc", "Portfolio_Niels_Lubberman.html")
        expected = json.loads(
            get_testdata("misc", "Portfolio_Niels_Lubberman.json").decode("UTF-8")
        )

        rdfae = RDFaExtractor()
        data = rdfae.extract(body, base_url="http://nielslubberman.nl/drupal/")

        self.assertJsonLDEqual(data, expected)

    def test_expanded_opengraph_support(self):
        body = get_testdata("misc", "expanded_OG_support_test.html")
        expected = json.loads(
            get_testdata("misc", "expanded_OG_support_test.json").decode("UTF-8")
        )

        rdfae = RDFaExtractor()
        data = rdfae.extract(body, base_url="http://www.example.com/index.html")

        self.assertJsonLDEqual(data, expected)

```

### `tests/test_tool.py`

```py
# mypy: disallow_untyped_defs=False
import json
import unittest
import unittest.mock as mock

from requests.exceptions import HTTPError

from extruct.tool import main, metadata_from_url
from tests import get_testdata, jsonize_dict


class TestTool(unittest.TestCase):
    def setUp(self):
        self.expected = json.loads(
            get_testdata("songkick", "tovestyrke.json").decode("UTF-8")
        )
        self.url = "https://www.songkick.com/concerts/30166884-tove-styrke-at-hoxton-square-bar-and-kitchen"

    @mock.patch("extruct.tool.requests.get")
    def test_metadata_from_url_all_types(self, mock_get):
        expected = self.expected
        expected["url"] = self.url
        expected["status"] = "200 OK"
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = metadata_from_url(self.url)
        self.assertEqual(jsonize_dict(data), expected)

    @mock.patch("extruct.tool.requests.get")
    def test_metadata_from_url_jsonld_only(self, mock_get):
        expected = {
            "json-ld": self.expected["json-ld"],
            "url": self.url,
            "status": "200 OK",
        }
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = metadata_from_url(self.url, syntaxes=["json-ld"])
        self.assertEqual(jsonize_dict(data), expected)

    @mock.patch("extruct.tool.requests.get")
    def test_metadata_from_url_microdata_only(self, mock_get):
        expected = {
            "microdata": self.expected["microdata"],
            "url": self.url,
            "status": "200 OK",
        }
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = metadata_from_url(self.url, syntaxes=["microdata"])

        self.assertEqual(jsonize_dict(data), expected)

    @mock.patch("extruct.tool.requests.get")
    def test_metadata_from_url_rdfa_only(self, mock_get):
        expected = {
            "rdfa": self.expected["rdfa"],
            "url": self.url,
            "status": "200 OK",
        }
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = metadata_from_url(self.url, syntaxes=["rdfa"])
        self.assertEqual(jsonize_dict(data), expected)

    @mock.patch("extruct.tool.requests.get")
    def test_metadata_from_url_opengraph_only(self, mock_get):
        expected = {
            "opengraph": self.expected["opengraph"],
            "url": self.url,
            "status": "200 OK",
        }
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = metadata_from_url(self.url, syntaxes=["opengraph"])
        self.assertEqual(jsonize_dict(data), expected)

    @mock.patch("extruct.tool.requests.get")
    def test_metadata_from_url_microformat_only(self, mock_get):
        expected = {
            "microformat": self.expected["microformat"],
            "url": self.url,
            "status": "200 OK",
        }
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = metadata_from_url(self.url, syntaxes=["microformat"])
        self.assertEqual(jsonize_dict(data), expected)

    @mock.patch("extruct.tool.requests.get")
    def test_metadata_from_url_unauthorized_page(self, mock_get):
        url = "http://example.com/unauthorized"
        expected = {
            "url": url,
            "status": "401 Unauthorized",
        }
        mock_response = build_mock_response(
            url,
            reason="Unauthorized",
            status=401,
        )
        mock_get.return_value = mock_response
        mock_response.raise_for_status.side_effect = http_error

        data = metadata_from_url(url)
        self.assertEqual(data, expected)

    @mock.patch("extruct.tool.requests.get")
    def test_main_all(self, mock_get):
        expected = self.expected
        expected["url"] = self.url
        expected["status"] = "200 OK"
        expected = json.dumps(expected, indent=2, sort_keys=True)
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = main([self.url])
        self.assertEqual(data, expected)

    @mock.patch("extruct.tool.requests.get")
    def test_main_single_syntax(self, mock_get):
        data = {
            "opengraph": self.expected["opengraph"],
            "url": self.url,
            "status": "200 OK",
        }
        expected = json.dumps(data, indent=2, sort_keys=True)
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = main([self.url, "--syntax", "opengraph"])
        self.assertEqual(data, expected)

    @mock.patch("extruct.tool.requests.get")
    def test_main_multiple_syntaxes(self, mock_get):
        data = {
            "opengraph": self.expected["opengraph"],
            "microdata": self.expected["microdata"],
            "url": self.url,
            "status": "200 OK",
        }
        expected = json.dumps(data, indent=2, sort_keys=True)
        mock_response = build_mock_response(
            url=self.url,
            content=get_testdata("songkick", "tovestyrke.html"),
        )
        mock_get.return_value = mock_response

        data = main([self.url, "--syntax", "opengraph", "microdata"])
        self.assertEqual(data, expected)


def build_mock_response(url, encoding="utf-8", content="", reason="OK", status=200):
    mock_response = mock.Mock()
    mock_response.url = url
    mock_response.encoding = encoding
    mock_response.content = content
    mock_response.reason = reason
    mock_response.status_code = status
    return mock_response


def http_error():
    raise HTTPError()

```

### `tests/test_uniform.py`

```py
# mypy: disallow_untyped_defs=False
import unittest

import extruct
from extruct.uniform import _flatten, _uopengraph, flatten_dict, infer_context
from tests import get_testdata


class TestUniform(unittest.TestCase):

    maxDiff = None

    def test_uopengraph(self):
        expected = [
            {
                "@context": {
                    "og": "http://ogp.me/ns#",
                    "fb": "http://www.facebook.com/2008/fbml",
                    "concerts": "http://ogp.me/ns/fb/songkick-concerts#",
                },
                "fb:app_id": "308540029359",
                "og:site_name": "Songkick",
                "@type": "songkick-concerts:artist",
                "og:title": "Elysian Fields",
                "og:description": "Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017.",
                "og:url": "http://www.songkick.com/artists/236156-elysian-fields",
                "og:image": "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg",
            }
        ]
        body = get_testdata("songkick", "elysianfields.html")
        data = extruct.extract(body, syntaxes=["opengraph"], uniform=True)
        self.assertEqual(data["opengraph"], expected)

    def test_uopengraph_with_og_array(self):
        expected = [
            {
                "@context": {
                    "og": "http://ogp.me/ns#",
                    "fb": "http://www.facebook.com/2008/fbml",
                    "concerts": "http://ogp.me/ns/fb/songkick-concerts#",
                },
                "fb:app_id": "308540029359",
                "og:site_name": "Songkick",
                "@type": "songkick-concerts:artist",
                "og:title": "Elysian Fields",
                "og:description": "Buy tickets for an upcoming Elysian Fields concert near you. List of all Elysian Fields tickets and tour dates for 2017.",
                "og:url": "http://www.songkick.com/artists/236156-elysian-fields",
                "og:image": [
                    "http://images.sk-static.com/images/media/img/col4/20100330-103600-169450.jpg",
                    "http://images.sk-static.com/SECONDARY_IMAGE.jpg",
                ],
            }
        ]
        body = get_testdata("songkick", "elysianfields.html")
        data = extruct.extract(
            body, syntaxes=["opengraph"], uniform=True, with_og_array=True
        )
        self.assertEqual(data["opengraph"], expected)

    def test_uopengraph_duplicated_priorities(self):
        # Ensures that first seen property is kept when flattening
        data = _uopengraph(
            [
                {
                    "properties": [
                        ("prop_{}".format(k), "value_{}".format(v))
                        for k in range(5)
                        for v in range(5)
                    ],
                    "namespace": "namespace",
                }
            ]
        )
        for k in range(5):
            assert data[0]["prop_{}".format(k)] == "value_0"

        # Ensures that empty is not returned if a property contains any
        # non empty value
        data = _uopengraph(
            [
                {
                    "properties": [
                        ("prop_empty", " "),
                        ("prop_non_empty", " "),
                        ("prop_non_empty", "value!"),
                        ("prop_non_empty2", "value!"),
                        ("prop_non_empty2", " "),
                        ("prop_non_empty3", " "),
                        ("prop_non_empty3", "value!"),
                        ("prop_non_empty3", "other value"),
                    ],
                    "namespace": "namespace",
                }
            ]
        )
        assert data[0]["prop_empty"] == " "
        assert data[0]["prop_non_empty"] == "value!"
        assert data[0]["prop_non_empty2"] == "value!"
        assert data[0]["prop_non_empty3"] == "value!"

    def test_uopengraph_duplicated_with_og_array(self):
        # Ensures that first seen property is kept when flattening
        data = _uopengraph(
            [
                {
                    "properties": [
                        ("prop_{}".format(k), "value_{}".format(v))
                        for k in range(5)
                        for v in range(5)
                    ],
                    "namespace": "namespace",
                }
            ],
            with_og_array=True,
        )
        for k in range(5):
            assert data[0]["prop_{}".format(k)] == [
                "value_0",
                "value_1",
                "value_2",
                "value_3",
                "value_4",
            ]

        # Ensures that empty is not returned if a property contains any
        # non empty value
        data = _uopengraph(
            [
                {
                    "properties": [
                        ("prop_empty", " "),
                        ("prop_non_empty", " "),
                        ("prop_non_empty", "value!"),
                        ("prop_non_empty2", "value!"),
                        ("prop_non_empty2", " "),
                        ("prop_non_empty3", " "),
                        ("prop_non_empty3", "value!"),
                        ("prop_non_empty3", "other value"),
                    ],
                    "namespace": "namespace",
                }
            ],
            with_og_array=True,
        )
        assert data[0]["prop_empty"] == " "
        assert data[0]["prop_non_empty"] == "value!"
        assert data[0]["prop_non_empty2"] == "value!"
        assert data[0]["prop_non_empty3"] == ["value!", "other value"]

    def test_umicroformat(self):
        expected = [
            {
                "@context": "http://microformats.org/wiki/",
                "@type": ["h-hidden-phone", "h-hidden-tablet"],
                "name": [""],
            },
            {
                "@context": "http://microformats.org/wiki/",
                "@type": ["h-hidden-phone"],
                "children": [
                    {"@type": ["h-hidden-phone", "h-hidden-tablet"], "name": [""]},
                    {
                        "@type": ["h-hidden-phone"],
                        "name": [
                            "aJ Styles FastLane 2018 15 x "
                            "17 Framed Plaque w/ Ring "
                            "Canvas"
                        ],
                        "photo": [
                            {
                                "alt": "aJ Styles FastLane 2018 15 x 17 Framed Plaque w/ Ring Canvas",
                                "value": "/on/demandware.static/-/Sites-main/default/dwa3227ee6/images/small/CN1148.jpg",
                            }
                        ],
                    },
                ],
            },
            {
                "@context": "http://microformats.org/wiki/",
                "@type": ["h-entry"],
                "author": [
                    {
                        "@type": ["h-card"],
                        "name": ["W. Developer"],
                        "url": ["http://example.com"],
                        "value": "W. Developer",
                    }
                ],
                "content": [
                    {"html": "<p>Blah blah blah</p>", "value": "Blah blah blah"}
                ],
                "name": ["Microformats are amazing"],
                "published": ["2013-06-13 12:00:00"],
                "summary": ["In which I extoll the virtues of using " "microformats."],
            },
        ]
        body = get_testdata("misc", "microformat_test.html")
        data = extruct.extract(body, syntaxes=["microformat"], uniform=True)
        self.assertEqual(data["microformat"], expected)

    def test_umicrodata(self):
        expected = [
            {
                "@context": "http://schema.org",
                "@type": "Product",
                "brand": "ACME",
                "name": "Executive Anvil",
                "image": "anvil_executive.jpg",
                "description": "Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.",
                "mpn": "925872",
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.4",
                    "reviewCount": "89",
                },
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "USD",
                    "price": "119.99",
                    "priceValidUntil": "2020-11-05",
                    "seller": {"@type": "Organization", "name": "Executive Objects"},
                    "itemCondition": "http://schema.org/UsedCondition",
                    "availability": "http://schema.org/InStock",
                },
            }
        ]
        body = get_testdata("misc", "product_microdata.html")
        data = extruct.extract(body, syntaxes=["microdata"], uniform=True)
        self.assertEqual(data["microdata"], expected)

    def test_udublincore(self):
        expected = [
            {
                "elements": [
                    {
                        "name": "DC.title",
                        "lang": "en",
                        "content": "Expressing Dublin Core\nin HTML/XHTML meta and link elements",
                        "URI": "http://purl.org/dc/elements/1.1/title",
                    },
                    {
                        "name": "DC.creator",
                        "content": "Andy Powell, UKOLN, University of Bath",
                        "URI": "http://purl.org/dc/elements/1.1/creator",
                    },
                    {
                        "name": "DC.identifier",
                        "scheme": "DCTERMS.URI",
                        "content": "http://dublincore.org/documents/dcq-html/",
                        "URI": "http://purl.org/dc/elements/1.1/identifier",
                    },
                    {
                        "name": "DC.format",
                        "scheme": "DCTERMS.IMT",
                        "content": "text/html",
                        "URI": "http://purl.org/dc/elements/1.1/format",
                    },
                ],
                "terms": [
                    {
                        "name": "DCTERMS.issued",
                        "scheme": "DCTERMS.W3CDTF",
                        "content": "2003-11-01",
                        "URI": "http://purl.org/dc/terms/issued",
                    },
                    {
                        "name": "DCTERMS.abstract",
                        "content": "This document describes how\nqualified Dublin Core metadata can be encoded\nin HTML/XHTML <meta> elements",
                        "URI": "http://purl.org/dc/terms/abstract",
                    },
                    {
                        "name": "DC.Date.modified",
                        "content": "2001-07-18",
                        "URI": "http://purl.org/dc/terms/modified",
                    },
                    {
                        "name": "DCTERMS.modified",
                        "content": "2001-07-18",
                        "URI": "http://purl.org/dc/terms/modified",
                    },
                    {
                        "rel": "DCTERMS.replaces",
                        "hreflang": "en",
                        "href": "http://dublincore.org/documents/2000/08/15/dcq-html/",
                        "URI": "http://purl.org/dc/terms/replaces",
                    },
                ],
                "@context": {
                    "DC": "http://purl.org/dc/elements/1.1/",
                    "DCTERMS": "http://purl.org/dc/terms/",
                },
                "@type": "Text",
            }
        ]
        body = get_testdata("misc", "dublincore_test.html")
        data = extruct.extract(body, syntaxes=["dublincore"], uniform=True)
        self.assertEqual(data["dublincore"], expected)

    def test_infer_context(self):
        context = "http://schema.org/UsedCondition"
        self.assertEqual(infer_context(context), ("http://schema.org", "UsedCondition"))

        context = "http://ogp.me/ns#description"
        self.assertEqual(infer_context(context), ("http://ogp.me/ns", "description"))

        context = "http://ogp.me/ns/fb#app_id"
        self.assertEqual(infer_context(context), ("http://ogp.me/ns/fb", "app_id"))

    def test_flatten_dict(self):
        d = {
            "type": "SPANISH INQUISITION",
            "properties": {
                "chief_weapon": "surprise",
                "extra_weapon": "fear",
                "another_one": "ruthless efficiency",
            },
        }
        expected = {
            "@type": "SPANISH INQUISITION",
            "@context": "http://schema.org",
            "chief_weapon": "surprise",
            "extra_weapon": "fear",
            "another_one": "ruthless efficiency",
        }
        self.assertEqual(
            flatten_dict(d, schema_context="http://schema.org", add_context=True),
            expected,
        )

    def test_flatten(self):
        d = {
            "children": [
                {
                    "properties": {"name": [""]},
                    "type": ["h-hidden-tablet", "h-hidden-phone"],
                },
                {
                    "properties": {
                        "name": [
                            "aJ Styles "
                            "FastLane 2018 "
                            "15 x 17 Framed "
                            "Plaque w/ Ring "
                            "Canvas"
                        ],
                        "photo": ["path.jpg"],
                    },
                    "type": ["h-hidden-phone"],
                },
            ],
            "properties": {"name": [""]},
            "type": ["h-hidden-phone"],
        }
        expected = {
            "children": [
                {"name": [""], "@type": ["h-hidden-tablet", "h-hidden-phone"]},
                {
                    "name": [
                        "aJ Styles "
                        "FastLane 2018 "
                        "15 x 17 Framed "
                        "Plaque w/ Ring "
                        "Canvas"
                    ],
                    "photo": ["path.jpg"],
                    "@type": ["h-hidden-phone"],
                },
            ],
            "name": [""],
            "@type": ["h-hidden-phone"],
        }
        self.assertEqual(_flatten(d, schema_context="http://schema.org"), expected)

```

### `tox.ini`

```ini
[tox]
envlist = py38, py39, py310, py311, py312


[testenv]
deps =
    -rrequirements-dev.txt
commands =
    py.test --cov-report=term --cov-report= --cov-report=xml --cov=extruct {posargs:extruct tests}

[testenv:py39]
commands =
    py.test --cov-report=term --cov-report= --cov-report=xml --cov=extruct {posargs:extruct tests}
    python -m readme_renderer README.rst -o /tmp/README.html

[testenv:linters]
deps = -rrequirements-dev.txt
commands = pre-commit run --all-files --show-diff-on-failure

[testenv:twinecheck]
deps =
    twine==5.1.0
    build==1.2.1
commands =
    python -m build --sdist
    twine check dist/*

```
