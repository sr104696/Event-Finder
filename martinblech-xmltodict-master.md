# martinblech/xmltodict@master

- Files included: 22
- Files skipped: 0
- Total size: 108.3 KB
- Estimated tokens: ~27,696

## Directory Structure

```
├── .github
│   ├── workflows
│   │   ├── commitlint.yml
│   │   ├── publish.yml
│   │   ├── release-please.yml
│   │   └── test.yml
│   └── FUNDING.yml
├── tests
│   ├── __init__.py
│   ├── test_dicttoxml.py
│   └── test_xmltodict.py
├── .gitignore
├── .pre-commit-config.yaml
├── .release-please-manifest.json
├── AGENTS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── release-please-config.json
├── SECURITY.md
├── tox.ini
└── xmltodict.py
```

## Code Digest

### `.github/FUNDING.yml`

```yml
# These are supported funding model platforms

github: [martinblech]

```

### `.github/workflows/commitlint.yml`

```yml
name: Lint Commit Messages
on: [pull_request, push]

permissions:
  contents: read
  pull-requests: read

jobs:
  commitlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: wagoid/commitlint-github-action@v6

```

### `.github/workflows/publish.yml`

```yml
name: Publish to PyPI

on:
  release:
    types: [published]
  workflow_dispatch: {}

permissions:
  id-token: write
  contents: write

jobs:
  build-and-publish:
    name: Build and publish python package
    runs-on: ubuntu-latest
    environment:
      name: pypi-publish
      url: https://pypi.org/p/xmltodict
    steps:
      - uses: actions/checkout@v5

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.x'

      - name: Install build backend
        run: |
          python -m pip install --upgrade pip
          python -m pip install build

      - name: Build sdist and wheel
        run: |
          python -m build --sdist --wheel --outdir dist/

      - name: Upload sdist and wheel as release assets
        uses: softprops/action-gh-release@v2
        with:
          files: dist/*

      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          print-hash: true

```

### `.github/workflows/release-please.yml`

```yml
name: release-please

on:
  push:
    branches:
      - main
      - master

permissions:
  contents: write
  issues: write
  pull-requests: write

jobs:
  release-please:
    runs-on: ubuntu-latest
    steps:
      - uses: googleapis/release-please-action@v4
        with:
          token: ${{ secrets.RELEASE_PLEASE_PAT }}
          config-file: release-please-config.json
          manifest-file: .release-please-manifest.json

```

### `.github/workflows/test.yml`

```yml
name: Tox Test

on:
  - push
  - pull_request

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12', '3.13', '3.14', '3.14t', pypy3.10, pypy3.11]

    steps:
    - uses: actions/checkout@v6
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v6
      with:
        python-version: ${{ matrix.python-version }}
        allow-prereleases: true
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install tox tox-gh-actions
    - name: Test with tox
      run: tox

  build-dist:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v6
    - name: Set up Python 3.x
      uses: actions/setup-python@v6
      with:
        python-version: '3.x'
    - name: Build and check distributions
      run: |
        python -m pip install --upgrade pip
        python -m pip install build twine
        python -m build --sdist --wheel --outdir dist/
        python -m twine check dist/*

```

### `.gitignore`

```gitignore
*.py[cod]

# C extensions
*.so

# Packages
*.egg
*.egg-info
dist
build
eggs
parts
bin
var
sdist
develop-eggs
.installed.cfg
lib
lib64

# Installer logs
pip-log.txt

# Unit test / coverage reports
.coverage
.tox
nosetests.xml

#Translations
*.mo

#Mr Developer
.mr.developer.cfg

#setuptools MANIFEST
MANIFEST

```

### `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v4.9.0
    hooks:
      - id: commitizen
        additional_dependencies:
          - deprecated

```

### `.release-please-manifest.json`

```json
{
  ".": "1.0.4"
}

```

### `AGENTS.md`

```md
# AGENTS.md — Working Context for `xmltodict`

This page gives coding agents only what they need to contribute safely and quickly. For full API details, examples, and edge‑case discussion, defer to the README.

---

## 1) What `xmltodict` is
A single‑file Python library that converts **XML ↔ dict**, making XML feel like JSON for most practical use cases. It aims for clarity and convenience over perfect round‑tripping of every XML nuance.

---

## 2) Core surface area
- **Module**: `xmltodict.py` (single file)
- **Primary functions**:
  - `parse(xml_input, **kwargs)` → `dict`
  - `unparse(input_dict, **kwargs)` → `str`/bytes
- **Options agents commonly need**:
  - Parsing: `process_namespaces`, `namespaces`, `force_list`, `force_cdata`, `item_depth` + `item_callback` (streaming), `process_comments`, `attr_prefix` (default `@`), `cdata_key` (default `#text`), `strip_whitespace`, `disable_entities` (default **True**)
  - Unparsing: `pretty`, `short_empty_elements`, `expand_iter`, `full_document`, `encoding`

---

## 3) Streaming guidance
For large XML, use **streaming** with `item_depth` + `item_callback`. Expect constant memory relative to item size, not whole‑document size. Keep callbacks fast and side‑effect‑free.

---

## 4) Security posture
- **Entity expansion is disabled by default** (`disable_entities=True`).
- **Input validation**: element/attribute names are validated and reject illegal characters (e.g., `<`, `>`, `/`, quotes, `=`, whitespace) and disallowed starts (e.g., `?`, `!`).
- **Reminder for agents**: do not relax security defaults unless tests cover your change.

---

## 5) Known caveats / non‑goals
- Exact **mixed content** ordering and **attribute order** are not guaranteed to be preserved.
- Comment handling is best‑effort; don’t rely on multiple top‑level comments round‑tripping in exact order.
- The project prioritizes common XML→dict workflows over exhaustive XML edge‑cases.

---

## 6) Project conventions (how to contribute changes)
- **Python**: 3.9+.
- **Commits**: Conventional Commits (`type(scope?): subject`).
- **Tests**: `pytest` (usually via `tox`). All new behavior must have tests; include edge cases and failure paths.
- **CI/CD**: GitHub Actions runs tox; releases are automated (Release Please + GitHub Release → PyPI).
- **Types**: Optional stub package `types-xmltodict` is available for type checkers.

---

## 7) Minimal repo map
```
xmltodict/
├── xmltodict.py          # Library (single file)
├── tests/                # Test suite
│   ├── test_xmltodict.py # XML→dict
│   └── test_dicttoxml.py # dict→XML
├── .github/workflows/    # CI/release automation
├── pyproject.toml        # Packaging/config (or equivalent)
└── README.md             # Authoritative API + examples
```

---

## 8) Agent checklists
### Adding/changing behavior
- [ ] Write or update tests first (success + failure cases).
- [ ] Preserve security defaults; document any opt‑outs.
- [ ] Keep kwargs names/backwards compatibility unless a major bump is justified.
- [ ] Update README only if public API changes.

### Performance changes
- [ ] Benchmark on representative large XML (streaming when applicable).
- [ ] Avoid unbounded growth in intermediate structures.

### Release readiness
- [ ] All tests pass locally and in CI across supported Pythons.
- [ ] Conventional commit message(s) are in place for changelog generation.

---

## 9) Pointers
- **README**: canonical API and usage.
- **Issues/PRs**: prior discussions on namespaces, streaming, and comment handling.
- **Type Stubs**: `types-xmltodict` on PyPI.

```

### `CHANGELOG.md`

```md
# Changelog

## [1.0.4](https://github.com/martinblech/xmltodict/compare/v1.0.3...v1.0.4) (2026-02-22)


### Bug Fixes

* **unparse:** add bytes_errors policy and handle bytes scalars consistently ([ed70434](https://github.com/martinblech/xmltodict/commit/ed704344226ed6451f6735811c695fb5004df44d))

## [1.0.3](https://github.com/martinblech/xmltodict/compare/v1.0.2...v1.0.3) (2026-02-15)


### Bug Fixes

* **unparse:** serialize None text/attrs as empty values (fixes [#401](https://github.com/martinblech/xmltodict/issues/401)) ([aa16511](https://github.com/martinblech/xmltodict/commit/aa165113bef2b3a1a822209863343b9dc9ffe43a))


### Documentation

* **readme:** fix Fedora and Arch package links ([fd6a73b](https://github.com/martinblech/xmltodict/commit/fd6a73bf606c3932bcc82bf559a70867a1dd75cd))

## [1.0.2](https://github.com/martinblech/xmltodict/compare/v1.0.1...v1.0.2) (2025-09-17)


### Bug Fixes

* allow DOCTYPE with disable_entities=True (default) ([25b61a4](https://github.com/martinblech/xmltodict/commit/25b61a41f580cfc211df07c5fbbf603bd8eb5a5f))

## [1.0.1](https://github.com/martinblech/xmltodict/compare/v1.0.0...v1.0.1) (2025-09-17)


### Bug Fixes

* fail closed when entities disabled ([c986d2d](https://github.com/martinblech/xmltodict/commit/c986d2d37a93d45fcc059b09063d9d9c45a655ec))
* validate XML comments ([3d4d2d3](https://github.com/martinblech/xmltodict/commit/3d4d2d3a4cd0f68d1211dba549010261fa87b969))


### Documentation

* add SECURITY.md ([6413023](https://github.com/martinblech/xmltodict/commit/64130233c8fea272a5f82f2f585e1593523ec1b1))
* clarify behavior for empty lists ([2025b5c](https://github.com/martinblech/xmltodict/commit/2025b5cb5e64fc9c4d54b8644187a0a193bdd0ed))
* clarify process_comments docs ([6b464fc](https://github.com/martinblech/xmltodict/commit/6b464fce284a93dbb292f3d063c9f310a478a014))
* clarify strip whitespace comment behavior ([b3e2203](https://github.com/martinblech/xmltodict/commit/b3e22032d21cc387d6cecf3930116e8fdc3151cf))
* create AGENTS.md for coding agents ([0da66ee](https://github.com/martinblech/xmltodict/commit/0da66ee797ced7479312aecef92c6a25e235007c))
* replace travis with actions badge ([2576b94](https://github.com/martinblech/xmltodict/commit/2576b94c918fbd154489a95dbbb3feda8bd3cbd8))
* update CONTRIBUTING.md ([db39180](https://github.com/martinblech/xmltodict/commit/db3918057cf125af989a1263d52df8df5ef8c642))

## [1.0.0](https://github.com/martinblech/xmltodict/compare/v0.15.1...v1.0.0) (2025-09-12)


### ⚠ BREAKING CHANGES

* modernize for Python 3.9+; drop legacy compat paths

### Features

* **unparse:** add limited XML comment round-trip; unify `_emit` behavior ([e43537e](https://github.com/martinblech/xmltodict/commit/e43537eee61c20ef50f0e4242eb9223de7a6aefd))
* **unparse:** add selective `force_cdata` support (bool/tuple/callable) ([a497fed](https://github.com/martinblech/xmltodict/commit/a497fedb7d6103d68af155543ac3337a73778b19)), closes [#375](https://github.com/martinblech/xmltodict/issues/375)


### Bug Fixes

* **namespaces:** attach `[@xmlns](https://github.com/xmlns)` to declaring element when process_namespaces=True ([f0322e5](https://github.com/martinblech/xmltodict/commit/f0322e578184421693434902547f330f4f0a44c3)), closes [#163](https://github.com/martinblech/xmltodict/issues/163)
* **streaming:** avoid parent accumulation at item_depth; add regression tests ([220240c](https://github.com/martinblech/xmltodict/commit/220240c5eb2d12b75adf26cc84ec9c803ce8bb2b))
* **unparse:** handle non-string `#text` with attributes; unify value conversion ([927a025](https://github.com/martinblech/xmltodict/commit/927a025ae8a62cbb542d5caff38b29161a2096fa)), closes [#366](https://github.com/martinblech/xmltodict/issues/366)
* **unparse:** skip empty lists to keep pretty/compact outputs consistent ([ab4c86f](https://github.com/martinblech/xmltodict/commit/ab4c86fed24dc8ef0e932a524edfb01c6453ecf6))


### Reverts

* remove initial Release Drafter config ([c0b74ed](https://github.com/martinblech/xmltodict/commit/c0b74ed58f933bffd160c60a58620f672710ff7c))


### Documentation

* **readme:** add API reference for parse()/unparse() kwargs ([e5039ad](https://github.com/martinblech/xmltodict/commit/e5039ad3f5159cc45ac1d52c4aa901ca50d4c722))
* **readme:** mention types-xmltodict stub package ([58ec03e](https://github.com/martinblech/xmltodict/commit/58ec03e6d94f17ed359742d9ce2f99e796669694))


### Code Refactoring

* modernize for Python 3.9+; drop legacy compat paths ([7364427](https://github.com/martinblech/xmltodict/commit/7364427c86c62f55ad4c2dce96df6761da69c354))

## v0.15.1
* Security: Further harden XML injection prevention during unparse (follow-up to
  v0.15.0). In addition to '<'/'>' rejection, now also reject element and
  attribute names (including `@xmlns` prefixes) that:
  - start with '?' or '!'
  - contain '/' or any whitespace
  - contain quotes (' or ") or '='
  - are non-strings (names must be `str`; no coercion)

## v0.15.0
* Security: Prevent XML injection (CVE-2025-9375) by rejecting '<'/'>' in
  element and attribute names (including `@xmlns` prefixes) during unparse.
  This limits validation to avoiding tag-context escapes; attribute values
  continue to be escaped by the SAX `XMLGenerator`.
  Advisory: https://fluidattacks.com/advisories/mono

## v0.14.2
* Revert "Ensure significant whitespace is not trimmed"
  * This changed was backwards incompatible and caused downstream issues.

## v0.14.1
* Drop support for Python older than 3.6
* Additional ruff/Pyflakes/codespell fixes.
  * Thanks @DimitriPapadopoulos!

## v0.14.0

* Drop old Python 2 support leftover code and apply several RUFF code health fixes.
  * Thanks, @DimitriPapadopoulos!
* Add Python 3.11, 3.12 and 3.13 support and tests.
  * Thanks, @angvp!
* Tests in gh-action.
  * Thanks, @almaz.kun!
* Remove defusedexpat import.
  * Thanks, @hanno!
* Replace deprecated BadZipfile with BadZipFile.
  * Thanks, @hugovk!
* Support indent using integer format, enable `python -m unittest tests/*.py`.
  * Thanks, @hiiwave!
* Ensure significant whitespace is not trimmed
  * Thanks, @trey.franklin!
* added conda installation command
  * Thanks, @sugatoray!
* fix attributes not appearing in streaming mode
  * Thanks, @timnguyen001!
* Fix Travis CI status badge URL
* Update push_release.sh to use twine.

## v0.13.0

* Add install info to readme for openSUSE. (#205)
  * Thanks, @smarlowucf!
* Support defaultdict for namespace mapping (#211)
  * Thanks, @nathanalderson!
* parse(generator) is now possible (#212)
  * Thanks, @xandey!
* Processing comments on parsing from xml to dict (connected to #109) (#221)
  * Thanks, @svetazol!
* Add expand_iter kw to unparse to expand iterables (#213)
  * Thanks, @claweyenuk!
* Fixed some typos
  * Thanks, @timgates42 and @kianmeng!
* Add support for python3.8
  * Thanks, @t0b3!
* Drop Jython/Python 2 and add Python 3.9/3.10.
* Drop OrderedDict in Python >= 3.7
* Do not use len() to determine if a sequence is empty
  * Thanks, @DimitriPapadopoulos!
* Add more namespace attribute tests
  * Thanks, @leogregianin!
* Fix encoding issue in setup.py
  * Thanks, @rjarry!

## v0.12.0

* Allow force_commits=True for getting all keys as lists (#204)
* README.md: fix useless uses of cat (#200)
* Add FreeBSD install instructions (#199)
* Fix and simplify travis config (#192)
* Add support for Python 3.7 (#189)
* Drop support for EOL Python (#191)
* Use Markdown long_description on PyPI (#190)
* correct spelling mistake (#165)
* correctly unparse booleans (#180)
* Updates README.md with svg badge

## v0.11.0

* Determine fileness by checking for `read` attr
  * Thanks, @jwodder!
* Add support for Python 3.6.
  * Thanks, @cclauss!
* Release as a universal wheel.
  * Thanks, @adamchainz!
* Updated docs examples to use print function.
  * Thanks, @cdeil!
* unparse: pass short_empty_elements to XMLGenerator
  * Thanks, @zhanglei002!
* Added namespace support when unparsing.
  * Thanks, @imiric!

## v0.10.2

* Fixed defusedexpat expat import.
  * Thanks, @fiebiga!

## v0.10.1

* Use defusedexpat if available.
* Allow non-string attributes in unparse.
* Add postprocessor support for attributes.
* Make command line interface Python 3-compatible.

## v0.10.0

* Add force_list feature.
  * Thanks, @guewen and @jonlooney!
* Add support for Python 3.4 and 3.5.
* Performance optimization: use list instead of string for CDATA.
  * Thanks, @bharel!
* Include Arch Linux package instructions in README.
  * Thanks, @felixonmars!
* Improved documentation.
  * Thanks, @ubershmekel!
* Allow any iterable in unparse, not just lists.
  * Thanks, @bzamecnik!
* Bugfix: Process namespaces in attributes too.
* Better testing under Python 2.6.
  * Thanks, @TyMaszWeb!

## v0.9.2

* Fix multiroot check for list values (edge case reported by @JKillian)

## v0.9.1

* Only check single root when full_document=True (Thanks @JKillian!)

## v0.9.0

* Added CHANGELOG.md
* Avoid ternary operator in call to ParserCreate().
* Adding Python 3.4 to Tox test environment.
* Added full_document flag to unparse (default=True).

## v0.8.7

* Merge pull request #56 from HansWeltar/master
* Improve performance for large files
* Updated README unparse example with pretty=True.

## v0.8.6

* Fixed extra newlines in pretty print mode.
* Fixed all flake8 warnings.

## v0.8.5

* Added Tox config.
* Let expat figure out the doc encoding.

## v0.8.4

* Fixed Jython TravisCI build.
* Moved nose and coverage to tests_require.
* Dropping python 2.5 from travis.yml.

## v0.8.3

* Use system setuptools if available.

## v0.8.2

* Switch to latest setuptools.

## v0.8.1

* Include distribute_setup.py in MANIFEST.in
* Updated package classifiers (python versions, PyPy, Jython).

## v0.8.0

* Merge pull request #40 from martinblech/jython-support
* Adding Jython support.
* Fix streaming example callback (must return True)

## v0.7.0

* Merge pull request #35 from martinblech/namespace-support
* Adding support for XML namespaces.
* Merge pull request #33 from bgilb/master
* fixes whitespace style
* changes module import syntax and assertRaises
* adds unittest assertRaises

## v0.6.0

* Merge pull request #31 from martinblech/document-unparse
* Adding documentation for unparse()
* Merge pull request #30 from martinblech/prettyprint
* Adding support for pretty print in unparse()

## v0.5.1

* Merge pull request #29 from dusual/master
* ordereddict import for less 2.6 if available

## v0.5.0

* Allow using alternate versions of `expat`.
* Added shameless link to GitTip.
* Merge pull request #20 from kevbo/master
* Adds unparse example to README

## v0.4.6

* fix try/catch block for pypi (throws AttributeError instead of TypeError)
* prevent encoding an already encoded string
* removed unnecessary try/catch for xml_input.encode(). check if file or string, EAFP style. (thanks @turicas)

## v0.4.5

* test with python 3.3 too
* avoid u'unicode' syntax (fails in python 3.2)
* handle unicode input strings properly
* add strip_whitespace option (default=True)
* Merge pull request #16 from slestak/master
* fix unittest
* working with upstream to improve #15
* remove pythonpath tweaks, change loc of #15 patch
* upstream  #15

## v0.4.4

* test attribute order roundtrip only if OrderedDict is available (python >= 2.7)
* Merge branch 'master' of github.com:martinblech/xmltodict
* preserve xml attribute order (fixes #13)

## v0.4.3

* fix #12: postprocess cdata items too
* added info about official fedora package

## v0.4.2

* Merge pull request #11 from ralphbean/master
* Include README, LICENSE, and tests in the distributed tarball.

## v0.4.1

* take all characters (no need to strip and filter)
* fixed CLI (marshal only takes dict, not OrderedDict)
* ignore MANIFEST

## v0.4

* #8 preprocessing callback in unparse()

## v0.3

* implemented postprocessor callback (#6)
* update readme with install instructions

## v0.2

* link to travis-ci build status
* more complete info in setup.py (for uploading to PyPi)
* coverage annotations for tricky py3k workarounds
* py3k compatibility
* removed unused __future__ print_function
* using io.StringIO on py3k
* removed unnecessary exception catching
* initial travis-ci configuration
* made _emit function private
* unparse functionality
* added tests
* updated (c) notice to acknowledge individual contributors
* added license information
* fixed README
* removed temp build directory and added a .gitignore to avoid that happening again
* Merge pull request #1 from scottscott/master
* Added setup script to make xmltodict a Python module.
* fixed bad handling of cdata in semistructured xml, changed _CDATA_ to #text as default
* added attr_prefix, cdata_key and force_cdata parameters
* links in README
* links in README
* improved README
* initial commit

```

### `CONTRIBUTING.md`

```md
# Contributing

We welcome contributions to this project! Please follow these guidelines to ensure a smooth and effective contribution process.

## How to Contribute

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes.
- Ensure that the tests pass.
- Submit a pull request with a clear description of your changes.

## Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for our commit messages.
This allows for automated changelog generation and release management.

The commit message format is:
`type(scope?): subject`

The `type` must be one of the following:
- `build`: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- `chore`: Other changes that don't modify src or test files
- `ci`: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- `docs`: Documentation only changes
- `feat`: A new feature
- `fix`: A bug fix
- `perf`: A code change that improves performance
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `revert`: Reverts a previous commit
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `test`: Adding missing tests or correcting existing tests

The `scope` is optional and can be used to specify the part of the codebase that is affected by the change.
The `subject` contains a succinct description of the change:
- Use the imperative, present tense: "add" not "added" nor "adds".
- Don't capitalize the first letter.
- No dot (.) at the end.
- The subject line must not exceed 50 characters.

The `body` of the commit message is optional and should be used to provide additional context.
- The body should be wrapped at 72 characters.

```

### `LICENSE`

```
Copyright (C) 2012 Martin Blech and individual contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

### `MANIFEST.in`

```in
recursive-include tests *

```

### `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=77.0.3"]
build-backend = "setuptools.build_meta"

[project]
name = "xmltodict"
version = "1.0.4"
description = "Makes working with XML feel like you are working with JSON"
readme = "README.md"
requires-python = ">=3.9"
license = "MIT"
license-files = ["LICENSE"]
authors = [{ name = "Martin Blech" }]
classifiers = [
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Text Processing :: Markup :: XML",
]

[project.optional-dependencies]
test = [
    "pytest",
    "pytest-cov",
]

[project.urls]
Homepage = "https://github.com/martinblech/xmltodict"

[tool.setuptools]
py-modules = ["xmltodict"]

```

### `README.md`

```md
# xmltodict

`xmltodict` is a Python module that makes working with XML feel like you are working with [JSON](http://docs.python.org/library/json.html), as in this ["spec"](http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html):

[![Tests](https://github.com/martinblech/xmltodict/actions/workflows/test.yml/badge.svg)](https://github.com/martinblech/xmltodict/actions/workflows/test.yml)

```python
>>> print(json.dumps(xmltodict.parse("""
...  <mydocument has="an attribute">
...    <and>
...      <many>elements</many>
...      <many>more elements</many>
...    </and>
...    <plus a="complex">
...      element as well
...    </plus>
...  </mydocument>
...  """), indent=4))
{
    "mydocument": {
        "@has": "an attribute",
        "and": {
            "many": [
                "elements",
                "more elements"
            ]
        },
        "plus": {
            "@a": "complex",
            "#text": "element as well"
        }
    }
}
```

## Namespace support

By default, `xmltodict` does no XML namespace processing (it just treats namespace declarations as regular node attributes), but passing `process_namespaces=True` will make it expand namespaces for you:

```python
>>> xml = """
... <root xmlns="http://defaultns.com/"
...       xmlns:a="http://a.com/"
...       xmlns:b="http://b.com/">
...   <x>1</x>
...   <a:y>2</a:y>
...   <b:z>3</b:z>
... </root>
... """
>>> xmltodict.parse(xml, process_namespaces=True) == {
...     'http://defaultns.com/:root': {
...         'http://defaultns.com/:x': '1',
...         'http://a.com/:y': '2',
...         'http://b.com/:z': '3',
...     }
... }
True
```

It also lets you collapse certain namespaces to shorthand prefixes, or skip them altogether:

```python
>>> namespaces = {
...     'http://defaultns.com/': None, # skip this namespace
...     'http://a.com/': 'ns_a', # collapse "http://a.com/" -> "ns_a"
... }
>>> xmltodict.parse(xml, process_namespaces=True, namespaces=namespaces) == {
...     'root': {
...         'x': '1',
...         'ns_a:y': '2',
...         'http://b.com/:z': '3',
...     },
... }
True
```

## Streaming mode

`xmltodict` is very fast ([Expat](http://docs.python.org/library/pyexpat.html)-based) and has a streaming mode with a small memory footprint, suitable for big XML dumps like [Discogs](http://discogs.com/data/) or [Wikipedia](http://dumps.wikimedia.org/):

```python
>>> def handle_artist(_, artist):
...     print(artist['name'])
...     return True
>>>
>>> xmltodict.parse(GzipFile('discogs_artists.xml.gz'),
...     item_depth=2, item_callback=handle_artist)
A Perfect Circle
Fantômas
King Crimson
Chris Potter
...
```

It can also be used from the command line to pipe objects to a script like this:

```python
import sys, marshal
while True:
    _, article = marshal.load(sys.stdin)
    print(article['title'])
```

```sh
$ bunzip2 enwiki-pages-articles.xml.bz2 | xmltodict.py 2 | myscript.py
AccessibleComputing
Anarchism
AfghanistanHistory
AfghanistanGeography
AfghanistanPeople
AfghanistanCommunications
Autism
...
```

Or just cache the dicts so you don't have to parse that big XML file again. You do this only once:

```sh
$ bunzip2 enwiki-pages-articles.xml.bz2 | xmltodict.py 2 | gzip > enwiki.dicts.gz
```

And you reuse the dicts with every script that needs them:

```sh
$ gunzip enwiki.dicts.gz | script1.py
$ gunzip enwiki.dicts.gz | script2.py
...
```

## Roundtripping

You can also convert in the other direction, using the `unparse()` method:

```python
>>> mydict = {
...     'response': {
...             'status': 'good',
...             'last_updated': '2014-02-16T23:10:12Z',
...     }
... }
>>> print(unparse(mydict, pretty=True))
<?xml version="1.0" encoding="utf-8"?>
<response>
	<status>good</status>
	<last_updated>2014-02-16T23:10:12Z</last_updated>
</response>
```

Text values for nodes can be specified with the `cdata_key` key in the python dict, while node properties can be specified with the `attr_prefix` prefixed to the key name in the python dict. The default value for `attr_prefix` is `@` and the default value for `cdata_key` is `#text`.

```python
>>> import xmltodict
>>>
>>> mydict = {
...     'text': {
...         '@color':'red',
...         '@stroke':'2',
...         '#text':'This is a test'
...     }
... }
>>> print(xmltodict.unparse(mydict, pretty=True))
<?xml version="1.0" encoding="utf-8"?>
<text stroke="2" color="red">This is a test</text>
```

Lists that are specified under a key in a dictionary use the key as a tag for each item. But if a list does have a parent key, for example if a list exists inside another list, it does not have a tag to use and the items are converted to a string as shown in the example below.  To give tags to nested lists, use the `expand_iter` keyword argument to provide a tag as demonstrated below. Note that using `expand_iter` will break roundtripping.

```python
>>> mydict = {
...     "line": {
...         "points": [
...             [1, 5],
...             [2, 6],
...         ]
...     }
... }
>>> print(xmltodict.unparse(mydict, pretty=True))
<?xml version="1.0" encoding="utf-8"?>
<line>
        <points>[1, 5]</points>
        <points>[2, 6]</points>
</line>
>>> print(xmltodict.unparse(mydict, pretty=True, expand_iter="coord"))
<?xml version="1.0" encoding="utf-8"?>
<line>
        <points>
                <coord>1</coord>
                <coord>5</coord>
        </points>
        <points>
                <coord>2</coord>
                <coord>6</coord>
        </points>
</line>
```

## API Reference

### xmltodict.parse()

Parse XML input into a Python dictionary.

- `xml_input`: XML input as a string, file-like object, or generator of strings.
- `encoding=None`: Character encoding for the input XML.
- `expat=expat`: XML parser module to use.
- `process_namespaces=False`: Expand XML namespaces if True.
- `namespace_separator=':'`: Separator between namespace URI and local name.
- `disable_entities=True`: Disable entity parsing for security.
- `process_comments=False`: Include XML comments if True. Comments can be preserved when enabled, but by default they are ignored. Multiple top-level comments may not be preserved in exact order.
- `xml_attribs=True`: Include attributes in output dict (with `attr_prefix`).
- `attr_prefix='@'`: Prefix for XML attributes in the dict.
- `cdata_key='#text'`: Key for text content in the dict.
- `force_cdata=False`: Force text content to be wrapped as CDATA for specific elements. Can be a boolean (True/False), a tuple of element names to force CDATA for, or a callable function that receives (path, key, value) and returns True/False.
- `cdata_separator=''`: Separator string to join multiple text nodes. This joins adjacent text nodes. For example, set to a space to avoid concatenation.
- `postprocessor=None`: Function to modify parsed items.
- `dict_constructor=dict`: Constructor for dictionaries (e.g., dict).
- `strip_whitespace=True`: Remove leading/trailing whitespace in text nodes. Default is True; this trims whitespace in text nodes. Set to False to preserve whitespace exactly. When `process_comments=True`, this same flag also trims comment text; disable `strip_whitespace` if you need to preserve comment indentation or padding. If you preserve whitespace text nodes, avoid combining this with `unparse(..., pretty=True)`: the preserved text nodes and pretty-print indentation/newlines will both be emitted.
- `namespaces=None`: Mapping of namespaces to prefixes, or None to keep full URIs.
- `force_list=None`: Force list values for specific elements. Can be a boolean (True/False), a tuple of element names to force lists for, or a callable function that receives (path, key, value) and returns True/False. Useful for elements that may appear once or multiple times to ensure consistent list output.
- `item_depth=0`: Depth at which to call `item_callback`.
- `item_callback=lambda *args: True`: Function called on items at `item_depth`.
- `comment_key='#comment'`: Key used for XML comments when `process_comments=True`. Only used when `process_comments=True`. Comments can be preserved but multiple top-level comments may not retain order.

### xmltodict.unparse()

Convert a Python dictionary back into XML.

- `input_dict`: Dictionary to convert to XML.
- `output=None`: File-like object to write XML to; returns string if None.
- `encoding='utf-8'`: Encoding of the output XML.
- `bytes_errors='replace'`: Error handler used when decoding byte values during unparse (for example `'replace'`, `'strict'`, `'ignore'`).
- `full_document=True`: Include XML declaration if True.
- `short_empty_elements=False`: Use short tags for empty elements (`<tag/>`).
- `attr_prefix='@'`: Prefix for dictionary keys representing attributes.
- `cdata_key='#text'`: Key for text content in the dictionary.
- `pretty=False`: Pretty-print the XML output. This adds indentation/newlines for readability, so it should generally not be combined with parsed whitespace-preserving content when exact round-tripping matters.
- `indent='\t'`: Indentation string for pretty printing. May also be an integer number of spaces.
- `newl='\n'`: Newline character for pretty printing.
- `expand_iter=None`: Tag name to use for items in nested lists (breaks roundtripping).

> **Note:** When building XML from dictionaries, keys whose values are empty
> lists are skipped. For example, `{'a': []}` produces no `<a>` element. Add a
> placeholder child (for example, `{'a': ['']}`) if an explicit empty container
> element is required in the output.

Note: xmltodict aims to cover the common 90% of cases. It does not preserve every XML nuance (attribute order, mixed content ordering, multiple top-level comments). For exact fidelity, use a full XML library such as lxml.

## Examples

### Selective force_cdata

The `force_cdata` parameter can be used to selectively force CDATA wrapping for specific elements:

```python
>>> xml = '<a><b>data1</b><c>data2</c><d>data3</d></a>'
>>> # Force CDATA only for 'b' and 'd' elements
>>> xmltodict.parse(xml, force_cdata=('b', 'd'))
{'a': {'b': {'#text': 'data1'}, 'c': 'data2', 'd': {'#text': 'data3'}}}

>>> # Force CDATA for all elements (original behavior)
>>> xmltodict.parse(xml, force_cdata=True)
{'a': {'b': {'#text': 'data1'}, 'c': {'#text': 'data2'}, 'd': {'#text': 'data3'}}}

>>> # Use a callable for complex logic
>>> def should_force_cdata(path, key, value):
...     return key in ['b', 'd'] and len(value) > 4
>>> xmltodict.parse(xml, force_cdata=should_force_cdata)
{'a': {'b': {'#text': 'data1'}, 'c': 'data2', 'd': {'#text': 'data3'}}}
```

### Selective force_list

The `force_list` parameter can be used to selectively force list values for specific elements:

```python
>>> xml = '<a><b>data1</b><b>data2</b><c>data3</c></a>'
>>> # Force lists only for 'b' elements
>>> xmltodict.parse(xml, force_list=('b',))
{'a': {'b': ['data1', 'data2'], 'c': 'data3'}}

>>> # Force lists for all elements (original behavior)
>>> xmltodict.parse(xml, force_list=True)
{'a': [{'b': ['data1', 'data2'], 'c': ['data3']}]}

>>> # Use a callable for complex logic
>>> def should_force_list(path, key, value):
...     return key in ['b'] and isinstance(value, str)
>>> xmltodict.parse(xml, force_list=should_force_list)
{'a': {'b': ['data1', 'data2'], 'c': 'data3'}}
```

## Ok, how do I get it?

### Using pypi

You just need to

```sh
$ pip install xmltodict
```

### Using conda

For installing `xmltodict` using Anaconda/Miniconda (*conda*) from the
[conda-forge channel][#xmltodict-conda] all you need to do is:

[#xmltodict-conda]: https://anaconda.org/conda-forge/xmltodict

```sh
$ conda install -c conda-forge xmltodict
```

### RPM-based distro (Fedora, RHEL, …)

There is an [official Fedora package for xmltodict](https://packages.fedoraproject.org/pkgs/python-xmltodict/).

```sh
$ sudo yum install python3-xmltodict
```

### Arch Linux

There is an [official Arch Linux package for xmltodict](https://archlinux.org/packages/extra/any/python-xmltodict/).

```sh
$ sudo pacman -S python-xmltodict
```

### Debian-based distro (Debian, Ubuntu, …)

There is an [official Debian package for xmltodict](https://tracker.debian.org/pkg/python-xmltodict).

```sh
$ sudo apt install python-xmltodict
```

### FreeBSD

There is an [official FreeBSD port for xmltodict](https://svnweb.freebsd.org/ports/head/devel/py-xmltodict/).

```sh
$ pkg install py36-xmltodict
```

### openSUSE/SLE (SLE 15, Leap 15, Tumbleweed)

There is an [official openSUSE package for xmltodict](https://software.opensuse.org/package/python-xmltodict).

```sh
# Python2
$ zypper in python2-xmltodict

# Python3
$ zypper in python3-xmltodict
```

## Type Annotations

For type checking support, install the external types package:

```sh
# Using pypi
$ pip install types-xmltodict

# Using conda
$ conda install -c conda-forge types-xmltodict
```

## Security Notes

A CVE (CVE-2025-9375) was filed against `xmltodict` but is [disputed](https://github.com/martinblech/xmltodict/issues/377#issuecomment-3255691923). The root issue lies in Python’s `xml.sax.saxutils.XMLGenerator` API, which does not validate XML element names and provides no built-in way to do so. Since `xmltodict` is a thin wrapper that passes keys directly to `XMLGenerator`, the same issue exists in the standard library itself.

It has been suggested that `xml.sax.saxutils.escape()` represents a secure usage path. This is incorrect: `escape()` is intended only for character data and attribute values, and can produce invalid XML when misapplied to element names. There is currently no secure, documented way in Python’s standard library to validate XML element names.

Despite this, Fluid Attacks chose to assign a CVE to `xmltodict` while leaving the identical behavior in Python’s own standard library unaddressed. Their disclosure process also gave only 10 days from first contact to publication—well short of the 90-day industry norm—leaving no real opportunity for maintainer response. These actions reflect an inconsistency of standards and priorities that raise concerns about motivations, as they do not primarily serve the security of the broader community.

The maintainer considers this CVE invalid and will formally dispute it with MITRE.

```

### `release-please-config.json`

```json
{
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
  "monorepo-tags": false,
  "include-component-in-tag": false,
  "release-type": "python",
  "packages": {
    ".": {
      "package-name": "xmltodict",
      "bootstrap-sha": "75a17701db20d5d3ec2ea1f6c901cf2211011eb5",
      "changelog-path": "CHANGELOG.md"
    }
  }
}

```

### `SECURITY.md`

```md
# Security Policy

## Supported Versions

We support the latest `1.x` release series. Versions older than `1.0` no longer receive security fixes.

## Reporting a Vulnerability

We ask that all security issues be reported privately so that we have a reasonable chance to understand and address the problem before it is made public. Please **do not open public GitHub issues, discussions, or pull requests** for suspected vulnerabilities.

Submit your report through GitHub's [private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability) tool for this repository. Reports sent through other channels may be missed.

When reporting, please include as much of the following information as you can:

* A clear description of the problem and its potential impact.
* Steps to reproduce the issue, preferably with a minimal XML payload or script.
* Any known workarounds or mitigations.
* Your preferred timeline for coordinated disclosure.

We may reach out to you via the GitHub vulnerability report thread for additional details or to coordinate testing a fix. If you need encrypted communication, please mention that in the report so we can explore options together.

## Coordinated Disclosure Expectations

This project currently has a single unpaid volunteer maintainer who may be offline for multiple weeks at a time. Because of this, please allow **up to 30 calendar days** for an initial response on your GitHub private vulnerability report before considering alternate disclosure paths. If you have not heard back within that window, feel free to update the same report to nudge us.

Once we have acknowledged the report, we ask for **at least 90 days** to investigate, implement, and release a fix before any public disclosure, unless we mutually agree on a different timeline. Complex issues, especially those requiring upstream changes or ecosystem coordination, may take longer. During that time we will keep you updated as we make progress. If we determine that a coordinated public disclosure is necessary before a fix is ready, we will work with you on messaging and timing.

## Recognition

We are grateful to the security community for helping keep `xmltodict` safe. With your permission, we will credit you in the release notes or changelog when a fix is published.

## Thank You

Responsible disclosure helps protect all users of `xmltodict`. Your patience and willingness to coordinate—especially given the maintainer's volunteer capacity—are essential to making that possible. Thank you for taking the time to report issues responsibly.

```

### `tests/__init__.py`

```py

```

### `tests/test_dicttoxml.py`

```py
from xmltodict import parse, unparse
import pytest
import re
from textwrap import dedent

_HEADER_RE = re.compile(r'^[^\n]*\n')


def _strip(fullxml):
    return _HEADER_RE.sub('', fullxml)


def test_root():
    obj = {'a': None}
    assert obj == parse(unparse(obj))
    assert unparse(obj) == unparse(parse(unparse(obj)))


def test_simple_cdata():
    obj = {'a': 'b'}
    assert obj == parse(unparse(obj))
    assert unparse(obj) == unparse(parse(unparse(obj)))


def test_cdata():
    obj = {'a': {'#text': 'y'}}
    assert obj == parse(unparse(obj), force_cdata=True)
    assert unparse(obj) == unparse(parse(unparse(obj)))


def test_attrib():
    obj = {'a': {'@href': 'x'}}
    assert obj == parse(unparse(obj))
    assert unparse(obj) == unparse(parse(unparse(obj)))


def test_attrib_and_cdata():
    obj = {'a': {'@href': 'x', '#text': 'y'}}
    assert obj == parse(unparse(obj))
    assert unparse(obj) == unparse(parse(unparse(obj)))


def test_list():
    obj = {'a': {'b': ['1', '2', '3']}}
    assert obj == parse(unparse(obj))
    assert unparse(obj) == unparse(parse(unparse(obj)))


def test_list_expand_iter():
    obj = {'a': {'b': [['1', '2'], ['3',]]}}
    #assert obj == parse(unparse(obj, expand_iter="item")))
    exp_xml = dedent('''\
    <?xml version="1.0" encoding="utf-8"?>
    <a><b><item>1</item><item>2</item></b><b><item>3</item></b></a>''')
    assert exp_xml == unparse(obj, expand_iter="item")


def test_generator():
    obj = {'a': {'b': ['1', '2', '3']}}

    def lazy_obj():
        return {'a': {'b': (i for i in ('1', '2', '3'))}}
    assert obj == parse(unparse(lazy_obj()))
    assert unparse(lazy_obj()) == unparse(parse(unparse(lazy_obj())))


def test_no_root():
    with pytest.raises(ValueError):
        unparse({})


def test_multiple_roots():
    with pytest.raises(ValueError):
        unparse({'a': '1', 'b': '2'})
    with pytest.raises(ValueError):
        unparse({'a': ['1', '2', '3']})


def test_no_root_nofulldoc():
    assert unparse({}, full_document=False) == ''


def test_multiple_roots_nofulldoc():
    obj = {"a": 1, "b": 2}
    xml = unparse(obj, full_document=False)
    assert xml == '<a>1</a><b>2</b>'
    obj = {'a': [1, 2]}
    xml = unparse(obj, full_document=False)
    assert xml == '<a>1</a><a>2</a>'


def test_nested():
    obj = {'a': {'b': '1', 'c': '2'}}
    assert obj == parse(unparse(obj))
    assert unparse(obj) == unparse(parse(unparse(obj)))
    obj = {'a': {'b': {'c': {'@a': 'x', '#text': 'y'}}}}
    assert obj == parse(unparse(obj))
    assert unparse(obj) == unparse(parse(unparse(obj)))


def test_semistructured():
    xml = '<a>abc<d/>efg</a>'
    assert _strip(unparse(parse(xml))) == '<a><d></d>abcefg</a>'


def test_preprocessor():
    obj = {"a": {"b:int": [1, 2], "b": "c"}}

    def p(key, value):
        try:
            key, _ = key.split(':')
        except ValueError:
            pass
        return key, value

    assert _strip(unparse(obj, preprocessor=p)) == '<a><b>1</b><b>2</b><b>c</b></a>'


def test_preprocessor_skipkey():
    obj = {'a': {'b': 1, 'c': 2}}

    def p(key, value):
        if key == 'b':
            return None
        return key, value

    assert _strip(unparse(obj, preprocessor=p)) == '<a><c>2</c></a>'


def test_attr_order_roundtrip():
    xml = '<root a="1" b="2" c="3"></root>'
    assert xml == _strip(unparse(parse(xml)))


def test_pretty_print():
    obj = {
        "a": {
            "b": [{"c": [1, 2]}, 3],
            "x": "y",
        }
    }
    newl = '\n'
    indent = '....'
    xml = dedent('''\
    <?xml version="1.0" encoding="utf-8"?>
    <a>
    ....<b>
    ........<c>1</c>
    ........<c>2</c>
    ....</b>
    ....<b>3</b>
    ....<x>y</x>
    </a>''')
    assert xml == unparse(obj, pretty=True, newl=newl, indent=indent)


def test_unparse_with_element_comment():
    obj = {"a": {"#comment": "note", "b": "1"}}
    xml = _strip(unparse(obj, full_document=True))
    assert xml == "<a><!--note--><b>1</b></a>"


def test_unparse_with_multiple_element_comments():
    obj = {"a": {"#comment": ["n1", "n2"], "b": "1"}}
    xml = _strip(unparse(obj, full_document=True))
    assert xml == "<a><!--n1--><!--n2--><b>1</b></a>"


def test_unparse_with_top_level_comment():
    obj = {"#comment": "top", "a": "1"}
    xml = _strip(unparse(obj, full_document=True))
    assert xml == "<!--top--><a>1</a>"


def test_unparse_with_multiple_top_level_comments():
    obj = {"#comment": ["t1", "t2"], "a": "1"}
    xml = _strip(unparse(obj, full_document=True))
    assert xml == "<!--t1--><!--t2--><a>1</a>"


def test_unparse_with_bytes_comment_uses_output_encoding():
    obj = {"#comment": b"caf\xe9", "a": "1"}
    xml = _strip(unparse(obj, full_document=True, encoding="iso-8859-1"))
    assert xml == "<!--caf\xe9--><a>1</a>"


def test_unparse_invalid_bytes_comment_replaced_by_default():
    obj = {"#comment": b"\xff", "a": "1"}
    xml = _strip(unparse(obj, full_document=True, encoding="utf-8"))
    assert xml == "<!--\ufffd--><a>1</a>"


def test_unparse_rejects_invalid_bytes_comment_for_encoding_with_strict():
    obj = {"#comment": b"\xff", "a": "1"}
    with pytest.raises(UnicodeDecodeError, match="'utf-8' codec can't decode byte 0xff"):
        unparse(
            obj,
            full_document=True,
            encoding="utf-8",
            bytes_errors="strict",
        )


def test_unparse_rejects_comment_with_double_hyphen():
    obj = {"#comment": "bad--comment", "a": "1"}
    with pytest.raises(ValueError, match="cannot contain '--'"):
        unparse(obj, full_document=True)


def test_unparse_rejects_comment_ending_with_hyphen():
    obj = {"#comment": "trailing-", "a": "1"}
    with pytest.raises(ValueError, match="cannot end with '-'"):
        unparse(obj, full_document=True)


def test_pretty_print_with_int_indent():
    obj = {
        "a": {
            "b": [{"c": [1, 2]}, 3],
            "x": "y",
        }
    }
    newl = '\n'
    indent = 2
    xml = dedent('''\
    <?xml version="1.0" encoding="utf-8"?>
    <a>
      <b>
        <c>1</c>
        <c>2</c>
      </b>
      <b>3</b>
      <x>y</x>
    </a>''')
    assert xml == unparse(obj, pretty=True, newl=newl, indent=indent)


def test_comment_roundtrip_limited():
    # Input with top-level comments and an element-level comment
    xml = """
    <!--top1--><a><b>1</b><!--e1--></a><!--top2-->
    """
    # Parse with comment processing enabled
    parsed1 = parse(xml, process_comments=True)
    # Unparse and parse again (roundtrip)
    xml2 = unparse(parsed1)
    parsed2 = parse(xml2, process_comments=True)

    # Content preserved
    assert 'a' in parsed2
    assert parsed2['a']['b'] == '1'

    # Element-level comment preserved under '#comment'
    assert parsed2['a']['#comment'] == 'e1'

    # Top-level comments preserved as a list (order not guaranteed)
    top = parsed2.get('#comment')
    assert top is not None
    top_list = top if isinstance(top, list) else [top]
    assert set(top_list) == {'top1', 'top2'}


def test_encoding():
    value = chr(39321)
    obj = {'a': value}
    utf8doc = unparse(obj, encoding='utf-8')
    latin1doc = unparse(obj, encoding='iso-8859-1')
    assert parse(utf8doc) == parse(latin1doc)
    assert parse(utf8doc) == obj


def test_fulldoc():
    xml_declaration_re = re.compile(
        '^' + re.escape('<?xml version="1.0" encoding="utf-8"?>'))
    assert xml_declaration_re.match(unparse({'a': 1}))
    assert not xml_declaration_re.match(unparse({'a': 1}, full_document=False))


def test_non_string_value():
    obj = {'a': 1}
    assert '<a>1</a>' == _strip(unparse(obj))


def test_non_string_attr():
    obj = {'a': {'@attr': 1}}
    assert '<a attr="1"></a>' == _strip(unparse(obj))


def test_short_empty_elements():
    obj = {'a': None}
    assert '<a/>' == _strip(unparse(obj, short_empty_elements=True))


def test_namespace_support():
    obj = {
        "http://defaultns.com/:root": {
            "@xmlns": {
                "": "http://defaultns.com/",
                "a": "http://a.com/",
                "b": "http://b.com/",
            },
            "http://defaultns.com/:x": {
                "@http://a.com/:attr": "val",
                "#text": "1",
            },
            "http://a.com/:y": "2",
            "http://b.com/:z": "3",
        },
    }
    ns = {
        'http://defaultns.com/': '',
        'http://a.com/': 'a',
        'http://b.com/': 'b',
    }

    expected_xml = '''<?xml version="1.0" encoding="utf-8"?>
<root xmlns="http://defaultns.com/" xmlns:a="http://a.com/" \
xmlns:b="http://b.com/"><x a:attr="val">1</x><a:y>2</a:y><b:z>3</b:z></root>'''
    xml = unparse(obj, namespaces=ns)

    assert xml == expected_xml


def test_xmlns_values_use_consistent_boolean_coercion():
    xml = unparse({"root": {"@xmlns": {"a": True}}}, full_document=False)
    assert xml == '<root xmlns:a="true"></root>'


def test_xmlns_dict_honors_custom_attr_prefix():
    # A namespace-declaration dict must be recognized under a custom
    # attr_prefix, like every other attribute — otherwise unparse cannot
    # round-trip what parse(..., attr_prefix="!") produced.
    xml = unparse(
        {"root": {"!xmlns": {"a": "http://a.com/"}, "!id": "7"}},
        attr_prefix="!",
        full_document=False,
    )
    assert xml == '<root xmlns:a="http://a.com/" id="7"></root>'


def test_namespace_roundtrip_honors_custom_attr_prefix():
    obj = parse(
        '<root xmlns:a="http://a.com/" id="7"><a:y>2</a:y></root>',
        process_namespaces=True,
        attr_prefix="!",
    )

    xml = unparse(
        obj,
        attr_prefix="!",
        namespaces={"http://a.com/": "a"},
        full_document=False,
    )

    assert xml == '<root id="7" xmlns:a="http://a.com/"><a:y>2</a:y></root>'


def test_xmlns_values_decode_bytes_with_output_encoding():
    xml = unparse(
        {"root": {"@xmlns": {"a": b"http://ex\xe9.com/"}}},
        full_document=False,
        encoding="iso-8859-1",
    )
    assert xml == '<root xmlns:a="http://ex\xe9.com/"></root>'


def test_xmlns_values_replace_invalid_bytes_by_default():
    xml = unparse(
        {"root": {"@xmlns": {"a": b"\xff"}}},
        full_document=False,
        encoding="utf-8",
    )
    assert xml == '<root xmlns:a="\ufffd"></root>'


def test_xmlns_values_reject_invalid_bytes_with_strict():
    with pytest.raises(UnicodeDecodeError, match="'utf-8' codec can't decode byte 0xff"):
        unparse(
            {"root": {"@xmlns": {"a": b"\xff"}}},
            full_document=False,
            encoding="utf-8",
            bytes_errors="strict",
        )


def test_boolean_unparse():
    expected_xml = '<?xml version="1.0" encoding="utf-8"?>\n<x>true</x>'
    xml = unparse(dict(x=True))
    assert xml == expected_xml

    expected_xml = '<?xml version="1.0" encoding="utf-8"?>\n<x>false</x>'
    xml = unparse(dict(x=False))
    assert xml == expected_xml

    expected_xml = '<?xml version="1.0" encoding="utf-8"?>\n<x attr="true"></x>'
    xml = unparse({'x': {'@attr': True}})
    assert xml == expected_xml

    expected_xml = '<?xml version="1.0" encoding="utf-8"?>\n<x attr="false"></x>'
    xml = unparse({'x': {'@attr': False}})
    assert xml == expected_xml


def test_unparse_bytes_in_attributes_and_cdata_use_output_encoding():
    xml = unparse({"x": {"@attr": b"caf\xe9", "#text": b"caf\xe9"}}, full_document=False, encoding="iso-8859-1")
    assert xml == '<x attr="caf\xe9">caf\xe9</x>'


def test_unparse_bytes_text_node_uses_output_encoding():
    xml = unparse({"x": b"caf\xe9"}, full_document=False, encoding="iso-8859-1")
    assert xml == "<x>caf\xe9</x>"


def test_unparse_bytes_text_node_with_expand_iter_uses_output_encoding():
    xml = unparse({"x": b"caf\xe9"}, full_document=False, encoding="iso-8859-1", expand_iter="item")
    assert xml == "<x>caf\xe9</x>"


def test_unparse_invalid_bytes_in_attributes_and_cdata_replaced_by_default():
    xml = unparse({"x": {"@attr": b"\xff", "#text": b"\xff"}}, full_document=False, encoding="utf-8")
    assert xml == '<x attr="\ufffd">\ufffd</x>'


def test_unparse_invalid_bytes_text_node_replaced_by_default():
    xml = unparse({"x": b"\xff"}, full_document=False, encoding="utf-8")
    assert xml == "<x>\ufffd</x>"


def test_unparse_rejects_invalid_bytes_in_attributes_and_cdata_for_encoding_with_strict():
    with pytest.raises(UnicodeDecodeError, match="'utf-8' codec can't decode byte 0xff"):
        unparse({"x": {"@attr": b"\xff"}}, full_document=False, encoding="utf-8", bytes_errors="strict")
    with pytest.raises(UnicodeDecodeError, match="'utf-8' codec can't decode byte 0xff"):
        unparse({"x": {"#text": b"\xff"}}, full_document=False, encoding="utf-8", bytes_errors="strict")


def test_unparse_rejects_invalid_bytes_text_node_for_encoding_with_strict():
    with pytest.raises(UnicodeDecodeError, match="'utf-8' codec can't decode byte 0xff"):
        unparse({"x": b"\xff"}, full_document=False, encoding="utf-8", bytes_errors="strict")


def test_unparse_rejects_invalid_bytes_errors_handler():
    with pytest.raises(ValueError, match="Invalid bytes_errors handler: nope"):
        unparse({"x": {"@attr": b"\xff"}}, full_document=False, bytes_errors="nope")


def test_rejects_tag_name_with_angle_brackets():
    # Minimal guard: disallow '<' or '>' to prevent breaking tag context
    with pytest.raises(ValueError):
        unparse({"m><tag>content</tag": "unsafe"}, full_document=False)


def test_rejects_attribute_name_with_angle_brackets():
    # Now we expect bad attribute names to be rejected
    with pytest.raises(ValueError):
        unparse(
            {"a": {"@m><tag>content</tag": "unsafe", "#text": "x"}},
            full_document=False,
        )


def test_rejects_malicious_xmlns_prefix():
    # xmlns prefixes go under @xmlns mapping; reject angle brackets in prefix
    with pytest.raises(ValueError):
        unparse(
            {
                "a": {
                    "@xmlns": {"m><bad": "http://example.com/"},
                    "#text": "x",
                }
            },
            full_document=False,
        )


def test_attribute_values_with_angle_brackets_are_escaped():
    # Attribute values should be escaped by XMLGenerator
    xml = unparse({"a": {"@attr": "1<middle>2", "#text": "x"}}, full_document=False)
    # The generated XML should contain escaped '<' and '>' within the attribute value
    assert 'attr="1&lt;middle&gt;2"' in xml


def test_rejects_tag_name_starting_with_question():
    with pytest.raises(ValueError):
        unparse({"?pi": "data"}, full_document=False)


def test_rejects_tag_name_starting_with_bang():
    with pytest.raises(ValueError):
        unparse({"!decl": "data"}, full_document=False)


def test_rejects_attribute_name_starting_with_question():
    with pytest.raises(ValueError):
        unparse({"a": {"@?weird": "x"}}, full_document=False)


def test_rejects_attribute_name_starting_with_bang():
    with pytest.raises(ValueError):
        unparse({"a": {"@!weird": "x"}}, full_document=False)


def test_rejects_xmlns_prefix_starting_with_question_or_bang():
    with pytest.raises(ValueError):
        unparse({"a": {"@xmlns": {"?p": "http://e/"}}}, full_document=False)
    with pytest.raises(ValueError):
        unparse({"a": {"@xmlns": {"!p": "http://e/"}}}, full_document=False)


def test_rejects_non_string_names():
    class Weird:
        def __str__(self):
            return "bad>name"

    # Non-string element key
    with pytest.raises(ValueError):
        unparse({Weird(): "x"}, full_document=False)
    # Non-string attribute key
    with pytest.raises(ValueError):
        unparse({"a": {Weird(): "x"}}, full_document=False)


def test_rejects_tag_name_with_slash():
    with pytest.raises(ValueError):
        unparse({"bad/name": "x"}, full_document=False)


def test_rejects_tag_name_with_whitespace():
    for name in ["bad name", "bad\tname", "bad\nname"]:
        with pytest.raises(ValueError):
            unparse({name: "x"}, full_document=False)


def test_rejects_attribute_name_with_slash():
    with pytest.raises(ValueError):
        unparse({"a": {"@bad/name": "x"}}, full_document=False)


def test_rejects_attribute_name_with_whitespace():
    for name in ["@bad name", "@bad\tname", "@bad\nname"]:
        with pytest.raises(ValueError):
            unparse({"a": {name: "x"}}, full_document=False)


def test_rejects_xmlns_prefix_with_slash_or_whitespace():
    # Slash
    with pytest.raises(ValueError):
        unparse({"a": {"@xmlns": {"bad/prefix": "http://e/"}}}, full_document=False)
    # Whitespace
    with pytest.raises(ValueError):
        unparse({"a": {"@xmlns": {"bad prefix": "http://e/"}}}, full_document=False)


def test_rejects_names_with_quotes_and_equals():
    # Element names
    for name in ['a"b', "a'b", "a=b"]:
        with pytest.raises(ValueError):
            unparse({name: "x"}, full_document=False)
    # Attribute names
    for name in ['@a"b', "@a'b", "@a=b"]:
        with pytest.raises(ValueError):
            unparse({"a": {name: "x"}}, full_document=False)
    # xmlns prefixes
    for prefix in ['a"b', "a'b", "a=b"]:
        with pytest.raises(ValueError):
            unparse({"a": {"@xmlns": {prefix: "http://e/"}}}, full_document=False)


def test_pretty_print_and_short_empty_elements_consistency():
    """Test that pretty and compact modes produce equivalent results when stripped.

    This test covers issue #352: Edge case with pretty_print and short_empty_elements.
    When short_empty_elements=True, empty elements should be written as <tag/>
    regardless of whether pretty printing is enabled.
    """
    # Test case from issue #352: empty list child
    input_dict = {"Foos": {"Foo": []}}

    compact = unparse(
        input_dict, pretty=False, short_empty_elements=True, full_document=False
    )
    pretty = unparse(
        input_dict, pretty=True, short_empty_elements=True, full_document=False
    )
    pretty_compacted = pretty.replace("\n", "").replace("\t", "")

    # They should be equal when pretty formatting is stripped
    assert pretty_compacted == compact
    assert compact == "<Foos/>"
    assert pretty_compacted == "<Foos/>"


def test_empty_list_filtering():
    """Test that empty lists are filtered out and don't create empty child elements."""
    # Test various cases with empty lists
    test_cases = [
        # Case 1: Single empty list child
        ({"Foos": {"Foo": []}}, "<Foos/>"),
        # Case 2: Multiple empty list children
        ({"Foos": {"Foo": [], "Bar": []}}, "<Foos/>"),
        # Case 3: Mixed empty and non-empty children
        ({"Foos": {"Foo": [], "Bar": "value"}}, "<Foos><Bar>value</Bar></Foos>"),
        # Case 4: Nested empty lists
        ({"Foos": {"Foo": {"Bar": []}}}, "<Foos><Foo/></Foos>"),
        # Case 5: Empty list with attributes
        ({"Foos": {"@attr": "value", "Foo": []}}, '<Foos attr="value"/>'),
    ]

    for input_dict, expected_compact in test_cases:
        # Test compact mode
        compact = unparse(
            input_dict,
            pretty=False,
            short_empty_elements=True,
            full_document=False,
        )
        assert compact == expected_compact

        # Test pretty mode
        pretty = unparse(
            input_dict,
            pretty=True,
            short_empty_elements=True,
            full_document=False,
        )
        pretty_compacted = pretty.replace("\n", "").replace("\t", "")
        assert pretty_compacted == expected_compact


def test_empty_list_filtering_with_short_empty_elements_false():
    """Test that empty lists are still filtered when short_empty_elements=False."""
    input_dict = {"Foos": {"Foo": []}}

    # With short_empty_elements=False, empty elements should be <tag></tag>
    compact = unparse(
        input_dict, pretty=False, short_empty_elements=False, full_document=False
    )
    pretty = unparse(
        input_dict, pretty=True, short_empty_elements=False, full_document=False
    )
    pretty_compacted = pretty.replace("\n", "").replace("\t", "")

    # They should be equal when pretty formatting is stripped
    assert pretty_compacted == compact
    assert compact == "<Foos></Foos>"
    assert pretty_compacted == "<Foos></Foos>"


def test_non_empty_lists_are_not_filtered():
    """Test that non-empty lists are not filtered out."""
    # Test with non-empty lists
    input_dict = {"Foos": {"Foo": ["item1", "item2"]}}

    compact = unparse(
        input_dict, pretty=False, short_empty_elements=True, full_document=False
    )
    pretty = unparse(
        input_dict, pretty=True, short_empty_elements=True, full_document=False
    )
    pretty_compacted = pretty.replace("\n", "").replace("\t", "")

    # The lists should be processed normally
    assert pretty_compacted == compact
    assert compact == "<Foos><Foo>item1</Foo><Foo>item2</Foo></Foos>"
    assert (
        pretty_compacted == "<Foos><Foo>item1</Foo><Foo>item2</Foo></Foos>"
    )


def test_empty_dict_vs_empty_list_behavior():
    """Test the difference between empty dicts and empty lists."""
    # Empty dict should create a child element
    input_dict_dict = {"Foos": {"Foo": {}}}
    compact_dict = unparse(
        input_dict_dict,
        pretty=False,
        short_empty_elements=True,
        full_document=False,
    )
    assert compact_dict == "<Foos><Foo/></Foos>"

    # Empty list should be filtered out
    input_dict_list = {"Foos": {"Foo": []}}
    compact_list = unparse(
        input_dict_list,
        pretty=False,
        short_empty_elements=True,
        full_document=False,
    )
    assert compact_list == "<Foos/>"

    # They should be different
    assert compact_dict != compact_list


def test_non_string_text_with_attributes():
    """Test that non-string #text values work when tag has attributes.

    This test covers GitHub issue #366: Tag value (#text) must be a string
    when tag has additional parameters - unparse.

    Also tests that plain values and explicit #text values are treated
    consistently (both go through the same conversion logic).
    """
    # Test cases for explicit #text values with attributes
    assert unparse({"a": {"@param": "test", "#text": 1}}, full_document=False) == '<a param="test">1</a>'

    assert unparse({"a": {"@param": 42, "#text": 3.14}}, full_document=False) == '<a param="42">3.14</a>'

    assert unparse({"a": {"@param": "flag", "#text": True}}, full_document=False) == '<a param="flag">true</a>'

    assert unparse({"a": {"@param": "test", "#text": None}}, full_document=False) == '<a param="test"></a>'

    assert unparse({"a": {"@param": "test", "#text": "string"}}, full_document=False) == '<a param="test">string</a>'

    assert unparse({"a": {"@attr1": "value1", "@attr2": 2, "#text": 100}}, full_document=False) == '<a attr1="value1" attr2="2">100</a>'

    # Test cases for plain values (should be treated the same as #text)
    assert unparse({"a": 1}, full_document=False) == '<a>1</a>'
    assert unparse({"a": 3.14}, full_document=False) == '<a>3.14</a>'
    assert unparse({"a": True}, full_document=False) == '<a>true</a>'
    assert unparse({"a": "hello"}, full_document=False) == '<a>hello</a>'
    assert unparse({"a": None}, full_document=False) == '<a></a>'

    # Consistency tests: plain values should match explicit #text values
    assert unparse({"a": 42}, full_document=False) == unparse({"a": {"#text": 42}}, full_document=False)

    assert unparse({"a": 3.14}, full_document=False) == unparse({"a": {"#text": 3.14}}, full_document=False)

    assert unparse({"a": True}, full_document=False) == unparse({"a": {"#text": True}}, full_document=False)

    assert unparse({"a": "hello"}, full_document=False) == unparse({"a": {"#text": "hello"}}, full_document=False)
    assert unparse({"a": None}, full_document=False) == unparse({"a": {"#text": None}}, full_document=False)


def test_none_text_with_short_empty_elements_and_attributes():
    obj = {"x": {"#text": None, "@pro": None}, "y": None}
    assert unparse(obj, short_empty_elements=True, full_document=False) == '<x pro=""/><y/>'


def test_none_attribute_serializes_as_empty_string():
    assert unparse({"x": {"@pro": None}}, full_document=False) == '<x pro=""></x>'


def test_unparse_skips_none_comment():
    obj = {"a": {"#comment": None, "b": "1"}}
    xml = _strip(unparse(obj, full_document=True))
    assert xml == "<a><b>1</b></a>"


def test_unparse_skips_empty_comment():
    obj = {"a": {"#comment": "", "b": "1"}}
    xml = _strip(unparse(obj, full_document=True))
    assert xml == "<a><b>1</b></a>"


def test_unparse_filters_none_and_empty_comments_in_list():
    obj = {"a": {"#comment": ["n1", None, "", "n2"], "b": "1"}}
    xml = _strip(unparse(obj, full_document=True))
    assert xml == "<a><!--n1--><!--n2--><b>1</b></a>"


def test_pretty_print_element_comments():
    obj = {"a": {"#comment": ["n1", "n2"], "b": "1"}}
    xml = dedent('''\
    <?xml version="1.0" encoding="utf-8"?>
    <a>
    \t<!--n1-->
    \t<!--n2-->
    \t<b>1</b>
    </a>''')
    assert xml == unparse(obj, pretty=True)


def test_pretty_print_top_level_comment_with_int_indent():
    obj = {"#comment": "top", "a": "1"}
    xml = dedent('''\
    <?xml version="1.0" encoding="utf-8"?>
    <!--top-->
    <a>1</a>''')
    assert xml == unparse(obj, pretty=True, indent=4)

```

### `tests/test_xmltodict.py`

```py
from xmltodict import parse, ParsingInterrupted
import collections
import pytest
from io import BytesIO

from xml.parsers.expat import ParserCreate
from xml.parsers import expat


def test_string_vs_file():
    xml = '<a>data</a>'
    assert parse(xml) == parse(BytesIO(xml.encode('ascii')))


def test_minimal():
    assert parse('<a/>') == {'a': None}
    assert parse('<a/>', force_cdata=True) == {'a': None}


def test_simple():
    assert parse('<a>data</a>') == {'a': 'data'}


def test_force_cdata():
    assert parse('<a>data</a>', force_cdata=True) == {'a': {'#text': 'data'}}


def test_selective_force_cdata_tuple():
    xml = "<a><b>data1</b><c>data2</c><d>data3</d></a>"
    # Test with tuple of specific element names
    result = parse(xml, force_cdata=("b", "d"))
    expected = {
        "a": {"b": {"#text": "data1"}, "c": "data2", "d": {"#text": "data3"}}
    }
    assert result == expected


def test_selective_force_cdata_single_element():
    xml = "<a><b>data1</b><c>data2</c></a>"
    # Test with single element name
    result = parse(xml, force_cdata=("b",))
    expected = {"a": {"b": {"#text": "data1"}, "c": "data2"}}
    assert result == expected


def test_selective_force_cdata_empty_tuple():
    xml = "<a><b>data1</b><c>data2</c></a>"
    # Test with empty tuple (should behave like force_cdata=False)
    result = parse(xml, force_cdata=())
    expected = {"a": {"b": "data1", "c": "data2"}}
    assert result == expected


def test_selective_force_cdata_callable():
    xml = "<a><b>data1</b><c>data2</c><d>data3</d></a>"

    # Test with callable function
    def should_force_cdata(path, key, value):
        return key in ["b", "d"]

    result = parse(xml, force_cdata=should_force_cdata)
    expected = {
        "a": {"b": {"#text": "data1"}, "c": "data2", "d": {"#text": "data3"}}
    }
    assert result == expected


def test_selective_force_cdata_nested_elements():
    xml = "<a><b><c>data1</c></b><d>data2</d></a>"
    # Test with nested elements - only 'c' should be forced
    result = parse(xml, force_cdata=("c",))
    expected = {"a": {"b": {"c": {"#text": "data1"}}, "d": "data2"}}
    assert result == expected


def test_selective_force_cdata_with_attributes():
    xml = '<a><b attr="value">data1</b><c>data2</c></a>'
    # Test with attributes - force_cdata should still work
    result = parse(xml, force_cdata=("b",))
    expected = {"a": {"b": {"@attr": "value", "#text": "data1"}, "c": "data2"}}
    assert result == expected


def test_selective_force_cdata_backwards_compatibility():
    xml = "<a><b>data1</b><c>data2</c></a>"
    # Test that boolean True still works (backwards compatibility)
    result_true = parse(xml, force_cdata=True)
    expected_true = {"a": {"b": {"#text": "data1"}, "c": {"#text": "data2"}}}
    assert result_true == expected_true

    # Test that boolean False still works (backwards compatibility)
    result_false = parse(xml, force_cdata=False)
    expected_false = {"a": {"b": "data1", "c": "data2"}}
    assert result_false == expected_false


def test_custom_cdata():
    assert parse('<a>data</a>', force_cdata=True, cdata_key='_CDATA_') == {'a': {'_CDATA_': 'data'}}


def test_list():
    assert parse('<a><b>1</b><b>2</b><b>3</b></a>') == {'a': {'b': ['1', '2', '3']}}


def test_attrib():
    assert parse('<a href="xyz"/>') == {'a': {'@href': 'xyz'}}


def test_skip_attrib():
    assert parse('<a href="xyz"/>', xml_attribs=False) == {'a': None}


def test_custom_attrib():
    assert parse('<a href="xyz"/>', attr_prefix='!') == {'a': {'!href': 'xyz'}}


def test_attrib_and_cdata():
    assert parse('<a href="xyz">123</a>') == {'a': {'@href': 'xyz', '#text': '123'}}


def test_semi_structured():
    assert parse('<a>abc<b/>def</a>') == {'a': {'b': None, '#text': 'abcdef'}}
    assert parse('<a>abc<b/>def</a>', cdata_separator='\n') == {'a': {'b': None, '#text': 'abc\ndef'}}


def test_nested_semi_structured():
    assert parse('<a>abc<b>123<c/>456</b>def</a>') == {'a': {'#text': 'abcdef', 'b': {'#text': '123456', 'c': None}}}


def test_skip_whitespace():
    xml = """
    <root>


      <emptya>           </emptya>
      <emptyb attr="attrvalue">


      </emptyb>
      <value>hello</value>
    </root>
    """
    assert parse(xml) == {'root': {'emptya': None, 'emptyb': {'@attr': 'attrvalue'}, 'value': 'hello'}}


def test_keep_whitespace():
    xml = "<root> </root>"
    assert parse(xml) == dict(root=None)
    assert parse(xml, strip_whitespace=False) == dict(root=' ')


def test_streaming():
    def cb(path, item):
        cb.count += 1
        assert path == [('a', {'x': 'y'}), ('b', None)]
        assert item == str(cb.count)
        return True
    cb.count = 0
    parse('<a x="y"><b>1</b><b>2</b><b>3</b></a>', item_depth=2, item_callback=cb)
    assert cb.count == 3


def test_streaming_interrupt():
    def cb(path, item):
        return False
    with pytest.raises(ParsingInterrupted):
        parse('<a>x</a>', item_depth=1, item_callback=cb)


def test_streaming_generator():
    def cb(path, item):
        cb.count += 1
        assert path == [('a', {'x': 'y'}), ('b', None)]
        assert item == str(cb.count)
        return True
    cb.count = 0
    parse((n for n in '<a x="y"><b>1</b><b>2</b><b>3</b></a>'), item_depth=2, item_callback=cb)
    assert cb.count == 3


def test_streaming_returns_none():
    # When streaming (item_depth > 0), parse should return None
    def cb(path, item):
        return True

    result = parse("<a><b>1</b><b>2</b></a>", item_depth=2, item_callback=cb)
    assert result is None


def _stream(xml, depth, **kwargs):
    items = []
    parse(xml, item_depth=depth,
          item_callback=lambda path, item: items.append(item) or True,
          **kwargs)
    return items


def test_streaming_text_with_attrs():
    # char data was dropped when the streamed item had attributes (#257)
    xml = '<items><item id="1">hello</item></items>'
    assert _stream(xml, 2) == [{'@id': '1', '#text': 'hello'}]


def test_streaming_text_postprocessor():
    def postprocessor(path, key, value):
        if key == '#text':
            assert path == [('items', None), ('item', {'id': '1'})]
            return 'text', value.upper()
        return key, value

    xml = '<items><item id="1">hello</item></items>'
    assert _stream(xml, 2, postprocessor=postprocessor) == \
        [{'@id': '1', 'text': 'HELLO'}]


def test_streaming_text_with_children():
    xml = '<a>free text<b>1</b><b>2</b></a>'
    assert _stream(xml, 1) == [{'b': ['1', '2'], '#text': 'free text'}]
    xml = '<items><item><sub>x</sub>tail</item></items>'
    assert _stream(xml, 2) == [{'sub': 'x', '#text': 'tail'}]


def test_streaming_text_whitespace():
    xml = '<items><item id="1"> spaced </item></items>'
    assert _stream(xml, 2) == [{'@id': '1', '#text': 'spaced'}]
    assert _stream(xml, 2, strip_whitespace=False) == \
        [{'@id': '1', '#text': ' spaced '}]
    # whitespace-only text is stripped to nothing, like non-streaming parse
    xml = '<items><item id="1"> </item></items>'
    assert _stream(xml, 2) == [{'@id': '1'}]


def test_streaming_force_cdata_and_cdata_key():
    xml = '<items><item>x</item></items>'
    assert _stream(xml, 2, force_cdata=True) == [{'#text': 'x'}]
    xml = '<items><item id="1">x</item></items>'
    assert _stream(xml, 2, cdata_key='$') == [{'@id': '1', '$': 'x'}]


def test_streaming_matches_nonstreaming():
    docs = [
        '<r><item>plain</item></r>',
        '<r><item id="1">text</item><item>only</item></r>',
        '<r><item a="1"><c>x</c>tail</item><item a="2">lead<c>y</c></item></r>',
        '<r><item><sub><deep d="3">v</deep></sub>mixed</item></r>',
        '<r><item> </item><item id="1"> </item></r>',
    ]
    for xml in docs:
        expected = parse(xml)['r']['item']
        if not isinstance(expected, list):
            expected = [expected]
        assert _stream(xml, 2) == expected, xml


def test_streaming_random_docs_match_nonstreaming():
    import random
    rnd = random.Random(20260715)
    for _ in range(200):
        items = []
        for i in range(rnd.randint(1, 4)):
            attr = f' id="{i}"' if rnd.random() < 0.5 else ''
            children = ''.join(f'<c{j}>v{j}</c{j}>'
                               for j in range(rnd.randint(0, 2)))
            text = rnd.choice(['', ' ', 'txt', 'a b'])
            if rnd.random() < 0.5:
                body = text + children
            else:
                body = children + text
            items.append(f'<item{attr}>{body}</item>')
        xml = f"<r>{''.join(items)}</r>"
        expected = parse(xml)['r']['item']
        if not isinstance(expected, list):
            expected = [expected]
        assert _stream(xml, 2) == expected, xml


def test_postprocessor():
    def postprocessor(path, key, value):
        try:
            return key + ':int', int(value)
        except (ValueError, TypeError):
            return key, value
    assert {'a': {'b:int': [1, 2], 'b': 'x'}} == parse('<a><b>1</b><b>2</b><b>x</b></a>', postprocessor=postprocessor)


def test_postprocessor_attribute():
    def postprocessor(path, key, value):
        try:
            return key + ':int', int(value)
        except (ValueError, TypeError):
            return key, value
    assert {'a': {'@b:int': 1}} == parse('<a b="1"/>', postprocessor=postprocessor)


def test_postprocessor_skip():
    def postprocessor(path, key, value):
        if key == 'b':
            value = int(value)
            if value == 3:
                return None
        return key, value
    assert {'a': {'b': [1, 2]}} == parse('<a><b>1</b><b>2</b><b>3</b></a>', postprocessor=postprocessor)


def test_unicode():
    value = chr(39321)
    assert {'a': value} == parse(f'<a>{value}</a>')


def test_encoded_string():
    value = chr(39321)
    xml = f'<a>{value}</a>'
    assert parse(xml) == parse(xml.encode('utf-8'))


def test_namespace_support():
    xml = """
    <root xmlns="http://defaultns.com/"
          xmlns:a="http://a.com/"
          xmlns:b="http://b.com/"
          version="1.00">
      <x a:attr="val">1</x>
      <a:y>2</a:y>
      <b:z>3</b:z>
    </root>
    """
    d = {
        'http://defaultns.com/:root': {
            '@version': '1.00',
            '@xmlns': {
                '': 'http://defaultns.com/',
                'a': 'http://a.com/',
                'b': 'http://b.com/',
            },
            'http://defaultns.com/:x': {
                '@http://a.com/:attr': 'val',
                '#text': '1',
            },
            'http://a.com/:y': '2',
            'http://b.com/:z': '3',
        }
    }
    res = parse(xml, process_namespaces=True)
    assert res == d


def test_namespace_collapse():
    xml = """
    <root xmlns="http://defaultns.com/"
          xmlns:a="http://a.com/"
          xmlns:b="http://b.com/"
          version="1.00">
      <x a:attr="val">1</x>
      <a:y>2</a:y>
      <b:z>3</b:z>
    </root>
    """
    namespaces = {
        'http://defaultns.com/': '',
        'http://a.com/': 'ns_a',
    }
    d = {
        'root': {
            '@version': '1.00',
            '@xmlns': {
                '': 'http://defaultns.com/',
                'a': 'http://a.com/',
                'b': 'http://b.com/',
            },
            'x': {
                '@ns_a:attr': 'val',
                '#text': '1',
            },
            'ns_a:y': '2',
            'http://b.com/:z': '3',
        },
    }
    res = parse(xml, process_namespaces=True, namespaces=namespaces)
    assert res == d


def test_namespace_collapse_all():
    xml = """
    <root xmlns="http://defaultns.com/"
          xmlns:a="http://a.com/"
          xmlns:b="http://b.com/"
          version="1.00">
      <x a:attr="val">1</x>
      <a:y>2</a:y>
      <b:z>3</b:z>
    </root>
    """
    namespaces = collections.defaultdict(lambda: None)
    d = {
        'root': {
            '@version': '1.00',
            '@xmlns': {
                '': 'http://defaultns.com/',
                'a': 'http://a.com/',
                'b': 'http://b.com/',
            },
            'x': {
                '@attr': 'val',
                '#text': '1',
            },
            'y': '2',
            'z': '3',
        },
    }
    res = parse(xml, process_namespaces=True, namespaces=namespaces)
    assert res == d


def test_namespace_ignore():
    xml = """
    <root xmlns="http://defaultns.com/"
          xmlns:a="http://a.com/"
          xmlns:b="http://b.com/"
          version="1.00">
      <x>1</x>
      <a:y>2</a:y>
      <b:z>3</b:z>
    </root>
    """
    d = {
        'root': {
            '@xmlns': 'http://defaultns.com/',
            '@xmlns:a': 'http://a.com/',
            '@xmlns:b': 'http://b.com/',
            '@version': '1.00',
            'x': '1',
            'a:y': '2',
            'b:z': '3',
        },
    }
    assert parse(xml) == d


def test_force_list_basic():
    xml = """
    <servers>
      <server>
        <name>server1</name>
        <os>os1</os>
      </server>
    </servers>
    """
    expectedResult = {
        'servers': {
            'server': [
                {
                    'name': 'server1',
                    'os': 'os1',
                },
            ],
        }
    }
    assert parse(xml, force_list=('server',)) == expectedResult


def test_force_list_callable():
    xml = """
    <config>
        <servers>
          <server>
            <name>server1</name>
            <os>os1</os>
          </server>
        </servers>
        <skip>
            <server></server>
        </skip>
    </config>
    """

    def force_list(path, key, value):
        """Only return True for servers/server, but not for skip/server."""
        if key != 'server':
            return False
        return path and path[-1][0] == 'servers'

    expectedResult = {
        'config': {
            'servers': {
                'server': [
                    {
                        'name': 'server1',
                        'os': 'os1',
                    },
                ],
            },
            'skip': {
                'server': None,
            },
        },
    }
    assert parse(xml, force_list=force_list, dict_constructor=dict) == expectedResult


def test_disable_entities_true_rejects_xmlbomb():
    xml = """
    <!DOCTYPE xmlbomb [
        <!ENTITY a "1234567890" >
        <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;">
        <!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;">
    ]>
    <bomb>&c;</bomb>
    """
    with pytest.raises(ValueError, match="entities are disabled"):
        parse(xml, disable_entities=True)


def test_disable_entities_false_returns_xmlbomb():
    xml = """
    <!DOCTYPE xmlbomb [
        <!ENTITY a "1234567890" >
        <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;">
        <!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;">
    ]>
    <bomb>&c;</bomb>
    """
    bomb = "1234567890" * 64
    expectedResult = {'bomb': bomb}
    assert parse(xml, disable_entities=False) == expectedResult


def test_external_entity():
    xml = """
    <!DOCTYPE external [
        <!ENTITY ee SYSTEM "http://www.python.org/">
    ]>
    <root>&ee;</root>
    """
    with pytest.raises(ValueError, match="entities are disabled"):
        parse(xml)
    assert parse(xml, disable_entities=False) == {"root": None}


def test_external_entity_with_custom_expat():
    xml = """
    <!DOCTYPE external [
        <!ENTITY ee SYSTEM "http://www.python.org/">
    ]>
    <root>&ee;</root>
    """

    class CustomExpat:
        def __init__(self, external_entity_result):
            self.external_entity_result = external_entity_result

        def ParserCreate(self, *args, **kwargs):
            parser = ParserCreate(*args, **kwargs)

            def _handler(*args, **kwargs):
                return self.external_entity_result

            parser.ExternalEntityRefHandler = _handler
            return parser

        ExpatError = expat.ExpatError

    with pytest.raises(expat.ExpatError):
        parse(xml, disable_entities=False, expat=CustomExpat(0))
    assert parse(xml, disable_entities=False, expat=CustomExpat(1)) == {"root": None}
    with pytest.raises(ValueError):
        assert parse(xml, disable_entities=True, expat=CustomExpat(1))
    with pytest.raises(ValueError):
        assert parse(xml, disable_entities=True, expat=CustomExpat(0))


def test_disable_entities_true_allows_doctype_without_entities():
    xml = """<?xml version='1.0' encoding='UTF-8'?>
    <!DOCTYPE data SYSTEM "diagram.dtd">
    <foo>bar</foo>
    """
    assert parse(xml, disable_entities=True) == {"foo": "bar"}
    assert parse(xml, disable_entities=False) == {"foo": "bar"}


def test_disable_entities_allows_comments_by_default():
    xml = """
    <a>
        <!-- ignored -->
        <b>1</b>
    </a>
    """
    assert parse(xml) == {'a': {'b': '1'}}


def test_comments():
    xml = """
    <a>
      <b>
        <!-- b comment -->
        <c>
            <!-- c comment -->
            1
        </c>
        <d>2</d>
      </b>
    </a>
    """
    expectedResult = {
        'a': {
            'b': {
                '#comment': 'b comment',
                'c': {

                    '#comment': 'c comment',
                    '#text': '1',
                },
                'd': '2',
            },
        }
    }
    assert parse(xml, process_comments=True) == expectedResult


def test_streaming_with_comments_and_attrs():
    xml = """
    <a>
        <b attr1="value">
            <!-- note -->
            <c>cdata</c>
        </b>
    </a>
    """

    def handler(path, item):
        expected = {
            "@attr1": "value",
            "#comment": "note",
            "c": "cdata",
        }
        assert expected == item
        return True

    parse(xml, item_depth=2, item_callback=handler, process_comments=True)


def test_streaming_memory_usage():
    # Guard against re-introducing accumulation of streamed items into parent
    try:
        import tracemalloc
    except ImportError:
        pytest.skip("tracemalloc not available")

    NUM_ITEMS = 20000

    def xml_gen():
        yield "<a>"
        # generate many children with attribute and text
        for i in range(NUM_ITEMS):
            yield f'<b attr="v">{i % 10}</b>'
        yield "</a>"

    count = 0

    def cb(path, item):
        nonlocal count
        count += 1
        return True

    tracemalloc.start()
    parse(xml_gen(), item_depth=2, item_callback=cb)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert count == NUM_ITEMS
    # Peak memory should remain reasonably bounded; choose a conservative threshold
    # This value should stay well below pathological accumulation levels
    MAX_BYTES = 32 * 1024  # 32 KiB
    assert peak < MAX_BYTES, f"peak memory too high: {peak} bytes"


def test_streaming_attrs():
    xml = """
    <a>
        <b attr1="value">
            <c>cdata</c>
        </b>
    </a>
    """
    def handler(path, item):
        expected = {
            '@attr1': 'value',
            'c': 'cdata'
        }
        assert expected == item
        return True

    parse(xml, item_depth=2, item_callback=handler)


def test_namespace_on_root_without_other_attrs():
    xml = """
    <MyXML xmlns="http://www.xml.org/schemas/Test">
        <Tag1>Text1</Tag1>
        <Tag2 attr2="en">Text2</Tag2>
        <Tag3>Text3</Tag3>
        <Tag4 attr4="en">Text4</Tag4>
    </MyXML>
    """
    namespaces = {
        "http://www.xml.org/schemas/Test": None,
    }
    expected = {
        "MyXML": {
            "@xmlns": {"": "http://www.xml.org/schemas/Test"},
            "Tag1": "Text1",
            "Tag2": {"@attr2": "en", "#text": "Text2"},
            "Tag3": "Text3",
            "Tag4": {"@attr4": "en", "#text": "Text4"},
        }
    }
    assert parse(xml, process_namespaces=True, namespaces=namespaces) == expected


def test_force_list_true_applies_to_all_keys():
    xml = "<a><b>1</b><b>2</b><c>x</c></a>"
    expected = {"a": [{"b": ["1", "2"], "c": ["x"]}]}
    assert parse(xml, force_list=True) == expected

```

### `tox.ini`

```ini
[tox]
envlist = py39, py310, py311, py312, py313, py314, pypy

[gh-actions]
python =
    3.9: py39
    3.10: py310
    3.11: py311
    3.12: py312
    3.13: py313
    3.14: py314
    pypy3.10: pypy
    pypy3.11: pypy

[testenv]
extras = test
commands = pytest --cov=xmltodict

```

### `xmltodict.py`

```py
#!/usr/bin/env python
"Makes working with XML feel like you are working with JSON"

from xml.parsers import expat
from xml.sax.saxutils import XMLGenerator, escape
from xml.sax.xmlreader import AttributesImpl
from io import StringIO
from inspect import isgenerator
import codecs

class ParsingInterrupted(Exception):
    pass


class _DictSAXHandler:
    def __init__(
        self,
        item_depth=0,
        item_callback=lambda *args: True,
        xml_attribs=True,
        attr_prefix="@",
        cdata_key="#text",
        force_cdata=False,
        cdata_separator="",
        postprocessor=None,
        dict_constructor=dict,
        strip_whitespace=True,
        namespace_separator=":",
        namespaces=None,
        force_list=None,
        comment_key="#comment",
    ):
        self.path = []
        self.stack = []
        self.data = []
        self.item = None
        self.item_depth = item_depth
        self.xml_attribs = xml_attribs
        self.item_callback = item_callback
        self.attr_prefix = attr_prefix
        self.cdata_key = cdata_key
        self.force_cdata = force_cdata
        self.cdata_separator = cdata_separator
        self.postprocessor = postprocessor
        self.dict_constructor = dict_constructor
        self.strip_whitespace = strip_whitespace
        self.namespace_separator = namespace_separator
        self.namespaces = namespaces
        self.namespace_declarations = dict_constructor()
        self.force_list = force_list
        self.comment_key = comment_key

    def _build_name(self, full_name):
        if self.namespaces is None:
            return full_name
        i = full_name.rfind(self.namespace_separator)
        if i == -1:
            return full_name
        namespace, name = full_name[:i], full_name[i+1:]
        try:
            short_namespace = self.namespaces[namespace]
        except KeyError:
            short_namespace = namespace
        if not short_namespace:
            return name
        else:
            return self.namespace_separator.join((short_namespace, name))

    def _attrs_to_dict(self, attrs):
        if isinstance(attrs, dict):
            return attrs
        return self.dict_constructor(zip(attrs[0::2], attrs[1::2]))

    def startNamespaceDecl(self, prefix, uri):
        self.namespace_declarations[prefix or ''] = uri

    def startElement(self, full_name, attrs):
        name = self._build_name(full_name)
        attrs = self._attrs_to_dict(attrs)
        if self.namespace_declarations:
            if not attrs:
                attrs = self.dict_constructor()
            attrs['xmlns'] = self.namespace_declarations
            self.namespace_declarations = self.dict_constructor()
        self.path.append((name, attrs or None))
        if len(self.path) >= self.item_depth:
            self.stack.append((self.item, self.data))
            if self.xml_attribs:
                attr_entries = []
                for key, value in attrs.items():
                    key = self.attr_prefix+self._build_name(key)
                    if self.postprocessor:
                        entry = self.postprocessor(self.path, key, value)
                    else:
                        entry = (key, value)
                    if entry:
                        attr_entries.append(entry)
                attrs = self.dict_constructor(attr_entries)
            else:
                attrs = None
            self.item = attrs or None
            self.data = []

    def endElement(self, full_name):
        name = self._build_name(full_name)
        # If we just closed an item at the streaming depth, emit it and drop it
        # without attaching it back to its parent. This avoids accumulating all
        # streamed items in memory when using item_depth > 0.
        if len(self.path) == self.item_depth:
            data = (None if not self.data
                    else self.cdata_separator.join(self.data))
            item = self.item
            if self.strip_whitespace and data:
                data = data.strip() or None
            if data and self._should_force_cdata(name, data) and item is None:
                item = self.dict_constructor()
            if item is not None:
                if data:
                    self.push_data(item, self.cdata_key, data)
            else:
                item = data

            should_continue = self.item_callback(self.path, item)
            if not should_continue:
                raise ParsingInterrupted
            # Reset state for the parent context without keeping a reference to
            # the emitted item.
            if self.stack:
                self.item, self.data = self.stack.pop()
            else:
                self.item = None
                self.data = []
            self.path.pop()
            return
        if self.stack:
            data = (None if not self.data
                    else self.cdata_separator.join(self.data))
            item = self.item
            self.item, self.data = self.stack.pop()
            if self.strip_whitespace and data:
                data = data.strip() or None
            if data and self._should_force_cdata(name, data) and item is None:
                item = self.dict_constructor()
            if item is not None:
                if data:
                    self.push_data(item, self.cdata_key, data)
                self.item = self.push_data(self.item, name, item)
            else:
                self.item = self.push_data(self.item, name, data)
        else:
            self.item = None
            self.data = []
        self.path.pop()

    def characters(self, data):
        if not self.data:
            self.data = [data]
        else:
            self.data.append(data)

    def comments(self, data):
        if self.strip_whitespace:
            data = data.strip()
        self.item = self.push_data(self.item, self.comment_key, data)

    def push_data(self, item, key, data):
        if self.postprocessor is not None:
            result = self.postprocessor(self.path, key, data)
            if result is None:
                return item
            key, data = result
        if item is None:
            item = self.dict_constructor()
        try:
            value = item[key]
            if isinstance(value, list):
                value.append(data)
            else:
                item[key] = [value, data]
        except KeyError:
            if self._should_force_list(key, data):
                item[key] = [data]
            else:
                item[key] = data
        return item

    def _should_force_list(self, key, value):
        if not self.force_list:
            return False
        if isinstance(self.force_list, bool):
            return self.force_list
        try:
            return key in self.force_list
        except TypeError:
            return self.force_list(self.path[:-1], key, value)

    def _should_force_cdata(self, key, value):
        if not self.force_cdata:
            return False
        if isinstance(self.force_cdata, bool):
            return self.force_cdata
        try:
            return key in self.force_cdata
        except TypeError:
            return self.force_cdata(self.path[:-1], key, value)


def parse(xml_input, encoding=None, expat=expat, process_namespaces=False,
          namespace_separator=':', disable_entities=True, process_comments=False, **kwargs):
    """Parse the given XML input and convert it into a dictionary.

    `xml_input` can either be a `string`, a file-like object, or a generator of strings.

    If `xml_attribs` is `True`, element attributes are put in the dictionary
    among regular child elements, using `@` as a prefix to avoid collisions. If
    set to `False`, they are just ignored.

    Simple example::

        >>> import xmltodict
        >>> doc = xmltodict.parse(\"\"\"
        ... <a prop="x">
        ...   <b>1</b>
        ...   <b>2</b>
        ... </a>
        ... \"\"\")
        >>> doc['a']['@prop']
        'x'
        >>> doc['a']['b']
        ['1', '2']

    If `item_depth` is `0`, the function returns a dictionary for the root
    element (default behavior). Otherwise, it calls `item_callback` every time
    an item at the specified depth is found and returns `None` in the end
    (streaming mode).

    The callback function receives two parameters: the `path` from the document
    root to the item (name-attribs pairs), and the `item` (dict). If the
    callback's return value is false-ish, parsing will be stopped with the
    :class:`ParsingInterrupted` exception.

    Streaming example::

        >>> def handle(path, item):
        ...     print('path:%s item:%s' % (path, item))
        ...     return True
        ...
        >>> xmltodict.parse(\"\"\"
        ... <a prop="x">
        ...   <b>1</b>
        ...   <b>2</b>
        ... </a>\"\"\", item_depth=2, item_callback=handle)
        path:[('a', {'prop': 'x'}), ('b', None)] item:1
        path:[('a', {'prop': 'x'}), ('b', None)] item:2

    The optional argument `postprocessor` is a function that takes `path`,
    `key` and `value` as positional arguments and returns a new `(key, value)`
    pair where both `key` and `value` may have changed. Usage example::

        >>> def postprocessor(path, key, value):
        ...     try:
        ...         return key + ':int', int(value)
        ...     except (ValueError, TypeError):
        ...         return key, value
        >>> xmltodict.parse('<a><b>1</b><b>2</b><b>x</b></a>',
        ...                 postprocessor=postprocessor)
        {'a': {'b:int': [1, 2], 'b': 'x'}}

    You can pass an alternate version of `expat` (such as `defusedexpat`) by
    using the `expat` parameter. E.g:

        >>> import defusedexpat
        >>> xmltodict.parse('<a>hello</a>', expat=defusedexpat.pyexpat)
        {'a': 'hello'}

    You can use the force_list argument to force lists to be created even
    when there is only a single child of a given level of hierarchy. The
    force_list argument is a tuple of keys. If the key for a given level
    of hierarchy is in the force_list argument, that level of hierarchy
    will have a list as a child (even if there is only one sub-element).
    The index_keys operation takes precedence over this. This is applied
    after any user-supplied postprocessor has already run.

        For example, given this input:
        <servers>
          <server>
            <name>host1</name>
            <os>Linux</os>
            <interfaces>
              <interface>
                <name>em0</name>
                <ip_address>10.0.0.1</ip_address>
              </interface>
            </interfaces>
          </server>
        </servers>

        If called with force_list=('interface',), it will produce
        this dictionary:
        {'servers':
          {'server':
            {'name': 'host1',
             'os': 'Linux'},
             'interfaces':
              {'interface':
                [ {'name': 'em0', 'ip_address': '10.0.0.1' } ] } } }

        `force_list` can also be a callable that receives `path`, `key` and
        `value`. This is helpful in cases where the logic that decides whether
        a list should be forced is more complex.


        If `process_comments` is `True`, comments will be added using `comment_key`
        (default=`'#comment'`) to the tag that contains the comment.

            For example, given this input:
            <a>
              <b>
                <!-- b comment -->
                <c>
                    <!-- c comment -->
                    1
                </c>
                <d>2</d>
              </b>
            </a>

            If called with `process_comments=True`, it will produce
            this dictionary:
            'a': {
                'b': {
                    '#comment': 'b comment',
                    'c': {

                        '#comment': 'c comment',
                        '#text': '1',
                    },
                    'd': '2',
                },
            }
        Comment text is subject to the `strip_whitespace` flag: when it is left
        at the default `True`, comments will have leading and trailing
        whitespace removed. Disable `strip_whitespace` to keep comment
        indentation or padding intact.
    """
    handler = _DictSAXHandler(namespace_separator=namespace_separator,
                              **kwargs)
    if isinstance(xml_input, str):
        encoding = encoding or 'utf-8'
        xml_input = xml_input.encode(encoding)
    if not process_namespaces:
        namespace_separator = None
    parser = expat.ParserCreate(
        encoding,
        namespace_separator
    )
    parser.ordered_attributes = True
    parser.StartNamespaceDeclHandler = handler.startNamespaceDecl
    parser.StartElementHandler = handler.startElement
    parser.EndElementHandler = handler.endElement
    parser.CharacterDataHandler = handler.characters
    if process_comments:
        parser.CommentHandler = handler.comments
    parser.buffer_text = True
    if disable_entities:
        def _forbid_entities(*_args, **_kwargs):
            raise ValueError("entities are disabled")

        parser.EntityDeclHandler = _forbid_entities
    if hasattr(xml_input, 'read'):
        parser.ParseFile(xml_input)
    elif isgenerator(xml_input):
        for chunk in xml_input:
            parser.Parse(chunk, False)
        parser.Parse(b'', True)
    else:
        parser.Parse(xml_input, True)
    return handler.item


def _convert_value_to_string(value, encoding='utf-8', bytes_errors='replace'):
    """Convert a value to its string representation for XML output.

    Handles boolean values consistently by converting them to lowercase.
    """
    if isinstance(value, str):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (bytes, bytearray, memoryview)):
        return bytes(value).decode(encoding, errors=bytes_errors)
    return str(value)


def _validate_name(value, kind):
    """Validate an element/attribute name for XML safety.

    Raises ValueError with a specific reason when invalid.

    kind: 'element' or 'attribute' (used in error messages)
    """
    if not isinstance(value, str):
        raise ValueError(f"{kind} name must be a string")
    if value.startswith("?") or value.startswith("!"):
        raise ValueError(f'Invalid {kind} name: cannot start with "?" or "!"')
    if "<" in value or ">" in value:
        raise ValueError(f'Invalid {kind} name: "<" or ">" not allowed')
    if "/" in value:
        raise ValueError(f'Invalid {kind} name: "/" not allowed')
    if '"' in value or "'" in value:
        raise ValueError(f"Invalid {kind} name: quotes not allowed")
    if "=" in value:
        raise ValueError(f'Invalid {kind} name: "=" not allowed')
    if any(ch.isspace() for ch in value):
        raise ValueError(f"Invalid {kind} name: whitespace not allowed")


def _validate_comment(value):
    if isinstance(value, bytes):
        try:
            value = value.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("Comment text must be valid UTF-8") from exc
    if not isinstance(value, str):
        raise ValueError("Comment text must be a string")
    if "--" in value:
        raise ValueError("Comment text cannot contain '--'")
    if value.endswith("-"):
        raise ValueError("Comment text cannot end with '-'")
    return value


def _process_namespace(name, namespaces, ns_sep=':', attr_prefix='@'):
    if not isinstance(name, str):
        return name
    if not namespaces:
        return name
    try:
        ns, name = name.rsplit(ns_sep, 1)
    except ValueError:
        pass
    else:
        ns_res = namespaces.get(ns.strip(attr_prefix))
        name = '{}{}{}{}'.format(
            attr_prefix if ns.startswith(attr_prefix) else '',
            ns_res, ns_sep, name) if ns_res else name
    return name


def _emit(key, value, content_handler,
          attr_prefix='@',
          cdata_key='#text',
          depth=0,
          preprocessor=None,
          pretty=False,
          newl='\n',
          indent='\t',
          namespace_separator=':',
          namespaces=None,
          full_document=True,
          expand_iter=None,
          encoding='utf-8',
          bytes_errors='replace',
          comment_key='#comment'):
    if isinstance(key, str) and key == comment_key:
        comments_list = value if isinstance(value, list) else [value]
        if isinstance(indent, int):
            indent = " " * indent
        for comment_text in comments_list:
            if comment_text is None:
                continue
            comment_text = _convert_value_to_string(
                comment_text, encoding=encoding, bytes_errors=bytes_errors
            )
            if not comment_text:
                continue
            if pretty:
                content_handler.ignorableWhitespace(depth * indent)
            content_handler.comment(comment_text)
            if pretty:
                content_handler.ignorableWhitespace(newl)
        return

    key = _process_namespace(key, namespaces, namespace_separator, attr_prefix)
    if preprocessor is not None:
        result = preprocessor(key, value)
        if result is None:
            return
        key, value = result
    # Minimal validation to avoid breaking out of tag context
    _validate_name(key, "element")
    if not hasattr(value, '__iter__') or isinstance(value, (str, bytes, bytearray, memoryview, dict)):
        value = [value]
    for index, v in enumerate(value):
        if full_document and depth == 0 and index > 0:
            raise ValueError('document with multiple roots')
        if v is None:
            v = {}
        elif not isinstance(v, (dict, str)):
            if expand_iter and hasattr(v, '__iter__') and not isinstance(v, (bytes, bytearray, memoryview)):
                v = {expand_iter: v}
            else:
                v = _convert_value_to_string(v, encoding=encoding, bytes_errors=bytes_errors)
        if isinstance(v, str):
            v = {cdata_key: v}
        cdata = None
        attrs = {}
        children = []
        for ik, iv in v.items():
            if ik == cdata_key:
                if iv is None:
                    cdata = None
                else:
                    cdata = _convert_value_to_string(iv, encoding=encoding, bytes_errors=bytes_errors)
                continue
            if isinstance(ik, str) and ik.startswith(attr_prefix):
                ik = _process_namespace(ik, namespaces, namespace_separator,
                                        attr_prefix)
                if ik == attr_prefix + 'xmlns' and isinstance(iv, dict):
                    for k, v in iv.items():
                        _validate_name(k, "attribute")
                        attr = 'xmlns{}'.format(f':{k}' if k else '')
                        attrs[attr] = '' if v is None else _convert_value_to_string(
                            v, encoding=encoding, bytes_errors=bytes_errors
                        )
                    continue
                if iv is None:
                    iv = ''
                elif not isinstance(iv, str):
                    iv = _convert_value_to_string(iv, encoding=encoding, bytes_errors=bytes_errors)
                attr_name = ik[len(attr_prefix) :]
                _validate_name(attr_name, "attribute")
                attrs[attr_name] = iv
                continue
            if isinstance(iv, list) and not iv:
                continue # Skip empty lists to avoid creating empty child elements
            children.append((ik, iv))
        if isinstance(indent, int):
            indent = ' ' * indent
        if pretty:
            content_handler.ignorableWhitespace(depth * indent)
        content_handler.startElement(key, AttributesImpl(attrs))
        if pretty and children:
            content_handler.ignorableWhitespace(newl)
        for child_key, child_value in children:
            _emit(child_key, child_value, content_handler,
                  attr_prefix, cdata_key, depth+1, preprocessor,
                  pretty, newl, indent, namespaces=namespaces,
                  namespace_separator=namespace_separator,
                  expand_iter=expand_iter, encoding=encoding,
                  bytes_errors=bytes_errors, comment_key=comment_key)
        if cdata is not None:
            content_handler.characters(cdata)
        if pretty and children:
            content_handler.ignorableWhitespace(depth * indent)
        content_handler.endElement(key)
        if pretty and depth:
            content_handler.ignorableWhitespace(newl)


class _XMLGenerator(XMLGenerator):
    def comment(self, text):
        text = _validate_comment(text)
        self._write(f"<!--{escape(text)}-->")


def unparse(input_dict, output=None, encoding='utf-8', full_document=True,
            short_empty_elements=False, comment_key='#comment',
            **kwargs):
    """Emit an XML document for the given `input_dict` (reverse of `parse`).

    The resulting XML document is returned as a string, but if `output` (a
    file-like object) is specified, it is written there instead.

    Dictionary keys prefixed with `attr_prefix` (default=`'@'`) are interpreted
    as XML node attributes, whereas keys equal to `cdata_key`
    (default=`'#text'`) are treated as character data.

    Empty lists are omitted entirely: ``{"a": []}`` produces no ``<a>`` element.
    Provide a placeholder entry (for example ``{"a": [""]}``) when an explicit
    empty container element must be emitted.

    The `pretty` parameter (default=`False`) enables pretty-printing. In this
    mode, lines are terminated with `'\n'` and indented with `'\t'`, but this
    can be customized with the `newl` and `indent` parameters.
    The `bytes_errors` parameter controls decoding errors for byte values and
    defaults to `'replace'`.

    """
    bytes_errors = kwargs.pop('bytes_errors', 'replace')
    try:
        codecs.lookup_error(bytes_errors)
    except LookupError as exc:
        raise ValueError(f"Invalid bytes_errors handler: {bytes_errors}") from exc

    must_return = False
    if output is None:
        output = StringIO()
        must_return = True
    if short_empty_elements:
        content_handler = _XMLGenerator(output, encoding, True)
    else:
        content_handler = _XMLGenerator(output, encoding)
    if full_document:
        content_handler.startDocument()
    seen_root = False
    for key, value in input_dict.items():
        if key != comment_key and full_document and seen_root:
            raise ValueError("Document must have exactly one root.")
        _emit(
            key,
            value,
            content_handler,
            full_document=full_document,
            encoding=encoding,
            bytes_errors=bytes_errors,
            comment_key=comment_key,
            **kwargs,
        )
        if key != comment_key:
            seen_root = True
    if full_document and not seen_root:
        raise ValueError("Document must have exactly one root.")
    if full_document:
        content_handler.endDocument()
    if must_return:
        value = output.getvalue()
        try:  # pragma no cover
            value = value.decode(encoding)
        except AttributeError:  # pragma no cover
            pass
        return value


if __name__ == '__main__':  # pragma: no cover
    import marshal
    import sys

    stdin = sys.stdin.buffer
    stdout = sys.stdout.buffer

    (item_depth,) = sys.argv[1:]
    item_depth = int(item_depth)

    def handle_item(path, item):
        marshal.dump((path, item), stdout)
        return True

    try:
        root = parse(stdin,
                     item_depth=item_depth,
                     item_callback=handle_item,
                     dict_constructor=dict)
        if item_depth == 0:
            handle_item([], root)
    except KeyboardInterrupt:
        pass

```
