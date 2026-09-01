# simonw/sqlite-utils@main

- Files included: 103
- Files skipped: 4
- Total size: 849.8 KB
- Estimated tokens: ~217,519

## Directory Structure

```
├── .github
│   ├── actions
│   │   └── setup-sqlite-version
│   │       ├── action.yml
│   │       └── setup-sqlite-version.sh
│   ├── workflows
│   │   ├── codeql-analysis.yml
│   │   ├── documentation-links.yml
│   │   ├── publish.yml
│   │   ├── spellcheck.yml
│   │   ├── test-coverage.yml
│   │   ├── test-sqlite-support.yml
│   │   └── test.yml
│   └── FUNDING.yml
├── docs
│   ├── _static
│   │   └── js
│   │       └── custom.js
│   ├── _templates
│   │   └── base.html
│   ├── .gitignore
│   ├── changelog.rst
│   ├── cli-reference.rst
│   ├── cli.rst
│   ├── codespell-ignore-words.txt
│   ├── conf.py
│   ├── contributing.rst
│   ├── index.rst
│   ├── installation.rst
│   ├── Makefile
│   ├── migrations.rst
│   ├── plugins.rst
│   ├── python-api.rst
│   ├── reference.rst
│   ├── tutorial.ipynb
│   └── upgrading.rst
├── sqlite_utils
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── create_table_parser.py
│   ├── db.py
│   ├── hookspecs.py
│   ├── migrations.py
│   ├── plugins.py
│   ├── py.typed
│   ├── recipes.py
│   └── utils.py
├── tests
│   ├── sniff
│   │   ├── example1.csv
│   │   ├── example2.csv
│   │   ├── example3.csv
│   │   └── example4.csv
│   ├── __init__.py
│   ├── conftest.py
│   ├── ext.c
│   ├── test_analyze_tables.py
│   ├── test_analyze.py
│   ├── test_atomic.py
│   ├── test_attach.py
│   ├── test_cli_bulk.py
│   ├── test_cli_convert.py
│   ├── test_cli_insert.py
│   ├── test_cli_memory.py
│   ├── test_cli_migrate.py
│   ├── test_cli.py
│   ├── test_column_affinity.py
│   ├── test_column_casing.py
│   ├── test_constructor.py
│   ├── test_conversions.py
│   ├── test_convert.py
│   ├── test_create_table_parser.py
│   ├── test_create_view.py
│   ├── test_create.py
│   ├── test_default_value.py
│   ├── test_delete.py
│   ├── test_docs.py
│   ├── test_duplicate.py
│   ├── test_enable_counts.py
│   ├── test_extract.py
│   ├── test_extracts.py
│   ├── test_foreign_keys.py
│   ├── test_fts.py
│   ├── test_get.py
│   ├── test_gis.py
│   ├── test_hypothesis.py
│   ├── test_insert_files.py
│   ├── test_introspect.py
│   ├── test_list_mode.py
│   ├── test_lookup.py
│   ├── test_m2m.py
│   ├── test_migrations.py
│   ├── test_mutator_transactions.py
│   ├── test_plugins.py
│   ├── test_query.py
│   ├── test_recipes.py
│   ├── test_recreate.py
│   ├── test_register_function.py
│   ├── test_rows_from_file.py
│   ├── test_rows.py
│   ├── test_sniff.py
│   ├── test_suggest_column_types.py
│   ├── test_tracer.py
│   ├── test_transform.py
│   ├── test_update.py
│   ├── test_upsert.py
│   ├── test_utils.py
│   └── test_wal.py
├── .gitignore
├── .readthedocs.yaml
├── codecov.yml
├── Justfile
├── LICENSE
├── MANIFEST.in
├── mypy.ini
├── pyproject.toml
└── README.md
```

## Code Digest

### `.github/actions/setup-sqlite-version/action.yml`

```yml
name: "Setup SQLite version"
description: "Build and activate a specific SQLite version from its amalgamation archive"
inputs:
  version:
    description: "The SQLite version to install"
    required: true
  cflags:
    description: "CFLAGS to use when compiling SQLite"
    required: false
    default: ""
  skip-activate:
    description: "Set to true to skip modifying the library path"
    required: false
    default: "false"
  fallback-urls:
    description: "Whitespace-separated fallback download URLs to try after sqlite.org"
    required: false
    default: ""
outputs:
  sqlite-location:
    description: "Directory containing the compiled SQLite library"
    value: ${{ steps.build.outputs.sqlite-location }}
runs:
  using: "composite"
  steps:
    - shell: bash
      run: mkdir -p "$RUNNER_TEMP/sqlite-versions/downloads"
    - uses: actions/cache@v6
      with:
        path: ${{ runner.temp }}/sqlite-versions/downloads
        key: setup-sqlite-version-${{ inputs.version }}-amalgamation-v1
    - id: build
      shell: bash
      run: bash "$GITHUB_ACTION_PATH/setup-sqlite-version.sh"
      env:
        SQLITE_VERSION: ${{ inputs.version }}
        SQLITE_CFLAGS: ${{ inputs.cflags }}
        SQLITE_SKIP_ACTIVATE: ${{ inputs.skip-activate }}
        SQLITE_EXTRA_FALLBACK_URLS: ${{ inputs.fallback-urls }}

```

### `.github/actions/setup-sqlite-version/setup-sqlite-version.sh`

```sh
#!/usr/bin/env bash
set -euo pipefail

version_spec="${SQLITE_VERSION:?SQLITE_VERSION is required}"
cflags="${SQLITE_CFLAGS:-}"
skip_activate="${SQLITE_SKIP_ACTIVATE:-false}"
extra_fallback_urls="${SQLITE_EXTRA_FALLBACK_URLS:-}"

case "$version_spec" in
  3.46 | 3.46.0)
    sqlite_version="3.46.0"
    sqlite_year="2024"
    amalgamation_id="3460000"
    builtin_fallback_urls="https://static.simonwillison.net/static/2026/sqlite-amalgamation-3460000.zip"
    ;;
  3.23.1)
    sqlite_version="3.23.1"
    sqlite_year="2018"
    amalgamation_id="3230100"
    builtin_fallback_urls="https://static.simonwillison.net/static/2026/sqlite-amalgamation-3230100.zip"
    ;;
  *)
    echo "::error::Unsupported SQLite version '$version_spec'. Add its release year and amalgamation id to $GITHUB_ACTION_PATH/setup-sqlite-version.sh."
    exit 1
    ;;
esac

case "$(uname -s)" in
  Linux)
    library_name="libsqlite3.so.0"
    library_path_var="LD_LIBRARY_PATH"
    ;;
  Darwin)
    library_name="libsqlite3.dylib"
    library_path_var="DYLD_LIBRARY_PATH"
    ;;
  *)
    echo "::error::Unsupported platform $(uname -s)"
    exit 1
    ;;
esac

runner_temp="${RUNNER_TEMP:-}"
if [ -z "$runner_temp" ]; then
  runner_temp="$(mktemp -d)"
fi

filename="sqlite-amalgamation-${amalgamation_id}"
official_url="https://www.sqlite.org/${sqlite_year}/${filename}.zip"
download_dir="${runner_temp}/sqlite-versions/downloads"
source_root="${runner_temp}/sqlite-versions/source"
source_dir="${source_root}/${filename}"
build_dir="${runner_temp}/sqlite-versions/build/${sqlite_version}"
archive_path="${download_dir}/${filename}.zip"

mkdir -p "$download_dir" "$source_root" "$build_dir"

download_archive() {
  local url
  local candidate_path="${archive_path}.tmp"
  local urls=("$official_url")

  for url in $builtin_fallback_urls $extra_fallback_urls; do
    urls+=("$url")
  done

  rm -f "$candidate_path"
  for url in "${urls[@]}"; do
    echo "Downloading SQLite ${sqlite_version} amalgamation from ${url}"
    if curl \
      --fail \
      --location \
      --show-error \
      --retry 5 \
      --retry-delay 2 \
      --retry-max-time 180 \
      --retry-all-errors \
      --connect-timeout 20 \
      --max-time 240 \
      --output "$candidate_path" \
      "$url"; then
      mv "$candidate_path" "$archive_path"
      return 0
    fi

    echo "::warning::Download failed from ${url}"
    rm -f "$candidate_path"
  done

  echo "::error::Could not download SQLite ${sqlite_version} amalgamation"
  return 1
}

if [ ! -f "${source_dir}/sqlite3.c" ]; then
  if [ ! -f "$archive_path" ]; then
    download_archive
  fi

  rm -rf "$source_dir"
  unzip -q "$archive_path" -d "$source_root"
fi

if [ ! -f "${source_dir}/sqlite3.c" ]; then
  echo "::error::Expected ${source_dir}/sqlite3.c after extracting ${archive_path}"
  exit 1
fi

read -r -a cflag_args <<< "$cflags"

echo "Compiling SQLite ${sqlite_version} to ${build_dir}/${library_name}"
gcc \
  -fPIC \
  -shared \
  "${cflag_args[@]}" \
  "${source_dir}/sqlite3.c" \
  "-I${source_dir}" \
  -o "${build_dir}/${library_name}"

if [ "$library_name" = "libsqlite3.so.0" ]; then
  ln -sf "$library_name" "${build_dir}/libsqlite3.so"
fi

if [ -n "${GITHUB_OUTPUT:-}" ]; then
  echo "sqlite-location=${build_dir}" >> "$GITHUB_OUTPUT"
else
  echo "sqlite-location=${build_dir}"
fi

case "$(printf '%s' "$skip_activate" | tr '[:upper:]' '[:lower:]')" in
  true | 1 | yes)
    echo "Skipping ${library_path_var} activation"
    ;;
  *)
    existing_value="${!library_path_var:-}"
    if [ -n "${GITHUB_ENV:-}" ]; then
      if [ -n "$existing_value" ]; then
        echo "${library_path_var}=${build_dir}:${existing_value}" >> "$GITHUB_ENV"
      else
        echo "${library_path_var}=${build_dir}" >> "$GITHUB_ENV"
      fi
    fi
    echo "Added ${build_dir} to ${library_path_var}"
    ;;
esac

```

### `.github/FUNDING.yml`

```yml
github: [simonw]

```

### `.github/workflows/codeql-analysis.yml`

```yml
name: "CodeQL"

on:
  push:
    branches: [main]
  schedule:
    - cron: '0 4 * * 5'

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest

    strategy:
      fail-fast: false
      matrix:
        # Override automatic language detection by changing the below list
        # Supported options are ['csharp', 'cpp', 'go', 'java', 'javascript', 'python']
        language: ['python']
        # Learn more...
        # https://docs.github.com/en/github/finding-security-vulnerabilities-and-errors-in-your-code/configuring-code-scanning#overriding-automatic-language-detection

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      with:
        # We must fetch at least the immediate parents so that if this is
        # a pull request then we can checkout the head.
        fetch-depth: 2

    # If this run was triggered by a pull request event, then checkout
    # the head of the pull request instead of the merge commit.
    - run: git checkout HEAD^2
      if: ${{ github.event_name == 'pull_request' }}

    # Initializes the CodeQL tools for scanning.
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v1
      with:
        languages: ${{ matrix.language }}
        # If you wish to specify custom queries, you can do so here or in a config file.
        # By default, queries listed here will override any specified in a config file. 
        # Prefix the list here with "+" to use these queries and those in the config file.
        # queries: ./path/to/local/query, your-org/your-repo/queries@main

    # Autobuild attempts to build any compiled languages  (C/C++, C#, or Java).
    # If this step fails, then you should remove it and run the build manually (see below)
    - name: Autobuild
      uses: github/codeql-action/autobuild@v1

    # ℹ️ Command-line programs to run using the OS shell.
    # 📚 https://git.io/JvXDl

    # ✏️ If the Autobuild fails above, remove it and uncomment the following three lines
    #    and modify them (or add more) to build your code if your project
    #    uses a compiled language

    #- run: |
    #   make bootstrap
    #   make release

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v1

```

### `.github/workflows/documentation-links.yml`

```yml
name: Read the Docs Pull Request Preview
on:
  pull_request_target:
    types:
      - opened

permissions:
  pull-requests: write

jobs:
  documentation-links:
    runs-on: ubuntu-latest
    steps:
      - uses: readthedocs/actions/preview@v1
        with:
          project-slug: "sqlite-utils"

```

### `.github/workflows/publish.yml`

```yml
name: Publish Python Package

on:
  release:
    types: [created]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12", "3.13", "3.14"]
        os: [ubuntu-latest, windows-latest, macos-latest]
    steps:
    - uses: actions/checkout@v7
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v6
      with:
        python-version: ${{ matrix.python-version }}
        cache: pip
        cache-dependency-path: pyproject.toml
    - name: Install dependencies
      run: |
        pip install . --group dev
    - name: Run tests
      run: |
        pytest
  deploy:
    runs-on: ubuntu-latest
    needs: [test]
    steps:
    - uses: actions/checkout@v7
    - name: Set up Python
      uses: actions/setup-python@v6
      with:
        python-version: '3.14'
        cache: pip
        cache-dependency-path: pyproject.toml
    - name: Install dependencies
      run: |
        pip install build twine
    - name: Publish
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_TOKEN }}
      run: |
        python -m build
        twine upload dist/*

```

### `.github/workflows/spellcheck.yml`

```yml
name: Check spelling in documentation

on: [push, pull_request]

jobs:
  spellcheck:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.12"
        cache: pip
        cache-dependency-path: pyproject.toml
    - name: Install dependencies
      run: |
        pip install . --group docs
    - name: Check spelling
      run: |
        codespell docs/*.rst --ignore-words docs/codespell-ignore-words.txt
        codespell sqlite_utils --ignore-words docs/codespell-ignore-words.txt

```

### `.github/workflows/test-coverage.yml`

```yml
name: Calculate test coverage

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - name: Check out repo
      uses: actions/checkout@v7
    - name: Set up Python
      uses: actions/setup-python@v6
      with:
        python-version: "3.11"
        cache: pip
        cache-dependency-path: pyproject.toml
    - name: Install SpatiaLite
      run: sudo apt-get install libsqlite3-mod-spatialite
    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install . --group dev
        python -m pip install pytest-cov
    - name: Run tests
      run: |-
        ls -lah
        pytest --cov=sqlite_utils --cov-report xml:coverage.xml --cov-report term
        ls -lah
    - name: Upload coverage report
      uses: codecov/codecov-action@v1
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
        file: coverage.xml

```

### `.github/workflows/test-sqlite-support.yml`

```yml
name: Test SQLite versions

on: [push, pull_request]

permissions:
  contents: read

jobs:
  test:
    runs-on: ${{ matrix.platform }}
    continue-on-error: true
    strategy:
      matrix:
        platform: [ubuntu-latest]
        python-version: ["3.10"]
        sqlite-version: [
          "3.46",
          "3.23.1", # 2018-04-10, before UPSERT
        ]
    steps:
    - uses: actions/checkout@v7
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v6
      with:
        python-version: ${{ matrix.python-version }}
        allow-prereleases: true
        cache: pip
        cache-dependency-path: pyproject.toml
    - name: Set up SQLite ${{ matrix.sqlite-version }}
      uses: ./.github/actions/setup-sqlite-version
      with:
        version: ${{ matrix.sqlite-version }}
        cflags: "-DSQLITE_ENABLE_DESERIALIZE -DSQLITE_ENABLE_FTS5 -DSQLITE_ENABLE_FTS4 -DSQLITE_ENABLE_FTS3_PARENTHESIS -DSQLITE_ENABLE_RTREE -DSQLITE_ENABLE_JSON1"
    - run: python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - name: Install dependencies
      run: |
        pip install . --group dev
        pip freeze
    - name: Run tests
      run: |
        python -m pytest

```

### `.github/workflows/test.yml`

```yml
name: Test

on: [push, pull_request]

env:
  FORCE_COLOR: 1

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12", "3.13", "3.14", "3.15-dev"]
        numpy: [0, 1]
        os: [ubuntu-latest, macos-latest, windows-latest, macos-14]
    steps:
    - uses: actions/checkout@v7
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v6
      with:
        python-version: ${{ matrix.python-version }}
        allow-prereleases: true
        cache: pip
        cache-dependency-path: pyproject.toml
    - name: Install dependencies
      run: |
        pip install . --group dev
    - name: Optionally install numpy
      if: matrix.numpy == 1
      run: pip install numpy
    - name: Install SpatiaLite
      if: matrix.os == 'ubuntu-latest'
      run: sudo apt-get install libsqlite3-mod-spatialite
    - name: Build extension for --load-extension test
      if: matrix.os == 'ubuntu-latest'
      run: |-
        (cd tests && gcc ext.c -fPIC -shared -o ext.so && ls -lah)
    - name: Run tests
      run: |
        pytest -v
    - name: Run autocommit tests just on 3.14/Ubuntu
      if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.14'
      run: pytest --sqlite-autocommit
    - name: run mypy
      run: mypy sqlite_utils tests
    - name: run pyright regression checks
      if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.14'
      run: pyright sqlite_utils tests
    - name: run flake8
      run: flake8
    - name: run ty
      if: matrix.os != 'windows-latest' && matrix.python-version == '3.14'
      run: |
        pip install uv
        uv run ty check sqlite_utils
    - name: Check no accidental dev= dependencies needed
      if: matrix.os == 'ubuntu-latest'
      run: |
        pip install uv
        uv run --no-default-groups sqlite-utils --help
    - name: Check formatting
      run: black . --check
    - name: Check if cog needs to be run
      run: |
        cog --check --diff README.md docs/*.rst

```

### `.gitignore`

```gitignore
.venv
dist
build
*.db
__pycache__/
*.py[cod]
*$py.class
venv
.eggs
.pytest_cache
*.egg-info
.DS_Store
.mypy_cache
.coverage
.schema
.vscode
.hypothesis
.claude/
Pipfile
Pipfile.lock
uv.lock
tests/*.dylib
tests/*.so
tests/*.dll

```

### `.readthedocs.yaml`

```yaml
version: 2

sphinx:
  configuration: docs/conf.py

build:
  os: ubuntu-24.04
  tools:
    python: "3.13"
  jobs:
    install:
    - pip install --upgrade pip
    - pip install . --group docs

formats:
- pdf
- epub

```

### `codecov.yml`

```yml
coverage:
  status:
    project:
      default:
        informational: true
    patch:
      default:
        informational: true

```

### `docs/_static/js/custom.js`

```js
jQuery(function ($) {
  // Show banner linking to /stable/ if this is a /latest/ page
  if (!/\/latest\//.test(location.pathname)) {
    return;
  }
  var stableUrl = location.pathname.replace("/latest/", "/stable/");
  // Check it's not a 404
  fetch(stableUrl, { method: "HEAD" }).then((response) => {
    if (response.status == 200) {
      var warning = $(
        `<div class="admonition warning">
           <p class="first admonition-title">Note</p>
           <p class="last">
             This documentation covers the <strong>development version</strong> of <code>sqlite-utils</code>.</p>
             <p>See <a href="${stableUrl}">this page</a> for the current stable release.
           </p>
        </div>`
      );
      warning.find("a").attr("href", stableUrl);
      $("article[role=main]").prepend(warning);
    }
  });
});

```

### `docs/_templates/base.html`

```html
{%- extends "!base.html" %}

{% block site_meta %}
{{ super() }}
<script defer data-domain="sqlite-utils.datasette.io" src="https://plausible.io/js/plausible.js"></script>
{% endblock %}

{% block scripts %}
{{ super() }}
<style type="text/css">
.highlight-output .highlight {
  border-left: 9px solid #30c94f;
}
</style>
<script>
document.addEventListener("DOMContentLoaded", function() {
  // Show banner linking to /stable/ if this is a /latest/ page
  if (!/\/latest\//.test(location.pathname)) {
    return;
  }
  var stableUrl = location.pathname.replace("/latest/", "/stable/");
  // Check it's not a 404
  fetch(stableUrl, { method: "HEAD" }).then((response) => {
    if (response.status === 200) {
      var warning = document.createElement("div");
      warning.className = "admonition warning";
      warning.innerHTML = `
        <p class="first admonition-title">Note</p>
        <p class="last">
          This documentation covers the <strong>development version</strong> of Datasette.
        </p>
        <p>
          See <a href="${stableUrl}">this page</a> for the current stable release.
        </p>
      `;
      var mainArticle = document.querySelector("article[role=main]");
      mainArticle.insertBefore(warning, mainArticle.firstChild);
    }
  });
});
</script>
{% endblock %}

```

### `docs/.gitignore`

```gitignore
_build

```

### `docs/cli-reference.rst`

```rst
.. _cli_reference:

===============
 CLI reference
===============

This page lists the ``--help`` for every ``sqlite-utils`` CLI sub-command.

.. contents:: :local:
   :class: this-will-duplicate-information-and-it-is-still-useful-here

.. [[[cog
    from sqlite_utils import cli
    import sys
    sys._called_from_test = True
    from click.testing import CliRunner
    import textwrap
    commands = list(cli.cli.commands.keys())
    go_first = [
        "query", "memory", "insert", "upsert", "bulk", "search", "transform", "extract",
        "schema", "insert-files", "analyze-tables", "convert", "tables", "views", "rows",
        "triggers", "indexes", "create-database", "create-table", "create-index", "drop-index",
        "migrate", "enable-fts", "populate-fts", "rebuild-fts", "disable-fts"
    ]
    refs = {
        "query": "cli_query",
        "memory": "cli_memory",
        "insert": [
            "cli_inserting_data", "cli_insert_csv_tsv", "cli_insert_unstructured", "cli_insert_convert"
        ],
        "upsert": "cli_upsert",
        "tables": "cli_tables",
        "views": "cli_views",
        "optimize": "cli_optimize",
        "rows": "cli_rows",
        "triggers": "cli_triggers",
        "indexes": "cli_indexes",
        "enable-fts": "cli_fts",
        "analyze": "cli_analyze",
        "vacuum": "cli_vacuum",
        "dump": "cli_dump",
        "add-column": "cli_add_column",
        "rename-table": "cli_renaming_tables",
        "duplicate": "cli_duplicate_table",
        "add-foreign-key": "cli_add_foreign_key",
        "add-foreign-keys": "cli_add_foreign_keys",
        "index-foreign-keys": "cli_index_foreign_keys",
        "create-index": "cli_create_index",
        "drop-index": "cli_drop_index",
        "enable-wal": "cli_wal",
        "enable-counts": "cli_enable_counts",
        "bulk": "cli_bulk",
        "migrate": "cli_migrate",
        "create-database": "cli_create_database",
        "create-table": "cli_create_table",
        "drop-table": "cli_drop_table",
        "create-view": "cli_create_view",
        "drop-view": "cli_drop_view",
        "search": "cli_search",
        "transform": "cli_transform_table",
        "extract": "cli_extract",
        "schema": "cli_schema",
        "insert-files": "cli_insert_files",
        "analyze-tables": "cli_analyze_tables",
        "convert": "cli_convert",
        "add-geometry-column": "cli_spatialite",
        "create-spatial-index": "cli_spatialite_indexes",
        "install": "cli_install",
        "uninstall": "cli_uninstall",
    }
    commands.sort(key = lambda command: go_first.index(command) if command in go_first else 999)
    cog.out("\n")
    for command in commands:
        cog.out(".. _cli_ref_" + command.replace("-", "_") + ":\n\n")
        cog.out(command + "\n")
        cog.out(("=" * len(command)) + "\n\n")
        if command in refs:
            command_refs = refs[command]
            if isinstance(command_refs, str):
                command_refs = [command_refs]
            cog.out(
                "See {}.\n\n".format(
                    ", ".join(":ref:`{}`".format(c) for c in command_refs)
                )
            )
        cog.out("::\n\n")
        result = CliRunner().invoke(cli.cli, [command, "--help"])
        output = result.output.replace("Usage: cli ", "Usage: sqlite-utils ")
        output = output.replace('\b', '')
        cog.out(textwrap.indent(output, '    '))
        cog.out("\n\n")
.. ]]]

.. _cli_ref_query:

query
=====

See :ref:`cli_query`.

::

    Usage: sqlite-utils query [OPTIONS] PATH SQL

      Execute SQL query and return the results as JSON

      Example:

          sqlite-utils data.db \
              "select * from chickens where age > :age" \
              -p age 1

      Pass "-" as the SQL to read the query from standard input:

          echo "select * from chickens" | sqlite-utils data.db -

    Options:
      --attach <TEXT FILE>...     Additional databases to attach - specify alias and
                                  filepath
      --nl                        Output newline-delimited JSON
      --arrays                    Output rows as arrays instead of objects
      --csv                       Output CSV
      --tsv                       Output TSV
      --no-headers                Omit headers from CSV/TSV and table/--fmt output
      -t, --table                 Output as a formatted table
      --fmt TEXT                  Table format - one of asciidoc, colon_grid,
                                  double_grid, double_outline, fancy_grid,
                                  fancy_outline, github, grid, heavy_grid,
                                  heavy_outline, html, jira, latex, latex_booktabs,
                                  latex_longtable, latex_raw, mediawiki, mixed_grid,
                                  mixed_outline, moinmoin, orgtbl, outline, pipe,
                                  plain, presto, pretty, psql, rounded_grid,
                                  rounded_outline, rst, simple, simple_grid,
                                  simple_outline, textile, tsv, unsafehtml, youtrack
      --json-cols                 Detect JSON cols and output them as JSON, not
                                  escaped strings
      --ascii                     Escape non-ASCII characters in JSON output as
                                  \uXXXX
      -r, --raw                   Raw output, first column of first row
      --raw-lines                 Raw output, first column of each row
      -p, --param <TEXT TEXT>...  Named :parameters for SQL query
      --functions TEXT            Python code or a file path defining custom SQL
                                  functions; can be used multiple times
      --load-extension TEXT       Path to SQLite extension, with optional
                                  :entrypoint
      -h, --help                  Show this message and exit.


.. _cli_ref_memory:

memory
======

See :ref:`cli_memory`.

::

    Usage: sqlite-utils memory [OPTIONS] [PATHS]... SQL

      Execute SQL query against an in-memory database, optionally populated by
      imported data

      To import data from CSV, TSV or JSON files pass them on the command-line:

          sqlite-utils memory one.csv two.json \
              "select * from one join two on one.two_id = two.id"

      For data piped into the tool from standard input, use "-" or "stdin":

          cat animals.csv | sqlite-utils memory - \
              "select * from stdin where species = 'dog'"

      The format of the data will be automatically detected. You can specify the
      format explicitly using :json, :csv, :tsv or :nl (for newline-delimited JSON)
      - for example:

          cat animals.csv | sqlite-utils memory stdin:csv places.dat:nl \
              "select * from stdin where place_id in (select id from places)"

      Use --schema to view the SQL schema of any imported files:

          sqlite-utils memory animals.csv --schema

    Options:
      --functions TEXT            Python code or a file path defining custom SQL
                                  functions; can be used multiple times
      --attach <TEXT FILE>...     Additional databases to attach - specify alias and
                                  filepath
      --flatten                   Flatten nested JSON objects, so {"foo": {"bar":
                                  1}} becomes {"foo_bar": 1}
      --nl                        Output newline-delimited JSON
      --arrays                    Output rows as arrays instead of objects
      --csv                       Output CSV
      --tsv                       Output TSV
      --no-headers                Omit headers from CSV/TSV and table/--fmt output
      -t, --table                 Output as a formatted table
      --fmt TEXT                  Table format - one of asciidoc, colon_grid,
                                  double_grid, double_outline, fancy_grid,
                                  fancy_outline, github, grid, heavy_grid,
                                  heavy_outline, html, jira, latex, latex_booktabs,
                                  latex_longtable, latex_raw, mediawiki, mixed_grid,
                                  mixed_outline, moinmoin, orgtbl, outline, pipe,
                                  plain, presto, pretty, psql, rounded_grid,
                                  rounded_outline, rst, simple, simple_grid,
                                  simple_outline, textile, tsv, unsafehtml, youtrack
      --json-cols                 Detect JSON cols and output them as JSON, not
                                  escaped strings
      --ascii                     Escape non-ASCII characters in JSON output as
                                  \uXXXX
      -r, --raw                   Raw output, first column of first row
      --raw-lines                 Raw output, first column of each row
      -p, --param <TEXT TEXT>...  Named :parameters for SQL query
      --encoding TEXT             Character encoding for CSV input, defaults to
                                  utf-8
      -n, --no-detect-types       Treat all CSV/TSV columns as TEXT
      --schema                    Show SQL schema for in-memory database
      --dump                      Dump SQL for in-memory database
      --save FILE                 Save in-memory database to this file
      --analyze                   Analyze resulting tables and output results
      --load-extension TEXT       Path to SQLite extension, with optional
                                  :entrypoint
      -h, --help                  Show this message and exit.


.. _cli_ref_insert:

insert
======

See :ref:`cli_inserting_data`, :ref:`cli_insert_csv_tsv`, :ref:`cli_insert_unstructured`, :ref:`cli_insert_convert`.

::

    Usage: sqlite-utils insert [OPTIONS] PATH TABLE [FILE]

      Insert records from FILE into a table, creating the table if it does not
      already exist.

      Example:

          echo '{"name": "Lila"}' | sqlite-utils insert data.db chickens -

      By default the input is expected to be a JSON object or array of objects.

      - Use --nl for newline-delimited JSON objects
      - Use --csv or --tsv for comma-separated or tab-separated input
      - Use --lines to write each incoming line to a column called "line"
      - Use --text to write the entire input to a column called "text"

      Use --type column-name type to override the type automatically chosen when the
      table is created.

      You can also use --convert to pass a fragment of Python code that will be used
      to convert each input.

      Your Python code will be passed a "row" variable representing the imported
      row, and can return a modified row.

      This example uses just the name, latitude and longitude columns from a CSV
      file, converting name to upper case and latitude and longitude to floating
      point numbers:

          sqlite-utils insert plants.db plants plants.csv --csv --convert '
            return {
              "name": row["name"].upper(),
              "latitude": float(row["latitude"]),
              "longitude": float(row["longitude"]),
            }'

      If you are using --lines your code will be passed a "line" variable, and for
      --text a "text" variable.

      When using --text your function can return an iterator of rows to insert. This
      example inserts one record per word in the input:

          echo 'A bunch of words' | sqlite-utils insert words.db words - \
            --text --convert '({"word": w} for w in text.split())'

      Instead of a FILE you can use --code to provide a block of Python code that
      defines the rows to insert, as either a rows() function that yields
      dictionaries or a "rows" iterable. --code can also be a path to a .py file:

          sqlite-utils insert data.db creatures --code '
          def rows():
              yield {"id": 1, "name": "Cleo"}
              yield {"id": 2, "name": "Suna"}
          ' --pk id

    Options:
      --pk TEXT                 Columns to use as the primary key, e.g. id
      --code TEXT               Python code defining a rows() function or iterable
                                of rows to insert
      --flatten                 Flatten nested JSON objects, so {"a": {"b": 1}}
                                becomes {"a_b": 1}
      --nl                      Expect newline-delimited JSON
      -c, --csv                 Expect CSV input
      --tsv                     Expect TSV input
      --empty-null              Treat empty strings as NULL
      --lines                   Treat each line as a single value called 'line'
      --text                    Treat input as a single value called 'text'
      --convert TEXT            Python code to convert each item
      --import TEXT             Python modules to import
      --delimiter TEXT          Delimiter to use for CSV files
      --quotechar TEXT          Quote character to use for CSV/TSV
      --sniff                   Detect delimiter and quote character
      --no-headers              CSV file has no header row
      --encoding TEXT           Character encoding for input, defaults to utf-8
      --batch-size INTEGER      Commit every X records
      --stop-after INTEGER      Stop after X records
      --alter                   Alter existing table to add any missing columns
      --not-null TEXT           Columns that should be created as NOT NULL
      --default <TEXT TEXT>...  Default value that should be set for a column
      --type <TEXT CHOICE>...   Column types to use when creating the table
      --no-detect-types         Treat all CSV/TSV columns as TEXT
      --analyze                 Run ANALYZE at the end of this operation
      --load-extension TEXT     Path to SQLite extension, with optional :entrypoint
      --silent                  Do not show progress bar
      --strict                  Apply STRICT mode to created table
      --ignore                  Ignore records if pk already exists
      --replace                 Replace records if pk already exists
      --truncate                Truncate table before inserting records, if table
                                already exists
      -h, --help                Show this message and exit.


.. _cli_ref_upsert:

upsert
======

See :ref:`cli_upsert`.

::

    Usage: sqlite-utils upsert [OPTIONS] PATH TABLE [FILE]

      Upsert records based on their primary key. Works like 'insert' but if an
      incoming record has a primary key that matches an existing record the existing
      record will be updated.

      If the table already exists and has a primary key, --pk can be omitted.

      Use --type column-name type to override the type automatically chosen when the
      table is created.

      Example:

          echo '[
              {"id": 1, "name": "Lila"},
              {"id": 2, "name": "Suna"}
          ]' | sqlite-utils upsert data.db chickens - --pk id

    Options:
      --pk TEXT                 Columns to use as the primary key, e.g. id
      --code TEXT               Python code defining a rows() function or iterable
                                of rows to insert
      --flatten                 Flatten nested JSON objects, so {"a": {"b": 1}}
                                becomes {"a_b": 1}
      --nl                      Expect newline-delimited JSON
      -c, --csv                 Expect CSV input
      --tsv                     Expect TSV input
      --empty-null              Treat empty strings as NULL
      --lines                   Treat each line as a single value called 'line'
      --text                    Treat input as a single value called 'text'
      --convert TEXT            Python code to convert each item
      --import TEXT             Python modules to import
      --delimiter TEXT          Delimiter to use for CSV files
      --quotechar TEXT          Quote character to use for CSV/TSV
      --sniff                   Detect delimiter and quote character
      --no-headers              CSV file has no header row
      --encoding TEXT           Character encoding for input, defaults to utf-8
      --batch-size INTEGER      Commit every X records
      --stop-after INTEGER      Stop after X records
      --alter                   Alter existing table to add any missing columns
      --not-null TEXT           Columns that should be created as NOT NULL
      --default <TEXT TEXT>...  Default value that should be set for a column
      --type <TEXT CHOICE>...   Column types to use when creating the table
      --no-detect-types         Treat all CSV/TSV columns as TEXT
      --analyze                 Run ANALYZE at the end of this operation
      --load-extension TEXT     Path to SQLite extension, with optional :entrypoint
      --silent                  Do not show progress bar
      --strict                  Apply STRICT mode to created table
      -h, --help                Show this message and exit.


.. _cli_ref_bulk:

bulk
====

See :ref:`cli_bulk`.

::

    Usage: sqlite-utils bulk [OPTIONS] PATH SQL FILE

      Execute parameterized SQL against the provided list of documents.

      Example:

          echo '[
              {"id": 1, "name": "Lila2"},
              {"id": 2, "name": "Suna2"}
          ]' | sqlite-utils bulk data.db '
              update chickens set name = :name where id = :id
          ' -

    Options:
      --batch-size INTEGER   Commit every X records
      --functions TEXT       Python code or a file path defining custom SQL
                             functions; can be used multiple times
      --flatten              Flatten nested JSON objects, so {"a": {"b": 1}} becomes
                             {"a_b": 1}
      --nl                   Expect newline-delimited JSON
      -c, --csv              Expect CSV input
      --tsv                  Expect TSV input
      --empty-null           Treat empty strings as NULL
      --lines                Treat each line as a single value called 'line'
      --text                 Treat input as a single value called 'text'
      --convert TEXT         Python code to convert each item
      --import TEXT          Python modules to import
      --delimiter TEXT       Delimiter to use for CSV files
      --quotechar TEXT       Quote character to use for CSV/TSV
      --sniff                Detect delimiter and quote character
      --no-headers           CSV file has no header row
      --encoding TEXT        Character encoding for input, defaults to utf-8
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_search:

search
======

See :ref:`cli_search`.

::

    Usage: sqlite-utils search [OPTIONS] PATH DBTABLE Q

      Execute a full-text search against this table

      Example:

          sqlite-utils search data.db chickens lila

    Options:
      -o, --order TEXT       Order by ('column' or 'column desc')
      -c, --column TEXT      Columns to return
      --limit INTEGER        Number of rows to return - defaults to everything
      --sql                  Show SQL query that would be run
      --quote                Apply FTS quoting rules to search term
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit headers from CSV/TSV and table/--fmt output
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, colon_grid,
                             double_grid, double_outline, fancy_grid, fancy_outline,
                             github, grid, heavy_grid, heavy_outline, html, jira,
                             latex, latex_booktabs, latex_longtable, latex_raw,
                             mediawiki, mixed_grid, mixed_outline, moinmoin, orgtbl,
                             outline, pipe, plain, presto, pretty, psql,
                             rounded_grid, rounded_outline, rst, simple,
                             simple_grid, simple_outline, textile, tsv, unsafehtml,
                             youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --ascii                Escape non-ASCII characters in JSON output as \uXXXX
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_transform:

transform
=========

See :ref:`cli_transform_table`.

::

    Usage: sqlite-utils transform [OPTIONS] PATH TABLE

      Transform a table beyond the capabilities of ALTER TABLE

      Example:

          sqlite-utils transform mydb.db mytable \
              --drop column1 \
              --rename column2 column_renamed

    Options:
      --type <TEXT CHOICE>...         Change column type to INTEGER, TEXT, FLOAT,
                                      REAL, BLOB or ANY
      --drop TEXT                     Drop this column
      --rename <TEXT TEXT>...         Rename this column to X
      -o, --column-order TEXT         Reorder columns
      --not-null TEXT                 Set this column to NOT NULL
      --not-null-false TEXT           Remove NOT NULL from this column
      --pk TEXT                       Make this column the primary key
      --pk-none                       Remove primary key (convert to rowid table)
      --default <TEXT TEXT>...        Set default value for this column
      --default-none TEXT             Remove default from this column
      --add-foreign-key <TEXT TEXT TEXT>...
                                      Add a foreign key constraint from a column to
                                      another table with another column
      --drop-foreign-key TEXT         Drop foreign key constraint for this column
      --strict / --no-strict          Enable or disable STRICT mode (default:
                                      preserve current mode)
      --sql                           Output SQL without executing it
      --load-extension TEXT           Path to SQLite extension, with optional
                                      :entrypoint
      -h, --help                      Show this message and exit.


.. _cli_ref_extract:

extract
=======

See :ref:`cli_extract`.

::

    Usage: sqlite-utils extract [OPTIONS] PATH TABLE COLUMNS...

      Extract one or more columns into a separate table

      Example:

          sqlite-utils extract trees.db Street_Trees species

    Options:
      --table TEXT             Name of the other table to extract columns to
      --fk-column TEXT         Name of the foreign key column to add to the table
      --rename <TEXT TEXT>...  Rename this column in extracted table
      --load-extension TEXT    Path to SQLite extension, with optional :entrypoint
      -h, --help               Show this message and exit.


.. _cli_ref_schema:

schema
======

See :ref:`cli_schema`.

::

    Usage: sqlite-utils schema [OPTIONS] PATH [TABLES]...

      Show full schema for this database or for specified tables

      Example:

          sqlite-utils schema trees.db

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_insert_files:

insert-files
============

See :ref:`cli_insert_files`.

::

    Usage: sqlite-utils insert-files [OPTIONS] PATH TABLE FILE_OR_DIR...

      Insert one or more files using BLOB columns in the specified table

      Example:

          sqlite-utils insert-files pics.db images *.gif \
              -c name:name \
              -c content:content \
              -c content_hash:sha256 \
              -c created:ctime_iso \
              -c modified:mtime_iso \
              -c size:size \
              --pk name

    Options:
      -c, --column TEXT      Column definitions for the table
      --pk TEXT              Column to use as primary key
      --alter                Alter table to add missing columns
      --replace              Replace files with matching primary key
      --upsert               Upsert files with matching primary key
      --name TEXT            File name to use
      --text                 Store file content as TEXT, not BLOB
      --encoding TEXT        Character encoding for input, defaults to utf-8
      -s, --silent           Don't show a progress bar
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_analyze_tables:

analyze-tables
==============

See :ref:`cli_analyze_tables`.

::

    Usage: sqlite-utils analyze-tables [OPTIONS] PATH [TABLES]...

      Analyze the columns in one or more tables

      Example:

          sqlite-utils analyze-tables data.db trees

    Options:
      -c, --column TEXT       Specific columns to analyze
      --save                  Save results to _analyze_tables table
      --common-limit INTEGER  How many common values
      --no-most               Skip most common values
      --no-least              Skip least common values
      --load-extension TEXT   Path to SQLite extension, with optional :entrypoint
      -h, --help              Show this message and exit.


.. _cli_ref_convert:

convert
=======

See :ref:`cli_convert`.

::

    Usage: sqlite-utils convert [OPTIONS] DB_PATH TABLE COLUMNS... CODE

      Convert columns using Python code you supply. For example:

      sqlite-utils convert my.db mytable mycolumn \
          '"\n".join(textwrap.wrap(value, 10))' \
          --import=textwrap

      "value" is a variable with the column value to be converted.

      CODE can also be a reference to a callable that takes the value, for example:

      sqlite-utils convert my.db mytable date r.parsedate
      sqlite-utils convert my.db mytable data json.loads --import json

      Use "-" for CODE to read Python code from standard input.

      The following common operations are available as recipe functions:

      r.jsonsplit(value: 'str', delimiter: 'str' = ',', type: 'Callable[[str],
      object]' = <class 'str'>) -> 'str'

      Convert a string like a,b,c into a JSON array ["a", "b", "c"]

      r.parsedate(value: 'str', dayfirst: 'bool' = False, yearfirst: 'bool' = False,
      errors: 'object | None' = None) -> 'str | None'

      Parse a date and convert it to ISO date format: yyyy-mm-dd
      - dayfirst=True: treat xx as the day in xx/yy/zz
      - yearfirst=True: treat xx as the year in xx/yy/zz
      - errors=r.IGNORE to ignore values that cannot be parsed
      - errors=r.SET_NULL to set values that cannot be parsed to null

      r.parsedatetime(value: 'str', dayfirst: 'bool' = False, yearfirst: 'bool' =
      False, errors: 'object | None' = None) -> 'str | None'

      Parse a datetime and convert it to ISO datetime format: yyyy-mm-ddTHH:MM:SS
      - dayfirst=True: treat xx as the day in xx/yy/zz
      - yearfirst=True: treat xx as the year in xx/yy/zz
      - errors=r.IGNORE to ignore values that cannot be parsed
      - errors=r.SET_NULL to set values that cannot be parsed to null

      You can use these recipes like so:

      sqlite-utils convert my.db mytable mycolumn \
          'r.jsonsplit(value, delimiter=":")'

    Options:
      --import TEXT                   Python modules to import
      --dry-run                       Show results of running this against first 10
                                      rows
      --multi                         Populate columns for keys in returned
                                      dictionary
      --where TEXT                    Optional where clause
      -p, --param <TEXT TEXT>...      Named :parameters for where clause
      --output TEXT                   Optional separate column to populate with the
                                      output
      --output-type [integer|float|blob|text]
                                      Column type to use for the output column
      --drop                          Drop original column afterwards
      -s, --silent                    Don't show a progress bar
      --pdb                           Open pdb debugger on first error
      -h, --help                      Show this message and exit.


.. _cli_ref_tables:

tables
======

See :ref:`cli_tables`.

::

    Usage: sqlite-utils tables [OPTIONS] PATH

      List the tables in the database

      Example:

          sqlite-utils tables trees.db

    Options:
      --fts4                 Just show FTS4 enabled tables
      --fts5                 Just show FTS5 enabled tables
      --counts               Include row counts per table
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit headers from CSV/TSV and table/--fmt output
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, colon_grid,
                             double_grid, double_outline, fancy_grid, fancy_outline,
                             github, grid, heavy_grid, heavy_outline, html, jira,
                             latex, latex_booktabs, latex_longtable, latex_raw,
                             mediawiki, mixed_grid, mixed_outline, moinmoin, orgtbl,
                             outline, pipe, plain, presto, pretty, psql,
                             rounded_grid, rounded_outline, rst, simple,
                             simple_grid, simple_outline, textile, tsv, unsafehtml,
                             youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --ascii                Escape non-ASCII characters in JSON output as \uXXXX
      --columns              Include list of columns for each table
      --schema               Include schema for each table
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_views:

views
=====

See :ref:`cli_views`.

::

    Usage: sqlite-utils views [OPTIONS] PATH

      List the views in the database

      Example:

          sqlite-utils views trees.db

    Options:
      --counts               Include row counts per view
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit headers from CSV/TSV and table/--fmt output
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, colon_grid,
                             double_grid, double_outline, fancy_grid, fancy_outline,
                             github, grid, heavy_grid, heavy_outline, html, jira,
                             latex, latex_booktabs, latex_longtable, latex_raw,
                             mediawiki, mixed_grid, mixed_outline, moinmoin, orgtbl,
                             outline, pipe, plain, presto, pretty, psql,
                             rounded_grid, rounded_outline, rst, simple,
                             simple_grid, simple_outline, textile, tsv, unsafehtml,
                             youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --ascii                Escape non-ASCII characters in JSON output as \uXXXX
      --columns              Include list of columns for each view
      --schema               Include schema for each view
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_rows:

rows
====

See :ref:`cli_rows`.

::

    Usage: sqlite-utils rows [OPTIONS] PATH DBTABLE

      Output all rows in the specified table

      Example:

          sqlite-utils rows trees.db Trees

    Options:
      -c, --column TEXT           Columns to return
      --where TEXT                Optional where clause
      -o, --order TEXT            Order by ('column' or 'column desc')
      -p, --param <TEXT TEXT>...  Named :parameters for where clause
      --limit INTEGER             Number of rows to return - defaults to everything
      --offset INTEGER            SQL offset to use
      --nl                        Output newline-delimited JSON
      --arrays                    Output rows as arrays instead of objects
      --csv                       Output CSV
      --tsv                       Output TSV
      --no-headers                Omit headers from CSV/TSV and table/--fmt output
      -t, --table                 Output as a formatted table
      --fmt TEXT                  Table format - one of asciidoc, colon_grid,
                                  double_grid, double_outline, fancy_grid,
                                  fancy_outline, github, grid, heavy_grid,
                                  heavy_outline, html, jira, latex, latex_booktabs,
                                  latex_longtable, latex_raw, mediawiki, mixed_grid,
                                  mixed_outline, moinmoin, orgtbl, outline, pipe,
                                  plain, presto, pretty, psql, rounded_grid,
                                  rounded_outline, rst, simple, simple_grid,
                                  simple_outline, textile, tsv, unsafehtml, youtrack
      --json-cols                 Detect JSON cols and output them as JSON, not
                                  escaped strings
      --ascii                     Escape non-ASCII characters in JSON output as
                                  \uXXXX
      --load-extension TEXT       Path to SQLite extension, with optional
                                  :entrypoint
      -h, --help                  Show this message and exit.


.. _cli_ref_triggers:

triggers
========

See :ref:`cli_triggers`.

::

    Usage: sqlite-utils triggers [OPTIONS] PATH [TABLES]...

      Show triggers configured in this database

      Example:

          sqlite-utils triggers trees.db

    Options:
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit headers from CSV/TSV and table/--fmt output
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, colon_grid,
                             double_grid, double_outline, fancy_grid, fancy_outline,
                             github, grid, heavy_grid, heavy_outline, html, jira,
                             latex, latex_booktabs, latex_longtable, latex_raw,
                             mediawiki, mixed_grid, mixed_outline, moinmoin, orgtbl,
                             outline, pipe, plain, presto, pretty, psql,
                             rounded_grid, rounded_outline, rst, simple,
                             simple_grid, simple_outline, textile, tsv, unsafehtml,
                             youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --ascii                Escape non-ASCII characters in JSON output as \uXXXX
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_indexes:

indexes
=======

See :ref:`cli_indexes`.

::

    Usage: sqlite-utils indexes [OPTIONS] PATH [TABLES]...

      Show indexes for the whole database or specific tables

      Example:

          sqlite-utils indexes trees.db Trees

    Options:
      --aux                  Include auxiliary columns
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit headers from CSV/TSV and table/--fmt output
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, colon_grid,
                             double_grid, double_outline, fancy_grid, fancy_outline,
                             github, grid, heavy_grid, heavy_outline, html, jira,
                             latex, latex_booktabs, latex_longtable, latex_raw,
                             mediawiki, mixed_grid, mixed_outline, moinmoin, orgtbl,
                             outline, pipe, plain, presto, pretty, psql,
                             rounded_grid, rounded_outline, rst, simple,
                             simple_grid, simple_outline, textile, tsv, unsafehtml,
                             youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --ascii                Escape non-ASCII characters in JSON output as \uXXXX
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_create_database:

create-database
===============

See :ref:`cli_create_database`.

::

    Usage: sqlite-utils create-database [OPTIONS] PATH

      Create a new empty database file

      Example:

          sqlite-utils create-database trees.db

    Options:
      --enable-wal           Enable WAL mode on the created database
      --init-spatialite      Enable SpatiaLite on the created database
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_create_table:

create-table
============

See :ref:`cli_create_table`.

::

    Usage: sqlite-utils create-table [OPTIONS] PATH TABLE COLUMNS...

      Add a table with the specified columns. Columns should be specified using
      name, type pairs, for example:

          sqlite-utils create-table my.db people \
              id integer \
              name text \
              height real \
              photo blob --pk id

      Valid column types are text, integer, real, float, blob and any.

    Options:
      --pk TEXT                 Column to use as primary key
      --not-null TEXT           Columns that should be created as NOT NULL
      --default <TEXT TEXT>...  Default value that should be set for a column
      --fk <TEXT TEXT TEXT>...  Column, other table, other column to set as a
                                foreign key
      --ignore                  If table already exists, do nothing
      --replace                 If table already exists, replace it
      --transform               If table already exists, try to transform the schema
      --load-extension TEXT     Path to SQLite extension, with optional :entrypoint
      --strict                  Apply STRICT mode to created table
      -h, --help                Show this message and exit.


.. _cli_ref_create_index:

create-index
============

See :ref:`cli_create_index`.

::

    Usage: sqlite-utils create-index [OPTIONS] PATH TABLE COLUMN...

      Add an index to the specified table for the specified columns

      Example:

          sqlite-utils create-index chickens.db chickens name

      To create an index in descending order:

          sqlite-utils create-index chickens.db chickens -- -name

    Options:
      --name TEXT                Explicit name for the new index
      --unique                   Make this a unique index
      --if-not-exists, --ignore  Ignore if index already exists
      --analyze                  Run ANALYZE after creating the index
      --load-extension TEXT      Path to SQLite extension, with optional :entrypoint
      -h, --help                 Show this message and exit.


.. _cli_ref_drop_index:

drop-index
==========

See :ref:`cli_drop_index`.

::

    Usage: sqlite-utils drop-index [OPTIONS] PATH TABLE INDEX

      Drop an index by index name from the specified table

      Example:

          sqlite-utils drop-index chickens.db chickens idx_chickens_name

    Options:
      --ignore               Ignore if index does not exist
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_migrate:

migrate
=======

See :ref:`cli_migrate`.

::

    Usage: sqlite-utils migrate [OPTIONS] DB_PATH [MIGRATIONS]...

      Apply pending database migrations.

      Usage:

          sqlite-utils migrate database.db

      This will find the migrations.py file in the current directory or
      subdirectories and apply any pending migrations.

      Or pass paths to one or more migrations.py files directly:

          sqlite-utils migrate database.db path/to/migrations.py

      Pass --list to see a list of applied and pending migrations without applying
      them.

      Use --stop-before migration_set:name to stop before a migration. This option
      can be used multiple times.

    Options:
      --stop-before TEXT  Stop before applying this migration. Use set:name to
                          target a migration set.
      --list              List migrations without running them
      -v, --verbose       Show verbose output
      -h, --help          Show this message and exit.


.. _cli_ref_enable_fts:

enable-fts
==========

See :ref:`cli_fts`.

::

    Usage: sqlite-utils enable-fts [OPTIONS] PATH TABLE COLUMN...

      Enable full-text search for specific table and columns

      Example:

          sqlite-utils enable-fts chickens.db chickens name

    Options:
      --fts4                 Use FTS4
      --fts5                 Use FTS5
      --tokenize TEXT        Tokenizer to use, e.g. porter
      --create-triggers      Create triggers to update the FTS tables when the
                             parent table changes.
      --replace              Replace existing FTS configuration if it exists
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_populate_fts:

populate-fts
============

::

    Usage: sqlite-utils populate-fts [OPTIONS] PATH TABLE COLUMN...

      Re-populate full-text search for specific table and columns

      Example:

          sqlite-utils populate-fts chickens.db chickens name

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_rebuild_fts:

rebuild-fts
===========

::

    Usage: sqlite-utils rebuild-fts [OPTIONS] PATH [TABLES]...

      Rebuild all or specific full-text search tables

      Example:

          sqlite-utils rebuild-fts chickens.db chickens

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_disable_fts:

disable-fts
===========

::

    Usage: sqlite-utils disable-fts [OPTIONS] PATH TABLE

      Disable full-text search for specific table

      Example:

          sqlite-utils disable-fts chickens.db chickens

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_optimize:

optimize
========

See :ref:`cli_optimize`.

::

    Usage: sqlite-utils optimize [OPTIONS] PATH [TABLES]...

      Optimize all full-text search tables and then run VACUUM - should shrink the
      database file

      Example:

          sqlite-utils optimize chickens.db

    Options:
      --no-vacuum            Don't run VACUUM
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_analyze:

analyze
=======

See :ref:`cli_analyze`.

::

    Usage: sqlite-utils analyze [OPTIONS] PATH [NAMES]...

      Run ANALYZE against the whole database, or against specific named indexes and
      tables

      Example:

          sqlite-utils analyze chickens.db

    Options:
      -h, --help  Show this message and exit.


.. _cli_ref_vacuum:

vacuum
======

See :ref:`cli_vacuum`.

::

    Usage: sqlite-utils vacuum [OPTIONS] PATH

      Run VACUUM against the database

      Example:

          sqlite-utils vacuum chickens.db

    Options:
      -h, --help  Show this message and exit.


.. _cli_ref_dump:

dump
====

See :ref:`cli_dump`.

::

    Usage: sqlite-utils dump [OPTIONS] PATH

      Output a SQL dump of the schema and full contents of the database

      Example:

          sqlite-utils dump chickens.db

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_add_column:

add-column
==========

See :ref:`cli_add_column`.

::

    Usage: sqlite-utils add-column [OPTIONS] PATH TABLE COL_NAME
                          [integer|int|float|real|text|str|blob|bytes|any]

      Add a column to the specified table

      Example:

          sqlite-utils add-column chickens.db chickens weight float

    Options:
      --fk TEXT                Table to reference as a foreign key
      --fk-col TEXT            Referenced column on that foreign key table - if
                               omitted will automatically use the primary key
      --not-null-default TEXT  Add NOT NULL DEFAULT 'TEXT' constraint
      --ignore                 If column already exists, do nothing
      --load-extension TEXT    Path to SQLite extension, with optional :entrypoint
      -h, --help               Show this message and exit.


.. _cli_ref_add_foreign_key:

add-foreign-key
===============

See :ref:`cli_add_foreign_key`.

::

    Usage: sqlite-utils add-foreign-key [OPTIONS] PATH TABLE COLUMN [OTHER_TABLE]
                               [OTHER_COLUMN]

      Add a new foreign key constraint to an existing table

      Example:

          sqlite-utils add-foreign-key my.db books author_id authors id

    Options:
      --ignore               If foreign key already exists, do nothing
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_add_foreign_keys:

add-foreign-keys
================

See :ref:`cli_add_foreign_keys`.

::

    Usage: sqlite-utils add-foreign-keys [OPTIONS] PATH [FOREIGN_KEY]...

      Add multiple new foreign key constraints to a database

      Example:

          sqlite-utils add-foreign-keys my.db \
              books author_id authors id \
              authors country_id countries id

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_index_foreign_keys:

index-foreign-keys
==================

See :ref:`cli_index_foreign_keys`.

::

    Usage: sqlite-utils index-foreign-keys [OPTIONS] PATH

      Ensure every foreign key column has an index on it

      Example:

          sqlite-utils index-foreign-keys chickens.db

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_enable_wal:

enable-wal
==========

See :ref:`cli_wal`.

::

    Usage: sqlite-utils enable-wal [OPTIONS] PATH...

      Enable WAL for database files

      Example:

          sqlite-utils enable-wal chickens.db

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_disable_wal:

disable-wal
===========

::

    Usage: sqlite-utils disable-wal [OPTIONS] PATH...

      Disable WAL for database files

      Example:

          sqlite-utils disable-wal chickens.db

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_enable_counts:

enable-counts
=============

See :ref:`cli_enable_counts`.

::

    Usage: sqlite-utils enable-counts [OPTIONS] PATH [TABLES]...

      Configure triggers to update a _counts table with row counts

      Example:

          sqlite-utils enable-counts chickens.db

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_reset_counts:

reset-counts
============

::

    Usage: sqlite-utils reset-counts [OPTIONS] PATH

      Reset calculated counts in the _counts table

      Example:

          sqlite-utils reset-counts chickens.db

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_duplicate:

duplicate
=========

See :ref:`cli_duplicate_table`.

::

    Usage: sqlite-utils duplicate [OPTIONS] PATH TABLE NEW_TABLE

      Create a duplicate of this table, copying across the schema and all row data.

    Options:
      --ignore               If table does not exist, do nothing
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_rename_table:

rename-table
============

See :ref:`cli_renaming_tables`.

::

    Usage: sqlite-utils rename-table [OPTIONS] PATH TABLE NEW_NAME

      Rename this table.

    Options:
      --ignore               If table does not exist, do nothing
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_drop_table:

drop-table
==========

See :ref:`cli_drop_table`.

::

    Usage: sqlite-utils drop-table [OPTIONS] PATH TABLE

      Drop the specified table

      Example:

          sqlite-utils drop-table chickens.db chickens

    Options:
      --ignore               If table does not exist, do nothing
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_create_view:

create-view
===========

See :ref:`cli_create_view`.

::

    Usage: sqlite-utils create-view [OPTIONS] PATH VIEW SELECT

      Create a view for the provided SELECT query

      Example:

          sqlite-utils create-view chickens.db heavy_chickens \
            'select * from chickens where weight > 3'

    Options:
      --ignore               If view already exists, do nothing
      --replace              If view already exists, replace it
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_drop_view:

drop-view
=========

See :ref:`cli_drop_view`.

::

    Usage: sqlite-utils drop-view [OPTIONS] PATH VIEW

      Drop the specified view

      Example:

          sqlite-utils drop-view chickens.db heavy_chickens

    Options:
      --ignore               If view does not exist, do nothing
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_install:

install
=======

See :ref:`cli_install`.

::

    Usage: sqlite-utils install [OPTIONS] [PACKAGES]...

      Install packages from PyPI into the same environment as sqlite-utils

    Options:
      -U, --upgrade        Upgrade packages to latest version
      -e, --editable TEXT  Install a project in editable mode from this path
      -h, --help           Show this message and exit.


.. _cli_ref_uninstall:

uninstall
=========

See :ref:`cli_uninstall`.

::

    Usage: sqlite-utils uninstall [OPTIONS] PACKAGES...

      Uninstall Python packages from the sqlite-utils environment

    Options:
      -y, --yes   Don't ask for confirmation
      -h, --help  Show this message and exit.


.. _cli_ref_add_geometry_column:

add-geometry-column
===================

See :ref:`cli_spatialite`.

::

    Usage: sqlite-utils add-geometry-column [OPTIONS] DB_PATH TABLE COLUMN_NAME

      Add a SpatiaLite geometry column to an existing table. Requires SpatiaLite
      extension.

      By default, this command will try to load the SpatiaLite extension from usual
      paths. To load it from a specific path, use --load-extension.

    Options:
      -t, --type [point|linestring|polygon|multipoint|multilinestring|multipolygon|geometrycollection|geometry]
                                      Specify a geometry type for this column.
                                      [default: GEOMETRY]
      --srid INTEGER                  Spatial Reference ID. See
                                      https://spatialreference.org for details on
                                      specific projections.  [default: 4326]
      --dimensions TEXT               Coordinate dimensions. Use XYZ for three-
                                      dimensional geometries.
      --not-null                      Add a NOT NULL constraint.
      --load-extension TEXT           Path to SQLite extension, with optional
                                      :entrypoint
      -h, --help                      Show this message and exit.


.. _cli_ref_create_spatial_index:

create-spatial-index
====================

See :ref:`cli_spatialite_indexes`.

::

    Usage: sqlite-utils create-spatial-index [OPTIONS] DB_PATH TABLE COLUMN_NAME

      Create a spatial index on a SpatiaLite geometry column. The table and geometry
      column must already exist before trying to add a spatial index.

      By default, this command will try to load the SpatiaLite extension from usual
      paths. To load it from a specific path, use --load-extension.

    Options:
      --load-extension TEXT  Path to SQLite extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_plugins:

plugins
=======

::

    Usage: sqlite-utils plugins [OPTIONS]

      List installed plugins

    Options:
      -h, --help  Show this message and exit.


.. [[[end]]]

```

### `docs/cli.rst`

```rst
.. _cli:

================================
 sqlite-utils command-line tool
================================

The ``sqlite-utils`` command-line tool can be used to manipulate SQLite databases in a number of different ways.

Once :ref:`installed <installation>` the tool should be available as ``sqlite-utils``. It can also be run using ``python -m sqlite_utils``.

.. contents:: :local:
   :class: this-will-duplicate-information-and-it-is-still-useful-here

.. _cli_query:

Running SQL queries
===================

The ``sqlite-utils query`` command lets you run queries directly against a SQLite database file. This is the default subcommand, so the following two examples work the same way:

.. code-block:: bash

    sqlite-utils query dogs.db "select * from dogs"

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs"

.. note::
    In Python: :ref:`db.query() <python_api_query>`  CLI reference: :ref:`sqlite-utils query <cli_ref_query>`

Pass ``-`` as the SQL query to read the query from standard input. This is useful for longer queries that would otherwise require careful shell escaping, or for piping in SQL generated by another tool:

.. code-block:: bash

    echo "select * from dogs" | sqlite-utils query dogs.db -

.. code-block:: bash

    sqlite-utils query dogs.db - < query.sql

.. _cli_query_json:

Returning JSON
--------------

The default format returned for queries is JSON:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs"

.. code-block:: output

    [{"id": 1, "age": 4, "name": "Cleo"},
     {"id": 2, "age": 2, "name": "Pancakes"}]

If the query returns more than one column with the same name, later occurrences are renamed with a numeric suffix - ``select 1 as id, 2 as id`` returns ``[{"id": 1, "id_2": 2}]``. This only applies to JSON output: :ref:`CSV and TSV <cli_query_csv>` and :ref:`table <cli_query_table>` output keep the duplicate column headers unchanged.

.. _cli_query_nl:

Newline-delimited JSON
~~~~~~~~~~~~~~~~~~~~~~

Use ``--nl`` to get back newline-delimited JSON objects:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --nl

.. code-block:: output

    {"id": 1, "age": 4, "name": "Cleo"}
    {"id": 2, "age": 2, "name": "Pancakes"}

.. _cli_query_arrays:

JSON arrays
~~~~~~~~~~~

You can use ``--arrays`` to request arrays instead of objects:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --arrays

.. code-block:: output

    [[1, 4, "Cleo"],
     [2, 2, "Pancakes"]]

You can also combine ``--arrays`` and ``--nl``:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --arrays --nl

.. code-block:: output

    [1, 4, "Cleo"]
    [2, 2, "Pancakes"]

If you want to pretty-print the output further, you can pipe it through ``python -mjson.tool``:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" | python -mjson.tool

.. code-block:: output

    [
        {
            "id": 1,
            "age": 4,
            "name": "Cleo"
        },
        {
            "id": 2,
            "age": 2,
            "name": "Pancakes"
        }
    ]

.. _cli_query_json_ascii:

Unicode characters in JSON
~~~~~~~~~~~~~~~~~~~~~~~~~~

JSON output includes unicode characters directly, without escaping them:

.. code-block:: bash

    sqlite-utils dogs.db "select '日本語' as text"

.. code-block:: output

    [{"text": "日本語"}]

Use ``--ascii`` to escape non-ASCII characters as ``\uXXXX`` sequences instead:

.. code-block:: bash

    sqlite-utils dogs.db "select '日本語' as text" --ascii

.. code-block:: output

    [{"text": "\u65e5\u672c\u8a9e"}]

The ``--ascii`` option can help on systems that cannot display or process UTF-8, such as Windows consoles using a legacy code page. On Windows, setting the ``PYTHONUTF8=1`` environment variable is an alternative fix for ``UnicodeEncodeError`` crashes when redirecting output to a file.

.. _cli_query_binary_json:

Binary data in JSON
~~~~~~~~~~~~~~~~~~~

Binary strings are not valid JSON, so BLOB columns containing binary data will be returned as a JSON object containing base64 encoded data, that looks like this:

.. code-block:: bash

    sqlite-utils dogs.db "select name, content from images" | python -mjson.tool

.. code-block:: output

    [
        {
            "name": "transparent.gif",
            "content": {
                "$base64": true,
                "encoded": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
            }
        }
    ]

.. _cli_json_values:

Nested JSON values
~~~~~~~~~~~~~~~~~~

If one of your columns contains JSON, by default it will be returned as an escaped string:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" | python -mjson.tool

.. code-block:: output

    [
        {
            "id": 1,
            "name": "Cleo",
            "friends": "[{\"name\": \"Pancakes\"}, {\"name\": \"Bailey\"}]"
        }
    ]

You can use the ``--json-cols`` option to automatically detect these JSON columns and output them as nested JSON data:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --json-cols | python -mjson.tool

.. code-block:: output

    [
        {
            "id": 1,
            "name": "Cleo",
            "friends": [
                {
                    "name": "Pancakes"
                },
                {
                    "name": "Bailey"
                }
            ]
        }
    ]

.. _cli_query_csv:

Returning CSV or TSV
--------------------

You can use the ``--csv`` option to return results as CSV:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --csv

.. code-block:: output

    id,age,name
    1,4,Cleo
    2,2,Pancakes

This will default to including the column names as a header row. To exclude the headers, use ``--no-headers``:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --csv --no-headers

.. code-block:: output

    1,4,Cleo
    2,2,Pancakes

Use ``--tsv`` instead of ``--csv`` to get back tab-separated values:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --tsv

.. code-block:: output

    id	age	name
    1	4	Cleo
    2	2	Pancakes

.. _cli_query_table:

Table-formatted output
----------------------

You can use the ``--table`` option (or ``-t`` shortcut) to output query results as a table:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --table

.. code-block:: output

      id    age  name
    ----  -----  --------
       1      4  Cleo
       2      2  Pancakes

You can use the ``--fmt`` option to specify different table formats, for example ``rst`` for reStructuredText:

.. code-block:: bash

    sqlite-utils dogs.db "select * from dogs" --fmt rst

.. code-block:: output

    ====  =====  ========
      id    age  name
    ====  =====  ========
       1      4  Cleo
       2      2  Pancakes
    ====  =====  ========

Available ``--fmt`` options are:

.. [[[cog
    import tabulate
    cog.out("\n" + "\n".join('- ``{}``'.format(t) for t in tabulate.tabulate_formats) + "\n\n")
.. ]]]

- ``asciidoc``
- ``colon_grid``
- ``double_grid``
- ``double_outline``
- ``fancy_grid``
- ``fancy_outline``
- ``github``
- ``grid``
- ``heavy_grid``
- ``heavy_outline``
- ``html``
- ``jira``
- ``latex``
- ``latex_booktabs``
- ``latex_longtable``
- ``latex_raw``
- ``mediawiki``
- ``mixed_grid``
- ``mixed_outline``
- ``moinmoin``
- ``orgtbl``
- ``outline``
- ``pipe``
- ``plain``
- ``presto``
- ``pretty``
- ``psql``
- ``rounded_grid``
- ``rounded_outline``
- ``rst``
- ``simple``
- ``simple_grid``
- ``simple_outline``
- ``textile``
- ``tsv``
- ``unsafehtml``
- ``youtrack``

.. [[[end]]]

This list can also be found by running ``sqlite-utils query --help``.

.. _cli_query_raw:

Returning raw data, such as binary content
------------------------------------------

If your table contains binary data in a ``BLOB`` you can use the ``--raw`` option to output specific columns directly to standard out.

For example, to retrieve a binary image from a ``BLOB`` column and store it in a file you can use the following:

.. code-block:: bash

    sqlite-utils photos.db "select contents from photos where id=1" --raw > myphoto.jpg

To return the first column of each result as raw data, separated by newlines, use ``--raw-lines``:

.. code-block:: bash

    sqlite-utils photos.db "select caption from photos" --raw-lines > captions.txt

.. _cli_query_parameters:

Using named parameters
----------------------

You can pass named parameters to the query using ``-p name value``:

.. code-block:: bash

    sqlite-utils query dogs.db "select :num * :num2" -p num 5 -p num2 6

.. code-block:: output

    [{":num * :num2": 30}]

These will be correctly quoted and escaped in the SQL query, providing a safe way to combine other values with SQL.

.. _cli_query_update_insert_delete:

UPDATE, INSERT and DELETE
-------------------------

If you execute an ``UPDATE``, ``INSERT`` or ``DELETE`` query the command will return the number of affected rows:

.. code-block:: bash

    sqlite-utils dogs.db "update dogs set age = 5 where name = 'Cleo'"

.. code-block:: output

    [{"rows_affected": 1}]

.. _cli_query_functions:

Defining custom SQL functions
-----------------------------

You can use the ``--functions`` option to pass a block of Python code that defines additional functions which can then be called by your SQL query.

This example defines a function which extracts the domain from a URL:

.. code-block:: bash

    sqlite-utils query sites.db "select url, domain(url) from urls" --functions '
    from urllib.parse import urlparse

    def domain(url):
        return urlparse(url).netloc
    '

Every callable object defined in the block will be registered as a SQL function with the same name, with the exception of functions with names that begin with an underscore.

You can also pass the path to a Python file containing function definitions:

.. code-block:: bash

    sqlite-utils query sites.db "select url, domain(url) from urls" --functions functions.py

The ``--functions`` option can be used multiple times to load functions from multiple sources:

.. code-block:: bash

    sqlite-utils query sites.db "select url, domain(url), extract_path(url) from urls" \
      --functions domain_funcs.py \
      --functions 'def extract_path(url):
        from urllib.parse import urlparse
        return urlparse(url).path'

.. note::
    In Python: :ref:`db.register_function() <python_api_register_function>`

.. _cli_query_extensions:

SQLite extensions
-----------------

You can load SQLite extension modules using the ``--load-extension`` option, see :ref:`cli_load_extension`.

.. code-block:: bash

    sqlite-utils dogs.db "select spatialite_version()" --load-extension=spatialite

.. code-block:: output

    [{"spatialite_version()": "4.3.0a"}]

.. _cli_query_attach:

Attaching additional databases
------------------------------

SQLite supports cross-database SQL queries, which can join data from tables in more than one database file.

You can attach one or more additional databases using the ``--attach`` option, providing an alias to use for that database and the path to the SQLite file on disk.

This example attaches the ``books.db`` database under the alias ``books`` and then runs a query that combines data from that database with the default ``dogs.db`` database:

.. code-block:: bash

    sqlite-utils dogs.db --attach books books.db \
       'select * from sqlite_master union all select * from books.sqlite_master'

.. note::
    In Python: :ref:`db.attach() <python_api_attach>`

.. _cli_memory:

Querying data directly using an in-memory database
==================================================

The ``sqlite-utils memory`` command works similar to ``sqlite-utils query``, but allows you to execute queries against an in-memory database.

You can also pass this command CSV or JSON files which will be loaded into a temporary in-memory table, allowing you to execute SQL against that data without a separate step to first convert it to SQLite.

Without any extra arguments, this command executes SQL against the in-memory database directly:

.. code-block:: bash

    sqlite-utils memory 'select sqlite_version()'

.. code-block:: output

    [{"sqlite_version()": "3.35.5"}]

It takes all of the same output formatting options as :ref:`sqlite-utils query <cli_query>`: ``--csv`` and ``--csv`` and ``--table`` and ``--nl``:

.. code-block:: bash

    sqlite-utils memory 'select sqlite_version()' --csv

.. code-block:: output

    sqlite_version()
    3.35.5

.. code-block:: bash

    sqlite-utils memory 'select sqlite_version()' --fmt grid

.. code-block:: output

    +--------------------+
    | sqlite_version()   |
    +====================+
    | 3.35.5             |
    +--------------------+

.. _cli_memory_csv_json:

Running queries directly against CSV or JSON
--------------------------------------------

If you have data in CSV or JSON format you can load it into an in-memory SQLite database and run queries against it directly in a single command using ``sqlite-utils memory`` like this:

.. code-block:: bash

    sqlite-utils memory data.csv "select * from data"

You can pass multiple files to the command if you want to run joins between data from different files:

.. code-block:: bash

    sqlite-utils memory one.csv two.json \
      "select * from one join two on one.id = two.other_id"

If your data is JSON it should be the same format supported by the :ref:`sqlite-utils insert command <cli_inserting_data>` - so either a single JSON object (treated as a single row) or a list of JSON objects.

CSV data can be comma- or tab- delimited.

The in-memory tables will be named after the files without their extensions. The tool also sets up aliases for those tables (using SQL views) as ``t1``, ``t2`` and so on, or you can use the alias ``t`` to refer to the first table:

.. code-block:: bash

    sqlite-utils memory example.csv "select * from t"

If two files have the same name they will be assigned a numeric suffix:

.. code-block:: bash

    sqlite-utils memory foo/data.csv bar/data.csv "select * from data_2"

To read from standard input, use either ``-`` or ``stdin`` as the filename - then use ``stdin`` or ``t`` or ``t1`` as the table name:

.. code-block:: bash

    cat example.csv | sqlite-utils memory - "select * from stdin"

Incoming CSV data will be assumed to use ``utf-8``. If your data uses a different character encoding you can specify that with ``--encoding``:

.. code-block:: bash

    cat example.csv | sqlite-utils memory - "select * from stdin" --encoding=latin-1

If you are joining across multiple CSV files they must all use the same encoding.

Column types will be automatically detected in CSV or TSV data, as described in :ref:`cli_insert_csv_tsv`. You can pass the ``--no-detect-types`` option to disable this automatic type detection and treat all CSV and TSV columns as ``TEXT``.

.. _cli_memory_explicit:

Explicitly specifying the format
--------------------------------

By default, ``sqlite-utils memory`` will attempt to detect the incoming data format (JSON, TSV or CSV) automatically.

You can instead specify an explicit format by adding a ``:csv``, ``:tsv``, ``:json`` or ``:nl`` (for newline-delimited JSON) suffix to the filename. For example:

.. code-block:: bash
    
    sqlite-utils memory one.dat:csv two.dat:nl \
      "select * from one union select * from two"

Here the contents of ``one.dat`` will be treated as CSV and the contents of ``two.dat`` will be treated as newline-delimited JSON.

To explicitly specify the format for data piped into the tool on standard input, use ``stdin:format`` - for example:

.. code-block:: bash

    cat one.dat | sqlite-utils memory stdin:csv "select * from stdin"

.. _cli_memory_attach:

Joining in-memory data against existing databases using \-\-attach
------------------------------------------------------------------

The :ref:`attach option <cli_query_attach>` can be used to attach database files to the in-memory connection, enabling joins between in-memory data loaded from a file and tables in existing SQLite database files. An example:

.. code-block:: bash

    echo "id\n1\n3\n5" | sqlite-utils memory - --attach trees trees.db \
      "select * from trees.trees where rowid in (select id from stdin)"

Here the ``--attach trees trees.db`` option makes the ``trees.db`` database available with an alias of ``trees``.

``select * from trees.trees where ...`` can then query the ``trees`` table in that database.

The CSV data that was piped into the script is available in the ``stdin`` table, so  ``... where rowid in (select id from stdin)`` can be used to return rows from the ``trees`` table that match IDs that were piped in as CSV content.

.. _cli_memory_schema_dump_save:

\-\-schema, \-\-analyze, \-\-dump and \-\-save
----------------------------------------------

To see the in-memory database schema that would be used for a file or for multiple files, use ``--schema``:

.. code-block:: bash

    sqlite-utils memory dogs.csv --schema

.. code-block:: output

    CREATE TABLE "dogs" (
        "id" INTEGER,
        "age" INTEGER,
        "name" TEXT
    );
    CREATE VIEW "t1" AS select * from "dogs";
    CREATE VIEW "t" AS select * from "dogs";

You can run the equivalent of the :ref:`analyze-tables <cli_analyze_tables>` command using ``--analyze``:

.. code-block:: bash

    sqlite-utils memory dogs.csv --analyze

.. code-block:: output

    dogs.id: (1/3)

      Total rows: 2
      Null rows: 0
      Blank rows: 0

      Distinct values: 2

    dogs.name: (2/3)

      Total rows: 2
      Null rows: 0
      Blank rows: 0

      Distinct values: 2

    dogs.age: (3/3)

      Total rows: 2
      Null rows: 0
      Blank rows: 0

      Distinct values: 2

You can output SQL that will both create the tables and insert the full data used to populate the in-memory database using ``--dump``:

.. code-block:: bash

    sqlite-utils memory dogs.csv --dump

.. code-block:: output

    BEGIN TRANSACTION;
    CREATE TABLE "dogs" (
        "id" INTEGER,
        "age" INTEGER,
        "name" TEXT
    );
    INSERT INTO "dogs" VALUES('1','4','Cleo');
    INSERT INTO "dogs" VALUES('2','2','Pancakes');
    CREATE VIEW "t1" AS select * from "dogs";
    CREATE VIEW "t" AS select * from "dogs";
    COMMIT;

Passing ``--save other.db`` will instead use that SQL to populate a new database file:

.. code-block:: bash

    sqlite-utils memory dogs.csv --save dogs.db

These features are mainly intended as debugging tools - for much more finely grained control over how data is inserted into a SQLite database file see :ref:`cli_inserting_data` and :ref:`cli_insert_csv_tsv`.

.. _cli_rows:

Returning all rows in a table
=============================

You can return every row in a specified table using the ``rows`` command:

.. code-block:: bash

    sqlite-utils rows dogs.db dogs

.. code-block:: output

    [{"id": 1, "age": 4, "name": "Cleo"},
     {"id": 2, "age": 2, "name": "Pancakes"}]

This command accepts the same output options as ``query`` - so you can pass ``--nl``, ``--csv``, ``--tsv``, ``--no-headers``, ``--table`` and ``--fmt``.

You can use the ``-c`` option to specify a subset of columns to return:

.. code-block:: bash

    sqlite-utils rows dogs.db dogs -c age -c name

.. code-block:: output

    [{"age": 4, "name": "Cleo"},
     {"age": 2, "name": "Pancakes"}]

You can filter rows using a where clause with the ``--where`` option:

.. code-block:: bash

    sqlite-utils rows dogs.db dogs -c name --where 'name = "Cleo"'

.. code-block:: output

    [{"name": "Cleo"}]

Or pass named parameters using ``--where`` in combination with ``-p``:

.. code-block:: bash

    sqlite-utils rows dogs.db dogs -c name --where 'name = :name' -p name Cleo

.. code-block:: output

    [{"name": "Cleo"}]

You can define a sort order using ``--order column`` or ``--order 'column desc'``.

Use ``--limit N`` to only return the first ``N`` rows. Use ``--offset N`` to return rows starting from the specified offset.

.. note::
    In Python: :ref:`table.rows <python_api_rows>`  CLI reference: :ref:`sqlite-utils rows <cli_ref_rows>`

.. _cli_tables:

Listing tables
==============

You can list the names of tables in a database using the ``tables`` command:

.. code-block:: bash

    sqlite-utils tables mydb.db

.. code-block:: output

    [{"table": "dogs"},
     {"table": "cats"},
     {"table": "chickens"}]

You can output this list in CSV using the ``--csv`` or ``--tsv`` options:

.. code-block:: bash

    sqlite-utils tables mydb.db --csv --no-headers

.. code-block:: output

    dogs
    cats
    chickens

If you just want to see the FTS4 tables, you can use ``--fts4`` (or ``--fts5`` for FTS5 tables):

.. code-block:: bash

    sqlite-utils tables docs.db --fts4

.. code-block:: output

    [{"table": "docs_fts"}]

Use ``--counts`` to include a count of the number of rows in each table:

.. code-block:: bash

    sqlite-utils tables mydb.db --counts

.. code-block:: output

    [{"table": "dogs", "count": 12},
     {"table": "cats", "count": 332},
     {"table": "chickens", "count": 9}]

Use ``--columns`` to include a list of columns in each table:

.. code-block:: bash

    sqlite-utils tables dogs.db --counts --columns

.. code-block:: output

    [{"table": "Gosh", "count": 0, "columns": ["c1", "c2", "c3"]},
     {"table": "Gosh2", "count": 0, "columns": ["c1", "c2", "c3"]},
     {"table": "dogs", "count": 2, "columns": ["id", "age", "name"]}]

Use ``--schema`` to include the schema of each table:

.. code-block:: bash

    sqlite-utils tables dogs.db --schema --table

.. code-block:: output

    table    schema
    -------  -----------------------------------------------
    Gosh     CREATE TABLE Gosh (c1 text, c2 text, c3 text)
    Gosh2    CREATE TABLE Gosh2 (c1 text, c2 text, c3 text)
    dogs     CREATE TABLE "dogs" (
               "id" INTEGER,
               "age" INTEGER,
               "name" TEXT)

The ``--nl``, ``--csv``, ``--tsv``, ``--table`` and ``--fmt`` options are also available.

.. note::
    In Python: :ref:`db.tables or db.table_names() <python_api_tables>`  CLI reference: :ref:`sqlite-utils tables <cli_ref_tables>`

.. _cli_views:

Listing views
=============

The ``views`` command shows any views defined in the database:

.. code-block:: bash

    sqlite-utils views sf-trees.db --table --counts --columns --schema

.. code-block:: output

    view         count  columns               schema
    ---------  -------  --------------------  --------------------------------------------------------------
    demo_view   189144  ['qSpecies']          CREATE VIEW demo_view AS select qSpecies from Street_Tree_List
    hello            1  ['sqlite_version()']  CREATE VIEW hello as select sqlite_version()

It takes the same options as the ``tables`` command:

* ``--columns``
* ``--schema``
* ``--counts``
* ``--nl``
* ``--csv``
* ``--tsv``
* ``--table``

.. note::
    In Python: :ref:`db.views or db.view_names() <python_api_views>`  CLI reference: :ref:`sqlite-utils views <cli_ref_views>`

.. _cli_indexes:

Listing indexes
===============

The ``indexes`` command lists any indexes configured for the database:

.. code-block:: bash

    sqlite-utils indexes covid.db --table

.. code-block:: output

    table                             index_name                                                seqno    cid  name                 desc  coll      key
    --------------------------------  ------------------------------------------------------  -------  -----  -----------------  ------  ------  -----
    johns_hopkins_csse_daily_reports  idx_johns_hopkins_csse_daily_reports_combined_key             0     12  combined_key            0  BINARY      1
    johns_hopkins_csse_daily_reports  idx_johns_hopkins_csse_daily_reports_country_or_region        0      1  country_or_region       0  BINARY      1
    johns_hopkins_csse_daily_reports  idx_johns_hopkins_csse_daily_reports_province_or_state        0      2  province_or_state       0  BINARY      1
    johns_hopkins_csse_daily_reports  idx_johns_hopkins_csse_daily_reports_day                      0      0  day                     0  BINARY      1
    ny_times_us_counties              idx_ny_times_us_counties_date                                 0      0  date                    1  BINARY      1
    ny_times_us_counties              idx_ny_times_us_counties_fips                                 0      3  fips                    0  BINARY      1
    ny_times_us_counties              idx_ny_times_us_counties_county                               0      1  county                  0  BINARY      1
    ny_times_us_counties              idx_ny_times_us_counties_state                                0      2  state                   0  BINARY      1

It shows indexes across all tables. To see indexes for specific tables, list those after the database:

.. code-block:: bash

    sqlite-utils indexes covid.db johns_hopkins_csse_daily_reports --table

The command defaults to only showing the columns that are explicitly part of the index. To also include auxiliary columns use the ``--aux`` option - these columns will be listed with a ``key`` of ``0``.

The command takes the same format options as the ``tables`` and ``views`` commands.

.. note::
    In Python: :ref:`table.indexes <python_api_introspection_indexes>`  CLI reference: :ref:`sqlite-utils indexes <cli_ref_indexes>`

.. _cli_triggers:

Listing triggers
================

The ``triggers`` command shows any triggers configured for the database:

.. code-block:: bash

    sqlite-utils triggers global-power-plants.db --table

.. code-block:: output

    name             table      sql
    ---------------  ---------  -----------------------------------------------------------------
    plants_insert    plants     CREATE TRIGGER "plants_insert" AFTER INSERT ON "plants"
                                BEGIN
                                    INSERT OR REPLACE INTO "_counts"
                                    VALUES (
                                      'plants',
                                      COALESCE(
                                        (SELECT count FROM "_counts" WHERE "table" = 'plants'),
                                      0
                                      ) + 1
                                    );
                                END

It defaults to showing triggers for all tables. To see triggers for one or more specific tables pass their names as arguments:

.. code-block:: bash

    sqlite-utils triggers global-power-plants.db plants

The command takes the same format options as the ``tables`` and ``views`` commands.

.. note::
    In Python: :ref:`table.triggers or db.triggers <python_api_introspection_triggers>`  CLI reference: :ref:`sqlite-utils triggers <cli_ref_triggers>`

.. _cli_schema:

Showing the schema
==================

The ``sqlite-utils schema`` command shows the full SQL schema for the database:

.. code-block:: bash

    sqlite-utils schema dogs.db

.. code-block:: output

    CREATE TABLE "dogs" (
        "id" INTEGER PRIMARY KEY,
        "name" TEXT
    );

This will show the schema for every table and index in the database. To view the schema just for a specified subset of tables pass those as additional arguments:

.. code-block:: bash

    sqlite-utils schema dogs.db dogs chickens

.. note::
    In Python: :ref:`table.schema <python_api_introspection_schema>` or :ref:`db.schema <python_api_schema>`  CLI reference: :ref:`sqlite-utils schema <cli_ref_schema>`

.. _cli_analyze_tables:

Analyzing tables
================

When working with a new database it can be useful to get an idea of the shape of the data. The ``sqlite-utils analyze-tables`` command inspects specified tables (or all tables) and calculates some useful details about each of the columns in those tables.

To inspect the ``tags`` table in the ``github.db`` database, run the following:

.. code-block:: bash

    sqlite-utils analyze-tables github.db tags

.. code-block:: output

    tags.repo: (1/3)

      Total rows: 261
      Null rows: 0
      Blank rows: 0

      Distinct values: 14

      Most common:
        88: 107914493
        75: 140912432
        27: 206156866

      Least common:
        1: 209590345
        2: 206649770
        2: 303218369

    tags.name: (2/3)

      Total rows: 261
      Null rows: 0
      Blank rows: 0

      Distinct values: 175

      Most common:
        10: 0.2
        9: 0.1
        7: 0.3

      Least common:
        1: 0.1.1
        1: 0.11.1
        1: 0.1a2

    tags.sha: (3/3)

      Total rows: 261
      Null rows: 0
      Blank rows: 0

      Distinct values: 261

For each column this tool displays the number of null rows, the number of blank rows (rows that contain an empty string), the number of distinct values and, for columns that are not entirely distinct, the most common and least common values.

If you do not specify any tables every table in the database will be analyzed:

.. code-block:: bash

    sqlite-utils analyze-tables github.db

If you wish to analyze one or more specific columns, use the ``-c`` option:

.. code-block:: bash

    sqlite-utils analyze-tables github.db tags -c sha

To show more than 10 common values, use ``--common-limit 20``.  To skip the most common or least common value analysis, use ``--no-most`` or ``--no-least``:

.. code-block:: bash

    sqlite-utils analyze-tables github.db tags --common-limit 20 --no-least

.. note::
    In Python: :ref:`table.analyze_column() <python_api_analyze_column>`  CLI reference: :ref:`sqlite-utils analyze-tables <cli_ref_analyze_tables>`

.. _cli_analyze_tables_save:

Saving the analyzed table details
---------------------------------

``analyze-tables`` can take quite a while to run for large database files. You can save the results of the analysis to a database table called ``_analyze_tables_`` using the ``--save`` option:

.. code-block:: bash

    sqlite-utils analyze-tables github.db --save

The ``_analyze_tables_`` table has the following schema:

.. code-block:: sql

    CREATE TABLE "_analyze_tables_" (
        "table" TEXT,
        "column" TEXT,
        "total_rows" INTEGER,
        "num_null" INTEGER,
        "num_blank" INTEGER,
        "num_distinct" INTEGER,
        "most_common" TEXT,
        "least_common" TEXT,
        PRIMARY KEY ("table", "column")
    );

The ``most_common`` and ``least_common`` columns will contain nested JSON arrays of the most common and least common values that look like this:

.. code-block:: json

    [
        ["Del Libertador, Av", 5068],
        ["Alberdi Juan Bautista Av.", 4612],
        ["Directorio Av.", 4552],
        ["Rivadavia, Av", 4532],
        ["Yerbal", 4512],
        ["Cosquín", 4472],
        ["Estado Plurinacional de Bolivia", 4440],
        ["Gordillo Timoteo", 4424],
        ["Montiel", 4360],
        ["Condarco", 4288]
    ]

.. _cli_create_database:

Creating an empty database
==========================

You can create a new empty database file using the ``create-database`` command:

.. code-block:: bash

    sqlite-utils create-database empty.db

To enable :ref:`cli_wal` on the newly created database add the ``--enable-wal`` option:

.. code-block:: bash

    sqlite-utils create-database empty.db --enable-wal

To enable SpatiaLite metadata on a newly created database, add the ``--init-spatialite`` flag:

.. code-block:: bash

    sqlite-utils create-database empty.db --init-spatialite

That will look for SpatiaLite in a set of predictable locations. To load it from somewhere else, use the ``--load-extension`` option:

.. code-block:: bash

    sqlite-utils create-database empty.db --init-spatialite --load-extension /path/to/spatialite.so

.. _cli_migrate:

Running migrations
==================

The ``migrate`` command applies pending Python migrations to a database. For the full migration file format and Python API, see :ref:`migrations`.

.. code-block:: bash

    sqlite-utils migrate creatures.db path/to/migrations.py

If you omit the migration path it will search the current directory and subdirectories for files called ``migrations.py``:

.. code-block:: bash

    sqlite-utils migrate creatures.db

Use ``--list`` to list applied and pending migrations without running them:

.. code-block:: bash

    sqlite-utils migrate creatures.db --list

Use ``--stop-before`` to stop before a named migration. The option can be passed more than once, and can target a specific migration set using ``migration_set:migration_name``:

.. code-block:: bash

    sqlite-utils migrate creatures.db path/to/migrations.py \
      --stop-before creatures:add_weight \
      --stop-before sales:drop_index

.. _cli_inserting_data:

Inserting JSON data
===================

If you have data as JSON, you can use ``sqlite-utils insert tablename`` to insert it into a database. The table will be created with the correct (automatically detected) columns if it does not already exist.

You can pass in a single JSON object or a list of JSON objects, either as a filename or piped directly to standard-in (by using ``-`` as the filename).

Here's the simplest possible example:

.. code-block:: bash

    echo '{"name": "Cleo", "age": 4}' | sqlite-utils insert dogs.db dogs -

To specify a column as the primary key, use ``--pk=column_name``.

To create a compound primary key across more than one column, use ``--pk`` multiple times.

If you feed it a JSON list it will insert multiple records. For example, if ``dogs.json`` looks like this:

.. code-block:: json

    [
        {
            "id": 1,
            "name": "Cleo",
            "age": 4
        },
        {
            "id": 2,
            "name": "Pancakes",
            "age": 2
        },
        {
            "id": 3,
            "name": "Toby",
            "age": 6
        }
    ]

You can import all three records into an automatically created ``dogs`` table and set the ``id`` column as the primary key like so:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.json --pk=id

Pass ``--pk`` multiple times to define a compound primary key.

You can skip inserting any records that have a primary key that already exists using ``--ignore``:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.json --pk=id --ignore

You can delete all the existing rows in the table before inserting the new records using ``--truncate``:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.json --truncate

You can add the ``--analyze`` option to run ``ANALYZE`` against the table after the rows have been inserted.

.. note::
    In Python: :ref:`table.insert_all() <python_api_bulk_inserts>`  CLI reference: :ref:`sqlite-utils insert <cli_ref_insert>`

.. _cli_inserting_data_binary:

Inserting binary data
---------------------

You can insert binary data into a BLOB column by first encoding it using base64 and then structuring it like this:

.. code-block:: json

    [
        {
            "name": "transparent.gif",
            "content": {
                "$base64": true,
                "encoded": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
            }
        }
    ]

.. _cli_inserting_data_nl_json:

Inserting newline-delimited JSON
--------------------------------

You can also import newline-delimited JSON (see `JSON Lines <https://jsonlines.org/>`__) using the ``--nl`` option:

.. code-block:: bash

    echo '{"id": 1, "name": "Cleo"}
    {"id": 2, "name": "Suna"}' | sqlite-utils insert creatures.db creatures - --nl

Newline-delimited JSON consists of full JSON objects separated by newlines.

If you are processing data using ``jq`` you can use the ``jq -c`` option to output valid newline-delimited JSON.

Since `Datasette <https://datasette.io/>`__ can export newline-delimited JSON, you can combine the Datasette and ``sqlite-utils`` like so:

.. code-block:: bash

    curl -L "https://latest.datasette.io/fixtures/facetable.json?_shape=array&_nl=on" \
        | sqlite-utils insert nl-demo.db facetable - --pk=id --nl

You can also pipe ``sqlite-utils`` together to create a new SQLite database file containing the results of a SQL query against another database:

.. code-block:: bash

    sqlite-utils sf-trees.db \
        "select TreeID, qAddress, Latitude, Longitude from Street_Tree_List" --nl \
      | sqlite-utils insert saved.db trees - --nl
    
.. code-block:: bash

    sqlite-utils saved.db "select * from trees limit 5" --csv

.. code-block:: output

    TreeID,qAddress,Latitude,Longitude
    141565,501X Baker St,37.7759676911831,-122.441396661871
    232565,940 Elizabeth St,37.7517102172731,-122.441498017841
    119263,495X Lakeshore Dr,,
    207368,920 Kirkham St,37.760210314285,-122.47073935813
    188702,1501 Evans Ave,37.7422086702947,-122.387293152263

.. _cli_inserting_data_flatten:

Flattening nested JSON objects
------------------------------

``sqlite-utils insert`` and ``sqlite-utils memory`` both expect incoming JSON data to consist of an array of JSON objects, where the top-level keys of each object will become columns in the created database table.

If your data is nested you can use the ``--flatten`` option to create columns that are derived from the nested data.

Consider this example document, in a file called ``log.json``:

.. code-block:: json

    {
        "httpRequest": {
            "latency": "0.112114537s",
            "requestMethod": "GET",
            "requestSize": "534",
            "status": 200
        },
        "insertId": "6111722f000b5b4c4d4071e2",
        "labels": {
            "service": "datasette-io"
        }
    }

Inserting this into a table using ``sqlite-utils insert logs.db logs log.json`` will create a table with the following schema:

.. code-block:: sql

    CREATE TABLE "logs" (
       "httpRequest" TEXT,
       "insertId" TEXT,
       "labels" TEXT
    );

With the ``--flatten`` option columns will be created using ``topkey_nextkey`` column names - so running ``sqlite-utils insert logs.db logs log.json --flatten`` will create the following schema instead:

.. code-block:: sql

    CREATE TABLE "logs" (
       "httpRequest_latency" TEXT,
       "httpRequest_requestMethod" TEXT,
       "httpRequest_requestSize" TEXT,
       "httpRequest_status" INTEGER,
       "insertId" TEXT,
       "labels_service" TEXT
    );

.. _cli_insert_csv_tsv:

Inserting CSV or TSV data
=========================

If your data is in CSV format, you can insert it using the ``--csv`` option:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.csv --csv

For tab-delimited data, use ``--tsv``:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.tsv --tsv

Data is expected to be encoded as Unicode UTF-8. If your data is an another character encoding you can specify it using the ``--encoding`` option:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.tsv --tsv --encoding=latin-1

To stop inserting after a specified number of records - useful for getting a faster preview of a large file - use the ``--stop-after`` option:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.csv --csv --stop-after=10

A progress bar is displayed when inserting data from a file. You can hide the progress bar using the ``--silent`` option.

By default, column types are automatically detected for CSV or TSV files - resulting in a mix of ``TEXT``, ``INTEGER`` and ``REAL`` columns. To disable type detection and treat all columns as ``TEXT``, use the ``--no-detect-types`` option.

Detected types are only applied when the table is created by the command. Inserting CSV or TSV data into a table that already exists leaves the existing column types unchanged - values are inserted using the table's existing schema.

For example, given a ``creatures.csv`` file containing this:

.. code-block::

    name,age,weight
    Cleo,6,45.5
    Dori,1,3.5

The following command:

.. code-block:: bash

    sqlite-utils insert creatures.db creatures creatures.csv --csv

Will produce this schema with automatically detected types:

.. code-block:: bash

    sqlite-utils schema creatures.db

.. code-block:: output

    CREATE TABLE "creatures" (
       "name" TEXT,
       "age" INTEGER,
       "weight" REAL
    );

.. _cli_insert_csv_tsv_column_types:

Overriding column types
-----------------------

Use ``--type column-name type`` to override the type automatically chosen when the table is created. This option can be used more than once, and works with both ``insert`` and ``upsert``:

.. code-block:: bash

    sqlite-utils insert places.db places places.csv --csv \
        --type zipcode text \
        --type score real

This is useful for values such as ZIP codes, which may look like integers but should be stored as ``TEXT`` to preserve leading zeros.

The column type should be one of ``TEXT``, ``INTEGER``, ``FLOAT``, ``REAL``, ``BLOB`` or ``ANY``. Column types are matched case-insensitively.

``ANY`` is especially useful with ``--strict``. An ``ANY`` column in a strict table preserves values without coercion, so text such as ``000123`` remains text instead of being converted to an integer:

.. code-block:: bash

    sqlite-utils insert events.db events events.csv --csv --strict \
        --type payload any

As with detected column types, ``--type`` only affects tables created by the command. If the table already exists, its existing column types are left unchanged.

To disable type detection and treat all columns as TEXT, use ``--no-detect-types``:

.. code-block:: bash

    sqlite-utils insert creatures.db creatures creatures.csv --csv --no-detect-types

If a CSV or TSV file includes empty cells, like this one:

::

    name,age,weight
    Cleo,6,
    Dori,,3.5

They will be imported into SQLite as empty string values, ``""``.

To import them as ``NULL`` values instead, use the ``--empty-null`` option:

.. code-block:: bash

    sqlite-utils insert creatures.db creatures creatures.csv --csv --empty-null

.. _cli_insert_csv_tsv_delimiter:

Alternative delimiters and quote characters
-------------------------------------------

If your file uses a delimiter other than ``,`` or a quote character other than ``"`` you can attempt to detect delimiters or you can specify them explicitly.

The ``--sniff`` option can be used to attempt to detect the delimiters:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.csv --sniff

Alternatively, you can specify them using the ``--delimiter`` and ``--quotechar`` options.

Here's a CSV file that uses ``;`` for delimiters and the ``|`` symbol for quote characters::

    name;description
    Cleo;|Very fine; a friendly dog|
    Pancakes;A local corgi

You can import that using:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.csv --delimiter=";" --quotechar="|"

Passing ``--delimiter``, ``--quotechar`` or ``--sniff`` implies ``--csv``, so you can omit the ``--csv`` option.

.. _cli_insert_csv_tsv_no_header:

CSV files without a header row
------------------------------

The first row of any CSV or TSV file is expected to contain the names of the columns in that file.

If your file does not include this row, you can use the ``--no-headers`` option to specify that the tool should not use that fist row as headers.

If you do this, the table will be created with column names called ``untitled_1`` and ``untitled_2`` and so on. You can then rename them using the ``sqlite-utils transform ... --rename`` command, see :ref:`cli_transform_table`.

.. _cli_insert_unstructured:

Inserting unstructured data with \-\-lines and \-\-text
=======================================================

If you have an unstructured file you can insert its contents into a table with a single ``line`` column containing each line from the file using ``--lines``. This can be useful if you intend to further analyze those lines using SQL string functions or :ref:`sqlite-utils convert <cli_convert>`:

.. code-block:: bash

    sqlite-utils insert logs.db loglines logfile.log --lines

This will produce the following schema:

.. code-block:: sql

    CREATE TABLE "loglines" (
       "line" TEXT
    );

You can also insert the entire contents of the file into a single column called ``text`` using ``--text``:

.. code-block:: bash

    sqlite-utils insert content.db content file.txt --text

The schema here will be:

.. code-block:: sql

    CREATE TABLE "content" (
       "text" TEXT
    );

.. _cli_insert_convert:

Applying conversions while inserting data
=========================================

The ``--convert`` option can be used to apply a Python conversion function to imported data before it is inserted into the database. It works in a similar way to :ref:`sqlite-utils convert <cli_convert>`.

Your Python function will be passed a dictionary called ``row`` for each item that is being imported. You can modify that dictionary and return it - or return a fresh dictionary - to change the data that will be inserted.

Given a JSON file called ``dogs.json`` containing this:

.. code-block:: json

    [
        {"id": 1, "name": "Cleo"},
        {"id": 2, "name": "Pancakes"}
    ]

The following command will insert that data and add an ``is_good`` column set to ``1`` for each dog:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs dogs.json --convert 'row["is_good"] = 1'

The ``--convert`` option also works with the ``--csv``, ``--tsv`` and ``--nl`` insert options.

As with ``sqlite-utils convert`` you can use ``--import`` to import additional Python modules, see :ref:`cli_convert_import` for details.

You can also pass code that runs some initialization steps and defines a ``convert(value)`` function, see :ref:`cli_convert_complex`.

.. _cli_insert_convert_lines:

\-\-convert with \-\-lines
--------------------------

Things work slightly differently when combined with the ``--lines`` or ``--text`` options.

With ``--lines``, instead of being passed a ``row`` dictionary your function will be passed a ``line`` string representing each line of the input. Given a file called ``access.log`` containing the following::

    INFO:     127.0.0.1:60581 - GET / HTTP/1.1 200 OK
    INFO:     127.0.0.1:60581 - GET /foo/-/static/app.css?cead5a HTTP/1.1 200 OK

You could convert it into structured data like so:

.. code-block:: bash

    sqlite-utils insert logs.db loglines access.log --convert '
    type, source, _, verb, path, _, status, _ = line.split()
    return {
        "type": type,
        "source": source,
        "verb": verb,
        "path": path,
        "status": status,
    }' --lines

The resulting table would look like this:

======  ===============  ======  ============================  ========
type    source           verb    path                            status
======  ===============  ======  ============================  ========
INFO:   127.0.0.1:60581  GET     /                                  200
INFO:   127.0.0.1:60581  GET     /foo/-/static/app.css?cead5a       200
======  ===============  ======  ============================  ========

.. _cli_insert_convert_text:

\-\-convert with \-\-text
-------------------------

With ``--text`` the entire input to the command will be made available to the function as a variable called ``text``.

The function can return a single dictionary which will be inserted as a single row, or it can return a list or iterator of dictionaries, each of which will be inserted.

Here's how to use ``--convert`` and ``--text`` to insert one record per word in the input:

.. code-block:: bash

    echo 'A bunch of words' | sqlite-utils insert words.db words - \
        --text --convert '({"word": w} for w in text.split())'

The result looks like this:

.. code-block:: bash

    sqlite-utils dump words.db

.. code-block:: output

    BEGIN TRANSACTION;
    CREATE TABLE "words" (
       "word" TEXT
    );
    INSERT INTO "words" VALUES('A');
    INSERT INTO "words" VALUES('bunch');
    INSERT INTO "words" VALUES('of');
    INSERT INTO "words" VALUES('words');
    COMMIT;


.. _cli_insert_code:

Inserting rows generated by Python code
=======================================

Instead of providing a ``FILE`` to import, you can use the ``--code`` option to pass a block of Python code that generates the rows to insert. This is the command-line equivalent of calling ``db["creatures"].insert_all(rows())`` from the :ref:`Python API <python_api>`.

Your code should define either a ``rows()`` function that returns or yields dictionaries, or a ``rows`` iterable such as a list of dictionaries:

.. code-block:: bash

    sqlite-utils insert data.db creatures --code '
    def rows():
        yield {"id": 1, "name": "Cleo"}
        yield {"id": 2, "name": "Suna"}
    ' --pk id

``--code`` can also be given a path to a Python ``.py`` file.

The ``--code`` option works with both ``sqlite-utils insert`` and ``sqlite-utils upsert``, and composes with table options such as ``--pk``, ``--replace``, ``--alter``, ``--not-null`` and ``--default``. It cannot be combined with a ``FILE`` argument or with input format options such as ``--csv`` or ``--convert``.

.. _cli_insert_replace:

Insert-replacing data
=====================

The ``--replace`` option to ``insert`` causes any existing records with the same primary key to be replaced entirely by the new records.

To replace a dog with in ID of 2 with a new record, run the following:

.. code-block:: bash

    echo '{"id": 2, "name": "Pancakes", "age": 3}' | \
        sqlite-utils insert dogs.db dogs - --pk=id --replace

.. note::
    In Python: :ref:`table.insert(..., replace=True) <python_api_insert_replace>`  CLI reference: :ref:`sqlite-utils insert <cli_ref_insert>`

.. _cli_upsert:

Upserting data
==============

Upserting is update-or-insert. If a row exists with the specified primary key the provided columns will be updated. If no row exists that row will be created.

Unlike ``insert --replace``, an upsert will ignore any column values that exist but are not present in the upsert document.

For example:

.. code-block:: bash

    echo '{"id": 2, "age": 4}' | \
        sqlite-utils upsert dogs.db dogs - --pk=id

This will update the dog with an ID of 2 to have an age of 4, creating a new record (with a null name) if one does not exist. If a row DOES exist the name will be left as-is.

If the table already exists and has a primary key, you can omit the ``--pk`` option and ``sqlite-utils`` will use that existing primary key.

The command will fail if you reference columns that do not exist on the table. To automatically create missing columns, use the ``--alter`` option.

.. note::
    ``upsert`` in sqlite-utils 1.x worked like ``insert ... --replace`` does in 2.x. See `issue #66 <https://github.com/simonw/sqlite-utils/issues/66>`__ for details of this change.


.. note::
    In Python: :ref:`table.upsert() <python_api_upsert>`  CLI reference: :ref:`sqlite-utils upsert <cli_ref_upsert>`

.. _cli_bulk:

Executing SQL in bulk
=====================

If you have a JSON, newline-delimited JSON, CSV or TSV file you can execute a bulk SQL query using each of the records in that file using the ``sqlite-utils bulk`` command.

The command takes the database file, the SQL to be executed and the file containing records to be used when evaluating the SQL query.

The SQL query should include ``:named`` parameters that match the keys in the records.

For example, given a ``chickens.csv`` CSV file containing the following:

.. code-block::

    id,name
    1,Blue
    2,Snowy
    3,Azi
    4,Lila
    5,Suna
    6,Cardi

You could insert those rows into a pre-created ``chickens`` table like so:

.. code-block:: bash

    sqlite-utils bulk chickens.db \
      'insert into chickens (id, name) values (:id, :name)' \
      chickens.csv --csv

This command takes the same options as the ``sqlite-utils insert`` command - so it defaults to expecting JSON but can accept other formats using ``--csv`` or ``--tsv`` or ``--nl`` or other options described above.

By default all of the SQL queries will be executed in a single transaction. To commit every 20 records, use ``--batch-size 20``.

.. _cli_insert_files:

Inserting data from files
=========================

The ``insert-files`` command can be used to insert the content of files, along with their metadata, into a SQLite table.

Here's an example that inserts all of the GIF files in the current directory into a ``gifs.db`` database, placing the file contents in an ``images`` table:

.. code-block:: bash

    sqlite-utils insert-files gifs.db images *.gif

You can also pass one or more directories, in which case every file in those directories will be added recursively:

.. code-block:: bash

    sqlite-utils insert-files gifs.db images path/to/my-gifs

By default this command will create a table with the following schema:

.. code-block:: sql

    CREATE TABLE "images" (
        "path" TEXT PRIMARY KEY,
        "content" BLOB,
        "size" INTEGER
    );

Content will be treated as binary by default and stored in a ``BLOB`` column. You can use the ``--text`` option to store that content in a ``TEXT`` column instead.

You can customize the schema using one or more ``-c`` options. For a table schema that includes just the path, MD5 hash and last modification time of the file, you would use this:

.. code-block:: bash

    sqlite-utils insert-files gifs.db images *.gif -c path -c md5 -c mtime --pk=path

This will result in the following schema:

.. code-block:: sql

    CREATE TABLE "images" (
        "path" TEXT PRIMARY KEY,
        "md5" TEXT,
        "mtime" REAL
    );

Note that there's no ``content`` column here at all - if you specify custom columns using ``-c`` you need to include ``-c content`` to create that column.

You can change the name of one of these columns using a ``-c colname:coldef`` parameter. To rename the ``mtime`` column to ``last_modified`` you would use this:

.. code-block:: bash

    sqlite-utils insert-files gifs.db images *.gif \
        -c path -c md5 -c last_modified:mtime --pk=path

You can pass ``--replace`` or ``--upsert`` to indicate what should happen if you try to insert a file with an existing primary key. Pass ``--alter`` to cause any missing columns to be added to the table.

The full list of column definitions you can use is as follows:

``name``
    The name of the file, e.g. ``cleo.jpg``
``path``
    The path to the file relative to the root folder, e.g. ``pictures/cleo.jpg``
``fullpath``
    The fully resolved path to the image, e.g. ``/home/simonw/pictures/cleo.jpg``
``sha256``
    The SHA256 hash of the file contents
``md5``
    The MD5 hash of the file contents
``mode``
    The permission bits of the file, as an integer - you may want to convert this to octal
``content``
    The binary file contents, which will be stored as a BLOB
``content_text``
    The text file contents, which will be stored as TEXT
``mtime``
    The modification time of the file, as floating point seconds since the Unix epoch
``ctime``
    The creation time of the file, as floating point seconds since the Unix epoch
``mtime_int``
    The modification time as an integer rather than a float
``ctime_int``
    The creation time as an integer rather than a float
``mtime_iso``
    The modification time as an ISO timestamp, e.g. ``2020-07-27T04:24:06.654246``
``ctime_iso``
    The creation time is an ISO timestamp
``size``
    The integer size of the file in bytes
``stem``
    The filename without the extension - for ``file.txt.gz`` this would be ``file.txt``
``suffix``
    The file extension - for ``file.txt.gz`` this would be ``.gz``

You can insert data piped from standard input like this:

.. code-block:: bash

    cat dog.jpg | sqlite-utils insert-files dogs.db pics - --name=dog.jpg

The ``-`` argument indicates data should be read from standard input. The string passed using the ``--name`` option will be used for the file name and path values.

When inserting data from standard input only the following column definitions are supported: ``name``, ``path``, ``content``, ``content_text``, ``sha256``, ``md5`` and ``size``.

.. _cli_convert:

Converting data in columns
==========================

The ``convert`` command can be used to transform the data in a specified column - for example to parse a date string into an ISO timestamp, or to split a string of tags into a JSON array.

The command accepts a database, table, one or more columns and a string of Python code to be executed against the values from those columns. The following example would replace the values in the ``headline`` column in the ``articles`` table with an upper-case version:

.. code-block:: bash

    sqlite-utils convert content.db articles headline 'value.upper()'

The Python code is passed as a string. Within that Python code the ``value`` variable will be the value of the current column.

The code you provide will be compiled into a function that takes ``value`` as a single argument. If you break your function body into multiple lines the last line should be a ``return`` statement:

.. code-block:: bash

    sqlite-utils convert content.db articles headline '
    value = str(value)
    return value.upper()'

Your code will be automatically wrapped in a function, but you can also define a function called ``convert(value)`` which will be called, if available:

.. code-block:: bash

    sqlite-utils convert content.db articles headline '
    def convert(value):
        return value.upper()'

Use a ``CODE`` value of ``-`` to read from standard input:

.. code-block:: bash

    cat mycode.py | sqlite-utils convert content.db articles headline -

Where ``mycode.py`` contains a fragment of Python code that looks like this:

.. code-block:: python

    def convert(value):
        return value.upper()

The conversion will be applied to every row in the specified table. You can limit that to just rows that match a ``WHERE`` clause using ``--where``:

.. code-block:: bash

    sqlite-utils convert content.db articles headline 'value.upper()' \
        --where "headline like '%cat%'"

You can include named parameters in your where clause and populate them using one or more ``--param`` options:

.. code-block:: bash

    sqlite-utils convert content.db articles headline 'value.upper()' \
        --where "headline like :query" \
        --param query '%cat%'

The ``--dry-run`` option will output a preview of the conversion against the first ten rows, without modifying the database.

.. note::
    In Python: :ref:`table.convert() <python_api_convert>`  CLI reference: :ref:`sqlite-utils convert <cli_ref_convert>`

.. _cli_convert_import:

Importing additional modules
----------------------------

You can specify Python modules that should be imported and made available to your code using one or more ``--import`` options. This example uses the ``textwrap`` module to wrap the ``content`` column at 100 characters:

.. code-block:: bash

    sqlite-utils convert content.db articles content \
        '"\n".join(textwrap.wrap(value, 100))' \
        --import=textwrap

This supports nested imports as well, for example to use `ElementTree <https://docs.python.org/3/library/xml.etree.elementtree.html>`__:

.. code-block:: bash

    sqlite-utils convert content.db articles content \
        'xml.etree.ElementTree.fromstring(value).attrib["title"]' \
        --import=xml.etree.ElementTree

.. _cli_convert_debugger:

Using the debugger
------------------

If an error occurs while running your conversion operation you may see a message like this::

    user-defined function raised exception

Add the ``--pdb`` option to catch the error and open the Python debugger at that point. The conversion operation will exit after you type ``q`` in the debugger.

Here's an example debugging session. First, create a ``articles`` table with invalid XML in the ``content`` column:

.. code-block:: bash

    echo '{"content": "This is not XML"}' | sqlite-utils insert content.db articles -

Now run the conversion with the ``--pdb`` option:

.. code-block:: bash

    sqlite-utils convert content.db articles content \
        'xml.etree.ElementTree.fromstring(value).attrib["title"]' \
        --import=xml.etree.ElementTree \
        --pdb

When the error occurs the debugger will open::

    Exception raised, dropping into pdb...: syntax error: line 1, column 0
    > .../python3.11/xml/etree/ElementTree.py(1338)XML()
    -> parser.feed(text)
    (Pdb) args
    text = 'This is not XML'
    parser = <xml.etree.ElementTree.XMLParser object at 0x102c405e0>
    (Pdb) q

``args`` here shows the arguments to the current function in the stack. The Python `pdb documentation <https://docs.python.org/3/library/pdb.html#debugger-commands>`__ has full details on the other available commands.

.. _cli_convert_complex:

Defining a convert() function
-----------------------------

Instead of providing a single line of code to be executed against each value, you can define a function called ``convert(value)``.

This mechanism can be used to execute one-off initialization code that runs once at the start of the conversion run.

The following example adds a new ``score`` column, then updates it to list a random number - after first seeding the random number generator to ensure that multiple runs produce the same results:

.. code-block:: bash

    sqlite-utils add-column content.db articles score float --not-null-default 1.0
    sqlite-utils convert content.db articles score '
    import random
    random.seed(10)

    def convert(value):
        return random.random()
    '

.. _cli_convert_recipes:

sqlite-utils convert recipes
----------------------------

Various built-in recipe functions are available for common operations. These are:

``r.jsonsplit(value, delimiter=',', type=<class 'str'>)``
  Convert a string like ``a,b,c`` into a JSON array ``["a", "b", "c"]``

  The ``delimiter`` parameter can be used to specify a different delimiter.

  The ``type`` parameter can be set to ``float`` or ``int`` to produce a JSON array of different types, for example if the column's string value was ``1.2,3,4.5`` the following::

      r.jsonsplit(value, type=float)

  Would produce an array like this: ``[1.2, 3.0, 4.5]``

``r.parsedate(value, dayfirst=False, yearfirst=False, errors=None)``
  Parse a date and convert it to ISO date format: ``yyyy-mm-dd``

  In the case of dates such as ``03/04/05`` U.S. ``MM/DD/YY`` format is assumed - you can use ``dayfirst=True`` or ``yearfirst=True`` to change how these ambiguous dates are interpreted.

  Use the ``errors=`` parameter to specify what should happen if a value cannot be parsed.

  By default, if any value cannot be parsed an error will be occurred and all values will be left as they were.

  Set ``errors=r.IGNORE`` to ignore any values that cannot be parsed, leaving them unchanged.

  Set ``errors=r.SET_NULL`` to set any values that cannot be parsed to ``null``.

``r.parsedatetime(value, dayfirst=False, yearfirst=False, errors=None)``
  Parse a datetime and convert it to ISO datetime format: ``yyyy-mm-ddTHH:MM:SS``

These recipes can be used in the code passed to ``sqlite-utils convert`` like this:

.. code-block:: bash

    sqlite-utils convert my.db mytable mycolumn \
      'r.jsonsplit(value)'

You can also pass the recipe function directly without the ``(value)`` part - sqlite-utils will detect that it is a callable and use it automatically:

.. code-block:: bash

    sqlite-utils convert my.db mytable mycolumn r.parsedate

This shorter syntax works for any callable, including functions from imported modules:

.. code-block:: bash

    sqlite-utils convert my.db mytable mycolumn json.loads --import json

To use any of the documented parameters, use the full function call syntax:

.. code-block:: bash

    sqlite-utils convert my.db mytable mycolumn \
      'r.jsonsplit(value, delimiter=":")'

.. _cli_convert_output:

Saving the result to a different column
---------------------------------------

The ``--output`` and ``--output-type`` options can be used to save the result of the conversion to a separate column, which will be created if that column does not already exist:

.. code-block:: bash

    sqlite-utils convert content.db articles headline 'value.upper()' \
      --output headline_upper

The type of the created column defaults to ``text``, but a different column type can be specified using ``--output-type``. This example will create a new floating point column called ``id_as_a_float`` with a copy of each item's ID increased by 0.5:

.. code-block:: bash

    sqlite-utils convert content.db articles id 'float(value) + 0.5' \
      --output id_as_a_float \
      --output-type float

You can drop the original column at the end of the operation by adding ``--drop``.

.. _cli_convert_multi:

Converting a column into multiple columns
-----------------------------------------

Sometimes you may wish to convert a single column into multiple derived columns. For example, you may have a ``location`` column containing ``latitude,longitude`` values which you wish to split out into separate ``latitude`` and ``longitude`` columns.

You can achieve this using the ``--multi`` option to ``sqlite-utils convert``. This option expects your Python code to return a Python dictionary: new columns well be created and populated for each of the keys in that dictionary.

For the ``latitude,longitude`` example you would use the following:

.. code-block:: bash

    sqlite-utils convert demo.db places location \
    'bits = value.split(",")
    return {
      "latitude": float(bits[0]),
      "longitude": float(bits[1]),
    }' --multi

The type of the returned values will be taken into account when creating the new columns. In this example, the resulting database schema will look like this:

.. code-block:: sql

    CREATE TABLE "places" (
        "location" TEXT,
        "latitude" REAL,
        "longitude" REAL
    );

The code function can also return ``None``, in which case its output will be ignored. You can drop the original column at the end of the operation by adding ``--drop``.

.. _cli_create_table:

Creating tables
===============

Most of the time creating tables by inserting example data is the quickest approach. If you need to create an empty table in advance of inserting data you can do so using the ``create-table`` command:

.. code-block:: bash

    sqlite-utils create-table mydb.db mytable id integer name text --pk=id

This will create a table called ``mytable`` with two columns - an integer ``id`` column and a text ``name`` column. It will set the ``id`` column to be the primary key.

You can pass as many column-name column-type pairs as you like. Valid types are ``integer``, ``text``, ``float`` and ``blob``.

Pass ``--pk`` more than once for a compound primary key that covers multiple columns.

You can specify columns that should be NOT NULL using ``--not-null colname``. You can specify default values for columns using ``--default colname defaultvalue``.

.. code-block:: bash

    sqlite-utils create-table mydb.db mytable \
        id integer \
        name text \
        age integer \
        is_good integer \
        --not-null name \
        --not-null age \
        --default is_good 1 \
        --pk=id

.. code-block:: bash

    sqlite-utils tables mydb.db --schema -t

.. code-block:: output

    table    schema
    -------  --------------------------------
    mytable  CREATE TABLE "mytable" (
                "id" INTEGER PRIMARY KEY,
                "name" TEXT NOT NULL,
                "age" INTEGER NOT NULL,
                "is_good" INTEGER DEFAULT '1'
            )

You can specify foreign key relationships between the tables you are creating using ``--fk colname othertable othercolumn``:

.. code-block:: bash

    sqlite-utils create-table books.db authors \
        id integer \
        name text \
        --pk=id

    sqlite-utils create-table books.db books \
        id integer \
        title text \
        author_id integer \
        --pk=id \
        --fk author_id authors id

.. code-block:: bash

    sqlite-utils tables books.db --schema -t

.. code-block:: output

    table    schema
    -------  -------------------------------------------------
    authors  CREATE TABLE "authors" (
                "id" INTEGER PRIMARY KEY,
                "name" TEXT
             )
    books    CREATE TABLE "books" (
                "id" INTEGER PRIMARY KEY,
                "title" TEXT,
                "author_id" INTEGER REFERENCES "authors"("id")
             )

You can create a table in `SQLite STRICT mode <https://www.sqlite.org/stricttables.html>`__ using ``--strict``:

.. code-block:: bash

   sqlite-utils create-table mydb.db mytable id integer name text --strict

Use the ``any`` type for a strict column that should accept integers, floating point values, text, binary data or null without coercion:

.. code-block:: bash

   sqlite-utils create-table events.db events id integer payload any --strict

.. code-block:: bash

   sqlite-utils tables mydb.db --schema -t

.. code-block:: output

   table    schema
   -------  ------------------------
   mytable  CREATE TABLE "mytable" (
               "id" INTEGER,
               "name" TEXT
            ) STRICT

If a table with the same name already exists, you will get an error. You can choose to silently ignore this error with ``--ignore``, or you can replace the existing table with a new, empty table using ``--replace``.

You can also pass ``--transform`` to transform the existing table to match the new schema. See :ref:`python_api_explicit_create` in the Python library documentation for details of how this option works.

.. note::
    In Python: :ref:`table.create() <python_api_explicit_create>`  CLI reference: :ref:`sqlite-utils create-table <cli_ref_create_table>`

.. _cli_renaming_tables:

Renaming a table
================

Yo ucan rename a table using the ``rename-table`` command:

.. code-block:: bash

    sqlite-utils rename-table mydb.db oldname newname

Pass ``--ignore`` to ignore any errors caused by the table not existing, or the new name already being in use.

.. note::
    In Python: :ref:`db.rename_table() <python_api_rename_table>`  CLI reference: :ref:`sqlite-utils rename-table <cli_ref_rename_table>`

.. _cli_duplicate_table:

Duplicating tables
==================

The ``duplicate`` command duplicates a table - creating a new table with the same schema and a copy of all of the rows:

.. code-block:: bash

    sqlite-utils duplicate books.db authors authors_copy

.. note::
    In Python: :ref:`table.duplicate() <python_api_duplicate>`  CLI reference: :ref:`sqlite-utils duplicate <cli_ref_duplicate>`

.. _cli_drop_table:

Dropping tables
===============

You can drop a table using the ``drop-table`` command:

.. code-block:: bash

    sqlite-utils drop-table mydb.db mytable

Use ``--ignore`` to ignore the error if the table does not exist.

.. note::
    In Python: :ref:`table.drop() <python_api_drop>`  CLI reference: :ref:`sqlite-utils drop-table <cli_ref_drop_table>`

.. _cli_transform_table:

Transforming tables
===================

The ``transform`` command allows you to apply complex transformations to a table that cannot be implemented using a regular SQLite ``ALTER TABLE`` command. See :ref:`python_api_transform` for details of how this works. By default, the ``transform`` command preserves a table's ``STRICT`` mode.

.. code-block:: bash

    sqlite-utils transform mydb.db mytable \
        --drop column1 \
        --rename column2 column_renamed

Every option for this table (with the exception of ``--pk-none``) can be specified multiple times. The options are as follows:

``--type column-name new-type``
    Change the type of the specified column. Valid types are ``integer``, ``text``, ``float``, ``real``, ``blob`` and ``any``. Changing a ``TEXT`` column to ``INTEGER``, ``FLOAT`` or ``REAL`` converts exact empty-string values to ``NULL``.

``--drop column-name``
    Drop the specified column.

``--rename column-name new-name``
    Rename this column to a new name.

``--column-order column``
    Use this multiple times to specify a new order for your columns. ``-o`` shortcut is also available.

``--not-null column-name``
    Set this column as ``NOT NULL``.

``--not-null-false column-name``
    For a column that is currently set as ``NOT NULL``, remove the ``NOT NULL``.

``--pk column-name``
    Change the primary key column for this table. Pass ``--pk`` multiple times if you want to create a compound primary key.

``--pk-none``
    Remove the primary key from this table, turning it into a ``rowid`` table.

``--default column-name value``
    Set the default value of this column.

``--default-none column``
    Remove the default value for this column.

``--drop-foreign-key column``
    Drop the specified foreign key.

``--add-foreign-key column other_table other_column``
    Add a foreign key constraint to ``column`` pointing to ``other_table.other_column``.

``--strict``
    Convert the table to a `SQLite STRICT table <https://www.sqlite.org/stricttables.html>`__. The command fails if the available SQLite version does not support strict tables. If existing rows contain values that are incompatible with their declared column types the transformation fails and the original table is left unchanged.

``--no-strict``
    Convert a strict table back to a regular non-strict table.

If you want to see the SQL that will be executed to make the change without actually executing it, add the ``--sql`` flag. For example:

.. code-block:: bash

    sqlite-utils transform fixtures.db roadside_attractions \
        --rename pk id \
        --default name Untitled \
        --column-order id \
        --column-order longitude \
        --column-order latitude \
        --drop address \
        --sql

.. code-block:: output

    CREATE TABLE "roadside_attractions_new_4033a60276b9" (
       "id" INTEGER PRIMARY KEY,
       "longitude" FLOAT,
       "latitude" FLOAT,
       "name" TEXT DEFAULT 'Untitled'
    );
    INSERT INTO "roadside_attractions_new_4033a60276b9" ("longitude", "latitude", "id", "name")
       SELECT "longitude", "latitude", "pk", "name" FROM "roadside_attractions";
    DROP TABLE "roadside_attractions";
    PRAGMA legacy_alter_table=ON;
    ALTER TABLE "roadside_attractions_new_4033a60276b9" RENAME TO "roadside_attractions";
    PRAGMA legacy_alter_table=OFF;

Tables that are referenced by views can be transformed - the view definitions are left unchanged, see :ref:`python_api_transform_views` for details.

.. note::
    In Python: :ref:`table.transform() <python_api_transform>`  CLI reference: :ref:`sqlite-utils transform <cli_ref_transform>`

.. _cli_transform_table_add_primary_key_to_rowid:

Adding a primary key to a rowid table
-------------------------------------

SQLite tables that are created without an explicit primary key are created as `rowid tables <https://www.sqlite.org/rowidtable.html>`__. They still have a numeric primary key which is available in the ``rowid`` column, but that column is not included in the output of ``select *``. Here's an example:

.. code-block:: bash

    echo '[{"name": "Azi"}, {"name": "Suna"}]' | \
        sqlite-utils insert chickens.db chickens -
    sqlite-utils schema chickens.db

.. code-block:: output

    CREATE TABLE "chickens" (
       "name" TEXT
    );

.. code-block:: bash

    sqlite-utils chickens.db 'select * from chickens'

.. code-block:: output

    [{"name": "Azi"},
     {"name": "Suna"}]

.. code-block:: bash

    sqlite-utils chickens.db 'select rowid, * from chickens'

.. code-block:: output

    [{"rowid": 1, "name": "Azi"},
     {"rowid": 2, "name": "Suna"}]

You can use ``sqlite-utils transform ... --pk id`` to add a primary key column called ``id`` to the table. The primary key will be created as an ``INTEGER PRIMARY KEY`` and the existing ``rowid`` values will be copied across to it. It will automatically increment as new rows are added to the table:

.. code-block:: bash

    sqlite-utils transform chickens.db chickens --pk id

.. code-block:: bash

    sqlite-utils schema chickens.db

.. code-block:: output

    CREATE TABLE "chickens" (
       "id" INTEGER PRIMARY KEY,
       "name" TEXT
    );

.. code-block:: bash

    sqlite-utils chickens.db 'select * from chickens'

.. code-block:: output

    [{"id": 1, "name": "Azi"},
     {"id": 2, "name": "Suna"}]

.. code-block:: bash

    echo '{"name": "Cardi"}' | sqlite-utils insert chickens.db chickens -

.. code-block:: bash

    sqlite-utils chickens.db 'select * from chickens'

.. code-block:: output

    [{"id": 1, "name": "Azi"},
     {"id": 2, "name": "Suna"},
     {"id": 3, "name": "Cardi"}]

.. _cli_extract:

Extracting columns into a separate table
========================================

The ``sqlite-utils extract`` command can be used to extract specified columns into a separate table.

Take a look at the Python API documentation for :ref:`python_api_extract` for a detailed description of how this works, including examples of table schemas before and after running an extraction operation.

Rows where every extracted column is ``null`` are not extracted - those rows get a ``null`` value in their new foreign key column and no record is created for them in the lookup table.

The command takes a database, table and one or more columns that should be extracted. To extract the ``species`` column from the ``trees`` table you would run:

.. code-block:: bash

    sqlite-utils extract my.db trees species

This would produce the following schema:

.. code-block:: sql

    CREATE TABLE "trees" (
        "id" INTEGER PRIMARY KEY,
        "TreeAddress" TEXT,
        "species_id" INTEGER,
        FOREIGN KEY(species_id) REFERENCES species(id)
    );
    CREATE TABLE "species" (
        "id" INTEGER PRIMARY KEY,
        "species" TEXT
    );
    CREATE UNIQUE INDEX "idx_species_species"
        ON "species" ("species");

The command takes the following options:

``--table TEXT``
    The name of the lookup to extract columns to. This defaults to using the name of the columns that are being extracted.

``--fk-column TEXT``
    The name of the foreign key column to add to the table. Defaults to ``columnname_id``.

``--rename <TEXT TEXT>``
    Use this option to rename the columns created in the new lookup table.

``--silent``
    Don't display the progress bar.

Here's a more complex example that makes use of these options. It converts `this CSV file <https://github.com/wri/global-power-plant-database/blob/232a666653e14d803ab02717efc01cdd437e7601/output_database/global_power_plant_database.csv>`__ full of global power plants into SQLite, then extracts the ``country`` and ``country_long`` columns into a separate ``countries`` table:

.. code-block:: bash

    wget 'https://github.com/wri/global-power-plant-database/blob/232a6666/output_database/global_power_plant_database.csv?raw=true'
    sqlite-utils insert global.db power_plants \
        'global_power_plant_database.csv?raw=true' --csv
    # Extract those columns:
    sqlite-utils extract global.db power_plants country country_long \
        --table countries \
        --fk-column country_id \
        --rename country_long name

After running the above, the command ``sqlite-utils schema global.db`` reveals the following schema:

.. code-block:: sql

    CREATE TABLE "countries" (
       "id" INTEGER PRIMARY KEY,
       "country" TEXT,
       "name" TEXT
    );
    CREATE TABLE "power_plants" (
       "country_id" INTEGER,
       "name" TEXT,
       "gppd_idnr" TEXT,
       "capacity_mw" TEXT,
       "latitude" TEXT,
       "longitude" TEXT,
       "primary_fuel" TEXT,
       "other_fuel1" TEXT,
       "other_fuel2" TEXT,
       "other_fuel3" TEXT,
       "commissioning_year" TEXT,
       "owner" TEXT,
       "source" TEXT,
       "url" TEXT,
       "geolocation_source" TEXT,
       "wepp_id" TEXT,
       "year_of_capacity_data" TEXT,
       "generation_gwh_2013" TEXT,
       "generation_gwh_2014" TEXT,
       "generation_gwh_2015" TEXT,
       "generation_gwh_2016" TEXT,
       "generation_gwh_2017" TEXT,
       "generation_data_source" TEXT,
       "estimated_generation_gwh" TEXT,
       FOREIGN KEY("country_id") REFERENCES "countries"("id")
    );
    CREATE UNIQUE INDEX "idx_countries_country_name"
        ON "countries" ("country", "name");

.. note::
    In Python: :ref:`table.extract() <python_api_extract>`  CLI reference: :ref:`sqlite-utils extract <cli_ref_extract>`

.. _cli_create_view:

Creating views
==============

You can create a view using the ``create-view`` command:

.. code-block:: bash

    sqlite-utils create-view mydb.db version "select sqlite_version()"

.. code-block:: bash

    sqlite-utils mydb.db "select * from version"

.. code-block:: output

    [{"sqlite_version()": "3.31.1"}]

Use ``--replace`` to replace an existing view of the same name, and ``--ignore`` to do nothing if a view already exists.

.. note::
    In Python: :ref:`db.create_view() <python_api_create_view>`  CLI reference: :ref:`sqlite-utils create-view <cli_ref_create_view>`

.. _cli_drop_view:

Dropping views
==============

You can drop a view using the ``drop-view`` command:

.. code-block:: bash

    sqlite-utils drop-view myview

Use ``--ignore`` to ignore the error if the view does not exist.

.. note::
    In Python: :ref:`view.drop() <python_api_drop>`  CLI reference: :ref:`sqlite-utils drop-view <cli_ref_drop_view>`

.. _cli_add_column:

Adding columns
==============

You can add a column using the ``add-column`` command:

.. code-block:: bash

    sqlite-utils add-column mydb.db mytable nameofcolumn text

The last argument here is the type of the column to be created. This can be one of:

- ``text`` or ``str``
- ``integer`` or ``int``
- ``float``
- ``blob`` or ``bytes``

This argument is optional and defaults to ``text``.

You can add a column that is a foreign key reference to another table using the ``--fk`` option:

.. code-block:: bash

    sqlite-utils add-column mydb.db dogs species_id --fk species

This will automatically detect the name of the primary key on the species table and use that (and its type) for the new column.

You can explicitly specify the column you wish to reference using ``--fk-col``:

.. code-block:: bash

    sqlite-utils add-column mydb.db dogs species_id --fk species --fk-col ref

You can set a ``NOT NULL DEFAULT 'x'`` constraint on the new column using ``--not-null-default``:

.. code-block:: bash

    sqlite-utils add-column mydb.db dogs friends_count integer --not-null-default 0

.. note::
    In Python: :ref:`table.add_column() <python_api_add_column>`  CLI reference: :ref:`sqlite-utils add-column <cli_ref_add_column>`

.. _cli_add_column_alter:

Adding columns automatically on insert/update
=============================================

You can use the ``--alter`` option to automatically add new columns if the data you are inserting or upserting is of a different shape:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs new-dogs.json --pk=id --alter

.. note::
    In Python: :ref:`table.insert(..., alter=True) <python_api_add_column_alter>`

.. _cli_add_foreign_key:

Adding foreign key constraints
==============================

The ``add-foreign-key`` command can be used to add new foreign key references to an existing table - something which SQLite's ``ALTER TABLE`` command does not support.

To add a foreign key constraint pointing the ``books.author_id`` column to ``authors.id`` in another table, do this:

.. code-block:: bash

    sqlite-utils add-foreign-key books.db books author_id authors id

If you omit the other table and other column references ``sqlite-utils`` will attempt to guess them - so the above example could instead look like this:

.. code-block:: bash

    sqlite-utils add-foreign-key books.db books author_id

Add ``--ignore`` to ignore an existing foreign key (as opposed to returning an error):

.. code-block:: bash

    sqlite-utils add-foreign-key books.db books author_id --ignore

See :ref:`python_api_add_foreign_key` in the Python API documentation for further details, including how the automatic table guessing mechanism works.

.. note::
    In Python: :ref:`table.add_foreign_key() <python_api_add_foreign_key>`  CLI reference: :ref:`sqlite-utils add-foreign-key <cli_ref_add_foreign_key>`

.. _cli_add_foreign_keys:

Adding multiple foreign keys at once
------------------------------------

Adding a foreign key requires a ``VACUUM``. On large databases this can be an expensive operation, so if you are adding multiple foreign keys you can combine them into one operation (and hence one ``VACUUM``) using ``add-foreign-keys``:

.. code-block:: bash

    sqlite-utils add-foreign-keys books.db \
        books author_id authors id \
        authors country_id countries id

When you are using this command each foreign key needs to be defined in full, as four arguments - the table, column, other table and other column.

.. note::
    In Python: :ref:`db.add_foreign_keys() <python_api_add_foreign_keys>`  CLI reference: :ref:`sqlite-utils add-foreign-keys <cli_ref_add_foreign_keys>`

.. _cli_index_foreign_keys:

Adding indexes for all foreign keys
-----------------------------------

If you want to ensure that every foreign key column in your database has a corresponding index, you can do so like this:

.. code-block:: bash

    sqlite-utils index-foreign-keys books.db

.. note::
    In Python: :ref:`db.index_foreign_keys() <python_api_index_foreign_keys>`  CLI reference: :ref:`sqlite-utils index-foreign-keys <cli_ref_index_foreign_keys>`

.. _cli_defaults_not_null:

Setting defaults and not null constraints
=========================================

You can use the ``--not-null`` and ``--default`` options (to both ``insert`` and ``upsert``) to specify columns that should be ``NOT NULL`` or to set database defaults for one or more specific columns:

.. code-block:: bash

    sqlite-utils insert dogs.db dogs_with_scores dogs-with-scores.json \
        --not-null=age \
        --not-null=name \
        --default age 2 \
        --default score 5

.. note::
    In Python: :ref:`not_null= and defaults= arguments <python_api_defaults_not_null>`

.. _cli_create_index:

Creating indexes
================

You can add an index to an existing table using the ``create-index`` command:

.. code-block:: bash

    sqlite-utils create-index mydb.db mytable col1 [col2...]

This can be used to create indexes against a single column or multiple columns.

The name of the index will be automatically derived from the table and columns. To specify a different name, use ``--name=name_of_index``.

Use the ``--unique`` option to create a unique index.

Use ``--if-not-exists`` to avoid attempting to create the index if one with that name already exists.

To add an index on a column in descending order, prefix the column with a hyphen. Since this can be confused for a command-line option you need to construct that like this:

.. code-block:: bash

    sqlite-utils create-index mydb.db mytable -- col1 -col2 col3

This will create an index on that table on ``(col1, col2 desc, col3)``.

If your column names are already prefixed with a hyphen you'll need to manually execute a ``CREATE INDEX`` SQL statement to add indexes to them rather than using this tool.

Add the ``--analyze`` option to run ``ANALYZE`` against the index after it has been created.

.. note::
    In Python: :ref:`table.create_index() <python_api_create_index>`  CLI reference: :ref:`sqlite-utils create-index <cli_ref_create_index>`

.. _cli_drop_index:

Dropping indexes
================

You can drop an index from an existing table using the ``drop-index`` command:

.. code-block:: bash

    sqlite-utils drop-index mydb.db mytable idx_mytable_col1

Use ``--ignore`` to ignore the error if the index does not exist on that table.

.. note::
    In Python: :ref:`table.drop_index() <python_api_create_index>`  CLI reference: :ref:`sqlite-utils drop-index <cli_ref_drop_index>`

.. _cli_fts:

Configuring full-text search
============================

You can enable SQLite full-text search on a table and a set of columns like this:

.. code-block:: bash

    sqlite-utils enable-fts mydb.db documents title summary

This will use SQLite's FTS5 module by default. Use ``--fts4`` if you want to use FTS4:

.. code-block:: bash

    sqlite-utils enable-fts mydb.db documents title summary --fts4

The ``enable-fts`` command will populate the new index with all existing documents. If you later add more documents you will need to use ``populate-fts`` to cause them to be indexed as well:

.. code-block:: bash

    sqlite-utils populate-fts mydb.db documents title summary

A better solution here is to use database triggers. You can set up database triggers to automatically update the full-text index using the ``--create-triggers`` option when you first run ``enable-fts``:

.. code-block:: bash

    sqlite-utils enable-fts mydb.db documents title summary --create-triggers

To set a custom FTS tokenizer, e.g. to enable Porter stemming, use ``--tokenize=``:

.. code-block:: bash

    sqlite-utils populate-fts mydb.db documents title summary --tokenize=porter

To remove the FTS tables and triggers you created, use ``disable-fts``:

.. code-block:: bash

    sqlite-utils disable-fts mydb.db documents

To rebuild one or more FTS tables (see :ref:`python_api_fts_rebuild`), use ``rebuild-fts``:

.. code-block:: bash

    sqlite-utils rebuild-fts mydb.db documents

You can rebuild every FTS table by running ``rebuild-fts`` without passing any table names:

.. code-block:: bash

    sqlite-utils rebuild-fts mydb.db

.. note::
    In Python: :ref:`table.enable_fts() <python_api_fts_enable>`  CLI reference: :ref:`sqlite-utils enable-fts <cli_ref_enable_fts>`

.. _cli_search:

Executing searches
==================

Once you have configured full-text search for a table, you can search it using ``sqlite-utils search``:

.. code-block:: bash

    sqlite-utils search mydb.db documents searchterm

This command accepts the same output options as ``sqlite-utils query``: ``--table``, ``--csv``, ``--tsv``, ``--nl`` etc.

By default it shows the most relevant matches first. You can specify a different sort order using the ``-o`` option, which can take a column or a column followed by ``desc``:

.. code-block:: bash

    # Sort by rowid
    sqlite-utils search mydb.db documents searchterm -o rowid
    # Sort by created in descending order
    sqlite-utils search mydb.db documents searchterm -o 'created desc'

SQLite `advanced search syntax <https://www.sqlite.org/fts5.html#full_text_query_syntax>`__ is enabled by default. To run a search with automatic quoting applied to the terms to avoid them being potentially interpreted as advanced search syntax use the ``--quote`` option.

You can specify a subset of columns to be returned using the ``-c`` option one or more times:

.. code-block:: bash

    sqlite-utils search mydb.db documents searchterm -c title -c created

By default all search results will be returned. You can use ``--limit 20`` to return just the first 20 results.

Use the ``--sql`` option to output the SQL that would be executed, rather than running the query:

.. code-block:: bash

    sqlite-utils search mydb.db documents searchterm --sql

.. code-block:: output

    with original as (
        select
            rowid,
            *
        from "documents"
    )
    select
        "original".*
    from
        "original"
        join "documents_fts" on "original".rowid = "documents_fts".rowid
    where
        "documents_fts" match :query
    order by
        "documents_fts".rank

.. note::
    In Python: :ref:`table.search() <python_api_fts_search>`  CLI reference: :ref:`sqlite-utils search <cli_ref_search>`

.. _cli_enable_counts:

Enabling cached counts
======================

``select count(*)`` queries can take a long time against large tables. ``sqlite-utils`` can speed these up by adding triggers to maintain a ``_counts`` table, see :ref:`python_api_cached_table_counts` for details.

The ``sqlite-utils enable-counts`` command can be used to configure these triggers, either for every table in the database or for specific tables.

.. code-block:: bash

    # Configure triggers for every table in the database
    sqlite-utils enable-counts mydb.db

    # Configure triggers just for specific tables
    sqlite-utils enable-counts mydb.db table1 table2

If the ``_counts`` table ever becomes out-of-sync with the actual table counts you can repair it using the ``reset-counts`` command:

.. code-block:: bash

    sqlite-utils reset-counts mydb.db

.. note::
    In Python: :ref:`table.enable_counts() <python_api_cached_table_counts>`  CLI reference: :ref:`sqlite-utils enable-counts <cli_ref_enable_counts>`

.. _cli_analyze:

Optimizing index usage with ANALYZE
===================================

The `SQLite ANALYZE command <https://www.sqlite.org/lang_analyze.html>`__ builds a table of statistics which the query planner can use to make better decisions about which indexes to use for a given query.

You should run ``ANALYZE`` if your database is large and you do not think your indexes are being efficiently used.

To run ``ANALYZE`` against every index in a database, use this:

.. code-block:: bash

    sqlite-utils analyze mydb.db

You can run it against specific tables, or against specific named indexes, by passing them as optional arguments:

.. code-block:: bash

    sqlite-utils analyze mydb.db mytable idx_mytable_name

You can also run ``ANALYZE`` as part of another command using the ``--analyze`` option. This is supported by the ``create-index``, ``insert`` and ``upsert`` commands.

.. note::
    In Python: :ref:`db.analyze() <python_api_analyze>`  CLI reference: :ref:`sqlite-utils analyze <cli_ref_analyze>`

.. _cli_vacuum:

Vacuum
======

You can run VACUUM to optimize your database like so:

.. code-block:: bash

    sqlite-utils vacuum mydb.db

.. note::
    In Python: :ref:`db.vacuum() <python_api_vacuum>`  CLI reference: :ref:`sqlite-utils vacuum <cli_ref_vacuum>`

.. _cli_optimize:

Optimize
========

The optimize command can dramatically reduce the size of your database if you are using SQLite full-text search. It runs OPTIMIZE against all of your FTS4 and FTS5 tables, then runs VACUUM.

If you just want to run OPTIMIZE without the VACUUM, use the ``--no-vacuum`` flag.

.. code-block:: bash

    # Optimize all FTS tables and then VACUUM
    sqlite-utils optimize mydb.db

    # Optimize but skip the VACUUM
    sqlite-utils optimize --no-vacuum mydb.db

To optimize specific tables rather than every FTS table, pass those tables as extra arguments:

.. code-block:: bash

    sqlite-utils optimize mydb.db table_1 table_2

.. note::
    In Python: :ref:`table.optimize() <python_api_fts_optimize>`  CLI reference: :ref:`sqlite-utils optimize <cli_ref_optimize>`

.. _cli_wal:

WAL mode
========

You can enable `Write-Ahead Logging <https://www.sqlite.org/wal.html>`__ for a database file using the ``enable-wal`` command:

.. code-block:: bash

    sqlite-utils enable-wal mydb.db

You can disable WAL mode using ``disable-wal``:

.. code-block:: bash

    sqlite-utils disable-wal mydb.db

Both of these commands accept one or more database files as arguments.

.. note::
    In Python: :ref:`db.enable_wal() and db.disable_wal() <python_api_wal>`  CLI reference: :ref:`sqlite-utils enable-wal <cli_ref_enable_wal>`

.. _cli_dump:

Dumping the database to SQL
===========================

The ``dump`` command outputs a SQL dump of the schema and full contents of the specified database file:

.. code-block:: bash

    sqlite-utils dump mydb.db
    BEGIN TRANSACTION;
    CREATE TABLE ...
    ...
    COMMIT;

.. note::
    In Python: :ref:`db.iterdump() <python_api_itedump>`  CLI reference: :ref:`sqlite-utils dump <cli_ref_dump>`

.. _cli_load_extension:

Loading SQLite extensions
=========================

Many of these commands have the ability to load additional SQLite extensions using the ``--load-extension=/path/to/extension`` option - use ``--help`` to check for support, e.g. ``sqlite-utils rows --help``.

This option can be applied multiple times to load multiple extensions.

Since `SpatiaLite <https://www.gaia-gis.it/fossil/libspatialite/index>`__ is commonly used with SQLite, the value ``spatialite`` is special: it will search for SpatiaLite in the most common installation locations, saving you from needing to remember exactly where that module is located:

.. code-block:: bash

    sqlite-utils memory "select spatialite_version()" --load-extension=spatialite

.. code-block:: output

    [{"spatialite_version()": "4.3.0a"}]

.. _cli_spatialite:

SpatiaLite helpers
==================

`SpatiaLite <https://www.gaia-gis.it/fossil/libspatialite/home>`_ adds geographic capability to SQLite (similar to how PostGIS builds on PostgreSQL). The `SpatiaLite cookbook <http://www.gaia-gis.it/gaia-sins/spatialite-cookbook-5/index.html>`__ is a good resource for learning what's possible with it.

You can convert an existing table to a geographic table by adding a geometry column, use the ``sqlite-utils add-geometry-column`` command:

.. code-block:: bash

    sqlite-utils add-geometry-column spatial.db locations geometry --type POLYGON --srid 4326

The table (``locations`` in the example above) must already exist before adding a geometry column. Use ``sqlite-utils create-table`` first, then ``add-geometry-column``.

Use the ``--type`` option to specify a geometry type. By default, ``add-geometry-column`` uses a generic ``GEOMETRY``, which will work with any type, though it may not be supported by some desktop GIS applications. 

Eight (case-insensitive) types are allowed:

* POINT
* LINESTRING
* POLYGON
* MULTIPOINT
* MULTILINESTRING
* MULTIPOLYGON
* GEOMETRYCOLLECTION
* GEOMETRY

.. note::
    In Python: :ref:`table.add_geometry_column() <python_api_gis_add_geometry_column>`  CLI reference: :ref:`sqlite-utils add-geometry-column <cli_ref_add_geometry_column>`

.. _cli_spatialite_indexes:

Adding spatial indexes
----------------------

Once you have a geometry column, you can speed up bounding box queries by adding a spatial index:

.. code-block:: bash

    sqlite-utils create-spatial-index spatial.db locations geometry

See this `SpatiaLite Cookbook recipe <http://www.gaia-gis.it/gaia-sins/spatialite-cookbook-5/cookbook_topics.03.html#topic_Wonderful_RTree_Spatial_Index>`__ for examples of how to use a spatial index.

.. note::
    In Python: :ref:`table.create_spatial_index() <python_api_gis_create_spatial_index>`  CLI reference: :ref:`sqlite-utils create-spatial-index <cli_ref_create_spatial_index>`

.. _cli_install:

Installing packages
===================

The :ref:`convert command <cli_convert>` and the :ref:`insert -\\-convert <cli_insert_convert>` and :ref:`query -\\-functions <cli_query_functions>` options can be provided with a Python script that imports additional modules from the ``sqlite-utils`` environment.

You can install packages from PyPI directly into the correct environment using ``sqlite-utils install <package>``. This is a wrapper around ``pip install``.

.. code-block:: bash

    sqlite-utils install beautifulsoup4

Use ``-U`` to upgrade an existing package.

.. _cli_uninstall:

Uninstalling packages
=====================

You can uninstall packages that were installed using ``sqlite-utils install`` with ``sqlite-utils uninstall <package>``:

.. code-block:: bash

    sqlite-utils uninstall beautifulsoup4

Use ``-y`` to skip the request for confirmation.

```

### `docs/codespell-ignore-words.txt`

```txt
doub

```

### `docs/conf.py`

```py
import inspect
import sys
from pathlib import Path
from subprocess import PIPE, CalledProcessError, Popen, check_output

# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx.ext.linkcode",
]
autodoc_member_order = "bysource"
autodoc_typehints = "description"

extlinks = {
    "issue": ("https://github.com/simonw/sqlite-utils/issues/%s", "#%s"),
}


def _linkcode_git_ref():
    try:
        return check_output(["git", "rev-parse", "HEAD"]).decode("utf8").strip()
    except (CalledProcessError, OSError):
        return "main"


def linkcode_resolve(domain, info):
    if domain != "py":
        return None

    module_name = info.get("module")
    if not module_name or module_name.split(".")[0] != "sqlite_utils":
        return None

    module = sys.modules.get(module_name)
    if module is None:
        return None

    obj = module
    for part in info.get("fullname", "").split("."):
        obj = getattr(obj, part, None)
        if obj is None:
            return None

    if isinstance(obj, property):
        obj = obj.fget

    try:
        obj = inspect.unwrap(obj)
        source_file = inspect.getsourcefile(obj)
        _, line_number = inspect.getsourcelines(obj)
    except (OSError, TypeError, ValueError):
        return None

    if source_file is None:
        return None

    try:
        filename = Path(source_file).resolve().relative_to(Path(__file__).parent.parent)
    except ValueError:
        return None

    return (
        "https://github.com/simonw/sqlite-utils/blob/"
        f"{_linkcode_git_ref()}/{filename}#L{line_number}"
    )


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "sqlite-utils"
copyright = "2018-2022, Simon Willison"
author = "Simon Willison"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
pipe = Popen("git describe --tags --always", stdout=PIPE, shell=True)
git_version = pipe.stdout.read().decode("utf8") if pipe.stdout else ""

if git_version:
    version = git_version.rsplit("-", 1)[0]
    release = git_version
else:
    version = ""
    release = ""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Only syntax highlight of code-block is used:
highlight_language = "none"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
html_title = "sqlite-utils"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_js_files = ["js/custom.js"]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "sqlite-utils-doc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "sqlite-utils.tex",
        "sqlite-utils documentation",
        "Simon Willison",
        "manual",
    )
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "sqlite-utils", "sqlite-utils documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "sqlite-utils",
        "sqlite-utils documentation",
        author,
        "sqlite-utils",
        "Python library for manipulating SQLite databases",
        "Miscellaneous",
    )
]

```

### `docs/contributing.rst`

```rst
.. _contributing:

==============
 Contributing
==============

Development of ``sqlite-utils`` takes place in the `sqlite-utils GitHub repository <https://github.com/simonw/sqlite-utils>`__.

All improvements to the software should start with an issue. Read `How I build a feature <https://simonwillison.net/2022/Jan/12/how-i-build-a-feature/>`__ for a detailed description of the recommended process for building bug fixes or enhancements.

.. _contributing_checkout:

Obtaining the code
==================

To work on this library locally, first checkout the code::

    git clone git@github.com:simonw/sqlite-utils
    cd sqlite-utils

Use ``uv run`` to run the development version of the tool::

    uv run sqlite-utils --help

.. _contributing_tests:

Running the tests
=================

Use ``uv run`` to run the tests::

    uv run pytest

.. _contributing_docs:

Building the documentation
==========================

To build the documentation run this command::

    uv run make livehtml --directory docs

This will start a server on port 8000 that will serve the documentation and live-reload any time you make an edit to a ``.rst`` file.

The `cog <https://github.com/nedbat/cog>`__ tool is used to maintain portions of the documentation. You can run it like so::

    uv run cog -r docs/*.rst

.. _contributing_linting:

Linting and formatting
======================

``sqlite-utils`` uses `Black <https://black.readthedocs.io/>`__ for code formatting, and `flake8 <https://flake8.pycqa.org/>`__ and `mypy <https://mypy.readthedocs.io/>`__ for linting and type checking::

    uv run black .

Linting tools can be run like this::

    uv run flake8
    uv run mypy sqlite_utils

All three of these tools are run by our CI mechanism against every commit and pull request.

.. _contributing_just:

Using Just
==========

If you install `Just <https://github.com/casey/just>`__ you can use it to manage your local development environment.

To run all of the tests and linters::

    just

To run tests, or run a specific test module or test by name::

    just test # All tests
    just test tests/test_cli_memory.py # Just this module
    just test -k test_memory_no_detect_types # Just this test

To run just the linters::

    just lint

To apply Black to your code::

    just black

To update documentation using Cog::

    just cog

To run the live documentation server (this will run Cog first)::

    just docs

And to list all available commands::

    just -l

.. _release_process:

Release process
===============

Releases are performed using tags. When a new release is published on GitHub, a `GitHub Actions workflow <https://github.com/simonw/sqlite-utils/blob/main/.github/workflows/publish.yml>`__ will perform the following:

* Run the unit tests against all supported Python versions. If the tests pass...
* Build a wheel bundle of the underlying Python source code
* Push that new wheel up to PyPI: https://pypi.org/project/sqlite-utils/

To deploy new releases you will need to have push access to the GitHub repository.

``sqlite-utils`` follows `Semantic Versioning <https://semver.org/>`__::

    major.minor.patch

We increment ``major`` for backwards-incompatible releases.

We increment ``minor`` for new features.

We increment ``patch`` for bugfix releass.

To release a new version, first create a commit that updates the version number in ``pyproject.toml`` and the :ref:`the changelog <changelog>` with highlights of the new version. An example `commit can be seen here <https://github.com/simonw/sqlite-utils/commit/b491f22d817836829965516983a3f4c3c72c05fc>`__::

    # Update changelog
    git commit -m " Release 3.29

    Refs #423, #458, #467, #469, #470, #471, #472, #475" -a
    git push

Referencing the issues that are part of the release in the commit message ensures the name of the release shows up on those issue pages, e.g. `here <https://github.com/simonw/sqlite-utils/issues/458#ref-commit-b491f22>`__.

You can generate the list of issue references for a specific release by copying and pasting text from the release notes or GitHub changes-since-last-release view into this `Extract issue numbers from pasted text <https://observablehq.com/@simonw/extract-issue-numbers-from-pasted-text>`__ tool.

To create the tag for the release, create `a new release <https://github.com/simonw/sqlite-utils/releases/new>`__ on GitHub matching the new version number. You can convert the release notes to Markdown by copying and pasting the rendered HTML into this `Paste to Markdown tool <https://euangoddard.github.io/clipboard2markdown/>`__.

```

### `docs/index.rst`

```rst
=======================
 sqlite-utils |version|
=======================

|PyPI| |Changelog| |CI| |License| |discord|

.. |PyPI| image:: https://img.shields.io/pypi/v/sqlite-utils.svg
   :target: https://pypi.org/project/sqlite-utils/
.. |Changelog| image:: https://img.shields.io/github/v/release/simonw/sqlite-utils?include_prereleases&label=changelog
   :target: https://sqlite-utils.datasette.io/en/stable/changelog.html
.. |CI| image:: https://github.com/simonw/sqlite-utils/workflows/Test/badge.svg
   :target: https://github.com/simonw/sqlite-utils/actions
.. |License| image:: https://img.shields.io/badge/license-Apache%202.0-blue.svg
   :target: https://github.com/simonw/sqlite-utils/blob/main/LICENSE
.. |discord| image:: https://img.shields.io/discord/823971286308356157?label=discord
   :target: https://discord.gg/Ass7bCAMDw

*CLI tool and Python library for manipulating SQLite databases*

This library and command-line utility helps create SQLite databases from an existing collection of data.

Most of the functionality is available as either a Python API or through the ``sqlite-utils`` command-line tool.

sqlite-utils is not intended to be a full ORM: the focus is utility helpers to make creating the initial database and populating it with data as productive as possible.

It is designed as a useful complement to `Datasette <https://datasette.io/>`_.

`Cleaning data with sqlite-utils and Datasette <https://datasette.io/tutorials/clean-data>`_ provides a tutorial introduction (and accompanying ten minute video) about using this tool.

Contents
--------

.. toctree::
   :maxdepth: 3

   installation
   cli
   python-api
   migrations
   plugins
   reference
   cli-reference
   upgrading
   contributing
   changelog

```

### `docs/installation.rst`

```rst
.. _installation:

==============
 Installation
==============

``sqlite-utils`` is tested on Linux, macOS and Windows.

.. _installation_homebrew:

Using Homebrew
==============

The :ref:`sqlite-utils command-line tool <cli>` can be installed on macOS using Homebrew::

    brew install sqlite-utils

If you have it installed and want to upgrade to the most recent release, you can run::

    brew upgrade sqlite-utils

Then run ``sqlite-utils --version`` to confirm the installed version.

.. _installation_pip:

Using pip
=========

The `sqlite-utils package <https://pypi.org/project/sqlite-utils/>`__ on PyPI includes both the :ref:`sqlite_utils Python library <python_api>` and the ``sqlite-utils`` command-line tool. You can install them using ``pip`` like so::

    pip install sqlite-utils

.. _installation_pipx:

Using pipx
==========

`pipx <https://pypi.org/project/pipx/>`__ is a tool for installing Python command-line applications in their own isolated environments. You can use ``pipx`` to install the ``sqlite-utils`` command-line tool like this::

    pipx install sqlite-utils

.. _installation_sqlite3_alternatives:

Alternatives to sqlite3
=======================

By default, ``sqlite-utils`` uses the ``sqlite3`` package bundled with the Python standard library.

Depending on your operating system, this may come with some limitations.

On some platforms the ability to load additional extensions (via ``conn.load_extension(...)`` or ``--load-extension=/path/to/extension``) may be disabled.

You may also see the error ``sqlite3.OperationalError: table sqlite_master may not be modified`` when trying to alter an existing table.

You can work around these limitations by installing the `pysqlite3 <https://pypi.org/project/pysqlite3/>`__ package, which provides a drop-in replacement for the standard library ``sqlite3`` module but with a recent version of SQLite and full support for loading extensions.

To install ``pysqlite3`` run the following:

.. code-block:: bash

    sqlite-utils install pysqlite3

``pysqlite3`` does not provide an implementation of the ``.iterdump()`` method. To use that method (see :ref:`python_api_itedump`) or the ``sqlite-utils dump`` command you should also install the ``sqlite-dump`` package:

.. code-block:: bash

    sqlite-utils install sqlite-dump

.. _installation_completion:

Setting up shell completion
===========================

You can configure shell tab completion for the ``sqlite-utils`` command using these commands.

For ``bash``:

.. code-block:: bash

    eval "$(_SQLITE_UTILS_COMPLETE=bash_source sqlite-utils)"

For ``zsh``:

.. code-block:: zsh

    eval "$(_SQLITE_UTILS_COMPLETE=zsh_source sqlite-utils)"

Add this code to ``~/.zshrc`` or ``~/.bashrc`` to automatically run it when you start a new shell.

See `the Click documentation <https://click.palletsprojects.com/en/8.1.x/shell-completion/>`__ for more details.

```

### `docs/Makefile`

```
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = sqlite-utils
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	sphinx-autobuild -a -b html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(0) --watch ../sqlite_utils

```

### `docs/migrations.rst`

```rst
.. _migrations:

=====================
 Database migrations
=====================

``sqlite-utils`` includes a migration system for applying repeatable changes to SQLite database files.

A migration is a Python function that receives a :class:`sqlite_utils.Database` instance and then executes Python code to modify that database - creating or transforming tables, adding indexes, inserting rows, or any other operation supported by SQLite.

Migrations are grouped into named sets using the :class:`sqlite_utils.Migrations` class, and each applied migration is recorded in the ``_sqlite_migrations`` table in that database.

This means you can run the migrate operation multiple times and it will only apply migrations that have not previously been recorded.

.. _migrations_define:

Defining migrations
===================

Ordered migration sets are defined by first creating a :class:`sqlite_utils.Migrations` object.

Individual migrations are Python functions that are then registered with that migration set. Each migration function is passed a single argument that is a :ref:`sqlite_utils.Database <reference_db_database>` instance.

The name passed to ``Migrations("creatures")`` identifies that set of migrations. Use a name that is unique for your project, since multiple migration sets can be applied to the same database.

Here is a simple example of a ``migrations.py`` file which creates a table, then adds an extra column to that table in a second migration:

.. code-block:: python

    from sqlite_utils import Migrations

    migrations = Migrations("creatures")

    @migrations()
    def create_table(db):
        db["creatures"].create(
            {"id": int, "name": str, "species": str},
            pk="id",
        )

    @migrations()
    def add_weight(db):
        db["creatures"].add_column("weight", float)

.. _migrations_python:

Applying migrations in Python
=============================

Once you have a ``Migrations(name)`` collection with one or more migrations registered to it, you can execute them in Python code like this:

.. code-block:: python

    from sqlite_utils import Database

    db = Database("creatures.db")
    migrations.apply(db)

Running ``migrations.apply(db)`` repeatedly is safe. Migrations that already have a matching ``migration_set`` and ``name`` row in ``_sqlite_migrations`` will be skipped.

Migration functions are applied in the order that they were registered. The function name is used as the migration name unless you pass one explicitly:

.. code-block:: python

    @migrations(name="001_create_table")
    def create_table(db):
        db["creatures"].create({"id": int, "name": str}, pk="id")

When you apply a set of migrations you can stop part way through by specifying a ``stop_before=`` migration name:

.. code-block:: python

    migrations.apply(db, stop_before="add_weight")

.. _migrations_transactions:

Migrations and transactions
===========================

Each migration runs inside a transaction, together with the ``_sqlite_migrations`` record of it having been applied. If a migration function raises an exception, everything it did is rolled back, no record is written and the migration stays pending - so fixing the error and re-applying will run that migration again from a clean state. Migrations that completed earlier in the same ``apply()`` run stay applied.

Some operations cannot run inside a transaction, for example ``VACUUM`` or changing the journal mode with ``db.enable_wal()``. Register migrations like these with ``transactional=False``:

.. code-block:: python

    @migrations(transactional=False)
    def compact(db):
        db.execute("VACUUM")

A migration registered with ``transactional=False`` runs without a wrapping transaction, so if it fails part way through any changes it already made will not be rolled back, and re-applying will run the whole function again.

Avoid calling ``db.commit()`` or otherwise managing transactions manually inside a transactional migration - register the migration with ``transactional=False`` if it needs to control its own transactions. Using ``with db.atomic():`` blocks inside a migration is fine: they nest as savepoints within the migration's transaction, so the migration as a whole still commits or rolls back as a single unit. See :ref:`python_api_transactions`.

Applying migrations using the CLI
=================================

Run migrations using the ``sqlite-utils migrate`` command:

.. code-block:: bash

    sqlite-utils migrate creatures.db path/to/migrations.py

The first argument is the database file. The remaining arguments can be paths to migration files or directories containing migration files.

If you omit migration paths, ``sqlite-utils`` searches the current directory and subdirectories for files called ``migrations.py``:

.. code-block:: bash

    sqlite-utils migrate creatures.db

You can also pass a directory. Every ``migrations.py`` file in that directory tree will be considered:

.. code-block:: bash

    sqlite-utils migrate creatures.db path/to/project/

Running the command repeatedly is safe. Migrations that already have a matching ``migration_set`` and ``name`` row in ``_sqlite_migrations`` will be skipped.

Listing migrations
==================

Use ``--list`` to show applied and pending migrations without running them. This is a read-only operation - it will not create the database file or the ``_sqlite_migrations`` table:

.. code-block:: bash

    sqlite-utils migrate creatures.db --list

Example output:

.. code-block:: output

    Migrations for: creatures

      Applied:
        create_table - 2026-06-09 17:23:12.048092+00:00
        add_weight - 2026-06-09 17:23:12.051249+00:00

      Pending:
        add_age

Stopping before a migration
===========================

When applying migrations using the CLI, you can stop before a named migration:

.. code-block:: bash

    sqlite-utils migrate creatures.db path/to/migrations.py --stop-before add_weight

This applies any pending migrations before ``add_weight`` and leaves ``add_weight`` and later migrations pending. An unqualified migration name matches in any migration set.

You can also target a specific migration set using ``migration_set:migration_name``. This is useful if a migrations file contains more than one migration set, or if multiple sets use the same migration name:

.. code-block:: bash

    sqlite-utils migrate creatures.db path/to/migrations.py \
      --stop-before creatures:add_weight \
      --stop-before sales:drop_index

The ``--stop-before`` option can be passed more than once.

If a ``--stop-before`` value does not match any known migration the command exits with an error, rather than silently applying everything. Naming a migration that has already been applied is also an error - stopping before it is impossible to honor - and no pending migrations are applied.

Verbose output
==============

Use ``--verbose`` or ``-v`` to show the schema before and after migrations are applied, plus a unified diff when the schema changes:

.. code-block:: bash

    sqlite-utils migrate creatures.db --verbose

Migrating from sqlite-migrate
=============================

This system uses the same migration table format as the older `sqlite-migrate <https://github.com/simonw/sqlite-migrate>`__ package. To use existing migration files directly with ``sqlite-utils``, update their import from ``sqlite_migrate`` to ``sqlite_utils``:

.. code-block:: python

    from sqlite_utils import Migrations

    migration = Migrations("creatures")

    @migration()
    def create_table(db):
        db["creatures"].create({"id": int, "name": str}, pk="id")

Python API
==========

.. autoclass:: sqlite_utils.migrations.Migrations
   :members:
   :undoc-members:
   :exclude-members: _Migration, _AppliedMigration

```

### `docs/plugins.rst`

```rst
.. _plugins:

=========
 Plugins
=========

``sqlite-utils`` supports plugins, which can be used to add extra features to the software.

Plugins can add new commands, for example ``sqlite-utils some-command ...``

Plugins can be installed using the ``sqlite-utils install`` command:

.. code-block:: bash

    sqlite-utils install sqlite-utils-name-of-plugin

You can see a JSON list of plugins that have been installed by running this:

.. code-block:: bash

    sqlite-utils plugins

Plugin hooks such as :ref:`plugins_hooks_prepare_connection` affect each instance of the ``Database`` class. You can opt-out of these plugins by creating that class instance like so:

.. code-block:: python

    db = Database(memory=True, execute_plugins=False)

.. _plugins_building:

Building a plugin
-----------------

Plugins are created in a directory named after the plugin. To create a "hello world" plugin, first create a ``hello-world`` directory:

.. code-block:: bash

    mkdir hello-world
    cd hello-world

In that folder create two files. The first is a ``pyproject.toml`` file describing the plugin:

.. code-block:: toml

    [project]
    name = "sqlite-utils-hello-world"
    version = "0.1"

    [project.entry-points.sqlite_utils]
    hello_world = "sqlite_utils_hello_world"

The ``[project.entry-points.sqlite_utils]`` section tells ``sqlite-utils`` which module to load when executing the plugin.

Then create ``sqlite_utils_hello_world.py`` with the following content:

.. code-block:: python

    import click
    import sqlite_utils

    @sqlite_utils.hookimpl
    def register_commands(cli):
        @cli.command()
        def hello_world():
            "Say hello world"
            click.echo("Hello world!")

Install the plugin in "editable" mode - so you can make changes to the code and have them picked up instantly by ``sqlite-utils`` - like this:

.. code-block:: bash

    sqlite-utils install -e .

Or pass the path to your plugin directory:

.. code-block:: bash

    sqlite-utils install -e /dev/sqlite-utils-hello-world

Now, running this should execute your new command:

.. code-block:: bash

    sqlite-utils hello-world

Your command will also be listed in the output of ``sqlite-utils --help``.

See the `LLM plugin documentation <https://llm.datasette.io/en/stable/plugins/tutorial-model-plugin.html#distributing-your-plugin>`__ for tips on distributing your plugin.

.. _plugins_hooks:

Plugin hooks
------------

Plugin hooks allow ``sqlite-utils`` to be customized.

.. _plugins_hooks_register_commands:

register_commands(cli)
~~~~~~~~~~~~~~~~~~~~~~

This hook can be used to register additional commands with the ``sqlite-utils`` CLI. It is called with the ``cli`` object, which is a ``click.Group`` instance.

Example implementation:

.. code-block:: python

    import click
    import sqlite_utils

    @sqlite_utils.hookimpl
    def register_commands(cli):
        @cli.command()
        def hello_world():
            "Say hello world"
            click.echo("Hello world!")

New commands implemented by plugins can invoke existing commands using the `context.invoke <https://click.palletsprojects.com/en/stable/api/#click.Context.invoke>`__ mechanism.

As a special niche feature, if your plugin needs to import some files and then act against an in-memory database containing those files you can forward to the :ref:`sqlite-utils memory command <cli_memory>` and pass it ``return_db=True``:

.. code-block:: python

    @cli.command()
    @click.pass_context
    @click.argument(
        "paths",
        type=click.Path(file_okay=True, dir_okay=False, allow_dash=True),
        required=False,
        nargs=-1,
    )
    def show_schema_for_files(ctx, paths):
        from sqlite_utils.cli import memory
        db = ctx.invoke(memory, paths=paths, return_db=True)
        # Now do something with that database
        click.echo(db.schema)

.. _plugins_hooks_prepare_connection:

prepare_connection(conn)
~~~~~~~~~~~~~~~~~~~~~~~~

This hook is called when a new SQLite database connection is created. You can use it to `register custom SQL functions <https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.create_function>`_, aggregates and collations. For example:

.. code-block:: python

    import sqlite_utils

    @sqlite_utils.hookimpl
    def prepare_connection(conn):
        conn.create_function(
            "hello", 1, lambda name: f"Hello, {name}!"
        )

This registers a SQL function called ``hello`` which takes a single argument and can be called like this:

.. code-block:: sql

    select hello("world"); -- "Hello, world!"

```

### `docs/reference.rst`

```rst
.. _reference:

===============
 API reference
===============

.. contents:: :local:
   :class: this-will-duplicate-information-and-it-is-still-useful-here

.. _reference_db_database:

sqlite_utils.db.Database
========================

.. autoclass:: sqlite_utils.db.Database
    :members:
    :undoc-members:
    :special-members: __getitem__
    :exclude-members: use_counts_table, execute_returning_dicts, resolve_foreign_keys

.. _reference_db_queryable:

sqlite_utils.db.Queryable
=========================

:ref:`Table <reference_db_table>` and :ref:`View <reference_db_view>` are  both subclasses of ``Queryable``, providing access to the following methods:

.. autoclass:: sqlite_utils.db.Queryable
    :members:
    :undoc-members:
    :exclude-members: execute_count

.. _reference_db_table:

sqlite_utils.db.Table
=====================

.. autoclass:: sqlite_utils.db.Table
    :members:
    :undoc-members:
    :show-inheritance:
    :exclude-members: guess_foreign_column, value_or_default, build_insert_queries_and_params, insert_chunk, add_missing_columns

.. _reference_db_view:

sqlite_utils.db.View
====================

.. autoclass:: sqlite_utils.db.View
    :members:
    :undoc-members:
    :show-inheritance:

.. _reference_db_other:

Other
=====

.. _reference_db_other_column:

sqlite_utils.db.Column
----------------------

.. autoclass:: sqlite_utils.db.Column

.. _reference_db_other_column_details:

sqlite_utils.db.ColumnDetails
-----------------------------

.. autoclass:: sqlite_utils.db.ColumnDetails

.. _reference_db_other_foreign_key:

sqlite_utils.db.ForeignKey
--------------------------

.. autoclass:: sqlite_utils.db.ForeignKey

sqlite_utils.utils
==================

.. _reference_utils_hash_record:

sqlite_utils.utils.hash_record
------------------------------

.. autofunction:: sqlite_utils.utils.hash_record

.. _reference_utils_rows_from_file:

sqlite_utils.utils.rows_from_file
---------------------------------

.. autofunction:: sqlite_utils.utils.rows_from_file

.. _reference_utils_typetracker:

sqlite_utils.utils.TypeTracker
------------------------------

.. autoclass:: sqlite_utils.utils.TypeTracker
   :members: wrap, types

.. _reference_utils_chunks:

sqlite_utils.utils.chunks
-------------------------

.. autofunction:: sqlite_utils.utils.chunks

.. _reference_utils_flatten:

sqlite_utils.utils.flatten
--------------------------

.. autofunction:: sqlite_utils.utils.flatten

```

### `docs/tutorial.ipynb`

```ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "27ae18ec",
   "metadata": {},
   "source": [
    "# The sqlite-utils tutorial\n",
    "\n",
    "[sqlite-utils](https://sqlite-utils.datasette.io/en/stable/python-api.html) is a Python library (and [command-line tool](https://sqlite-utils.datasette.io/en/stable/cli.html) for quickly creating and manipulating SQLite database files.\n",
    "\n",
    "This tutorial will show you how to use the Python library to manipulate data.\n",
    "\n",
    "## Installation\n",
    "\n",
    "To install the library, run:\n",
    "\n",
    "    pip install sqlite-utils\n",
    "\n",
    "You can run this in a Jupyter notebook cell by executing:\n",
    "\n",
    "    %pip install sqlite-utils\n",
    "    \n",
    "Or use `pip install -U sqlite-utils` to ensure you have upgraded to the most recent version."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bddee0d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: sqlite_utils in /usr/local/Cellar/jupyterlab/3.0.16_1/libexec/lib/python3.9/site-packages (3.14)\n",
      "Requirement already satisfied: click-default-group in /usr/local/lib/python3.9/site-packages (from sqlite_utils) (1.2.2)\n",
      "Requirement already satisfied: sqlite-fts4 in /usr/local/lib/python3.9/site-packages (from sqlite_utils) (1.0.1)\n",
      "Requirement already satisfied: click in /Users/simon/Library/Python/3.9/lib/python/site-packages (from sqlite_utils) (7.1.2)\n",
      "Requirement already satisfied: tabulate in /usr/local/lib/python3.9/site-packages (from sqlite_utils) (0.8.7)\n",
      "Requirement already satisfied: python-dateutil in /usr/local/Cellar/jupyterlab/3.0.16_1/libexec/lib/python3.9/site-package (from sqlite-utils) (2.8.1)\n",
      "Requirement already satisfied: six>=1.5 in /usr/local/Cellar/jupyterlab/3.0.16_1/libexec/lib/python3.9/site-package (from python-dateutil->sqlite-utils) (1.16.0)\n",
      "\u001b[33mWARNING: You are using pip version 21.1.1; however, version 21.2.2 is available.\n",
      "You should consider upgrading via the '/usr/local/Cellar/jupyterlab/3.0.16_1/libexec/bin/python3.9 -m pip install --upgrade pip' command.\u001b[0m\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install -U sqlite_utils"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "050e85a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite_utils"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "348bcbfc",
   "metadata": {},
   "source": [
    "You can use the library with a database file on disk by running:\n",
    "\n",
    "    db = sqlite_utils.Database(\"path/to/my/database.db\")\n",
    "\n",
    "In this tutorial we will use an in-memory database. This is a quick way to try out new things, though you should note that when you close the notebook the data store in the in-memory database will be lost."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4b2aee7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Database <sqlite3.Connection object at 0x139a16300>>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db = sqlite_utils.Database(memory=True)\n",
    "db"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1598ab43",
   "metadata": {},
   "source": [
    "## Creating a table\n",
    "\n",
    "We are going to create a new table in our database called `creatures` by passing in a Python list of dictionaries.\n",
    "\n",
    "`db[name_of_table]` will access a database table object with that name.\n",
    "\n",
    "Inserting data into that table will create it if it does not already exist."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4a0ac420",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Table creatures (name, species, age)>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db[\"creatures\"].insert_all([{\n",
    "    \"name\": \"Cleo\",\n",
    "    \"species\": \"dog\",\n",
    "    \"age\": 6\n",
    "}, {\n",
    "    \"name\": \"Lila\",\n",
    "    \"species\": \"chicken\",\n",
    "    \"age\": 0.8,\n",
    "}, {\n",
    "    \"name\": \"Bants\",\n",
    "    \"species\": \"chicken\",\n",
    "    \"age\": 0.8,\n",
    "}])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "049d110b",
   "metadata": {},
   "source": [
    "Let's grab a `table` reference to the new creatures table:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8d84ad9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "table = db[\"creatures\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ffe45750",
   "metadata": {},
   "source": [
    "`sqlite-utils` automatically creates a table schema that matches the keys and data types of the dictionaries that were passed to `.insert_all()`.\n",
    "\n",
    "We can see that schema using `table.schema`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "136cee1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CREATE TABLE \"creatures\" (\n",
      "   \"name\" TEXT,\n",
      "   \"species\" TEXT,\n",
      "   \"age\" FLOAT\n",
      ")\n"
     ]
    }
   ],
   "source": [
    "print(table.schema)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e5c3ae9",
   "metadata": {},
   "source": [
    "## Accessing data\n",
    "\n",
    "The `table.rows` property lets us loop through the rows in the table, returning each one as a Python dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f812914d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'Cleo', 'species': 'dog', 'age': 6.0}\n",
      "{'name': 'Lila', 'species': 'chicken', 'age': 0.8}\n",
      "{'name': 'Bants', 'species': 'chicken', 'age': 0.8}\n"
     ]
    }
   ],
   "source": [
    "for row in table.rows:\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60bc6b2c",
   "metadata": {},
   "source": [
    "The `db.query(sql)` method can be used to execute SQL queries and return the results as dictionaries:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "eaadd85f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'name': 'Cleo', 'species': 'dog', 'age': 6.0},\n",
       " {'name': 'Lila', 'species': 'chicken', 'age': 0.8},\n",
       " {'name': 'Bants', 'species': 'chicken', 'age': 0.8}]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(db.query(\"select * from creatures\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6614467b",
   "metadata": {},
   "source": [
    "Or in a loop:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "88fdd52e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cleo is a dog\n",
      "Lila is a chicken\n",
      "Bants is a chicken\n"
     ]
    }
   ],
   "source": [
    "for row in db.query(\"select name, species from creatures\"):\n",
    "    print(f'{row[\"name\"]} is a {row[\"species\"]}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b81c031c",
   "metadata": {},
   "source": [
    "### SQL parameters\n",
    "\n",
    "You can run a parameterized query using `?` as placeholders and passing a list of variables. The variables you pass will be correctly quoted, protecting your code from SQL injection vulnerabilities."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "267035d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'name': 'Cleo', 'species': 'dog', 'age': 6.0}]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(db.query(\"select * from creatures where age > ?\", [1.0]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87cb301b",
   "metadata": {},
   "source": [
    "As an alternative to question marks we can use `:name` parameters and feed in the values using a dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "83be9a80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'name': 'Lila', 'species': 'chicken', 'age': 0.8},\n",
       " {'name': 'Bants', 'species': 'chicken', 'age': 0.8}]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(db.query(\"select * from creatures where species = :species\", {\"species\": \"chicken\"}))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e5179cc",
   "metadata": {},
   "source": [
    "### Primary keys\n",
    "\n",
    "When we created this table we did not specify a primary key. SQLite automatically creates a primary key called `rowid` if no other primary key is defined.\n",
    "\n",
    "We can run `select rowid, * from creatures` to see this hidden primary key:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c9d963df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'rowid': 1, 'name': 'Cleo', 'species': 'dog', 'age': 6.0},\n",
       " {'rowid': 2, 'name': 'Lila', 'species': 'chicken', 'age': 0.8},\n",
       " {'rowid': 3, 'name': 'Bants', 'species': 'chicken', 'age': 0.8}]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(db.query(\"select rowid, * from creatures\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f87cdfb",
   "metadata": {},
   "source": [
    "We can also see that using `table.pks_and_rows_where()`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d365e405",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 {'rowid': 1, 'name': 'Cleo', 'species': 'dog', 'age': 6.0}\n",
      "2 {'rowid': 2, 'name': 'Lila', 'species': 'chicken', 'age': 0.8}\n",
      "3 {'rowid': 3, 'name': 'Bants', 'species': 'chicken', 'age': 0.8}\n"
     ]
    }
   ],
   "source": [
    "for pk, row in table.pks_and_rows_where():\n",
    "    print(pk, row)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5b0e9b74",
   "metadata": {},
   "source": [
    "Let's recreate the table with our own primary key, which we will call `id`.\n",
    "\n",
    "`table.drop()` drops the table:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "568a0e29",
   "metadata": {},
   "outputs": [],
   "source": [
    "table.drop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "13ebd3ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Table creatures (does not exist yet)>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "522aa6d0",
   "metadata": {},
   "source": [
    "We can see a list of tables in the database using `db.tables`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f3e62678",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db.tables"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b80d523",
   "metadata": {},
   "source": [
    "We'll create the table again, this time with an `id` column.\n",
    "\n",
    "We use `pk=\"id\"` to specify that the `id` column should be treated as the primary key for the table:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c9ee8b9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Table creatures (id, name, species, age)>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db[\"creatures\"].insert_all([{\n",
    "    \"id\": 1,\n",
    "    \"name\": \"Cleo\",\n",
    "    \"species\": \"dog\",\n",
    "    \"age\": 6\n",
    "}, {\n",
    "    \"id\": 2,\n",
    "    \"name\": \"Lila\",\n",
    "    \"species\": \"chicken\",\n",
    "    \"age\": 0.8,\n",
    "}, {\n",
    "    \"id\": 3,\n",
    "    \"name\": \"Bants\",\n",
    "    \"species\": \"chicken\",\n",
    "    \"age\": 0.8,\n",
    "}], pk=\"id\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "523e01ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CREATE TABLE \"creatures\" (\n",
      "   \"id\" INTEGER PRIMARY KEY,\n",
      "   \"name\" TEXT,\n",
      "   \"species\" TEXT,\n",
      "   \"age\" FLOAT\n",
      ")\n"
     ]
    }
   ],
   "source": [
    "print(table.schema)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "811bea70",
   "metadata": {},
   "source": [
    "## Inserting more records\n",
    "\n",
    "We can call `.insert_all()` again to insert more records. Let's add two more chickens."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "716df161",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Table creatures (id, name, species, age)>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table.insert_all([{\n",
    "    \"id\": 4,\n",
    "    \"name\": \"Azi\",\n",
    "    \"species\": \"chicken\",\n",
    "    \"age\": 0.8,\n",
    "}, {\n",
    "    \"id\": 5,\n",
    "    \"name\": \"Snowy\",\n",
    "    \"species\": \"chicken\",\n",
    "    \"age\": 0.9,\n",
    "}], pk=\"id\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4b1b2476",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'id': 1, 'name': 'Cleo', 'species': 'dog', 'age': 6.0},\n",
       " {'id': 2, 'name': 'Lila', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 3, 'name': 'Bants', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 4, 'name': 'Azi', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 5, 'name': 'Snowy', 'species': 'chicken', 'age': 0.9}]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(table.rows)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2af4ae75",
   "metadata": {},
   "source": [
    "Since the `id` column is an integer primary key, we can insert a record without specifying an ID and one will be automatically added.\n",
    "\n",
    "Since we are only adding one record we will use `.insert()` instead of `.insert_all()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "246c6dd5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Table creatures (id, name, species, age)>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table.insert({\"name\": \"Blue\", \"species\": \"chicken\", \"age\": 0.9})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7c28e4d",
   "metadata": {},
   "source": [
    "We can use `table.last_pk` to see the ID of the record we just added."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "de012e1e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table.last_pk"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c38edaf4",
   "metadata": {},
   "source": [
    "Here's the full list of rows again:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7c27075e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'id': 1, 'name': 'Cleo', 'species': 'dog', 'age': 6.0},\n",
       " {'id': 2, 'name': 'Lila', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 3, 'name': 'Bants', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 4, 'name': 'Azi', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 5, 'name': 'Snowy', 'species': 'chicken', 'age': 0.9},\n",
       " {'id': 6, 'name': 'Blue', 'species': 'chicken', 'age': 0.9}]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(table.rows)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64931bd0",
   "metadata": {},
   "source": [
    "If you try to add a new record with an existing ID, you will get an `IntegrityError`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "36327794",
   "metadata": {},
   "outputs": [
    {
     "ename": "IntegrityError",
     "evalue": "UNIQUE constraint failed: creatures.id",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIntegrityError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-24-4222c6abc759>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtable\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minsert\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m\"id\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;36m6\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"name\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"Red\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"species\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"chicken\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"age\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;36m0.9\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/usr/local/Cellar/jupyterlab/3.0.16_1/libexec/lib/python3.9/site-packages/sqlite_utils/db.py\u001b[0m in \u001b[0;36minsert\u001b[0;34m(self, record, pk, foreign_keys, column_order, not_null, defaults, hash_id, alter, ignore, replace, extracts, conversions, columns)\u001b[0m\n\u001b[1;32m   2027\u001b[0m         \u001b[0mcolumns\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDEFAULT\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2028\u001b[0m     ):\n\u001b[0;32m-> 2029\u001b[0;31m         return self.insert_all(\n\u001b[0m\u001b[1;32m   2030\u001b[0m             \u001b[0;34m[\u001b[0m\u001b[0mrecord\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2031\u001b[0m             \u001b[0mpk\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mpk\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/Cellar/jupyterlab/3.0.16_1/libexec/lib/python3.9/site-packages/sqlite_utils/db.py\u001b[0m in \u001b[0;36minsert_all\u001b[0;34m(self, records, pk, foreign_keys, column_order, not_null, defaults, batch_size, hash_id, alter, ignore, replace, truncate, extracts, conversions, columns, upsert)\u001b[0m\n\u001b[1;32m   2143\u001b[0m             \u001b[0mfirst\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2144\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2145\u001b[0;31m             self.insert_chunk(\n\u001b[0m\u001b[1;32m   2146\u001b[0m                 \u001b[0malter\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2147\u001b[0m                 \u001b[0mextracts\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/Cellar/jupyterlab/3.0.16_1/libexec/lib/python3.9/site-packages/sqlite_utils/db.py\u001b[0m in \u001b[0;36minsert_chunk\u001b[0;34m(self, alter, extracts, chunk, all_columns, hash_id, upsert, pk, conversions, num_records_processed, replace, ignore)\u001b[0m\n\u001b[1;32m   1955\u001b[0m             \u001b[0;32mfor\u001b[0m \u001b[0mquery\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mqueries_and_params\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1956\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1957\u001b[0;31m                     \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdb\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1958\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mOperationalError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1959\u001b[0m                     \u001b[0;32mif\u001b[0m \u001b[0malter\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;34m\" column\"\u001b[0m \u001b[0;32min\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/Cellar/jupyterlab/3.0.16_1/libexec/lib/python3.9/site-packages/sqlite_utils/db.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, sql, parameters)\u001b[0m\n\u001b[1;32m    255\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tracer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    256\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mparameters\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 257\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    258\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    259\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msql\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIntegrityError\u001b[0m: UNIQUE constraint failed: creatures.id"
     ]
    }
   ],
   "source": [
    "table.insert({\"id\": 6, \"name\": \"Red\", \"species\": \"chicken\", \"age\": 0.9})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e00692f",
   "metadata": {},
   "source": [
    "You can use `replace=True` to replace the matching record with a new one:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2be75589",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Table creatures (id, name, species, age)>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table.insert({\"id\": 6, \"name\": \"Red\", \"species\": \"chicken\", \"age\": 0.9}, replace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "83281675",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'id': 1, 'name': 'Cleo', 'species': 'dog', 'age': 6.0},\n",
       " {'id': 2, 'name': 'Lila', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 3, 'name': 'Bants', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 4, 'name': 'Azi', 'species': 'chicken', 'age': 0.8},\n",
       " {'id': 5, 'name': 'Snowy', 'species': 'chicken', 'age': 0.9},\n",
       " {'id': 6, 'name': 'Red', 'species': 'chicken', 'age': 0.9}]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(table.rows)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7122b76",
   "metadata": {},
   "source": [
    "## Updating a record\n",
    "\n",
    "We will rename that row back to `Blue`, this time using the `table.update(pk, updates)` method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "43df156d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Table creatures (id, name, species, age)>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table.update(6, {\"name\": \"Blue\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0b8f8422",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'id': 6, 'name': 'Blue', 'species': 'chicken', 'age': 0.9}]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(db.query(\"select * from creatures where id = ?\", [6]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58142b86",
   "metadata": {},
   "source": [
    "## Extracting one of the columns into another table\n",
    "\n",
    "Our current table has a `species` column with a string in it - let's pull that out into a separate table.\n",
    "\n",
    "We can do that using the [table.extract() method](https://sqlite-utils.datasette.io/en/stable/python-api.html#extracting-columns-into-a-separate-table)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "6ab69111",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Table creatures (id, name, species_id, age)>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table.extract(\"species\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dca327b2",
   "metadata": {},
   "source": [
    "We now have a new table called `species`, which we can see using the `db.tables` method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "76e95b36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<Table species (id, species)>, <Table creatures (id, name, species_id, age)>]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db.tables"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ea43bf5",
   "metadata": {},
   "source": [
    "Our creatures table has been modified - instead of a `species` column it now has `species_id` which is a foreign key to the new table:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "c0438bff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CREATE TABLE \"creatures\" (\n",
      "   \"id\" INTEGER PRIMARY KEY,\n",
      "   \"name\" TEXT,\n",
      "   \"species_id\" INTEGER,\n",
      "   \"age\" FLOAT,\n",
      "   FOREIGN KEY(\"species_id\") REFERENCES \"species\"(\"id\")\n",
      ")\n",
      "[{'id': 1, 'name': 'Cleo', 'species_id': 1, 'age': 6.0}, {'id': 2, 'name': 'Lila', 'species_id': 2, 'age': 0.8}, {'id': 3, 'name': 'Bants', 'species_id': 2, 'age': 0.8}, {'id': 4, 'name': 'Azi', 'species_id': 2, 'age': 0.8}, {'id': 5, 'name': 'Snowy', 'species_id': 2, 'age': 0.9}, {'id': 6, 'name': 'Blue', 'species_id': 2, 'age': 0.9}]\n"
     ]
    }
   ],
   "source": [
    "print(db[\"creatures\"].schema)\n",
    "print(list(db[\"creatures\"].rows))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0452c201",
   "metadata": {},
   "source": [
    "The new `species` table has been created and populated too:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "5d38c3a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CREATE TABLE \"species\" (\n",
      "   \"id\" INTEGER PRIMARY KEY,\n",
      "   \"species\" TEXT\n",
      ")\n",
      "[{'id': 1, 'species': 'dog'}, {'id': 2, 'species': 'chicken'}]\n"
     ]
    }
   ],
   "source": [
    "print(db[\"species\"].schema)\n",
    "print(list(db[\"species\"].rows))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0312d1e",
   "metadata": {},
   "source": [
    "We can use a join SQL query to combine data from these two tables:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "6734ed5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'id': 1, 'name': 'Cleo', 'age': 6.0, 'species_id': 1, 'species': 'dog'},\n",
       " {'id': 2, 'name': 'Lila', 'age': 0.8, 'species_id': 2, 'species': 'chicken'},\n",
       " {'id': 3, 'name': 'Bants', 'age': 0.8, 'species_id': 2, 'species': 'chicken'},\n",
       " {'id': 4, 'name': 'Azi', 'age': 0.8, 'species_id': 2, 'species': 'chicken'},\n",
       " {'id': 5, 'name': 'Snowy', 'age': 0.9, 'species_id': 2, 'species': 'chicken'},\n",
       " {'id': 6, 'name': 'Blue', 'age': 0.9, 'species_id': 2, 'species': 'chicken'}]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(db.query(\"\"\"\n",
    "    select\n",
    "      creatures.id,\n",
    "      creatures.name,\n",
    "      creatures.age,\n",
    "      species.id as species_id,\n",
    "      species.species\n",
    "    from creatures\n",
    "      join species on creatures.species_id = species.id\n",
    "\"\"\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c4802ac",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

### `docs/upgrading.rst`

```rst
.. _upgrading:

===========
 Upgrading
===========

This page describes the changes you may need to make to your own code or scripts when upgrading between major versions of ``sqlite-utils``.

For the full list of changes in every release see the :ref:`changelog`.

.. _upgrading_3_to_4:

Upgrading from 3.x to 4.0
=========================

Requirements
------------

- Python 3.10 or higher is required.
- The ``click`` dependency must be version 8.3.1 or later.

Command-line changes
--------------------

**Type detection is now the default for CSV and TSV imports.** ``sqlite-utils insert`` and ``sqlite-utils upsert`` now detect column types when importing CSV or TSV data - previously every column was created as ``TEXT`` unless you passed ``--detect-types``. To restore the old behavior pass the new ``--no-detect-types`` flag:

.. code-block:: bash

    sqlite-utils insert data.db rows data.csv --csv --no-detect-types

Two related things have been removed:

- The ``SQLITE_UTILS_DETECT_TYPES`` environment variable.
- The old ``-d/--detect-types`` flag itself. Since detection is now the default the flag did nothing - remove it from any scripts that used it.

**The convert command no longer skips falsey values.** ``sqlite-utils convert`` previously skipped values that evaluated to ``False`` (empty strings, ``0``) unless you passed ``--no-skip-false``. All values are now converted and the ``--no-skip-false`` flag has been removed.

**drop-table and drop-view check the object type.** ``sqlite-utils drop-table`` now refuses to drop a view, and ``drop-view`` refuses to drop a table. Previously each would silently drop the wrong type of object if the name matched. If you relied on that (unlikely), use the matching command instead.

**sqlite-utils tui has moved to a plugin.** The optional terminal interface is now provided by the `sqlite-utils-tui <https://github.com/simonw/sqlite-utils-tui>`__ plugin:

.. code-block:: bash

    sqlite-utils install sqlite-utils-tui

Python API changes
------------------

**db.query() now rejects SQL that does not return rows.** This is likely the most common change you will need to make to existing code. ``db.query()`` used to accept any SQL statement - passing one that returns no rows, such as an ``INSERT`` or ``UPDATE`` without a ``RETURNING`` clause or a ``CREATE TABLE``, did nothing at all, silently. Those statements now raise a ``ValueError``, and are rolled back so they have no effect on the database. Transaction control statements (``BEGIN``, ``COMMIT``, ``END``, ``ROLLBACK``, ``SAVEPOINT``, ``RELEASE``) plus ``VACUUM``, ``ATTACH`` and ``DETACH`` are also rejected with a ``ValueError``, without being executed at all. Use ``db.execute()`` for statements that do not return rows:

.. code-block:: python

    # 3.x accepted this but silently did nothing:
    db.query("update dogs set name = 'Cleopaws'")

    # In 4.0 use execute() for SQL that does not return rows:
    db.execute("update dogs set name = 'Cleopaws'")

**db.query() executes immediately.** ``db.query(sql)`` previously returned a generator that did not execute the SQL until you started iterating over it. The SQL now runs as soon as the method is called - rows are still fetched lazily, but errors in your SQL raise at the ``db.query()`` call site rather than on first iteration, and a write with a ``RETURNING`` clause takes effect even if you never iterate over its results.

**db.table() no longer returns views.** ``db.table(name)`` now raises a ``sqlite_utils.db.NoTable`` exception if ``name`` is a SQL view. Use the new ``db.view(name)`` method for views:

.. code-block:: python

    table = db.table("my_table")
    view = db.view("my_view")

``db["name"]`` still returns either a ``Table`` or a ``View`` depending on what exists in the database.

**Upserts use INSERT ... ON CONFLICT.** Upsert operations now use SQLite's ``INSERT ... ON CONFLICT SET`` syntax rather than the previous ``INSERT OR IGNORE`` followed by ``UPDATE``. If your code depends on the old behavior, pass ``use_old_upsert=True`` to the ``Database()`` constructor - see :ref:`python_api_old_upsert`.

**Upsert records must include their primary keys.** ``table.upsert()`` and ``table.upsert_all()`` now raise ``sqlite_utils.db.PrimaryKeyRequired`` if a record is missing a value for any primary key column (or has ``None`` for one). Previously such records were quietly inserted as new rows. Relatedly, ``pk=`` is now optional when the table already exists with a primary key - it is detected automatically.

**Floating point columns are now REAL.** Auto-detected floating point columns are created with the correct SQLite type ``REAL`` instead of ``FLOAT``. Code that inspects column types should expect ``REAL``.

**Generated schemas use double quotes.** Tables created by this library now wrap table and column names in ``"double-quotes"`` where they previously used ``[square-braces]``. If you compare ``table.schema`` strings against expected values you will need to update them.

**table.convert() no longer skips falsey values.** Matching the CLI change above, ``table.convert()`` now converts every value. The ``skip_false`` parameter has been removed - previously it defaulted to ``True``, skipping empty strings and other falsey values.

**Null values are no longer extracted into lookup tables.** ``table.extract()`` and the ``sqlite-utils extract`` command leave rows alone if every extracted column is ``null`` - the new foreign key column is left as ``null`` instead of pointing at an all-``null`` record in the lookup table. The ``extracts=`` insert option similarly keeps ``None`` values as ``null``. Relatedly, ``table.lookup()`` now compares values using ``IS`` so that looking up a value containing ``None`` returns the existing matching row - previously it inserted a duplicate row on every call.

**ensure_autocommit_off() is now ensure_autocommit_on().** The ``db.ensure_autocommit_off()`` context manager has been renamed to ``db.ensure_autocommit_on()``. The old name described the opposite of what the method did: it temporarily puts the connection into driver-level autocommit mode (by setting ``isolation_level = None``), so that statements such as ``PRAGMA journal_mode=wal`` can run outside of an implicit transaction. The behavior is unchanged - update any calls to use the new name.

**View.enable_fts() has been removed.** The ``View`` class previously had an ``enable_fts()`` method that existed only to raise ``NotImplementedError`` - full-text search is not supported for views. Calling it now raises ``AttributeError`` like any other missing method.

**ForeignKey is now a dataclass, not a namedtuple.** The ``ForeignKey`` objects returned by ``table.foreign_keys`` gained new fields - ``columns``, ``other_columns``, ``is_compound``, ``on_delete`` and ``on_update`` - so that compound (multi-column) foreign keys and foreign key actions can be represented. To make room for those fields cleanly ``ForeignKey`` is now a dataclass rather than a ``namedtuple``, so it can no longer be unpacked or indexed as a tuple. Access its fields by name instead:

.. code-block:: python

    # 3.x - tuple unpacking, no longer works:
    for table, column, other_table, other_column in db["courses"].foreign_keys:
        ...

    # 4.0 - access fields by name:
    for fk in db["courses"].foreign_keys:
        fk.table, fk.column, fk.other_table, fk.other_column

Attempting the old unpacking or ``fk[0]`` indexing now raises ``TypeError``, so any code using those patterns will fail loudly rather than silently misbehave. Like the old namedtuple, ``ForeignKey`` instances are immutable and hashable - they can be collected into sets and used as dictionary keys. Note that equality now includes the ``on_delete`` and ``on_update`` actions: a ``ForeignKey`` with ``ON DELETE CASCADE`` is not equal to one without.

Compound foreign keys - previously returned as one ``ForeignKey`` per column, misleadingly suggesting several independent single-column keys - are now returned as a single ``ForeignKey`` with ``is_compound=True``. For these the scalar ``column`` and ``other_column`` fields are ``None``; use the ``columns`` and ``other_columns`` tuples instead. Single-column foreign keys are unaffected apart from the class change: ``column``/``other_column`` behave as before and ``columns``/``other_columns`` are one-item tuples.

Two related behavior changes to ``table.transform()``: compound foreign keys now survive a transform (previously they were split into separate single-column keys), and ``ON DELETE``/``ON UPDATE`` actions such as ``ON DELETE CASCADE`` are now preserved (previously they were silently stripped from the schema).

**Validation errors raise ValueError.** Invalid arguments to Python API methods - for example ``create_table()`` with no columns, or ``ignore=True`` together with ``replace=True`` - now raise ``ValueError``. They previously raised ``AssertionError`` from bare ``assert`` statements, which were silently skipped under ``python -O``.

**Transaction behavior is now well-defined.** 4.0 introduces the :ref:`db.atomic() <python_api_atomic>` context manager and uses it consistently for every write operation - the full model is described in :ref:`python_api_transactions`. Changes you may notice:

- Write statements executed with raw ``db.execute()`` calls now commit automatically, unless a transaction is already open in which case they join it. Previously they opened an implicit transaction that nothing committed - if your code used ``db.execute()`` for writes and relied on ``db.conn.rollback()`` to undo them, open an explicit transaction with the new ``db.begin()`` method first.
- Multi-step operations such as ``table.transform()`` no longer commit an existing transaction you have open - they use savepoints inside it instead.
- ``db.enable_wal()`` and ``db.disable_wal()`` raise a ``sqlite_utils.db.TransactionError`` if called while a transaction is open, instead of silently committing it.
- Using ``Database`` as a context manager (``with Database(path) as db:``) closes the connection on exit *without* committing - a transaction you explicitly opened with ``db.begin()`` and did not commit is rolled back.
- ``Database()`` rejects connections created with the Python 3.12+ ``sqlite3.connect(..., autocommit=True)`` or ``autocommit=False`` options, raising ``sqlite_utils.db.TransactionError``. On those connections every write the library made was silently discarded when the connection closed.

Packaging changes
-----------------

- ``sqlite-utils`` now uses ``pyproject.toml`` in place of ``setup.py``.
- ``pip`` is now a runtime dependency, used by the ``sqlite-utils install`` and ``uninstall`` commands.

New features to be aware of
---------------------------

Not breaking changes, but new in 4.0 and worth knowing about when you upgrade:

- A :ref:`database migrations system <migrations>`, incorporating the functionality of the ``sqlite-migrate`` plugin. If you used that plugin, the built-in system reads the same ``_sqlite_migrations`` table - your applied migrations will not run again. Update your migration files to use ``from sqlite_utils import Migrations``.
- :ref:`db.atomic() <python_api_atomic>` for nested transaction support.
- ``table.insert_all()`` and ``table.upsert_all()`` accept an iterator of lists or tuples as an alternative to dictionaries - see :ref:`python_api_insert_lists`.

.. _upgrading_2_to_3:

Upgrading from 2.x to 3.0
=========================

The 3.0 release redesigned search. The breaking changes were minor:

- ``table.search()`` returns a generator of dictionaries, sorted by relevance. It previously returned a list of tuples sorted by ``rowid``.
- The ``-c`` shortcut for ``--csv`` and the ``-f`` shortcut for ``--fmt`` were removed from the CLI - use the full option names.

.. _upgrading_1_to_2:

Upgrading from 1.x to 2.0
=========================

The 2.0 release changed the meaning of *upsert*. In 1.x, ``table.upsert()`` and ``table.upsert_all()`` actually performed ``INSERT OR REPLACE`` operations - entirely replacing the existing row. Since 2.0 an upsert updates only the columns you provide, leaving other columns untouched.

If you want the 1.x behavior, use ``table.insert(..., replace=True)`` or ``table.insert_all(..., replace=True)`` instead.

```

### `Justfile`

```
# Run tests and linters
@default: test lint

# Run pytest with supplied options
@test *options: test-no-dev-dependencies
  uv run pytest {{options}}

@test-no-dev-dependencies:
  uv run --isolated --no-default-groups sqlite-utils --help > /dev/null

@run *options:
  uv run -- {{options}}

# Run linters: black, flake8, mypy, pyright, ty, cog
@lint:
  just run black . --check
  uv run flake8
  uv run mypy sqlite_utils tests
  uv run pyright sqlite_utils tests
  uv run ty check sqlite_utils
  uv run cog --check README.md docs/*.rst
  uv run --group docs codespell docs/*.rst --ignore-words docs/codespell-ignore-words.txt
  uv run --group docs codespell sqlite_utils --ignore-words docs/codespell-ignore-words.txt

# Rebuild docs with cog
@cog:
  uv run --group docs cog -r README.md docs/*.rst

# Serve live docs on localhost:8000
@docs: cog
  #!/usr/bin/env bash
  cd docs
  uv run --group docs make livehtml


# Apply Black
@black:
  uv run black .

```

### `LICENSE`

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

### `MANIFEST.in`

```in
include LICENSE
include README.md
recursive-include docs *.rst
recursive-include tests *.py

```

### `mypy.ini`

```ini
[mypy]
python_version = 3.10
warn_return_any = False
warn_unused_configs = True
warn_redundant_casts = False
warn_unused_ignores = False
check_untyped_defs = True
disallow_untyped_defs = False
disallow_incomplete_defs = False
no_implicit_optional = True
strict_equality = True

[mypy-sqlite_utils.cli]
ignore_errors = True

[mypy-pysqlite3.*]
ignore_missing_imports = True

[mypy-sqlite_dump.*]
ignore_missing_imports = True

[mypy-sqlite_fts4.*]
ignore_missing_imports = True

[mypy-pandas.*]
ignore_missing_imports = True

[mypy-numpy.*]
ignore_missing_imports = True

[mypy-tests.*]
ignore_errors = True

```

### `pyproject.toml`

```toml
[project]
name = "sqlite-utils"
version = "4.2.1"
description = "CLI tool and Python library for manipulating SQLite databases"
readme = { file = "README.md", content-type = "text/markdown" }
authors = [
    { name = "Simon Willison" },
]
license = "Apache-2.0"
requires-python = ">=3.10"
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Topic :: Database",
]

dependencies = [
    "click>=8.3.1",
    "click-default-group>=1.2.3",
    "pluggy",
    "python-dateutil",
    "sqlite-fts4",
    "tabulate",
    "pip",
]

[dependency-groups]
dev = [
    "black>=26.3.1",
    "click>=8.4.2",
    "cogapp",
    "hypothesis",
    "pytest",
    # mypy
    "data-science-types",
    "mypy",
    "types-click",
    "types-pluggy",
    "types-python-dateutil",
    "types-tabulate",
    # flake8
    "flake8",
    "flake8-pyproject",
    "pyright>=1.1.411",
    "ty>=0.0.37",
    # For stable cog:
    "tabulate>=0.10.0",
]
docs = [
    "codespell",
    "furo",
    "pygments-csv-lexer",
    "sphinx-autobuild",
    "sphinx-copybutton",
]

[project.urls]
Homepage = "https://github.com/simonw/sqlite-utils"
Documentation = "https://sqlite-utils.datasette.io/en/stable/"
Changelog = "https://sqlite-utils.datasette.io/en/stable/changelog.html"
Issues = "https://github.com/simonw/sqlite-utils/issues"
CI = "https://github.com/simonw/sqlite-utils/actions"

[project.scripts]
sqlite-utils = "sqlite_utils.cli:cli"

[build-system]
# setuptools 77+ is needed for the PEP 639 license = "Apache-2.0" expression
requires = ["setuptools>=77"]
build-backend = "setuptools.build_meta"

[tool.flake8]
max-line-length = 160
# Black compatibility, E203 whitespace before ':':
extend-ignore = ["E203"]
extend-exclude = [
    ".venv",
    ".claude",
    "build",
    "dist",
    "docs",
    "sqlite_utils.egg-info",
]

[tool.setuptools.package-data]
sqlite_utils = ["py.typed"]

```

### `README.md`

```md
# sqlite-utils

[![PyPI](https://img.shields.io/pypi/v/sqlite-utils.svg)](https://pypi.org/project/sqlite-utils/)
[![Changelog](https://img.shields.io/github/v/release/simonw/sqlite-utils?include_prereleases&label=changelog)](https://sqlite-utils.datasette.io/en/stable/changelog.html)
[![Python 3.x](https://img.shields.io/pypi/pyversions/sqlite-utils.svg?logo=python&logoColor=white)](https://pypi.org/project/sqlite-utils/)
[![Tests](https://github.com/simonw/sqlite-utils/workflows/Test/badge.svg)](https://github.com/simonw/sqlite-utils/actions?query=workflow%3ATest)
[![Documentation Status](https://readthedocs.org/projects/sqlite-utils/badge/?version=stable)](http://sqlite-utils.datasette.io/en/stable/?badge=stable)
[![codecov](https://codecov.io/gh/simonw/sqlite-utils/branch/main/graph/badge.svg)](https://codecov.io/gh/simonw/sqlite-utils)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/sqlite-utils/blob/main/LICENSE)
[![discord](https://img.shields.io/discord/823971286308356157?label=discord)](https://discord.gg/Ass7bCAMDw)

Python CLI utility and library for manipulating SQLite databases.

## Some feature highlights

- [Pipe JSON](https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-json-data) (or [CSV or TSV](https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-csv-or-tsv-data)) directly into a new SQLite database file, automatically creating a table with the appropriate schema
- [Run in-memory SQL queries](https://sqlite-utils.datasette.io/en/stable/cli.html#querying-data-directly-using-an-in-memory-database), including joins, directly against data in CSV, TSV or JSON files and view the results
- [Configure SQLite full-text search](https://sqlite-utils.datasette.io/en/stable/cli.html#configuring-full-text-search) against your database tables and run search queries against them, ordered by relevance
- Run [transformations against your tables](https://sqlite-utils.datasette.io/en/stable/cli.html#transforming-tables) to make schema changes that SQLite `ALTER TABLE` does not directly support, such as changing the type of a column
- [Extract columns](https://sqlite-utils.datasette.io/en/stable/cli.html#extracting-columns-into-a-separate-table) into separate tables to better normalize your existing data
- [Manage database migrations](https://sqlite-utils.datasette.io/en/stable/migrations.html) using Python migration files and the `sqlite-utils migrate` command
- [Install plugins](https://sqlite-utils.datasette.io/en/stable/plugins.html) to add custom SQL functions and additional features

Upgrading from sqlite-utils 3.x? See the [4.0 upgrade guide](https://sqlite-utils.datasette.io/en/stable/upgrading.html#upgrading-from-3-x-to-4-0).

Read more on my blog, in this series of posts on [New features in sqlite-utils](https://simonwillison.net/series/sqlite-utils-features/) and other [entries tagged sqlite-utils](https://simonwillison.net/tags/sqlite-utils/).

## Installation

    pip install sqlite-utils

Or if you use [Homebrew](https://brew.sh/) for macOS:

    brew install sqlite-utils

## Using as a CLI tool

Now you can do things with the CLI utility like this:

    $ sqlite-utils memory dogs.csv "select * from t"
    [{"id": 1, "age": 4, "name": "Cleo"},
     {"id": 2, "age": 2, "name": "Pancakes"}]

    $ sqlite-utils insert dogs.db dogs dogs.csv --csv
    [####################################]  100%

    $ sqlite-utils tables dogs.db --counts
    [{"table": "dogs", "count": 2}]

    $ sqlite-utils dogs.db "select id, name from dogs"
    [{"id": 1, "name": "Cleo"},
     {"id": 2, "name": "Pancakes"}]

    $ sqlite-utils dogs.db "select * from dogs" --csv
    id,age,name
    1,4,Cleo
    2,2,Pancakes

    $ sqlite-utils dogs.db "select * from dogs" --table
      id    age  name
    ----  -----  --------
       1      4  Cleo
       2      2  Pancakes

You can import JSON data into a new database table like this:

    $ curl https://api.github.com/repos/simonw/sqlite-utils/releases \
        | sqlite-utils insert releases.db releases - --pk id

Or for data in a CSV file:

    $ sqlite-utils insert dogs.db dogs dogs.csv --csv

`sqlite-utils memory` lets you import CSV or JSON data into an in-memory database and run SQL queries against it in a single command:

    $ cat dogs.csv | sqlite-utils memory - "select name, age from stdin"

See the [full CLI documentation](https://sqlite-utils.datasette.io/en/stable/cli.html) for comprehensive coverage of many more commands.

## Using as a library

You can also `import sqlite_utils` and use it as a Python library like this:

```python
import sqlite_utils
db = sqlite_utils.Database("demo_database.db")
# This line creates a "dogs" table if one does not already exist:
db["dogs"].insert_all([
    {"id": 1, "age": 4, "name": "Cleo"},
    {"id": 2, "age": 2, "name": "Pancakes"}
], pk="id")
```

Check out the [full library documentation](https://sqlite-utils.datasette.io/en/stable/python-api.html) for everything else you can do with the Python library.

## Related projects

* [Datasette](https://datasette.io/): A tool for exploring and publishing data
* [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite): Convert CSV files into a SQLite database
* [db-to-sqlite](https://github.com/simonw/db-to-sqlite): CLI tool for exporting a MySQL or PostgreSQL database as a SQLite file
* [dogsheep](https://dogsheep.github.io/): A family of tools for personal analytics, built on top of `sqlite-utils`

```

### `sqlite_utils/__init__.py`

```py
from .db import Database
from .hookspecs import hookimpl, hookspec
from .migrations import Migrations
from .utils import ANY, suggest_column_types

__all__ = [
    "ANY",
    "Database",
    "Migrations",
    "hookimpl",
    "hookspec",
    "suggest_column_types",
]

```

### `sqlite_utils/__main__.py`

```py
from .cli import cli

if __name__ == "__main__":
    cli()

```

### `sqlite_utils/create_table_parser.py`

```py
"""Helpers for parsing constraints from SQLite CREATE TABLE SQL.

SQLite does not expose CHECK constraints through a pragma, so preserving them
across a table rebuild requires reading ``sqlite_schema.sql``.  This module is
deliberately small, but it uses a real lexer: strings, quoted identifiers and
comments are opaque, every token retains its source span and malformed input is
reported instead of being silently under-parsed.
"""

import re
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Check:
    check: str
    name: str = ""
    column: str = ""
    options: list[Any] | None = None
    # Source details are excluded from equality and repr so callers can compare
    # semantic constraints while still having the original SQL available for
    # diagnostics or future lossless edits.
    sql: str = field(default="", compare=False, repr=False)
    start: int = field(default=-1, compare=False, repr=False)
    end: int = field(default=-1, compare=False, repr=False)


@dataclass(frozen=True)
class ColumnComments:
    before: str = ""
    after: str = ""


@dataclass(frozen=True)
class UniqueColumn:
    name: str
    collation: str = ""
    order: str = ""


@dataclass
class Unique:
    columns: tuple[UniqueColumn, ...]
    name: str = ""
    column: str = ""
    conflict: str = ""
    sql: str = field(default="", compare=False, repr=False)
    start: int = field(default=-1, compare=False, repr=False)
    end: int = field(default=-1, compare=False, repr=False)


class ParseError(ValueError):
    pass


@dataclass(frozen=True)
class _Token:
    kind: str
    text: str
    start: int
    end: int

    def is_keyword(self, keyword: str) -> bool:
        return self.kind == "word" and self.text.upper() == keyword


_PUNCTUATION = frozenset("(),.;+-*/%<>=!~|&?:")
_TRIVIA = frozenset(("whitespace", "comment"))
_TABLE_CONSTRAINT_KEYWORDS = frozenset(("PRIMARY", "UNIQUE", "CHECK", "FOREIGN"))
_OTHER_COLUMN_CONSTRAINT_KEYWORDS = frozenset(
    ("PRIMARY", "UNIQUE", "REFERENCES", "DEFAULT", "NOT", "COLLATE", "GENERATED")
)
_SQLITE_KEYWORDS = frozenset(
    (
        "ABORT",
        "ACTION",
        "ADD",
        "AFTER",
        "ALL",
        "ALTER",
        "ANALYZE",
        "AND",
        "AS",
        "ASC",
        "ATTACH",
        "AUTOINCREMENT",
        "BEFORE",
        "BEGIN",
        "BETWEEN",
        "BY",
        "CASCADE",
        "CASE",
        "CAST",
        "CHECK",
        "COLLATE",
        "COLUMN",
        "COMMIT",
        "CONFLICT",
        "CONSTRAINT",
        "CREATE",
        "CROSS",
        "CURRENT_DATE",
        "CURRENT_TIME",
        "CURRENT_TIMESTAMP",
        "DATABASE",
        "DEFAULT",
        "DEFERRABLE",
        "DEFERRED",
        "DELETE",
        "DESC",
        "DETACH",
        "DISTINCT",
        "DO",
        "DROP",
        "EACH",
        "ELSE",
        "END",
        "ESCAPE",
        "EXCEPT",
        "EXCLUDE",
        "EXCLUSIVE",
        "EXISTS",
        "EXPLAIN",
        "FAIL",
        "FALSE",
        "FILTER",
        "FIRST",
        "FOLLOWING",
        "FOR",
        "FOREIGN",
        "FROM",
        "FULL",
        "GENERATED",
        "GLOB",
        "GROUP",
        "GROUPS",
        "HAVING",
        "IF",
        "IGNORE",
        "IMMEDIATE",
        "IN",
        "INDEX",
        "INDEXED",
        "INITIALLY",
        "INNER",
        "INSERT",
        "INSTEAD",
        "INTERSECT",
        "INTO",
        "IS",
        "ISNULL",
        "JOIN",
        "KEY",
        "LAST",
        "LEFT",
        "LIKE",
        "LIMIT",
        "MATCH",
        "MATERIALIZED",
        "NATURAL",
        "NO",
        "NOT",
        "NOTHING",
        "NOTNULL",
        "NULL",
        "NULLS",
        "OF",
        "OFFSET",
        "ON",
        "OR",
        "ORDER",
        "OTHERS",
        "OUTER",
        "OVER",
        "PARTITION",
        "PLAN",
        "PRAGMA",
        "PRECEDING",
        "PRIMARY",
        "QUERY",
        "RAISE",
        "RANGE",
        "RECURSIVE",
        "REFERENCES",
        "REGEXP",
        "REINDEX",
        "RELEASE",
        "RENAME",
        "REPLACE",
        "RESTRICT",
        "RETURNING",
        "RIGHT",
        "ROLLBACK",
        "ROW",
        "ROWS",
        "SAVEPOINT",
        "SELECT",
        "SET",
        "STRICT",
        "TABLE",
        "TEMP",
        "TEMPORARY",
        "THEN",
        "TIES",
        "TO",
        "TRANSACTION",
        "TRIGGER",
        "TRUE",
        "UNBOUNDED",
        "UNION",
        "UNIQUE",
        "UPDATE",
        "USING",
        "VACUUM",
        "VALUES",
        "VIEW",
        "VIRTUAL",
        "WHEN",
        "WHERE",
        "WINDOW",
        "WITH",
        "WITHOUT",
    )
)
_INTEGER_RE = re.compile(r"[+-]?(?:0[xX][0-9a-fA-F]+|[0-9]+)\Z")
_FLOAT_RE = re.compile(
    r"[+-]?(?:(?:[0-9]+\.[0-9]*|\.[0-9]+)(?:[eE][+-]?[0-9]+)?|"
    r"[0-9]+[eE][+-]?[0-9]+)\Z"
)


def _lex(sql: str) -> list[_Token]:
    tokens: list[_Token] = []
    i = 0
    while i < len(sql):
        start = i
        char = sql[i]
        if char.isspace():
            i += 1
            while i < len(sql) and sql[i].isspace():
                i += 1
            tokens.append(_Token("whitespace", sql[start:i], start, i))
            continue
        if sql.startswith("--", i):
            newline = sql.find("\n", i + 2)
            i = len(sql) if newline == -1 else newline + 1
            tokens.append(_Token("comment", sql[start:i], start, i))
            continue
        if sql.startswith("/*", i):
            end = sql.find("*/", i + 2)
            if end == -1:
                raise ParseError("Unterminated SQL comment")
            i = end + 2
            tokens.append(_Token("comment", sql[start:i], start, i))
            continue
        if char in ("'", '"', "`"):
            quote = char
            i += 1
            while i < len(sql):
                if sql[i] == quote:
                    if i + 1 < len(sql) and sql[i + 1] == quote:
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
            else:
                raise ParseError(f"Unterminated {quote} quoted token")
            kind = "string" if quote == "'" else "identifier"
            tokens.append(_Token(kind, sql[start:i], start, i))
            continue
        if char == "[":
            end = sql.find("]", i + 1)
            if end == -1:
                raise ParseError("Unterminated [ quoted identifier")
            i = end + 1
            tokens.append(_Token("identifier", sql[start:i], start, i))
            continue
        if char in _PUNCTUATION:
            i += 1
            tokens.append(_Token("punct", char, start, i))
            continue
        # SQLite accepts any character >= U+0080 in a bare identifier.  More
        # generally, consume until a lexical delimiter rather than relying on
        # Python's narrower definition of an alphanumeric character.
        i += 1
        while i < len(sql):
            if sql[i].isspace() or sql[i] in _PUNCTUATION or sql[i] in "'\"`[":
                break
            i += 1
        tokens.append(_Token("word", sql[start:i], start, i))
    return tokens


def _meaningful(tokens: list[_Token]) -> list[_Token]:
    return [token for token in tokens if token.kind not in _TRIVIA]


def _unquote(token: str) -> str:
    if len(token) >= 2 and token[0] in ("'", '"', "`") and token[-1] == token[0]:
        return token[1:-1].replace(token[0] * 2, token[0])
    if len(token) >= 2 and token[0] == "[" and token[-1] == "]":
        return token[1:-1]
    return token


def _matching_paren(tokens: list[_Token], open_index: int) -> int:
    if tokens[open_index].text != "(":
        raise ParseError("Expected an opening parenthesis")
    depth = 0
    for index in range(open_index, len(tokens)):
        if tokens[index].text == "(":
            depth += 1
        elif tokens[index].text == ")":
            depth -= 1
            if depth == 0:
                return index
    raise ParseError("Unbalanced parentheses")


def _split_spans(sql: str, tokens: list[_Token]) -> list[tuple[str, int, int]]:
    if not tokens:
        return []
    items: list[tuple[str, int, int]] = []
    depth = 0
    start = tokens[0].start
    for token in tokens:
        if token.text == "(":
            depth += 1
        elif token.text == ")":
            depth -= 1
            if depth < 0:
                raise ParseError("Unbalanced parentheses")
        elif token.text == "," and depth == 0:
            raw = sql[start : token.start]
            item = raw.strip()
            if item:
                item_start = start + len(raw) - len(raw.lstrip())
                items.append((item, item_start, item_start + len(item)))
            start = token.end
    if depth:
        raise ParseError("Unbalanced parentheses")
    raw = sql[start : tokens[-1].end]
    item = raw.strip()
    if item:
        item_start = start + len(raw) - len(raw.lstrip())
        items.append((item, item_start, item_start + len(item)))
    return items


def _split_ranges(sql: str, tokens: list[_Token]) -> list[str]:
    return [item for item, _, _ in _split_spans(sql, tokens)]


def _strip_outer_parens(tokens: list[_Token]) -> list[_Token]:
    while tokens and tokens[0].text == "(":
        close = _matching_paren(tokens, 0)
        if close != len(tokens) - 1:
            break
        tokens = tokens[1:-1]
    return tokens


_NO_LITERAL = object()


def _literal_value(text: str) -> Any:
    tokens = _meaningful(_lex(text))
    if len(tokens) == 1 and tokens[0].kind == "string":
        return _unquote(tokens[0].text)
    raw = "".join(token.text for token in tokens)
    if raw.upper() == "NULL":
        return None
    if raw.upper() == "TRUE":
        return True
    if raw.upper() == "FALSE":
        return False
    if _INTEGER_RE.fullmatch(raw):
        try:
            return (
                int(raw, 16) if raw.lower().lstrip("+-").startswith("0x") else int(raw)
            )
        except ValueError:
            return _NO_LITERAL
    if _FLOAT_RE.fullmatch(raw):
        try:
            return float(raw)
        except ValueError:
            return _NO_LITERAL
    return _NO_LITERAL


def _ascii_fold(identifier: str) -> str:
    return identifier.translate(
        str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    )


def _parse_options(expression: str, column: str) -> list[Any] | None:
    tokens = _strip_outer_parens(_meaningful(_lex(expression)))
    if len(tokens) < 4:
        return None
    lhs = tokens[0]
    if lhs.kind not in ("word", "identifier"):
        return None
    if column and _ascii_fold(_unquote(lhs.text)) != _ascii_fold(column):
        return None
    if not tokens[1].is_keyword("IN") or tokens[2].text != "(":
        return None
    close = _matching_paren(tokens, 2)
    if close != len(tokens) - 1:
        return None
    inner = expression[tokens[2].end : tokens[close].start]
    inner_tokens = _lex(inner)
    if not _meaningful(inner_tokens):
        return []
    values = []
    for item in _split_ranges(inner, inner_tokens):
        value = _literal_value(item)
        if value is _NO_LITERAL:
            return None
        values.append(value)
    return values


def _check_after(
    item: str,
    tokens: list[_Token],
    check_index: int,
    name: str,
    column: str,
    constraint_start: int,
    base_offset: int,
) -> tuple[Check, int]:
    if check_index + 1 >= len(tokens) or tokens[check_index + 1].text != "(":
        raise ParseError("CHECK must be followed by a parenthesized expression")
    close = _matching_paren(tokens, check_index + 1)
    expression = item[tokens[check_index + 1].end : tokens[close].start].strip()
    source_start = tokens[constraint_start].start
    source_end = tokens[close].end
    return (
        Check(
            expression,
            name=name,
            column=column,
            options=_parse_options(expression, column),
            sql=item[source_start:source_end],
            start=base_offset + source_start,
            end=base_offset + source_end,
        ),
        close + 1,
    )


def _column_checks(
    item: str, tokens: list[_Token], column: str, base_offset: int
) -> list[Check]:
    checks: list[Check] = []
    pending_name = ""
    pending_start: int | None = None
    index = 1
    while index < len(tokens):
        token = tokens[index]
        if token.text == "(":
            index = _matching_paren(tokens, index) + 1
            continue
        if token.is_keyword("CONSTRAINT"):
            if index + 1 >= len(tokens):
                raise ParseError("CONSTRAINT is missing its name")
            pending_name = _unquote(tokens[index + 1].text)
            pending_start = index
            index += 2
            continue
        if token.is_keyword("CHECK"):
            check, index = _check_after(
                item,
                tokens,
                index,
                pending_name,
                column,
                pending_start if pending_start is not None else index,
                base_offset,
            )
            checks.append(check)
            pending_name = ""
            pending_start = None
            continue
        if (
            token.kind == "word"
            and token.text.upper() in _OTHER_COLUMN_CONSTRAINT_KEYWORDS
        ):
            pending_name = ""
            pending_start = None
        index += 1
    return checks


def _table_body(create_sql: str) -> tuple[str, int] | None:
    all_tokens = _lex(create_sql)
    tokens = _meaningful(all_tokens)
    if not tokens or not tokens[0].is_keyword("CREATE"):
        raise ParseError("Expected CREATE TABLE")
    index = 1
    if index < len(tokens) and (
        tokens[index].is_keyword("TEMP") or tokens[index].is_keyword("TEMPORARY")
    ):
        index += 1
    if index < len(tokens) and tokens[index].is_keyword("VIRTUAL"):
        return None
    if index >= len(tokens) or not tokens[index].is_keyword("TABLE"):
        raise ParseError("Expected CREATE TABLE")
    index += 1
    if (
        index + 2 < len(tokens)
        and tokens[index].is_keyword("IF")
        and tokens[index + 1].is_keyword("NOT")
        and tokens[index + 2].is_keyword("EXISTS")
    ):
        index += 3
    if index >= len(tokens):
        raise ParseError("CREATE TABLE is missing its table name")
    index += 1
    if index + 1 < len(tokens) and tokens[index].text == ".":
        index += 2
    if index < len(tokens) and tokens[index].is_keyword("AS"):
        return None
    if index >= len(tokens) or tokens[index].text != "(":
        raise ParseError("CREATE TABLE is missing its column list")
    close = _matching_paren(tokens, index)
    trailing = tokens[close + 1 :]
    allowed_trailing = {"STRICT", "WITHOUT", "ROWID", ",", ";"}
    if any(token.text.upper() not in allowed_trailing for token in trailing):
        raise ParseError("Unexpected SQL after CREATE TABLE column list")

    body_start = tokens[index].end
    body_end = tokens[close].start
    return create_sql[body_start:body_end], body_start


def parse_checks(create_sql: str) -> list[Check]:
    """Return CHECK constraints from a valid SQLite CREATE TABLE statement."""
    body_info = _table_body(create_sql)
    if body_info is None:
        return []
    body, body_start = body_info
    body_tokens = _lex(body)
    checks: list[Check] = []
    for item, item_start, _ in _split_spans(body, body_tokens):
        item_tokens = _meaningful(_lex(item))
        if not item_tokens:
            continue
        item_index = 0
        constraint_name = ""
        if item_tokens[item_index].is_keyword("CONSTRAINT"):
            if len(item_tokens) < 2:
                raise ParseError("CONSTRAINT is missing its name")
            constraint_name = _unquote(item_tokens[1].text)
            item_index = 2
        head = item_tokens[item_index] if item_index < len(item_tokens) else None
        if (
            head
            and head.kind == "word"
            and head.text.upper() in _TABLE_CONSTRAINT_KEYWORDS
        ):
            if head.is_keyword("CHECK"):
                check, _ = _check_after(
                    item,
                    item_tokens,
                    item_index,
                    constraint_name,
                    "",
                    0,
                    body_start + item_start,
                )
                checks.append(check)
            continue
        column = _unquote(item_tokens[0].text)
        checks.extend(
            _column_checks(item, item_tokens, column, body_start + item_start)
        )
    return checks


def parse_autoincrement(create_sql: str) -> str | None:
    """Return the AUTOINCREMENT column from a valid CREATE TABLE statement."""
    body_info = _table_body(create_sql)
    if body_info is None:
        return None
    body, _ = body_info
    for item, _, _ in _split_spans(body, _lex(body)):
        item_tokens = _meaningful(_lex(item))
        if not item_tokens:
            continue
        head = item_tokens[0]
        if (
            head.kind == "word" and head.text.upper() in _TABLE_CONSTRAINT_KEYWORDS
        ) or head.is_keyword("CONSTRAINT"):
            continue
        column = _unquote(head.text)
        index = 1
        while index < len(item_tokens):
            token = item_tokens[index]
            if token.text == "(":
                index = _matching_paren(item_tokens, index) + 1
                continue
            if token.is_keyword("AUTOINCREMENT"):
                return column
            index += 1
    return None


_CONFLICT_ACTIONS = frozenset(("ROLLBACK", "ABORT", "FAIL", "IGNORE", "REPLACE"))


def _conflict_after(tokens: list[_Token], index: int) -> tuple[str, int]:
    if index >= len(tokens) or not tokens[index].is_keyword("ON"):
        return "", index
    if index + 2 >= len(tokens) or not tokens[index + 1].is_keyword("CONFLICT"):
        raise ParseError("ON after UNIQUE must be followed by CONFLICT and an action")
    action = tokens[index + 2].text.upper()
    if tokens[index + 2].kind != "word" or action not in _CONFLICT_ACTIONS:
        raise ParseError("Invalid UNIQUE ON CONFLICT action")
    return action, index + 3


def _unique_columns(
    item: str, tokens: list[_Token], open_index: int
) -> tuple[tuple[UniqueColumn, ...], int]:
    close = _matching_paren(tokens, open_index)
    inner = item[tokens[open_index].end : tokens[close].start]
    columns: list[UniqueColumn] = []
    for raw_column in _split_ranges(inner, _lex(inner)):
        column_tokens = _meaningful(_lex(raw_column))
        if not column_tokens or column_tokens[0].kind not in (
            "word",
            "identifier",
            "string",
        ):
            raise ParseError("UNIQUE constraint has an invalid column")
        name = _unquote(column_tokens[0].text)
        collation = ""
        order = ""
        index = 1
        if index < len(column_tokens) and column_tokens[index].is_keyword("COLLATE"):
            if index + 1 >= len(column_tokens):
                raise ParseError("COLLATE in UNIQUE constraint is missing its name")
            collation = _unquote(column_tokens[index + 1].text)
            index += 2
        if index < len(column_tokens) and (
            column_tokens[index].is_keyword("ASC")
            or column_tokens[index].is_keyword("DESC")
        ):
            order = column_tokens[index].text.upper()
            index += 1
        if index != len(column_tokens):
            raise ParseError("UNIQUE constraint has an invalid indexed column")
        columns.append(UniqueColumn(name, collation=collation, order=order))
    if not columns:
        raise ParseError("UNIQUE constraint must include at least one column")
    return tuple(columns), close + 1


def _column_uniques(
    item: str, tokens: list[_Token], column: str, base_offset: int
) -> list[Unique]:
    uniques: list[Unique] = []
    collation = ""
    collation_index = 1
    while collation_index < len(tokens):
        token = tokens[collation_index]
        if token.text == "(":
            collation_index = _matching_paren(tokens, collation_index) + 1
            continue
        if token.is_keyword("COLLATE"):
            if collation_index + 1 >= len(tokens):
                raise ParseError("COLLATE is missing its name")
            collation = _unquote(tokens[collation_index + 1].text)
            collation_index += 2
            continue
        collation_index += 1
    pending_name = ""
    pending_start: int | None = None
    index = 1
    while index < len(tokens):
        token = tokens[index]
        if token.text == "(":
            index = _matching_paren(tokens, index) + 1
            continue
        if token.is_keyword("CONSTRAINT"):
            if index + 1 >= len(tokens):
                raise ParseError("CONSTRAINT is missing its name")
            pending_name = _unquote(tokens[index + 1].text)
            pending_start = index
            index += 2
            continue
        if token.is_keyword("UNIQUE"):
            source_start = tokens[
                pending_start if pending_start is not None else index
            ].start
            conflict, next_index = _conflict_after(tokens, index + 1)
            source_end = tokens[next_index - 1].end
            uniques.append(
                Unique(
                    (UniqueColumn(column, collation=collation),),
                    name=pending_name,
                    column=column,
                    conflict=conflict,
                    sql=item[source_start:source_end],
                    start=base_offset + source_start,
                    end=base_offset + source_end,
                )
            )
            pending_name = ""
            pending_start = None
            index = next_index
            continue
        if (
            token.kind == "word"
            and token.text.upper() in _OTHER_COLUMN_CONSTRAINT_KEYWORDS
        ):
            pending_name = ""
            pending_start = None
        index += 1
    return uniques


def parse_uniques(create_sql: str) -> list[Unique]:
    """Return column-level and table-level UNIQUE constraints."""
    body_info = _table_body(create_sql)
    if body_info is None:
        return []
    body, body_start = body_info
    uniques: list[Unique] = []
    for item, item_start, _ in _split_spans(body, _lex(body)):
        item_tokens = _meaningful(_lex(item))
        if not item_tokens:
            continue
        item_index = 0
        constraint_name = ""
        if item_tokens[item_index].is_keyword("CONSTRAINT"):
            if len(item_tokens) < 2:
                raise ParseError("CONSTRAINT is missing its name")
            constraint_name = _unquote(item_tokens[1].text)
            item_index = 2
        head = item_tokens[item_index] if item_index < len(item_tokens) else None
        if head and head.is_keyword("UNIQUE"):
            if (
                item_index + 1 >= len(item_tokens)
                or item_tokens[item_index + 1].text != "("
            ):
                raise ParseError("Table UNIQUE must be followed by a column list")
            columns, next_index = _unique_columns(item, item_tokens, item_index + 1)
            conflict, next_index = _conflict_after(item_tokens, next_index)
            if next_index != len(item_tokens):
                raise ParseError("Unexpected SQL after UNIQUE constraint")
            source_start = item_tokens[0].start
            source_end = item_tokens[next_index - 1].end
            uniques.append(
                Unique(
                    columns,
                    name=constraint_name,
                    conflict=conflict,
                    sql=item[source_start:source_end],
                    start=body_start + item_start + source_start,
                    end=body_start + item_start + source_end,
                )
            )
            continue
        if (
            head
            and head.kind == "word"
            and head.text.upper() in _TABLE_CONSTRAINT_KEYWORDS
        ):
            continue
        column = _unquote(item_tokens[0].text)
        uniques.extend(
            _column_uniques(
                item,
                item_tokens,
                column,
                body_start + item_start,
            )
        )
    return uniques


def parse_column_comments(create_sql: str) -> dict[str, ColumnComments]:
    """Return comments immediately before and after each column definition."""
    body_info = _table_body(create_sql)
    if body_info is None:
        return {}
    body, _ = body_info
    comments: dict[str, ColumnComments] = {}
    for item, _, _ in _split_spans(body, _lex(body)):
        item_tokens = _meaningful(_lex(item))
        if not item_tokens:
            continue
        item_index = 0
        if item_tokens[item_index].is_keyword("CONSTRAINT"):
            item_index = 2
        head = item_tokens[item_index] if item_index < len(item_tokens) else None
        if (
            head
            and head.kind == "word"
            and head.text.upper() in _TABLE_CONSTRAINT_KEYWORDS
        ):
            continue
        column = _unquote(item_tokens[0].text)
        before = item[: item_tokens[0].start].strip()
        after = item[item_tokens[-1].end :].strip()
        if before or after:
            comments[column] = ColumnComments(before=before, after=after)
    return comments


def _is_identifier_token(tokens: list[_Token], index: int) -> bool:
    token = tokens[index]
    if index + 1 < len(tokens) and tokens[index + 1].text in ("(", "."):
        return False
    if index and (
        tokens[index - 1].is_keyword("COLLATE") or tokens[index - 1].is_keyword("AS")
    ):
        return False
    if token.kind == "identifier":
        return True
    if token.kind != "word" or token.text.upper() in _SQLITE_KEYWORDS:
        return False
    return True


def check_references_identifier(expression: str, identifier: str) -> bool:
    tokens = _meaningful(_lex(expression))
    folded = _ascii_fold(identifier)
    return any(
        _is_identifier_token(tokens, index)
        and _ascii_fold(_unquote(token.text)) == folded
        for index, token in enumerate(tokens)
    )


def sql_ends_in_line_comment(sql: str) -> bool:
    """Return True if appended SQL would be swallowed by a ``--`` comment."""
    tokens = _lex(sql)
    if not tokens:
        return False
    final = tokens[-1]
    return (
        final.kind == "comment"
        and final.text.startswith("--")
        and not final.text.endswith(("\n", "\r"))
    )


def _valid_bare_identifier(identifier: str) -> bool:
    if not identifier or identifier.upper() in _SQLITE_KEYWORDS:
        return False
    first = identifier[0]
    if not (first == "_" or first.isalpha() or ord(first) >= 0x80):
        return False
    return all(
        char == "_" or char == "$" or char.isalnum() or ord(char) >= 0x80
        for char in identifier[1:]
    )


def _quote_replacement(original: str, replacement: str) -> str:
    if original.startswith('"'):
        return '"{}"'.format(replacement.replace('"', '""'))
    if original.startswith("`"):
        return "`{}`".format(replacement.replace("`", "``"))
    if original.startswith("[") and "]" not in replacement:
        return f"[{replacement}]"
    if _valid_bare_identifier(replacement):
        return replacement
    return '"{}"'.format(replacement.replace('"', '""'))


def rewrite_check_expression(expression: str, rename: dict[str, str]) -> str:
    """Rewrite column identifiers in a CHECK expression, preserving trivia."""
    if not rename:
        return expression
    tokens = _lex(expression)
    meaningful = _meaningful(tokens)
    replacements = {_ascii_fold(key): value for key, value in rename.items()}
    edits: list[tuple[int, int, str]] = []
    for index, token in enumerate(meaningful):
        if not _is_identifier_token(meaningful, index):
            continue
        replacement = replacements.get(_ascii_fold(_unquote(token.text)))
        if replacement is not None:
            edits.append(
                (token.start, token.end, _quote_replacement(token.text, replacement))
            )
    for start, end, replacement in reversed(edits):
        expression = expression[:start] + replacement + expression[end:]
    return expression

```

### `sqlite_utils/hookspecs.py`

```py
import sqlite3

import click
from pluggy import HookimplMarker, HookspecMarker

hookspec = HookspecMarker("sqlite_utils")
hookimpl = HookimplMarker("sqlite_utils")


@hookspec
def register_commands(cli: click.Group) -> None:
    """Register additional CLI commands, e.g. 'sqlite-utils mycommand ...'"""


@hookspec
def prepare_connection(conn: sqlite3.Connection) -> None:
    """Modify SQLite connection in some way e.g. register custom SQL functions"""

```

### `sqlite_utils/migrations.py`

```py
import datetime
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol, TypeVar, cast

if TYPE_CHECKING:
    from sqlite_utils.db import Database, Table


class _MigrationFunction(Protocol):
    __name__: str

    def __call__(self, db: "Database", /) -> None: ...


_MigrationFunctionT = TypeVar("_MigrationFunctionT", bound=_MigrationFunction)


class Migrations:
    migrations_table = "_sqlite_migrations"

    @dataclass
    class _Migration:
        name: str
        fn: _MigrationFunction
        transactional: bool = True

    @dataclass
    class _AppliedMigration:
        name: str
        # A string timestamp such as "2026-07-04 12:00:00.000000+00:00" -
        # stored as TEXT in the _sqlite_migrations table
        applied_at: str

    def __init__(self, name: str):
        """
        :param name: The name of the migration set. This should be unique.
        """
        self.name = name
        self._migrations: list[Migrations._Migration] = []

    def __call__(
        self, *, name: str | None = None, transactional: bool = True
    ) -> Callable[[_MigrationFunctionT], _MigrationFunctionT]:
        """
        :param name: The name to use for this migration - if not provided,
          the name of the function will be used.
        :param transactional: If ``True`` (the default) the migration and the
          record of it having been applied are wrapped in a transaction, which
          will be rolled back if the migration raises an exception. Pass
          ``False`` for migrations that cannot run inside a transaction, for
          example those that execute ``VACUUM``.
        """

        def inner(func: _MigrationFunctionT) -> _MigrationFunctionT:
            migration_name = name or func.__name__
            if any(m.name == migration_name for m in self._migrations):
                raise ValueError(
                    f"Migration '{migration_name}' is already registered in set '{self.name}'"
                )
            self._migrations.append(
                self._Migration(migration_name, func, transactional)
            )
            return func

        return inner

    def pending(self, db: "Database") -> list["Migrations._Migration"]:
        """
        Return a list of pending migrations.

        This is a read-only operation - it does not write to the database.
        """
        already_applied = {migration.name for migration in self.applied(db)}
        return [
            migration
            for migration in self._migrations
            if migration.name not in already_applied
        ]

    def applied(self, db: "Database") -> list["Migrations._AppliedMigration"]:
        """
        Return a list of applied migrations, in the order they were applied.

        This is a read-only operation - it does not write to the database.
        """
        table = _table(db, self.migrations_table)
        if not table.exists():
            return []
        return [
            self._AppliedMigration(name=row["name"], applied_at=row["applied_at"])
            for row in table.rows_where(
                "migration_set = ?", [self.name], order_by="rowid"
            )
        ]

    def apply(self, db: "Database", *, stop_before: str | Iterable[str] | None = None):
        """
        Apply any pending migrations to the database.

        Each migration runs inside a transaction, together with the record of
        it having been applied - if the migration raises an exception its
        changes are rolled back, no record is written and the migration stays
        pending. Migrations registered with ``transactional=False`` run
        outside of a transaction.

        :raises ValueError: if a ``stop_before`` name matches a migration in
          this set that has already been applied - stopping before it is
          impossible to honor, and no pending migrations are applied
        """
        if stop_before is None:
            stop_before_names = set()
        elif isinstance(stop_before, str):
            stop_before_names = {stop_before}
        else:
            stop_before_names = set(stop_before)
        # A stop_before naming an already-applied migration cannot be
        # honored - error rather than applying everything after it. Names
        # not in this set at all are ignored, because unqualified CLI
        # values are offered to every migration set
        already_applied = stop_before_names.intersection(
            migration.name for migration in self.applied(db)
        )
        if already_applied:
            raise ValueError(
                "Cannot stop before migration{} {} in set '{}' - already "
                "been applied".format(
                    "s" if len(already_applied) > 1 else "",
                    ", ".join(sorted(already_applied)),
                    self.name,
                )
            )
        self.ensure_migrations_table(db)
        for migration in self.pending(db):
            name = migration.name
            if name in stop_before_names:
                return
            if migration.transactional:
                with db.atomic():
                    migration.fn(db)
                    self._record_applied(db, name)
            else:
                migration.fn(db)
                self._record_applied(db, name)

    def _record_applied(self, db: "Database", name: str):
        _table(db, self.migrations_table).insert(
            {
                "migration_set": self.name,
                "name": name,
                "applied_at": str(datetime.datetime.now(datetime.timezone.utc)),
            }
        )

    def ensure_migrations_table(self, db: "Database"):
        """
        Ensure the _sqlite_migrations table exists and has the correct schema.
        """
        table = _table(db, self.migrations_table)
        if not table.exists():
            table.create(
                {
                    "id": int,
                    "migration_set": str,
                    "name": str,
                    "applied_at": str,
                },
                pk="id",
            )
            table.create_index(["migration_set", "name"], unique=True)
        elif table.pks != ["id"]:
            table.transform(pk="id")
            unique_indexes = {tuple(index.columns) for index in table.indexes}
            if ("migration_set", "name") not in unique_indexes:
                table.create_index(["migration_set", "name"], unique=True)

    def __repr__(self):
        return "<Migrations '{}': [{}]>".format(
            self.name, ", ".join(m.name for m in self._migrations)
        )


def _table(db: "Database", name: str) -> "Table":
    return cast("Table", db[name])

```

### `sqlite_utils/plugins.py`

```py
import sys

import pluggy

from . import hookspecs

pm: pluggy.PluginManager = pluggy.PluginManager("sqlite_utils")
pm.add_hookspecs(hookspecs)
_plugins_loaded = False


def ensure_plugins_loaded() -> None:
    global _plugins_loaded
    if _plugins_loaded or getattr(sys, "_called_from_test", False):
        return
    pm.load_setuptools_entrypoints("sqlite_utils")
    _plugins_loaded = True


def get_plugins() -> list[dict[str, str | list[str]]]:
    ensure_plugins_loaded()
    plugins: list[dict[str, str | list[str]]] = []
    plugin_to_distinfo = dict(pm.list_plugin_distinfo())
    for plugin in pm.get_plugins():
        hookcallers = pm.get_hookcallers(plugin) or []
        plugin_info: dict[str, str | list[str]] = {
            "name": plugin.__name__,
            "hooks": [h.name for h in hookcallers],
        }
        distinfo = plugin_to_distinfo.get(plugin)
        if distinfo:
            plugin_info["version"] = distinfo.version
            plugin_info["name"] = distinfo.project_name
        plugins.append(plugin_info)
    return plugins

```

### `sqlite_utils/py.typed`

```typed

```

### `sqlite_utils/recipes.py`

```py
from __future__ import annotations

import json
from collections.abc import Callable

from dateutil import parser

IGNORE: object = object()
SET_NULL: object = object()


def parsedate(
    value: str,
    dayfirst: bool = False,
    yearfirst: bool = False,
    errors: object | None = None,
) -> str | None:
    """
    Parse a date and convert it to ISO date format: yyyy-mm-dd
    \b
    - dayfirst=True: treat xx as the day in xx/yy/zz
    - yearfirst=True: treat xx as the year in xx/yy/zz
    - errors=r.IGNORE to ignore values that cannot be parsed
    - errors=r.SET_NULL to set values that cannot be parsed to null
    """
    if not value:
        return value
    try:
        return (
            parser.parse(value, dayfirst=dayfirst, yearfirst=yearfirst)
            .date()
            .isoformat()
        )
    except parser.ParserError:
        if errors is IGNORE:
            return value
        elif errors is SET_NULL:
            return None
        else:
            raise


def parsedatetime(
    value: str,
    dayfirst: bool = False,
    yearfirst: bool = False,
    errors: object | None = None,
) -> str | None:
    """
    Parse a datetime and convert it to ISO datetime format: yyyy-mm-ddTHH:MM:SS
    \b
    - dayfirst=True: treat xx as the day in xx/yy/zz
    - yearfirst=True: treat xx as the year in xx/yy/zz
    - errors=r.IGNORE to ignore values that cannot be parsed
    - errors=r.SET_NULL to set values that cannot be parsed to null
    """
    if not value:
        return value
    try:
        return parser.parse(value, dayfirst=dayfirst, yearfirst=yearfirst).isoformat()
    except parser.ParserError:
        if errors is IGNORE:
            return value
        elif errors is SET_NULL:
            return None
        else:
            raise


def jsonsplit(
    value: str, delimiter: str = ",", type: Callable[[str], object] = str
) -> str:
    """
    Convert a string like a,b,c into a JSON array ["a", "b", "c"]
    """
    return json.dumps([type(s.strip()) for s in value.split(delimiter)])

```

### `sqlite_utils/utils.py`

```py
import base64
import contextlib
import csv
import enum
import hashlib
import importlib
import io
import itertools
import json
import os
import sys
from collections.abc import Callable, Generator, Iterable, Iterator
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Generic,
    TypeVar,
    Union,
    cast,
)

import click

from . import recipes

if TYPE_CHECKING:
    import sqlite3
    from sqlite3 import dbapi2

    OperationalError = dbapi2.OperationalError
else:
    try:
        sqlite3 = importlib.import_module("pysqlite3")
        dbapi2 = importlib.import_module("pysqlite3.dbapi2")
        OperationalError = dbapi2.OperationalError
    except ImportError:
        import sqlite3  # noqa: F401
        from sqlite3 import dbapi2

        OperationalError = dbapi2.OperationalError


SPATIALITE_PATHS = (
    "/usr/lib/x86_64-linux-gnu/mod_spatialite.so",
    "/usr/lib/aarch64-linux-gnu/mod_spatialite.so",
    "/usr/local/lib/mod_spatialite.dylib",
    "/usr/local/lib/mod_spatialite.so",
    "/opt/homebrew/lib/mod_spatialite.dylib",
)

# Mainly so we can restore it if needed in the tests:
ORIGINAL_CSV_FIELD_SIZE_LIMIT = csv.field_size_limit()

# Type alias for row dictionaries - values can be various SQLite-compatible types
RowValue = None | int | float | str | bytes | bool | list[str]
Row = dict[str, RowValue]

T = TypeVar("T")


class ANY:
    """Marker type for an SQLite ``ANY`` column."""


class _CloseableIterator(Iterator[Row]):
    """Iterator wrapper that closes a file when iteration is complete."""

    def __init__(self, iterator: Iterator[Row], closeable: io.IOBase) -> None:
        self._iterator = iterator
        self._closeable = closeable

    def __iter__(self) -> "_CloseableIterator":
        return self

    def __next__(self) -> Row:
        try:
            return next(self._iterator)
        except StopIteration:
            self._closeable.close()
            raise

    def close(self) -> None:
        self._closeable.close()


def maximize_csv_field_size_limit() -> None:
    """
    Increase the CSV field size limit to the maximum possible.
    """
    # https://stackoverflow.com/a/15063941
    field_size_limit = sys.maxsize

    while True:
        try:
            csv.field_size_limit(field_size_limit)
            break
        except OverflowError:
            field_size_limit = int(field_size_limit / 10)


def find_spatialite() -> str | None:
    """
    The ``find_spatialite()`` function searches for the `SpatiaLite <https://www.gaia-gis.it/fossil/libspatialite/index>`__
    SQLite extension in some common places. It returns a string path to the location, or ``None`` if SpatiaLite was not found.

    You can use it in code like this:

    .. code-block:: python

        from sqlite_utils import Database
        from sqlite_utils.utils import find_spatialite

        db = Database("mydb.db")
        spatialite = find_spatialite()
        if spatialite:
            db.conn.enable_load_extension(True)
            db.conn.load_extension(spatialite)

        # or use with db.init_spatialite like this
        db.init_spatialite(find_spatialite())

    """
    for path in SPATIALITE_PATHS:
        if os.path.exists(path):
            return path
    return None


def suggest_column_types(
    records: Iterable[dict[str, Any]],
) -> dict[str, type]:
    all_column_types: dict[str, set[type]] = {}
    for record in records:
        for key, value in record.items():
            all_column_types.setdefault(key, set()).add(type(value))
    return types_for_column_types(all_column_types)


def types_for_column_types(
    all_column_types: dict[str, set[type]],
) -> dict[str, type]:
    column_types: dict[str, type] = {}
    for key, types in all_column_types.items():
        # Ignore null values if at least one other type present:
        if len(types) > 1:
            types.discard(None.__class__)
        t: type
        if {None.__class__} == types:
            t = str
        elif len(types) == 1:
            t = next(iter(types))
            # But if it's a subclass of list / tuple / dict, use str
            # instead as we will be storing it as JSON in the table
            for superclass in (list, tuple, dict):
                if issubclass(t, superclass):
                    t = str
        elif {int, bool}.issuperset(types):
            t = int
        elif {int, float, bool}.issuperset(types):
            t = float
        elif {bytes, str}.issuperset(types):
            t = bytes
        else:
            t = str
        column_types[key] = t
    return column_types


def column_affinity(column_type: str) -> type:
    # Implementation of SQLite affinity rules from
    # https://www.sqlite.org/datatype3.html#determination_of_column_affinity
    assert isinstance(column_type, str)
    column_type = column_type.upper().strip()
    if column_type == "":
        return str  # We differ from spec, which says it should be BLOB
    if "INT" in column_type:
        return int
    if "CHAR" in column_type or "CLOB" in column_type or "TEXT" in column_type:
        return str
    if "BLOB" in column_type:
        return bytes
    if "REAL" in column_type or "FLOA" in column_type or "DOUB" in column_type:
        return float
    if column_type == "ANY":
        return ANY
    # Default is 'NUMERIC', which we currently also treat as float
    return float


def decode_base64_values(doc: dict[str, Any]) -> dict[str, Any]:
    # Looks for '{"$base64": true..., "encoded": ...}' values and decodes them
    to_fix = [
        k
        for k in doc
        if isinstance(doc[k], dict)
        and cast(dict, doc[k]).get("$base64") is True
        and "encoded" in cast(dict, doc[k])
    ]
    if not to_fix:
        return doc
    return dict(
        doc, **{k: base64.b64decode(cast(dict, doc[k])["encoded"]) for k in to_fix}
    )


class UpdateWrapper:
    def __init__(self, wrapped: io.IOBase, update: Callable[[int], None]) -> None:
        self._wrapped = wrapped
        self._update = update

    def __iter__(self) -> Iterator[bytes]:
        for line in self._wrapped:
            self._update(len(line))
            yield line

    def read(self, size: int = -1) -> bytes:
        data = self._wrapped.read(size)
        self._update(len(data))
        return data


@contextlib.contextmanager
def file_progress(
    file: io.IOBase, silent: bool = False, **kwargs: object
) -> Generator[Union[io.IOBase, "UpdateWrapper"], None, None]:
    if silent:
        yield file
        return
    # file.fileno() throws an exception in our test suite
    try:
        fileno = file.fileno()
    except io.UnsupportedOperation:
        yield file
        return
    if fileno == 0:  # 0 means stdin
        yield file
    else:
        file_length = os.path.getsize(file.name)  # type: ignore
        with click.progressbar(length=file_length, **kwargs) as bar:  # type: ignore
            yield UpdateWrapper(file, bar.update)


class Format(enum.Enum):
    CSV = 1
    TSV = 2
    JSON = 3
    NL = 4


class RowsFromFileError(Exception):
    pass


class RowsFromFileBadJSON(RowsFromFileError):
    pass


class RowError(Exception):
    pass


def _extra_key_strategy(
    reader: Iterable[dict[str | None, object]],
    ignore_extras: bool | None = False,
    extras_key: str | None = None,
) -> Iterable[Row]:
    # Logic for handling CSV rows with more values than there are headings
    for row in reader:
        # DictReader adds a 'None' key with extra row values
        if None not in row:
            yield cast(Row, row)
        elif ignore_extras:
            # ignoring row.pop(none) because of this issue:
            # https://github.com/simonw/sqlite-utils/issues/440#issuecomment-1155358637
            row.pop(None)
            yield cast(Row, row)
        elif not extras_key:
            extras = row.pop(None)
            raise RowError(f"Row {row} contained these extra values: {extras}")
        else:
            extras_value = row.pop(None)
            row_out = cast(Row, row)
            row_out[extras_key] = cast(RowValue, extras_value)
            yield row_out


def rows_from_file(
    fp: BinaryIO,
    format: Format | None = None,
    dialect: type[csv.Dialect] | None = None,
    encoding: str | None = None,
    ignore_extras: bool | None = False,
    extras_key: str | None = None,
) -> tuple[Iterable[Row], Format]:
    """
    Load a sequence of dictionaries from a file-like object containing one of four different formats.

    .. code-block:: python

        from sqlite_utils.utils import rows_from_file
        import io

        rows, format = rows_from_file(io.StringIO("id,name\\n1,Cleo")))
        print(list(rows), format)
        # Outputs [{'id': '1', 'name': 'Cleo'}] Format.CSV

    This defaults to attempting to automatically detect the format of the data, or you can pass in an
    explicit format using the format= option.

    Returns a tuple of ``(rows_generator, format_used)`` where ``rows_generator`` can be iterated over
    to return dictionaries, while ``format_used`` is a value from the ``sqlite_utils.utils.Format`` enum:

    .. code-block:: python

        class Format(enum.Enum):
            CSV = 1
            TSV = 2
            JSON = 3
            NL = 4

    If a CSV or TSV file includes rows with more fields than are declared in the header a
    ``sqlite_utils.utils.RowError`` exception will be raised when you loop over the generator.

    You can instead ignore the extra data by passing ``ignore_extras=True``.

    Or pass ``extras_key="rest"`` to put those additional values in a list in a key called ``rest``.

    :param fp: a file-like object containing binary data
    :param format: the format to use - omit this to detect the format
    :param dialect: the CSV dialect to use - omit this to detect the dialect
    :param encoding: the character encoding to use when reading CSV/TSV data
    :param ignore_extras: ignore any extra fields on rows
    :param extras_key: put any extra fields in a list with this key
    """
    if ignore_extras and extras_key:
        raise ValueError("Cannot use ignore_extras= and extras_key= together")
    if format == Format.JSON:
        decoded = json.load(fp)
        if isinstance(decoded, dict):
            decoded = [decoded]
        if not isinstance(decoded, list):
            raise RowsFromFileBadJSON("JSON must be a list or a dictionary")
        return decoded, Format.JSON
    elif format == Format.NL:
        return (json.loads(line) for line in fp if line.strip()), Format.NL
    elif format == Format.CSV:
        use_encoding: str = encoding or "utf-8-sig"
        decoded_fp = io.TextIOWrapper(fp, encoding=use_encoding)
        if dialect is not None:
            reader = csv.DictReader(decoded_fp, dialect=dialect)
        else:
            reader = csv.DictReader(decoded_fp)
        rows = _extra_key_strategy(
            cast(Iterable[dict[str | None, object]], reader),
            ignore_extras,
            extras_key,
        )
        return _CloseableIterator(iter(rows), decoded_fp), Format.CSV
    elif format == Format.TSV:
        rows, _ = rows_from_file(
            fp, format=Format.CSV, dialect=csv.excel_tab, encoding=encoding
        )
        return (
            _extra_key_strategy(
                cast(Iterable[dict[str | None, object]], rows),
                ignore_extras,
                extras_key,
            ),
            Format.TSV,
        )
    elif format is None:
        # Detect the format, then call this recursively
        buffered = io.BufferedReader(cast(io.RawIOBase, fp), buffer_size=4096)
        try:
            first_bytes = buffered.peek(2048).strip()
        except AttributeError:
            # Likely the user passed a TextIO when this needs a BytesIO
            raise TypeError(
                "rows_from_file() requires a file-like object that supports peek(), such as io.BytesIO"
            )
        if not first_bytes:
            return (), Format.CSV
        if first_bytes.startswith((b"[", b"{")):
            # TODO: Detect newline-JSON
            return rows_from_file(buffered, format=Format.JSON)
        else:
            dialect = csv.Sniffer().sniff(
                first_bytes.decode(encoding or "utf-8-sig", "ignore")
            )
            rows, _ = rows_from_file(
                buffered, format=Format.CSV, dialect=dialect, encoding=encoding
            )
            # Make sure we return the format we detected
            detected_format = Format.TSV if dialect.delimiter == "\t" else Format.CSV
            return (
                _extra_key_strategy(
                    cast(Iterable[dict[str | None, object]], rows),
                    ignore_extras,
                    extras_key,
                ),
                detected_format,
            )
    else:
        raise RowsFromFileError("Bad format")


class TypeTracker:
    """
    Wrap an iterator of dictionaries and keep track of which SQLite column
    types are the most likely fit for each of their keys.

    Example usage:

    .. code-block:: python

        from sqlite_utils.utils import TypeTracker
        import sqlite_utils

        db = sqlite_utils.Database(memory=True)
        tracker = TypeTracker()
        rows = [{"id": "1", "name": "Cleo", "id": "2", "name": "Cardi"}]
        db["creatures"].insert_all(tracker.wrap(rows))
        print(tracker.types)
        # Outputs {'id': 'integer', 'name': 'text'}
        db["creatures"].transform(types=tracker.types)
    """

    def __init__(self) -> None:
        self.trackers: dict[str, ValueTracker] = {}

    def wrap(self, iterator: Iterable[dict[str, Any]]) -> Iterable[dict[str, Any]]:
        """
        Use this to loop through an existing iterator, tracking the column types
        as part of the iteration.

        :param iterator: The iterator to wrap
        """
        for row in iterator:
            for key, value in row.items():
                tracker = self.trackers.setdefault(key, ValueTracker())
                tracker.evaluate(value)
            yield row

    @property
    def types(self) -> dict[str, str]:
        """
        A dictionary mapping column names to their detected types. This can be passed
        to the ``db[table_name].transform(types=tracker.types)`` method.
        """
        return {key: tracker.guessed_type for key, tracker in self.trackers.items()}


class ValueTracker:
    couldbe: dict[str, Callable[[object], bool]]

    def __init__(self) -> None:
        self.couldbe = {key: getattr(self, "test_" + key) for key in self.get_tests()}

    @classmethod
    def get_tests(cls) -> list[str]:
        return [
            key.split("test_")[-1] for key in cls.__dict__ if key.startswith("test_")
        ]

    def test_integer(self, value: object) -> bool:
        try:
            int(cast(Any, value))
            return True
        except (ValueError, TypeError):
            return False

    def test_float(self, value: object) -> bool:
        try:
            float(cast(Any, value))
            return True
        except (ValueError, TypeError):
            return False

    def __repr__(self) -> str:
        return self.guessed_type + ": possibilities = " + repr(self.couldbe)

    @property
    def guessed_type(self) -> str:
        options = set(self.couldbe.keys())
        # Return based on precedence
        for key in self.get_tests():
            if key in options:
                return key
        return "text"

    def evaluate(self, value: object) -> None:
        if not value or not self.couldbe:
            return
        not_these: list[str] = []
        for name, test in self.couldbe.items():
            if not test(value):
                not_these.append(name)
        for key in not_these:
            del self.couldbe[key]


class NullProgressBar(Generic[T]):
    def __init__(self, *args: Iterable[T]) -> None:
        self.args = args

    def __iter__(self) -> Iterator[T]:
        yield from self.args[0]

    def update(self, value: int) -> None:
        pass


@contextlib.contextmanager
def progressbar(*args: Iterable[T], **kwargs: Any) -> Generator[Any, None, None]:
    silent = kwargs.pop("silent")
    if silent:
        yield NullProgressBar(*args)
    else:
        with click.progressbar(*args, **kwargs) as bar:  # type: ignore
            yield bar


def _compile_code(
    code: str, imports: Iterable[str], variable: str = "value"
) -> Callable[..., Any]:
    globals_dict: dict[str, Any] = {"r": recipes, "recipes": recipes}
    # Handle imports first so they're available for all approaches
    for import_ in imports:
        globals_dict[import_.split(".")[0]] = __import__(import_)

    # If user defined a convert() function, return that
    try:
        exec(code, globals_dict)  # noqa: S102
        return cast(Callable[..., object], globals_dict["convert"])
    except (AttributeError, SyntaxError, NameError, KeyError, TypeError):
        pass

    # Check if code is a direct callable reference
    # e.g. "r.parsedate" instead of "r.parsedate(value)"
    try:
        fn = eval(code, globals_dict)
        if callable(fn):
            return cast(Callable[..., object], fn)
    except Exception:  # noqa: BLE001, S110
        pass

    # Try compiling their code as a function instead
    body_variants = [code]
    # If single line and no 'return', try adding the return
    if "\n" not in code and not code.strip().startswith("return "):
        body_variants.insert(0, f"return {code}")

    code_o = None
    for variant in body_variants:
        new_code = [f"def fn({variable}):"]
        for line in variant.split("\n"):
            new_code.append(f"    {line}")
        try:
            code_o = compile("\n".join(new_code), "<string>", "exec")
            break
        except SyntaxError:
            # Try another variant, e.g. for 'return row["column"] = 1'
            continue

    if code_o is None:
        raise SyntaxError("Could not compile code")

    exec(code_o, globals_dict)  # noqa: S102
    return cast(Callable[..., object], globals_dict["fn"])


def chunks(sequence: Iterable[T], size: int) -> Iterable[Iterable[T]]:
    """
    Iterate over chunks of the sequence of the given size.

    :param sequence: Any Python iterator
    :param size: The size of each chunk
    """
    iterator = iter(sequence)
    for item in iterator:
        yield itertools.chain([item], itertools.islice(iterator, size - 1))


def hash_record(record: dict[str, Any], keys: Iterable[str] | None = None) -> str:
    """
    ``record`` should be a Python dictionary. Returns a sha1 hash of the
    keys and values in that record.

    If ``keys=`` is provided, uses just those keys to generate the hash.

    Example usage::

        from sqlite_utils.utils import hash_record

        hashed = hash_record({"name": "Cleo", "twitter": "CleoPaws"})
        # Or with the keys= option:
        hashed = hash_record(
            {"name": "Cleo", "twitter": "CleoPaws", "age": 7},
            keys=("name", "twitter")
        )

    :param record: Record to generate a hash for
    :param keys: Subset of keys to use for that hash
    """
    to_hash: dict[str, Any] = record
    if keys is not None:
        to_hash = {key: record[key] for key in keys}
    return hashlib.sha1(
        json.dumps(to_hash, separators=(",", ":"), sort_keys=True, default=repr).encode(
            "utf8"
        )
    ).hexdigest()


def dedupe_keys(keys: Iterable[str]) -> list[str]:
    """
    Rename duplicates in a list of column names so every name is unique,
    by appending ``_2``, ``_3``... to later occurrences - skipping any
    suffix that would collide with another column in the list.

    Used when converting SQL query rows to dictionaries, where duplicate
    column names would otherwise silently overwrite each other.

    :param keys: List of column names, possibly containing duplicates
    """
    keys = list(keys)
    taken = set(keys)
    if len(taken) == len(keys):
        # No duplicates - the common case
        return keys
    seen: set = set()
    result = []
    for key in keys:
        if key in seen:
            new_key = key
            suffix = 2
            while new_key in seen or new_key in taken:
                new_key = f"{key}_{suffix}"
                suffix += 1
            key = new_key
        seen.add(key)
        result.append(key)
    return result


def _flatten(d: dict[str, Any]) -> Generator[tuple[str, Any], None, None]:
    for key, value in d.items():
        if isinstance(value, dict):
            for key2, value2 in _flatten(value):
                yield key + "_" + key2, value2
        else:
            yield key, value


def flatten(row: dict[str, Any]) -> dict[str, Any]:
    """
    Turn a nested dict e.g. ``{"a": {"b": 1}}`` into a flat dict: ``{"a_b": 1}``

    :param row: A Python dictionary, optionally with nested dictionaries
    """
    return dict(_flatten(row))

```

### `tests/__init__.py`

```py

```

### `tests/conftest.py`

```py
import pytest

from sqlite_utils import Database
from sqlite_utils.utils import sqlite3

CREATE_TABLES = """
create table Gosh (c1 text, c2 text, c3 text);
create table Gosh2 (c1 text, c2 text, c3 text);
"""


def pytest_addoption(parser):
    parser.addoption(
        "--sqlite-autocommit",
        action="store_true",
        default=False,
        help=(
            "Run every test against connections created with the Python 3.12+ "
            "sqlite3.connect(autocommit=True) mode"
        ),
    )


def pytest_configure(config):
    import sys

    sys._called_from_test = True  # type: ignore[attr-defined]

    if config.getoption("--sqlite-autocommit"):
        if sys.version_info < (3, 12):
            raise pytest.UsageError(
                "--sqlite-autocommit requires Python 3.12 or higher"
            )
        real_connect = sqlite3.connect

        def autocommit_connect(*args, **kwargs):
            kwargs.setdefault("autocommit", True)
            return real_connect(*args, **kwargs)

        sqlite3.connect = autocommit_connect


@pytest.fixture(autouse=True)
def close_all_databases():
    """Automatically close all Database objects created during a test."""
    databases = []
    original_init = Database.__init__

    def tracking_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        databases.append(self)

    Database.__init__ = tracking_init  # type: ignore[method-assign]
    yield
    Database.__init__ = original_init  # type: ignore[method-assign]
    for db in databases:
        try:
            db.close()
        except sqlite3.Error:
            pass


@pytest.fixture
def fresh_db():
    return Database(memory=True)


@pytest.fixture
def existing_db():
    database = Database(memory=True)
    database.executescript("""
        CREATE TABLE foo (text TEXT);
        INSERT INTO foo (text) values ("one");
        INSERT INTO foo (text) values ("two");
        INSERT INTO foo (text) values ("three");
    """)
    return database


@pytest.fixture
def db_path(tmpdir):
    path = str(tmpdir / "test.db")
    db = sqlite3.connect(path)
    db.executescript(CREATE_TABLES)
    db.close()
    return path

```

### `tests/ext.c`

```c
/*
** This file implements a SQLite extension with multiple entrypoints.
**
** The default entrypoint, sqlite3_ext_init, has a single function "a".
** The 1st alternate entrypoint, sqlite3_ext_b_init, has a single function "b".
** The 2nd alternate entrypoint, sqlite3_ext_c_init, has a single function "c".
**
** Compiling instructions:
**     https://www.sqlite.org/loadext.html#compiling_a_loadable_extension
**
*/

#include "sqlite3ext.h"

SQLITE_EXTENSION_INIT1

// SQL function that returns back the value supplied during sqlite3_create_function()
static void func(sqlite3_context *context, int argc, sqlite3_value **argv) {
  sqlite3_result_text(context, (char *) sqlite3_user_data(context), -1, SQLITE_STATIC);
}


// The default entrypoint, since it matches the "ext.dylib"/"ext.so" name
#ifdef _WIN32
__declspec(dllexport)
#endif
int sqlite3_ext_init(sqlite3 *db, char **pzErrMsg, const sqlite3_api_routines *pApi) {
  SQLITE_EXTENSION_INIT2(pApi);
  return sqlite3_create_function(db, "a", 0, 0, "a", func, 0, 0);
}

// Alternate entrypoint #1
#ifdef _WIN32
__declspec(dllexport)
#endif
int sqlite3_ext_b_init(sqlite3 *db, char **pzErrMsg, const sqlite3_api_routines *pApi) {
  SQLITE_EXTENSION_INIT2(pApi);
  return sqlite3_create_function(db, "b", 0, 0, "b", func, 0, 0);
}

// Alternate entrypoint #2
#ifdef _WIN32
__declspec(dllexport)
#endif
int sqlite3_ext_c_init(sqlite3 *db, char **pzErrMsg, const sqlite3_api_routines *pApi) {
  SQLITE_EXTENSION_INIT2(pApi);
  return sqlite3_create_function(db, "c", 0, 0, "c", func, 0, 0);
}

```

### `tests/sniff/example1.csv`

```csv
id,species,name,age
1,dog,Cleo,5
2,dog,Pancakes,4
3,cat,Mozie,8
4,spider,"Daisy, the tarantula",6

```

### `tests/sniff/example2.csv`

```csv
id;species;name;age
1;dog;Cleo;5
2;dog;Pancakes;4
3;cat;Mozie;8
4;spider;"Daisy, the tarantula";6

```

### `tests/sniff/example3.csv`

```csv
id,species,name,age
1,dog,Cleo,5
2,dog,Pancakes,4
3,cat,Mozie,8
4,spider,'Daisy, the tarantula',6

```

### `tests/sniff/example4.csv`

```csv
id	species	name	age
1	dog	Cleo	5
2	dog	Pancakes	4
3	cat	Mozie	8
4	spider	'Daisy, the tarantula'	6

```

### `tests/test_analyze_tables.py`

```py
import sqlite3

import pytest
from click.testing import CliRunner

from sqlite_utils import cli
from sqlite_utils.db import ColumnDetails, Database


@pytest.fixture
def db_to_analyze(fresh_db):
    stuff = fresh_db.table("stuff")
    stuff.insert_all(
        [
            {"id": 1, "owner": "Terryterryterry", "size": 5},
            {"id": 2, "owner": "Joan", "size": 4},
            {"id": 3, "owner": "Kumar", "size": 5},
            {"id": 4, "owner": "Anne", "size": 5},
            {"id": 5, "owner": "Terryterryterry", "size": 5},
            {"id": 6, "owner": "Joan", "size": 4},
            {"id": 7, "owner": "Kumar", "size": 5},
            {"id": 8, "owner": "Joan", "size": 4},
        ],
        pk="id",
    )
    return fresh_db


@pytest.fixture
def big_db_to_analyze_path(tmpdir):
    path = str(tmpdir / "test.db")
    db = Database(path)
    categories = {
        "A": 40,
        "B": 30,
        "C": 20,
        "D": 10,
    }
    to_insert = []
    for category, count in categories.items():
        for _ in range(count):
            to_insert.append(
                {
                    "category": category,
                    "all_null": None,
                }
            )
    db.table("stuff").insert_all(to_insert)
    return path


@pytest.mark.parametrize(
    "column,extra_kwargs,expected",
    [
        (
            "id",
            {},
            ColumnDetails(
                table="stuff",
                column="id",
                total_rows=8,
                num_null=0,
                num_blank=0,
                num_distinct=8,
                most_common=None,
                least_common=None,
            ),
        ),
        (
            "owner",
            {},
            ColumnDetails(
                table="stuff",
                column="owner",
                total_rows=8,
                num_null=0,
                num_blank=0,
                num_distinct=4,
                most_common=[("Joan", 3), ("Kumar", 2)],
                least_common=[("Anne", 1), ("Terry...", 2)],
            ),
        ),
        (
            "size",
            {},
            ColumnDetails(
                table="stuff",
                column="size",
                total_rows=8,
                num_null=0,
                num_blank=0,
                num_distinct=2,
                most_common=[(5, 5), (4, 3)],
                least_common=None,
            ),
        ),
        (
            "owner",
            {"most_common": False},
            ColumnDetails(
                table="stuff",
                column="owner",
                total_rows=8,
                num_null=0,
                num_blank=0,
                num_distinct=4,
                most_common=None,
                least_common=[("Anne", 1), ("Terry...", 2)],
            ),
        ),
        (
            "owner",
            {"least_common": False},
            ColumnDetails(
                table="stuff",
                column="owner",
                total_rows=8,
                num_null=0,
                num_blank=0,
                num_distinct=4,
                most_common=[("Joan", 3), ("Kumar", 2)],
                least_common=None,
            ),
        ),
    ],
)
def test_analyze_column(db_to_analyze, column, extra_kwargs, expected):
    assert (
        db_to_analyze.table("stuff").analyze_column(
            column, common_limit=2, value_truncate=5, **extra_kwargs
        )
        == expected
    )


@pytest.fixture
def db_to_analyze_path(db_to_analyze, tmpdir):
    path = str(tmpdir / "test.db")
    db = sqlite3.connect(path)
    sql = "\n".join(db_to_analyze.iterdump())
    db.executescript(sql)
    db.close()
    return path


def test_analyze_table(db_to_analyze_path):
    result = CliRunner().invoke(cli.cli, ["analyze-tables", db_to_analyze_path])
    assert result.output.strip() == ("""
stuff.id: (1/3)

  Total rows: 8
  Null rows: 0
  Blank rows: 0

  Distinct values: 8

stuff.owner: (2/3)

  Total rows: 8
  Null rows: 0
  Blank rows: 0

  Distinct values: 4

  Most common:
    3: Joan
    2: Terryterryterry
    2: Kumar
    1: Anne

stuff.size: (3/3)

  Total rows: 8
  Null rows: 0
  Blank rows: 0

  Distinct values: 2

  Most common:
    5: 5
    3: 4""").strip()


def test_analyze_table_save(db_to_analyze_path):
    result = CliRunner().invoke(
        cli.cli, ["analyze-tables", db_to_analyze_path, "--save"]
    )
    assert result.exit_code == 0
    rows = list(Database(db_to_analyze_path).table("_analyze_tables_").rows)
    assert rows == [
        {
            "table": "stuff",
            "column": "id",
            "total_rows": 8,
            "num_null": 0,
            "num_blank": 0,
            "num_distinct": 8,
            "most_common": None,
            "least_common": None,
        },
        {
            "table": "stuff",
            "column": "owner",
            "total_rows": 8,
            "num_null": 0,
            "num_blank": 0,
            "num_distinct": 4,
            "most_common": '[["Joan", 3], ["Terryterryterry", 2], ["Kumar", 2], ["Anne", 1]]',
            "least_common": None,
        },
        {
            "table": "stuff",
            "column": "size",
            "total_rows": 8,
            "num_null": 0,
            "num_blank": 0,
            "num_distinct": 2,
            "most_common": "[[5, 5], [4, 3]]",
            "least_common": None,
        },
    ]


@pytest.mark.parametrize(
    "no_most,no_least",
    (
        (False, False),
        (True, False),
        (False, True),
        (True, True),
    ),
)
def test_analyze_table_save_no_most_no_least_options(
    no_most, no_least, big_db_to_analyze_path
):
    args = [
        "analyze-tables",
        big_db_to_analyze_path,
        "--save",
        "--common-limit",
        "2",
        "--column",
        "category",
    ]
    if no_most:
        args.append("--no-most")
    if no_least:
        args.append("--no-least")
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 0
    rows = list(Database(big_db_to_analyze_path).table("_analyze_tables_").rows)
    expected = {
        "table": "stuff",
        "column": "category",
        "total_rows": 100,
        "num_null": 0,
        "num_blank": 0,
        "num_distinct": 4,
        "most_common": None,
        "least_common": None,
    }
    if not no_most:
        expected["most_common"] = '[["A", 40], ["B", 30]]'
    if not no_least:
        expected["least_common"] = '[["D", 10], ["C", 20]]'

    assert rows == [expected]


def test_analyze_table_column_all_nulls(big_db_to_analyze_path):
    result = CliRunner().invoke(
        cli.cli,
        ["analyze-tables", big_db_to_analyze_path, "stuff", "--column", "all_null"],
    )
    assert result.exit_code == 0
    assert result.output == (
        "stuff.all_null: (1/1)\n\n  Total rows: 100\n"
        "  Null rows: 100\n"
        "  Blank rows: 0\n"
        "\n"
        "  Distinct values: 0\n\n"
    )


@pytest.mark.parametrize(
    "args,expected_error",
    (
        (["-c", "bad_column"], "These columns were not found: bad_column\n"),
        (["one", "-c", "age"], "These columns were not found: age\n"),
        (["two", "-c", "age"], None),
        (
            ["one", "-c", "age", "--column", "bad"],
            "These columns were not found: age, bad\n",
        ),
    ),
)
def test_analyze_table_validate_columns(tmpdir, args, expected_error):
    path = str(tmpdir / "test_validate_columns.db")
    db = Database(path)
    db.table("one").insert(
        {
            "id": 1,
            "name": "one",
        }
    )
    db.table("two").insert(
        {
            "id": 1,
            "age": 5,
        }
    )
    result = CliRunner().invoke(
        cli.cli,
        ["analyze-tables", path] + args,
        catch_exceptions=False,
    )
    assert result.exit_code == (1 if expected_error else 0)
    if expected_error:
        assert expected_error in result.output

```

### `tests/test_analyze.py`

```py
import pytest


@pytest.fixture
def db(fresh_db):
    fresh_db.table("one_index").insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.table("one_index").create_index(["name"])
    fresh_db.table("two_indexes").insert(
        {"id": 1, "name": "Cleo", "species": "dog"}, pk="id"
    )
    fresh_db.table("two_indexes").create_index(["name"])
    fresh_db.table("two_indexes").create_index(["species"])
    return fresh_db


def test_analyze_whole_database(db):
    assert set(db.table_names()) == {"one_index", "two_indexes"}
    db.analyze()
    assert set(db.table_names()).issuperset(
        {"one_index", "two_indexes", "sqlite_stat1"}
    )
    assert list(db.table("sqlite_stat1").rows) == [
        {"tbl": "two_indexes", "idx": "idx_two_indexes_species", "stat": "1 1"},
        {"tbl": "two_indexes", "idx": "idx_two_indexes_name", "stat": "1 1"},
        {"tbl": "one_index", "idx": "idx_one_index_name", "stat": "1 1"},
    ]


@pytest.mark.parametrize("method", ("db_method_with_name", "table_method"))
def test_analyze_one_table(db, method):
    assert set(db.table_names()).issuperset({"one_index", "two_indexes"})
    if method == "db_method_with_name":
        db.analyze("one_index")
    elif method == "table_method":
        db.table("one_index").analyze()

    assert set(db.table_names()).issuperset(
        {"one_index", "two_indexes", "sqlite_stat1"}
    )
    assert list(db.table("sqlite_stat1").rows) == [
        {"tbl": "one_index", "idx": "idx_one_index_name", "stat": "1 1"}
    ]


def test_analyze_index_by_name(db):
    assert set(db.table_names()) == {"one_index", "two_indexes"}
    db.analyze("idx_two_indexes_species")
    assert set(db.table_names()).issuperset(
        {"one_index", "two_indexes", "sqlite_stat1"}
    )
    assert list(db.table("sqlite_stat1").rows) == [
        {"tbl": "two_indexes", "idx": "idx_two_indexes_species", "stat": "1 1"},
    ]

```

### `tests/test_atomic.py`

```py
import pytest

from sqlite_utils.db import Database, _iter_complete_sql_statements
from sqlite_utils.utils import sqlite3


@pytest.mark.parametrize(
    "sql,expected",
    (
        (
            "CREATE TABLE t(id); INSERT INTO t VALUES (1)",
            ["CREATE TABLE t(id);", "INSERT INTO t VALUES (1)"],
        ),
        (
            "INSERT INTO t VALUES ('a;b');",
            ["INSERT INTO t VALUES ('a;b');"],
        ),
        (
            "-- comment;\nCREATE TABLE t(id);",
            ["-- comment;\nCREATE TABLE t(id);"],
        ),
        (
            """
            CREATE TRIGGER t_ai AFTER INSERT ON t
            BEGIN
                UPDATE t SET value = 'a;b' WHERE id = new.id;
                INSERT INTO log VALUES ('x;y');
            END;
            """,
            [
                (
                    "CREATE TRIGGER t_ai AFTER INSERT ON t\n"
                    "            BEGIN\n"
                    "                UPDATE t SET value = 'a;b' WHERE id = new.id;\n"
                    "                INSERT INTO log VALUES ('x;y');\n"
                    "            END;"
                )
            ],
        ),
    ),
)
def test_iter_complete_sql_statements(sql, expected):
    assert list(_iter_complete_sql_statements(sql)) == expected


def test_atomic_commits(fresh_db):
    with fresh_db.atomic():
        fresh_db.table("dogs").insert({"id": 1, "name": "Cleo"}, pk="id")

    assert list(fresh_db.table("dogs").rows) == [{"id": 1, "name": "Cleo"}]


def test_atomic_rolls_back(fresh_db):
    with pytest.raises(RuntimeError), fresh_db.atomic():
        fresh_db.table("dogs").insert({"id": 1, "name": "Cleo"}, pk="id")
        raise RuntimeError("boom")

    assert not fresh_db.table("dogs").exists()


def test_nested_atomic_rolls_back_to_savepoint(fresh_db):
    fresh_db.table("dogs").create({"id": int, "name": str}, pk="id")

    with fresh_db.atomic():
        fresh_db.table("dogs").insert({"id": 1, "name": "Cleo"})
        with pytest.raises(RuntimeError), fresh_db.atomic():
            fresh_db.table("dogs").insert({"id": 2, "name": "Pancakes"})
            raise RuntimeError("boom")
        fresh_db.table("dogs").insert({"id": 3, "name": "Marnie"})

    assert list(fresh_db.table("dogs").rows) == [
        {"id": 1, "name": "Cleo"},
        {"id": 3, "name": "Marnie"},
    ]


def test_outer_atomic_rolls_back_released_savepoint(fresh_db):
    with pytest.raises(RuntimeError), fresh_db.atomic():
        fresh_db.table("dogs").insert({"id": 1, "name": "Cleo"}, pk="id")
        with fresh_db.atomic():
            fresh_db.table("dogs").insert({"id": 2, "name": "Pancakes"})
        raise RuntimeError("boom")

    assert not fresh_db.table("dogs").exists()


def test_executescript_does_not_commit_open_atomic_block(fresh_db):
    with pytest.raises(RuntimeError), fresh_db.atomic():
        fresh_db.executescript("""
                CREATE TABLE dogs(id INTEGER PRIMARY KEY, name TEXT);
                CREATE TRIGGER dogs_ai AFTER INSERT ON dogs
                BEGIN
                    UPDATE dogs SET name = upper(new.name) || '; updated' WHERE id = new.id;
                END;
                -- This comment has a semicolon;
                INSERT INTO dogs VALUES (1, 'Cleo; the first');
            """)
        raise RuntimeError("boom")

    assert not fresh_db.table("dogs").exists()


def test_transform_does_not_commit_open_atomic_block(fresh_db):
    fresh_db.table("dogs").insert({"id": 1, "name": "Cleo", "age": "5"}, pk="id")

    with pytest.raises(RuntimeError), fresh_db.atomic():
        fresh_db.table("dogs").insert({"id": 2, "name": "Pancakes", "age": "6"})
        fresh_db.table("dogs").transform(rename={"age": "dog_age"})
        raise RuntimeError("boom")

    assert (
        fresh_db.table("dogs").schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" TEXT\n)'
    )
    assert list(fresh_db.table("dogs").rows) == [
        {"id": 1, "name": "Cleo", "age": "5"},
    ]


def test_transform_parent_table_with_foreign_keys_in_atomic(fresh_db):
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.table("authors").insert({"id": 1, "name": "Tina"}, pk="id")
    fresh_db.table("books").insert(
        {"id": 1, "title": "Book", "author_id": 1},
        pk="id",
        foreign_keys={"author_id"},
    )

    with fresh_db.atomic():
        fresh_db.table("authors").transform(rename={"name": "full_name"})
        assert fresh_db.conn.execute("PRAGMA foreign_keys").fetchone()[0]

    assert (
        fresh_db.table("authors").schema
        == 'CREATE TABLE "authors" (\n   "id" INTEGER PRIMARY KEY,\n   "full_name" TEXT\n)'
    )
    assert fresh_db.execute("PRAGMA foreign_key_check").fetchall() == []


def test_transform_parent_table_with_foreign_keys_rolls_back(fresh_db):
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.table("authors").insert({"id": 1, "name": "Tina"}, pk="id")
    fresh_db.table("books").insert(
        {"id": 1, "title": "Book", "author_id": 1},
        pk="id",
        foreign_keys={"author_id"},
    )

    with pytest.raises(RuntimeError), fresh_db.atomic():
        fresh_db.table("authors").transform(rename={"name": "full_name"})
        raise RuntimeError("boom")

    assert (
        fresh_db.table("authors").schema
        == 'CREATE TABLE "authors" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT\n)'
    )
    assert fresh_db.conn.execute("PRAGMA foreign_keys").fetchone()[0]
    assert fresh_db.execute("PRAGMA foreign_key_check").fetchall() == []


def test_transform_detects_foreign_key_check_violations(fresh_db):
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.table("authors").insert({"id": 1, "name": "Tina"}, pk="id")
    fresh_db.table("books").insert({"id": 1, "author_id": 2}, pk="id")

    with pytest.raises(sqlite3.IntegrityError):
        fresh_db.table("books").transform(
            add_foreign_keys=(("author_id", "authors", "id"),)
        )

    assert fresh_db.table("books").foreign_keys == []
    assert fresh_db.conn.execute("PRAGMA foreign_keys").fetchone()[0]


def test_atomic_inside_manual_transaction_uses_savepoint(fresh_db):
    fresh_db.table("t").insert({"id": 1}, pk="id")
    fresh_db.execute("begin")
    with fresh_db.atomic():
        fresh_db.table("t").insert({"id": 2}, pk="id")
    # Nothing is committed until the user's own transaction commits
    assert fresh_db.conn.in_transaction
    fresh_db.rollback()
    assert [r["id"] for r in fresh_db.table("t").rows] == [1]
    # And with a commit instead, the atomic block's writes persist
    fresh_db.execute("begin")
    with fresh_db.atomic():
        fresh_db.table("t").insert({"id": 3}, pk="id")
    fresh_db.commit()
    assert [r["id"] for r in fresh_db.table("t").rows] == [1, 3]


def test_begin_commit_rollback(tmpdir):
    path = str(tmpdir / "test.db")
    db = Database(path)
    db.table("t").insert({"id": 1}, pk="id")
    db.begin()
    db.table("t").insert({"id": 2}, pk="id")
    assert db.conn.in_transaction
    db.rollback()
    assert not db.conn.in_transaction
    assert [r["id"] for r in db.table("t").rows] == [1]
    db.begin()
    db.table("t").insert({"id": 3}, pk="id")
    db.commit()
    db.close()
    db2 = Database(path)
    assert [r["id"] for r in db2.table("t").rows] == [1, 3]
    db2.close()


def test_begin_inside_transaction_errors(fresh_db):
    fresh_db.begin()
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.begin()
    fresh_db.rollback()


def test_commit_and_rollback_without_transaction_are_noops(fresh_db):
    fresh_db.commit()
    fresh_db.rollback()
    assert not fresh_db.conn.in_transaction


def test_execute_write_commits_immediately(tmpdir):
    path = str(tmpdir / "test.db")
    db = Database(path)
    db.table("t").insert({"id": 1}, pk="id")
    db.execute("insert into t (id) values (2)")
    # No implicit transaction is left open
    assert not db.conn.in_transaction
    # A completely separate connection sees the row straight away
    other = sqlite3.connect(path)
    assert other.execute("select count(*) from t").fetchone()[0] == 2
    other.close()
    db.close()


def test_execute_write_respects_explicit_transaction(fresh_db):
    fresh_db.table("t").insert({"id": 1}, pk="id")
    fresh_db.begin()
    fresh_db.execute("insert into t (id) values (2)")
    # Still inside the explicit transaction - not committed
    assert fresh_db.conn.in_transaction
    fresh_db.rollback()
    assert [r["id"] for r in fresh_db.table("t").rows] == [1]


def test_execute_comment_prefixed_begin_leaves_transaction_open(fresh_db):
    # A BEGIN hidden behind a leading comment must not be auto-committed
    # out from under the caller
    fresh_db.table("t").insert({"id": 1}, pk="id")
    fresh_db.execute("-- start a transaction\nbegin")
    assert fresh_db.conn.in_transaction
    fresh_db.execute("insert into t (id) values (2)")
    fresh_db.rollback()
    assert [r["id"] for r in fresh_db.table("t").rows] == [1]


def _sqlite_accepts_bom():
    try:
        sqlite3.connect(":memory:").execute("\ufeffselect 1")
        return True
    except sqlite3.OperationalError:
        return False


@pytest.mark.parametrize("begin_sql", ["; begin", "\ufeffbegin"])
def test_execute_prefixed_begin_leaves_transaction_open(fresh_db, begin_sql):
    # sqlite3 tolerates empty statements and a UTF-8 BOM before the first
    # real token, so a BEGIN behind either must not be auto-committed
    # out from under the caller
    if begin_sql.startswith("\ufeff") and not _sqlite_accepts_bom():
        pytest.skip("This SQLite version rejects a leading byte order mark")
    fresh_db.table("t").insert({"id": 1}, pk="id")
    fresh_db.execute(begin_sql)
    assert fresh_db.conn.in_transaction
    fresh_db.execute("insert into t (id) values (2)")
    fresh_db.rollback()
    assert [r["id"] for r in fresh_db.table("t").rows] == [1]


def test_execute_failed_write_rolls_back_implicit_transaction(tmpdir):
    # A failed write must not leave the driver's implicit transaction open -
    # that would silently disable auto-commit for every subsequent write
    path = str(tmpdir / "test.db")
    db = Database(path)
    db.table("t").insert({"id": 1}, pk="id")
    with pytest.raises(sqlite3.IntegrityError):
        db.execute("insert into t (id) values (1)")
    assert not db.conn.in_transaction
    # Subsequent writes commit as normal and survive closing the connection
    db.table("other").insert({"id": 2})
    db.close()
    db2 = Database(path)
    assert db2.table("other").exists()
    db2.close()


def test_execute_failed_write_preserves_explicit_transaction(fresh_db):
    # A failed write inside an explicit transaction must not roll back
    # the caller's earlier work - only the caller decides that
    fresh_db.table("t").insert({"id": 1}, pk="id")
    fresh_db.begin()
    fresh_db.execute("insert into t (id) values (2)")
    with pytest.raises(sqlite3.IntegrityError):
        fresh_db.execute("insert into t (id) values (1)")
    assert fresh_db.conn.in_transaction
    fresh_db.commit()
    assert [r["id"] for r in fresh_db.table("t").rows] == [1, 2]


def test_execute_failed_write_inside_atomic_preserves_block(fresh_db):
    # A caught failure inside an atomic() block must leave the block's
    # transaction open so its other work still commits
    fresh_db.table("t").insert({"id": 1}, pk="id")
    with fresh_db.atomic():
        fresh_db.execute("insert into t (id) values (2)")
        with pytest.raises(sqlite3.IntegrityError):
            fresh_db.execute("insert into t (id) values (1)")
    assert [r["id"] for r in fresh_db.table("t").rows] == [1, 2]


def test_query_returning_commits_after_iteration(tmpdir):
    if sqlite3.sqlite_version_info < (3, 35, 0):
        import pytest as _pytest

        _pytest.skip("RETURNING requires SQLite 3.35.0 or higher")
    path = str(tmpdir / "test.db")
    db = Database(path)
    db.table("t").insert({"id": 1}, pk="id")
    rows = list(db.query("insert into t (id) values (2) returning id"))
    assert rows == [{"id": 2}]
    assert not db.conn.in_transaction
    other = sqlite3.connect(path)
    assert other.execute("select count(*) from t").fetchone()[0] == 2
    other.close()
    db.close()


TRIGGER_SQL = """
create trigger no_bad before insert on t
when new.v = 'bad'
begin
    select raise(rollback, 'trigger says no');
end
"""


def test_atomic_preserves_error_from_transaction_destroying_trigger(fresh_db):
    # RAISE(ROLLBACK) rolls back the whole transaction and destroys every
    # savepoint - atomic()'s cleanup must not mask the IntegrityError
    # with "cannot rollback - no transaction is active"
    fresh_db.execute("create table t (id integer primary key, v text)")
    fresh_db.execute(TRIGGER_SQL)
    with (
        pytest.raises(sqlite3.IntegrityError, match="trigger says no"),
        fresh_db.atomic(),
    ):
        fresh_db.execute("insert into t (v) values ('bad')")
    assert not fresh_db.conn.in_transaction


def test_nested_atomic_preserves_error_from_transaction_destroying_trigger(
    fresh_db,
):
    # The nested savepoint branch previously raised
    # "no such savepoint" from ROLLBACK TO SAVEPOINT
    fresh_db.execute("create table t (id integer primary key, v text)")
    fresh_db.execute(TRIGGER_SQL)
    with (
        pytest.raises(sqlite3.IntegrityError, match="trigger says no"),
        fresh_db.atomic(),
        fresh_db.atomic(),
    ):
        fresh_db.execute("insert into t (v) values ('bad')")
    assert not fresh_db.conn.in_transaction


def test_atomic_preserves_error_from_insert_or_rollback(fresh_db):
    fresh_db.table("t").insert({"id": 1}, pk="id")
    with pytest.raises(sqlite3.IntegrityError), fresh_db.atomic():
        fresh_db.execute("insert or rollback into t (id) values (1)")
    assert not fresh_db.conn.in_transaction

```

### `tests/test_attach.py`

```py
from sqlite_utils import Database


def test_attach(tmpdir):
    foo_path = str(tmpdir / "foo.db")
    bar_path = str(tmpdir / "bar.db")
    db = Database(foo_path)
    with db.conn:
        db.table("foo").insert({"id": 1, "text": "foo"})
    db2 = Database(bar_path)
    with db2.conn:
        db2.table("bar").insert({"id": 1, "text": "bar"})
    db.attach("bar", bar_path)
    assert db.execute(
        "select * from foo union all select * from bar.bar"
    ).fetchall() == [(1, "foo"), (1, "bar")]

```

### `tests/test_cli_bulk.py`

```py
import pathlib
import subprocess
import sys
import time

import pytest
from click.testing import CliRunner

from sqlite_utils import Database, cli


@pytest.fixture
def test_db_and_path(tmpdir):
    db_path = str(pathlib.Path(tmpdir) / "data.db")
    db = Database(db_path)
    db.table("example").insert_all(
        [
            {"id": 1, "name": "One"},
            {"id": 2, "name": "Two"},
        ],
        pk="id",
    )
    return db, db_path


def test_cli_bulk(test_db_and_path):
    db, db_path = test_db_and_path
    result = CliRunner().invoke(
        cli.cli,
        [
            "bulk",
            db_path,
            "insert into example (id, name) values (:id, myupper(:name))",
            "-",
            "--nl",
            "--functions",
            "myupper = lambda s: s.upper()",
        ],
        input='{"id": 3, "name": "Three"}\n{"id": 4, "name": "Four"}\n',
    )
    assert result.exit_code == 0, result.output
    assert [
        {"id": 1, "name": "One"},
        {"id": 2, "name": "Two"},
        {"id": 3, "name": "THREE"},
        {"id": 4, "name": "FOUR"},
    ] == list(db.table("example").rows)


def test_cli_bulk_multiple_functions(test_db_and_path):
    db, db_path = test_db_and_path
    result = CliRunner().invoke(
        cli.cli,
        [
            "bulk",
            db_path,
            "insert into example (id, name) values (:id, myupper(mylower(:name)))",
            "-",
            "--nl",
            "--functions",
            "myupper = lambda s: s.upper()",
            "--functions",
            "mylower = lambda s: s.lower()",
        ],
        input='{"id": 3, "name": "ThReE"}\n{"id": 4, "name": "FoUr"}\n',
    )
    assert result.exit_code == 0, result.output
    assert [
        {"id": 1, "name": "One"},
        {"id": 2, "name": "Two"},
        {"id": 3, "name": "THREE"},
        {"id": 4, "name": "FOUR"},
    ] == list(db.table("example").rows)


def test_cli_bulk_batch_size(test_db_and_path):
    db, db_path = test_db_and_path
    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "sqlite_utils",
            "bulk",
            db_path,
            "insert into example (id, name) values (:id, :name)",
            "-",
            "--nl",
            "--batch-size",
            "2",
        ],
        stdin=subprocess.PIPE,
        stdout=sys.stdout,
    )
    assert proc.stdin is not None
    # Writing one record should not commit
    proc.stdin.write(b'{"id": 3, "name": "Three"}\n\n')
    proc.stdin.flush()
    time.sleep(1)
    assert db.table("example").count == 2

    # Writing another should trigger a commit:
    proc.stdin.write(b'{"id": 4, "name": "Four"}\n\n')
    proc.stdin.flush()
    time.sleep(1)
    assert db.table("example").count == 4

    proc.stdin.close()
    proc.wait()
    assert proc.returncode == 0


def test_cli_bulk_error(test_db_and_path):
    _, db_path = test_db_and_path
    result = CliRunner().invoke(
        cli.cli,
        [
            "bulk",
            db_path,
            "insert into example (id, name) value (:id, :name)",
            "-",
            "--nl",
        ],
        input='{"id": 3, "name": "Three"}',
    )
    assert result.exit_code == 1
    assert result.output == 'Error: near "value": syntax error\n'

```

### `tests/test_cli_convert.py`

```py
import json
import pathlib
import textwrap

import pytest
from click.testing import CliRunner

import sqlite_utils
from sqlite_utils import cli


@pytest.fixture
def test_db_and_path(fresh_db_and_path):
    db, db_path = fresh_db_and_path
    db.table("example").insert_all(
        [
            {"id": 1, "dt": "5th October 2019 12:04"},
            {"id": 2, "dt": "6th October 2019 00:05:06"},
            {"id": 3, "dt": ""},
            {"id": 4, "dt": None},
        ],
        pk="id",
    )
    return db, db_path


@pytest.fixture
def fresh_db_and_path(tmpdir):
    db_path = str(pathlib.Path(tmpdir) / "data.db")
    db = sqlite_utils.Database(db_path)
    return db, db_path


@pytest.mark.parametrize(
    "code",
    [
        "return value.replace('October', 'Spooktober')",
        # Return is optional:
        "value.replace('October', 'Spooktober')",
        # Multiple lines are supported:
        "v = value.replace('October', 'Spooktober')\nreturn v",
        # Can also define a convert() function
        "def convert(value): return value.replace('October', 'Spooktober')",
        # ... with imports
        "import re\n\ndef convert(value): return value.replace('October', 'Spooktober')",
    ],
)
def test_convert_code(fresh_db_and_path, code):
    db, db_path = fresh_db_and_path
    db.table("t").insert({"text": "October"})
    result = CliRunner().invoke(
        cli.cli, ["convert", db_path, "t", "text", code], catch_exceptions=False
    )
    assert result.exit_code == 0, result.output
    value = next(iter(db.table("t").rows))["text"]
    assert value == "Spooktober"


@pytest.mark.parametrize(
    "bad_code",
    (
        "def foo(value)",
        "$",
    ),
)
def test_convert_code_errors(fresh_db_and_path, bad_code):
    db, db_path = fresh_db_and_path
    db.table("t").insert({"text": "October"})
    result = CliRunner().invoke(
        cli.cli, ["convert", db_path, "t", "text", bad_code], catch_exceptions=False
    )
    assert result.exit_code == 1
    assert result.output == "Error: Could not compile code\n"


def test_convert_import(test_db_and_path):
    db, db_path = test_db_and_path
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
            "dt",
            "return re.sub('O..', 'OXX', value) if value else value",
            "--import",
            "re",
        ],
    )
    assert result.exit_code == 0, result.output
    assert [
        {"id": 1, "dt": "5th OXXober 2019 12:04"},
        {"id": 2, "dt": "6th OXXober 2019 00:05:06"},
        {"id": 3, "dt": ""},
        {"id": 4, "dt": None},
    ] == list(db.table("example").rows)


def test_convert_import_nested(fresh_db_and_path):
    db, db_path = fresh_db_and_path
    db.table("example").insert({"xml": '<item name="Cleo" />'})
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
            "xml",
            'xml.etree.ElementTree.fromstring(value).attrib["name"]',
            "--import",
            "xml.etree.ElementTree",
        ],
    )
    assert result.exit_code == 0, result.output
    assert [
        {"xml": "Cleo"},
    ] == list(db.table("example").rows)


def test_convert_dryrun(test_db_and_path):
    db, db_path = test_db_and_path
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
            "dt",
            "return re.sub('O..', 'OXX', value)",
            "--import",
            "re",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0
    assert result.output.strip() == (
        "5th October 2019 12:04\n"
        " --- becomes:\n"
        "5th OXXober 2019 12:04\n"
        "\n"
        "6th October 2019 00:05:06\n"
        " --- becomes:\n"
        "6th OXXober 2019 00:05:06\n"
        "\n"
        "\n"
        " --- becomes:\n"
        "\n"
        "\n"
        "None\n"
        " --- becomes:\n"
        "None\n\n"
        "Would affect 4 rows"
    )
    # But it should not have actually modified the table data
    assert list(db.table("example").rows) == [
        {"id": 1, "dt": "5th October 2019 12:04"},
        {"id": 2, "dt": "6th October 2019 00:05:06"},
        {"id": 3, "dt": ""},
        {"id": 4, "dt": None},
    ]
    # Test with a where clause too
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
            "dt",
            "return re.sub('O..', 'OXX', value)",
            "--import",
            "re",
            "--dry-run",
            "--where",
            "id = :id",
            "-p",
            "id",
            "4",
        ],
    )
    assert result.exit_code == 0
    assert result.output.strip().split("\n")[-1] == "Would affect 1 row"


def test_convert_dryrun_table_and_column_names_containing_closing_bracket(
    fresh_db_and_path,
):
    db, db_path = fresh_db_and_path
    table_name = "table]name"
    column_name = "column]name"
    db[table_name].insert({column_name: "hello"})

    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            table_name,
            column_name,
            "value.upper()",
            "--dry-run",
        ],
        catch_exceptions=False,
    )

    assert result.exit_code == 0
    assert result.output.strip() == (
        "hello\n --- becomes:\nHELLO\n\nWould affect 1 row"
    )
    assert list(db[table_name].rows) == [{column_name: "hello"}]


def test_convert_multi_dryrun(test_db_and_path):
    db_path = test_db_and_path[1]
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
            "dt",
            "{'foo': 'bar', 'baz': 1}",
            "--dry-run",
            "--multi",
        ],
    )
    assert result.exit_code == 0
    assert result.output.strip() == (
        "5th October 2019 12:04\n"
        " --- becomes:\n"
        '{"foo": "bar", "baz": 1}\n'
        "\n"
        "6th October 2019 00:05:06\n"
        " --- becomes:\n"
        '{"foo": "bar", "baz": 1}\n'
        "\n"
        "\n"
        " --- becomes:\n"
        "\n"
        "\n"
        "None\n"
        " --- becomes:\n"
        "None\n"
        "\n"
        "Would affect 4 rows"
    )


def test_convert_multi_dryrun_unicode_not_escaped(test_db_and_path):
    db_path = test_db_and_path[1]
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
            "dt",
            "{'text': 'Japanese 日本語'}",
            "--dry-run",
            "--multi",
        ],
    )
    assert result.exit_code == 0
    # Preview should match what jsonify_if_needed() would actually store
    assert '{"text": "Japanese 日本語"}' in result.output


@pytest.mark.parametrize("drop", (True, False))
def test_convert_output_column(test_db_and_path, drop):
    db, db_path = test_db_and_path
    args = [
        "convert",
        db_path,
        "example",
        "dt",
        "value.replace('October', 'Spooktober') if value else value",
        "--output",
        "newcol",
    ]
    if drop:
        args += ["--drop"]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 0, result.output
    expected = [
        {
            "id": 1,
            "dt": "5th October 2019 12:04",
            "newcol": "5th Spooktober 2019 12:04",
        },
        {
            "id": 2,
            "dt": "6th October 2019 00:05:06",
            "newcol": "6th Spooktober 2019 00:05:06",
        },
        {"id": 3, "dt": "", "newcol": ""},
        {"id": 4, "dt": None, "newcol": None},
    ]
    if drop:
        for row in expected:
            del row["dt"]
    assert list(db.table("example").rows) == expected


@pytest.mark.parametrize(
    "output_type,expected",
    (
        ("text", [(1, "1"), (2, "2"), (3, "3"), (4, "4")]),
        ("float", [(1, 1.0), (2, 2.0), (3, 3.0), (4, 4.0)]),
        ("integer", [(1, 1), (2, 2), (3, 3), (4, 4)]),
        (None, [(1, "1"), (2, "2"), (3, "3"), (4, "4")]),
    ),
)
def test_convert_output_column_output_type(test_db_and_path, output_type, expected):
    db, db_path = test_db_and_path
    args = [
        "convert",
        db_path,
        "example",
        "id",
        "value",
        "--output",
        "new_id",
    ]
    if output_type:
        args += ["--output-type", output_type]
    result = CliRunner().invoke(
        cli.cli,
        args,
    )
    assert result.exit_code == 0, result.output
    assert expected == list(db.execute("select id, new_id from example"))


@pytest.mark.parametrize(
    "options,expected_error",
    [
        (
            [
                "dt",
                "id",
                "value.replace('October', 'Spooktober')",
                "--output",
                "newcol",
            ],
            "Cannot use --output with more than one column",
        ),
        (
            [
                "dt",
                "value.replace('October', 'Spooktober')",
                "--output",
                "newcol",
                "--output-type",
                "invalid",
            ],
            "Error: Invalid value for '--output-type'",
        ),
        (
            [
                "value.replace('October', 'Spooktober')",
            ],
            "Missing argument 'COLUMNS...'",
        ),
    ],
)
def test_convert_output_error(test_db_and_path, options, expected_error):
    db_path = test_db_and_path[1]
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
        ]
        + options,
    )
    assert result.exit_code != 0
    assert expected_error in result.output


@pytest.mark.parametrize("drop", (True, False))
def test_convert_multi(fresh_db_and_path, drop):
    db, db_path = fresh_db_and_path
    db.table("creatures").insert_all(
        [
            {"id": 1, "name": "Simon"},
            {"id": 2, "name": "Cleo"},
        ],
        pk="id",
    )
    args = [
        "convert",
        db_path,
        "creatures",
        "name",
        "--multi",
        '{"upper": value.upper(), "lower": value.lower()}',
    ]
    if drop:
        args += ["--drop"]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 0, result.output
    expected = [
        {"id": 1, "name": "Simon", "upper": "SIMON", "lower": "simon"},
        {"id": 2, "name": "Cleo", "upper": "CLEO", "lower": "cleo"},
    ]
    if drop:
        for row in expected:
            del row["name"]
    assert list(db.table("creatures").rows) == expected


def test_convert_multi_complex_column_types(fresh_db_and_path):
    db, db_path = fresh_db_and_path
    db.table("rows").insert_all(
        [
            {"id": 1},
            {"id": 2},
            {"id": 3},
            {"id": 4},
        ],
        pk="id",
    )
    code = textwrap.dedent("""
    if value == 1:
        return {"is_str": "", "is_float": 1.2, "is_int": None}
    elif value == 2:
        return {"is_float": 1, "is_int": 12}
    elif value == 3:
        return {"is_bytes": b"blah"}
    """)
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "rows",
            "id",
            "--multi",
            code,
        ],
    )
    assert result.exit_code == 0, result.output
    assert list(db.table("rows").rows) == [
        {"id": 1, "is_str": "", "is_float": 1.2, "is_int": None, "is_bytes": None},
        {"id": 2, "is_str": None, "is_float": 1.0, "is_int": 12, "is_bytes": None},
        {
            "id": 3,
            "is_str": None,
            "is_float": None,
            "is_int": None,
            "is_bytes": b"blah",
        },
        {"id": 4, "is_str": None, "is_float": None, "is_int": None, "is_bytes": None},
    ]
    assert db.table("rows").schema == (
        'CREATE TABLE "rows" (\n'
        '   "id" INTEGER PRIMARY KEY\n'
        ', "is_str" TEXT, "is_float" REAL, "is_int" INTEGER, "is_bytes" BLOB)'
    )


@pytest.mark.parametrize("delimiter", [None, ";", "-"])
def test_recipe_jsonsplit(tmpdir, delimiter):
    db_path = str(pathlib.Path(tmpdir) / "data.db")
    db = sqlite_utils.Database(db_path)
    db.table("example").insert_all(
        [
            {"id": 1, "tags": (delimiter or ",").join(["foo", "bar"])},
            {"id": 2, "tags": (delimiter or ",").join(["bar", "baz"])},
        ],
        pk="id",
    )
    code = "r.jsonsplit(value)"
    if delimiter:
        code = f'recipes.jsonsplit(value, delimiter="{delimiter}")'
    args = ["convert", db_path, "example", "tags", code]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 0, result.output
    assert list(db.table("example").rows) == [
        {"id": 1, "tags": '["foo", "bar"]'},
        {"id": 2, "tags": '["bar", "baz"]'},
    ]


@pytest.mark.parametrize(
    "type,expected_array",
    (
        (None, ["1", "2", "3"]),
        ("float", [1.0, 2.0, 3.0]),
        ("int", [1, 2, 3]),
    ),
)
def test_recipe_jsonsplit_type(fresh_db_and_path, type, expected_array):
    db, db_path = fresh_db_and_path
    db.table("example").insert_all(
        [
            {"id": 1, "records": "1,2,3"},
        ],
        pk="id",
    )
    code = "r.jsonsplit(value)"
    if type:
        code = f"recipes.jsonsplit(value, type={type})"
    args = ["convert", db_path, "example", "records", code]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 0, result.output
    assert json.loads(db.table("example").get(1)["records"]) == expected_array


@pytest.mark.parametrize("drop", (True, False))
def test_recipe_jsonsplit_output(fresh_db_and_path, drop):
    db, db_path = fresh_db_and_path
    db.table("example").insert_all(
        [
            {"id": 1, "records": "1,2,3"},
        ],
        pk="id",
    )
    code = "r.jsonsplit(value)"
    args = ["convert", db_path, "example", "records", code, "--output", "tags"]
    if drop:
        args += ["--drop"]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 0, result.output
    expected = {
        "id": 1,
        "records": "1,2,3",
        "tags": '["1", "2", "3"]',
    }
    if drop:
        del expected["records"]
    assert db.table("example").get(1) == expected


def test_cannot_use_drop_without_multi_or_output(fresh_db_and_path):
    args = ["convert", fresh_db_and_path[1], "example", "records", "value", "--drop"]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 1, result.output
    assert "Error: --drop can only be used with --output or --multi" in result.output


def test_cannot_use_multi_with_more_than_one_column(fresh_db_and_path):
    args = [
        "convert",
        fresh_db_and_path[1],
        "example",
        "records",
        "othercol",
        "value",
        "--multi",
    ]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 1, result.output
    assert "Error: Cannot use --multi with more than one column" in result.output


def test_multi_with_bad_function(test_db_and_path):
    args = [
        "convert",
        test_db_and_path[1],
        "example",
        "dt",
        "value.upper()",
        "--multi",
    ]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 1, result.output
    assert "When using --multi code must return a Python dictionary" in result.output


def test_convert_where(test_db_and_path):
    db, db_path = test_db_and_path
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
            "dt",
            "str(value).upper()",
            "--where",
            "id = :id",
            "-p",
            "id",
            "2",
        ],
    )
    assert result.exit_code == 0, result.output
    assert list(db.table("example").rows) == [
        {"id": 1, "dt": "5th October 2019 12:04"},
        {"id": 2, "dt": "6TH OCTOBER 2019 00:05:06"},
        {"id": 3, "dt": ""},
        {"id": 4, "dt": None},
    ]


def test_convert_where_multi(fresh_db_and_path):
    db, db_path = fresh_db_and_path
    db.table("names").insert_all(
        [{"id": 1, "name": "Cleo"}, {"id": 2, "name": "Bants"}], pk="id"
    )
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "names",
            "name",
            '{"upper": value.upper()}',
            "--where",
            "id = :id",
            "-p",
            "id",
            "2",
            "--multi",
        ],
    )
    assert result.exit_code == 0, result.output
    assert list(db.table("names").rows) == [
        {"id": 1, "name": "Cleo", "upper": None},
        {"id": 2, "name": "Bants", "upper": "BANTS"},
    ]


def test_convert_code_standard_input(fresh_db_and_path):
    db, db_path = fresh_db_and_path
    db.table("names").insert_all([{"id": 1, "name": "Cleo"}], pk="id")
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "names",
            "name",
            "-",
        ],
        input="value.upper()",
    )
    assert result.exit_code == 0, result.output
    assert list(db.table("names").rows) == [
        {"id": 1, "name": "CLEO"},
    ]


def test_convert_hyphen_workaround(fresh_db_and_path):
    db, db_path = fresh_db_and_path
    db.table("names").insert_all([{"id": 1, "name": "Cleo"}], pk="id")
    result = CliRunner().invoke(
        cli.cli,
        ["convert", db_path, "names", "name", '"-"'],
    )
    assert result.exit_code == 0, result.output
    assert list(db.table("names").rows) == [
        {"id": 1, "name": "-"},
    ]


def test_convert_initialization_pattern(fresh_db_and_path):
    db, db_path = fresh_db_and_path
    db.table("names").insert_all([{"id": 1, "name": "Cleo"}], pk="id")
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "names",
            "name",
            "-",
        ],
        input="import random\nrandom.seed(1)\ndef convert(value):    return random.randint(0, 100)",
    )
    assert result.exit_code == 0, result.output
    assert list(db.table("names").rows) == [
        {"id": 1, "name": "17"},
    ]


def test_convert_handles_falsey_values(fresh_db_and_path):
    # Falsey values like 0 should be converted (issue #527)
    db, db_path = fresh_db_and_path
    args = [
        "convert",
        db_path,
        "t",
        "x",
        "-",
    ]
    db.table("t").insert_all([{"x": 0}, {"x": 1}])
    assert db.table("t").get(1)["x"] == 0
    assert db.table("t").get(2)["x"] == 1
    result = CliRunner().invoke(cli.cli, args, input="value + 1")
    assert result.exit_code == 0, result.output
    assert db.table("t").get(1)["x"] == 1
    assert db.table("t").get(2)["x"] == 2


@pytest.mark.parametrize(
    "code",
    [
        # Direct callable reference (issue #686)
        "r.parsedate",
        "recipes.parsedate",
        # Traditional call syntax still works
        "r.parsedate(value)",
        "recipes.parsedate(value)",
    ],
)
def test_convert_callable_reference(test_db_and_path, code):
    """Test that callable references like r.parsedate work without (value)"""
    db, db_path = test_db_and_path
    result = CliRunner().invoke(
        cli.cli, ["convert", db_path, "example", "dt", code], catch_exceptions=False
    )
    assert result.exit_code == 0, result.output
    rows = list(db.table("example").rows)
    assert rows[0]["dt"] == "2019-10-05"
    assert rows[1]["dt"] == "2019-10-06"
    assert rows[2]["dt"] == ""
    assert rows[3]["dt"] is None


def test_convert_callable_reference_with_import(fresh_db_and_path):
    """Test callable reference from an imported module"""
    db, db_path = fresh_db_and_path
    db.table("example").insert({"id": 1, "data": '{"name": "test"}'})
    result = CliRunner().invoke(
        cli.cli,
        [
            "convert",
            db_path,
            "example",
            "data",
            "json.loads",
            "--import",
            "json",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    # json.loads returns a dict, which sqlite stores as JSON string
    row = db.table("example").get(1)
    assert row["data"] == '{"name": "test"}'

```

### `tests/test_cli_insert.py`

```py
import json
import subprocess
import sys
import time

import pytest
from click.testing import CliRunner

from sqlite_utils import Database, cli


def test_insert_simple(tmpdir):
    json_path = str(tmpdir / "dog.json")
    db_path = str(tmpdir / "dogs.db")
    with open(json_path, "w") as fp:
        fp.write(json.dumps({"name": "Cleo", "age": 4}))
    result = CliRunner().invoke(cli.cli, ["insert", db_path, "dogs", json_path])
    assert result.exit_code == 0
    assert [{"age": 4, "name": "Cleo"}] == list(
        Database(db_path).query("select * from dogs")
    )
    db = Database(db_path)
    assert ["dogs"] == db.table_names()
    assert [] == db.table("dogs").indexes


def test_insert_from_stdin(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "dogs", "-"],
        input=json.dumps({"name": "Cleo", "age": 4}),
    )
    assert result.exit_code == 0
    assert [{"age": 4, "name": "Cleo"}] == list(
        Database(db_path).query("select * from dogs")
    )


def test_insert_invalid_json_error(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "dogs", "-"],
        input="name,age\nCleo,4",
    )
    assert result.exit_code == 1
    assert result.output == (
        "Error: Invalid JSON - use --csv for CSV or --tsv for TSV files\n\n"
        "JSON error: Expecting value: line 1 column 1 (char 0)\n"
    )


def test_insert_json_flatten(tmpdir):
    db_path = str(tmpdir / "flat.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "items", "-", "--flatten"],
        input=json.dumps({"nested": {"data": 4}}),
    )
    assert result.exit_code == 0
    assert list(Database(db_path).query("select * from items")) == [{"nested_data": 4}]


def test_insert_json_flatten_nl(tmpdir):
    db_path = str(tmpdir / "flat.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "items", "-", "--flatten", "--nl"],
        input="\n".join(
            json.dumps(item)
            for item in [{"nested": {"data": 4}}, {"nested": {"other": 3}}]
        ),
    )
    assert result.exit_code == 0
    assert list(Database(db_path).query("select * from items")) == [
        {"nested_data": 4, "nested_other": None},
        {"nested_data": None, "nested_other": 3},
    ]


@pytest.mark.parametrize(
    "args,expected_pks",
    (
        (["--pk", "id"], ["id"]),
        (["--pk", "id", "--pk", "name"], ["id", "name"]),
    ),
)
def test_insert_with_primary_keys(db_path, tmpdir, args, expected_pks):
    json_path = str(tmpdir / "dog.json")
    with open(json_path, "w") as fp:
        fp.write(json.dumps({"id": 1, "name": "Cleo", "age": 4}))
    result = CliRunner().invoke(cli.cli, ["insert", db_path, "dogs", json_path] + args)
    assert result.exit_code == 0
    assert [{"id": 1, "age": 4, "name": "Cleo"}] == list(
        Database(db_path).query("select * from dogs")
    )
    db = Database(db_path)
    assert db.table("dogs").pks == expected_pks


def test_insert_multiple_with_primary_key(db_path, tmpdir):
    json_path = str(tmpdir / "dogs.json")
    dogs = [{"id": i, "name": f"Cleo {i}", "age": i + 3} for i in range(1, 21)]
    with open(json_path, "w") as fp:
        fp.write(json.dumps(dogs))
    result = CliRunner().invoke(
        cli.cli, ["insert", db_path, "dogs", json_path, "--pk", "id"]
    )
    assert result.exit_code == 0
    db = Database(db_path)
    assert dogs == list(db.query("select * from dogs order by id"))
    assert ["id"] == db.table("dogs").pks


def test_insert_multiple_with_compound_primary_key(db_path, tmpdir):
    json_path = str(tmpdir / "dogs.json")
    dogs = [
        {"breed": "mixed", "id": i, "name": f"Cleo {i}", "age": i + 3}
        for i in range(1, 21)
    ]
    with open(json_path, "w") as fp:
        fp.write(json.dumps(dogs))
    result = CliRunner().invoke(
        cli.cli, ["insert", db_path, "dogs", json_path, "--pk", "id", "--pk", "breed"]
    )
    assert result.exit_code == 0
    db = Database(db_path)
    assert dogs == list(db.query("select * from dogs order by breed, id"))
    assert {"breed", "id"} == set(db.table("dogs").pks)
    assert (
        'CREATE TABLE "dogs" (\n'
        '   "breed" TEXT,\n'
        '   "id" INTEGER,\n'
        '   "name" TEXT,\n'
        '   "age" INTEGER,\n'
        '   PRIMARY KEY ("id", "breed")\n'
        ")"
    ) == db.table("dogs").schema


def test_insert_not_null_default(db_path, tmpdir):
    json_path = str(tmpdir / "dogs.json")
    dogs = [
        {"id": i, "name": f"Cleo {i}", "age": i + 3, "score": 10} for i in range(1, 21)
    ]
    with open(json_path, "w") as fp:
        fp.write(json.dumps(dogs))
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "dogs", json_path, "--pk", "id"]
        + ["--not-null", "name", "--not-null", "age"]
        + ["--default", "score", "5", "--default", "age", "1"],
    )
    assert result.exit_code == 0
    db = Database(db_path)
    assert (
        'CREATE TABLE "dogs" (\n'
        '   "id" INTEGER PRIMARY KEY,\n'
        '   "name" TEXT NOT NULL,\n'
        "   \"age\" INTEGER NOT NULL DEFAULT '1',\n"
        "   \"score\" INTEGER DEFAULT '5'\n)"
    ) == db.table("dogs").schema


def test_insert_binary_base64(db_path):
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "files", "-"],
        input=r'{"content": {"$base64": true, "encoded": "aGVsbG8="}}',
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    actual = list(db.query("select content from files"))
    assert actual == [{"content": b"hello"}]


def test_insert_newline_delimited(db_path):
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "from_json_nl", "-", "--nl"],
        input='{"foo": "bar", "n": 1}\n\n{"foo": "baz", "n": 2}',
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    assert [
        {"foo": "bar", "n": 1},
        {"foo": "baz", "n": 2},
    ] == list(db.query("select foo, n from from_json_nl"))


def test_insert_ignore(db_path, tmpdir):
    db = Database(db_path)
    db.table("dogs").insert({"id": 1, "name": "Cleo"}, pk="id")
    json_path = str(tmpdir / "dogs.json")
    with open(json_path, "w") as fp:
        fp.write(json.dumps([{"id": 1, "name": "Bailey"}]))
    # Should raise error without --ignore
    result = CliRunner().invoke(
        cli.cli, ["insert", db_path, "dogs", json_path, "--pk", "id"]
    )
    assert result.exit_code != 0, result.output
    # If we use --ignore it should run OK
    result = CliRunner().invoke(
        cli.cli, ["insert", db_path, "dogs", json_path, "--pk", "id", "--ignore"]
    )
    assert result.exit_code == 0, result.output
    # ... but it should actually have no effect
    assert [{"id": 1, "name": "Cleo"}] == list(db.query("select * from dogs"))


@pytest.mark.parametrize(
    "content,options",
    [
        ("foo\tbar\tbaz\n1\t2\tcat,dog", ["--tsv"]),
        ('foo,bar,baz\n1,2,"cat,dog"', ["--csv"]),
        ('foo;bar;baz\n1;2;"cat,dog"', ["--csv", "--delimiter", ";"]),
        # --delimiter implies --csv:
        ('foo;bar;baz\n1;2;"cat,dog"', ["--delimiter", ";"]),
        ("foo,bar,baz\n1,2,|cat,dog|", ["--csv", "--quotechar", "|"]),
        ("foo,bar,baz\n1,2,|cat,dog|", ["--quotechar", "|"]),
    ],
)
def test_insert_csv_tsv(content, options, db_path, tmpdir):
    db = Database(db_path)
    file_path = str(tmpdir / "insert.csv-tsv")
    with open(file_path, "w") as fp:
        fp.write(content)
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "data", file_path] + options + ["--no-detect-types"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert [{"foo": "1", "bar": "2", "baz": "cat,dog"}] == list(db.table("data").rows)


@pytest.mark.parametrize("empty_null", (True, False))
def test_insert_csv_empty_null(db_path, empty_null):
    options = ["--csv", "--no-detect-types"]
    if empty_null:
        options.append("--empty-null")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "data", "-"] + options,
        catch_exceptions=False,
        input="foo,bar,baz\n1,,cat,dog",
    )
    assert result.exit_code == 0
    db = Database(db_path)
    assert [r for r in db.table("data").rows] == [
        {"foo": "1", "bar": None if empty_null else "", "baz": "cat"}
    ]


@pytest.mark.parametrize(
    "input,args",
    (
        (
            json.dumps(
                [{"name": "One"}, {"name": "Two"}, {"name": "Three"}, {"name": "Four"}]
            ),
            [],
        ),
        ("name\nOne\nTwo\nThree\nFour\n", ["--csv"]),
    ),
)
def test_insert_stop_after(tmpdir, input, args):
    db_path = str(tmpdir / "data.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "rows", "-", "--stop-after", "2"] + args,
        input=input,
    )
    assert result.exit_code == 0
    assert [{"name": "One"}, {"name": "Two"}] == list(
        Database(db_path).query("select * from rows")
    )


@pytest.mark.parametrize(
    "options",
    (
        ["--tsv", "--nl"],
        ["--tsv", "--csv"],
        ["--csv", "--nl"],
        ["--csv", "--nl", "--tsv"],
    ),
)
def test_only_allow_one_of_nl_tsv_csv(options, db_path, tmpdir):
    file_path = str(tmpdir / "insert.csv-tsv")
    with open(file_path, "w") as fp:
        fp.write("foo")
    result = CliRunner().invoke(
        cli.cli, ["insert", db_path, "data", file_path] + options
    )
    assert result.exit_code != 0
    assert "Error: Use just one of --nl, --csv or --tsv" == result.output.strip()


def test_insert_replace(db_path, tmpdir):
    test_insert_multiple_with_primary_key(db_path, tmpdir)
    json_path = str(tmpdir / "insert-replace.json")
    db = Database(db_path)
    assert db.table("dogs").count == 20
    insert_replace_dogs = [
        {"id": 1, "name": "Insert replaced 1", "age": 4},
        {"id": 2, "name": "Insert replaced 2", "age": 4},
        {"id": 21, "name": "Fresh insert 21", "age": 6},
    ]
    with open(json_path, "w") as fp:
        fp.write(json.dumps(insert_replace_dogs))
    result = CliRunner().invoke(
        cli.cli, ["insert", db_path, "dogs", json_path, "--pk", "id", "--replace"]
    )
    assert result.exit_code == 0, result.output
    assert db.table("dogs").count == 21
    assert (
        list(db.query("select * from dogs where id in (1, 2, 21) order by id"))
        == insert_replace_dogs
    )


def test_insert_truncate(db_path):
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "from_json_nl", "-", "--nl", "--batch-size=1"],
        input='{"foo": "bar", "n": 1}\n{"foo": "baz", "n": 2}',
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    assert [
        {"foo": "bar", "n": 1},
        {"foo": "baz", "n": 2},
    ] == list(db.query("select foo, n from from_json_nl"))
    # Truncate and insert new rows
    result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "from_json_nl",
            "-",
            "--nl",
            "--truncate",
            "--batch-size=1",
        ],
        input='{"foo": "bam", "n": 3}\n{"foo": "bat", "n": 4}',
    )
    assert result.exit_code == 0, result.output
    assert [
        {"foo": "bam", "n": 3},
        {"foo": "bat", "n": 4},
    ] == list(db.query("select foo, n from from_json_nl"))


def test_insert_alter(db_path, tmpdir):
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "from_json_nl", "-", "--nl"],
        input='{"foo": "bar", "n": 1}\n{"foo": "baz", "n": 2}',
    )
    assert result.exit_code == 0, result.output
    # Should get an error with incorrect shaped additional data
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "from_json_nl", "-", "--nl"],
        input='{"foo": "bar", "baz": 5}',
    )
    assert result.exit_code != 0, result.output
    # If we run it again with --alter it should work correctly
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "from_json_nl", "-", "--nl", "--alter"],
        input='{"foo": "bar", "baz": 5}',
    )
    assert result.exit_code == 0, result.output
    # Soundness check the database itself
    db = Database(db_path)
    assert {"foo": str, "n": int, "baz": int} == db.table("from_json_nl").columns_dict
    assert [
        {"foo": "bar", "n": 1, "baz": None},
        {"foo": "baz", "n": 2, "baz": None},
        {"foo": "bar", "baz": 5, "n": None},
    ] == list(db.query("select foo, n, baz from from_json_nl"))


def test_insert_analyze(db_path):
    db = Database(db_path)
    db.table("rows").insert({"foo": "x", "n": 3})
    db.table("rows").create_index(["n"])
    assert "sqlite_stat1" not in db.table_names()
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "rows", "-", "--nl", "--analyze"],
        input='{"foo": "bar", "n": 1}\n{"foo": "baz", "n": 2}',
    )
    assert result.exit_code == 0, result.output
    assert "sqlite_stat1" in db.table_names()


def test_insert_lines(db_path):
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "from_lines", "-", "--lines"],
        input='First line\nSecond line\n{"foo": "baz"}',
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    assert [
        {"line": "First line"},
        {"line": "Second line"},
        {"line": '{"foo": "baz"}'},
    ] == list(db.query("select line from from_lines"))


def test_insert_text(db_path):
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "from_text", "-", "--text"],
        input='First line\nSecond line\n{"foo": "baz"}',
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    assert [{"text": 'First line\nSecond line\n{"foo": "baz"}'}] == list(
        db.query("select text from from_text")
    )


@pytest.mark.parametrize(
    "options,input",
    (
        ([], '[{"id": "1", "name": "Bob"}, {"id": "2", "name": "Cat"}]'),
        (["--csv", "--no-detect-types"], "id,name\n1,Bob\n2,Cat"),
        (["--nl"], '{"id": "1", "name": "Bob"}\n{"id": "2", "name": "Cat"}'),
    ),
)
def test_insert_convert_json_csv_jsonnl(db_path, options, input):
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "rows", "-", "--convert", '{**row, **{"extra": 1}}']
        + options,
        input=input,
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    rows = list(db.query("select id, name, extra from rows"))
    assert rows == [
        {"id": "1", "name": "Bob", "extra": 1},
        {"id": "2", "name": "Cat", "extra": 1},
    ]


def test_insert_convert_text(db_path):
    result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "text",
            "-",
            "--text",
            "--convert",
            '{"text": text.upper()}',
        ],
        input="This is text\nwill be upper now",
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    rows = list(db.query('select "text" from "text"'))
    assert rows == [{"text": "THIS IS TEXT\nWILL BE UPPER NOW"}]


def test_insert_convert_text_returning_iterator(db_path):
    result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "text",
            "-",
            "--text",
            "--convert",
            '({"word": w} for w in text.split())',
        ],
        input="A bunch of words",
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    rows = list(db.query('select "word" from "text"'))
    assert rows == [{"word": "A"}, {"word": "bunch"}, {"word": "of"}, {"word": "words"}]


def test_insert_convert_lines(db_path):
    result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "all",
            "-",
            "--lines",
            "--convert",
            '{"line": line.upper()}',
        ],
        input="This is text\nwill be upper now",
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    rows = list(db.query('select "line" from "all"'))
    assert rows == [{"line": "THIS IS TEXT"}, {"line": "WILL BE UPPER NOW"}]


def test_insert_convert_row_modifying_in_place(db_path):
    result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "rows",
            "-",
            "--convert",
            'row["is_chicken"] = True',
        ],
        input='{"name": "Azi"}',
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    rows = list(db.query("select name, is_chicken from rows"))
    assert rows == [{"name": "Azi", "is_chicken": 1}]


@pytest.mark.parametrize(
    "options,expected_error",
    (
        (
            ["--text", "--convert", "1"],
            "Error: --convert must return dict or iterator\n",
        ),
        (["--convert", "1"], "Error: Rows must all be dictionaries, got: 1\n"),
    ),
)
def test_insert_convert_error_messages(db_path, options, expected_error):
    result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "rows",
            "-",
        ]
        + options,
        input='{"name": "Azi"}',
    )
    assert result.exit_code == 1
    assert result.output == expected_error


def test_insert_streaming_batch_size_1(db_path):
    # https://github.com/simonw/sqlite-utils/issues/364
    # Streaming with --batch-size 1 should commit on each record
    # Can't use CliRunner().invoke() here bacuse we need to
    # run assertions in between writing to process stdin
    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "sqlite_utils",
            "insert",
            db_path,
            "rows",
            "-",
            "--nl",
            "--batch-size",
            "1",
        ],
        stdin=subprocess.PIPE,
        stdout=sys.stdout,
    )
    assert proc.stdin is not None
    proc.stdin.write(b'{"name": "Azi"}\n')
    proc.stdin.flush()

    def try_until(expected):
        tries = 0
        while True:
            rows = list(Database(db_path).table("rows").rows)
            if rows == expected:
                return
            tries += 1
            if tries > 10:
                assert False, f"Expected {expected}, got {rows}"
            time.sleep(tries * 0.1)

    try_until([{"name": "Azi"}])
    proc.stdin.write(b'{"name": "Suna"}\n')
    proc.stdin.flush()
    try_until([{"name": "Azi"}, {"name": "Suna"}])
    proc.stdin.close()
    proc.wait()
    assert proc.returncode == 0


def test_insert_csv_headers_only(tmpdir):
    """Test that CSV with only header row (no data) works with --detect-types (issue #702)"""
    db_path = str(tmpdir / "test.db")
    csv_path = str(tmpdir / "headers_only.csv")
    with open(csv_path, "w") as fp:
        fp.write("id,name,age\n")
    # Should not crash with --detect-types (which is now the default)
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "data", csv_path, "--csv"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    # Table should not exist since there were no data rows
    db = Database(db_path)
    assert not db.table("data").exists()


def test_insert_into_view_errors(tmpdir):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("t").insert({"id": 1})
    db.create_view("v", "select * from t")
    db.close()
    result = CliRunner().invoke(
        cli.cli, ["insert", db_path, "v", "-"], input='{"id": 2}'
    )
    assert result.exit_code == 1
    assert result.output.strip() == "Error: Table v is actually a view"


def test_insert_csv_detect_types_leaves_existing_table_alone(db_path):
    # Type detection is the default for CSV/TSV inserts, but it must only
    # apply to tables created by this command - transforming a pre-existing
    # table would rewrite its column types and corrupt data such as
    # TEXT zip codes with leading zeros
    db = Database(db_path)
    db.table("places").insert({"name": "Boston", "zip": "01234"})
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "places", "-", "--csv"],
        catch_exceptions=False,
        input="name,zip\nSF,94107",
    )
    assert result.exit_code == 0, result.output
    assert db.table("places").columns_dict["zip"] is str
    assert list(db.table("places").rows) == [
        {"name": "Boston", "zip": "01234"},
        {"name": "SF", "zip": "94107"},
    ]


def test_insert_csv_detect_types_new_table(db_path):
    # A table created by the insert still gets detected types
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "data", "-", "--csv"],
        catch_exceptions=False,
        input="name,age,weight\nCleo,5,12.5",
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    assert db.table("data").columns_dict == {"name": str, "age": int, "weight": float}


@pytest.mark.parametrize(
    "command,extra_args,input_text,expected_row",
    (
        (
            "insert",
            [],
            "zipcode,score\n01234,9.5\n",
            {"zipcode": "01234", "score": 9.5},
        ),
        (
            "upsert",
            ["--pk", "id"],
            "id,zipcode,score\n1,01234,9.5\n",
            {"id": 1, "zipcode": "01234", "score": 9.5},
        ),
    ),
)
def test_insert_upsert_csv_type_overrides_detected_types(
    db_path, command, extra_args, input_text, expected_row
):
    result = CliRunner().invoke(
        cli.cli,
        [
            command,
            db_path,
            "places",
            "-",
            "--csv",
        ]
        + extra_args
        + [
            "--type",
            "zipcode",
            "text",
        ],
        catch_exceptions=False,
        input=input_text,
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    expected_columns = {"zipcode": str, "score": float}
    if command == "upsert":
        expected_columns = {"id": int, **expected_columns}
    assert db.table("places").columns_dict == expected_columns
    assert list(db.table("places").rows) == [expected_row]


def test_upsert_csv_detect_types_leaves_existing_table_alone(db_path):
    db = Database(db_path)
    db.table("places").insert({"id": 1, "name": "Boston", "zip": "01234"}, pk="id")
    result = CliRunner().invoke(
        cli.cli,
        ["upsert", db_path, "places", "-", "--csv", "--pk", "id"],
        catch_exceptions=False,
        input="id,name,zip\n2,SF,94107",
    )
    assert result.exit_code == 0, result.output
    assert db.table("places").columns_dict["zip"] is str
    assert db.table("places").get(1)["zip"] == "01234"


def test_insert_invalid_pk_clean_error(db_path):
    # An invalid --pk against an existing table should be a clean CLI
    # error, not a raw InvalidColumns traceback
    db = Database(db_path)
    db.table("t").insert({"a": 1})
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "t", "-", "--pk", "badcol"],
        input='{"a": 2}',
    )
    assert result.exit_code == 1
    assert result.exception is None or isinstance(result.exception, SystemExit)
    assert result.output.startswith("Error: Invalid primary key column")


# --code tests, see https://github.com/simonw/sqlite-utils/issues/684
CODE_ROWS_FUNCTION = """
def rows():
    yield {"id": 1, "name": "Cleo"}
    yield {"id": 2, "name": "Suna"}
"""

CODE_ROWS_ITERABLE = """
rows = [
    {"id": 1, "name": "Cleo"},
    {"id": 2, "name": "Suna"},
]
"""


@pytest.mark.parametrize("code", (CODE_ROWS_FUNCTION, CODE_ROWS_ITERABLE))
def test_insert_code(tmpdir, code):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "--code", code, "--pk", "id"],
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    assert db.table("creatures").pks == ["id"]
    assert list(db.table("creatures").rows) == [
        {"id": 1, "name": "Cleo"},
        {"id": 2, "name": "Suna"},
    ]


def test_insert_code_from_file(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    code_path = str(tmpdir / "gen.py")
    with open(code_path, "w") as fp:
        fp.write(CODE_ROWS_FUNCTION)
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "--code", code_path],
    )
    assert result.exit_code == 0, result.output
    assert list(Database(db_path).table("creatures").rows) == [
        {"id": 1, "name": "Cleo"},
        {"id": 2, "name": "Suna"},
    ]


def test_upsert_code(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    db = Database(db_path)
    db.table("creatures").insert_all(
        [{"id": 1, "name": "old"}, {"id": 2, "name": "Suna"}], pk="id"
    )
    result = CliRunner().invoke(
        cli.cli,
        ["upsert", db_path, "creatures", "--code", CODE_ROWS_FUNCTION, "--pk", "id"],
    )
    assert result.exit_code == 0, result.output
    assert list(db.table("creatures").rows) == [
        {"id": 1, "name": "Cleo"},
        {"id": 2, "name": "Suna"},
    ]


def test_insert_code_requires_file_or_code(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(cli.cli, ["insert", db_path, "creatures"])
    assert result.exit_code == 1
    assert "Provide either a FILE argument or --code" in result.output


def test_insert_code_mutually_exclusive_with_file(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "-", "--code", CODE_ROWS_FUNCTION],
        input="{}",
    )
    assert result.exit_code == 1
    assert "--code cannot be used with a FILE argument" in result.output


def test_insert_code_rejects_input_format_options(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "--code", CODE_ROWS_FUNCTION, "--csv"],
    )
    assert result.exit_code == 1
    assert "--code cannot be used with input format options" in result.output


def test_insert_code_missing_rows(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "--code", "x = 1"],
    )
    assert result.exit_code == 1
    assert "must define a 'rows' function or iterable" in result.output


def test_insert_code_single_dict(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "creatures",
            "--code",
            'rows = {"id": 1, "name": "Cleo"}',
            "--pk",
            "id",
        ],
    )
    assert result.exit_code == 0, result.output
    assert list(Database(db_path).table("creatures").rows) == [
        {"id": 1, "name": "Cleo"}
    ]


def test_insert_code_not_iterable(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "--code", "rows = 5"],
    )
    assert result.exit_code == 1
    assert "must define a 'rows' function or iterable" in result.output


def test_insert_code_syntax_error(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "--code", "def rows(:"],
    )
    assert result.exit_code == 1
    assert "Error in --code" in result.output


def test_insert_code_file_not_found(tmpdir):
    db_path = str(tmpdir / "dogs.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "--code", "missing.py"],
    )
    assert result.exit_code == 1
    assert "File not found: missing.py" in result.output

```

### `tests/test_cli_memory.py`

```py
import json

import click
import pytest
from click.testing import CliRunner

from sqlite_utils import Database, cli


def test_memory_basic():
    result = CliRunner().invoke(cli.cli, ["memory", "select 1 + 1"])
    assert result.exit_code == 0
    assert result.output.strip() == '[{"1 + 1": 2}]'


@pytest.mark.parametrize("sql_from", ("test", "t", "t1"))
@pytest.mark.parametrize("use_stdin", (True, False))
def test_memory_csv(tmpdir, sql_from, use_stdin):
    content = "id,name\n1,Cleo\n2,Bants"
    input = None
    if use_stdin:
        input = content
        csv_path = "-"
        if sql_from == "test":
            sql_from = "stdin"
    else:
        csv_path = str(tmpdir / "test.csv")
        with open(csv_path, "w") as fp:
            fp.write(content)
    result = CliRunner().invoke(
        cli.cli,
        ["memory", csv_path, f"select * from {sql_from}", "--nl"],
        input=input,
    )
    assert result.exit_code == 0
    assert (
        result.output.strip() == '{"id": 1, "name": "Cleo"}\n{"id": 2, "name": "Bants"}'
    )


@pytest.mark.parametrize("use_stdin", (True, False))
def test_memory_tsv(tmpdir, use_stdin):
    data = "id\tname\n1\tCleo\n2\tBants"
    if use_stdin:
        input = data
        path = "stdin:tsv"
        sql_from = "stdin"
    else:
        input = None
        path = str(tmpdir / "chickens.tsv")
        with open(path, "w") as fp:
            fp.write(data)
        path = path + ":tsv"
        sql_from = "chickens"
    result = CliRunner().invoke(
        cli.cli,
        ["memory", path, f"select * from {sql_from}"],
        input=input,
    )
    assert result.exit_code == 0, result.output
    assert json.loads(result.output.strip()) == [
        {"id": 1, "name": "Cleo"},
        {"id": 2, "name": "Bants"},
    ]


@pytest.mark.parametrize("use_stdin", (True, False))
def test_memory_json(tmpdir, use_stdin):
    data = '[{"name": "Bants"}, {"name": "Dori", "age": 1, "nested": {"nest": 1}}]'
    if use_stdin:
        input = data
        path = "stdin:json"
        sql_from = "stdin"
    else:
        input = None
        path = str(tmpdir / "chickens.json")
        with open(path, "w") as fp:
            fp.write(data)
        path = path + ":json"
        sql_from = "chickens"
    result = CliRunner().invoke(
        cli.cli,
        ["memory", path, f"select * from {sql_from}"],
        input=input,
    )
    assert result.exit_code == 0, result.output
    assert json.loads(result.output.strip()) == [
        {"name": "Bants", "age": None, "nested": None},
        {"name": "Dori", "age": 1, "nested": '{"nest": 1}'},
    ]


@pytest.mark.parametrize("use_stdin", (True, False))
def test_memory_json_nl(tmpdir, use_stdin):
    data = '{"name": "Bants"}\n\n{"name": "Dori"}'
    if use_stdin:
        input = data
        path = "stdin:nl"
        sql_from = "stdin"
    else:
        input = None
        path = str(tmpdir / "chickens.json")
        with open(path, "w") as fp:
            fp.write(data)
        path = path + ":nl"
        sql_from = "chickens"
    result = CliRunner().invoke(
        cli.cli,
        ["memory", path, f"select * from {sql_from}"],
        input=input,
    )
    assert result.exit_code == 0, result.output
    assert json.loads(result.output.strip()) == [
        {"name": "Bants"},
        {"name": "Dori"},
    ]


@pytest.mark.parametrize("use_stdin", (True, False))
def test_memory_csv_encoding(tmpdir, use_stdin):
    latin1_csv = (
        b"date,name,latitude,longitude\n" b"2020-03-04,S\xe3o Paulo,-23.561,-46.645\n"
    )
    input = None
    if use_stdin:
        input = latin1_csv
        csv_path = "-"
        sql_from = "stdin"
    else:
        csv_path = str(tmpdir / "test.csv")
        with open(csv_path, "wb") as fp:
            fp.write(latin1_csv)
        sql_from = "test"
    # Without --encoding should error:
    assert (
        CliRunner()
        .invoke(
            cli.cli,
            ["memory", csv_path, f"select * from {sql_from}", "--nl"],
            input=input,
        )
        .exit_code
        == 1
    )
    # With --encoding should work:
    result = CliRunner().invoke(
        cli.cli,
        ["memory", "-", "select * from stdin", "--encoding", "latin-1", "--nl"],
        input=latin1_csv,
    )
    assert result.exit_code == 0, result.output
    assert json.loads(result.output.strip()) == {
        "date": "2020-03-04",
        "name": "São Paulo",
        "latitude": -23.561,
        "longitude": -46.645,
    }


def test_memory_csv_headers_only(tmpdir):
    csv_path = str(tmpdir / "headers_only.csv")
    with open(csv_path, "w") as fp:
        fp.write("id,name,age\n")

    result = CliRunner().invoke(
        cli.cli,
        ["memory", csv_path, "", "--schema"],
        catch_exceptions=False,
    )

    assert result.exit_code == 0
    assert result.output.strip() == (
        'CREATE VIEW "t1" AS select * from "headers_only";\n'
        'CREATE VIEW "t" AS select * from "headers_only";'
    )


@pytest.mark.parametrize("extra_args", ([], ["select 1"]))
def test_memory_dump(extra_args):
    result = CliRunner().invoke(
        cli.cli,
        ["memory", "-"] + extra_args + ["--dump"],
        input="id,name\n1,Cleo\n2,Bants",
    )
    assert result.exit_code == 0
    expected = (
        "BEGIN TRANSACTION;\n"
        'CREATE TABLE IF NOT EXISTS "stdin" (\n'
        '   "id" INTEGER,\n'
        '   "name" TEXT\n'
        ");\n"
        "INSERT INTO \"stdin\" VALUES(1,'Cleo');\n"
        "INSERT INTO \"stdin\" VALUES(2,'Bants');\n"
        'CREATE VIEW "t1" AS select * from "stdin";\n'
        'CREATE VIEW "t" AS select * from "stdin";\n'
        "COMMIT;"
    )
    # Using sqlite-dump it won't have IF NOT EXISTS
    expected_alternative = expected.replace("IF NOT EXISTS ", "")
    assert result.output.strip() in (expected, expected_alternative)


@pytest.mark.parametrize("extra_args", ([], ["select 1"]))
def test_memory_schema(extra_args):
    result = CliRunner().invoke(
        cli.cli,
        ["memory", "-"] + extra_args + ["--schema"],
        input="id,name\n1,Cleo\n2,Bants",
    )
    assert result.exit_code == 0
    assert result.output.strip() == (
        'CREATE TABLE "stdin" (\n'
        '   "id" INTEGER,\n'
        '   "name" TEXT\n'
        ");\n"
        'CREATE VIEW "t1" AS select * from "stdin";\n'
        'CREATE VIEW "t" AS select * from "stdin";'
    )


@pytest.mark.parametrize("extra_args", ([], ["select 1"]))
def test_memory_save(tmpdir, extra_args):
    save_to = str(tmpdir / "save.db")
    result = CliRunner().invoke(
        cli.cli,
        ["memory", "-"] + extra_args + ["--save", save_to],
        input="id,name\n1,Cleo\n2,Bants",
    )
    assert result.exit_code == 0
    db = Database(save_to)
    assert list(db.table("stdin").rows) == [
        {"id": 1, "name": "Cleo"},
        {"id": 2, "name": "Bants"},
    ]


@pytest.mark.parametrize("option", ("-n", "--no-detect-types"))
def test_memory_no_detect_types(option):
    result = CliRunner().invoke(
        cli.cli,
        ["memory", "-", "select * from stdin"] + [option],
        input="id,name,weight\n1,Cleo,45.5\n2,Bants,3.5",
    )
    assert result.exit_code == 0, result.output
    assert json.loads(result.output.strip()) == [
        {"id": "1", "name": "Cleo", "weight": "45.5"},
        {"id": "2", "name": "Bants", "weight": "3.5"},
    ]


def test_memory_flatten():
    result = CliRunner().invoke(
        cli.cli,
        ["memory", "-", "select * from stdin", "--flatten"],
        input=json.dumps(
            {
                "httpRequest": {
                    "latency": "0.112114537s",
                    "requestMethod": "GET",
                },
                "insertId": "6111722f000b5b4c4d4071e2",
            }
        ),
    )
    assert result.exit_code == 0, result.output
    assert json.loads(result.output.strip()) == [
        {
            "httpRequest_latency": "0.112114537s",
            "httpRequest_requestMethod": "GET",
            "insertId": "6111722f000b5b4c4d4071e2",
        }
    ]


def test_memory_analyze():
    result = CliRunner().invoke(
        cli.cli,
        ["memory", "-", "--analyze"],
        input="id,name\n1,Cleo\n2,Bants",
    )
    assert result.exit_code == 0
    assert result.output == (
        "stdin.id: (1/2)\n\n"
        "  Total rows: 2\n"
        "  Null rows: 0\n"
        "  Blank rows: 0\n\n"
        "  Distinct values: 2\n\n"
        "stdin.name: (2/2)\n\n"
        "  Total rows: 2\n"
        "  Null rows: 0\n"
        "  Blank rows: 0\n\n"
        "  Distinct values: 2\n\n"
    )


def test_memory_two_files_with_same_stem(tmpdir):
    (tmpdir / "one").mkdir()
    (tmpdir / "two").mkdir()
    one = tmpdir / "one" / "data.csv"
    two = tmpdir / "two" / "data.csv"
    one.write_text("id,name\n1,Cleo\n2,Bants", encoding="utf-8")
    two.write_text("id,name\n3,Blue\n4,Lila", encoding="utf-8")
    result = CliRunner().invoke(cli.cli, ["memory", str(one), str(two), "", "--schema"])
    assert result.exit_code == 0
    assert result.output == (
        'CREATE TABLE "data" (\n'
        '   "id" INTEGER,\n'
        '   "name" TEXT\n'
        ");\n"
        'CREATE VIEW "t1" AS select * from "data";\n'
        'CREATE VIEW "t" AS select * from "data";\n'
        'CREATE TABLE "data_2" (\n'
        '   "id" INTEGER,\n'
        '   "name" TEXT\n'
        ");\n"
        'CREATE VIEW "t2" AS select * from "data_2";\n'
    )


def test_memory_functions():
    result = CliRunner().invoke(
        cli.cli,
        ["memory", "select hello()", "--functions", "hello = lambda: 'Hello'"],
    )
    assert result.exit_code == 0
    assert result.output.strip() == '[{"hello()": "Hello"}]'


def test_memory_functions_multiple():
    result = CliRunner().invoke(
        cli.cli,
        [
            "memory",
            "select triple(2), quadruple(2)",
            "--functions",
            "def triple(x):\n    return x * 3",
            "--functions",
            "def quadruple(x):\n    return x * 4",
        ],
    )
    assert result.exit_code == 0
    assert result.output.strip() == '[{"triple(2)": 6, "quadruple(2)": 8}]'


def test_memory_return_db(tmpdir):
    # https://github.com/simonw/sqlite-utils/issues/643
    from sqlite_utils.cli import cli

    path = str(tmpdir / "dogs.csv")
    with open(path, "w") as f:
        f.write("id,name\n1,Cleo")

    with click.Context(cli) as ctx:  # type: ignore[attr-defined]
        db = ctx.invoke(cli.commands["memory"], paths=(path,), return_db=True)

    assert db.table_names() == ["dogs"]

```

### `tests/test_cli_migrate.py`

```py
import pathlib

import pytest
from click.testing import CliRunner

import sqlite_utils
import sqlite_utils.cli

TWO_MIGRATIONS = """
from sqlite_utils import Migrations

m = Migrations("hello")

@m()
def foo(db):
    db.table("foo").insert({"hello": "world"})

@m()
def bar(db):
    db.table("bar").insert({"hello": "world"})
"""


@pytest.fixture
def two_migrations(tmpdir):
    path = pathlib.Path(tmpdir)
    (path / "foo").mkdir()
    migrations_py = path / "foo" / "migrations.py"
    migrations_py.write_text(TWO_MIGRATIONS, "utf-8")
    return path, migrations_py


@pytest.fixture
def two_sets_same_migration_name(tmpdir):
    path = pathlib.Path(tmpdir)
    migrations_py = path / "migrations.py"
    migrations_py.write_text(
        """
from sqlite_utils import Migrations

creatures = Migrations("creatures")

@creatures()
def create_table(db):
    db.table("creatures").insert({"name": "Cleo"})

@creatures()
def add_weight(db):
    db.table("creature_weights").insert({"weight": 4.2})

sales = Migrations("sales")

@sales()
def create_table(db):
    db.table("sales").insert({"id": 1})

@sales()
def add_weight(db):
    db.table("sales_weights").insert({"weight": 10})
""",
        "utf-8",
    )
    return path, migrations_py


@pytest.mark.parametrize("arg", ("TMPDIR", "TMPDIR/foo/migrations.py", "TMPDIR/foo/"))
def test_basic(two_migrations, arg):
    path, _ = two_migrations
    db_path = str(path / "test.db")

    runner = CliRunner()

    def _list():
        list_result = runner.invoke(
            sqlite_utils.cli.cli,
            ["migrate", db_path, "--list", arg.replace("TMPDIR", str(path))],
        )
        assert list_result.exit_code == 0
        return list_result.output

    assert _list() == (
        "Migrations for: hello\n\n"
        "  Applied:\n\n"
        "  Pending:\n"
        "    foo\n"
        "    bar\n\n"
    )

    result = runner.invoke(
        sqlite_utils.cli.cli, ["migrate", db_path, arg.replace("TMPDIR", str(path))]
    )
    assert result.exit_code == 0, result.output

    list_output = _list()
    assert "Migrations for: hello\n\n  Applied:\n    " in list_output
    prior_to_pending = list_output.split(" Pending")[0]
    assert "  foo" in prior_to_pending
    assert "  bar" in prior_to_pending
    assert " Pending:\n    (none)" in list_output

    db = sqlite_utils.Database(db_path)
    assert db.table("foo").exists()
    assert db.table("bar").exists()
    assert db.table("_sqlite_migrations").exists()
    rows = list(db.table("_sqlite_migrations").rows)
    assert len(rows) == 2
    assert rows[0]["name"] == "foo"
    assert rows[1]["name"] == "bar"


def test_list_same_migration_names_in_different_sets(capsys):
    applied = sqlite_utils.Migrations("applied")

    @applied(name="foo")
    def applied_foo(db):
        db.table("applied").insert({"hello": "world"})

    pending = sqlite_utils.Migrations("pending")

    @pending(name="foo")
    def pending_foo(db):
        db.table("pending").insert({"hello": "world"})

    db = sqlite_utils.Database(memory=True)
    applied.apply(db)

    sqlite_utils.cli._display_migration_list(db, [applied, pending])

    output = capsys.readouterr().out
    assert (
        "Migrations for: pending\n\n" "  Applied:\n\n" "  Pending:\n" "    foo\n\n"
    ) in output


def test_verbose(tmpdir):
    path = pathlib.Path(tmpdir)
    (path / "foo").mkdir()
    migrations_py = path / "foo" / "migrations.py"
    migrations_py.write_text(
        """
from sqlite_utils import Migrations

m = Migrations("hello")

@m()
def foo(db):
    db.table("dogs").insert({"id": 1, "name": "Cleo"})
    """,
        "utf-8",
    )
    db_path = str(path / "test.db")
    runner = CliRunner()
    result = runner.invoke(
        sqlite_utils.cli.cli, ["migrate", db_path, str(migrations_py)]
    )
    assert result.exit_code == 0

    result = runner.invoke(
        sqlite_utils.cli.cli, ["migrate", db_path, str(migrations_py), "--verbose"]
    )
    assert result.exit_code == 0
    expected = """
Schema before:

  CREATE TABLE "_sqlite_migrations" (
     "id" INTEGER PRIMARY KEY,
     "migration_set" TEXT,
     "name" TEXT,
     "applied_at" TEXT
  );
  CREATE UNIQUE INDEX "idx__sqlite_migrations_migration_set_name"
      ON "_sqlite_migrations" ("migration_set", "name");
  CREATE TABLE "dogs" (
     "id" INTEGER,
     "name" TEXT
  );

Schema after:

  (unchanged)
""".strip()
    assert expected in result.output

    new_migration = """
@m()
def bar(db):
    db.table("dogs").add_column("age", int)
    db.table("dogs").add_column("weight", float)
    db.table("dogs").transform()
"""
    migrations_py.write_text(migrations_py.read_text("utf-8") + new_migration)

    result = runner.invoke(
        sqlite_utils.cli.cli, ["migrate", db_path, str(migrations_py), "--verbose"]
    )
    assert result.exit_code == 0
    expected_diff = """
Schema diff:

     ON "_sqlite_migrations" ("migration_set", "name");
 CREATE TABLE "dogs" (
    "id" INTEGER,
-   "name" TEXT
+   "name" TEXT,
+   "age" INTEGER,
+   "weight" REAL
 );
""".strip()
    assert expected_diff in result.output


def test_stop_before(two_migrations):
    path, _ = two_migrations
    db_path = str(path / "test.db")
    result = CliRunner().invoke(
        sqlite_utils.cli.cli,
        [
            "migrate",
            db_path,
            str(path / "foo" / "migrations.py"),
            "--stop-before",
            "bar",
        ],
    )
    assert result.exit_code == 0
    db = sqlite_utils.Database(db_path)
    assert db.table("foo").exists()
    assert not db.table("bar").exists()


def test_stop_before_multiple_sets_unqualified(two_migrations):
    path, _ = two_migrations
    db_path = str(path / "test.db")
    (path / "foo" / "migrations2.py").write_text(
        """
from sqlite_utils import Migrations

m = Migrations("hello2")

@m()
def foo(db):
    db.table("foo").insert({"hello": "world"})
    """,
        "utf-8",
    )
    result = CliRunner().invoke(
        sqlite_utils.cli.cli,
        [
            "migrate",
            db_path,
            str(path / "foo" / "migrations.py"),
            str(path / "foo" / "migrations2.py"),
            "--stop-before",
            "foo",
        ],
    )
    assert result.exit_code == 0, result.output
    db = sqlite_utils.Database(db_path)
    assert db.table_names() == ["_sqlite_migrations"]
    assert list(db.table("_sqlite_migrations").rows) == []


def test_stop_before_qualified_only_affects_named_set(two_sets_same_migration_name):
    path, migrations_py = two_sets_same_migration_name
    db_path = str(path / "test.db")
    result = CliRunner().invoke(
        sqlite_utils.cli.cli,
        [
            "migrate",
            db_path,
            str(migrations_py),
            "--stop-before",
            "creatures:add_weight",
        ],
    )
    assert result.exit_code == 0, result.output
    db = sqlite_utils.Database(db_path)
    assert db.table("creatures").exists()
    assert not db.table("creature_weights").exists()
    assert db.table("sales").exists()
    assert db.table("sales_weights").exists()


def test_stop_before_multiple_qualified(two_sets_same_migration_name):
    path, migrations_py = two_sets_same_migration_name
    db_path = str(path / "test.db")
    result = CliRunner().invoke(
        sqlite_utils.cli.cli,
        [
            "migrate",
            db_path,
            str(migrations_py),
            "--stop-before",
            "creatures:add_weight",
            "--stop-before",
            "sales:add_weight",
        ],
    )
    assert result.exit_code == 0, result.output
    db = sqlite_utils.Database(db_path)
    assert db.table("creatures").exists()
    assert not db.table("creature_weights").exists()
    assert db.table("sales").exists()
    assert not db.table("sales_weights").exists()


LEGACY_MIGRATIONS = """
import datetime

class _Migration:
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

class _Applied:
    def __init__(self, name, applied_at):
        self.name = name
        self.applied_at = applied_at

class LegacyMigrations:
    # Mimics the sqlite-migrate 0.x Migrations class, in particular
    # apply(db, stop_before=None) taking a single string
    migrations_table = "_sqlite_migrations"

    def __init__(self, name):
        self.name = name
        self._migrations = []

    def __call__(self, fn):
        self._migrations.append(_Migration(fn.__name__, fn))
        return fn

    def ensure_migrations_table(self, db):
        db.table(self.migrations_table).create(
            {"migration_set": str, "name": str, "applied_at": str},
            pk=("migration_set", "name"),
            if_not_exists=True,
        )

    def applied(self, db):
        self.ensure_migrations_table(db)
        return [
            _Applied(row["name"], row["applied_at"])
            for row in db.table(self.migrations_table).rows_where(
                "migration_set = ?", [self.name]
            )
        ]

    def pending(self, db):
        applied = {m.name for m in self.applied(db)}
        return [m for m in self._migrations if m.name not in applied]

    def apply(self, db, stop_before=None):
        for migration in self.pending(db):
            if migration.name == stop_before:
                return
            migration.fn(db)
            db.table(self.migrations_table).insert(
                {
                    "migration_set": self.name,
                    "name": migration.name,
                    "applied_at": str(
                        datetime.datetime.now(datetime.timezone.utc)
                    ),
                }
            )

legacy = LegacyMigrations("legacy_set")

@legacy
def first(db):
    db.table("first").insert({"hello": "world"})

@legacy
def second(db):
    db.table("second").insert({"hello": "world"})
"""


def test_stop_before_unknown_name_errors(two_migrations):
    path, _ = two_migrations
    db_path = str(path / "test.db")
    runner = CliRunner()
    result = runner.invoke(
        sqlite_utils.cli.cli,
        ["migrate", db_path, str(path), "--stop-before", "fooo"],
    )
    assert result.exit_code == 1
    assert "--stop-before did not match any migrations: fooo" in result.output
    # Nothing should have been applied
    db = sqlite_utils.Database(db_path)
    assert "foo" not in db.table_names()
    assert "bar" not in db.table_names()


def test_stop_before_with_legacy_migrations_class(tmpdir):
    path = pathlib.Path(tmpdir)
    (path / "migrations.py").write_text(LEGACY_MIGRATIONS, "utf-8")
    db_path = str(path / "test.db")
    runner = CliRunner()
    result = runner.invoke(
        sqlite_utils.cli.cli,
        ["migrate", db_path, str(path), "--stop-before", "second"],
    )
    assert result.exit_code == 0, result.output
    db = sqlite_utils.Database(db_path)
    assert "first" in db.table_names()
    assert "second" not in db.table_names()


def test_stop_before_multiple_values_for_legacy_set_errors(tmpdir):
    path = pathlib.Path(tmpdir)
    (path / "migrations.py").write_text(LEGACY_MIGRATIONS, "utf-8")
    db_path = str(path / "test.db")
    runner = CliRunner()
    result = runner.invoke(
        sqlite_utils.cli.cli,
        [
            "migrate",
            db_path,
            str(path),
            "--stop-before",
            "legacy_set:first",
            "--stop-before",
            "legacy_set:second",
        ],
    )
    assert result.exit_code == 1
    assert "single --stop-before" in result.output


def test_list_does_not_create_database_file(two_migrations):
    path, _ = two_migrations
    db_path = path / "test.db"
    runner = CliRunner()
    result = runner.invoke(
        sqlite_utils.cli.cli, ["migrate", str(db_path), str(path), "--list"]
    )
    assert result.exit_code == 0, result.output
    assert "Pending:\n    foo\n    bar" in result.output
    # Listing migrations must not create the database file
    assert not db_path.exists()


def test_list_does_not_upgrade_legacy_migrations_table(two_migrations):
    path, _ = two_migrations
    db_path = str(path / "test.db")
    db = sqlite_utils.Database(db_path)
    db.table("_sqlite_migrations").create(
        {"migration_set": str, "name": str, "applied_at": str},
        pk=("migration_set", "name"),
    )
    db.table("_sqlite_migrations").insert(
        {"migration_set": "hello", "name": "foo", "applied_at": "x"}
    )
    db.close()
    runner = CliRunner()
    result = runner.invoke(
        sqlite_utils.cli.cli, ["migrate", db_path, str(path), "--list"]
    )
    assert result.exit_code == 0, result.output
    assert "foo - x" in result.output
    # --list must not perform the one-way legacy schema upgrade
    db2 = sqlite_utils.Database(db_path)
    assert db2.table("_sqlite_migrations").pks == ["migration_set", "name"]
    db2.close()


def test_stop_before_applied_migration_errors(two_migrations):
    path, _ = two_migrations
    db_path = str(path / "test.db")
    migrations_path = str(path / "foo" / "migrations.py")
    # Apply everything first
    first = CliRunner().invoke(
        sqlite_utils.cli.cli,
        ["migrate", db_path, migrations_path, "--stop-before", "bar"],
    )
    assert first.exit_code == 0
    # foo is now applied - stopping before it is an error, and bar
    # must not be applied as a side effect
    result = CliRunner().invoke(
        sqlite_utils.cli.cli,
        ["migrate", db_path, migrations_path, "--stop-before", "foo"],
    )
    assert result.exit_code != 0
    assert "already been applied" in result.output
    db = sqlite_utils.Database(db_path)
    assert not db.table("bar").exists()


def test_list_with_legacy_class_is_read_only(tmpdir):
    # Legacy sqlite-migrate classes create the _sqlite_migrations table
    # from their pending()/applied() methods - --list must roll that
    # back so it stays a read-only operation as documented
    path = pathlib.Path(tmpdir)
    (path / "migrations.py").write_text(LEGACY_MIGRATIONS, "utf-8")
    db_path = str(path / "test.db")
    db = sqlite_utils.Database(db_path)
    db.table("existing").insert({"id": 1})
    db.close()
    result = CliRunner().invoke(
        sqlite_utils.cli.cli, ["migrate", db_path, str(path), "--list"]
    )
    assert result.exit_code == 0, result.output
    assert "first" in result.output
    db2 = sqlite_utils.Database(db_path)
    assert "_sqlite_migrations" not in db2.table_names()
    db2.close()

```

### `tests/test_cli.py`

```py
import json
import os
import sqlite3
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest
from click.testing import CliRunner

from sqlite_utils import ANY, Database, cli
from sqlite_utils.db import ForeignKey, Index


def write_json(file_path, data):
    with open(file_path, "w") as fp:
        json.dump(data, fp)


def _supports_pragma_function_list():
    db = Database(memory=True)
    try:
        db.execute("select * from pragma_function_list()")
        return True
    except sqlite3.DatabaseError:
        return False
    finally:
        db.close()


def _has_compiled_ext():
    for ext in ["dylib", "so", "dll"]:
        path = Path(__file__).parent / f"ext.{ext}"
        if path.is_file():
            return True
    return False


COMPILED_EXTENSION_PATH = str(Path(__file__).parent / "ext")


@pytest.mark.parametrize(
    "options",
    (
        ["-h"],
        ["--help"],
        ["insert", "-h"],
        ["insert", "--help"],
    ),
)
def test_help(options):
    result = CliRunner().invoke(cli.cli, options)
    assert result.exit_code == 0
    assert result.output.startswith("Usage: ")
    assert "-h, --help" in result.output


def test_tables(db_path):
    result = CliRunner().invoke(cli.cli, ["tables", db_path], catch_exceptions=False)
    assert '[{"table": "Gosh"},\n {"table": "Gosh2"}]' == result.output.strip()


def test_views(db_path):
    Database(db_path).create_view("hello", "select sqlite_version()")
    result = CliRunner().invoke(cli.cli, ["views", db_path, "--table", "--schema"])
    assert (
        "view    schema\n"
        "------  ----------------------------------------------\n"
        'hello   CREATE VIEW "hello" AS select sqlite_version()'
    ) == result.output.strip()


def test_tables_fts4(db_path):
    Database(db_path).table("Gosh").enable_fts(["c2"], fts_version="FTS4")
    result = CliRunner().invoke(cli.cli, ["tables", "--fts4", db_path])
    assert '[{"table": "Gosh_fts"}]' == result.output.strip()


def test_tables_fts5(db_path):
    Database(db_path).table("Gosh").enable_fts(["c2"], fts_version="FTS5")
    result = CliRunner().invoke(cli.cli, ["tables", "--fts5", db_path])
    assert '[{"table": "Gosh_fts"}]' == result.output.strip()


def test_tables_counts_and_columns(db_path):
    db = Database(db_path)
    with db.conn:
        db.table("lots").insert_all([{"id": i, "age": i + 1} for i in range(30)])
    result = CliRunner().invoke(cli.cli, ["tables", "--counts", "--columns", db_path])
    assert (
        '[{"table": "Gosh", "count": 0, "columns": ["c1", "c2", "c3"]},\n'
        ' {"table": "Gosh2", "count": 0, "columns": ["c1", "c2", "c3"]},\n'
        ' {"table": "lots", "count": 30, "columns": ["id", "age"]}]'
    ) == result.output.strip()


@pytest.mark.parametrize(
    "format,expected",
    [
        (
            "--csv",
            (
                "table,count,columns\n"
                'Gosh,0,"c1\n'
                "c2\n"
                'c3"\n'
                'Gosh2,0,"c1\n'
                "c2\n"
                'c3"\n'
                'lots,30,"id\n'
                'age"'
            ),
        ),
        (
            "--tsv",
            "table\tcount\tcolumns\nGosh\t0\t['c1', 'c2', 'c3']\nGosh2\t0\t['c1', 'c2', 'c3']\nlots\t30\t['id', 'age']",
        ),
    ],
)
def test_tables_counts_and_columns_csv(db_path, format, expected):
    db = Database(db_path)
    with db.conn:
        db.table("lots").insert_all([{"id": i, "age": i + 1} for i in range(30)])
    result = CliRunner().invoke(
        cli.cli, ["tables", "--counts", "--columns", format, db_path]
    )
    assert result.output.strip().replace("\r", "") == expected


def test_tables_schema(db_path):
    db = Database(db_path)
    with db.conn:
        db.table("lots").insert_all([{"id": i, "age": i + 1} for i in range(30)])
    result = CliRunner().invoke(cli.cli, ["tables", "--schema", db_path])
    assert (
        '[{"table": "Gosh", "schema": "CREATE TABLE Gosh (c1 text, c2 text, c3 text)"},\n'
        ' {"table": "Gosh2", "schema": "CREATE TABLE Gosh2 (c1 text, c2 text, c3 text)"},\n'
        ' {"table": "lots", "schema": "CREATE TABLE \\"lots\\" (\\n   \\"id\\" INTEGER,\\n   \\"age\\" INTEGER\\n)"}]'
    ) == result.output.strip()


@pytest.mark.parametrize(
    "options,expected",
    [
        (
            ["--fmt", "simple"],
            (
                "c1     c2     c3\n"
                "-----  -----  ----------\n"
                "verb0  noun0  adjective0\n"
                "verb1  noun1  adjective1\n"
                "verb2  noun2  adjective2\n"
                "verb3  noun3  adjective3"
            ),
        ),
        (
            ["-t"],
            (
                "c1     c2     c3\n"
                "-----  -----  ----------\n"
                "verb0  noun0  adjective0\n"
                "verb1  noun1  adjective1\n"
                "verb2  noun2  adjective2\n"
                "verb3  noun3  adjective3"
            ),
        ),
        (
            ["--fmt", "rst"],
            (
                "=====  =====  ==========\n"
                "c1     c2     c3\n"
                "=====  =====  ==========\n"
                "verb0  noun0  adjective0\n"
                "verb1  noun1  adjective1\n"
                "verb2  noun2  adjective2\n"
                "verb3  noun3  adjective3\n"
                "=====  =====  =========="
            ),
        ),
    ],
)
def test_output_table(db_path, options, expected):
    db = Database(db_path)
    with db.conn:
        db.table("rows").insert_all(
            [
                {
                    "c1": f"verb{i}",
                    "c2": f"noun{i}",
                    "c3": f"adjective{i}",
                }
                for i in range(4)
            ]
        )
    result = CliRunner().invoke(cli.cli, ["rows", db_path, "rows"] + options)
    assert result.exit_code == 0
    assert expected == result.output.strip()


@pytest.mark.parametrize(
    "fmt_option", [["--fmt", "simple"], ["-t"], ["--fmt", "github"]]
)
def test_output_table_no_headers(db_path, fmt_option):
    # --no-headers should omit the header row from --fmt/--table output too, not
    # just from --csv/--tsv (#566). Previously the flag was silently ignored for
    # tabulate formats and the column names were always printed.
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert_all(
            [
                {"id": 1, "name": "Cleo", "age": 4},
                {"id": 2, "name": "Pancakes", "age": 2},
            ]
        )
    sql = "select id, name, age from dogs order by id"

    with_headers = CliRunner().invoke(cli.cli, ["query", db_path, sql] + fmt_option)
    without_headers = CliRunner().invoke(
        cli.cli, ["query", db_path, sql] + fmt_option + ["--no-headers"]
    )
    assert with_headers.exit_code == 0
    assert without_headers.exit_code == 0

    # The column names appear when headers are shown, and must not appear at all
    # once --no-headers is passed.
    assert "name" in with_headers.output
    for header in ("id", "name", "age"):
        assert (
            header not in without_headers.output
        ), f"header {header!r} leaked into --no-headers output"
    # The data is still all present.
    for value in ("Cleo", "Pancakes", "1", "2", "4"):
        assert value in without_headers.output

    # The rows command shares the same code path.
    rows_no_headers = CliRunner().invoke(
        cli.cli, ["rows", db_path, "dogs"] + fmt_option + ["--no-headers"]
    )
    assert rows_no_headers.exit_code == 0
    assert "name" not in rows_no_headers.output
    assert "Cleo" in rows_no_headers.output


def test_create_index(db_path):
    db = Database(db_path)
    assert [] == db.table("Gosh").indexes
    result = CliRunner().invoke(cli.cli, ["create-index", db_path, "Gosh", "c1"])
    assert result.exit_code == 0
    assert [
        Index(
            seq=0, name="idx_Gosh_c1", unique=0, origin="c", partial=0, columns=["c1"]
        )
    ] == db.table("Gosh").indexes
    # Try with a custom name
    result = CliRunner().invoke(
        cli.cli, ["create-index", db_path, "Gosh", "c2", "--name", "blah"]
    )
    assert result.exit_code == 0
    assert [
        Index(seq=0, name="blah", unique=0, origin="c", partial=0, columns=["c2"]),
        Index(
            seq=1, name="idx_Gosh_c1", unique=0, origin="c", partial=0, columns=["c1"]
        ),
    ] == db.table("Gosh").indexes
    # Try a two-column unique index
    create_index_unique_args = [
        "create-index",
        db_path,
        "Gosh2",
        "c1",
        "c2",
        "--unique",
    ]
    result = CliRunner().invoke(cli.cli, create_index_unique_args)
    assert result.exit_code == 0
    assert [
        Index(
            seq=0,
            name="idx_Gosh2_c1_c2",
            unique=1,
            origin="c",
            partial=0,
            columns=["c1", "c2"],
        )
    ] == db.table("Gosh2").indexes
    # Trying to create the same index should fail
    assert CliRunner().invoke(cli.cli, create_index_unique_args).exit_code != 0
    # ... unless we use --if-not-exists or --ignore
    for option in ("--if-not-exists", "--ignore"):
        assert (
            CliRunner().invoke(cli.cli, create_index_unique_args + [option]).exit_code
            == 0
        )


def test_drop_index(db_path):
    db = Database(db_path)
    db.table("Gosh").create_index(["c1"])
    assert [index.name for index in db.table("Gosh").indexes] == ["idx_Gosh_c1"]
    result = CliRunner().invoke(cli.cli, ["drop-index", db_path, "Gosh", "idx_Gosh_c1"])
    assert result.exit_code == 0
    assert db.table("Gosh").indexes == []

    result = CliRunner().invoke(cli.cli, ["drop-index", db_path, "Gosh", "idx_Gosh_c1"])
    assert result.exit_code == 1
    assert "No index named idx_Gosh_c1" in result.output

    result = CliRunner().invoke(
        cli.cli, ["drop-index", db_path, "Gosh", "idx_Gosh_c1", "--ignore"]
    )
    assert result.exit_code == 0


def test_create_index_analyze(db_path):
    db = Database(db_path)
    assert "sqlite_stat1" not in db.table_names()
    assert [] == db.table("Gosh").indexes
    result = CliRunner().invoke(
        cli.cli, ["create-index", db_path, "Gosh", "c1", "--analyze"]
    )
    assert result.exit_code == 0
    assert "sqlite_stat1" in db.table_names()


def test_create_index_desc(db_path):
    db = Database(db_path)
    assert [] == db.table("Gosh").indexes
    result = CliRunner().invoke(cli.cli, ["create-index", db_path, "Gosh", "--", "-c1"])
    assert result.exit_code == 0
    assert (
        db.execute("select sql from sqlite_master where type='index'").fetchone()[0]
        == 'CREATE INDEX "idx_Gosh_c1"\n    ON "Gosh" ("c1" desc)'
    )


@pytest.mark.parametrize(
    "col_name,col_type,expected_schema",
    (
        ("text", "TEXT", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "text" TEXT)'),
        ("text", "str", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "text" TEXT)'),
        ("text", "STR", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "text" TEXT)'),
        (
            "integer",
            "INTEGER",
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "integer" INTEGER)',
        ),
        (
            "integer",
            "int",
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "integer" INTEGER)',
        ),
        ("float", "FLOAT", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "float" REAL)'),
        ("blob", "blob", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "blob" BLOB)'),
        ("blob", "BLOB", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "blob" BLOB)'),
        ("blob", "bytes", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "blob" BLOB)'),
        ("blob", "BYTES", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "blob" BLOB)'),
        ("anything", "any", 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "anything" ANY)'),
        ("default", None, 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "default" TEXT)'),
    ),
)
def test_add_column(db_path, col_name, col_type, expected_schema):
    db = Database(db_path)
    db.create_table("dogs", {"name": str})
    assert db.table("dogs").schema == 'CREATE TABLE "dogs" (\n   "name" TEXT\n)'
    args = ["add-column", db_path, "dogs", col_name]
    if col_type is not None:
        args.append(col_type)
    assert CliRunner().invoke(cli.cli, args).exit_code == 0
    assert db.table("dogs").schema == expected_schema


@pytest.mark.parametrize("ignore", (True, False))
def test_add_column_ignore(db_path, ignore):
    db = Database(db_path)
    db.create_table("dogs", {"name": str})
    args = ["add-column", db_path, "dogs", "name"] + (["--ignore"] if ignore else [])
    result = CliRunner().invoke(cli.cli, args)
    if ignore:
        assert result.exit_code == 0
    else:
        assert result.exit_code == 1
        assert result.output == "Error: duplicate column name: name\n"


def test_add_column_not_null_default(db_path):
    db = Database(db_path)
    db.create_table("dogs", {"name": str})
    assert db.table("dogs").schema == 'CREATE TABLE "dogs" (\n   "name" TEXT\n)'
    args = [
        "add-column",
        db_path,
        "dogs",
        "nickname",
        "--not-null-default",
        "dogs'dawg",
    ]
    assert CliRunner().invoke(cli.cli, args).exit_code == 0
    assert db.table("dogs").schema == (
        'CREATE TABLE "dogs" (\n'
        '   "name" TEXT\n'
        ", \"nickname\" TEXT NOT NULL DEFAULT 'dogs''dawg')"
    )


@pytest.mark.parametrize(
    "args,assert_message",
    (
        (
            ["books", "author_id", "authors", "id"],
            "Explicit other_table and other_column",
        ),
        (["books", "author_id", "authors"], "Explicit other_table, guess other_column"),
        (["books", "author_id"], "Automatically guess other_table and other_column"),
    ),
)
def test_add_foreign_key(db_path, args, assert_message):
    db = Database(db_path)
    db.table("authors").insert_all(
        [{"id": 1, "name": "Sally"}, {"id": 2, "name": "Asheesh"}], pk="id"
    )
    db.table("books").insert_all(
        [
            {"title": "Hedgehogs of the world", "author_id": 1},
            {"title": "How to train your wolf", "author_id": 2},
        ]
    )
    assert (
        CliRunner().invoke(cli.cli, ["add-foreign-key", db_path] + args).exit_code == 0
    ), assert_message
    assert [
        ForeignKey(
            table="books", column="author_id", other_table="authors", other_column="id"
        )
    ] == db.table("books").foreign_keys

    # Error if we try to add it twice:
    result = CliRunner().invoke(
        cli.cli, ["add-foreign-key", db_path, "books", "author_id", "authors", "id"]
    )
    assert result.exit_code != 0
    assert (
        "Error: Foreign key already exists for author_id => authors.id"
        == result.output.strip()
    )

    # No error if we add it twice with --ignore
    result = CliRunner().invoke(
        cli.cli,
        ["add-foreign-key", db_path, "books", "author_id", "authors", "id", "--ignore"],
    )
    assert result.exit_code == 0

    # Error if we try against an invalid column
    result = CliRunner().invoke(
        cli.cli, ["add-foreign-key", db_path, "books", "author_id", "authors", "bad"]
    )
    assert result.exit_code != 0
    assert "Error: No such column: authors.bad" == result.output.strip()


def test_add_column_foreign_key(db_path):
    db = Database(db_path)
    db.table("authors").insert({"id": 1, "name": "Sally"}, pk="id")
    db.table("books").insert({"title": "Hedgehogs of the world"})
    # Add an author_id foreign key column to the books table
    result = CliRunner().invoke(
        cli.cli, ["add-column", db_path, "books", "author_id", "--fk", "authors"]
    )
    assert result.exit_code == 0, result.output
    assert db.table("books").schema == (
        'CREATE TABLE "books" (\n'
        '   "title" TEXT,\n'
        '   "author_id" INTEGER REFERENCES "authors"("id")\n'
        ")"
    )
    # Try it again with a custom --fk-col
    result = CliRunner().invoke(
        cli.cli,
        [
            "add-column",
            db_path,
            "books",
            "author_name_ref",
            "--fk",
            "authors",
            "--fk-col",
            "name",
        ],
    )
    assert result.exit_code == 0, result.output
    assert db.table("books").schema == (
        'CREATE TABLE "books" (\n'
        '   "title" TEXT,\n'
        '   "author_id" INTEGER REFERENCES "authors"("id"),\n'
        '   "author_name_ref" TEXT REFERENCES "authors"("name")\n'
        ")"
    )
    # Throw an error if the --fk table does not exist
    result = CliRunner().invoke(
        cli.cli, ["add-column", db_path, "books", "author_id", "--fk", "bobcats"]
    )
    assert result.exit_code != 0
    assert "table 'bobcats' does not exist" in str(result.exception)


def test_suggest_alter_if_column_missing(db_path):
    db = Database(db_path)
    db.table("authors").insert({"id": 1, "name": "Sally"}, pk="id")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "authors", "-"],
        input='{"id": 2, "name": "Barry", "age": 43}',
    )
    assert result.exit_code != 0
    assert result.output.strip() == (
        "Error: table authors has no column named age\n\n"
        "Try using --alter to add additional columns"
    )


def test_index_foreign_keys(db_path):
    test_add_column_foreign_key(db_path)
    db = Database(db_path)
    assert [] == db.table("books").indexes
    result = CliRunner().invoke(cli.cli, ["index-foreign-keys", db_path])
    assert result.exit_code == 0
    assert [["author_id"], ["author_name_ref"]] == [
        i.columns for i in db.table("books").indexes
    ]


def test_enable_fts(db_path):
    db = Database(db_path)
    assert db.table("Gosh").detect_fts() is None
    result = CliRunner().invoke(
        cli.cli, ["enable-fts", db_path, "Gosh", "c1", "--fts4"]
    )
    assert result.exit_code == 0
    assert "Gosh_fts" == db.table("Gosh").detect_fts()

    # Table names with restricted chars are handled correctly.
    # colons and dots are restricted characters for table names.
    db.table("http://example.com").create({"c1": str, "c2": str, "c3": str})
    assert db.table("http://example.com").detect_fts() is None
    result = CliRunner().invoke(
        cli.cli,
        [
            "enable-fts",
            db_path,
            "http://example.com",
            "c1",
            "--fts4",
            "--tokenize",
            "porter",
        ],
    )
    assert result.exit_code == 0
    assert "http://example.com_fts" == db.table("http://example.com").detect_fts()
    # Check tokenize was set to porter
    assert (
        'CREATE VIRTUAL TABLE "http://example.com_fts" USING FTS4 (\n'
        '    "c1",\n'
        "    tokenize='porter',\n"
        '    content="http://example.com"'
        "\n)"
    ) == db.table("http://example.com_fts").schema
    db.table("http://example.com").drop()


def test_enable_fts_replace(db_path):
    db = Database(db_path)
    assert db.table("Gosh").detect_fts() is None
    result = CliRunner().invoke(
        cli.cli, ["enable-fts", db_path, "Gosh", "c1", "--fts4"]
    )
    assert result.exit_code == 0
    assert "Gosh_fts" == db.table("Gosh").detect_fts()
    assert db.table("Gosh_fts").columns_dict == {"c1": str}

    # This should throw an error
    result2 = CliRunner().invoke(
        cli.cli, ["enable-fts", db_path, "Gosh", "c1", "--fts4"]
    )
    assert result2.exit_code == 1
    assert result2.output == 'Error: table "Gosh_fts" already exists\n'

    # This should work
    result3 = CliRunner().invoke(
        cli.cli, ["enable-fts", db_path, "Gosh", "c2", "--fts4", "--replace"]
    )
    assert result3.exit_code == 0
    assert db.table("Gosh_fts").columns_dict == {"c2": str}


def test_enable_fts_with_triggers(db_path):
    Database(db_path).table("Gosh").insert_all([{"c1": "baz"}])
    exit_code = (
        CliRunner()
        .invoke(
            cli.cli,
            ["enable-fts", db_path, "Gosh", "c1", "--fts4", "--create-triggers"],
        )
        .exit_code
    )
    assert exit_code == 0

    def search(q):
        return (
            Database(db_path)
            .execute("select c1 from Gosh_fts where c1 match ?", [q])
            .fetchall()
        )

    assert [("baz",)] == search("baz")
    Database(db_path).table("Gosh").insert_all([{"c1": "martha"}])
    assert [("martha",)] == search("martha")


def test_populate_fts(db_path):
    Database(db_path).table("Gosh").insert_all([{"c1": "baz"}])
    exit_code = (
        CliRunner()
        .invoke(cli.cli, ["enable-fts", db_path, "Gosh", "c1", "--fts4"])
        .exit_code
    )
    assert exit_code == 0

    def search(q):
        return (
            Database(db_path)
            .execute("select c1 from Gosh_fts where c1 match ?", [q])
            .fetchall()
        )

    assert [("baz",)] == search("baz")
    Database(db_path).table("Gosh").insert_all([{"c1": "martha"}])
    assert [] == search("martha")
    exit_code = (
        CliRunner().invoke(cli.cli, ["populate-fts", db_path, "Gosh", "c1"]).exit_code
    )
    assert exit_code == 0
    assert [("martha",)] == search("martha")


def test_disable_fts(db_path):
    db = Database(db_path)
    assert {"Gosh", "Gosh2"} == set(db.table_names())
    db.table("Gosh").enable_fts(["c1"], create_triggers=True)
    assert {
        "Gosh_fts",
        "Gosh_fts_idx",
        "Gosh_fts_data",
        "Gosh2",
        "Gosh_fts_config",
        "Gosh",
        "Gosh_fts_docsize",
    } == set(db.table_names())
    exit_code = CliRunner().invoke(cli.cli, ["disable-fts", db_path, "Gosh"]).exit_code
    assert exit_code == 0
    assert {"Gosh", "Gosh2"} == set(db.table_names())


def test_vacuum(db_path):
    result = CliRunner().invoke(cli.cli, ["vacuum", db_path])
    assert result.exit_code == 0


def test_dump(db_path):
    result = CliRunner().invoke(cli.cli, ["dump", db_path])
    assert result.exit_code == 0
    assert result.output.startswith("BEGIN TRANSACTION;")
    assert result.output.strip().endswith("COMMIT;")


@pytest.mark.parametrize("tables", ([], ["Gosh"], ["Gosh2"]))
def test_optimize(db_path, tables):
    db = Database(db_path)
    with db.conn:
        for table in ("Gosh", "Gosh2"):
            db.table(table).insert_all(
                [
                    {
                        "c1": f"verb{i}",
                        "c2": f"noun{i}",
                        "c3": f"adjective{i}",
                    }
                    for i in range(10000)
                ]
            )
        db.table("Gosh").enable_fts(["c1", "c2", "c3"], fts_version="FTS4")
        db.table("Gosh2").enable_fts(["c1", "c2", "c3"], fts_version="FTS5")
    size_before_optimize = os.stat(db_path).st_size
    result = CliRunner().invoke(cli.cli, ["optimize", db_path] + tables)
    assert result.exit_code == 0
    size_after_optimize = os.stat(db_path).st_size
    # Weirdest thing: tests started failing because size after
    # ended up larger than size before in some cases. I think
    # it's OK to tolerate that happening, though it's very strange.
    assert size_after_optimize <= (size_before_optimize + 10000)
    # Soundness check that --no-vacuum doesn't throw errors:
    result = CliRunner().invoke(cli.cli, ["optimize", "--no-vacuum", db_path])
    assert result.exit_code == 0


def test_rebuild_fts_fixes_docsize_error(db_path):
    db = Database(db_path, recursive_triggers=False)
    records = [
        {
            "c1": f"verb{i}",
            "c2": f"noun{i}",
            "c3": f"adjective{i}",
        }
        for i in range(10000)
    ]
    with db.conn:
        db.table("fts5_table").insert_all(records, pk="c1")
        db.table("fts5_table").enable_fts(
            ["c1", "c2", "c3"], fts_version="FTS5", create_triggers=True
        )
    # Search should work
    assert list(db.table("fts5_table").search("verb1"))
    # Replicate docsize error from this issue for FTS5
    # https://github.com/simonw/sqlite-utils/issues/149
    assert db.table("fts5_table_fts_docsize").count == 10000
    db.table("fts5_table").insert_all(records, replace=True)
    assert db.table("fts5_table").count == 10000
    assert db.table("fts5_table_fts_docsize").count == 20000
    # Running rebuild-fts should fix this
    result = CliRunner().invoke(cli.cli, ["rebuild-fts", db_path, "fts5_table"])
    assert result.exit_code == 0
    assert db.table("fts5_table_fts_docsize").count == 10000


@pytest.mark.parametrize(
    "format,expected",
    [
        ("--csv", "id,name,age\n1,Cleo,4\n2,Pancakes,2\n"),
        ("--tsv", "id\tname\tage\n1\tCleo\t4\n2\tPancakes\t2\n"),
    ],
)
def test_query_csv(db_path, format, expected):
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert_all(
            [
                {"id": 1, "age": 4, "name": "Cleo"},
                {"id": 2, "age": 2, "name": "Pancakes"},
            ]
        )
    result = CliRunner().invoke(
        cli.cli, [db_path, "select id, name, age from dogs", format]
    )
    assert result.exit_code == 0
    assert result.output.replace("\r", "") == expected
    # Test the no-headers option:
    result = CliRunner().invoke(
        cli.cli, [db_path, "select id, name, age from dogs", "--no-headers", format]
    )
    expected_rest = "\n".join(expected.split("\n")[1:]).strip()
    assert result.output.strip().replace("\r", "") == expected_rest


_all_query = "select id, name, age from dogs"
_one_query = "select id, name, age from dogs where id = 1"


@pytest.mark.parametrize(
    "sql,args,expected",
    [
        (
            _all_query,
            [],
            '[{"id": 1, "name": "Cleo", "age": 4},\n {"id": 2, "name": "Pancakes", "age": 2}]',
        ),
        (
            _all_query,
            ["--nl"],
            '{"id": 1, "name": "Cleo", "age": 4}\n{"id": 2, "name": "Pancakes", "age": 2}',
        ),
        (_all_query, ["--arrays"], '[[1, "Cleo", 4],\n [2, "Pancakes", 2]]'),
        (_all_query, ["--arrays", "--nl"], '[1, "Cleo", 4]\n[2, "Pancakes", 2]'),
        (_one_query, [], '[{"id": 1, "name": "Cleo", "age": 4}]'),
        (_one_query, ["--nl"], '{"id": 1, "name": "Cleo", "age": 4}'),
        (_one_query, ["--arrays"], '[[1, "Cleo", 4]]'),
        (_one_query, ["--arrays", "--nl"], '[1, "Cleo", 4]'),
        (
            "select id, dog(age) from dogs",
            ["--functions", "def dog(i):\n  return i * 7"],
            '[{"id": 1, "dog(age)": 28},\n {"id": 2, "dog(age)": 14}]',
        ),
    ],
)
def test_query_json(db_path, sql, args, expected):
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert_all(
            [
                {"id": 1, "age": 4, "name": "Cleo"},
                {"id": 2, "age": 2, "name": "Pancakes"},
            ]
        )
    result = CliRunner().invoke(cli.cli, [db_path, sql] + args)
    assert expected == result.output.strip()


def test_query_sql_from_stdin(db_path):
    # https://github.com/simonw/sqlite-utils/issues/765
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert_all(
            [
                {"id": 1, "age": 4, "name": "Cleo"},
                {"id": 2, "age": 2, "name": "Pancakes"},
            ]
        )
    result = CliRunner().invoke(
        cli.cli,
        ["query", db_path, "-"],
        input="select name from dogs order by name",
    )
    assert result.exit_code == 0, result.output
    assert json.loads(result.output) == [{"name": "Cleo"}, {"name": "Pancakes"}]


def test_query_json_empty(db_path):
    result = CliRunner().invoke(
        cli.cli,
        [db_path, "select * from sqlite_master where 0"],
    )
    assert result.output.strip() == "[]"


def test_query_json_duplicate_columns_are_deduped(db_path):
    # https://github.com/simonw/sqlite-utils/issues/624
    result = CliRunner().invoke(
        cli.cli,
        [db_path, "select 1 as id, 2 as id, 'x' as value, 'y' as value"],
    )
    assert result.output.strip() == (
        '[{"id": 1, "id_2": 2, "value": "x", "value_2": "y"}]'
    )


def test_query_csv_duplicate_columns_are_preserved(db_path):
    # CSV output should keep the duplicate headers, not rename them
    result = CliRunner().invoke(
        cli.cli,
        [db_path, "select 1 as id, 2 as id", "--csv"],
    )
    assert result.output.replace("\r", "").strip() == "id,id\n1,2"


def test_query_invalid_function(db_path):
    result = CliRunner().invoke(
        cli.cli, [db_path, "select bad()", "--functions", "def invalid_python"]
    )
    assert result.exit_code == 1
    assert result.output.startswith("Error: Error in functions definition:")


TEST_FUNCTIONS = """
def zero():
    return 0

def one(a):
    return a

def _two(a, b):
    return a + b

def two(a, b):
    return _two(a, b)
"""


def test_query_complex_function(db_path):
    result = CliRunner().invoke(
        cli.cli,
        [
            db_path,
            "select zero(), one(1), two(1, 2)",
            "--functions",
            TEST_FUNCTIONS,
        ],
    )
    assert result.exit_code == 0
    assert json.loads(result.output.strip()) == [
        {"zero()": 0, "one(1)": 1, "two(1, 2)": 3}
    ]


@pytest.mark.skipif(
    not _supports_pragma_function_list(),
    reason="Needs SQLite version that supports pragma_function_list()",
)
def test_hidden_functions_are_hidden(db_path):
    result = CliRunner().invoke(
        cli.cli,
        [
            db_path,
            "select name from pragma_function_list()",
            "--functions",
            TEST_FUNCTIONS,
        ],
    )
    assert result.exit_code == 0
    functions = {r["name"] for r in json.loads(result.output.strip())}
    assert "zero" in functions
    assert "one" in functions
    assert "two" in functions
    assert "_two" not in functions


def test_query_functions_from_file(db_path, tmp_path):
    # Create a temporary file with function definitions
    functions_file = tmp_path / "my_functions.py"
    functions_file.write_text(TEST_FUNCTIONS)

    result = CliRunner().invoke(
        cli.cli,
        [
            db_path,
            "select zero(), one(1), two(1, 2)",
            "--functions",
            str(functions_file),
        ],
    )
    assert result.exit_code == 0
    assert json.loads(result.output.strip()) == [
        {"zero()": 0, "one(1)": 1, "two(1, 2)": 3}
    ]


def test_query_functions_file_not_found(db_path):
    result = CliRunner().invoke(
        cli.cli,
        [
            db_path,
            "select zero()",
            "--functions",
            "nonexistent.py",
        ],
    )
    assert result.exit_code == 1
    assert "File not found: nonexistent.py" in result.output


def test_query_functions_multiple_invocations(db_path):
    # Test using --functions multiple times
    result = CliRunner().invoke(
        cli.cli,
        [
            db_path,
            "select triple(2), quadruple(2)",
            "--functions",
            "def triple(x):\n    return x * 3",
            "--functions",
            "def quadruple(x):\n    return x * 4",
        ],
    )
    assert result.exit_code == 0
    assert json.loads(result.output.strip()) == [{"triple(2)": 6, "quadruple(2)": 8}]


def test_query_functions_file_and_inline(db_path, tmp_path):
    # Test combining file and inline code
    functions_file = tmp_path / "file_funcs.py"
    functions_file.write_text("def triple(x):\n    return x * 3")

    result = CliRunner().invoke(
        cli.cli,
        [
            db_path,
            "select triple(2), quadruple(2)",
            "--functions",
            str(functions_file),
            "--functions",
            "def quadruple(x):\n    return x * 4",
        ],
    )
    assert result.exit_code == 0
    assert json.loads(result.output.strip()) == [{"triple(2)": 6, "quadruple(2)": 8}]


LOREM_IPSUM_COMPRESSED = (
    b"x\x9c\xed\xd1\xcdq\x03!\x0c\x05\xe0\xbb\xabP\x01\x1eW\x91\xdc|M\x01\n\xc8\x8e"
    b"f\xf83H\x1e\x97\x1f\x91M\x8e\xe9\xe0\xdd\x96\x05\x84\xf4\xbek\x9fRI\xc7\xf2J"
    b"\xb9\x97>i\xa9\x11W\xb13\xa5\xde\x96$\x13\xf3I\x9cu\xe8J\xda\xee$EcsI\x8e\x0b"
    b"$\xea\xab\xf6L&u\xc4emI\xb3foFnT\xf83\xca\x93\xd8QZ\xa8\xf2\xbd1q\xd1\x87\xf3"
    b"\x85>\x8c\xa4i\x8d\xdaTu\x7f<c\xc9\xf5L\x0f\xd7E\xad/\x9b\x9eI^2\x93\x1a\x9b"
    b"\xf6F^\n\xd7\xd4\x8f\xca\xfb\x90.\xdd/\xfd\x94\xd4\x11\x87I8\x1a\xaf\xd1S?\x06"
    b"\x88\xa7\xecBo\xbb$\xbb\t\xe9\xf4\xe8\xe4\x98U\x1bM\x19S\xbe\xa4e\x991x\xfc"
    b"x\xf6\xe2#\x9e\x93h'&%YK(i)\x7f\t\xc5@N7\xbf+\x1b\xb5\xdd\x10\r\x9e\xb1\xf0"
    b"y\xa1\xf7W\x92a\xe2;\xc6\xc8\xa0\xa7\xc4\x92\xe2\\\xf2\xa1\x99m\xdf\x88)\xc6"
    b"\xec\x9a\xa5\xed\x14wR\xf1h\xf22x\xcfM\xfdv\xd3\xa4LY\x96\xcc\xbd[{\xd9m\xf0"
    b"\x0eH#\x8e\xf5\x9b\xab\xd7\xcb\xe9t\x05\x1f\xf8\xc0\x07>\xf0\x81\x0f|\xe0\x03"
    b"\x1f\xf8\xc0\x07>\xf0\x81\x0f|\xe0\x03\x1f\xf8\xc0\x07>\xf0\x81\x0f|\xe0\x03"
    b"\x1f\xf8\xc0\x07>\xf0\x81\x0f|\xe0\x03\x1f\xf8\xc0\x07>\xf0\x81\x0f|\xe0\x03"
    b"\x1f\xf8\xc0\x07>\xf0\x81\x0f|\xe0\x03\x1f\xf8\xc0\x07>\xf0\x81\x0f|\xe0\x03"
    b"\x1f\xf8\xc0\x07>\xf0\x81\x0f|\xe0\xfb\x8f\xef\x1b\x9b\x06\x83}"
)


def test_query_json_binary(db_path):
    db = Database(db_path)
    with db.conn:
        db.table("files").insert(
            {
                "name": "lorem.txt",
                "sz": 16984,
                "data": LOREM_IPSUM_COMPRESSED,
            },
            pk="name",
        )
    result = CliRunner().invoke(cli.cli, [db_path, "select name, sz, data from files"])
    assert result.exit_code == 0, str(result)
    assert json.loads(result.output.strip()) == [
        {
            "name": "lorem.txt",
            "sz": 16984,
            "data": {
                "$base64": True,
                "encoded": (
                    "eJzt0c1xAyEMBeC7q1ABHleR3HxNAQrIjmb4M0gelx+RTY7p4N2WBYT0vmufUknH"
                    "8kq5lz5pqRFXsTOl3pYkE/NJnHXoStruJEVjc0mOCyTqq/ZMJnXEZW1Js2ZvRm5U+"
                    "DPKk9hRWqjyvTFx0YfzhT6MpGmN2lR1fzxjyfVMD9dFrS+bnkleMpMam/ZGXgrX1I"
                    "/K+5Au3S/9lNQRh0k4Gq/RUz8GiKfsQm+7JLsJ6fTo5JhVG00ZU76kZZkxePx49uI"
                    "jnpNoJyYlWUsoaSl/CcVATje/Kxu13RANnrHweaH3V5Jh4jvGyKCnxJLiXPKhmW3f"
                    "iCnG7Jql7RR3UvFo8jJ4z039dtOkTFmWzL1be9lt8A5II471m6vXy+l0BR/4wAc+8"
                    "IEPfOADH/jABz7wgQ984AMf+MAHPvCBD3zgAx/4wAc+8IEPfOADH/jABz7wgQ984A"
                    "Mf+MAHPvCBD3zgAx/4wAc+8IEPfOADH/jABz7wgQ984PuP7xubBoN9"
                ),
            },
        }
    ]


@pytest.mark.parametrize(
    "sql,params,expected",
    [
        ("select 1 + 1 as out", {"p": "2"}, 2),
        ("select 1 + :p as out", {"p": "2"}, 3),
        (
            "select :hello as out",
            {"hello": """This"has'many'quote"s"""},
            """This"has'many'quote"s""",
        ),
    ],
)
def test_query_params(db_path, sql, params, expected):
    extra_args = []
    for key, value in params.items():
        extra_args.extend(["-p", key, value])
    result = CliRunner().invoke(cli.cli, [db_path, sql] + extra_args)
    assert result.exit_code == 0, str(result)
    assert json.loads(result.output.strip()) == [{"out": expected}]


def test_query_json_with_json_cols(db_path):
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert(
            {
                "id": 1,
                "name": "Cleo",
                "friends": [{"name": "Pancakes"}, {"name": "Bailey"}],
            }
        )
    result = CliRunner().invoke(
        cli.cli, [db_path, "select id, name, friends from dogs"]
    )
    assert r"""
    [{"id": 1, "name": "Cleo", "friends": "[{\"name\": \"Pancakes\"}, {\"name\": \"Bailey\"}]"}]
    """.strip() == result.output.strip()
    # With --json-cols:
    result = CliRunner().invoke(
        cli.cli, [db_path, "select id, name, friends from dogs", "--json-cols"]
    )
    expected = r"""
    [{"id": 1, "name": "Cleo", "friends": [{"name": "Pancakes"}, {"name": "Bailey"}]}]
    """.strip()
    assert expected == result.output.strip()
    # Test rows command too
    result_rows = CliRunner().invoke(cli.cli, ["rows", db_path, "dogs", "--json-cols"])
    assert expected == result_rows.output.strip()


def test_query_json_unicode_not_escaped_by_default(db_path):
    db = Database(db_path)
    with db.conn:
        db.table("text").insert({"id": 1, "text": "Japanese 日本語"}, pk="id")
    result = CliRunner().invoke(cli.cli, [db_path, "select id, text from text"])
    assert result.exit_code == 0
    assert result.output.strip() == '[{"id": 1, "text": "Japanese 日本語"}]'
    # Same for --nl
    result = CliRunner().invoke(cli.cli, [db_path, "select id, text from text", "--nl"])
    assert result.exit_code == 0
    assert result.output.strip() == '{"id": 1, "text": "Japanese 日本語"}'


@pytest.mark.parametrize("command", ["query", "rows"])
def test_query_json_ascii_option(db_path, command):
    db = Database(db_path)
    with db.conn:
        db.table("text").insert({"id": 1, "text": "Japanese 日本語"}, pk="id")
    if command == "query":
        args = [db_path, "select id, text from text", "--ascii"]
    else:
        args = ["rows", db_path, "text", "--ascii"]
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 0
    expected = '[{"id": 1, "text": "Japanese ' + "\\u65e5\\u672c\\u8a9e" + '"}]'
    assert result.output.strip() == expected


@pytest.mark.parametrize(
    "content,is_binary",
    [(b"\x00\x0fbinary", True), ("this is text", False), (1, False), (1.5, False)],
)
def test_query_raw(db_path, content, is_binary):
    Database(db_path).table("files").insert({"content": content})
    result = CliRunner().invoke(
        cli.cli, [db_path, "select content from files", "--raw"]
    )
    if is_binary:
        assert result.stdout_bytes == content
    else:
        assert result.output == str(content)


@pytest.mark.parametrize(
    "content,is_binary",
    [(b"\x00\x0fbinary", True), ("this is text", False), (1, False), (1.5, False)],
)
def test_query_raw_lines(db_path, content, is_binary):
    Database(db_path).table("files").insert_all({"content": content} for _ in range(3))
    result = CliRunner().invoke(
        cli.cli, [db_path, "select content from files", "--raw-lines"]
    )
    if is_binary:
        assert result.stdout_bytes == b"\n".join(content for _ in range(3)) + b"\n"
    else:
        assert result.output == "\n".join(str(content) for _ in range(3)) + "\n"


def test_query_memory_does_not_create_file(tmpdir):
    owd = os.getcwd()
    try:
        os.chdir(tmpdir)
        # This should create a foo.db file
        CliRunner().invoke(cli.cli, ["foo.db", "select sqlite_version()"])
        # This should NOT create a file
        result = CliRunner().invoke(cli.cli, [":memory:", "select sqlite_version()"])
        assert ["sqlite_version()"] == list(json.loads(result.output)[0].keys())
    finally:
        os.chdir(owd)
    assert ["foo.db"] == os.listdir(tmpdir)


@pytest.mark.parametrize(
    "args,expected",
    [
        (
            [],
            '[{"id": 1, "name": "Cleo", "age": 4},\n {"id": 2, "name": "Pancakes", "age": 2}]',
        ),
        (
            ["--nl"],
            '{"id": 1, "name": "Cleo", "age": 4}\n{"id": 2, "name": "Pancakes", "age": 2}',
        ),
        (["--arrays"], '[[1, "Cleo", 4],\n [2, "Pancakes", 2]]'),
        (["--arrays", "--nl"], '[1, "Cleo", 4]\n[2, "Pancakes", 2]'),
        (
            ["--nl", "-c", "age", "-c", "name"],
            '{"age": 4, "name": "Cleo"}\n{"age": 2, "name": "Pancakes"}',
        ),
        # --limit and --offset
        (
            ["-c", "name", "--limit", "1"],
            '[{"name": "Cleo"}]',
        ),
        (
            ["-c", "name", "--limit", "1", "--offset", "1"],
            '[{"name": "Pancakes"}]',
        ),
        # --offset without --limit
        (
            ["-c", "name", "--offset", "1"],
            '[{"name": "Pancakes"}]',
        ),
        # --where
        (
            ["-c", "name", "--where", "id = 1"],
            '[{"name": "Cleo"}]',
        ),
        (
            ["-c", "name", "--where", "id = :id", "-p", "id", "1"],
            '[{"name": "Cleo"}]',
        ),
        (
            ["-c", "name", "--where", "id = :id", "--param", "id", "1"],
            '[{"name": "Cleo"}]',
        ),
        # --order
        (
            ["-c", "id", "--order", "id desc", "--limit", "1"],
            '[{"id": 2}]',
        ),
        (
            ["-c", "id", "--order", "id", "--limit", "1"],
            '[{"id": 1}]',
        ),
    ],
)
def test_rows(db_path, args, expected):
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert_all(
            [
                {"id": 1, "age": 4, "name": "Cleo"},
                {"id": 2, "age": 2, "name": "Pancakes"},
            ],
            column_order=["id", "name", "age"],
        )
    result = CliRunner().invoke(cli.cli, ["rows", db_path, "dogs"] + args)
    assert expected == result.output.strip()


def test_upsert(db_path, tmpdir):
    json_path = str(tmpdir / "dogs.json")
    db = Database(db_path)
    insert_dogs = [
        {"id": 1, "name": "Cleo", "age": 4},
        {"id": 2, "name": "Nixie", "age": 4},
    ]
    write_json(json_path, insert_dogs)
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "dogs", json_path, "--pk", "id"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    assert 2 == db.table("dogs").count
    # Now run the upsert to update just their ages
    upsert_dogs = [
        {"id": 1, "age": 5},
        {"id": 2, "age": 5},
    ]
    write_json(json_path, upsert_dogs)
    result = CliRunner().invoke(
        cli.cli,
        ["upsert", db_path, "dogs", json_path, "--pk", "id"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    assert list(db.query("select * from dogs order by id")) == [
        {"id": 1, "name": "Cleo", "age": 5},
        {"id": 2, "name": "Nixie", "age": 5},
    ]


def test_upsert_pk_inferred_from_existing_table(db_path, tmpdir):
    json_path = str(tmpdir / "dogs.json")
    db = Database(db_path)
    insert_dogs = [
        {"id": 1, "name": "Cleo", "age": 4},
        {"id": 2, "name": "Nixie", "age": 4},
    ]
    write_json(json_path, insert_dogs)
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "dogs", json_path, "--pk", "id"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output

    write_json(
        json_path,
        [
            {"id": 1, "age": 5},
            {"id": 2, "age": 5},
        ],
    )
    result = CliRunner().invoke(
        cli.cli,
        ["upsert", db_path, "dogs", json_path],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    assert list(db.query("select * from dogs order by id")) == [
        {"id": 1, "name": "Cleo", "age": 5},
        {"id": 2, "name": "Nixie", "age": 5},
    ]


def test_upsert_analyze(db_path, tmpdir):
    db = Database(db_path)
    db.table("rows").insert({"id": 1, "foo": "x", "n": 3}, pk="id")
    db.table("rows").create_index(["n"])
    assert "sqlite_stat1" not in db.table_names()
    result = CliRunner().invoke(
        cli.cli,
        ["upsert", db_path, "rows", "-", "--nl", "--analyze", "--pk", "id"],
        input='{"id": 2, "foo": "bar", "n": 1}',
    )
    assert result.exit_code == 0, result.output
    assert "sqlite_stat1" in db.table_names()


def test_upsert_flatten(tmpdir):
    db_path = str(tmpdir / "flat.db")
    db = Database(db_path)
    db.table("upsert_me").insert({"id": 1, "name": "Example"}, pk="id")
    result = CliRunner().invoke(
        cli.cli,
        ["upsert", db_path, "upsert_me", "-", "--flatten", "--pk", "id", "--alter"],
        input=json.dumps({"id": 1, "nested": {"two": 2}}),
    )
    assert result.exit_code == 0
    assert list(db.query("select * from upsert_me")) == [
        {"id": 1, "name": "Example", "nested_two": 2}
    ]


def test_upsert_alter(db_path, tmpdir):
    json_path = str(tmpdir / "dogs.json")
    db = Database(db_path)
    insert_dogs = [{"id": 1, "name": "Cleo"}]
    write_json(json_path, insert_dogs)
    result = CliRunner().invoke(
        cli.cli, ["insert", db_path, "dogs", json_path, "--pk", "id"]
    )
    assert result.exit_code == 0, result.output
    # Should fail with error code if no --alter
    upsert_dogs = [{"id": 1, "age": 5}]
    write_json(json_path, upsert_dogs)
    result = CliRunner().invoke(
        cli.cli, ["upsert", db_path, "dogs", json_path, "--pk", "id"]
    )
    assert result.exit_code == 1
    # Could be one of two errors depending on SQLite version
    assert ("Try using --alter to add additional columns") in result.output.strip()
    # Should succeed with --alter
    result = CliRunner().invoke(
        cli.cli, ["upsert", db_path, "dogs", json_path, "--pk", "id", "--alter"]
    )
    assert result.exit_code == 0
    assert list(db.query("select * from dogs order by id")) == [
        {"id": 1, "name": "Cleo", "age": 5},
    ]


@pytest.mark.parametrize(
    "args,schema",
    [
        # No primary key
        (
            [
                "name",
                "text",
                "age",
                "integer",
            ],
            ('CREATE TABLE "t" (\n   "name" TEXT,\n   "age" INTEGER\n)'),
        ),
        # All types:
        (
            [
                "id",
                "integer",
                "name",
                "text",
                "age",
                "integer",
                "weight",
                "float",
                "thumbnail",
                "blob",
                "--pk",
                "id",
            ],
            (
                'CREATE TABLE "t" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "name" TEXT,\n'
                '   "age" INTEGER,\n'
                '   "weight" FLOAT,\n'
                '   "thumbnail" BLOB\n'
                ")"
            ),
        ),
        # Not null:
        (
            ["name", "text", "--not-null", "name"],
            ('CREATE TABLE "t" (\n' '   "name" TEXT NOT NULL\n' ")"),
        ),
        # Default:
        (
            ["age", "integer", "--default", "age", "3"],
            ('CREATE TABLE "t" (\n' "   \"age\" INTEGER DEFAULT '3'\n" ")"),
        ),
        # Compound primary key
        (
            ["category", "text", "name", "text", "--pk", "category", "--pk", "name"],
            (
                'CREATE TABLE "t" (\n   "category" TEXT,\n   "name" TEXT,\n'
                '   PRIMARY KEY ("category", "name")\n)'
            ),
        ),
    ],
)
def test_create_table(args, schema):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli.cli,
            [
                "create-table",
                "test.db",
                "t",
            ]
            + args,
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        db = Database("test.db")
        assert schema == db.table("t").schema


def test_create_table_foreign_key():
    runner = CliRunner()
    creates = (
        ["authors", "id", "integer", "name", "text", "--pk", "id"],
        [
            "books",
            "id",
            "integer",
            "title",
            "text",
            "author_id",
            "integer",
            "--pk",
            "id",
            "--fk",
            "author_id",
            "authors",
            "id",
        ],
    )
    with runner.isolated_filesystem():
        for args in creates:
            result = runner.invoke(
                cli.cli, ["create-table", "books.db"] + args, catch_exceptions=False
            )
            assert result.exit_code == 0
        db = Database("books.db")
        assert (
            'CREATE TABLE "authors" (\n'
            '   "id" INTEGER PRIMARY KEY,\n'
            '   "name" TEXT\n'
            ")"
        ) == db.table("authors").schema
        assert (
            'CREATE TABLE "books" (\n'
            '   "id" INTEGER PRIMARY KEY,\n'
            '   "title" TEXT,\n'
            '   "author_id" INTEGER REFERENCES "authors"("id")\n'
            ")"
        ) == db.table("books").schema


def test_create_table_error_if_table_exists():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.table("dogs").insert({"name": "Cleo"})
        result = runner.invoke(
            cli.cli, ["create-table", "test.db", "dogs", "id", "integer"]
        )
        assert result.exit_code == 1
        assert (
            'Error: Table "dogs" already exists. Use --replace to delete and replace it.'
            == result.output.strip()
        )


def test_create_table_ignore():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.table("dogs").insert({"name": "Cleo"})
        result = runner.invoke(
            cli.cli, ["create-table", "test.db", "dogs", "id", "integer", "--ignore"]
        )
        assert result.exit_code == 0
        assert 'CREATE TABLE "dogs" (\n   "name" TEXT\n)' == db.table("dogs").schema


def test_create_table_replace():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.table("dogs").insert({"name": "Cleo"})
        result = runner.invoke(
            cli.cli, ["create-table", "test.db", "dogs", "id", "integer", "--replace"]
        )
        assert result.exit_code == 0
        assert 'CREATE TABLE "dogs" (\n   "id" INTEGER\n)' == db.table("dogs").schema


def test_create_view():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        result = runner.invoke(
            cli.cli, ["create-view", "test.db", "version", "select sqlite_version()"]
        )
        assert result.exit_code == 0
        assert (
            'CREATE VIEW "version" AS select sqlite_version()'
            == db.view("version").schema
        )


def test_create_view_error_if_view_exists():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.create_view("version", "select sqlite_version() + 1")
        result = runner.invoke(
            cli.cli, ["create-view", "test.db", "version", "select sqlite_version()"]
        )
        assert result.exit_code == 1
        assert (
            'Error: View "version" already exists. Use --replace to delete and replace it.'
            == result.output.strip()
        )


def test_create_view_ignore():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.create_view("version", "select sqlite_version() + 1")
        result = runner.invoke(
            cli.cli,
            [
                "create-view",
                "test.db",
                "version",
                "select sqlite_version()",
                "--ignore",
            ],
        )
        assert result.exit_code == 0
        assert (
            'CREATE VIEW "version" AS select sqlite_version() + 1'
            == db.view("version").schema
        )


def test_create_view_replace():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.create_view("version", "select sqlite_version() + 1")
        result = runner.invoke(
            cli.cli,
            [
                "create-view",
                "test.db",
                "version",
                "select sqlite_version()",
                "--replace",
            ],
        )
        assert result.exit_code == 0
        assert (
            'CREATE VIEW "version" AS select sqlite_version()'
            == db.view("version").schema
        )


def test_drop_table():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.table("t").create({"pk": int}, pk="pk")
        assert "t" in db.table_names()
        result = runner.invoke(
            cli.cli,
            [
                "drop-table",
                "test.db",
                "t",
            ],
        )
        assert result.exit_code == 0
        assert "t" not in db.table_names()


def test_drop_table_error():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.table("t").create({"pk": int}, pk="pk")
        result = runner.invoke(
            cli.cli,
            [
                "drop-table",
                "test.db",
                "t2",
            ],
        )
        assert result.exit_code == 1
        assert 'Error: Table "t2" does not exist' == result.output.strip()
        # Using --ignore suppresses that error
        result = runner.invoke(
            cli.cli,
            ["drop-table", "test.db", "t2", "--ignore"],
        )
        assert result.exit_code == 0


def test_drop_table_on_view_errors():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.table("t").insert({"id": 1})
        db.create_view("v", "select * from t")
        result = runner.invoke(cli.cli, ["drop-table", "test.db", "v"])
        assert result.exit_code == 1
        assert 'Error: "v" is a view, not a table - use drop-view to drop it' == (
            result.output.strip()
        )
        assert "v" in db.view_names()
        # --ignore exits cleanly but must still not drop the view
        result = runner.invoke(cli.cli, ["drop-table", "test.db", "v", "--ignore"])
        assert result.exit_code == 0
        assert "v" in db.view_names()


def test_drop_view():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.create_view("hello", "select 1")
        assert "hello" in db.view_names()
        result = runner.invoke(
            cli.cli,
            [
                "drop-view",
                "test.db",
                "hello",
            ],
        )
        assert result.exit_code == 0
        assert "hello" not in db.view_names()


def test_drop_view_on_table_errors():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.table("t").insert({"id": 1})
        result = runner.invoke(cli.cli, ["drop-view", "test.db", "t"])
        assert result.exit_code == 1
        assert 'Error: "t" is a table, not a view - use drop-table to drop it' == (
            result.output.strip()
        )
        assert "t" in db.table_names()
        # --ignore exits cleanly but must still not drop the table
        result = runner.invoke(cli.cli, ["drop-view", "test.db", "t", "--ignore"])
        assert result.exit_code == 0
        assert "t" in db.table_names()


def test_drop_view_error():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        db.table("t").create({"pk": int}, pk="pk")
        result = runner.invoke(
            cli.cli,
            [
                "drop-view",
                "test.db",
                "t2",
            ],
        )
        assert result.exit_code == 1
        assert 'Error: View "t2" does not exist' == result.output.strip()
        # Using --ignore suppresses that error
        result = runner.invoke(
            cli.cli,
            ["drop-view", "test.db", "t2", "--ignore"],
        )
        assert result.exit_code == 0


def test_enable_wal():
    runner = CliRunner()
    dbs = ["test.db", "test2.db"]
    with runner.isolated_filesystem():
        for dbname in dbs:
            db = Database(dbname)
            db.table("t").create({"pk": int}, pk="pk")
            assert db.journal_mode == "delete"
        result = runner.invoke(cli.cli, ["enable-wal"] + dbs, catch_exceptions=False)
        assert result.exit_code == 0
        for dbname in dbs:
            db = Database(dbname)
            assert db.journal_mode == "wal"


def test_disable_wal():
    runner = CliRunner()
    dbs = ["test.db", "test2.db"]
    with runner.isolated_filesystem():
        for dbname in dbs:
            db = Database(dbname)
            db.table("t").create({"pk": int}, pk="pk")
            db.enable_wal()
            assert db.journal_mode == "wal"
        result = runner.invoke(cli.cli, ["disable-wal"] + dbs)
        assert result.exit_code == 0
        for dbname in dbs:
            db = Database(dbname)
            assert db.journal_mode == "delete"


@pytest.mark.parametrize(
    "args,expected",
    [
        (
            [],
            '[{"rows_affected": 1}]',
        ),
        (["-t"], "rows_affected\n---------------\n              1"),
    ],
)
def test_query_update(db_path, args, expected):
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert_all(
            [
                {"id": 1, "age": 4, "name": "Cleo"},
            ]
        )
    result = CliRunner().invoke(
        cli.cli, [db_path, "update dogs set age = 5 where name = 'Cleo'"] + args
    )
    assert expected == result.output.strip()
    assert list(db.query("select * from dogs")) == [
        {"id": 1, "age": 5, "name": "Cleo"},
    ]


def test_add_foreign_keys(db_path):
    db = Database(db_path)
    db.table("countries").insert({"id": 7, "name": "Panama"}, pk="id")
    db.table("authors").insert({"id": 3, "name": "Matilda", "country_id": 7}, pk="id")
    db.table("books").insert(
        {"id": 2, "title": "Wolf anatomy", "author_id": 3}, pk="id"
    )
    assert db.table("authors").foreign_keys == []
    assert db.table("books").foreign_keys == []
    result = CliRunner().invoke(
        cli.cli,
        [
            "add-foreign-keys",
            db_path,
            "authors",
            "country_id",
            "countries",
            "id",
            "books",
            "author_id",
            "authors",
            "id",
        ],
    )
    assert result.exit_code == 0
    assert db.table("authors").foreign_keys == [
        ForeignKey(
            table="authors",
            column="country_id",
            other_table="countries",
            other_column="id",
        )
    ]
    assert db.table("books").foreign_keys == [
        ForeignKey(
            table="books", column="author_id", other_table="authors", other_column="id"
        )
    ]


@pytest.mark.parametrize(
    "args,expected_schema",
    [
        (
            [],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                "   \"age\" INTEGER NOT NULL DEFAULT '1',\n"
                '   "name" TEXT\n'
                ")"
            ),
        ),
        (
            ["--type", "age", "text"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                "   \"age\" TEXT NOT NULL DEFAULT '1',\n"
                '   "name" TEXT\n'
                ")"
            ),
        ),
        (
            ["--drop", "age"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "name" TEXT\n'
                ")"
            ),
        ),
        (
            ["--rename", "age", "age2", "--rename", "id", "pk"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "pk" INTEGER PRIMARY KEY,\n'
                "   \"age2\" INTEGER NOT NULL DEFAULT '1',\n"
                '   "name" TEXT\n'
                ")"
            ),
        ),
        (
            ["--not-null", "name"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                "   \"age\" INTEGER NOT NULL DEFAULT '1',\n"
                '   "name" TEXT NOT NULL\n'
                ")"
            ),
        ),
        (
            ["--not-null-false", "age"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                "   \"age\" INTEGER DEFAULT '1',\n"
                '   "name" TEXT\n'
                ")"
            ),
        ),
        (
            ["--pk", "name"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER,\n'
                "   \"age\" INTEGER NOT NULL DEFAULT '1',\n"
                '   "name" TEXT PRIMARY KEY\n'
                ")"
            ),
        ),
        (
            ["--pk-none"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER,\n'
                "   \"age\" INTEGER NOT NULL DEFAULT '1',\n"
                '   "name" TEXT\n'
                ")"
            ),
        ),
        (
            ["--default", "name", "Turnip"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                "   \"age\" INTEGER NOT NULL DEFAULT '1',\n"
                "   \"name\" TEXT DEFAULT 'Turnip'\n"
                ")"
            ),
        ),
        (
            ["--default-none", "age"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "age" INTEGER NOT NULL,\n'
                '   "name" TEXT\n'
                ")"
            ),
        ),
        (
            ["-o", "name", "--column-order", "age", "-o", "id"],
            (
                'CREATE TABLE "dogs" (\n'
                '   "name" TEXT,\n'
                "   \"age\" INTEGER NOT NULL DEFAULT '1',\n"
                '   "id" INTEGER PRIMARY KEY\n'
                ")"
            ),
        ),
    ],
)
def test_transform(db_path, args, expected_schema):
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert(
            {"id": 1, "age": 4, "name": "Cleo"},
            not_null={"age"},
            defaults={"age": 1},
            pk="id",
        )
    result = CliRunner().invoke(cli.cli, ["transform", db_path, "dogs"] + args)
    print(result.output)
    assert result.exit_code == 0
    schema = db.table("dogs").schema
    assert schema == expected_schema


def test_transform_sql(db_path):
    db = Database(db_path)
    with db.conn:
        db.table("dogs").insert(
            {"id": 1, "age": 4, "name": "Cleo"},
            not_null={"age"},
            defaults={"age": 1},
            pk="id",
        )
    original_schema = db.table("dogs").schema

    result = CliRunner().invoke(
        cli.cli, ["transform", db_path, "dogs", "--drop", "name", "--sql"]
    )

    assert result.exit_code == 0, result.output
    assert 'CREATE TABLE "dogs_new_' in result.output
    assert '"age" INTEGER NOT NULL DEFAULT' in result.output
    assert 'DROP TABLE "dogs";' in result.output
    assert 'ALTER TABLE "dogs_new_' in result.output
    assert db.table("dogs").schema == original_schema


@pytest.mark.parametrize(
    "initial_strict,args,expected_strict",
    (
        (False, [], False),
        (True, [], True),
        (False, ["--strict"], True),
        (True, ["--no-strict"], False),
    ),
)
def test_transform_strict_option(db_path, initial_strict, args, expected_strict):
    db = Database(db_path)
    if not db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    db.table("dogs").create({"id": int}, strict=initial_strict)

    result = CliRunner().invoke(cli.cli, ["transform", db_path, "dogs"] + args)

    assert result.exit_code == 0, result.output
    assert db.table("dogs").strict is expected_strict


@pytest.mark.parametrize(
    "initial_strict,flag,sql_is_strict",
    (
        (False, "--strict", True),
        (True, "--no-strict", False),
    ),
)
def test_transform_strict_option_sql(db_path, initial_strict, flag, sql_is_strict):
    db = Database(db_path)
    if not db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    db.table("dogs").create({"id": int}, strict=initial_strict)

    result = CliRunner().invoke(cli.cli, ["transform", db_path, "dogs", flag, "--sql"])

    assert result.exit_code == 0, result.output
    assert (") STRICT;" in result.output) is sql_is_strict
    assert db.table("dogs").strict is initial_strict


def test_transform_strict_option_with_invalid_data(db_path):
    db = Database(db_path)
    if not db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    dogs = db.table("dogs")
    dogs.create({"id": int})
    dogs.insert({"id": "not-an-integer"})

    result = CliRunner().invoke(cli.cli, ["transform", db_path, "dogs", "--strict"])

    assert result.exit_code == 1
    assert isinstance(result.exception, sqlite3.IntegrityError)
    assert dogs.strict is False
    assert list(dogs.rows) == [{"id": "not-an-integer"}]
    assert not any(name.startswith("dogs_new_") for name in db.table_names())


def test_transform_column_to_any(db_path):
    db = Database(db_path)
    if not db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    db.table("items").create({"data": str}, strict=True)
    db.table("items").insert({"data": "000123"})

    result = CliRunner().invoke(
        cli.cli, ["transform", db_path, "items", "--type", "data", "any"]
    )

    assert result.exit_code == 0, result.output
    assert db.table("items").columns_dict == {"data": ANY}
    assert db.execute("select typeof(data), data from items").fetchone() == (
        "text",
        "000123",
    )


@pytest.mark.parametrize(
    "extra_args,expected_schema",
    (
        (
            ["--drop-foreign-key", "country"],
            (
                'CREATE TABLE "places" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "name" TEXT,\n'
                '   "country" INTEGER,\n'
                '   "city" INTEGER REFERENCES "city"("id"),\n'
                '   "continent" INTEGER\n'
                ")"
            ),
        ),
        (
            ["--drop-foreign-key", "country", "--drop-foreign-key", "city"],
            (
                'CREATE TABLE "places" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "name" TEXT,\n'
                '   "country" INTEGER,\n'
                '   "city" INTEGER,\n'
                '   "continent" INTEGER\n'
                ")"
            ),
        ),
        (
            ["--add-foreign-key", "continent", "continent", "id"],
            (
                'CREATE TABLE "places" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "name" TEXT,\n'
                '   "country" INTEGER REFERENCES "country"("id"),\n'
                '   "city" INTEGER REFERENCES "city"("id"),\n'
                '   "continent" INTEGER REFERENCES "continent"("id")\n'
                ")"
            ),
        ),
    ),
)
def test_transform_add_or_drop_foreign_key(db_path, extra_args, expected_schema):
    db = Database(db_path)
    with db.conn:
        # Create table with three foreign keys so we can drop two of them
        db.table("continent").insert({"id": 1, "name": "Europe"}, pk="id")
        db.table("country").insert({"id": 1, "name": "France"}, pk="id")
        db.table("city").insert({"id": 24, "name": "Paris"}, pk="id")
        db.table("places").insert(
            {
                "id": 32,
                "name": "Caveau de la Huchette",
                "country": 1,
                "city": 24,
                "continent": 1,
            },
            foreign_keys=("country", "city"),
            pk="id",
        )
    result = CliRunner().invoke(
        cli.cli,
        [
            "transform",
            db_path,
            "places",
        ]
        + extra_args,
    )
    assert result.exit_code == 0
    schema = db.table("places").schema
    assert schema == expected_schema


_common_other_schema = (
    'CREATE TABLE "species" (\n   "id" INTEGER PRIMARY KEY,\n   "species" TEXT\n)'
)


@pytest.mark.parametrize(
    "args,expected_table_schema,expected_other_schema",
    [
        (
            [],
            (
                'CREATE TABLE "trees" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "address" TEXT,\n'
                '   "species_id" INTEGER REFERENCES "species"("id")\n'
                ")"
            ),
            _common_other_schema,
        ),
        (
            ["--table", "custom_table"],
            (
                'CREATE TABLE "trees" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "address" TEXT,\n'
                '   "custom_table_id" INTEGER REFERENCES "custom_table"("id")\n'
                ")"
            ),
            'CREATE TABLE "custom_table" (\n   "id" INTEGER PRIMARY KEY,\n   "species" TEXT\n)',
        ),
        (
            ["--fk-column", "custom_fk"],
            (
                'CREATE TABLE "trees" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "address" TEXT,\n'
                '   "custom_fk" INTEGER REFERENCES "species"("id")\n'
                ")"
            ),
            _common_other_schema,
        ),
        (
            ["--rename", "name", "name2"],
            (
                'CREATE TABLE "trees" (\n'
                '   "id" INTEGER PRIMARY KEY,\n'
                '   "address" TEXT,\n'
                '   "species_id" INTEGER REFERENCES "species"("id")\n'
                ")"
            ),
            'CREATE TABLE "species" (\n   "id" INTEGER PRIMARY KEY,\n   "species" TEXT\n)',
        ),
    ],
)
def test_extract(db_path, args, expected_table_schema, expected_other_schema):
    db = Database(db_path)
    with db.conn:
        db.table("trees").insert(
            {"id": 1, "address": "4 Park Ave", "species": "Palm"},
            pk="id",
        )
    result = CliRunner().invoke(
        cli.cli, ["extract", db_path, "trees", "species"] + args
    )
    print(result.output)
    assert result.exit_code == 0
    schema = db.table("trees").schema
    assert schema == expected_table_schema
    other_schema = next(
        t for t in db.tables if t.name not in ("trees", "Gosh", "Gosh2")
    ).schema
    assert other_schema == expected_other_schema


def test_insert_encoding(tmpdir):
    db_path = str(tmpdir / "test.db")
    latin1_csv = (
        b"date,name,latitude,longitude\n"
        b"2020-01-01,Barra da Lagoa,-27.574,-48.422\n"
        b"2020-03-04,S\xe3o Paulo,-23.561,-46.645\n"
        b"2020-04-05,Salta,-24.793:-65.408"
    )
    assert latin1_csv.decode("latin-1").split("\n")[2].split(",")[1] == "São Paulo"
    csv_path = str(tmpdir / "test.csv")
    with open(csv_path, "wb") as fp:
        fp.write(latin1_csv)
    # First attempt should error:
    bad_result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "places", csv_path, "--csv"],
        catch_exceptions=False,
    )
    assert bad_result.exit_code == 1
    assert (
        "The input you provided uses a character encoding other than utf-8"
        in bad_result.output
    )
    # Using --encoding=latin-1 should work
    good_result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "places",
            csv_path,
            "--encoding",
            "latin-1",
            "--csv",
            "--no-detect-types",
        ],
        catch_exceptions=False,
    )
    assert good_result.exit_code == 0
    db = Database(db_path)
    assert list(db.table("places").rows) == [
        {
            "date": "2020-01-01",
            "name": "Barra da Lagoa",
            "latitude": "-27.574",
            "longitude": "-48.422",
        },
        {
            "date": "2020-03-04",
            "name": "São Paulo",
            "latitude": "-23.561",
            "longitude": "-46.645",
        },
        {
            "date": "2020-04-05",
            "name": "Salta",
            "latitude": "-24.793:-65.408",
            "longitude": None,
        },
    ]


@pytest.mark.parametrize("fts", ["FTS4", "FTS5"])
@pytest.mark.parametrize(
    "extra_arg,expected",
    [
        (
            None,
            '[{"rowid": 2, "id": 2, "title": "Title the second"}]\n',
        ),
        ("--csv", "rowid,id,title\n2,2,Title the second\n"),
    ],
)
def test_search(tmpdir, fts, extra_arg, expected):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("articles").insert_all(
        [
            {"id": 1, "title": "Title the first"},
            {"id": 2, "title": "Title the second"},
            {"id": 3, "title": "Title the third"},
        ],
        pk="id",
    )
    db.table("articles").enable_fts(["title"], fts_version=fts)
    result = CliRunner().invoke(
        cli.cli,
        ["search", db_path, "articles", "second"] + ([extra_arg] if extra_arg else []),
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert result.output.replace("\r", "") == expected


def test_search_quote(tmpdir):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("creatures").insert({"name": "dog."}).enable_fts(["name"])
    # Without --quote should return an error
    error_result = CliRunner().invoke(cli.cli, ["search", db_path, "creatures", 'dog"'])
    assert error_result.exit_code == 1
    assert error_result.output == (
        "Error: unterminated string\n\n"
        "Try running this again with the --quote option\n"
    )
    # With --quote it should work
    result = CliRunner().invoke(
        cli.cli, ["search", db_path, "creatures", 'dog"', "--quote"]
    )
    assert result.exit_code == 0
    assert result.output.strip() == '[{"rowid": 1, "name": "dog."}]'


def test_indexes(tmpdir):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.conn.executescript("""
        create table Gosh (c1 text, c2 text, c3 text);
        create index Gosh_idx on Gosh(c2, c3 desc);
    """)
    result = CliRunner().invoke(
        cli.cli,
        ["indexes", str(db_path)],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert json.loads(result.output) == [
        {
            "table": "Gosh",
            "index_name": "Gosh_idx",
            "seqno": 0,
            "cid": 1,
            "name": "c2",
            "desc": 0,
            "coll": "BINARY",
            "key": 1,
        },
        {
            "table": "Gosh",
            "index_name": "Gosh_idx",
            "seqno": 1,
            "cid": 2,
            "name": "c3",
            "desc": 1,
            "coll": "BINARY",
            "key": 1,
        },
    ]
    result2 = CliRunner().invoke(
        cli.cli,
        ["indexes", str(db_path), "--aux"],
        catch_exceptions=False,
    )
    assert result2.exit_code == 0
    assert json.loads(result2.output) == [
        {
            "table": "Gosh",
            "index_name": "Gosh_idx",
            "seqno": 0,
            "cid": 1,
            "name": "c2",
            "desc": 0,
            "coll": "BINARY",
            "key": 1,
        },
        {
            "table": "Gosh",
            "index_name": "Gosh_idx",
            "seqno": 1,
            "cid": 2,
            "name": "c3",
            "desc": 1,
            "coll": "BINARY",
            "key": 1,
        },
        {
            "table": "Gosh",
            "index_name": "Gosh_idx",
            "seqno": 2,
            "cid": -1,
            "name": None,
            "desc": 0,
            "coll": "BINARY",
            "key": 0,
        },
    ]


_TRIGGERS_EXPECTED = (
    '[{"name": "blah", "table": "articles", "sql": "CREATE TRIGGER blah '
    'AFTER INSERT ON articles\\nBEGIN\\n    UPDATE counter SET count = count + 1;\\nEND"}]\n'
)


@pytest.mark.parametrize(
    "extra_args,expected",
    [
        ([], _TRIGGERS_EXPECTED),
        (["articles"], _TRIGGERS_EXPECTED),
        (["counter"], "[]\n"),
    ],
)
def test_triggers(tmpdir, extra_args, expected):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("articles").insert(
        {"id": 1, "title": "Title the first"},
        pk="id",
    )
    db.table("counter").insert({"count": 1})
    db.conn.execute(textwrap.dedent("""
        CREATE TRIGGER blah AFTER INSERT ON articles
        BEGIN
            UPDATE counter SET count = count + 1;
        END
    """))
    args = ["triggers", db_path]
    if extra_args:
        args.extend(extra_args)
    result = CliRunner().invoke(
        cli.cli,
        args,
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert result.output == expected


@pytest.mark.parametrize(
    "options,expected",
    (
        (
            [],
            (
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER,\n'
                '   "name" TEXT\n'
                ");\n"
                'CREATE TABLE "chickens" (\n'
                '   "id" INTEGER,\n'
                '   "name" TEXT,\n'
                '   "breed" TEXT\n'
                ");\n"
                'CREATE INDEX "idx_chickens_breed"\n'
                '    ON "chickens" ("breed");\n'
            ),
        ),
        (
            ["dogs"],
            ('CREATE TABLE "dogs" (\n' '   "id" INTEGER,\n' '   "name" TEXT\n' ")\n"),
        ),
        (
            ["chickens", "dogs"],
            (
                'CREATE TABLE "chickens" (\n'
                '   "id" INTEGER,\n'
                '   "name" TEXT,\n'
                '   "breed" TEXT\n'
                ")\n"
                'CREATE TABLE "dogs" (\n'
                '   "id" INTEGER,\n'
                '   "name" TEXT\n'
                ")\n"
            ),
        ),
    ),
)
def test_schema(tmpdir, options, expected):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("dogs").create({"id": int, "name": str})
    db.table("chickens").create({"id": int, "name": str, "breed": str})
    db.table("chickens").create_index(["breed"])
    result = CliRunner().invoke(
        cli.cli,
        ["schema", db_path] + options,
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert result.output == expected


def test_long_csv_column_value(tmpdir):
    db_path = str(tmpdir / "test.db")
    csv_path = str(tmpdir / "test.csv")
    with open(csv_path, "w") as csv_file:
        long_string = "a" * 131073
        csv_file.write("id,text\n")
        csv_file.write(f"1,{long_string}\n")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "bigtable", csv_path, "--csv"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    db = Database(db_path)
    rows = list(db.table("bigtable").rows)
    assert len(rows) == 1
    assert rows[0]["text"] == long_string


@pytest.mark.parametrize(
    "args,tsv",
    (
        (["--csv", "--no-headers"], False),
        (["--no-headers"], False),
        (["--tsv", "--no-headers"], True),
    ),
)
def test_import_no_headers(tmpdir, args, tsv):
    db_path = str(tmpdir / "test.db")
    csv_path = str(tmpdir / "test.csv")
    with open(csv_path, "w") as csv_file:
        sep = "\t" if tsv else ","
        csv_file.write(f"Cleo{sep}Dog{sep}5\n")
        csv_file.write(f"Tracy{sep}Spider{sep}7\n")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", csv_path] + args + ["--no-detect-types"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    schema = db.table("creatures").schema
    assert schema == (
        'CREATE TABLE "creatures" (\n'
        '   "untitled_1" TEXT,\n'
        '   "untitled_2" TEXT,\n'
        '   "untitled_3" TEXT\n'
        ")"
    )
    rows = list(db.table("creatures").rows)
    assert rows == [
        {"untitled_1": "Cleo", "untitled_2": "Dog", "untitled_3": "5"},
        {"untitled_1": "Tracy", "untitled_2": "Spider", "untitled_3": "7"},
    ]


def test_attach(tmpdir):
    foo_path = str(tmpdir / "foo.db")
    bar_path = str(tmpdir / "bar.db")
    db = Database(foo_path)
    with db.conn:
        db.table("foo").insert({"id": 1, "text": "foo"})
    db2 = Database(bar_path)
    with db2.conn:
        db2.table("bar").insert({"id": 1, "text": "bar"})
    db.attach("bar", bar_path)
    sql = "select * from foo union all select * from bar.bar"
    result = CliRunner().invoke(
        cli.cli,
        [foo_path, "--attach", "bar", bar_path, sql],
        catch_exceptions=False,
    )
    assert json.loads(result.output) == [
        {"id": 1, "text": "foo"},
        {"id": 1, "text": "bar"},
    ]


def test_csv_insert_bom(tmpdir):
    db_path = str(tmpdir / "test.db")
    bom_csv_path = str(tmpdir / "bom.csv")
    with open(bom_csv_path, "wb") as fp:
        fp.write(b"\xef\xbb\xbfname,age\nCleo,5")
    result = CliRunner().invoke(
        cli.cli,
        [
            "insert",
            db_path,
            "broken",
            bom_csv_path,
            "--encoding",
            "utf-8",
            "--csv",
            "--no-detect-types",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    result2 = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "fixed", bom_csv_path, "--csv", "--no-detect-types"],
        catch_exceptions=False,
    )
    assert result2.exit_code == 0
    db = Database(db_path)
    tables = db.execute("select name, sql from sqlite_master").fetchall()
    assert tables == [
        ("broken", 'CREATE TABLE "broken" (\n   "\ufeffname" TEXT,\n   "age" TEXT\n)'),
        ("fixed", 'CREATE TABLE "fixed" (\n   "name" TEXT,\n   "age" TEXT\n)'),
    ]


def test_insert_detect_types(tmpdir):
    """Test that type detection is the default behavior"""
    db_path = str(tmpdir / "test.db")
    data = "name,age,weight\nCleo,6,45.5\nDori,1,3.5"

    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "-", "--csv"],
        catch_exceptions=False,
        input=data,
    )
    assert result.exit_code == 0
    db = Database(db_path)
    assert list(db.table("creatures").rows) == [
        {"name": "Cleo", "age": 6, "weight": 45.5},
        {"name": "Dori", "age": 1, "weight": 3.5},
    ]


@pytest.mark.parametrize("command", ("insert", "upsert"))
@pytest.mark.parametrize("option", ("-d", "--detect-types"))
def test_detect_types_flag_removed(tmpdir, command, option):
    # The old no-op flag was removed in 4.0 - it should now error
    db_path = str(tmpdir / "test.db")
    result = CliRunner().invoke(
        cli.cli,
        [command, db_path, "creatures", "-", "--csv", "--pk", "id", option],
        input="id,name\n1,Cleo",
    )
    assert result.exit_code == 2
    assert "No such option" in result.output


def test_upsert_detect_types(tmpdir):
    """Test that type detection is the default behavior for upsert"""
    db_path = str(tmpdir / "test.db")
    data = "id,name,age,weight\n1,Cleo,6,45.5\n2,Dori,1,3.5"
    result = CliRunner().invoke(
        cli.cli,
        ["upsert", db_path, "creatures", "-", "--csv", "--pk", "id"],
        catch_exceptions=False,
        input=data,
    )
    assert result.exit_code == 0
    db = Database(db_path)
    assert list(db.table("creatures").rows) == [
        {"id": 1, "name": "Cleo", "age": 6, "weight": 45.5},
        {"id": 2, "name": "Dori", "age": 1, "weight": 3.5},
    ]


def test_csv_detect_types_creates_real_columns(tmpdir):
    """Test that CSV import creates REAL columns for floats (default behavior)"""
    db_path = str(tmpdir / "test.db")
    data = "name,age,weight\nCleo,6,45.5\nDori,1,3.5"
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "-", "--csv"],
        catch_exceptions=False,
        input=data,
    )
    assert result.exit_code == 0
    db = Database(db_path)
    # Check that the schema uses REAL for the weight column
    assert db.table("creatures").schema == (
        'CREATE TABLE "creatures" (\n'
        '   "name" TEXT,\n'
        '   "age" INTEGER,\n'
        '   "weight" REAL\n'
        ")"
    )


def test_insert_no_detect_types(tmpdir):
    """Test that --no-detect-types treats all columns as TEXT"""
    db_path = str(tmpdir / "test.db")
    data = "name,age,weight\nCleo,6,45.5\nDori,1,3.5"
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "creatures", "-", "--csv", "--no-detect-types"],
        catch_exceptions=False,
        input=data,
    )
    assert result.exit_code == 0
    db = Database(db_path)
    # All columns should be TEXT when --no-detect-types is used
    assert list(db.table("creatures").rows) == [
        {"name": "Cleo", "age": "6", "weight": "45.5"},
        {"name": "Dori", "age": "1", "weight": "3.5"},
    ]
    assert db.table("creatures").schema == (
        'CREATE TABLE "creatures" (\n'
        '   "name" TEXT,\n'
        '   "age" TEXT,\n'
        '   "weight" TEXT\n'
        ")"
    )


def test_upsert_no_detect_types(tmpdir):
    """Test that --no-detect-types treats all columns as TEXT for upsert"""
    db_path = str(tmpdir / "test.db")
    data = "id,name,age,weight\n1,Cleo,6,45.5\n2,Dori,1,3.5"
    result = CliRunner().invoke(
        cli.cli,
        [
            "upsert",
            db_path,
            "creatures",
            "-",
            "--csv",
            "--pk",
            "id",
            "--no-detect-types",
        ],
        catch_exceptions=False,
        input=data,
    )
    assert result.exit_code == 0
    db = Database(db_path)
    # All columns should be TEXT when --no-detect-types is used
    assert list(db.table("creatures").rows) == [
        {"id": "1", "name": "Cleo", "age": "6", "weight": "45.5"},
        {"id": "2", "name": "Dori", "age": "1", "weight": "3.5"},
    ]
    assert db.table("creatures").schema == (
        'CREATE TABLE "creatures" (\n'
        '   "id" TEXT PRIMARY KEY,\n'
        '   "name" TEXT,\n'
        '   "age" TEXT,\n'
        '   "weight" TEXT\n'
        ")"
    )


def test_integer_overflow_error(tmpdir):
    db_path = str(tmpdir / "test.db")
    result = CliRunner().invoke(
        cli.cli,
        ["insert", db_path, "items", "-"],
        input=json.dumps({"bignumber": 34223049823094832094802398430298048240}),
    )
    assert result.exit_code == 1
    assert result.output == (
        "Error: Python int too large to convert to SQLite INTEGER\n\n"
        'sql = INSERT INTO "items" ("bignumber") VALUES (?)\n'
        "parameters = [34223049823094832094802398430298048240]\n"
    )


def test_python_dash_m():
    "Tool can be run using python -m sqlite_utils"
    result = subprocess.run(
        [sys.executable, "-m", "sqlite_utils", "--help"],
        stdout=subprocess.PIPE,
        check=False,
    )
    assert result.returncode == 0
    assert b"Commands for interacting with a SQLite database" in result.stdout


@pytest.mark.parametrize("enable_wal", (False, True))
def test_create_database(tmpdir, enable_wal):
    db_path = tmpdir / "test.db"
    assert not db_path.exists()
    args = ["create-database", str(db_path)]
    if enable_wal:
        args.append("--enable-wal")
    result = CliRunner().invoke(cli.cli, args)
    assert result.exit_code == 0, result.output
    assert db_path.exists()
    assert db_path.read_binary()[:16] == b"SQLite format 3\x00"
    db = Database(str(db_path))
    if enable_wal:
        assert db.journal_mode == "wal"
    else:
        assert db.journal_mode == "delete"


@pytest.mark.parametrize(
    "options,expected",
    (
        (
            [],
            [
                {"tbl": "two_indexes", "idx": "idx_two_indexes_species", "stat": "1 1"},
                {"tbl": "two_indexes", "idx": "idx_two_indexes_name", "stat": "1 1"},
                {"tbl": "one_index", "idx": "idx_one_index_name", "stat": "1 1"},
            ],
        ),
        (
            ["one_index"],
            [
                {"tbl": "one_index", "idx": "idx_one_index_name", "stat": "1 1"},
            ],
        ),
        (
            ["idx_two_indexes_name"],
            [
                {"tbl": "two_indexes", "idx": "idx_two_indexes_name", "stat": "1 1"},
            ],
        ),
    ),
)
def test_analyze(tmpdir, options, expected):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("one_index").insert({"id": 1, "name": "Cleo"}, pk="id")
    db.table("one_index").create_index(["name"])
    db.table("two_indexes").insert({"id": 1, "name": "Cleo", "species": "dog"}, pk="id")
    db.table("two_indexes").create_index(["name"])
    db.table("two_indexes").create_index(["species"])
    result = CliRunner().invoke(cli.cli, ["analyze", db_path] + options)
    assert result.exit_code == 0
    assert list(db.table("sqlite_stat1").rows) == expected


def test_rename_table(tmpdir):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("one").insert({"id": 1, "name": "Cleo"}, pk="id")
    # First try a non-existent table
    result_error = CliRunner().invoke(
        cli.cli,
        ["rename-table", db_path, "missing", "two"],
        catch_exceptions=False,
    )
    assert result_error.exit_code == 1
    assert result_error.output == (
        'Error: Table "missing" could not be renamed. ' "no such table: missing\n"
    )
    # And check --ignore works
    result_error2 = CliRunner().invoke(
        cli.cli,
        ["rename-table", db_path, "missing", "two", "--ignore"],
        catch_exceptions=False,
    )
    assert result_error2.exit_code == 0
    previous_columns = db.table("one").columns_dict
    # Now try for a table that exists
    result = CliRunner().invoke(
        cli.cli,
        ["rename-table", db_path, "one", "two"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert db.table("two").columns_dict == previous_columns


def test_duplicate_table(tmpdir):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("one").insert({"id": 1, "name": "Cleo"}, pk="id")
    # First try a non-existent table
    result_error = CliRunner().invoke(
        cli.cli,
        ["duplicate", db_path, "missing", "two"],
        catch_exceptions=False,
    )
    assert result_error.exit_code == 1
    assert result_error.output == 'Error: Table "missing" does not exist\n'
    # And check --ignore works
    result_error2 = CliRunner().invoke(
        cli.cli,
        ["duplicate", db_path, "missing", "two", "--ignore"],
        catch_exceptions=False,
    )
    assert result_error2.exit_code == 0
    # Now try for a table that exists
    result = CliRunner().invoke(
        cli.cli,
        ["duplicate", db_path, "one", "two"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert db.table("one").columns_dict == db.table("two").columns_dict
    assert list(db.table("one").rows) == list(db.table("two").rows)


@pytest.mark.skipif(not _has_compiled_ext(), reason="Requires compiled ext.c")
@pytest.mark.parametrize(
    "entrypoint,should_pass,should_fail",
    (
        (None, ("a",), ("b", "c")),
        ("sqlite3_ext_b_init", ("b"), ("a", "c")),
        ("sqlite3_ext_c_init", ("c"), ("a", "b")),
    ),
)
def test_load_extension(entrypoint, should_pass, should_fail):
    ext = COMPILED_EXTENSION_PATH
    if entrypoint:
        ext += ":" + entrypoint
    for func in should_pass:
        result = CliRunner().invoke(
            cli.cli,
            ["memory", f"select {func}()", "--load-extension", ext],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
    for func in should_fail:
        result = CliRunner().invoke(
            cli.cli,
            ["memory", f"select {func}()", "--load-extension", ext],
            catch_exceptions=False,
        )
        assert result.exit_code == 1


@pytest.mark.parametrize("strict", (False, True))
def test_create_table_strict(strict):
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        result = runner.invoke(
            cli.cli,
            ["create-table", "test.db", "items", "id", "integer", "w", "float"]
            + (["--strict"] if strict else []),
        )
        assert result.exit_code == 0
        assert db.table("items").strict == strict or not db.supports_strict
        # Should have a floating point column
        assert db.table("items").columns_dict == {"id": int, "w": float}


def test_create_table_strict_any():
    runner = CliRunner()
    with runner.isolated_filesystem():
        db = Database("test.db")
        if not db.supports_strict:
            pytest.skip("SQLite version does not support strict tables")
        result = runner.invoke(
            cli.cli,
            [
                "create-table",
                "test.db",
                "items",
                "id",
                "integer",
                "data",
                "any",
                "--strict",
            ],
        )
        assert result.exit_code == 0, result.output
        assert db.table("items").strict is True
        assert db.table("items").columns_dict == {"id": int, "data": ANY}


@pytest.mark.parametrize("method", ("insert", "upsert"))
@pytest.mark.parametrize("strict", (False, True))
def test_insert_upsert_strict(tmpdir, method, strict):
    db_path = str(tmpdir / "test.db")
    result = CliRunner().invoke(
        cli.cli,
        [method, db_path, "items", "-", "--csv", "--pk", "id"]
        + (["--strict"] if strict else []),
        input="id\n1",
    )
    assert result.exit_code == 0
    db = Database(db_path)
    assert db.table("items").strict == strict or not db.supports_strict


@pytest.mark.parametrize("method", ("insert", "upsert"))
def test_insert_upsert_strict_any(tmpdir, method):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    if not db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    db.close()
    result = CliRunner().invoke(
        cli.cli,
        [
            method,
            db_path,
            "items",
            "-",
            "--csv",
            "--pk",
            "id",
            "--type",
            "data",
            "any",
            "--strict",
        ],
        input="id,data\n1,000123",
    )
    assert result.exit_code == 0, result.output
    db = Database(db_path)
    assert db.table("items").columns_dict == {"id": int, "data": ANY}
    assert db.execute("select typeof(data), data from items").fetchone() == (
        "text",
        "000123",
    )


def test_extract_bad_column_clean_error(db_path):
    db = Database(db_path)
    db.table("trees").insert({"id": 1, "species": "Palm"}, pk="id")
    result = CliRunner().invoke(cli.cli, ["extract", db_path, "trees", "nope"])
    assert result.exit_code == 1
    assert result.exception is None or isinstance(result.exception, SystemExit)
    assert result.output.startswith("Error: Invalid columns")


def test_extract_view_clean_error(db_path):
    db = Database(db_path)
    db.table("trees").insert({"id": 1, "species": "Palm"}, pk="id")
    db.create_view("v", "select * from trees")
    result = CliRunner().invoke(cli.cli, ["extract", db_path, "v", "species"])
    assert result.exit_code == 1
    assert result.exception is None or isinstance(result.exception, SystemExit)
    assert result.output.startswith("Error:")

```

### `tests/test_column_affinity.py`

```py
import pytest

from sqlite_utils import ANY
from sqlite_utils.utils import column_affinity

EXAMPLES = [
    # Examples from https://www.sqlite.org/datatype3.html#affinity_name_examples
    ("INT", int),
    ("INTEGER", int),
    ("TINYINT", int),
    ("SMALLINT", int),
    ("MEDIUMINT", int),
    ("BIGINT", int),
    ("UNSIGNED BIG INT", int),
    ("INT2", int),
    ("INT8", int),
    ("CHARACTER(20)", str),
    ("VARCHAR(255)", str),
    ("VARYING CHARACTER(255)", str),
    ("NCHAR(55)", str),
    ("NATIVE CHARACTER(70)", str),
    ("NVARCHAR(100)", str),
    ("TEXT", str),
    ("CLOB", str),
    ("BLOB", bytes),
    ("REAL", float),
    ("DOUBLE", float),
    ("DOUBLE PRECISION", float),
    ("FLOAT", float),
    ("ANY", ANY),
    ("any", ANY),
    # Numeric, treated as float:
    ("NUMERIC", float),
    ("DECIMAL(10,5)", float),
    ("BOOLEAN", float),
    ("DATE", float),
    ("DATETIME", float),
]


@pytest.mark.parametrize("column_def,expected_type", EXAMPLES)
def test_column_affinity(column_def, expected_type):
    assert expected_type is column_affinity(column_def)


@pytest.mark.parametrize("column_def,expected_type", EXAMPLES)
def test_columns_dict(fresh_db, column_def, expected_type):
    fresh_db.execute(f"create table foo (col {column_def})")
    assert {"col": expected_type} == fresh_db.table("foo").columns_dict

```

### `tests/test_column_casing.py`

```py
"""
SQLite treats column names as case-insensitive. These tests exercise the
places where sqlite-utils performs Python-side lookups of column names
provided by the caller, which should match the schema case-insensitively.

https://github.com/simonw/sqlite-utils/issues/760
"""

import pytest

from sqlite_utils import Database
from sqlite_utils.db import ForeignKey


def test_insert_populates_last_pk_case_insensitively(fresh_db):
    books = fresh_db.table("books")
    books.create({"Id": int, "Title": str}, pk="Id")
    books.insert({"Id": 1, "Title": "One"}, pk="id")
    assert books.last_pk == 1


def test_insert_populates_last_pk_compound_pk_case_insensitively(fresh_db):
    books = fresh_db.table("books")
    books.create({"Author": str, "Position": int, "Title": str})
    books.insert(
        {"Author": "Sue", "Position": 1, "Title": "One"}, pk=("author", "position")
    )
    assert books.last_pk == ("Sue", 1)


@pytest.mark.parametrize("use_old_upsert", (False, True))
def test_upsert_pk_case_differs_from_schema(use_old_upsert):
    db = Database(memory=True, use_old_upsert=use_old_upsert)
    books = db.table("books")
    books.create({"Id": int, "Title": str}, pk="Id")
    books.insert({"Id": 1, "Title": "One"})
    books.upsert({"id": 1, "title": "Won"}, pk="id")
    assert list(books.rows) == [{"Id": 1, "Title": "Won"}]
    assert books.last_pk == 1


@pytest.mark.parametrize("use_old_upsert", (False, True))
def test_upsert_record_key_case_differs_from_pk(use_old_upsert):
    # all_columns comes from the record keys, pk= from the caller
    db = Database(memory=True, use_old_upsert=use_old_upsert)
    books = db.table("books")
    books.create({"Id": int, "Title": str}, pk="Id")
    books.upsert({"ID": 1, "Title": "One"}, pk="id")
    assert list(books.rows) == [{"Id": 1, "Title": "One"}]
    assert books.last_pk == 1


def test_upsert_inferred_pk_case_differs_from_record_keys(fresh_db):
    # pk is inferred from the existing schema as "Id", records use "id"
    books = fresh_db.table("books")
    books.create({"Id": int, "Title": str}, pk="Id")
    books.upsert({"id": 1, "title": "One"})
    assert list(books.rows) == [{"Id": 1, "Title": "One"}]
    assert books.last_pk == 1


def test_upsert_list_mode_pk_case_insensitive(fresh_db):
    books = fresh_db.table("books")
    books.create({"Id": int, "Title": str}, pk="Id")
    books.upsert_all([["id", "title"], [1, "One"]], pk="Id")
    assert list(books.rows) == [{"Id": 1, "Title": "One"}]
    assert books.last_pk == 1


def test_lookup_pk_case_insensitive(fresh_db):
    fresh_db.table("species").create({"ID": int, "Name": str}, pk="ID")
    fresh_db.table("species").insert({"ID": 5, "Name": "Palm"})
    fresh_db.table("species").create_index(["Name"], unique=True)
    assert fresh_db.table("species").lookup({"Name": "Palm"}, pk="id") == 5


def test_lookup_does_not_create_redundant_index(fresh_db):
    fresh_db.table("species").create({"id": int, "Name": str}, pk="id")
    fresh_db.table("species").create_index(["Name"], unique=True)
    fresh_db.table("species").lookup({"name": "Palm"})
    assert len(fresh_db.table("species").indexes) == 1


def test_create_table_transform_same_columns_different_case(fresh_db):
    fresh_db.table("t").create({"Name": str, "Age": int})
    fresh_db.table("t").insert({"Name": "Cleo", "Age": 5})
    fresh_db.create_table("t", {"name": str, "age": int}, transform=True)
    # Schema casing is preserved - SQLite considers these the same columns
    assert fresh_db.table("t").columns_dict == {"Name": str, "Age": int}
    assert list(fresh_db.table("t").rows) == [{"Name": "Cleo", "Age": 5}]


def test_create_table_transform_case_insensitive_with_changes(fresh_db):
    fresh_db.table("t").create({"Name": str, "Age": int})
    fresh_db.create_table("t", {"name": str, "age": str, "size": int}, transform=True)
    # age changed type, size added, Name untouched
    assert fresh_db.table("t").columns_dict == {"Name": str, "Age": str, "size": int}


def test_transform_types_case_insensitive(fresh_db):
    fresh_db.table("t").create({"Name": str, "Age": str})
    fresh_db.table("t").transform(types={"age": int})
    assert fresh_db.table("t").columns_dict == {"Name": str, "Age": int}


def test_transform_rename_case_insensitive(fresh_db):
    fresh_db.table("t").create({"Name": str})
    fresh_db.table("t").transform(rename={"name": "title"})
    assert fresh_db.table("t").columns_dict == {"title": str}


def test_transform_drop_case_insensitive(fresh_db):
    fresh_db.table("t").create({"Name": str, "Age": int})
    fresh_db.table("t").transform(drop=["name"])
    assert fresh_db.table("t").columns_dict == {"Age": int}


def test_transform_not_null_and_defaults_case_insensitive(fresh_db):
    fresh_db.table("t").create({"Name": str, "Age": int})
    fresh_db.table("t").transform(not_null={"name"}, defaults={"age": 3})
    columns = {c.name: c for c in fresh_db.table("t").columns}
    assert columns["Name"].notnull
    assert fresh_db.table("t").default_values == {"Age": 3}


def test_transform_pk_case_insensitive(fresh_db):
    fresh_db.table("t").create({"Id": int, "Name": str})
    fresh_db.table("t").transform(pk="id")
    assert fresh_db.table("t").pks == ["Id"]
    assert fresh_db.table("t").columns_dict == {"Id": int, "Name": str}


def test_transform_drop_foreign_keys_case_insensitive(fresh_db):
    fresh_db.table("parent").create({"Id": int}, pk="Id")
    fresh_db.table("child").create(
        {"id": int, "Parent_ID": int},
        pk="id",
        foreign_keys=[("Parent_ID", "parent", "Id")],
    )
    fresh_db.table("child").transform(drop_foreign_keys=["parent_id"])
    assert fresh_db.table("child").foreign_keys == []


def test_add_foreign_key_case_insensitive(fresh_db):
    fresh_db.table("parent").create({"Id": int}, pk="Id")
    fresh_db.table("child").create({"id": int, "Parent_ID": int}, pk="id")
    fresh_db.table("child").add_foreign_key("parent_id", "parent", "id")
    fks = fresh_db.table("child").foreign_keys
    assert len(fks) == 1
    # The foreign key should use the schema casing of the columns
    assert fks[0].column == "Parent_ID"
    assert fks[0].other_column == "Id"


def test_add_foreign_keys_case_insensitive(fresh_db):
    fresh_db.table("parent").create({"Id": int}, pk="Id")
    fresh_db.table("child").create({"id": int, "Parent_ID": int}, pk="id")
    fresh_db.add_foreign_keys([("child", "parent_id", "parent", "id")])
    fks = fresh_db.table("child").foreign_keys
    assert len(fks) == 1
    assert fks[0].column == "Parent_ID"
    assert fks[0].other_column == "Id"


def test_add_foreign_key_detects_existing_case_insensitively(fresh_db):
    fresh_db.table("parent").create({"Id": int}, pk="Id")
    fresh_db.table("child").create(
        {"id": int, "Parent_ID": int},
        pk="id",
        foreign_keys=[("Parent_ID", "parent", "Id")],
    )
    # ignore=True should treat this as already existing, not add a duplicate
    fresh_db.table("child").add_foreign_key("parent_id", "parent", "id", ignore=True)
    assert len(fresh_db.table("child").foreign_keys) == 1


def test_add_column_fk_col_case_insensitive(fresh_db):
    fresh_db.table("parent").create({"Id": int}, pk="Id")
    fresh_db.table("child").create({"id": int}, pk="id")
    fresh_db.table("child").add_column("parent_id", int, fk="parent", fk_col="id")
    fks = fresh_db.table("child").foreign_keys
    assert len(fks) == 1
    assert fks[0].other_column == "Id"


def test_extract_case_insensitive(fresh_db):
    fresh_db.table("trees").insert({"id": 1, "Species": "Palm"}, pk="id")
    fresh_db.table("trees").extract("species")
    assert fresh_db.table("trees").columns_dict == {"id": int, "Species_id": int}
    assert list(fresh_db.table("Species").rows) == [{"id": 1, "Species": "Palm"}]


def test_convert_multi_case_insensitive(fresh_db):
    fresh_db.table("t").insert({"id": 1, "Name": "Cleo"}, pk="id")
    fresh_db.table("t").convert("name", lambda v: {"upper": v.upper()}, multi=True)
    assert list(fresh_db.table("t").rows) == [
        {"id": 1, "Name": "Cleo", "upper": "CLEO"}
    ]


def test_convert_output_case_insensitive(fresh_db):
    fresh_db.table("t").insert({"id": 1, "Name": "Cleo", "Upper": None}, pk="id")
    fresh_db.table("t").convert("name", lambda v: v.upper(), output="upper")
    assert list(fresh_db.table("t").rows) == [
        {"id": 1, "Name": "Cleo", "Upper": "CLEO"}
    ]


def test_create_table_sql_pk_case_insensitive(fresh_db):
    fresh_db.table("t").create({"Id": int, "Name": str}, pk="id")
    # Should not have created an extra lowercase "id" column
    assert fresh_db.table("t").columns_dict == {"Id": int, "Name": str}
    assert fresh_db.table("t").pks == ["Id"]


def test_create_table_not_null_and_defaults_case_insensitive(fresh_db):
    fresh_db.table("t").create(
        {"Name": str, "Age": int}, not_null={"name"}, defaults={"age": 1}
    )
    columns = {c.name: c for c in fresh_db.table("t").columns}
    assert columns["Name"].notnull
    assert fresh_db.table("t").default_values == {"Age": 1}


def test_create_table_foreign_keys_case_insensitive(fresh_db):
    fresh_db.table("parent").create({"Id": int}, pk="Id")
    fresh_db.table("child").create(
        {"id": int, "Parent_ID": int},
        pk="id",
        foreign_keys=[("parent_id", "parent", "id")],
    )
    fks = fresh_db.table("child").foreign_keys
    assert fks == [
        ForeignKey(
            table="child", column="Parent_ID", other_table="parent", other_column="Id"
        )
    ]

```

### `tests/test_constructor.py`

```py
import sys

import pytest

from sqlite_utils import Database
from sqlite_utils.db import TransactionError
from sqlite_utils.utils import sqlite3


def test_recursive_triggers():
    db = Database(memory=True)
    assert db.execute("PRAGMA recursive_triggers").fetchone()[0]


def test_recursive_triggers_off():
    db = Database(memory=True, recursive_triggers=False)
    assert not db.execute("PRAGMA recursive_triggers").fetchone()[0]


def test_memory_name():
    db1 = Database(memory_name="shared")
    db2 = Database(memory_name="shared")
    db1.table("dogs").insert({"name": "Cleo"})
    assert list(db2.table("dogs").rows) == [{"name": "Cleo"}]


def test_sqlite_version():
    db = Database(memory=True)
    version = db.sqlite_version
    assert isinstance(version, tuple)
    as_string = ".".join(map(str, version))
    actual = next(db.query("select sqlite_version() as v"))["v"]
    assert actual == as_string


def test_database_context_manager(tmpdir):
    path = str(tmpdir / "test.db")
    with Database(path) as db:
        db.table("t").insert({"id": 1})
        # Raw writes commit automatically too
        db.execute("insert into t (id) values (2)")
        # An explicitly opened transaction left uncommitted on purpose:
        db.begin()
        db.execute("insert into t (id) values (3)")
    # The connection is closed...
    with pytest.raises(sqlite3.ProgrammingError):
        db.execute("select 1")
    # ... and the open explicit transaction was rolled back, not committed
    db2 = Database(path)
    assert [r["id"] for r in db2.table("t").rows] == [1, 2]
    db2.close()


@pytest.mark.parametrize("memory", [True, False])
def test_database_close(tmpdir, memory):
    if memory:
        db = Database(memory=True)
    else:
        db = Database(str(tmpdir / "test.db"))
    assert db.execute("select 1 + 1").fetchone()[0] == 2
    db.close()
    with pytest.raises(sqlite3.ProgrammingError):
        db.execute("select 1 + 1")


@pytest.mark.skipif(
    sys.version_info < (3, 12),
    reason="sqlite3.connect(autocommit=) requires Python 3.12",
)
@pytest.mark.parametrize("autocommit", [True, False])
def test_autocommit_connections_are_rejected(tmpdir, autocommit):
    # These connection modes break commit()/rollback() in ways that
    # silently lose data, so the constructor refuses them
    conn = sqlite3.connect(str(tmpdir / "test.db"), autocommit=autocommit)
    with pytest.raises(TransactionError):
        Database(conn)
    conn.close()


@pytest.mark.skipif(
    sys.version_info < (3, 12),
    reason="sqlite3.LEGACY_TRANSACTION_CONTROL requires Python 3.12",
)
def test_legacy_transaction_control_connection_is_accepted(tmpdir):
    conn = sqlite3.connect(
        str(tmpdir / "test.db"),
        autocommit=sqlite3.LEGACY_TRANSACTION_CONTROL,  # type: ignore[arg-type]
    )
    db = Database(conn)
    db.table("t").insert({"id": 1}, pk="id")
    assert [r["id"] for r in db.table("t").rows] == [1]
    db.close()


def test_memory_attribute_for_memory_true():
    db = Database(memory=True)
    assert db.memory is True
    assert db.memory_name is None


def test_memory_attribute_for_memory_name():
    db = Database(memory_name="shared_attr")
    assert db.memory is True
    assert db.memory_name == "shared_attr"


def test_memory_attribute_for_memory_string_path():
    db = Database(":memory:")
    assert db.memory is True
    assert db.memory_name is None


def test_memory_attribute_for_file_path(tmpdir):
    db = Database(str(tmpdir / "file.db"))
    assert db.memory is False
    assert db.memory_name is None

```

### `tests/test_conversions.py`

```py
def test_insert_conversion(fresh_db):
    table = fresh_db.table("table")
    table.insert({"foo": "bar"}, conversions={"foo": "upper(?)"})
    assert [{"foo": "BAR"}] == list(table.rows)


def test_insert_all_conversion(fresh_db):
    table = fresh_db.table("table")
    table.insert_all([{"foo": "bar"}], conversions={"foo": "upper(?)"})
    assert [{"foo": "BAR"}] == list(table.rows)


def test_upsert_conversion(fresh_db):
    table = fresh_db.table("table")
    table.upsert({"id": 1, "foo": "bar"}, pk="id", conversions={"foo": "upper(?)"})
    assert [{"id": 1, "foo": "BAR"}] == list(table.rows)
    table.upsert(
        {"id": 1, "bar": "baz"}, pk="id", conversions={"bar": "upper(?)"}, alter=True
    )
    assert [{"id": 1, "foo": "BAR", "bar": "BAZ"}] == list(table.rows)


def test_upsert_all_conversion(fresh_db):
    table = fresh_db.table("table")
    table.upsert_all(
        [{"id": 1, "foo": "bar"}], pk="id", conversions={"foo": "upper(?)"}
    )
    assert [{"id": 1, "foo": "BAR"}] == list(table.rows)


def test_update_conversion(fresh_db):
    table = fresh_db.table("table")
    table.insert({"id": 5, "foo": "bar"}, pk="id")
    table.update(5, {"foo": "baz"}, conversions={"foo": "upper(?)"})
    assert [{"id": 5, "foo": "BAZ"}] == list(table.rows)


def test_table_constructor_conversion(fresh_db):
    table = fresh_db.table("table", conversions={"bar": "upper(?)"})
    table.insert({"bar": "baz"})
    assert [{"bar": "BAZ"}] == list(table.rows)

```

### `tests/test_convert.py`

```py
import pytest

from sqlite_utils.db import BadMultiValues


@pytest.mark.parametrize(
    "columns,fn,expected",
    (
        (
            "title",
            lambda value: value.upper(),
            {"title": "MIXED CASE", "abstract": "Abstract"},
        ),
        (
            ["title", "abstract"],
            lambda value: value.upper(),
            {"title": "MIXED CASE", "abstract": "ABSTRACT"},
        ),
        (
            "title",
            lambda value: {"upper": value.upper(), "lower": value.lower()},
            {
                "title": '{"upper": "MIXED CASE", "lower": "mixed case"}',
                "abstract": "Abstract",
            },
        ),
    ),
)
def test_convert(fresh_db, columns, fn, expected):
    table = fresh_db.table("table")
    table.insert({"title": "Mixed Case", "abstract": "Abstract"})
    table.convert(columns, fn)
    assert list(table.rows) == [expected]


@pytest.mark.parametrize(
    "where,where_args", (("id > 1", None), ("id > :id", {"id": 1}), ("id > ?", [1]))
)
def test_convert_where(fresh_db, where, where_args):
    table = fresh_db.table("table")
    table.insert_all(
        [
            {"id": 1, "title": "One"},
            {"id": 2, "title": "Two"},
        ],
        pk="id",
    )
    table.convert(
        "title", lambda value: value.upper(), where=where, where_args=where_args
    )
    assert list(table.rows) == [{"id": 1, "title": "One"}, {"id": 2, "title": "TWO"}]


def test_convert_handles_falsey_values(fresh_db):
    # Falsey values like 0 should be converted (issue #527)
    table = fresh_db.table("table")
    table.insert_all([{"x": 0}, {"x": 1}])
    assert table.get(1)["x"] == 0
    assert table.get(2)["x"] == 1
    table.convert("x", lambda x: x + 1)
    assert table.get(1)["x"] == 1
    assert table.get(2)["x"] == 2


@pytest.mark.parametrize(
    "drop,expected",
    (
        (False, {"title": "Mixed Case", "other": "MIXED CASE"}),
        (True, {"other": "MIXED CASE"}),
    ),
)
def test_convert_output(fresh_db, drop, expected):
    table = fresh_db.table("table")
    table.insert({"title": "Mixed Case"})
    table.convert("title", lambda v: v.upper(), output="other", drop=drop)
    assert list(table.rows) == [expected]


def test_convert_output_multiple_column_error(fresh_db):
    table = fresh_db.table("table")
    with pytest.raises(ValueError) as excinfo:
        table.convert(["title", "other"], lambda v: v, output="out")
        assert "output= can only be used with a single column" in str(excinfo.value)


@pytest.mark.parametrize(
    "type,expected",
    (
        (int, {"other": 123}),
        (float, {"other": 123.0}),
    ),
)
def test_convert_output_type(fresh_db, type, expected):
    table = fresh_db.table("table")
    table.insert({"number": "123"})
    table.convert("number", lambda v: v, output="other", output_type=type, drop=True)
    assert list(table.rows) == [expected]


def test_convert_multi(fresh_db):
    table = fresh_db.table("table")
    table.insert({"title": "Mixed Case"})
    table.convert(
        "title",
        lambda v: {
            "upper": v.upper(),
            "lower": v.lower(),
            "both": {
                "upper": v.upper(),
                "lower": v.lower(),
            },
        },
        multi=True,
    )
    assert list(table.rows) == [
        {
            "title": "Mixed Case",
            "upper": "MIXED CASE",
            "lower": "mixed case",
            "both": '{"upper": "MIXED CASE", "lower": "mixed case"}',
        }
    ]


def test_convert_multi_where(fresh_db):
    table = fresh_db.table("table")
    table.insert_all(
        [
            {"id": 1, "title": "One"},
            {"id": 2, "title": "Two"},
        ],
        pk="id",
    )
    table.convert(
        "title",
        lambda v: {"upper": v.upper(), "lower": v.lower()},
        multi=True,
        where="id > ?",
        where_args=[1],
    )
    assert list(table.rows) == [
        {"id": 1, "lower": None, "title": "One", "upper": None},
        {"id": 2, "lower": "two", "title": "Two", "upper": "TWO"},
    ]


def test_convert_multi_exception(fresh_db):
    table = fresh_db.table("table")
    table.insert({"title": "Mixed Case"})
    with pytest.raises(BadMultiValues):
        table.convert("title", lambda v: v.upper(), multi=True)


def test_convert_repeated(fresh_db):
    table = fresh_db.table("table")
    col = "num"
    table.insert({col: 1})
    table.convert(col, lambda x: x * 2)
    table.convert(col, lambda _x: 0)
    assert table.get(1) == {col: 0}

```

### `tests/test_create_table_parser.py`

```py
import sqlite3

import hypothesis.strategies as st
import pytest
from hypothesis import given

from sqlite_utils.create_table_parser import (
    Check,
    ColumnComments,
    ParseError,
    Unique,
    UniqueColumn,
    parse_autoincrement,
    parse_checks,
    parse_column_comments,
    parse_uniques,
)


def test_parse_column_and_table_checks():
    sql = """
        CREATE TABLE people (
            age INTEGER CONSTRAINT positive CHECK (age > 0),
            status TEXT CHECK(status IN ('active', 'inactive')),
            CONSTRAINT adult CHECK(age >= 18)
        )
    """
    assert parse_checks(sql) == [
        Check("age > 0", name="positive", column="age"),
        Check(
            "status IN ('active', 'inactive')",
            column="status",
            options=["active", "inactive"],
        ),
        Check("age >= 18", name="adult"),
    ]
    checks = parse_checks(sql)
    assert checks[0].sql == "CONSTRAINT positive CHECK (age > 0)"
    assert sql[checks[0].start : checks[0].end] == checks[0].sql
    assert checks[1].sql == "CHECK(status IN ('active', 'inactive'))"
    assert sql[checks[2].start : checks[2].end] == checks[2].sql


def test_comments_are_trivia_not_constraints():
    sql = """
        CREATE /* fake CHECK (nope), ( */ TABLE t (
            a INTEGER /* CHECK (a < 0), phantom */,
            b INTEGER CHECK /* between keyword and expression */ (b > 0),
            /* CHECK (also_fake) */ CONSTRAINT upper CHECK(b < 10)
        )
    """
    sqlite3.connect(":memory:").execute(sql)
    assert parse_checks(sql) == [
        Check("b > 0", column="b"),
        Check("b < 10", name="upper"),
    ]


def test_parse_comments_owned_by_columns():
    sql = """
        CREATE TABLE t (
            -- Before id
            id /* Between name and type */ INTEGER /* After id */,
            /* Between column definitions */
            value TEXT CHECK(value != '') /* After value */,
            /* Before a table constraint, not a column */
            CHECK(value != 'forbidden')
        )
    """
    assert parse_column_comments(sql) == {
        "id": ColumnComments(before="-- Before id", after="/* After id */"),
        "value": ColumnComments(
            before="/* Between column definitions */",
            after="/* After value */",
        ),
    }


@pytest.mark.parametrize(
    "expression,expected",
    [
        ("value IN ('one', 'two')", ["one", "two"]),
        ("((value IN ('one', 'two')))", ["one", "two"]),
        ("value NOT IN ('one', 'two')", None),
        ("value IN ('one', 'two') OR enabled", None),
        ("other IN ('one', 'two')", None),
        ("value IN (lower('one'), 'two')", None),
        ('value IN ("other")', None),
    ],
)
def test_options_only_for_exact_literal_in_check(expression, expected):
    sql = f"CREATE TABLE t(value TEXT CHECK({expression}), enabled INTEGER, other TEXT)"
    sqlite3.connect(":memory:").execute(sql)
    assert parse_checks(sql)[0].options == expected


@pytest.mark.parametrize("column", ["💩x", "e\u0301"])
def test_unquoted_unicode_identifiers(column):
    sql = f"CREATE TABLE t({column} INTEGER CHECK({column} > 0))"
    sqlite3.connect(":memory:").execute(sql)
    assert parse_checks(sql) == [Check(f"{column} > 0", column=column)]


@pytest.mark.parametrize(
    "sql",
    [
        "SELECT CHECK(x > 0)",
        "CREATE TABLE t(x INTEGER CHECK(x > 0)",
        "CREATE TABLE t(x TEXT CHECK(x != 'unterminated))",
        "CREATE TABLE t(x INTEGER /* unterminated)",
    ],
)
def test_invalid_sql_raises_parse_error(sql):
    with pytest.raises(ParseError):
        parse_checks(sql)


def test_virtual_table_has_no_checks():
    assert (
        parse_checks("CREATE /* comment */ VIRTUAL TABLE search USING fts5(text)") == []
    )


@pytest.mark.parametrize(
    "sql,expected",
    [
        (
            "CREATE TABLE t(id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT)",
            "id",
        ),
        (
            'CREATE TABLE t("quoted id" INTEGER PRIMARY KEY AUTOINCREMENT)',
            "quoted id",
        ),
        (
            'CREATE TABLE t("autoincrement" INTEGER PRIMARY KEY, value TEXT)',
            None,
        ),
        (
            "CREATE TABLE t(id INTEGER PRIMARY KEY /* AUTOINCREMENT */, value TEXT)",
            None,
        ),
        (
            "CREATE TABLE t(id INTEGER PRIMARY KEY, value TEXT CHECK(value != 'AUTOINCREMENT'))",
            None,
        ),
    ],
)
def test_parse_autoincrement(sql, expected):
    sqlite3.connect(":memory:").execute(sql)
    assert parse_autoincrement(sql) == expected


def test_parse_column_and_table_uniques():
    sql = """
        CREATE TABLE memberships (
            email TEXT COLLATE RTRIM CONSTRAINT unique_email UNIQUE ON CONFLICT IGNORE,
            account_id INTEGER,
            CONSTRAINT unique_membership UNIQUE (
                account_id DESC,
                email COLLATE NOCASE ASC
            ) ON CONFLICT REPLACE
        )
    """
    sqlite3.connect(":memory:").execute(sql)
    assert parse_uniques(sql) == [
        Unique(
            (UniqueColumn("email", collation="RTRIM"),),
            name="unique_email",
            column="email",
            conflict="IGNORE",
        ),
        Unique(
            (
                UniqueColumn("account_id", order="DESC"),
                UniqueColumn("email", collation="NOCASE", order="ASC"),
            ),
            name="unique_membership",
            conflict="REPLACE",
        ),
    ]
    uniques = parse_uniques(sql)
    assert uniques[0].sql == "CONSTRAINT unique_email UNIQUE ON CONFLICT IGNORE"
    assert sql[uniques[1].start : uniques[1].end] == uniques[1].sql


def test_unique_like_text_in_comments_and_checks_is_ignored():
    sql = """
        CREATE TABLE t (
            value TEXT /* UNIQUE ON CONFLICT REPLACE */
                CHECK(value != 'UNIQUE(other)'),
            other TEXT
        )
    """
    sqlite3.connect(":memory:").execute(sql)
    assert parse_uniques(sql) == []


comment_or_space = st.sampled_from(
    [
        " ",
        "\n  ",
        "/* comment with , ( ) and CHECK(fake) */",
        "-- comment with , ( ) and CHECK(fake)\n",
    ]
)


@given(gaps=st.lists(comment_or_space, min_size=5, max_size=5))
def test_comments_and_whitespace_can_separate_check_tokens(gaps):
    sql = (
        f"CREATE{gaps[0]}TABLE{gaps[1]}t{gaps[2]}("
        f"value INTEGER CHECK{gaps[3]}(value{gaps[4]}> 0))"
    )
    connection = sqlite3.connect(":memory:")
    connection.execute(sql)
    stored_sql = connection.execute(
        "select sql from sqlite_master where name = 't'"
    ).fetchone()[0]
    assert parse_checks(stored_sql) == [Check(f"value{gaps[4]}> 0", column="value")]


safe_string_text = st.text(
    alphabet=st.characters(
        blacklist_categories=("Cc", "Cs"),
        blacklist_characters=("'",),
    ),
    max_size=40,
)


@given(value=safe_string_text)
def test_check_like_text_inside_strings_is_opaque(value):
    sql = f"CREATE TABLE t(value TEXT CHECK(value != '{value}'))"
    connection = sqlite3.connect(":memory:")
    connection.execute(sql)
    stored_sql = connection.execute(
        "select sql from sqlite_master where name = 't'"
    ).fetchone()[0]
    checks = parse_checks(stored_sql)
    assert len(checks) == 1
    assert checks[0].column == "value"
    assert checks[0].check == f"value != '{value}'"

```

### `tests/test_create_view.py`

```py
import pytest

from sqlite_utils.utils import OperationalError


def test_create_view(fresh_db):
    fresh_db.create_view("bar", "select 1 + 1")
    rows = fresh_db.execute("select * from bar").fetchall()
    assert [(2,)] == rows


def test_create_view_error(fresh_db):
    fresh_db.create_view("bar", "select 1 + 1")
    with pytest.raises(OperationalError):
        fresh_db.create_view("bar", "select 1 + 2")


def test_create_view_only_arrow_one_param(fresh_db):
    with pytest.raises(ValueError):
        fresh_db.create_view("bar", "select 1 + 2", ignore=True, replace=True)


def test_create_view_ignore(fresh_db):
    fresh_db.create_view("bar", "select 1 + 1").create_view(
        "bar", "select 1 + 2", ignore=True
    )
    rows = fresh_db.execute("select * from bar").fetchall()
    assert [(2,)] == rows


def test_create_view_replace(fresh_db):
    fresh_db.create_view("bar", "select 1 + 1").create_view(
        "bar", "select 1 + 2", replace=True
    )
    rows = fresh_db.execute("select * from bar").fetchall()
    assert [(3,)] == rows


def test_create_view_replace_with_same_does_nothing(fresh_db):
    fresh_db.create_view("bar", "select 1 + 1")
    initial_version = fresh_db.execute("PRAGMA schema_version").fetchone()[0]
    fresh_db.create_view("bar", "select 1 + 1", replace=True)
    after_version = fresh_db.execute("PRAGMA schema_version").fetchone()[0]
    assert after_version == initial_version

```

### `tests/test_create.py`

```py
import collections
import datetime
import decimal
import json
import pathlib
import uuid

import pytest

from sqlite_utils import ANY
from sqlite_utils.db import (
    AlterError,
    Database,
    DescIndex,
    ForeignKey,
    Index,
    InvalidColumns,
    NoObviousTable,
    NoTable,
    NoView,
    OperationalError,
    Table,
    View,
)
from sqlite_utils.utils import hash_record, sqlite3

try:
    import pandas as pd  # type: ignore
except ImportError:
    pd = None  # type: ignore


def test_create_table(fresh_db):
    assert [] == fresh_db.table_names()
    table = fresh_db.create_table(
        "test_table",
        {
            "text_col": str,
            "float_col": float,
            "int_col": int,
            "bool_col": bool,
            "bytes_col": bytes,
            "datetime_col": datetime.datetime,
        },
    )
    assert ["test_table"] == fresh_db.table_names()
    assert [
        {"name": "text_col", "type": "TEXT"},
        {"name": "float_col", "type": "REAL"},
        {"name": "int_col", "type": "INTEGER"},
        {"name": "bool_col", "type": "INTEGER"},
        {"name": "bytes_col", "type": "BLOB"},
        {"name": "datetime_col", "type": "TEXT"},
    ] == [{"name": col.name, "type": col.type} for col in table.columns]
    assert (
        'CREATE TABLE "test_table" (\n'
        '   "text_col" TEXT,\n'
        '   "float_col" REAL,\n'
        '   "int_col" INTEGER,\n'
        '   "bool_col" INTEGER,\n'
        '   "bytes_col" BLOB,\n'
        '   "datetime_col" TEXT\n'
        ")"
    ) == table.schema


def test_create_table_compound_primary_key(fresh_db):
    table = fresh_db.create_table(
        "test_table", {"id1": str, "id2": str, "value": int}, pk=("id1", "id2")
    )
    assert (
        'CREATE TABLE "test_table" (\n'
        '   "id1" TEXT,\n'
        '   "id2" TEXT,\n'
        '   "value" INTEGER,\n'
        '   PRIMARY KEY ("id1", "id2")\n'
        ")"
    ) == table.schema
    assert ["id1", "id2"] == table.pks


@pytest.mark.parametrize("pk", ("id", ["id"]))
def test_create_table_with_single_primary_key(fresh_db, pk):
    fresh_db.table("foo").insert({"id": 1}, pk=pk)
    assert (
        fresh_db.table("foo").schema
        == 'CREATE TABLE "foo" (\n   "id" INTEGER PRIMARY KEY\n)'
    )


def test_create_table_with_special_column_characters(fresh_db):
    # With double-quote escaping, columns with special characters are now valid
    table = fresh_db.create_table("players", {"name[foo]": str})
    assert ["players"] == fresh_db.table_names()
    assert [{"name": "name[foo]", "type": "TEXT"}] == [
        {"name": col.name, "type": col.type} for col in table.columns
    ]


def test_create_table_with_defaults(fresh_db):
    table = fresh_db.create_table(
        "players",
        {"name": str, "score": int},
        defaults={"score": 1, "name": "bob''bob"},
    )
    assert ["players"] == fresh_db.table_names()
    assert [{"name": "name", "type": "TEXT"}, {"name": "score", "type": "INTEGER"}] == [
        {"name": col.name, "type": col.type} for col in table.columns
    ]
    assert (
        "CREATE TABLE \"players\" (\n   \"name\" TEXT DEFAULT 'bob''''bob',\n   \"score\" INTEGER DEFAULT 1\n)"
    ) == table.schema


def test_create_table_with_bad_not_null(fresh_db):
    with pytest.raises(ValueError):
        fresh_db.create_table(
            "players", {"name": str, "score": int}, not_null={"mouse"}
        )


def test_create_table_with_not_null(fresh_db):
    table = fresh_db.create_table(
        "players",
        {"name": str, "score": int},
        not_null={"name", "score"},
        defaults={"score": 3},
    )
    assert ["players"] == fresh_db.table_names()
    assert [{"name": "name", "type": "TEXT"}, {"name": "score", "type": "INTEGER"}] == [
        {"name": col.name, "type": col.type} for col in table.columns
    ]
    assert (
        'CREATE TABLE "players" (\n   "name" TEXT NOT NULL,\n   "score" INTEGER NOT NULL DEFAULT 3\n)'
    ) == table.schema


@pytest.mark.parametrize(
    "example,expected_columns",
    (
        (
            {"name": "Ravi", "age": 63},
            [{"name": "name", "type": "TEXT"}, {"name": "age", "type": "INTEGER"}],
        ),
        (
            {"create": "Reserved word", "table": "Another"},
            [{"name": "create", "type": "TEXT"}, {"name": "table", "type": "TEXT"}],
        ),
        ({"day": datetime.time(11, 0)}, [{"name": "day", "type": "TEXT"}]),
        ({"decimal": decimal.Decimal("1.2")}, [{"name": "decimal", "type": "REAL"}]),
        (
            {"memoryview": memoryview(b"hello")},
            [{"name": "memoryview", "type": "BLOB"}],
        ),
        ({"uuid": uuid.uuid4()}, [{"name": "uuid", "type": "TEXT"}]),
        ({"foo[bar]": 1}, [{"name": "foo[bar]", "type": "INTEGER"}]),
        (
            {"timedelta": datetime.timedelta(hours=1)},
            [{"name": "timedelta", "type": "TEXT"}],
        ),
    ),
)
def test_create_table_from_example(fresh_db, example, expected_columns):
    people_table = fresh_db.table("people")
    assert people_table.last_rowid is None
    assert people_table.last_pk is None
    people_table.insert(example)
    assert people_table.last_rowid == 1
    assert people_table.last_pk == 1
    assert ["people"] == fresh_db.table_names()
    assert expected_columns == [
        {"name": col.name, "type": col.type} for col in fresh_db.table("people").columns
    ]


def test_create_table_from_example_with_compound_primary_keys(fresh_db):
    record = {"name": "Zhang", "group": "staff", "employee_id": 2}
    table = fresh_db.table("people").insert(record, pk=("group", "employee_id"))
    assert ["group", "employee_id"] == table.pks
    assert record == table.get(("staff", 2))


@pytest.mark.parametrize(
    "method_name", ("insert", "upsert", "insert_all", "upsert_all")
)
@pytest.mark.parametrize("use_old_upsert", (False, True))
def test_create_table_with_custom_columns(method_name, use_old_upsert):
    db = Database(memory=True, use_old_upsert=use_old_upsert)
    table = db.table("dogs")
    method = getattr(table, method_name)
    record = {"id": 1, "name": "Cleo", "age": "5"}
    if method_name.endswith("_all"):
        record = [record]
    method(record, pk="id", columns={"age": int, "weight": float})
    assert ["dogs"] == db.table_names()
    expected_columns = [
        {"name": "id", "type": "INTEGER"},
        {"name": "name", "type": "TEXT"},
        {"name": "age", "type": "INTEGER"},
        {"name": "weight", "type": "REAL"},
    ]
    assert expected_columns == [
        {"name": col.name, "type": col.type} for col in table.columns
    ]
    assert [{"id": 1, "name": "Cleo", "age": 5, "weight": None}] == list(table.rows)


@pytest.mark.parametrize("use_table_factory", [True, False])
def test_create_table_column_order(fresh_db, use_table_factory):
    row = collections.OrderedDict(
        (
            ("zzz", "third"),
            ("abc", "first"),
            ("ccc", "second"),
            ("bbb", "second-to-last"),
            ("aaa", "last"),
        )
    )
    column_order = ("abc", "ccc", "zzz")
    if use_table_factory:
        fresh_db.table("table", column_order=column_order).insert(row)
    else:
        fresh_db.table("table").insert(row, column_order=column_order)
    assert [
        {"name": "abc", "type": "TEXT"},
        {"name": "ccc", "type": "TEXT"},
        {"name": "zzz", "type": "TEXT"},
        {"name": "bbb", "type": "TEXT"},
        {"name": "aaa", "type": "TEXT"},
    ] == [
        {"name": col.name, "type": col.type} for col in fresh_db.table("table").columns
    ]


@pytest.mark.parametrize(
    "foreign_key_specification,expected_exception",
    (
        # You can specify triples, pairs, or a list of columns
        ((("one_id", "one", "id"), ("two_id", "two", "id")), False),
        ((("one_id", "one"), ("two_id", "two")), False),
        (("one_id", "two_id"), False),
        # You can also specify ForeignKey tuples:
        (
            (
                ForeignKey("m2m", "one_id", "one", "id"),
                ForeignKey("m2m", "two_id", "two", "id"),
            ),
            False,
        ),
        # If you specify a column that doesn't point to a table, you  get an error:
        (("one_id", "two_id", "three_id"), NoObviousTable),
        # Tuples of the wrong length get an error:
        ((("one_id", "one", "id", "five"), ("two_id", "two", "id")), ValueError),
        # Likewise a bad column:
        ((("one_id", "one", "id2"),), AlterError),
        # Or a list of dicts
        (({"one_id": "one"},), ValueError),
    ),
)
@pytest.mark.parametrize("use_table_factory", [True, False])
def test_create_table_works_for_m2m_with_only_foreign_keys(
    fresh_db, foreign_key_specification, expected_exception, use_table_factory
):
    if use_table_factory:
        fresh_db.table("one", pk="id").insert({"id": 1})
        fresh_db.table("two", pk="id").insert({"id": 1})
    else:
        fresh_db.table("one").insert({"id": 1}, pk="id")
        fresh_db.table("two").insert({"id": 1}, pk="id")

    row = {"one_id": 1, "two_id": 1}

    def do_it():
        if use_table_factory:
            fresh_db.table("m2m", foreign_keys=foreign_key_specification).insert(row)
        else:
            fresh_db.table("m2m").insert(row, foreign_keys=foreign_key_specification)

    if expected_exception:
        with pytest.raises(expected_exception):
            do_it()
        return
    else:
        do_it()
    assert [
        {"name": "one_id", "type": "INTEGER"},
        {"name": "two_id", "type": "INTEGER"},
    ] == [{"name": col.name, "type": col.type} for col in fresh_db.table("m2m").columns]
    assert sorted(
        [
            {"column": "one_id", "other_table": "one", "other_column": "id"},
            {"column": "two_id", "other_table": "two", "other_column": "id"},
        ],
        key=lambda s: repr(s),
    ) == sorted(
        [
            {
                "column": fk.column,
                "other_table": fk.other_table,
                "other_column": fk.other_column,
            }
            for fk in fresh_db.table("m2m").foreign_keys
        ],
        key=lambda s: repr(s),
    )


def test_self_referential_foreign_key(fresh_db):
    assert [] == fresh_db.table_names()
    table = fresh_db.create_table(
        "test_table",
        columns={
            "id": int,
            "ref": int,
        },
        pk="id",
        foreign_keys=(("ref", "test_table", "id"),),
    )
    assert (
        'CREATE TABLE "test_table" (\n'
        '   "id" INTEGER PRIMARY KEY,\n'
        '   "ref" INTEGER REFERENCES "test_table"("id")\n'
        ")"
    ) == table.schema


def test_create_error_if_invalid_foreign_keys(fresh_db):
    with pytest.raises(AlterError):
        fresh_db.table("one").insert(
            {"id": 1, "ref_id": 3},
            pk="id",
            foreign_keys=(("ref_id", "bad_table", "bad_column"),),
        )


def test_create_error_if_invalid_self_referential_foreign_keys(fresh_db):
    with pytest.raises(AlterError) as ex:
        fresh_db.table("one").insert(
            {"id": 1, "ref_id": 3},
            pk="id",
            foreign_keys=(("ref_id", "one", "bad_column"),),
        )
        assert ex.value.args == ("No such column: one.bad_column",)


@pytest.mark.parametrize(
    "col_name,col_type,not_null_default,expected_schema",
    (
        (
            "nickname",
            str,
            None,
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "nickname" TEXT)',
        ),
        (
            "dob",
            datetime.date,
            None,
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "dob" TEXT)',
        ),
        ("age", int, None, 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "age" INTEGER)'),
        (
            "weight",
            float,
            None,
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "weight" REAL)',
        ),
        ("text", "TEXT", None, 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "text" TEXT)'),
        (
            "integer",
            "INTEGER",
            None,
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "integer" INTEGER)',
        ),
        (
            "float",
            "FLOAT",
            None,
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "float" FLOAT)',
        ),
        ("blob", "blob", None, 'CREATE TABLE "dogs" (\n   "name" TEXT\n, "blob" BLOB)'),
        (
            "default_str",
            None,
            None,
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "default_str" TEXT)',
        ),
        (
            "nickname",
            str,
            "",
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "nickname" TEXT NOT NULL DEFAULT \'\')',
        ),
        (
            "nickname",
            str,
            "dawg's dawg",
            'CREATE TABLE "dogs" (\n   "name" TEXT\n, "nickname" TEXT NOT NULL DEFAULT \'dawg\'\'s dawg\')',
        ),
    ),
)
def test_add_column(fresh_db, col_name, col_type, not_null_default, expected_schema):
    fresh_db.create_table("dogs", {"name": str})
    assert fresh_db.table("dogs").schema == 'CREATE TABLE "dogs" (\n   "name" TEXT\n)'
    fresh_db.table("dogs").add_column(
        col_name, col_type, not_null_default=not_null_default
    )
    assert fresh_db.table("dogs").schema == expected_schema


def test_add_foreign_key(fresh_db):
    fresh_db.table("authors").insert_all(
        [{"id": 1, "name": "Sally"}, {"id": 2, "name": "Asheesh"}], pk="id"
    )
    fresh_db.table("books").insert_all(
        [
            {"title": "Hedgehogs of the world", "author_id": 1},
            {"title": "How to train your wolf", "author_id": 2},
        ]
    )
    assert [] == fresh_db.table("books").foreign_keys
    t = fresh_db.table("books").add_foreign_key("author_id", "authors", "id")
    # Ensure it returned self:
    assert isinstance(t, Table) and t.name == "books"
    assert [
        ForeignKey(
            table="books", column="author_id", other_table="authors", other_column="id"
        )
    ] == fresh_db.table("books").foreign_keys


def test_add_foreign_key_if_column_contains_space(fresh_db):
    fresh_db.table("authors").insert_all([{"id": 1, "name": "Sally"}], pk="id")
    fresh_db.table("books").insert_all(
        [
            {"title": "Hedgehogs of the world", "author id": 1},
        ]
    )
    fresh_db.table("books").add_foreign_key("author id", "authors", "id")
    assert fresh_db.table("books").foreign_keys == [
        ForeignKey(
            table="books", column="author id", other_table="authors", other_column="id"
        )
    ]


def test_add_foreign_key_error_if_column_does_not_exist(fresh_db):
    fresh_db.table("books").insert(
        {"id": 1, "title": "Hedgehogs of the world", "author_id": 1}
    )
    with pytest.raises(AlterError):
        fresh_db.table("books").add_foreign_key("author2_id", "books", "id")


def test_add_foreign_key_error_if_other_table_does_not_exist(fresh_db):
    fresh_db.table("books").insert({"title": "Hedgehogs of the world", "author_id": 1})
    with pytest.raises(AlterError):
        fresh_db.table("books").add_foreign_key("author_id", "authors", "id")


def test_add_foreign_key_error_if_already_exists(fresh_db):
    fresh_db.table("books").insert({"title": "Hedgehogs of the world", "author_id": 1})
    fresh_db.table("authors").insert({"id": 1, "name": "Sally"}, pk="id")
    fresh_db.table("books").add_foreign_key("author_id", "authors", "id")
    with pytest.raises(AlterError) as ex:
        fresh_db.table("books").add_foreign_key("author_id", "authors", "id")
    assert "Foreign key already exists for author_id => authors.id" == ex.value.args[0]


def test_add_foreign_key_no_error_if_exists_and_ignore_true(fresh_db):
    fresh_db.table("books").insert({"title": "Hedgehogs of the world", "author_id": 1})
    fresh_db.table("authors").insert({"id": 1, "name": "Sally"}, pk="id")
    fresh_db.table("books").add_foreign_key("author_id", "authors", "id")
    fresh_db.table("books").add_foreign_key("author_id", "authors", "id", ignore=True)


def test_add_foreign_keys(fresh_db):
    fresh_db.table("authors").insert_all(
        [{"id": 1, "name": "Sally"}, {"id": 2, "name": "Asheesh"}], pk="id"
    )
    fresh_db.table("categories").insert_all([{"id": 1, "name": "Wildlife"}], pk="id")
    fresh_db.table("books").insert_all(
        [{"title": "Hedgehogs of the world", "author_id": 1, "category_id": 1}]
    )
    assert [] == fresh_db.table("books").foreign_keys
    fresh_db.add_foreign_keys(
        [
            ("books", "author_id", "authors", "id"),
            ("books", "category_id", "categories", "id"),
        ]
    )
    assert [
        ForeignKey(
            table="books", column="author_id", other_table="authors", other_column="id"
        ),
        ForeignKey(
            table="books",
            column="category_id",
            other_table="categories",
            other_column="id",
        ),
    ] == sorted(fresh_db.table("books").foreign_keys)


def test_add_column_foreign_key(fresh_db):
    fresh_db.create_table("dogs", {"name": str})
    fresh_db.create_table("breeds", {"name": str})
    fresh_db.table("dogs").add_column("breed_id", fk="breeds")
    assert fresh_db.table("dogs").schema == (
        'CREATE TABLE "dogs" (\n'
        '   "name" TEXT,\n'
        '   "breed_id" INTEGER REFERENCES "breeds"("rowid")\n'
        ")"
    )
    # And again with an explicit primary key column
    fresh_db.create_table("subbreeds", {"name": str, "primkey": str}, pk="primkey")
    fresh_db.table("dogs").add_column("subbreed_id", fk="subbreeds")
    assert fresh_db.table("dogs").schema == (
        'CREATE TABLE "dogs" (\n'
        '   "name" TEXT,\n'
        '   "breed_id" INTEGER REFERENCES "breeds"("rowid"),\n'
        '   "subbreed_id" TEXT REFERENCES "subbreeds"("primkey")\n'
        ")"
    )


def test_add_foreign_key_guess_table(fresh_db):
    fresh_db.create_table("dogs", {"name": str})
    fresh_db.create_table("breeds", {"name": str, "id": int}, pk="id")
    fresh_db.table("dogs").add_column("breed_id", int)
    fresh_db.table("dogs").add_foreign_key("breed_id")
    assert fresh_db.table("dogs").schema == (
        'CREATE TABLE "dogs" (\n'
        '   "name" TEXT,\n'
        '   "breed_id" INTEGER REFERENCES "breeds"("id")\n'
        ")"
    )


def test_index_foreign_keys(fresh_db):
    test_add_foreign_key_guess_table(fresh_db)
    assert [] == fresh_db.table("dogs").indexes
    fresh_db.index_foreign_keys()
    assert [["breed_id"]] == [i.columns for i in fresh_db.table("dogs").indexes]
    # Calling it a second time should do nothing
    fresh_db.index_foreign_keys()
    assert [["breed_id"]] == [i.columns for i in fresh_db.table("dogs").indexes]


def test_index_foreign_keys_if_index_name_is_already_used(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/335
    test_add_foreign_key_guess_table(fresh_db)
    # Add index with a name that will conflict with index_foreign_keys()
    fresh_db.table("dogs").create_index(["name"], index_name="idx_dogs_breed_id")
    fresh_db.index_foreign_keys()
    assert {
        (idx.name, tuple(idx.columns)) for idx in fresh_db.table("dogs").indexes
    } == {
        ("idx_dogs_breed_id_2", ("breed_id",)),
        ("idx_dogs_breed_id", ("name",)),
    }


@pytest.mark.parametrize(
    "extra_data,expected_new_columns",
    [
        ({"species": "squirrels"}, [{"name": "species", "type": "TEXT"}]),
        (
            {"species": "squirrels", "hats": 5},
            [{"name": "species", "type": "TEXT"}, {"name": "hats", "type": "INTEGER"}],
        ),
        (
            {"hats": 5, "rating": 3.5},
            [{"name": "hats", "type": "INTEGER"}, {"name": "rating", "type": "REAL"}],
        ),
    ],
)
@pytest.mark.parametrize("use_table_factory", [True, False])
def test_insert_row_alter_table(
    fresh_db, extra_data, expected_new_columns, use_table_factory
):
    table = fresh_db.table("books")
    table.insert({"title": "Hedgehogs of the world", "author_id": 1})
    assert [
        {"name": "title", "type": "TEXT"},
        {"name": "author_id", "type": "INTEGER"},
    ] == [{"name": col.name, "type": col.type} for col in table.columns]
    record = {"title": "Squirrels of the world", "author_id": 2}
    record.update(extra_data)
    if use_table_factory:
        fresh_db.table("books", alter=True).insert(record)
    else:
        fresh_db.table("books").insert(record, alter=True)
    assert [
        {"name": "title", "type": "TEXT"},
        {"name": "author_id", "type": "INTEGER"},
    ] + expected_new_columns == [
        {"name": col.name, "type": col.type} for col in table.columns
    ]


def test_add_missing_columns_case_insensitive(fresh_db):
    table = fresh_db.table("foo")
    table.insert({"id": 1, "name": "Cleo"}, pk="id")
    table.add_missing_columns([{"Name": ".", "age": 4}])
    assert (
        table.schema
        == 'CREATE TABLE "foo" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT\n, "age" INTEGER)'
    )


@pytest.mark.parametrize("use_table_factory", [True, False])
def test_insert_replace_rows_alter_table(fresh_db, use_table_factory):
    first_row = {"id": 1, "title": "Hedgehogs of the world", "author_id": 1}
    next_rows = [
        {"id": 1, "title": "Hedgehogs of the World", "species": "hedgehogs"},
        {"id": 2, "title": "Squirrels of the World", "num_species": 200},
        {
            "id": 3,
            "title": "Badgers of the World",
            "significant_continents": ["Europe", "North America"],
        },
    ]
    if use_table_factory:
        table = fresh_db.table("books", pk="id", alter=True)
        table.insert(first_row)
        table.insert_all(next_rows, replace=True)
    else:
        table = fresh_db.table("books")
        table.insert(first_row, pk="id")
        table.insert_all(next_rows, alter=True, replace=True)
    assert {
        "author_id": int,
        "id": int,
        "num_species": int,
        "significant_continents": str,
        "species": str,
        "title": str,
    } == table.columns_dict
    assert [
        {
            "author_id": None,
            "id": 1,
            "num_species": None,
            "significant_continents": None,
            "species": "hedgehogs",
            "title": "Hedgehogs of the World",
        },
        {
            "author_id": None,
            "id": 2,
            "num_species": 200,
            "significant_continents": None,
            "species": None,
            "title": "Squirrels of the World",
        },
        {
            "author_id": None,
            "id": 3,
            "num_species": None,
            "significant_continents": '["Europe", "North America"]',
            "species": None,
            "title": "Badgers of the World",
        },
    ] == list(table.rows)


def test_insert_all_with_extra_columns_in_later_chunks(fresh_db):
    chunk = [
        {"record": "Record 1"},
        {"record": "Record 2"},
        {"record": "Record 3"},
        {"record": "Record 4", "extra": 1},
    ]
    fresh_db.table("t").insert_all(chunk, batch_size=2, alter=True)
    assert list(fresh_db.table("t").rows) == [
        {"record": "Record 1", "extra": None},
        {"record": "Record 2", "extra": None},
        {"record": "Record 3", "extra": None},
        {"record": "Record 4", "extra": 1},
    ]


def test_bulk_insert_more_than_999_values(fresh_db):
    "Inserting 100 items with 11 columns should work"
    fresh_db.table("big").insert_all(
        (
            {
                "id": i + 1,
                "c2": 2,
                "c3": 3,
                "c4": 4,
                "c5": 5,
                "c6": 6,
                "c7": 7,
                "c8": 8,
                "c9": 9,
                "c10": 10,
                "c11": 11,
            }
            for i in range(100)
        ),
        pk="id",
    )
    assert fresh_db.table("big").count == 100


@pytest.mark.parametrize(
    "num_columns,should_error", ((900, False), (999, False), (1000, True))
)
def test_error_if_more_than_999_columns(fresh_db, num_columns, should_error):
    record = {f"c{i}": i for i in range(num_columns)}
    if should_error:
        with pytest.raises(ValueError):
            fresh_db.table("big").insert(record)
    else:
        fresh_db.table("big").insert(record)


def test_columns_not_in_first_record_should_not_cause_batch_to_be_too_large(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/145
    # sqlite on homebrew and Debian/Ubuntu etc. is typically compiled with
    #  SQLITE_MAX_VARIABLE_NUMBER set to 250,000, so we need to exceed this value to
    #  trigger the error on these systems.
    THRESHOLD = 250000
    batch_size = 999
    extra_columns = 1 + (THRESHOLD - 1) // (batch_size - 1)
    records = [
        {"c0": "first record"},  # one column in first record -> batch size = 999
        # fill out the batch with 99 records with enough columns to exceed THRESHOLD
        *[{f"c{i}": j for i in range(extra_columns)} for j in range(batch_size - 1)],
    ]
    fresh_db.table("too_many_columns").insert_all(
        records, alter=True, batch_size=batch_size
    )


@pytest.mark.parametrize(
    "columns,index_name,expected_index",
    (
        (
            ["is good dog"],
            None,
            Index(
                seq=0,
                name="idx_dogs_is good dog",
                unique=0,
                origin="c",
                partial=0,
                columns=["is good dog"],
            ),
        ),
        (
            ["is good dog", "age"],
            None,
            Index(
                seq=0,
                name="idx_dogs_is good dog_age",
                unique=0,
                origin="c",
                partial=0,
                columns=["is good dog", "age"],
            ),
        ),
        (
            ["age"],
            "age_index",
            Index(
                seq=0,
                name="age_index",
                unique=0,
                origin="c",
                partial=0,
                columns=["age"],
            ),
        ),
    ),
)
def test_create_index(fresh_db, columns, index_name, expected_index):
    dogs = fresh_db.table("dogs")
    dogs.insert({"name": "Cleo", "twitter": "cleopaws", "age": 3, "is good dog": True})
    assert [] == dogs.indexes
    dogs.create_index(columns, index_name)
    assert expected_index == dogs.indexes[0]


def test_create_index_unique(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"name": "Cleo", "twitter": "cleopaws", "age": 3, "is_good_dog": True})
    assert [] == dogs.indexes
    dogs.create_index(["name"], unique=True)
    assert (
        Index(
            seq=0,
            name="idx_dogs_name",
            unique=1,
            origin="c",
            partial=0,
            columns=["name"],
        )
        == dogs.indexes[0]
    )


def test_create_index_if_not_exists(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"name": "Cleo", "twitter": "cleopaws", "age": 3, "is_good_dog": True})
    assert [] == dogs.indexes
    dogs.create_index(["name"])
    assert len(dogs.indexes) == 1
    with pytest.raises(Exception, match="index idx_dogs_name already exists"):
        dogs.create_index(["name"])
    dogs.create_index(["name"], if_not_exists=True)


def test_drop_index(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"name": "Cleo", "twitter": "cleopaws", "age": 3, "is_good_dog": True})
    dogs.create_index(["name"])
    assert [index.name for index in dogs.indexes] == ["idx_dogs_name"]
    dogs.drop_index("idx_dogs_name")
    assert dogs.indexes == []


def test_drop_index_ignore(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"name": "Cleo"})
    with pytest.raises(OperationalError, match="No index named idx_dogs_name"):
        dogs.drop_index("idx_dogs_name")
    dogs.drop_index("idx_dogs_name", ignore=True)


def test_drop_index_wrong_table(fresh_db):
    dogs = fresh_db.table("dogs")
    cats = fresh_db.table("cats")
    dogs.insert({"name": "Cleo"})
    cats.insert({"name": "Misty"})
    dogs.create_index(["name"])
    with pytest.raises(OperationalError, match="No index named idx_dogs_name"):
        cats.drop_index("idx_dogs_name")
    assert [index.name for index in dogs.indexes] == ["idx_dogs_name"]


def test_create_index_desc(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"name": "Cleo", "twitter": "cleopaws", "age": 3, "is good dog": True})
    assert [] == dogs.indexes
    dogs.create_index([DescIndex("age"), "name"])
    sql = fresh_db.execute(
        "select sql from sqlite_master where name='idx_dogs_age_name'"
    ).fetchone()[0]
    assert sql == (
        'CREATE INDEX "idx_dogs_age_name"\n' '    ON "dogs" ("age" desc, "name")'
    )


def test_create_index_find_unique_name(fresh_db):
    table = fresh_db.table("t")
    table.insert({"id": 1})
    table.create_index(["id"])
    # Without find_unique_name should error
    with pytest.raises(OperationalError, match="index idx_t_id already exists"):
        table.create_index(["id"])
    # With find_unique_name=True it should work
    table.create_index(["id"], find_unique_name=True)
    table.create_index(["id"], find_unique_name=True)
    # Should have three now
    index_names = {idx.name for idx in table.indexes}
    assert index_names == {"idx_t_id", "idx_t_id_2", "idx_t_id_3"}


def test_create_index_analyze(fresh_db):
    dogs = fresh_db.table("dogs")
    assert "sqlite_stat1" not in fresh_db.table_names()
    dogs.insert({"name": "Cleo", "twitter": "cleopaws"})
    dogs.create_index(["name"], analyze=True)
    assert "sqlite_stat1" in fresh_db.table_names()
    assert list(fresh_db.table("sqlite_stat1").rows) == [
        {"tbl": "dogs", "idx": "idx_dogs_name", "stat": "1 1"}
    ]


@pytest.mark.parametrize(
    "data_structure",
    (
        ["list with one item"],
        ["list with", "two items"],
        {"dictionary": "simple"},
        {"dictionary": {"nested": "complex"}},
        collections.OrderedDict(
            [
                ("key1", {"nested": ["cømplex"]}),
                ("key2", "foo"),
            ]
        ),
        [{"list": "of"}, {"two": "dicts"}],
    ),
)
def test_insert_dictionaries_and_lists_as_json(fresh_db, data_structure):
    fresh_db.table("test").insert({"id": 1, "data": data_structure}, pk="id")
    row = fresh_db.execute("select id, data from test").fetchone()
    assert row[0] == 1
    assert data_structure == json.loads(row[1])


def test_insert_list_nested_unicode(fresh_db):
    fresh_db.table("test").insert(
        {"id": 1, "data": {"key1": {"nested": ["cømplex"]}}}, pk="id"
    )
    row = fresh_db.execute("select id, data from test").fetchone()
    assert row[1] == '{"key1": {"nested": ["cømplex"]}}'


def test_insert_uuid(fresh_db):
    uuid4 = uuid.uuid4()
    fresh_db.table("test").insert({"uuid": uuid4})
    row = next(iter(fresh_db.table("test").rows))
    assert {"uuid"} == row.keys()
    assert isinstance(row["uuid"], str)
    assert row["uuid"] == str(uuid4)


def test_insert_memoryview(fresh_db):
    fresh_db.table("test").insert({"data": memoryview(b"hello")})
    row = next(iter(fresh_db.table("test").rows))
    assert {"data"} == row.keys()
    assert isinstance(row["data"], bytes)
    assert row["data"] == b"hello"


def test_insert_thousands_using_generator(fresh_db):
    fresh_db.table("test").insert_all(
        {"i": i, "word": f"word_{i}"} for i in range(10000)
    )
    assert [{"name": "i", "type": "INTEGER"}, {"name": "word", "type": "TEXT"}] == [
        {"name": col.name, "type": col.type} for col in fresh_db.table("test").columns
    ]
    assert fresh_db.table("test").count == 10000


def test_insert_thousands_raises_exception_with_extra_columns_after_first_100(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/139
    with pytest.raises(Exception, match="table test has no column named extra"):
        fresh_db.table("test").insert_all(
            [{"i": i, "word": f"word_{i}"} for i in range(100)]
            + [{"i": 101, "extra": "This extra column should cause an exception"}],
        )


def test_insert_thousands_adds_extra_columns_after_first_100_with_alter(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/139
    fresh_db.table("test").insert_all(
        [{"i": i, "word": f"word_{i}"} for i in range(100)]
        + [{"i": 101, "extra": "Should trigger ALTER"}],
        alter=True,
    )
    rows = list(fresh_db.query("select * from test where i = 101"))
    assert rows == [{"i": 101, "word": None, "extra": "Should trigger ALTER"}]


@pytest.mark.parametrize("num_rows", (0, 1, 2, 3, 10))
def test_insert_all_pk_not_in_records_raises(fresh_db, num_rows):
    # https://github.com/simonw/sqlite-utils/issues/732
    fresh_db.conn.execute("CREATE TABLE t (a TEXT, b INT, PRIMARY KEY (a, b))")
    rows = [{"a": f"x{i}", "b": i} for i in range(num_rows)]

    with pytest.raises(InvalidColumns) as ex:
        fresh_db.table("t").insert_all(rows, pk="not_a_column")

    assert ex.value.args == (
        "Invalid primary key column ['not_a_column'] for table t with columns ['a', 'b']",
    )
    assert fresh_db.table("t").count == 0


@pytest.mark.parametrize("num_rows", (1, 2, 3, 10))
def test_insert_all_pk_not_in_records_alter_raises(fresh_db, num_rows):
    # With alter=True the check is deferred until the record keys are
    # known - a pk column that is in neither the table nor the records
    # still raises
    fresh_db.conn.execute("CREATE TABLE t (a TEXT, b INT, PRIMARY KEY (a, b))")
    rows = [{"a": f"x{i}", "b": i} for i in range(num_rows)]

    with pytest.raises(InvalidColumns) as ex:
        fresh_db.table("t").insert_all(rows, pk="not_a_column", alter=True)

    assert ex.value.args == (
        "Invalid primary key column ['not_a_column'] for table t with columns ['a', 'b']",
    )
    assert fresh_db.table("t").count == 0


def test_insert_pk_in_records_with_alter_adds_column(fresh_db):
    # 3.x allowed insert(pk=..., alter=True) to add the pk column from the
    # records - the InvalidColumns check must not fire in that case
    fresh_db.table("t").insert({"a": 1})
    fresh_db.table("t").insert({"id": 5, "a": 2}, pk="id", alter=True)
    assert fresh_db.table("t").columns_dict.keys() == {"a", "id"}
    assert list(fresh_db.query("select * from t order by a")) == [
        {"a": 1, "id": None},
        {"a": 2, "id": 5},
    ]


def test_insert_all_invalid_pk_alter_empty_records_is_noop(fresh_db):
    # With alter=True the pk check needs record keys, so an empty iterator
    # returns without error - matching the 3.x no-op for empty inserts
    fresh_db.conn.execute("CREATE TABLE t (a TEXT)")
    fresh_db.table("t").insert_all([], pk="not_a_column", alter=True)
    assert fresh_db.table("t").count == 0


def test_insert_ignore(fresh_db):
    fresh_db.table("test").insert({"id": 1, "bar": 2}, pk="id")
    # Should raise an error if we try this again
    with pytest.raises(Exception, match="UNIQUE constraint failed"):
        fresh_db.table("test").insert({"id": 1, "bar": 2}, pk="id")
    # Using ignore=True should cause our insert to be silently ignored
    fresh_db.table("test").insert({"id": 1, "bar": 3}, pk="id", ignore=True)
    # Only one row, and it should be bar=2, not bar=3
    rows = list(fresh_db.query("select * from test"))
    assert rows == [{"id": 1, "bar": 2}]


def test_insert_ignore_reports_existing_row(fresh_db):
    # An ignored insert (row already exists) should point last_rowid and
    # last_pk at the existing conflicting row - see the Datasette insert API
    fresh_db.table("docs").insert({"id": 1, "title": "Exists"}, pk="id")
    # Insert a conflicting row with ignore=True and no explicit pk=
    table = fresh_db.table("docs").insert({"id": 1, "title": "One"}, ignore=True)
    assert table.last_rowid == 1
    assert table.last_pk == 1
    assert list(fresh_db.table("docs").rows_where("rowid = ?", [table.last_rowid])) == [
        {"id": 1, "title": "Exists"}
    ]


@pytest.mark.parametrize("rowid_alias", ("rowid", "_rowid_", "oid"))
@pytest.mark.parametrize("method", ("upsert", "insert_replace", "insert_ignore"))
def test_pk_rowid_alias_on_rowid_table(fresh_db, rowid_alias, method):
    # rowid and its aliases are valid primary keys for a rowid table even
    # though they are not listed among the table's columns - see the Datasette
    # upsert API against tables without an explicit primary key
    fresh_db.table("t").insert({"title": "Hello"})
    assert fresh_db.table("t").pks == ["rowid"]
    record = {rowid_alias: 1, "title": "Updated"}
    if method == "upsert":
        table = fresh_db.table("t").upsert(record, pk=rowid_alias)
    elif method == "insert_replace":
        table = fresh_db.table("t").insert(record, pk=rowid_alias, replace=True)
    else:
        table = fresh_db.table("t").insert(record, pk=rowid_alias, ignore=True)
    assert table.last_pk == 1
    expected_title = "Hello" if method == "insert_ignore" else "Updated"
    assert list(fresh_db.table("t").rows) == [{"title": expected_title}]


def test_insert_ignore_reports_existing_row_compound_pk(fresh_db):
    # Compound primary key variant of the ignored-insert lookup
    fresh_db.table("t").insert_all([{"a": 1, "b": 2, "note": "first"}], pk=("a", "b"))
    table = fresh_db.table("t").insert(
        {"a": 1, "b": 2, "note": "second"}, pk=("a", "b"), ignore=True
    )
    assert table.last_pk == (1, 2)
    assert list(fresh_db.table("t").rows_where("rowid = ?", [table.last_rowid])) == [
        {"a": 1, "b": 2, "note": "first"}
    ]


def test_insert_ignore_reports_existing_row_list_mode(fresh_db):
    # List-based iteration variant of the ignored-insert lookup
    fresh_db.table("t").insert_all([["id", "title"], [1, "first"]], pk="id")
    table = fresh_db.table("t").insert_all(
        [["id", "title"], [1, "second"]], pk="id", ignore=True
    )
    assert table.last_pk == 1
    assert table.last_rowid == 1
    assert list(fresh_db.table("t").rows) == [{"id": 1, "title": "first"}]


def test_insert_ignore_hash_id_reports_pk(fresh_db):
    # With hash_id the pk is the computed hash; the original record has no id
    # column to look up so last_rowid is left unset
    first = fresh_db.table("dogs").insert({"name": "Cleo"}, hash_id="id")
    table = fresh_db.table("dogs").insert({"name": "Cleo"}, hash_id="id", ignore=True)
    assert table.last_pk == first.last_pk
    assert table.last_rowid is None
    assert fresh_db.table("dogs").count == 1


def test_insert_ignore_unresolvable_conflict_leaves_pk_unset(fresh_db):
    # When the conflict cannot be resolved to a primary key lookup, last_pk and
    # last_rowid are left unset rather than reporting a misleading value

    # rowid table with a UNIQUE column and no primary key: no pk to look up
    fresh_db.table("u").db.execute("create table u (title text unique)")
    fresh_db.table("u").insert({"title": "x"})
    table = fresh_db.table("u").insert({"title": "x"}, ignore=True)
    assert table.last_pk is None
    assert table.last_rowid is None
    assert fresh_db.table("u").count == 1

    # Conflict on a UNIQUE column other than the primary key: the pk value from
    # the record does not match the existing row, so the lookup finds nothing
    fresh_db.table("docs").db.execute(
        "create table docs (id integer primary key, email text unique)"
    )
    fresh_db.table("docs").insert({"id": 1, "email": "a"}, pk="id")
    table = fresh_db.table("docs").insert({"id": 2, "email": "a"}, ignore=True)
    assert table.last_pk is None
    assert table.last_rowid is None
    assert fresh_db.table("docs").count == 1


def test_insert_ignore_with_pk_after_other_table_insert(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/554
    user = {"id": "abc", "name": "david"}

    fresh_db.table("users").insert(user, pk="id")
    fresh_db.table("comments").insert_all(
        [
            {"id": "def", "text": "ok"},
            {"id": "ghi", "text": "great"},
        ],
    )

    table = fresh_db.table("users").insert(user, pk="id", ignore=True)

    assert table.last_pk == "abc"
    assert list(fresh_db.table("users").rows) == [user]


def test_insert_hash_id(fresh_db):
    dogs = fresh_db.table("dogs")
    id = dogs.insert({"name": "Cleo", "twitter": "cleopaws"}, hash_id="id").last_pk
    assert "f501265970505d9825d8d9f590bfab3519fb20b1" == id
    assert dogs.count == 1
    # Insert replacing a second time should not create a new row
    id2 = dogs.insert(
        {"name": "Cleo", "twitter": "cleopaws"}, hash_id="id", replace=True
    ).last_pk
    assert "f501265970505d9825d8d9f590bfab3519fb20b1" == id2
    assert dogs.count == 1


@pytest.mark.parametrize("use_table_factory", [True, False])
def test_insert_hash_id_columns(fresh_db, use_table_factory):
    if use_table_factory:
        dogs = fresh_db.table("dogs", hash_id_columns=("name", "twitter"))
        insert_kwargs = {}
    else:
        dogs = fresh_db.table("dogs")
        insert_kwargs = {"hash_id_columns": ("name", "twitter")}

    id = dogs.insert(
        {"name": "Cleo", "twitter": "cleopaws", "age": 5},
        **insert_kwargs,
    ).last_pk
    expected_hash = hash_record({"name": "Cleo", "twitter": "cleopaws"})
    assert id == expected_hash
    assert dogs.count == 1
    # Insert replacing a second time should not create a new row
    id2 = dogs.insert(
        {"name": "Cleo", "twitter": "cleopaws", "age": 6},
        **insert_kwargs,
        replace=True,
    ).last_pk
    assert id2 == expected_hash
    assert dogs.count == 1


def test_vacuum(fresh_db):
    fresh_db.table("data").insert({"foo": "foo", "bar": "bar"})
    fresh_db.vacuum()


def test_works_with_pathlib_path(tmpdir):
    path = pathlib.Path(tmpdir / "test.db")
    db = Database(path)
    db.table("demo").insert_all([{"foo": 1}])
    assert db.table("demo").count == 1


@pytest.mark.skipif(pd is None, reason="pandas and numpy are not installed")
def test_create_table_numpy(fresh_db):
    assert pd is not None
    df = pd.DataFrame({"col 1": range(3), "col 2": range(3)})
    fresh_db.table("pandas").insert_all(df.to_dict(orient="records"))
    assert [
        {"col 1": 0, "col 2": 0},
        {"col 1": 1, "col 2": 1},
        {"col 1": 2, "col 2": 2},
    ] == list(fresh_db.table("pandas").rows)
    # Now try all the different types
    df = pd.DataFrame(
        {
            "np.int8": [-8],
            "np.int16": [-16],
            "np.int32": [-32],
            "np.int64": [-64],
            "np.uint8": [8],
            "np.uint16": [16],
            "np.uint32": [32],
            "np.uint64": [64],
            "np.float16": [16.5],
            "np.float32": [32.5],
            "np.float64": [64.5],
        }
    )
    df = df.astype(
        {
            "np.int8": "int8",
            "np.int16": "int16",
            "np.int32": "int32",
            "np.int64": "int64",
            "np.uint8": "uint8",
            "np.uint16": "uint16",
            "np.uint32": "uint32",
            "np.uint64": "uint64",
            "np.float16": "float16",
            "np.float32": "float32",
            "np.float64": "float64",
        }
    )
    assert [
        "int8",
        "int16",
        "int32",
        "int64",
        "uint8",
        "uint16",
        "uint32",
        "uint64",
        "float16",
        "float32",
        "float64",
    ] == [str(t) for t in df.dtypes]
    fresh_db.table("types").insert_all(df.to_dict(orient="records"))
    assert [
        {
            "np.float16": 16.5,
            "np.float32": 32.5,
            "np.float64": 64.5,
            "np.int16": -16,
            "np.int32": -32,
            "np.int64": -64,
            "np.int8": -8,
            "np.uint16": 16,
            "np.uint32": 32,
            "np.uint64": 64,
            "np.uint8": 8,
        }
    ] == list(fresh_db.table("types").rows)


def test_cannot_provide_both_filename_and_memory():
    with pytest.raises(
        ValueError, match="Either specify a filename_or_conn or pass memory=True"
    ):
        Database("/tmp/foo.db", memory=True)


def test_creates_id_column(fresh_db):
    last_pk = fresh_db.table("cats", pk="id").insert({"name": "barry"}).last_pk
    assert [{"name": "barry", "id": last_pk}] == list(fresh_db.table("cats").rows)


def test_drop(fresh_db):
    fresh_db.table("t").insert({"foo": 1})
    assert ["t"] == fresh_db.table_names()
    assert None is fresh_db.table("t").drop()
    assert [] == fresh_db.table_names()


def test_drop_view(fresh_db):
    fresh_db.create_view("foo_view", "select 1")
    assert ["foo_view"] == fresh_db.view_names()
    assert None is fresh_db.view("foo_view").drop()
    assert [] == fresh_db.view_names()


def test_drop_ignore(fresh_db):
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.table("does_not_exist").drop()
    fresh_db.table("does_not_exist").drop(ignore=True)
    # Testing view is harder, we need to create it in order
    # to get a View object, then drop it twice
    fresh_db.create_view("foo_view", "select 1")
    view = fresh_db.view("foo_view")
    assert isinstance(view, View)
    view.drop()
    with pytest.raises(sqlite3.OperationalError):
        view.drop()
    view.drop(ignore=True)


def test_insert_all_empty_list(fresh_db):
    fresh_db.table("t").insert({"foo": 1})
    assert fresh_db.table("t").count == 1
    fresh_db.table("t").insert_all([])
    assert fresh_db.table("t").count == 1
    fresh_db.table("t").insert_all([], replace=True)
    assert fresh_db.table("t").count == 1


def test_insert_all_single_column(fresh_db):
    table = fresh_db.table("table")
    table.insert_all([{"name": "Cleo"}], pk="name")
    assert [{"name": "Cleo"}] == list(table.rows)
    assert table.pks == ["name"]


@pytest.mark.parametrize("method_name", ("insert_all", "upsert_all"))
def test_insert_all_analyze(fresh_db, method_name):
    table = fresh_db.table("table")
    table.insert_all([{"id": 1, "name": "Cleo"}], pk="id")
    assert "sqlite_stat1" not in fresh_db.table_names()
    table.create_index(["name"], analyze=True)
    assert list(fresh_db.table("sqlite_stat1").rows) == [
        {"tbl": "table", "idx": "idx_table_name", "stat": "1 1"}
    ]
    method = getattr(table, method_name)
    method([{"id": 2, "name": "Suna"}], pk="id", analyze=True)
    assert "sqlite_stat1" in fresh_db.table_names()
    assert list(fresh_db.table("sqlite_stat1").rows) == [
        {"tbl": "table", "idx": "idx_table_name", "stat": "2 1"}
    ]


def test_create_with_a_null_column(fresh_db):
    record = {"name": "Name", "description": None}
    fresh_db.table("t").insert(record)
    assert [record] == list(fresh_db.table("t").rows)


def test_create_with_nested_bytes(fresh_db):
    record = {"id": 1, "data": {"foo": b"bytes"}}
    fresh_db.table("t").insert(record)
    assert [{"id": 1, "data": '{"foo": "b\'bytes\'"}'}] == list(
        fresh_db.table("t").rows
    )


@pytest.mark.parametrize(
    "input,expected", [("hello", "'hello'"), ("hello'there'", "'hello''there'''")]
)
def test_quote(fresh_db, input, expected):
    assert fresh_db.quote(input) == expected


@pytest.mark.parametrize(
    "columns,expected_sql_middle",
    (
        (
            {"id": int},
            '"id" INTEGER',
        ),
        (
            {"col": dict},
            '"col" TEXT',
        ),
        (
            {"col": tuple},
            '"col" TEXT',
        ),
        (
            {"col": list},
            '"col" TEXT',
        ),
        (
            {"col": ANY},
            '"col" ANY',
        ),
        (
            {"col": "ANY"},
            '"col" ANY',
        ),
        (
            {"col": "any"},
            '"col" ANY',
        ),
    ),
)
def test_create_table_sql(fresh_db, columns, expected_sql_middle):
    sql = fresh_db.create_table_sql("t", columns)
    middle = sql.split("(")[1].split(")")[0].strip()
    assert middle == expected_sql_middle


def test_create(fresh_db):
    fresh_db.table("t").create(
        {
            "id": int,
            "text": str,
            "float": float,
            "integer": int,
            "bytes": bytes,
        },
        pk="id",
        column_order=("id", "float"),
        not_null=("float", "integer"),
        defaults={"integer": 0},
    )
    assert fresh_db.table("t").schema == (
        'CREATE TABLE "t" (\n'
        '   "id" INTEGER PRIMARY KEY,\n'
        '   "float" REAL NOT NULL,\n'
        '   "text" TEXT,\n'
        '   "integer" INTEGER NOT NULL DEFAULT 0,\n'
        '   "bytes" BLOB\n'
        ")"
    )


def test_create_if_not_exists(fresh_db):
    fresh_db.table("t").create({"id": int})
    # This should error
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.table("t").create({"id": int})
    # This should not
    fresh_db.table("t").create({"id": int}, if_not_exists=True)


def test_create_if_no_columns(fresh_db):
    with pytest.raises(ValueError) as error:
        fresh_db.table("t").create({})
    assert error.value.args[0] == "Tables must have at least one column"


def test_create_ignore(fresh_db):
    fresh_db.table("t").create({"id": int})
    # This should error
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.table("t").create({"id": int})
    # This should not
    fresh_db.table("t").create({"id": int}, ignore=True)


def test_create_replace(fresh_db):
    fresh_db.table("t").create({"id": int})
    # This should error
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.table("t").create({"id": int})
    # This should not
    fresh_db.table("t").create({"name": str}, replace=True)
    assert fresh_db.table("t").schema == ('CREATE TABLE "t" (\n' '   "name" TEXT\n' ")")


@pytest.mark.parametrize(
    "cols,kwargs,expected_schema,should_transform",
    (
        # Change nothing
        (
            {"id": int, "name": str},
            {"pk": "id"},
            'CREATE TABLE "demo" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT\n)',
            False,
        ),
        # Drop name column, remove primary key
        ({"id": int}, {}, 'CREATE TABLE "demo" (\n   "id" INTEGER\n)', True),
        # Add a new column
        (
            {"id": int, "name": str, "age": int},
            {"pk": "id"},
            'CREATE TABLE "demo" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" INTEGER\n)',
            True,
        ),
        # Change a column type
        (
            {"id": int, "name": bytes},
            {"pk": "id"},
            'CREATE TABLE "demo" (\n   "id" INTEGER PRIMARY KEY,\n   "name" BLOB\n)',
            True,
        ),
        # Change the primary key
        (
            {"id": int, "name": str},
            {"pk": "name"},
            'CREATE TABLE "demo" (\n   "id" INTEGER,\n   "name" TEXT PRIMARY KEY\n)',
            True,
        ),
        # Change in column order
        (
            {"id": int, "name": str},
            {"pk": "id", "column_order": ["name"]},
            'CREATE TABLE "demo" (\n   "name" TEXT,\n   "id" INTEGER PRIMARY KEY\n)',
            True,
        ),
        # Same column order is ignored
        (
            {"id": int, "name": str},
            {"pk": "id", "column_order": ["id", "name"]},
            'CREATE TABLE "demo" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT\n)',
            False,
        ),
        # Change not null
        (
            {"id": int, "name": str},
            {"pk": "id", "not_null": {"name"}},
            'CREATE TABLE "demo" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT NOT NULL\n)',
            True,
        ),
        # Change default values
        (
            {"id": int, "name": str},
            {"pk": "id", "defaults": {"id": 0, "name": "Bob"}},
            'CREATE TABLE "demo" (\n   "id" INTEGER PRIMARY KEY DEFAULT 0,\n   "name" TEXT DEFAULT \'Bob\'\n)',
            True,
        ),
    ),
)
def test_create_transform(fresh_db, cols, kwargs, expected_schema, should_transform):
    fresh_db.create_table("demo", {"id": int, "name": str}, pk="id")
    fresh_db.table("demo").insert({"id": 1, "name": "Cleo"})
    traces = []
    with fresh_db.tracer(lambda sql, parameters: traces.append((sql, parameters))):
        fresh_db.table("demo").create(cols, **kwargs, transform=True)
    at_least_one_create_table = any(sql.startswith("CREATE TABLE") for sql, _ in traces)
    assert should_transform == at_least_one_create_table
    new_schema = fresh_db.table("demo").schema
    assert new_schema == expected_schema, repr(new_schema)
    assert fresh_db.table("demo").count == 1


def test_create_transform_keyword_literal_defaults_unchanged(fresh_db):
    fresh_db.execute(
        "create table demo ("
        "id integer primary key, "
        "enabled integer default TRUE, "
        "disabled integer default FALSE, "
        "nullable text default NULL"
        ")"
    )
    traces = []
    with fresh_db.tracer(lambda sql, parameters: traces.append((sql, parameters))):
        fresh_db.table("demo").create(
            {"id": int, "enabled": int, "disabled": int, "nullable": str},
            pk="id",
            defaults={"enabled": True, "disabled": False, "nullable": None},
            transform=True,
        )
    assert not any(sql.startswith("CREATE TABLE") for sql, _ in traces)


def test_rename_table(fresh_db):
    fresh_db.table("t").insert({"foo": "bar"})
    assert ["t"] == fresh_db.table_names()
    fresh_db.rename_table("t", "renamed")
    assert ["renamed"] == fresh_db.table_names()
    assert [{"foo": "bar"}] == list(fresh_db.table("renamed").rows)
    # Should error if table does not exist:
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.rename_table("does_not_exist", "renamed")


@pytest.mark.parametrize("strict", (False, True))
def test_database_strict(strict):
    db = Database(memory=True, strict=strict)
    table = db.table("t", columns={"id": int})
    table.insert({"id": 1})
    assert table.strict == strict or not db.supports_strict


@pytest.mark.parametrize("strict", (False, True))
def test_database_strict_override(strict):
    db = Database(memory=True, strict=strict)
    table = db.table("t", columns={"id": int}, strict=not strict)
    table.insert({"id": 1})
    assert table.strict != strict or not db.supports_strict


@pytest.mark.parametrize(
    "method_name", ("insert", "upsert", "insert_all", "upsert_all")
)
@pytest.mark.parametrize("strict", (False, True))
def test_insert_upsert_strict(fresh_db, method_name, strict):
    table = fresh_db.table("t")
    method = getattr(table, method_name)
    record = {"id": 1}
    if method_name.endswith("_all"):
        record = [record]
    method(record, pk="id", strict=strict)
    assert table.strict == strict or not fresh_db.supports_strict


@pytest.mark.parametrize("strict", (False, True))
def test_create_table_strict(fresh_db, strict):
    table = fresh_db.create_table("t", {"id": int, "f": float}, strict=strict)
    assert table.strict == strict or not fresh_db.supports_strict
    expected_schema = 'CREATE TABLE "t" (\n' '   "id" INTEGER,\n' '   "f" REAL\n' ")"
    if strict and not fresh_db.supports_strict:
        return
    if strict:
        expected_schema = 'CREATE TABLE "t" (\n   "id" INTEGER,\n   "f" REAL\n) STRICT'
    assert table.schema == expected_schema


@pytest.mark.parametrize("strict", (False, True))
def test_create_strict(fresh_db, strict):
    table = fresh_db.table("t")
    table.create({"id": int}, strict=strict)
    assert table.strict == strict or not fresh_db.supports_strict


def test_create_strict_with_any(fresh_db):
    if not fresh_db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    table = fresh_db.table("items").create(
        {"id": int, "data": ANY}, pk="id", strict=True
    )
    table.insert_all(
        [
            {"id": 1, "data": 42},
            {"id": 2, "data": "000123"},
            {"id": 3, "data": 3.14},
            {"id": 4, "data": b"bytes"},
            {"id": 5, "data": None},
        ]
    )
    assert table.columns_dict == {"id": int, "data": ANY}
    assert fresh_db.execute(
        "select typeof(data), data from items order by id"
    ).fetchall() == [
        ("integer", 42),
        ("text", "000123"),
        ("real", 3.14),
        ("blob", b"bytes"),
        ("null", None),
    ]


def test_bad_table_and_view_exceptions(fresh_db):
    fresh_db.table("t").insert({"id": 1}, pk="id")
    fresh_db.create_view("v", "select * from t")
    with pytest.raises(NoTable) as ex:
        fresh_db.table("v")
    assert ex.value.args[0] == "Table v is actually a view"
    with pytest.raises(NoView) as ex2:
        fresh_db.view("t")
    assert ex2.value.args[0] == "View t does not exist - t is a table"
    with pytest.raises(NoView) as ex3:
        fresh_db.view("missing")
    assert ex3.value.args[0] == "View missing does not exist"


# Tests for issue #655: Table configuration should be stored in _defaults
# after table creation, so subsequent operations use the same settings.


def test_pk_persists_after_insert_655(fresh_db):
    """When pk is passed to insert(), subsequent inserts should use it."""
    table = fresh_db.table("users")
    table.insert({"id": 1, "name": "Alice"}, pk="id")
    # Second insert should use pk="id" from _defaults
    table.insert({"id": 2, "name": "Bob"})
    assert table.pks == ["id"]
    # Verify both rows exist (not overwritten due to missing pk)
    assert table.count == 2


def test_pk_persists_after_insert_all_655(fresh_db):
    """When pk is passed to insert_all(), subsequent inserts should use it."""
    table = fresh_db.table("users")
    table.insert_all([{"id": 1, "name": "Alice"}], pk="id")
    # Second insert_all should use pk="id" from _defaults
    table.insert_all([{"id": 2, "name": "Bob"}])
    assert table.pks == ["id"]
    assert table.count == 2


def test_pk_persists_after_create_655(fresh_db):
    """When pk is passed to create(), it should be stored in _defaults."""
    table = fresh_db.table("users")
    table.create({"id": int, "name": str}, pk="id")
    assert table._defaults["pk"] == "id"
    # Subsequent insert should use the pk
    table.insert({"id": 1, "name": "Alice"})
    table.insert({"id": 2, "name": "Bob"})
    assert table.count == 2


def test_foreign_keys_persist_after_create_655(fresh_db):
    """When foreign_keys is passed to create(), it should be stored in _defaults."""
    fresh_db.table("authors").insert({"id": 1, "name": "Alice"}, pk="id")
    table = fresh_db.table("books")
    table.create(
        {"id": int, "title": str, "author_id": int},
        pk="id",
        foreign_keys=[("author_id", "authors", "id")],
    )
    assert table._defaults["pk"] == "id"
    assert table._defaults["foreign_keys"] == [("author_id", "authors", "id")]


def test_not_null_persists_after_create_655(fresh_db):
    """When not_null is passed to create(), it should be stored in _defaults."""
    table = fresh_db.table("users")
    table.create({"id": int, "name": str}, pk="id", not_null=["name"])
    assert table._defaults["not_null"] == ["name"]


def test_defaults_persist_after_create_655(fresh_db):
    """When defaults is passed to create(), it should be stored in _defaults."""
    table = fresh_db.table("users")
    table.create({"id": int, "score": int}, pk="id", defaults={"score": 0})
    assert table._defaults["defaults"] == {"score": 0}


def test_strict_persists_after_create_655(fresh_db):
    """When strict is passed to create(), it should be stored in _defaults."""
    table = fresh_db.table("users")
    table.create({"id": int, "name": str}, pk="id", strict=True)
    assert table._defaults["strict"] is True


def test_upsert_uses_pk_from_prior_insert_655(fresh_db):
    """After insert with pk, upsert should use the same pk."""
    table = fresh_db.table("users")
    table.insert({"id": 1, "name": "Alice"}, pk="id")
    # Upsert should work without specifying pk again
    table.upsert({"id": 1, "name": "Alice Updated"})
    assert table.count == 1
    assert next(iter(table.rows))["name"] == "Alice Updated"


def test_upsert_all_uses_pk_from_prior_insert_655(fresh_db):
    """After insert with pk, upsert_all should use the same pk."""
    table = fresh_db.table("users")
    table.insert({"id": 1, "name": "Alice"}, pk="id")
    # Upsert_all should work without specifying pk again
    table.upsert_all([{"id": 1, "name": "Alice Updated"}, {"id": 2, "name": "Bob"}])
    assert table.count == 2
    rows = {row["id"]: row["name"] for row in table.rows}
    assert rows == {1: "Alice Updated", 2: "Bob"}


def test_chained_create_sets_pks(fresh_db):
    table = fresh_db.table("dogs3", pk="id").create(
        {"id": int, "name": str, "color": str}
    )
    assert table.pks == ["id"]

```

### `tests/test_default_value.py`

```py
import pytest

EXAMPLES = [
    ("TEXT DEFAULT 'foo'", "'foo'", "'foo'"),
    ("TEXT DEFAULT 'foo)'", "'foo)'", "'foo)'"),
    ("INTEGER DEFAULT '1'", "'1'", "'1'"),
    ("INTEGER DEFAULT 1", "1", "'1'"),
    ("INTEGER DEFAULT (1)", "1", "'1'"),
    # Expressions
    (
        "TEXT DEFAULT (STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))",
        "STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')",
        "(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))",
    ),
    # Special values
    ("TEXT DEFAULT CURRENT_TIME", "CURRENT_TIME", "CURRENT_TIME"),
    ("TEXT DEFAULT CURRENT_DATE", "CURRENT_DATE", "CURRENT_DATE"),
    ("TEXT DEFAULT CURRENT_TIMESTAMP", "CURRENT_TIMESTAMP", "CURRENT_TIMESTAMP"),
    ("TEXT DEFAULT current_timestamp", "current_timestamp", "current_timestamp"),
    ("TEXT DEFAULT (CURRENT_TIMESTAMP)", "CURRENT_TIMESTAMP", "CURRENT_TIMESTAMP"),
    # Strings
    ("TEXT DEFAULT 'CURRENT_TIMESTAMP'", "'CURRENT_TIMESTAMP'", "'CURRENT_TIMESTAMP'"),
    ('TEXT DEFAULT "CURRENT_TIMESTAMP"', '"CURRENT_TIMESTAMP"', '"CURRENT_TIMESTAMP"'),
    # Boolean and null keyword literals must stay unquoted
    ("INTEGER DEFAULT TRUE", "TRUE", "TRUE"),
    ("INTEGER DEFAULT FALSE", "FALSE", "FALSE"),
    ("INTEGER DEFAULT true", "true", "true"),
    ("TEXT DEFAULT NULL", "NULL", "NULL"),
]


@pytest.mark.parametrize("column_def,initial_value,expected_value", EXAMPLES)
def test_quote_default_value(fresh_db, column_def, initial_value, expected_value):
    fresh_db.execute(f"create table foo (col {column_def})")
    assert initial_value == fresh_db.table("foo").columns[0].default_value
    assert expected_value == fresh_db.quote_default_value(
        fresh_db.table("foo").columns[0].default_value
    )


def test_insert_empty_record_uses_default_values(fresh_db):
    fresh_db.execute("""
        CREATE TABLE has_defaults (
            id INTEGER PRIMARY KEY,
            name TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            is_active INTEGER NOT NULL DEFAULT 1
        )
        """)

    table = fresh_db.table("has_defaults")
    table.insert({})

    rows = list(table.rows)
    assert len(rows) == 1
    assert rows[0]["id"] == 1
    assert rows[0]["name"] is None
    assert rows[0]["timestamp"] is not None
    assert rows[0]["is_active"] == 1

```

### `tests/test_delete.py`

```py
import sqlite_utils


def test_delete_rowid_table(fresh_db):
    table = fresh_db.table("table")
    table.insert({"foo": 1})
    rowid = table.insert({"foo": 2}).last_pk
    table.delete(rowid)
    assert [{"foo": 1}] == list(table.rows)


def test_delete_pk_table(fresh_db):
    table = fresh_db.table("table")
    table.insert({"id": 1}, pk="id")
    table.insert({"id": 2}, pk="id")
    table.delete(1)
    assert [{"id": 2}] == list(table.rows)


def test_delete_where(fresh_db):
    table = fresh_db.table("table")
    for i in range(1, 11):
        table.insert({"id": i}, pk="id")
    assert table.count == 10
    table.delete_where("id > ?", [5])
    assert table.count == 5


def test_delete_where_all(fresh_db):
    table = fresh_db.table("table")
    for i in range(1, 11):
        table.insert({"id": i}, pk="id")
    assert table.count == 10
    table.delete_where()
    assert table.count == 0


def test_delete_where_commits(tmpdir):
    path = str(tmpdir / "test.db")
    db = sqlite_utils.Database(path)
    db.table("table").insert_all([{"id": i} for i in range(5)], pk="id")
    db.table("table").delete_where("id > ?", [2])
    # The connection must not be left inside an open transaction,
    # otherwise subsequent atomic() blocks never commit either
    assert not db.conn.in_transaction
    db.table("table").insert({"id": 100})
    db.close()
    db2 = sqlite_utils.Database(path)
    assert [r["id"] for r in db2.table("table").rows] == [0, 1, 2, 100]
    db2.close()


def test_delete_where_analyze(fresh_db):
    table = fresh_db.table("table")
    table.insert_all(({"id": i, "i": i} for i in range(10)), pk="id")
    table.create_index(["i"], analyze=True)
    assert "sqlite_stat1" in fresh_db.table_names()
    assert list(fresh_db.table("sqlite_stat1").rows) == [
        {"tbl": "table", "idx": "idx_table_i", "stat": "10 1"}
    ]
    table.delete_where("id > ?", [5], analyze=True)
    assert list(fresh_db.table("sqlite_stat1").rows) == [
        {"tbl": "table", "idx": "idx_table_i", "stat": "6 1"}
    ]

```

### `tests/test_docs.py`

```py
import re
from pathlib import Path

import pytest
from click.testing import CliRunner

from sqlite_utils import cli, recipes

docs_path = Path(__file__).parent.parent / "docs"
commands_re = re.compile(r"(?:\$ |    )sqlite-utils (\S+)")
recipes_re = re.compile(r"r\.(\w+)\(")


@pytest.fixture(scope="session")
def documented_commands():
    rst = ""
    for doc in ("cli.rst", "plugins.rst"):
        rst += (docs_path / doc).read_text()
    return {
        command
        for command in commands_re.findall(rst)
        if "." not in command and ":" not in command
    }


@pytest.fixture(scope="session")
def documented_recipes():
    rst = (docs_path / "cli.rst").read_text()
    return set(recipes_re.findall(rst))


@pytest.mark.parametrize("command", cli.cli.commands.keys())
def test_commands_are_documented(documented_commands, command):
    assert command in documented_commands


@pytest.mark.parametrize("command", cli.cli.commands.values())
def test_commands_have_help(command):
    assert command.help, f"{command} is missing its help"


def test_convert_help():
    result = CliRunner().invoke(cli.cli, ["convert", "--help"])
    assert result.exit_code == 0
    for expected in (
        "r.jsonsplit(value:",
        "r.parsedate(value:",
        "r.parsedatetime(value:",
    ):
        assert expected in result.output


@pytest.mark.parametrize(
    "recipe",
    [
        n
        for n in dir(recipes)
        if not n.startswith("_")
        and n not in ("json", "parser", "Callable", "Optional")
        and callable(getattr(recipes, n))
    ],
)
def test_recipes_are_documented(documented_recipes, recipe):
    assert recipe in documented_recipes

```

### `tests/test_duplicate.py`

```py
import datetime

import pytest

from sqlite_utils.db import NoTable


def test_duplicate(fresh_db):
    # Create table using native Sqlite statement:
    fresh_db.execute("""CREATE TABLE "table1" (
    "text_col" TEXT,
    "real_col" REAL,
    "int_col" INTEGER,
    "bool_col" INTEGER,
    "datetime_col" TEXT)""")
    # Insert one row of mock data:
    dt = datetime.datetime.now(datetime.timezone.utc)
    data = {
        "text_col": "Cleo",
        "real_col": 3.14,
        "int_col": -255,
        "bool_col": True,
        "datetime_col": str(dt),
    }
    table1 = fresh_db.table("table1")
    row_id = table1.insert(data).last_rowid
    # Duplicate table:
    table2 = table1.duplicate("table2")
    # Ensure data integrity:
    assert data == table2.get(row_id)
    # Ensure schema integrity:
    assert [
        {"name": "text_col", "type": "TEXT"},
        {"name": "real_col", "type": "REAL"},
        {"name": "int_col", "type": "INT"},
        {"name": "bool_col", "type": "INT"},
        {"name": "datetime_col", "type": "TEXT"},
    ] == [{"name": col.name, "type": col.type} for col in table2.columns]


def test_duplicate_fails_if_table_does_not_exist(fresh_db):
    with pytest.raises(NoTable):
        fresh_db.table("not_a_table").duplicate("duplicated")

```

### `tests/test_enable_counts.py`

```py
import pytest
from click.testing import CliRunner

from sqlite_utils import Database, cli


def test_enable_counts_specific_table(fresh_db):
    foo = fresh_db.table("foo")
    assert fresh_db.table_names() == []
    for i in range(10):
        foo.insert({"name": f"item {i}"})
    assert fresh_db.table_names() == ["foo"]
    assert foo.count == 10
    # Now enable counts
    foo.enable_counts()
    assert foo.triggers_dict == {
        "foo_counts_insert": (
            'CREATE TRIGGER "foo_counts_insert" AFTER INSERT ON "foo"\n'
            "BEGIN\n"
            '    INSERT OR REPLACE INTO "_counts"\n'
            "    VALUES (\n        'foo',\n"
            "        COALESCE(\n"
            '            (SELECT count FROM "_counts" WHERE "table" = \'foo\'),\n'
            "        0\n"
            "        ) + 1\n"
            "    );\n"
            "END"
        ),
        "foo_counts_delete": (
            'CREATE TRIGGER "foo_counts_delete" AFTER DELETE ON "foo"\n'
            "BEGIN\n"
            '    INSERT OR REPLACE INTO "_counts"\n'
            "    VALUES (\n"
            "        'foo',\n"
            "        COALESCE(\n"
            '            (SELECT count FROM "_counts" WHERE "table" = \'foo\'),\n'
            "        0\n"
            "        ) - 1\n"
            "    );\n"
            "END"
        ),
    }
    assert fresh_db.table_names() == ["foo", "_counts"]
    assert list(fresh_db.table("_counts").rows) == [{"count": 10, "table": "foo"}]
    # Add some items to test the triggers
    for i in range(5):
        foo.insert({"name": f"item {10 + i}"})
    assert foo.count == 15
    assert list(fresh_db.table("_counts").rows) == [{"count": 15, "table": "foo"}]
    # Delete some items
    foo.delete_where("rowid < 7")
    assert foo.count == 9
    assert list(fresh_db.table("_counts").rows) == [{"count": 9, "table": "foo"}]
    foo.delete_where()
    assert foo.count == 0
    assert list(fresh_db.table("_counts").rows) == [{"count": 0, "table": "foo"}]


def test_enable_counts_all_tables(fresh_db):
    foo = fresh_db.table("foo")
    bar = fresh_db.table("bar")
    foo.insert({"name": "Cleo"})
    bar.insert({"name": "Cleo"})
    foo.enable_fts(["name"])
    fresh_db.enable_counts()
    assert set(fresh_db.table_names()) == {
        "foo",
        "bar",
        "foo_fts",
        "foo_fts_data",
        "foo_fts_idx",
        "foo_fts_docsize",
        "foo_fts_config",
        "_counts",
    }
    assert list(fresh_db.table("_counts").rows) == [
        {"count": 1, "table": "foo"},
        {"count": 1, "table": "bar"},
        {"count": 3, "table": "foo_fts_data"},
        {"count": 1, "table": "foo_fts_idx"},
        {"count": 1, "table": "foo_fts_docsize"},
        {"count": 1, "table": "foo_fts_config"},
    ]


@pytest.fixture
def counts_db_path(tmpdir):
    path = str(tmpdir / "test.db")
    db = Database(path)
    db.table("foo").insert({"name": "bar"})
    db.table("bar").insert({"name": "bar"})
    db.table("bar").insert({"name": "bar"})
    db.table("baz").insert({"name": "bar"})
    return path


@pytest.mark.parametrize(
    "extra_args,expected_triggers",
    [
        (
            [],
            [
                "foo_counts_insert",
                "foo_counts_delete",
                "bar_counts_insert",
                "bar_counts_delete",
                "baz_counts_insert",
                "baz_counts_delete",
            ],
        ),
        (
            ["bar"],
            [
                "bar_counts_insert",
                "bar_counts_delete",
            ],
        ),
    ],
)
def test_cli_enable_counts(counts_db_path, extra_args, expected_triggers):
    db = Database(counts_db_path)
    assert list(db.triggers_dict.keys()) == []
    result = CliRunner().invoke(cli.cli, ["enable-counts", counts_db_path] + extra_args)
    assert result.exit_code == 0
    assert list(db.triggers_dict.keys()) == expected_triggers


def test_uses_counts_after_enable_counts(counts_db_path):
    db = Database(counts_db_path)
    logged = []
    with db.tracer(lambda sql, parameters: logged.append((sql, parameters))):
        assert db.table("foo").count == 1
        assert logged == [
            ("select name from sqlite_master where type = 'view'", None),
            ('select count(*) from "foo"', []),
        ]
        logged.clear()
        assert not db.use_counts_table
        db.enable_counts()
        assert db.use_counts_table
        assert db.table("foo").count == 1
    assert logged == [
        (
            'CREATE TABLE IF NOT EXISTS "_counts"(\n   "table" TEXT PRIMARY KEY,\n   count INTEGER DEFAULT 0\n);',
            None,
        ),
        ("select name from sqlite_master where type = 'table'", None),
        ("select name from sqlite_master where type = 'view'", None),
        ("select name from sqlite_master where type = 'view'", None),
        ("select name from sqlite_master where type = 'view'", None),
        ("select name from sqlite_master where type = 'view'", None),
        ("select sql from sqlite_master where name = ?", ("foo",)),
        ("SELECT quote(:value)", {"value": "foo"}),
        ("select sql from sqlite_master where name = ?", ("bar",)),
        ("SELECT quote(:value)", {"value": "bar"}),
        ("select sql from sqlite_master where name = ?", ("baz",)),
        ("SELECT quote(:value)", {"value": "baz"}),
        ("select sql from sqlite_master where name = ?", ("_counts",)),
        ("select name from sqlite_master where type = 'view'", None),
        ('select "table", count from _counts where "table" in (?)', ["foo"]),
    ]


def test_reset_counts(counts_db_path):
    db = Database(counts_db_path)
    db.table("foo").enable_counts()
    db.table("bar").enable_counts()
    assert db.cached_counts() == {"foo": 1, "bar": 2}
    # Corrupt the value
    db.table("_counts").update("foo", {"count": 3})
    assert db.cached_counts() == {"foo": 3, "bar": 2}
    assert db.table("foo").count == 3
    # Reset them
    db.reset_counts()
    assert db.cached_counts() == {"foo": 1, "bar": 2}
    assert db.table("foo").count == 1


def test_reset_counts_cli(counts_db_path):
    db = Database(counts_db_path)
    db.table("foo").enable_counts()
    db.table("bar").enable_counts()
    assert db.cached_counts() == {"foo": 1, "bar": 2}
    db.table("_counts").update("foo", {"count": 3})
    result = CliRunner().invoke(cli.cli, ["reset-counts", counts_db_path])
    assert result.exit_code == 0
    assert db.cached_counts() == {"foo": 1, "bar": 2}

```

### `tests/test_extract.py`

```py
import itertools

import pytest

from sqlite_utils import ANY
from sqlite_utils.db import InvalidColumns


@pytest.mark.parametrize("table", [None, "Species"])
@pytest.mark.parametrize("fk_column", [None, "species"])
def test_extract_single_column(fresh_db, table, fk_column):
    expected_table = table or "species"
    expected_fk = fk_column or f"{expected_table}_id"
    iter_species = itertools.cycle(["Palm", "Spruce", "Mangrove", "Oak"])
    fresh_db.table("tree").insert_all(
        (
            {
                "id": i,
                "name": f"Tree {i}",
                "species": next(iter_species),
                "end": 1,
            }
            for i in range(1, 1001)
        ),
        pk="id",
    )
    fresh_db.table("tree").extract("species", table=table, fk_column=fk_column)
    assert fresh_db.table("tree").schema == (
        'CREATE TABLE "tree" (\n'
        '   "id" INTEGER PRIMARY KEY,\n'
        '   "name" TEXT,\n'
        f'   "{expected_fk}" INTEGER REFERENCES "{expected_table}"("id"),\n'
        + '   "end" INTEGER\n'
        + ")"
    )
    assert fresh_db.table(expected_table).schema == (
        f'CREATE TABLE "{expected_table}" (\n' + '   "id" INTEGER PRIMARY KEY,\n'
        '   "species" TEXT\n'
        ")"
    )
    assert list(fresh_db.table(expected_table).rows) == [
        {"id": 1, "species": "Palm"},
        {"id": 2, "species": "Spruce"},
        {"id": 3, "species": "Mangrove"},
        {"id": 4, "species": "Oak"},
    ]
    assert list(itertools.islice(fresh_db.table("tree").rows, 0, 4)) == [
        {"id": 1, "name": "Tree 1", expected_fk: 1, "end": 1},
        {"id": 2, "name": "Tree 2", expected_fk: 2, "end": 1},
        {"id": 3, "name": "Tree 3", expected_fk: 3, "end": 1},
        {"id": 4, "name": "Tree 4", expected_fk: 4, "end": 1},
    ]


def test_extract_multiple_columns_with_rename(fresh_db):
    iter_common = itertools.cycle(["Palm", "Spruce", "Mangrove", "Oak"])
    iter_latin = itertools.cycle(["Arecaceae", "Picea", "Rhizophora", "Quercus"])
    fresh_db.table("tree").insert_all(
        (
            {
                "id": i,
                "name": f"Tree {i}",
                "common_name": next(iter_common),
                "latin_name": next(iter_latin),
            }
            for i in range(1, 1001)
        ),
        pk="id",
    )

    fresh_db.table("tree").extract(
        ["common_name", "latin_name"], rename={"common_name": "name"}
    )
    assert fresh_db.table("tree").schema == (
        'CREATE TABLE "tree" (\n'
        '   "id" INTEGER PRIMARY KEY,\n'
        '   "name" TEXT,\n'
        '   "common_name_latin_name_id" INTEGER REFERENCES "common_name_latin_name"("id")\n'
        ")"
    )
    assert fresh_db.table("common_name_latin_name").schema == (
        'CREATE TABLE "common_name_latin_name" (\n'
        '   "id" INTEGER PRIMARY KEY,\n'
        '   "name" TEXT,\n'
        '   "latin_name" TEXT\n'
        ")"
    )
    assert list(fresh_db.table("common_name_latin_name").rows) == [
        {"name": "Palm", "id": 1, "latin_name": "Arecaceae"},
        {"name": "Spruce", "id": 2, "latin_name": "Picea"},
        {"name": "Mangrove", "id": 3, "latin_name": "Rhizophora"},
        {"name": "Oak", "id": 4, "latin_name": "Quercus"},
    ]
    assert list(itertools.islice(fresh_db.table("tree").rows, 0, 4)) == [
        {"id": 1, "name": "Tree 1", "common_name_latin_name_id": 1},
        {"id": 2, "name": "Tree 2", "common_name_latin_name_id": 2},
        {"id": 3, "name": "Tree 3", "common_name_latin_name_id": 3},
        {"id": 4, "name": "Tree 4", "common_name_latin_name_id": 4},
    ]


def test_extract_invalid_columns(fresh_db):
    fresh_db.table("tree").insert(
        {
            "id": 1,
            "name": "Tree 1",
            "common_name": "Palm",
            "latin_name": "Arecaceae",
        },
        pk="id",
    )
    with pytest.raises(InvalidColumns):
        fresh_db.table("tree").extract(["bad_column"])


def test_extract_rowid_table(fresh_db):
    fresh_db.table("tree").insert(
        {
            "name": "Tree 1",
            "common_name": "Palm",
            "latin_name": "Arecaceae",
        }
    )
    fresh_db.table("tree").extract(["common_name", "latin_name"])
    assert fresh_db.table("tree").schema == (
        'CREATE TABLE "tree" (\n'
        '   "name" TEXT,\n'
        '   "common_name_latin_name_id" INTEGER REFERENCES "common_name_latin_name"("id")\n'
        ")"
    )
    assert fresh_db.execute("""
        select
            tree.name,
            common_name_latin_name.common_name,
            common_name_latin_name.latin_name
        from tree
            join common_name_latin_name
            on tree.common_name_latin_name_id = common_name_latin_name.id
    """).fetchall() == [("Tree 1", "Palm", "Arecaceae")]


def test_reuse_lookup_table(fresh_db):
    fresh_db.table("species").insert({"id": 1, "name": "Wolf"}, pk="id")
    fresh_db.table("sightings").insert({"id": 10, "species": "Wolf"}, pk="id")
    fresh_db.table("individuals").insert(
        {"id": 10, "name": "Terriana", "species": "Fox"}, pk="id"
    )
    fresh_db.table("sightings").extract("species", rename={"species": "name"})
    fresh_db.table("individuals").extract("species", rename={"species": "name"})
    assert fresh_db.table("sightings").schema == (
        'CREATE TABLE "sightings" (\n'
        '   "id" INTEGER PRIMARY KEY,\n'
        '   "species_id" INTEGER REFERENCES "species"("id")\n'
        ")"
    )
    assert fresh_db.table("individuals").schema == (
        'CREATE TABLE "individuals" (\n'
        '   "id" INTEGER PRIMARY KEY,\n'
        '   "name" TEXT,\n'
        '   "species_id" INTEGER REFERENCES "species"("id")\n'
        ")"
    )
    assert list(fresh_db.table("species").rows) == [
        {"id": 1, "name": "Wolf"},
        {"id": 2, "name": "Fox"},
    ]


def test_extract_error_on_incompatible_existing_lookup_table(fresh_db):
    fresh_db.table("species").insert({"id": 1})
    fresh_db.table("tree").insert({"name": "Tree 1", "common_name": "Palm"})
    with pytest.raises(InvalidColumns):
        fresh_db.table("tree").extract("common_name", table="species")

    # Try again with incompatible existing column type
    fresh_db.table("species2").insert({"id": 1, "common_name": 3.5})
    with pytest.raises(InvalidColumns):
        fresh_db.table("tree").extract("common_name", table="species2")


def test_extract_works_with_null_values(fresh_db):
    fresh_db.table("listens").insert_all(
        [
            {"id": 1, "track_title": "foo", "album_title": "bar"},
            {"id": 2, "track_title": "baz", "album_title": None},
        ],
        pk="id",
    )
    fresh_db.table("listens").extract(
        columns=["album_title"], table="albums", fk_column="album_id"
    )
    assert list(fresh_db.table("listens").rows) == [
        {"id": 1, "track_title": "foo", "album_id": 1},
        {"id": 2, "track_title": "baz", "album_id": None},
    ]
    assert list(fresh_db.table("albums").rows) == [
        {"id": 1, "album_title": "bar"},
    ]


def test_extract_null_values_single_column(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/186
    fresh_db.table("species").insert({"id": 1, "species": "Wolf"}, pk="id")
    fresh_db.table("individuals").insert_all(
        [
            {"id": 10, "name": "Terriana", "species": "Fox"},
            {"id": 11, "name": "Spenidorm", "species": None},
            {"id": 12, "name": "Grantheim", "species": "Wolf"},
            {"id": 13, "name": "Turnutopia", "species": None},
            {"id": 14, "name": "Wargal", "species": "Wolf"},
        ],
        pk="id",
    )
    fresh_db.table("individuals").extract("species")
    # No null row should have been added to species
    assert list(fresh_db.table("species").rows) == [
        {"id": 1, "species": "Wolf"},
        {"id": 2, "species": "Fox"},
    ]
    assert list(fresh_db.table("individuals").rows) == [
        {"id": 10, "name": "Terriana", "species_id": 2},
        {"id": 11, "name": "Spenidorm", "species_id": None},
        {"id": 12, "name": "Grantheim", "species_id": 1},
        {"id": 13, "name": "Turnutopia", "species_id": None},
        {"id": 14, "name": "Wargal", "species_id": 1},
    ]


def test_extract_null_values_multiple_columns(fresh_db):
    # A row should be extracted if at least one column is not null -
    # only rows where ALL extracted columns are null are left alone
    fresh_db.table("circulation").insert_all(
        [
            {"id": 1, "title": "title one", "creator": "creator one", "year": 2018},
            {"id": 2, "title": "title two", "creator": None, "year": 2019},
            {"id": 3, "title": None, "creator": None, "year": 2020},
            {"id": 4, "title": None, "creator": None, "year": 2021},
        ],
        pk="id",
    )
    fresh_db.table("circulation").extract(
        ["title", "creator"], table="books", fk_column="book_id"
    )
    assert list(fresh_db.table("books").rows) == [
        {"id": 1, "title": "title one", "creator": "creator one"},
        {"id": 2, "title": "title two", "creator": None},
    ]
    assert list(fresh_db.table("circulation").rows) == [
        {"id": 1, "book_id": 1, "year": 2018},
        {"id": 2, "book_id": 2, "year": 2019},
        {"id": 3, "book_id": None, "year": 2020},
        {"id": 4, "book_id": None, "year": 2021},
    ]


def test_extract_null_values_existing_lookup_table_with_null_row(fresh_db):
    # Even if the lookup table already contains an all-null row, rows where
    # every extracted column is null should keep a null foreign key
    fresh_db.table("species").insert({"id": 1, "species": None}, pk="id")
    fresh_db.table("individuals").insert_all(
        [
            {"id": 10, "name": "Terriana", "species": "Fox"},
            {"id": 11, "name": "Spenidorm", "species": None},
        ],
        pk="id",
    )
    fresh_db.table("individuals").extract("species")
    assert list(fresh_db.table("species").rows) == [
        {"id": 1, "species": None},
        {"id": 2, "species": "Fox"},
    ]
    assert list(fresh_db.table("individuals").rows) == [
        {"id": 10, "name": "Terriana", "species_id": 2},
        {"id": 11, "name": "Spenidorm", "species_id": None},
    ]


def test_extract_repeated_into_shared_lookup_with_nulls(fresh_db):
    # Unique indexes treat NULLs as distinct, so INSERT OR IGNORE alone
    # cannot dedupe NULL-containing rows against the existing lookup
    # table - extracting a second table into the same lookup previously
    # inserted duplicate rows that nothing pointed to
    fresh_db.table("t1").insert_all(
        [
            {"id": 1, "species": None, "common": "X"},
            {"id": 2, "species": "Oak", "common": "Oak"},
        ],
        pk="id",
    )
    fresh_db.table("t2").insert_all(
        [{"id": 1, "species": None, "common": "X"}], pk="id"
    )
    fresh_db.table("t1").extract(["species", "common"], table="lk")
    fresh_db.table("t2").extract(["species", "common"], table="lk")
    assert fresh_db.table("lk").count == 2
    # Both tables point at the same lookup row
    t1_fk = fresh_db.execute("select lk_id from t1 where id = 1").fetchone()[0]
    t2_fk = fresh_db.execute("select lk_id from t2 where id = 1").fetchone()[0]
    assert t1_fk == t2_fk


def test_extract_repeated_into_shared_lookup_no_nulls(fresh_db):
    # Non-NULL rows were already deduped by the unique index - keep it so
    fresh_db.table("t1").insert_all([{"id": 1, "species": "Oak"}], pk="id")
    fresh_db.table("t2").insert_all([{"id": 1, "species": "Oak"}], pk="id")
    fresh_db.table("t1").extract(["species"], table="lk")
    fresh_db.table("t2").extract(["species"], table="lk")
    assert fresh_db.table("lk").count == 1


def test_extract_preserves_strict_any(fresh_db):
    if not fresh_db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    fresh_db.execute("create table items (id integer primary key, data any) strict")
    fresh_db.execute("insert into items values (1, ?)", ("000123",))

    fresh_db["items"].extract("data", table="data_values")

    lookup = fresh_db["data_values"]
    assert lookup.strict is True
    assert lookup.columns_dict == {"id": int, "data": ANY}
    assert fresh_db.execute(
        "select typeof(data), data from data_values"
    ).fetchone() == ("text", "000123")


def test_extract_strict_any_rejects_non_strict_lookup(fresh_db):
    if not fresh_db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    fresh_db.execute("create table items (data any) strict")
    fresh_db.execute("insert into items values (?)", ("000123",))
    fresh_db.execute("create table data_values (id integer primary key, data any)")

    with pytest.raises(
        InvalidColumns,
        match="is not STRICT, so it cannot preserve ANY column values",
    ):
        fresh_db["items"].extract("data", table="data_values")

    assert fresh_db.execute("select typeof(data), data from items").fetchone() == (
        "text",
        "000123",
    )

```

### `tests/test_extracts.py`

```py
import pytest

from sqlite_utils.db import Index


@pytest.mark.parametrize(
    "kwargs,expected_table",
    [
        ({"extracts": {"species_id": "Species"}}, "Species"),
        ({"extracts": ["species_id"]}, "species_id"),
        ({"extracts": ("species_id",)}, "species_id"),
    ],
)
@pytest.mark.parametrize("use_table_factory", [True, False])
def test_extracts(fresh_db, kwargs, expected_table, use_table_factory):
    table_kwargs = {}
    insert_kwargs = {}
    if use_table_factory:
        table_kwargs = kwargs
    else:
        insert_kwargs = kwargs
    trees = fresh_db.table("Trees", **table_kwargs)
    trees.insert_all(
        [
            {"id": 1, "species_id": "Oak"},
            {"id": 2, "species_id": "Oak"},
            {"id": 3, "species_id": "Palm"},
        ],
        **insert_kwargs,
    )
    # Should now have two tables: Trees and Species
    assert {expected_table, "Trees"} == set(fresh_db.table_names())
    assert (
        f'CREATE TABLE "{expected_table}" (\n   "id" INTEGER PRIMARY KEY,\n   "value" TEXT\n)'
        == fresh_db.table(expected_table).schema
    )
    assert (
        f'CREATE TABLE "Trees" (\n   "id" INTEGER,\n   "species_id" INTEGER REFERENCES "{expected_table}"("id")\n)'
        == fresh_db.table("Trees").schema
    )
    # Should have a foreign key reference
    assert len(fresh_db.table("Trees").foreign_keys) == 1
    fk = fresh_db.table("Trees").foreign_keys[0]
    assert fk.table == "Trees"
    assert fk.column == "species_id"

    # Should have unique index on Species
    assert [
        Index(
            seq=0,
            name=f"idx_{expected_table}_value",
            unique=1,
            origin="c",
            partial=0,
            columns=["value"],
        )
    ] == fresh_db.table(expected_table).indexes
    # Finally, check the rows
    assert [{"id": 1, "value": "Oak"}, {"id": 2, "value": "Palm"}] == list(
        fresh_db.table(expected_table).rows
    )
    assert [
        {"id": 1, "species_id": 1},
        {"id": 2, "species_id": 1},
        {"id": 3, "species_id": 2},
    ] == list(fresh_db.table("Trees").rows)


def test_extracts_null_values(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/186
    # Null values should stay null, not be extracted into the lookup table
    fresh_db.table("Trees").insert_all(
        [
            {"id": 1, "species_id": "Oak"},
            {"id": 2, "species_id": None},
            {"id": 3, "species_id": "Palm"},
            {"id": 4, "species_id": None},
        ],
        extracts={"species_id": "Species"},
    )
    assert list(fresh_db.table("Species").rows) == [
        {"id": 1, "value": "Oak"},
        {"id": 2, "value": "Palm"},
    ]
    assert list(fresh_db.table("Trees").rows) == [
        {"id": 1, "species_id": 1},
        {"id": 2, "species_id": None},
        {"id": 3, "species_id": 2},
        {"id": 4, "species_id": None},
    ]


def test_extracts_null_values_list_mode(fresh_db):
    # Same as test_extracts_null_values but for list-based records
    fresh_db.table("Trees").insert_all(
        [
            ["id", "species_id"],
            [1, "Oak"],
            [2, None],
            [3, "Palm"],
            [4, None],
        ],
        extracts={"species_id": "Species"},
    )
    assert list(fresh_db.table("Species").rows) == [
        {"id": 1, "value": "Oak"},
        {"id": 2, "value": "Palm"},
    ]
    assert list(fresh_db.table("Trees").rows) == [
        {"id": 1, "species_id": 1},
        {"id": 2, "species_id": None},
        {"id": 3, "species_id": 2},
        {"id": 4, "species_id": None},
    ]

```

### `tests/test_foreign_keys.py`

```py
"""Tests for compound (multi-column) foreign keys - issue #594."""

import pytest

from sqlite_utils import Database
from sqlite_utils.db import AlterError, ForeignKey
from sqlite_utils.utils import sqlite3

COMPOUND_SCHEMA = """
CREATE TABLE departments (
    campus_name TEXT NOT NULL,
    dept_code TEXT NOT NULL,
    dept_name TEXT,
    PRIMARY KEY (campus_name, dept_code)
);
CREATE TABLE courses (
    course_code TEXT PRIMARY KEY,
    course_name TEXT,
    campus_name TEXT NOT NULL,
    dept_code TEXT NOT NULL,
    FOREIGN KEY (campus_name, dept_code)
    REFERENCES departments(campus_name, dept_code)
);
"""


@pytest.fixture
def compound_db():
    db = Database(memory=True)
    db.executescript(COMPOUND_SCHEMA)
    return db


def test_compound_foreign_key(compound_db):
    fks = compound_db.table("courses").foreign_keys
    assert len(fks) == 1
    fk = fks[0]
    assert fk.is_compound is True
    assert fk.table == "courses"
    assert fk.other_table == "departments"
    assert fk.columns == ("campus_name", "dept_code")
    assert fk.other_columns == ("campus_name", "dept_code")
    # Scalar column/other_column can't sensibly hold a compound key
    assert fk.column is None
    assert fk.other_column is None


def test_single_foreign_key_gets_columns_fields(fresh_db):
    fresh_db.table("authors").insert({"id": 1, "name": "Sally"}, pk="id")
    fresh_db.table("books").insert({"title": "Hedgehogs", "author_id": 1})
    fresh_db.table("books").add_foreign_key("author_id", "authors", "id")
    fk = fresh_db.table("books").foreign_keys[0]
    assert fk.is_compound is False
    assert fk.column == "author_id"
    assert fk.other_column == "id"
    assert fk.columns == ("author_id",)
    assert fk.other_columns == ("id",)


def test_foreign_key_no_longer_unpacks_as_tuple(fresh_db):
    # Clean break in 4.0: ForeignKey is a dataclass, not a namedtuple, so the
    # old tuple unpacking and indexing patterns now fail hard.
    fresh_db.table("authors").insert({"id": 1, "name": "Sally"}, pk="id")
    fresh_db.table("books").insert({"title": "Hedgehogs", "author_id": 1})
    fresh_db.table("books").add_foreign_key("author_id", "authors", "id")
    fk = fresh_db.table("books").foreign_keys[0]
    with pytest.raises(TypeError):
        _table, _column, _other_table, _other_column = fk
    with pytest.raises(TypeError):
        fk[0]


def test_foreign_keys_are_sortable(fresh_db):
    fresh_db.table("authors").insert({"id": 1, "name": "Sally"}, pk="id")
    fresh_db.table("categories").insert({"id": 1, "name": "Wildlife"}, pk="id")
    fresh_db.table("books").insert(
        {"title": "Hedgehogs", "author_id": 1, "category_id": 1}
    )
    fresh_db.add_foreign_keys(
        [
            ("books", "author_id", "authors", "id"),
            ("books", "category_id", "categories", "id"),
        ]
    )
    fks = sorted(fresh_db.table("books").foreign_keys)
    assert fks[0].column == "author_id"
    assert fks[1].column == "category_id"


def test_mixed_compound_and_single_foreign_keys_are_sortable():
    # compound FKs have column=None, which must not break sorting
    # against single-column FKs (None < str raises TypeError)
    db = Database(memory=True)
    db.executescript("""
    CREATE TABLE departments (
        campus_name TEXT NOT NULL,
        dept_code TEXT NOT NULL,
        PRIMARY KEY (campus_name, dept_code)
    );
    CREATE TABLE accreditations (id INTEGER PRIMARY KEY);
    CREATE TABLE courses (
        course_code TEXT PRIMARY KEY,
        campus_name TEXT NOT NULL,
        dept_code TEXT NOT NULL,
        accreditation_id INTEGER REFERENCES accreditations(id),
        FOREIGN KEY (campus_name, dept_code)
        REFERENCES departments(campus_name, dept_code)
    );
    """)
    fks = db.table("courses").foreign_keys
    assert len(fks) == 2
    assert {fk.is_compound for fk in fks} == {True, False}
    fks_sorted = sorted(fks)
    assert fks_sorted[0].other_table == "accreditations"
    assert fks_sorted[1].other_table == "departments"


@pytest.fixture
def departments_db():
    db = Database(memory=True)
    db.create_table(
        "departments",
        {"campus_name": str, "dept_code": str, "dept_name": str},
        pk=("campus_name", "dept_code"),
    )
    return db


EXPECTED_COURSES_SCHEMA = (
    'CREATE TABLE "courses" (\n'
    '   "course_code" TEXT PRIMARY KEY,\n'
    '   "campus_name" TEXT,\n'
    '   "dept_code" TEXT,\n'
    '   FOREIGN KEY ("campus_name", "dept_code") '
    'REFERENCES "departments"("campus_name", "dept_code")\n'
    ")"
)


@pytest.mark.parametrize(
    "foreign_keys",
    (
        [
            ForeignKey(
                table="courses",
                column=None,
                other_table="departments",
                other_column=None,
                columns=("campus_name", "dept_code"),
                other_columns=("campus_name", "dept_code"),
                is_compound=True,
            )
        ],
        [(("campus_name", "dept_code"), "departments", ("campus_name", "dept_code"))],
        # Two-item form guesses the other table's primary key:
        [(("campus_name", "dept_code"), "departments")],
        # Lists work too, though tuples are the documented form:
        [(["campus_name", "dept_code"], "departments", ["campus_name", "dept_code"])],
    ),
)
def test_create_table_with_compound_foreign_key(departments_db, foreign_keys):
    departments_db.create_table(
        "courses",
        {"course_code": str, "campus_name": str, "dept_code": str},
        pk="course_code",
        foreign_keys=foreign_keys,
    )
    assert departments_db.table("courses").schema == EXPECTED_COURSES_SCHEMA
    fks = departments_db.table("courses").foreign_keys
    assert len(fks) == 1
    fk = fks[0]
    assert fk.is_compound is True
    assert fk.columns == ("campus_name", "dept_code")
    assert fk.other_table == "departments"
    assert fk.other_columns == ("campus_name", "dept_code")


def test_create_table_compound_foreign_key_enforced(departments_db):
    departments_db.execute("PRAGMA foreign_keys = ON")
    departments_db.create_table(
        "courses",
        {"course_code": str, "campus_name": str, "dept_code": str},
        pk="course_code",
        foreign_keys=[(("campus_name", "dept_code"), "departments")],
    )
    departments_db.table("departments").insert(
        {"campus_name": "Berkeley", "dept_code": "CS", "dept_name": "Computer Science"}
    )
    departments_db.table("courses").insert(
        {"course_code": "CS101", "campus_name": "Berkeley", "dept_code": "CS"}
    )
    with pytest.raises(sqlite3.IntegrityError):
        departments_db.execute(
            "insert into courses (course_code, campus_name, dept_code) "
            "values ('X1', 'Nowhere', 'NOPE')"
        )


def test_create_table_compound_foreign_key_missing_other_column(departments_db):
    with pytest.raises(AlterError):
        departments_db.create_table(
            "courses",
            {"course_code": str, "campus_name": str, "dept_code": str},
            pk="course_code",
            foreign_keys=[
                (("campus_name", "dept_code"), "departments", ("campus_name", "nope"))
            ],
        )


def test_transform_preserves_compound_foreign_key(compound_db):
    compound_db.table("courses").transform(rename={"course_name": "title"})
    fks = compound_db.table("courses").foreign_keys
    assert len(fks) == 1
    fk = fks[0]
    assert fk.is_compound is True
    assert fk.columns == ("campus_name", "dept_code")
    assert fk.other_table == "departments"
    assert fk.other_columns == ("campus_name", "dept_code")


def test_transform_rename_member_column_updates_compound_foreign_key(compound_db):
    compound_db.table("courses").transform(rename={"campus_name": "campus"})
    fks = compound_db.table("courses").foreign_keys
    assert len(fks) == 1
    fk = fks[0]
    assert fk.is_compound is True
    assert fk.columns == ("campus", "dept_code")
    # Referenced columns in the other table are unchanged
    assert fk.other_columns == ("campus_name", "dept_code")


def test_transform_drop_member_column_drops_compound_foreign_key(compound_db):
    # Matches single-column behavior: dropping the column silently
    # drops the foreign key that used it
    compound_db.table("courses").transform(drop={"dept_code"})
    assert compound_db.table("courses").foreign_keys == []
    assert "FOREIGN KEY" not in compound_db.table("courses").schema


@pytest.mark.parametrize(
    "drop_foreign_keys",
    (
        # A bare column name matches any foreign key it participates in:
        ["campus_name"],
        # A tuple must match the full compound key:
        [("campus_name", "dept_code")],
    ),
)
def test_transform_drop_compound_foreign_key(compound_db, drop_foreign_keys):
    compound_db.table("courses").transform(drop_foreign_keys=drop_foreign_keys)
    assert compound_db.table("courses").foreign_keys == []
    # The columns themselves survive
    assert {"campus_name", "dept_code"} <= set(
        compound_db.table("courses").columns_dict.keys()
    )


@pytest.fixture
def courses_db(departments_db):
    departments_db.create_table(
        "courses",
        {"course_code": str, "campus_name": str, "dept_code": str},
        pk="course_code",
    )
    return departments_db


def test_add_compound_foreign_key(courses_db):
    t = courses_db.table("courses").add_foreign_key(
        ("campus_name", "dept_code"), "departments", ("campus_name", "dept_code")
    )
    # Returns self
    assert t.name == "courses"
    fks = courses_db.table("courses").foreign_keys
    assert len(fks) == 1
    fk = fks[0]
    assert fk.is_compound is True
    assert fk.columns == ("campus_name", "dept_code")
    assert fk.other_table == "departments"
    assert fk.other_columns == ("campus_name", "dept_code")


def test_add_compound_foreign_key_guesses_other_columns(courses_db):
    # Lists work here too, though tuples are the documented form
    courses_db.table("courses").add_foreign_key(
        ["campus_name", "dept_code"], "departments"
    )
    fk = courses_db.table("courses").foreign_keys[0]
    assert fk.other_columns == ("campus_name", "dept_code")


def test_add_compound_foreign_key_error_if_already_exists(courses_db):
    courses_db.table("courses").add_foreign_key(
        ("campus_name", "dept_code"), "departments"
    )
    with pytest.raises(AlterError) as ex:
        courses_db.table("courses").add_foreign_key(
            ("campus_name", "dept_code"), "departments"
        )
    assert "already exists" in ex.value.args[0]
    # ignore=True should not raise
    courses_db.table("courses").add_foreign_key(
        ("campus_name", "dept_code"), "departments", ignore=True
    )


def test_add_compound_foreign_key_error_if_column_missing(courses_db):
    with pytest.raises(AlterError):
        courses_db.table("courses").add_foreign_key(
            ("campus_name", "nope"), "departments"
        )


def test_db_add_foreign_keys_compound(courses_db):
    courses_db.add_foreign_keys(
        [
            (
                "courses",
                ("campus_name", "dept_code"),
                "departments",
                ("campus_name", "dept_code"),
            )
        ]
    )
    fk = courses_db.table("courses").foreign_keys[0]
    assert fk.is_compound is True
    assert fk.columns == ("campus_name", "dept_code")


def test_index_foreign_keys_compound_creates_composite_index(compound_db):
    compound_db.index_foreign_keys()
    index_columns = [i.columns for i in compound_db.table("courses").indexes]
    assert ["campus_name", "dept_code"] in index_columns
    # No separate single-column indexes for the members
    assert ["campus_name"] not in index_columns
    assert ["dept_code"] not in index_columns


def test_foreign_key_captures_on_delete_and_on_update():
    db = Database(memory=True)
    db.executescript("""
    CREATE TABLE authors (id INTEGER PRIMARY KEY);
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        author_id INTEGER REFERENCES authors(id)
            ON DELETE CASCADE ON UPDATE RESTRICT
    );
    """)
    fk = db.table("books").foreign_keys[0]
    assert fk.on_delete == "CASCADE"
    assert fk.on_update == "RESTRICT"


def test_foreign_key_on_delete_defaults_to_no_action(fresh_db):
    fresh_db.table("authors").insert({"id": 1}, pk="id")
    fresh_db.table("books").insert({"id": 1, "author_id": 1}, pk="id")
    fresh_db.table("books").add_foreign_key("author_id", "authors", "id")
    fk = fresh_db.table("books").foreign_keys[0]
    assert fk.on_delete == "NO ACTION"
    assert fk.on_update == "NO ACTION"


def test_create_table_foreign_key_with_on_delete(fresh_db):
    fresh_db.table("authors").insert({"id": 1}, pk="id")
    fresh_db.create_table(
        "books",
        {"id": int, "author_id": int},
        pk="id",
        foreign_keys=[
            ForeignKey(
                table="books",
                column="author_id",
                other_table="authors",
                other_column="id",
                on_delete="CASCADE",
            )
        ],
    )
    assert "ON DELETE CASCADE" in fresh_db.table("books").schema
    assert fresh_db.table("books").foreign_keys[0].on_delete == "CASCADE"


def test_transform_preserves_on_delete_cascade():
    db = Database(memory=True)
    db.executescript("""
    CREATE TABLE authors (id INTEGER PRIMARY KEY);
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE
    );
    """)
    db.table("books").transform(rename={"title": "book_title"})
    fk = db.table("books").foreign_keys[0]
    assert fk.on_delete == "CASCADE"
    assert fk.on_update == "NO ACTION"
    assert "ON DELETE CASCADE" in db.table("books").schema


def test_transform_preserves_compound_foreign_key_on_delete():
    db = Database(memory=True)
    db.executescript("""
    CREATE TABLE departments (
        campus_name TEXT NOT NULL,
        dept_code TEXT NOT NULL,
        PRIMARY KEY (campus_name, dept_code)
    );
    CREATE TABLE courses (
        course_code TEXT PRIMARY KEY,
        campus_name TEXT NOT NULL,
        dept_code TEXT NOT NULL,
        FOREIGN KEY (campus_name, dept_code)
        REFERENCES departments(campus_name, dept_code) ON DELETE CASCADE
    );
    """)
    db.table("courses").transform(rename={"course_code": "code"})
    fk = db.table("courses").foreign_keys[0]
    assert fk.is_compound is True
    assert fk.on_delete == "CASCADE"
    assert "ON DELETE CASCADE" in db.table("courses").schema


def test_implicit_primary_key_reference_is_resolved():
    # REFERENCES authors (no column) has "to" of None in the pragma -
    # it should be resolved to the primary key of the other table
    db = Database(memory=True)
    db.executescript("""
    CREATE TABLE authors (author_id INTEGER PRIMARY KEY);
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        author_id INTEGER REFERENCES authors
    );
    """)
    fk = db.table("books").foreign_keys[0]
    assert fk.is_compound is False
    assert fk.other_column == "author_id"
    assert fk.other_columns == ("author_id",)


def test_implicit_compound_primary_key_reference_is_resolved():
    db = Database(memory=True)
    db.executescript("""
    CREATE TABLE departments (
        campus_name TEXT NOT NULL,
        dept_code TEXT NOT NULL,
        PRIMARY KEY (campus_name, dept_code)
    );
    CREATE TABLE courses (
        course_code TEXT PRIMARY KEY,
        campus_name TEXT NOT NULL,
        dept_code TEXT NOT NULL,
        FOREIGN KEY (campus_name, dept_code) REFERENCES departments
    );
    """)
    fk = db.table("courses").foreign_keys[0]
    assert fk.is_compound is True
    assert fk.other_columns == ("campus_name", "dept_code")


def test_foreign_key_normalizes_list_columns_to_tuples():
    # Compound columns passed as lists are normalized to tuples, so they
    # compare equal to introspected ForeignKeys
    fk = ForeignKey(
        table="courses",
        column=None,
        other_table="departments",
        other_column=None,
        columns=["campus_name", "dept_code"],
        other_columns=["campus_name", "dept_code"],
        is_compound=True,
    )
    assert fk.columns == ("campus_name", "dept_code")
    assert fk.other_columns == ("campus_name", "dept_code")


def test_add_foreign_keys_preserves_actions(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/594 review finding:
    # ForeignKey objects passed to db.add_foreign_keys() were flattened
    # to plain tuples, losing on_delete/on_update
    fresh_db.table("authors").insert({"id": 1}, pk="id")
    fresh_db.table("books").insert({"id": 1, "author_id": 1}, pk="id")
    fresh_db.add_foreign_keys(
        [ForeignKey("books", "author_id", "authors", "id", on_delete="CASCADE")]
    )
    fk = fresh_db.table("books").foreign_keys[0]
    assert fk.on_delete == "CASCADE"
    assert "ON DELETE CASCADE" in fresh_db.table("books").schema


def test_add_foreign_keys_preserves_actions_compound(courses_db):
    courses_db.add_foreign_keys(
        [
            ForeignKey(
                table="courses",
                column=None,
                other_table="departments",
                other_column=None,
                columns=("campus_name", "dept_code"),
                other_columns=("campus_name", "dept_code"),
                is_compound=True,
                on_delete="CASCADE",
            )
        ]
    )
    fk = courses_db.table("courses").foreign_keys[0]
    assert fk.is_compound is True
    assert fk.on_delete == "CASCADE"
    assert "ON DELETE CASCADE" in courses_db.table("courses").schema


def test_add_foreign_key_on_delete_on_update(fresh_db):
    fresh_db.table("authors").insert({"id": 1}, pk="id")
    fresh_db.table("books").insert({"id": 1, "author_id": 1}, pk="id")
    fresh_db.table("books").add_foreign_key(
        "author_id", "authors", "id", on_delete="CASCADE", on_update="RESTRICT"
    )
    fk = fresh_db.table("books").foreign_keys[0]
    assert fk.on_delete == "CASCADE"
    assert fk.on_update == "RESTRICT"
    assert "ON UPDATE RESTRICT ON DELETE CASCADE" in fresh_db.table("books").schema
    # The cascade should actually fire
    fresh_db.execute("PRAGMA foreign_keys = ON")
    fresh_db.execute("delete from authors where id = 1")
    assert fresh_db.table("books").count == 0


def test_add_compound_foreign_key_on_delete(courses_db):
    courses_db.table("courses").add_foreign_key(
        ("campus_name", "dept_code"), "departments", on_delete="SET NULL"
    )
    fk = courses_db.table("courses").foreign_keys[0]
    assert fk.is_compound is True
    assert fk.on_delete == "SET NULL"
    assert "ON DELETE SET NULL" in courses_db.table("courses").schema


def test_implicit_compound_foreign_key_resolves_pk_declaration_order(fresh_db):
    # The other table's PRIMARY KEY declares its columns in a different
    # order to the table's column order. SQLite resolves the implicit
    # "REFERENCES other" using PRIMARY KEY declaration order, so the
    # introspected other_columns must too
    fresh_db.execute("create table other (b text, a text, primary key (a, b))")
    fresh_db.execute(
        "create table child (x text, y text, foreign key (x, y) references other)"
    )
    fk = fresh_db.table("child").foreign_keys[0]
    assert fk.other_columns == ("a", "b")


def test_transform_implicit_compound_foreign_key_stays_valid(fresh_db):
    # transform() rewrites the implicit FK with explicit columns - they
    # must be in PRIMARY KEY declaration order or valid data fails the
    # foreign key check with an IntegrityError
    fresh_db.execute("create table other (b text, a text, primary key (a, b))")
    fresh_db.execute(
        "create table child (x text, y text, foreign key (x, y) references other)"
    )
    fresh_db.execute("PRAGMA foreign_keys = ON")
    fresh_db.table("other").insert({"a": "A", "b": "B"})
    fresh_db.table("child").insert({"x": "A", "y": "B"})
    fresh_db.table("child").transform(types={"x": str})
    assert fresh_db.table("child").foreign_keys[0].other_columns == ("a", "b")
    # The constraint still points the right way around
    fresh_db.table("child").insert({"x": "A", "y": "B"})
    with pytest.raises(sqlite3.IntegrityError):
        fresh_db.table("child").insert({"x": "B", "y": "A"})


def test_create_compound_foreign_key_guesses_pk_declaration_order(fresh_db):
    fresh_db.execute("create table other (b text, a text, primary key (a, b))")
    fresh_db.table("other").insert({"a": "A", "b": "B"})
    fresh_db.table("child").create(
        {"id": int, "x": str, "y": str},
        pk="id",
        foreign_keys=[(("x", "y"), "other")],
    )
    assert fresh_db.table("child").foreign_keys[0].other_columns == ("a", "b")
    fresh_db.execute("PRAGMA foreign_keys = ON")
    fresh_db.table("child").insert({"id": 1, "x": "A", "y": "B"})
    with pytest.raises(sqlite3.IntegrityError):
        fresh_db.table("child").insert({"id": 2, "x": "B", "y": "A"})


def test_add_compound_foreign_key_guesses_pk_declaration_order(fresh_db):
    fresh_db.execute("create table other (b text, a text, primary key (a, b))")
    fresh_db.table("child").insert({"id": 1, "x": "A", "y": "B"}, pk="id")
    fresh_db.table("child").add_foreign_key(("x", "y"), "other")
    assert fresh_db.table("child").foreign_keys[0].other_columns == ("a", "b")


def test_foreign_keys_are_hashable(fresh_db):
    # set() over foreign_keys worked with the 3.x namedtuple and must
    # keep working with the dataclass
    fresh_db.table("p").insert({"id": 1}, pk="id")
    fresh_db.table("c").insert(
        {"id": 1, "pid": 1}, pk="id", foreign_keys=[("pid", "p", "id")]
    )
    fks = set(fresh_db.table("c").foreign_keys)
    assert len(fks) == 1
    assert ForeignKey("c", "pid", "p", "id") in fks
    # Usable as dict keys too
    assert {fk: True for fk in fks}


def test_foreign_key_is_immutable():
    import dataclasses

    fk = ForeignKey("c", "pid", "p", "id")
    with pytest.raises(dataclasses.FrozenInstanceError):
        setattr(fk, "table", "other")


def test_foreign_key_equality_and_hash_include_actions():
    # Two foreign keys differing only in ON DELETE behavior are different
    # constraints - they compare unequal and hash separately
    plain = ForeignKey("c", "pid", "p", "id")
    cascade = ForeignKey("c", "pid", "p", "id", on_delete="CASCADE")
    assert plain != cascade
    assert len({plain, cascade}) == 2
    assert plain == ForeignKey("c", "pid", "p", "id")


def test_create_table_mixed_foreign_keys_list(fresh_db):
    # 3.x accepted a mix of ForeignKey objects, tuples and bare column
    # strings in foreign_keys= (ForeignKey was a namedtuple, so it passed
    # the tuple check) - keep accepting the mix
    fresh_db.table("authors").insert({"id": 1}, pk="id")
    fresh_db.table("publishers").insert({"id": 1}, pk="id")
    fresh_db.table("books").create(
        {"id": int, "author_id": int, "publisher_id": int},
        pk="id",
        foreign_keys=[
            ForeignKey("books", "author_id", "authors", "id"),
            ("publisher_id", "publishers", "id"),
        ],
    )
    fks = {fk.column: fk.other_table for fk in fresh_db.table("books").foreign_keys}
    assert fks == {"author_id": "authors", "publisher_id": "publishers"}


def test_create_table_mixed_foreign_keys_with_string(fresh_db):
    fresh_db.table("authors").insert({"id": 1}, pk="id")
    fresh_db.table("publishers").insert({"id": 1}, pk="id")
    fresh_db.table("books").create(
        {"id": int, "author_id": int, "publisher_id": int},
        pk="id",
        foreign_keys=[
            "author_id",  # bare column, table and column guessed
            ("publisher_id", "publishers", "id"),
        ],
    )
    fks = {fk.column: fk.other_table for fk in fresh_db.table("books").foreign_keys}
    assert fks == {"author_id": "authors", "publisher_id": "publishers"}


def test_add_foreign_keys_existing_with_different_actions_errors(fresh_db):
    # Requesting an existing foreign key with different ON DELETE/ON UPDATE
    # actions was silently skipped, dropping the requested change
    fresh_db.table("authors").insert({"id": 1}, pk="id")
    fresh_db.table("books").insert(
        {"id": 1, "author_id": 1},
        pk="id",
        foreign_keys=[("author_id", "authors", "id")],
    )
    with pytest.raises(AlterError) as ex:
        fresh_db.add_foreign_keys(
            [ForeignKey("books", "author_id", "authors", "id", on_delete="CASCADE")]
        )
    assert "ON DELETE" in str(ex.value)
    assert fresh_db.table("books").foreign_keys[0].on_delete == "NO ACTION"


def test_add_foreign_keys_identical_existing_is_noop(fresh_db):
    # An exact match, including actions, is silently skipped so repeated
    # calls stay idempotent
    fresh_db.table("authors").insert({"id": 1}, pk="id")
    fresh_db.table("books").insert({"id": 1, "author_id": 1}, pk="id")
    fresh_db.table("books").add_foreign_key(
        "author_id", "authors", "id", on_delete="CASCADE"
    )
    fresh_db.add_foreign_keys(
        [ForeignKey("books", "author_id", "authors", "id", on_delete="CASCADE")]
    )
    fks = fresh_db.table("books").foreign_keys
    assert len(fks) == 1
    assert fks[0].on_delete == "CASCADE"


def test_add_foreign_keys_compound_column_count_mismatch_errors(fresh_db):
    # Previously the extra other-column was silently discarded, creating
    # a single-column foreign key to just ("id")
    fresh_db.table("departments").insert(
        {"campus": "north", "code": "cs"}, pk=("campus", "code")
    )
    fresh_db.table("courses").insert({"id": 1, "campus": "north"}, pk="id")
    with pytest.raises(ValueError) as ex:
        fresh_db.add_foreign_keys(
            [("courses", ("campus",), "departments", ("campus", "code"))]
        )
    assert "same number of columns" in str(ex.value)
    assert fresh_db.table("courses").foreign_keys == []

```

### `tests/test_fts.py`

```py
from unittest.mock import ANY

import pytest

from sqlite_utils import Database
from sqlite_utils.utils import sqlite3

search_records = [
    {
        "text": "tanuki are running tricksters",
        "country": "Japan",
        "not_searchable": "foo",
    },
    {
        "text": "racoons are biting trash pandas",
        "country": "USA",
        "not_searchable": "bar",
    },
]


def test_enable_fts(fresh_db):
    table = fresh_db.table("searchable")
    table.insert_all(search_records)
    assert ["searchable"] == fresh_db.table_names()
    table.enable_fts(["text", "country"], fts_version="FTS4")
    assert [
        "searchable",
        "searchable_fts",
        "searchable_fts_segments",
        "searchable_fts_segdir",
        "searchable_fts_docsize",
        "searchable_fts_stat",
    ] == fresh_db.table_names()
    assert [
        {
            "rowid": 1,
            "text": "tanuki are running tricksters",
            "country": "Japan",
            "not_searchable": "foo",
        }
    ] == list(table.search("tanuki"))
    assert [
        {
            "rowid": 2,
            "text": "racoons are biting trash pandas",
            "country": "USA",
            "not_searchable": "bar",
        }
    ] == list(table.search("usa"))
    assert [] == list(table.search("bar"))


def test_enable_fts_escape_table_names(fresh_db):
    # Table names with restricted chars are handled correctly.
    # colons and dots are restricted characters for table names.
    table = fresh_db.table("http://example.com")
    table.insert_all(search_records)
    assert ["http://example.com"] == fresh_db.table_names()
    table.enable_fts(["text", "country"], fts_version="FTS4")
    assert [
        "http://example.com",
        "http://example.com_fts",
        "http://example.com_fts_segments",
        "http://example.com_fts_segdir",
        "http://example.com_fts_docsize",
        "http://example.com_fts_stat",
    ] == fresh_db.table_names()
    assert [
        {
            "rowid": 1,
            "text": "tanuki are running tricksters",
            "country": "Japan",
            "not_searchable": "foo",
        }
    ] == list(table.search("tanuki"))
    assert [
        {
            "rowid": 2,
            "text": "racoons are biting trash pandas",
            "country": "USA",
            "not_searchable": "bar",
        }
    ] == list(table.search("usa"))
    assert [] == list(table.search("bar"))


def test_search_duplicate_columns_are_deduped(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/624
    table = fresh_db.table("t")
    table.insert_all(search_records)
    table.enable_fts(["text", "country"], fts_version="FTS4")
    rows = list(table.search("tanuki", columns=["text", "text"]))
    assert rows == [
        {
            "text": "tanuki are running tricksters",
            "text_2": "tanuki are running tricksters",
        }
    ]


def test_search_limit_offset(fresh_db):
    table = fresh_db.table("t")
    table.insert_all(search_records)
    table.enable_fts(["text", "country"], fts_version="FTS4")
    assert len(list(table.search("are"))) == 2
    assert len(list(table.search("are", limit=1))) == 1
    assert next(iter(table.search("are", limit=1, order_by="rowid")))["rowid"] == 1
    assert (
        next(iter(table.search("are", limit=1, offset=1, order_by="rowid")))["rowid"]
        == 2
    )


def test_search_offset_without_limit(fresh_db):
    table = fresh_db.table("t")
    table.insert_all(search_records)
    table.enable_fts(["text", "country"], fts_version="FTS4")
    assert [row["rowid"] for row in table.search("are", order_by="rowid")] == [1, 2]
    assert [
        row["rowid"] for row in table.search("are", offset=1, order_by="rowid")
    ] == [2]
    assert table.search_sql(offset=1).strip().endswith("limit -1 offset 1")


@pytest.mark.parametrize("fts_version", ("FTS4", "FTS5"))
def test_search_where(fresh_db, fts_version):
    table = fresh_db.table("t")
    table.insert_all(search_records)
    table.enable_fts(["text", "country"], fts_version=fts_version)
    results = list(
        table.search("are", where="country = :country", where_args={"country": "Japan"})
    )
    assert results == [
        {
            "rowid": 1,
            "text": "tanuki are running tricksters",
            "country": "Japan",
            "not_searchable": "foo",
        }
    ]


def test_search_where_args_disallows_query(fresh_db):
    table = fresh_db.table("t")
    with pytest.raises(ValueError) as ex:
        list(
            table.search(
                "x", where="author = :query", where_args={"query": "not allowed"}
            )
        )
    assert (
        ex.value.args[0]
        == "'query' is a reserved key and cannot be passed to where_args for .search()"
    )


def test_search_include_rank(fresh_db):
    table = fresh_db.table("t")
    table.insert_all(search_records)
    table.enable_fts(["text", "country"], fts_version="FTS5")
    results = list(table.search("are", include_rank=True))
    assert results == [
        {
            "rowid": 1,
            "text": "tanuki are running tricksters",
            "country": "Japan",
            "not_searchable": "foo",
            "rank": ANY,
        },
        {
            "rowid": 2,
            "text": "racoons are biting trash pandas",
            "country": "USA",
            "not_searchable": "bar",
            "rank": ANY,
        },
    ]
    assert isinstance(results[0]["rank"], float)
    assert isinstance(results[1]["rank"], float)
    assert results[0]["rank"] < results[1]["rank"]


def test_enable_fts_table_names_containing_spaces(fresh_db):
    table = fresh_db.table("test")
    table.insert({"column with spaces": "in its name"})
    table.enable_fts(["column with spaces"])
    assert [
        "test",
        "test_fts",
        "test_fts_data",
        "test_fts_idx",
        "test_fts_docsize",
        "test_fts_config",
    ] == fresh_db.table_names()


def test_populate_fts(fresh_db):
    table = fresh_db.table("populatable")
    table.insert(search_records[0])
    table.enable_fts(["text", "country"], fts_version="FTS4")
    assert [] == list(table.search("trash pandas"))
    table.insert(search_records[1])
    assert [] == list(table.search("trash pandas"))
    # Now run populate_fts to make this record available
    table.populate_fts(["text", "country"])
    rows = list(table.search("usa"))
    assert [
        {
            "rowid": 2,
            "text": "racoons are biting trash pandas",
            "country": "USA",
            "not_searchable": "bar",
        }
    ] == rows


def test_populate_fts_escape_table_names(fresh_db):
    # Restricted characters such as colon and dots should be escaped.
    table = fresh_db.table("http://example.com")
    table.insert(search_records[0])
    table.enable_fts(["text", "country"], fts_version="FTS4")
    assert [] == list(table.search("trash pandas"))
    table.insert(search_records[1])
    assert [] == list(table.search("trash pandas"))
    # Now run populate_fts to make this record available
    table.populate_fts(["text", "country"])
    assert [
        {
            "rowid": 2,
            "text": "racoons are biting trash pandas",
            "country": "USA",
            "not_searchable": "bar",
        }
    ] == list(table.search("usa"))


@pytest.mark.parametrize("fts_version", ("4", "5"))
def test_fts_tokenize(fresh_db, fts_version):
    table_name = f"searchable_{fts_version}"
    table = fresh_db.table(table_name)
    table.insert_all(search_records)
    # Test without porter stemming
    table.enable_fts(
        ["text", "country"],
        fts_version=f"FTS{fts_version}",
    )
    assert [] == list(table.search("bite"))
    # Test WITH stemming
    table.disable_fts()
    table.enable_fts(
        ["text", "country"],
        fts_version=f"FTS{fts_version}",
        tokenize="porter",
    )
    rows = list(table.search("bite", order_by="rowid"))
    assert len(rows) == 1
    assert {
        "rowid": 2,
        "text": "racoons are biting trash pandas",
        "country": "USA",
        "not_searchable": "bar",
    }.items() <= rows[0].items()


def test_fts_tokenize_escaped(fresh_db):
    # A malicious tokenize value must not be able to break out of the
    # string literal in the CREATE VIRTUAL TABLE statement.
    table = fresh_db.table("searchable")
    table.insert_all(search_records)
    malicious = "porter'); CREATE TABLE injected(x); --"
    with pytest.raises(Exception):
        table.enable_fts(["text"], tokenize=malicious)
    # The injected statement must not have executed
    assert "injected" not in fresh_db.table_names()


def test_optimize_fts(fresh_db):
    for fts_version in ("4", "5"):
        table_name = f"searchable_{fts_version}"
        table = fresh_db.table(table_name)
        table.insert_all(search_records)
        table.enable_fts(["text", "country"], fts_version=f"FTS{fts_version}")
    # You can call optimize successfully against the tables OR their _fts equivalents:
    for table_name in (
        "searchable_4",
        "searchable_5",
        "searchable_4_fts",
        "searchable_5_fts",
    ):
        fresh_db.table(table_name).optimize()


def test_enable_fts_with_triggers(fresh_db):
    table = fresh_db.table("searchable")
    table.insert(search_records[0])
    table.enable_fts(["text", "country"], fts_version="FTS4", create_triggers=True)
    rows1 = list(table.search("tanuki"))
    assert len(rows1) == 1
    assert rows1 == [
        {
            "rowid": 1,
            "text": "tanuki are running tricksters",
            "country": "Japan",
            "not_searchable": "foo",
        }
    ]
    table.insert(search_records[1])
    # Triggers will auto-populate FTS virtual table, not need to call populate_fts()
    rows2 = list(table.search("usa"))
    assert rows2 == [
        {
            "rowid": 2,
            "text": "racoons are biting trash pandas",
            "country": "USA",
            "not_searchable": "bar",
        }
    ]
    assert [] == list(table.search("bar"))


@pytest.mark.parametrize("create_triggers", [True, False])
def test_disable_fts(fresh_db, create_triggers):
    table = fresh_db.table("searchable")
    table.insert(search_records[0])
    table.enable_fts(["text", "country"], create_triggers=create_triggers)
    assert {
        "searchable",
        "searchable_fts",
        "searchable_fts_data",
        "searchable_fts_idx",
        "searchable_fts_docsize",
        "searchable_fts_config",
    } == set(fresh_db.table_names())
    if create_triggers:
        expected_triggers = {"searchable_ai", "searchable_ad", "searchable_au"}
    else:
        expected_triggers = set()
    assert expected_triggers == {
        r[0]
        for r in fresh_db.execute(
            "select name from sqlite_master where type = 'trigger'"
        ).fetchall()
    }
    # Now run .disable_fts() and confirm it worked
    table.disable_fts()
    assert (
        0
        == fresh_db.execute(
            "select count(*) from sqlite_master where type = 'trigger'"
        ).fetchone()[0]
    )
    assert ["searchable"] == fresh_db.table_names()


def test_rebuild_fts(fresh_db):
    table = fresh_db.table("searchable")
    table.insert(search_records[0])
    table.enable_fts(["text", "country"])
    # Run a search
    rows = list(table.search("are"))
    assert len(rows) == 1
    assert {
        "rowid": 1,
        "text": "tanuki are running tricksters",
        "country": "Japan",
        "not_searchable": "foo",
    }.items() <= rows[0].items()
    # Insert another record
    table.insert(search_records[1])
    # This should NOT show up in searches
    assert len(list(table.search("are"))) == 1
    # Running rebuild_fts() should fix it
    table.rebuild_fts()
    rows2 = list(table.search("are"))
    assert len(rows2) == 2


@pytest.mark.parametrize("method", ["optimize", "rebuild_fts"])
def test_optimize_and_rebuild_fts_commit(tmpdir, method):
    path = str(tmpdir / "test.db")
    db = Database(path)
    table = db.table("searchable")
    table.insert(search_records[0])
    table.enable_fts(["text", "country"])
    getattr(table, method)()
    # The connection must not be left inside an open transaction,
    # otherwise this and all subsequent writes are lost on close
    assert not db.conn.in_transaction
    table.insert(search_records[1])
    db.close()
    db2 = Database(path)
    assert db2.table("searchable").count == 2
    db2.close()


@pytest.mark.parametrize("invalid_table", ["does_not_exist", "not_searchable"])
def test_rebuild_fts_invalid(fresh_db, invalid_table):
    fresh_db.table("not_searchable").insert({"foo": "bar"})
    # Raise OperationalError on invalid table
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.table(invalid_table).rebuild_fts()


@pytest.mark.parametrize("fts_version", ["FTS4", "FTS5"])
def test_rebuild_removes_junk_docsize_rows(tmpdir, fts_version):
    # Recreating https://github.com/simonw/sqlite-utils/issues/149
    path = tmpdir / "test.db"
    db = Database(str(path), recursive_triggers=False)
    licenses = [{"key": "apache2", "name": "Apache 2"}, {"key": "bsd", "name": "BSD"}]
    db.table("licenses").insert_all(licenses, pk="key", replace=True)
    db.table("licenses").enable_fts(
        ["name"], create_triggers=True, fts_version=fts_version
    )
    assert db.table("licenses_fts_docsize").count == 2
    # Bug: insert with replace increases the number of rows in _docsize:
    db.table("licenses").insert_all(licenses, pk="key", replace=True)
    assert db.table("licenses_fts_docsize").count == 4
    # rebuild should fix this:
    db.table("licenses_fts").rebuild_fts()
    assert db.table("licenses_fts_docsize").count == 2


@pytest.mark.parametrize(
    "kwargs",
    [
        {"columns": ["title"]},
        {"fts_version": "FTS4"},
        {"create_triggers": True},
        {"tokenize": "porter"},
    ],
)
def test_enable_fts_replace(kwargs):
    db = Database(memory=True)
    db.table("books").insert(
        {
            "id": 1,
            "title": "Habits of Australian Marsupials",
            "author": "Marlee Hawkins",
        },
        pk="id",
    )
    db.table("books").enable_fts(["title", "author"])
    assert not db.table("books").triggers
    assert db.table("books_fts").columns_dict.keys() == {"title", "author"}
    assert "FTS5" in db.table("books_fts").schema
    assert "porter" not in db.table("books_fts").schema
    # Now modify the FTS configuration
    should_have_changed_columns = "columns" in kwargs
    if "columns" not in kwargs:
        kwargs["columns"] = ["title", "author"]
    db.table("books").enable_fts(**kwargs, replace=True)
    # Check that the new configuration is correct
    if should_have_changed_columns:
        assert db.table("books_fts").columns_dict.keys() == {"title"}
    if "create_triggers" in kwargs:
        assert db.table("books").triggers
    if "fts_version" in kwargs:
        assert "FTS4" in db.table("books_fts").schema
    if "tokenize" in kwargs:
        assert "porter" in db.table("books_fts").schema


def test_enable_fts_replace_does_nothing_if_args_the_same():
    queries = []
    db = Database(memory=True, tracer=lambda sql, params: queries.append((sql, params)))
    db.table("books").insert(
        {
            "id": 1,
            "title": "Habits of Australian Marsupials",
            "author": "Marlee Hawkins",
        },
        pk="id",
    )
    db.table("books").enable_fts(["title", "author"], create_triggers=True)
    queries.clear()
    # Running that again shouldn't run much SQL:
    db.table("books").enable_fts(
        ["title", "author"], create_triggers=True, replace=True
    )
    # The only SQL that executed should be select statements
    assert all(q[0].startswith("select ") for q in queries)


def test_enable_fts_replace_handles_legacy_bracket_quoted_content_table():
    db = Database(memory=True)
    db.table("books").insert(
        {
            "id": 1,
            "title": "Habits of Australian Marsupials",
            "author": "Marlee Hawkins",
        },
        pk="id",
    )
    db.executescript("""
        CREATE VIRTUAL TABLE [books_fts] USING FTS5 (
            [title],
            content=[books]
        );
    """)

    db.table("books").enable_fts(["title", "author"], replace=True)

    assert db.table("books_fts").columns_dict.keys() == {"title", "author"}
    assert 'content="books"' in db.table("books_fts").schema


def test_view_has_no_enable_fts():
    db = Database(memory=True)
    db.create_view("hello", "select 1 + 1")
    # Views deliberately do not have an enable_fts() method
    with pytest.raises(AttributeError):
        db.view("hello").enable_fts()  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    "kwargs,fts,expected",
    [
        (
            {},
            "FTS5",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                "        *\n"
                '    from "books"\n'
                ")\n"
                "select\n"
                '    "original".*\n'
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                '    "books_fts".rank'
            ),
        ),
        (
            {"columns": ["title"], "order_by": "rowid", "limit": 10},
            "FTS5",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                '        "title"\n'
                '    from "books"\n'
                ")\n"
                "select\n"
                '    "original"."title"\n'
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                "    rowid\n"
                "limit 10"
            ),
        ),
        (
            {"where": "author = :author"},
            "FTS5",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                "        *\n"
                '    from "books"\n'
                "    where author = :author\n"
                ")\n"
                "select\n"
                '    "original".*\n'
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                '    "books_fts".rank'
            ),
        ),
        (
            {"columns": ["title"]},
            "FTS4",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                '        "title"\n'
                '    from "books"\n'
                ")\n"
                "select\n"
                '    "original"."title"\n'
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                "    rank_bm25(matchinfo(\"books_fts\", 'pcnalx'))"
            ),
        ),
        (
            {"offset": 1, "limit": 1},
            "FTS4",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                "        *\n"
                '    from "books"\n'
                ")\n"
                "select\n"
                '    "original".*\n'
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                "    rank_bm25(matchinfo(\"books_fts\", 'pcnalx'))\n"
                "limit 1 offset 1"
            ),
        ),
        (
            {"limit": 2},
            "FTS4",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                "        *\n"
                '    from "books"\n'
                ")\n"
                "select\n"
                '    "original".*\n'
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                "    rank_bm25(matchinfo(\"books_fts\", 'pcnalx'))\n"
                "limit 2"
            ),
        ),
        (
            {"where": "author = :author"},
            "FTS4",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                "        *\n"
                '    from "books"\n'
                "    where author = :author\n"
                ")\n"
                "select\n"
                '    "original".*\n'
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                "    rank_bm25(matchinfo(\"books_fts\", 'pcnalx'))"
            ),
        ),
        (
            {"include_rank": True},
            "FTS5",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                "        *\n"
                '    from "books"\n'
                ")\n"
                "select\n"
                '    "original".*,\n'
                '    "books_fts".rank rank\n'
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                '    "books_fts".rank'
            ),
        ),
        (
            {"include_rank": True},
            "FTS4",
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                "        *\n"
                '    from "books"\n'
                ")\n"
                "select\n"
                '    "original".*,\n'
                "    rank_bm25(matchinfo(\"books_fts\", 'pcnalx')) rank\n"
                "from\n"
                '    "original"\n'
                '    join "books_fts" on "original".rowid = "books_fts".rowid\n'
                "where\n"
                '    "books_fts" match :query\n'
                "order by\n"
                "    rank_bm25(matchinfo(\"books_fts\", 'pcnalx'))"
            ),
        ),
    ],
)
def test_search_sql(kwargs, fts, expected):
    db = Database(memory=True)
    db.table("books").insert(
        {
            "title": "Habits of Australian Marsupials",
            "author": "Marlee Hawkins",
        }
    )
    db.table("books").enable_fts(["title", "author"], fts_version=fts)
    sql = db.table("books").search_sql(**kwargs)
    assert sql == expected


@pytest.mark.parametrize(
    "input,expected",
    (
        ("dog", '"dog"'),
        ("cat,", '"cat,"'),
        ("cat's", '"cat\'s"'),
        ("dog.", '"dog."'),
        ("cat dog", '"cat" "dog"'),
        # If a phrase is already double quoted, leave it so
        ('"cat dog"', '"cat dog"'),
        ('"cat dog" fish', '"cat dog" "fish"'),
        # Sensibly handle unbalanced double quotes
        ('cat"', '"cat"'),
        ('"cat dog" "fish', '"cat dog" "fish"'),
    ),
)
def test_quote_fts_query(fresh_db, input, expected):
    table = fresh_db.table("searchable")
    table.insert_all(search_records)
    table.enable_fts(["text", "country"])
    quoted = fresh_db.quote_fts(input)
    assert quoted == expected
    # Executing query does not crash.
    list(table.search(quoted))


def test_search_quote(fresh_db):
    table = fresh_db.table("searchable")
    table.insert_all(search_records)
    table.enable_fts(["text", "country"])
    query = "cat's"
    with pytest.raises(sqlite3.OperationalError):
        list(table.search(query))
    # No exception with quote=True
    list(table.search(query, quote=True))


def test_enable_fts_cli_on_view_errors(tmpdir):
    db_path = str(tmpdir / "test.db")
    db = Database(db_path)
    db.table("t").insert({"text": "hello"})
    db.create_view("v", "select * from t")
    db.close()
    from click.testing import CliRunner

    from sqlite_utils import cli as cli_module

    result = CliRunner().invoke(cli_module.cli, ["enable-fts", db_path, "v", "text"])
    assert result.exit_code == 1
    assert result.output.strip() == "Error: Table v is actually a view"

```

### `tests/test_get.py`

```py
import pytest

from sqlite_utils.db import NotFoundError


def test_get_rowid(fresh_db):
    dogs = fresh_db.table("dogs")
    cleo = {"name": "Cleo", "age": 4}
    row_id = dogs.insert(cleo).last_rowid
    assert cleo == dogs.get(row_id)


def test_get_primary_key(fresh_db):
    dogs = fresh_db.table("dogs")
    cleo = {"name": "Cleo", "age": 4, "id": 5}
    last_pk = dogs.insert(cleo, pk="id").last_pk
    assert 5 == last_pk
    assert cleo == dogs.get(5)


@pytest.mark.parametrize(
    "argument,expected_msg",
    [(100, None), (None, None), ((1, 2), "Need 1 primary key value"), ("2", None)],
)
def test_get_not_found(argument, expected_msg, fresh_db):
    fresh_db.table("dogs").insert(
        {"id": 1, "name": "Cleo", "age": 4, "is_good": True}, pk="id"
    )
    with pytest.raises(NotFoundError) as excinfo:
        fresh_db.table("dogs").get(argument)
    if expected_msg is not None:
        assert expected_msg == excinfo.value.args[0]

```

### `tests/test_gis.py`

```py
import json

import pytest
from click.testing import CliRunner

from sqlite_utils.cli import cli
from sqlite_utils.db import Database
from sqlite_utils.utils import find_spatialite, sqlite3

pytestmark = [
    pytest.mark.skipif(
        not find_spatialite(), reason="Could not find SpatiaLite extension"
    ),
    pytest.mark.skipif(
        not hasattr(sqlite3.Connection, "enable_load_extension"),
        reason="sqlite3.Connection missing enable_load_extension",
    ),
]


# python API tests
def test_find_spatialite():
    spatialite = find_spatialite()
    assert spatialite is None or isinstance(spatialite, str)


def test_init_spatialite():
    db = Database(memory=True)
    spatialite = find_spatialite()
    db.init_spatialite(spatialite)
    assert "spatial_ref_sys" in db.table_names()


def test_add_geometry_column():
    db = Database(memory=True)
    spatialite = find_spatialite()
    db.init_spatialite(spatialite)

    # create a table first
    table = db.create_table("locations", {"id": str, "properties": str})
    table.add_geometry_column(
        column_name="geometry",
        geometry_type="Point",
        srid=4326,
        coord_dimension="XY",
    )

    assert db.table("geometry_columns").get(["locations", "geometry"]) == {
        "f_table_name": "locations",
        "f_geometry_column": "geometry",
        "geometry_type": 1,  # point
        "coord_dimension": 2,
        "srid": 4326,
        "spatial_index_enabled": 0,
    }


def test_create_spatial_index():
    db = Database(memory=True)
    spatialite = find_spatialite()
    assert db.init_spatialite(spatialite)

    # create a table, add a geometry column with default values
    table = db.create_table("locations", {"id": str, "properties": str})
    assert table.add_geometry_column("geometry", "Point")

    # index it
    assert table.create_spatial_index("geometry")

    assert "idx_locations_geometry" in db.table_names()


def test_double_create_spatial_index():
    db = Database(memory=True)
    spatialite = find_spatialite()
    db.init_spatialite(spatialite)

    # create a table, add a geometry column with default values
    table = db.create_table("locations", {"id": str, "properties": str})
    table.add_geometry_column("geometry", "Point")

    # index it, return True
    assert table.create_spatial_index("geometry")

    assert "idx_locations_geometry" in db.table_names()

    # call it again, return False
    assert not table.create_spatial_index("geometry")


# cli tests
@pytest.mark.parametrize("use_spatialite_shortcut", [True, False])
def test_query_load_extension(use_spatialite_shortcut):
    # Without --load-extension:
    result = CliRunner().invoke(cli, [":memory:", "select spatialite_version()"])
    assert result.exit_code == 1
    assert "no such function: spatialite_version" in result.output
    # With --load-extension:
    if use_spatialite_shortcut:
        load_extension = "spatialite"
    else:
        load_extension = find_spatialite()
    result = CliRunner().invoke(
        cli,
        [
            ":memory:",
            "select spatialite_version()",
            f"--load-extension={load_extension}",
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert ["spatialite_version()"] == list(json.loads(result.output)[0].keys())


def test_cli_create_spatialite(tmpdir):
    # sqlite-utils create test.db --init-spatialite
    db_path = tmpdir / "created.db"
    result = CliRunner().invoke(
        cli, ["create-database", str(db_path), "--init-spatialite"]
    )

    assert result.exit_code == 0
    assert db_path.exists()
    assert db_path.read_binary()[:16] == b"SQLite format 3\x00"

    db = Database(str(db_path))
    assert "spatial_ref_sys" in db.table_names()


def test_cli_add_geometry_column(tmpdir):
    # create a rowid table with one column
    db_path = tmpdir / "spatial.db"
    db = Database(str(db_path))
    db.init_spatialite()

    table = db.table("locations").create({"name": str})

    result = CliRunner().invoke(
        cli,
        [
            "add-geometry-column",
            str(db_path),
            table.name,
            "geometry",
            "--type",
            "POINT",
        ],
    )

    assert result.exit_code == 0

    assert db.table("geometry_columns").get(["locations", "geometry"]) == {
        "f_table_name": "locations",
        "f_geometry_column": "geometry",
        "geometry_type": 1,  # point
        "coord_dimension": 2,
        "srid": 4326,
        "spatial_index_enabled": 0,
    }


def test_cli_add_geometry_column_options(tmpdir):
    # create a rowid table with one column
    db_path = tmpdir / "spatial.db"
    db = Database(str(db_path))
    db.init_spatialite()
    table = db.table("locations").create({"name": str})

    result = CliRunner().invoke(
        cli,
        [
            "add-geometry-column",
            str(db_path),
            table.name,
            "geometry",
            "-t",
            "POLYGON",
            "--srid",
            "3857",  # https://epsg.io/3857
            "--not-null",
        ],
    )

    assert result.exit_code == 0

    assert db.table("geometry_columns").get(["locations", "geometry"]) == {
        "f_table_name": "locations",
        "f_geometry_column": "geometry",
        "geometry_type": 3,  # polygon
        "coord_dimension": 2,
        "srid": 3857,
        "spatial_index_enabled": 0,
    }

    column = table.columns[1]
    assert column.notnull


def test_cli_add_geometry_column_invalid_type(tmpdir):
    # create a rowid table with one column
    db_path = tmpdir / "spatial.db"
    db = Database(str(db_path))
    db.init_spatialite()

    table = db.table("locations").create({"name": str})

    result = CliRunner().invoke(
        cli,
        [
            "add-geometry-column",
            str(db_path),
            table.name,
            "geometry",
            "--type",
            "NOT-A-TYPE",
        ],
    )

    assert 2 == result.exit_code


def test_cli_create_spatial_index(tmpdir):
    # create a rowid table with one column
    db_path = tmpdir / "spatial.db"
    db = Database(str(db_path))
    db.init_spatialite()

    table = db.table("locations").create({"name": str})
    table.add_geometry_column("geometry", "POINT")

    result = CliRunner().invoke(
        cli, ["create-spatial-index", str(db_path), table.name, "geometry"]
    )

    assert result.exit_code == 0

    assert "idx_locations_geometry" in db.table_names()

```

### `tests/test_hypothesis.py`

```py
import hypothesis.strategies as st
from hypothesis import given

import sqlite_utils


# SQLite integers are -(2^63) to 2^63 - 1
@given(st.integers(-9223372036854775808, 9223372036854775807))
def test_roundtrip_integers(integer):
    db = sqlite_utils.Database(memory=True)
    row = {
        "integer": integer,
    }
    db.table("test").insert(row)
    assert list(db.table("test").rows) == [row]


@given(st.text())
def test_roundtrip_text(text):
    db = sqlite_utils.Database(memory=True)
    row = {
        "text": text,
    }
    db.table("test").insert(row)
    assert list(db.table("test").rows) == [row]


@given(st.binary(max_size=1024 * 1024))
def test_roundtrip_binary(binary):
    db = sqlite_utils.Database(memory=True)
    row = {
        "binary": binary,
    }
    db.table("test").insert(row)
    assert list(db.table("test").rows) == [row]


@given(st.floats(allow_nan=False))
def test_roundtrip_floats(floats):
    db = sqlite_utils.Database(memory=True)
    row = {
        "floats": floats,
    }
    db.table("test").insert(row)
    assert list(db.table("test").rows) == [row]

```

### `tests/test_insert_files.py`

```py
import os
import pathlib
import sys

import pytest
from click.testing import CliRunner

from sqlite_utils import Database, cli


@pytest.mark.parametrize("silent", (False, True))
@pytest.mark.parametrize(
    "pk_args,expected_pks",
    (
        (["--pk", "path"], ["path"]),
        (["--pk", "path", "--pk", "name"], ["path", "name"]),
    ),
)
def test_insert_files(silent, pk_args, expected_pks):
    runner = CliRunner()
    with runner.isolated_filesystem():
        tmpdir = pathlib.Path(".")
        db_path = str(tmpdir / "files.db")
        (tmpdir / "one.txt").write_text("This is file one", "utf-8")
        (tmpdir / "two.txt").write_text("Two is shorter", "utf-8")
        (tmpdir / "nested").mkdir()
        (tmpdir / "nested" / "three.zz.txt").write_text("Three is nested", "utf-8")
        coltypes = (
            "name",
            "path",
            "fullpath",
            "sha256",
            "md5",
            "mode",
            "content",
            "content_text",
            "mtime",
            "ctime",
            "mtime_int",
            "ctime_int",
            "mtime_iso",
            "ctime_iso",
            "size",
            "suffix",
            "stem",
        )
        cols = []
        for coltype in coltypes:
            cols += ["-c", f"{coltype}:{coltype}"]
        result = runner.invoke(
            cli.cli,
            ["insert-files", db_path, "files", str(tmpdir)]
            + cols
            + pk_args
            + (["--silent"] if silent else []),
            catch_exceptions=False,
        )
        assert result.exit_code == 0, result.stdout
        db = Database(db_path)
        rows_by_path = {r["path"]: r for r in db.table("files").rows}
        one, two, three = (
            rows_by_path["one.txt"],
            rows_by_path["two.txt"],
            rows_by_path[os.path.join("nested", "three.zz.txt")],
        )
        assert {
            "content": b"This is file one",
            "content_text": "This is file one",
            "md5": "556dfb57fce9ca301f914e2273adf354",
            "name": "one.txt",
            "path": "one.txt",
            "sha256": "e34138f26b5f7368f298b4e736fea0aad87ddec69fbd04dc183b20f4d844bad5",
            "size": 16,
            "stem": "one",
            "suffix": ".txt",
        }.items() <= one.items()
        assert {
            "content": b"Two is shorter",
            "content_text": "Two is shorter",
            "md5": "f86f067b083af1911043eb215e74ac70",
            "name": "two.txt",
            "path": "two.txt",
            "sha256": "9368988ed16d4a2da0af9db9b686d385b942cb3ffd4e013f43aed2ec041183d9",
            "size": 14,
            "stem": "two",
            "suffix": ".txt",
        }.items() <= two.items()
        assert {
            "content": b"Three is nested",
            "content_text": "Three is nested",
            "md5": "12580f341781f5a5b589164d3cd39523",
            "name": "three.zz.txt",
            "path": os.path.join("nested", "three.zz.txt"),
            "sha256": "6dd45aaaaa6b9f96af19363a92c8fca5d34791d3c35c44eb19468a6a862cc8cd",
            "size": 15,
            "stem": "three.zz",
            "suffix": ".txt",
        }.items() <= three.items()
        # Assert the other int/str/float columns exist and are of the right types
        expected_types = {
            "ctime": float,
            "ctime_int": int,
            "ctime_iso": str,
            "mtime": float,
            "mtime_int": int,
            "mtime_iso": str,
            "mode": int,
            "fullpath": str,
            "content": bytes,
            "content_text": str,
            "stem": str,
            "suffix": str,
        }
        for colname, expected_type in expected_types.items():
            for row in (one, two, three):
                assert isinstance(row[colname], expected_type)
        assert set(db.table("files").pks) == set(expected_pks)


@pytest.mark.parametrize(
    "use_text,encoding,input,expected",
    (
        (False, None, "hello world", b"hello world"),
        (True, None, "hello world", "hello world"),
        (False, None, b"S\xe3o Paulo", b"S\xe3o Paulo"),
        (True, "latin-1", b"S\xe3o Paulo", "S\xe3o Paulo"),
    ),
)
def test_insert_files_stdin(use_text, encoding, input, expected):
    runner = CliRunner()
    with runner.isolated_filesystem():
        tmpdir = pathlib.Path(".")
        db_path = str(tmpdir / "files.db")
        args = ["insert-files", db_path, "files", "-", "--name", "stdin-name"]
        if use_text:
            args += ["--text"]
        if encoding is not None:
            args += ["--encoding", encoding]
        result = runner.invoke(
            cli.cli,
            args,
            catch_exceptions=False,
            input=input,
        )
        assert result.exit_code == 0, result.stdout
        db = Database(db_path)
        row = next(iter(db.table("files").rows))
        key = "content"
        if use_text:
            key = "content_text"
        assert {"path": "stdin-name", key: expected}.items() <= row.items()


@pytest.mark.skipif(
    sys.platform.startswith("win"),
    reason="Windows has a different way of handling default encodings",
)
def test_insert_files_bad_text_encoding_error():
    runner = CliRunner()
    with runner.isolated_filesystem():
        tmpdir = pathlib.Path(".")
        latin = tmpdir / "latin.txt"
        latin.write_bytes(b"S\xe3o Paulo")
        db_path = str(tmpdir / "files.db")
        result = runner.invoke(
            cli.cli,
            ["insert-files", db_path, "files", str(latin), "--text"],
            catch_exceptions=False,
        )
        assert result.exit_code == 1, result.output
        assert result.output.strip().startswith(
            f"Error: Could not read file '{latin.resolve()!s}' as text"
        )

```

### `tests/test_introspect.py`

```py
import pytest

from sqlite_utils.db import Check, Database, Index, Table, View, XIndex, XIndexColumn


def _check_supports_strict():
    """Check if SQLite supports strict tables without leaking the database."""
    db = Database(memory=True)
    result = db.supports_strict
    db.close()
    return result


def test_table_names(existing_db):
    assert ["foo"] == existing_db.table_names()


def test_view_names(fresh_db):
    fresh_db.create_view("foo_view", "select 1")
    assert ["foo_view"] == fresh_db.view_names()


def test_table_names_fts4(existing_db):
    existing_db.table("woo").insert({"title": "Hello"}).enable_fts(
        ["title"], fts_version="FTS4"
    )
    existing_db.table("woo2").insert({"title": "Hello"}).enable_fts(
        ["title"], fts_version="FTS5"
    )
    assert ["woo_fts"] == existing_db.table_names(fts4=True)
    assert ["woo2_fts"] == existing_db.table_names(fts5=True)


def test_detect_fts(existing_db):
    existing_db.table("woo").insert({"title": "Hello"}).enable_fts(
        ["title"], fts_version="FTS4"
    )
    existing_db.table("woo2").insert({"title": "Hello"}).enable_fts(
        ["title"], fts_version="FTS5"
    )
    assert "woo_fts" == existing_db.table("woo").detect_fts()
    assert "woo_fts" == existing_db.table("woo_fts").detect_fts()
    assert "woo2_fts" == existing_db.table("woo2").detect_fts()
    assert "woo2_fts" == existing_db.table("woo2_fts").detect_fts()
    assert existing_db.table("foo").detect_fts() is None


@pytest.mark.parametrize("reverse_order", (True, False))
def test_detect_fts_similar_tables(fresh_db, reverse_order):
    # https://github.com/simonw/sqlite-utils/issues/434
    table1, table2 = ("demo", "demo2")
    if reverse_order:
        table1, table2 = table2, table1

    fresh_db.table(table1).insert({"title": "Hello"}).enable_fts(
        ["title"], fts_version="FTS4"
    )
    fresh_db.table(table2).insert({"title": "Hello"}).enable_fts(
        ["title"], fts_version="FTS4"
    )
    assert fresh_db.table(table1).detect_fts() == f"{table1}_fts"
    assert fresh_db.table(table2).detect_fts() == f"{table2}_fts"


def test_tables(existing_db):
    assert len(existing_db.tables) == 1
    assert existing_db.tables[0].name == "foo"


def test_views(fresh_db):
    fresh_db.create_view("foo_view", "select 1")
    assert len(fresh_db.views) == 1
    view = fresh_db.views[0]
    assert isinstance(view, View)
    assert view.name == "foo_view"
    assert repr(view) == "<View foo_view (1)>"
    assert view.columns_dict == {"1": str}


def test_getitem_returns_table_or_view(fresh_db):
    fresh_db.table("items").insert({"id": 1}, pk="id")
    fresh_db.create_view("item_ids", "select id from items")

    assert isinstance(fresh_db["items"], Table)
    assert isinstance(fresh_db["item_ids"], View)


def test_count(existing_db):
    assert existing_db.table("foo").count == 3
    assert existing_db.table("foo").count_where() == 3
    assert existing_db.table("foo").execute_count() == 3


def test_count_where(existing_db):
    assert existing_db.table("foo").count_where("text != ?", ["two"]) == 2
    assert existing_db.table("foo").count_where("text != :t", {"t": "two"}) == 2


def test_columns(existing_db):
    table = existing_db.table("foo")
    assert [{"name": "text", "type": "TEXT"}] == [
        {"name": col.name, "type": col.type} for col in table.columns
    ]


def test_table_schema(existing_db):
    assert existing_db.table("foo").schema == "CREATE TABLE foo (text TEXT)"


def test_database_schema(existing_db):
    assert existing_db.schema == "CREATE TABLE foo (text TEXT);"


def test_table_repr(fresh_db):
    table = fresh_db.table("dogs").insert({"name": "Cleo", "age": 4})
    assert "<Table dogs (name, age)>" == repr(table)
    assert "<Table cats (does not exist yet)>" == repr(fresh_db.table("cats"))


def test_indexes(fresh_db):
    fresh_db.executescript("""
        create table Gosh (c1 text, c2 text, c3 text);
        create index Gosh_c1 on Gosh(c1);
        create index Gosh_c2c3 on Gosh(c2, c3);
    """)
    assert [
        Index(
            seq=0,
            name="Gosh_c2c3",
            unique=0,
            origin="c",
            partial=0,
            columns=["c2", "c3"],
        ),
        Index(seq=1, name="Gosh_c1", unique=0, origin="c", partial=0, columns=["c1"]),
    ] == fresh_db.table("Gosh").indexes


def test_xindexes(fresh_db):
    fresh_db.executescript("""
        create table Gosh (c1 text, c2 text, c3 text);
        create index Gosh_c1 on Gosh(c1);
        create index Gosh_c2c3 on Gosh(c2, c3 desc);
    """)
    assert fresh_db.table("Gosh").xindexes == [
        XIndex(
            name="Gosh_c2c3",
            columns=[
                XIndexColumn(seqno=0, cid=1, name="c2", desc=0, coll="BINARY", key=1),
                XIndexColumn(seqno=1, cid=2, name="c3", desc=1, coll="BINARY", key=1),
                XIndexColumn(seqno=2, cid=-1, name=None, desc=0, coll="BINARY", key=0),
            ],
        ),
        XIndex(
            name="Gosh_c1",
            columns=[
                XIndexColumn(seqno=0, cid=0, name="c1", desc=0, coll="BINARY", key=1),
                XIndexColumn(seqno=1, cid=-1, name=None, desc=0, coll="BINARY", key=0),
            ],
        ),
    ]


def test_indexes_with_double_quotes_in_identifiers(fresh_db):
    fresh_db['Go"sh'].insert({"id": 1, 'c"1': 2}, pk="id")
    fresh_db['Go"sh'].create_index(['c"1'])
    assert [(index.name, index.columns) for index in fresh_db['Go"sh'].indexes] == [
        ('idx_Go"sh_c"1', ['c"1'])
    ]
    assert fresh_db['Go"sh'].xindexes == [
        XIndex(
            name='idx_Go"sh_c"1',
            columns=[
                XIndexColumn(seqno=0, cid=1, name='c"1', desc=0, coll="BINARY", key=1),
                XIndexColumn(seqno=1, cid=-1, name=None, desc=0, coll="BINARY", key=0),
            ],
        )
    ]


def test_transform_table_with_double_quotes_in_identifiers(fresh_db):
    fresh_db['Go"sh'].insert({"id": 1, 'c"1': 2, "c2": 3}, pk="id")
    fresh_db['Go"sh'].create_index(['c"1'])
    fresh_db['Go"sh'].transform(types={"c2": str})
    assert fresh_db['Go"sh'].columns_dict["c2"] is str
    assert [index.columns for index in fresh_db['Go"sh'].indexes] == [['c"1']]


@pytest.mark.parametrize(
    "column,expected_table_guess",
    (
        ("author", "authors"),
        ("author_id", "authors"),
        ("authors", "authors"),
        ("genre", "genre"),
        ("genre_id", "genre"),
    ),
)
def test_guess_foreign_table(fresh_db, column, expected_table_guess):
    fresh_db.create_table("authors", {"name": str})
    fresh_db.create_table("genre", {"name": str})
    assert expected_table_guess == fresh_db.table("books").guess_foreign_table(column)


@pytest.mark.parametrize(
    "pk,expected", ((None, ["rowid"]), ("id", ["id"]), (["id", "id2"], ["id", "id2"]))
)
def test_pks(fresh_db, pk, expected):
    fresh_db.table("foo").insert_all([{"id": 1, "id2": 2}], pk=pk)
    assert expected == fresh_db.table("foo").pks


def test_checks(fresh_db):
    fresh_db.execute("""
        CREATE TABLE scores (
            score INTEGER CONSTRAINT positive CHECK(score > 0),
            maximum INTEGER,
            CONSTRAINT within_maximum CHECK(score <= maximum)
        )
    """)
    scores = fresh_db.table("scores")
    expected_column = Check("score > 0", name="positive", column="score")
    expected_table = Check("score <= maximum", name="within_maximum")
    assert scores.checks == [expected_column, expected_table]
    assert scores.column_checks == {"score": [expected_column]}
    assert scores.table_checks == [expected_table]
    assert scores.checks[0].sql == "CONSTRAINT positive CHECK(score > 0)"


def test_checks_nonexistent_and_virtual_tables(fresh_db):
    assert fresh_db.table("does_not_exist").checks == []
    fresh_db.table("searchable").insert({"text": "hello"}).enable_fts(
        ["text"], fts_version="FTS5"
    )
    assert fresh_db.table("searchable_fts").checks == []


def test_triggers_and_triggers_dict(fresh_db):
    assert [] == fresh_db.triggers
    authors = fresh_db.table("authors")
    authors.insert_all(
        [
            {"name": "Frank Herbert", "famous_works": "Dune"},
            {"name": "Neal Stephenson", "famous_works": "Cryptonomicon"},
        ]
    )
    fresh_db.table("other").insert({"foo": "bar"})
    assert authors.triggers == []
    assert authors.triggers_dict == {}
    assert fresh_db.table("other").triggers == []
    assert fresh_db.triggers_dict == {}
    authors.enable_fts(
        ["name", "famous_works"], fts_version="FTS4", create_triggers=True
    )
    expected_triggers = {
        ("authors_ai", "authors"),
        ("authors_ad", "authors"),
        ("authors_au", "authors"),
    }
    assert expected_triggers == {(t.name, t.table) for t in fresh_db.triggers}
    assert expected_triggers == {
        (t.name, t.table) for t in fresh_db.table("authors").triggers
    }
    expected_triggers = {
        "authors_ai": (
            'CREATE TRIGGER "authors_ai" AFTER INSERT ON "authors" BEGIN\n'
            '  INSERT INTO "authors_fts" (rowid, "name", "famous_works") VALUES (new.rowid, new."name", new."famous_works");\n'
            "END"
        ),
        "authors_ad": (
            'CREATE TRIGGER "authors_ad" AFTER DELETE ON "authors" BEGIN\n'
            '  INSERT INTO "authors_fts" ("authors_fts", rowid, "name", "famous_works") VALUES(\'delete\', old.rowid, old."name", old."famous_works");\n'
            "END"
        ),
        "authors_au": (
            'CREATE TRIGGER "authors_au" AFTER UPDATE ON "authors" BEGIN\n'
            '  INSERT INTO "authors_fts" ("authors_fts", rowid, "name", "famous_works") VALUES(\'delete\', old.rowid, old."name", old."famous_works");\n'
            '  INSERT INTO "authors_fts" (rowid, "name", "famous_works") VALUES (new.rowid, new."name", new."famous_works");\nEND'
        ),
    }
    assert authors.triggers_dict == expected_triggers
    assert fresh_db.table("other").triggers == []
    assert fresh_db.table("other").triggers_dict == {}
    assert fresh_db.triggers_dict == expected_triggers


def test_has_counts_triggers(fresh_db):
    authors = fresh_db.table("authors")
    authors.insert({"name": "Frank Herbert"})
    assert not authors.has_counts_triggers
    authors.enable_counts()
    assert authors.has_counts_triggers


@pytest.mark.parametrize(
    "sql,expected_name,expected_using",
    [
        (
            """
            CREATE VIRTUAL TABLE foo USING FTS5(name)
            """,
            "foo",
            "FTS5",
        ),
        (
            """
            CREATE VIRTUAL TABLE "foo" USING FTS4(name)
            """,
            "foo",
            "FTS4",
        ),
        (
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS `foo` USING FTS4(name)
            """,
            "foo",
            "FTS4",
        ),
        (
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS `foo` USING fts5(name)
            """,
            "foo",
            "FTS5",
        ),
        (
            """
            CREATE TABLE IF NOT EXISTS `foo` (id integer primary key)
            """,
            "foo",
            None,
        ),
    ],
)
def test_virtual_table_using(fresh_db, sql, expected_name, expected_using):
    fresh_db.execute(sql)
    assert fresh_db.table(expected_name).virtual_table_using == expected_using


def test_use_rowid(fresh_db):
    fresh_db.table("rowid_table").insert({"name": "Cleo"})
    fresh_db.table("regular_table").insert({"id": 1, "name": "Cleo"}, pk="id")
    assert fresh_db.table("rowid_table").use_rowid
    assert not fresh_db.table("regular_table").use_rowid


@pytest.mark.skipif(
    not _check_supports_strict(),
    reason="Needs SQLite version that supports strict",
)
@pytest.mark.parametrize(
    "create_table,expected_strict",
    (
        ("create table t (id integer) strict", True),
        ("create table t (id integer) STRICT", True),
        ("create table t (id integer primary key) StriCt, WITHOUT ROWID", True),
        ("create table t (id integer primary key) WITHOUT ROWID", False),
        ("create table t (id integer)", False),
    ),
)
def test_table_strict(fresh_db, create_table, expected_strict):
    fresh_db.execute(create_table)
    table = fresh_db.table("t")
    assert table.strict == expected_strict


@pytest.mark.parametrize(
    "value",
    (
        1,
        1.3,
        "foo",
        "O'Brien",
        True,
        b"binary",
    ),
)
def test_table_default_values(fresh_db, value):
    fresh_db.table("default_values").insert(
        {"nodefault": 1, "value": value}, defaults={"value": value}
    )
    default_values = fresh_db.table("default_values").default_values
    assert default_values == {"value": value}


def test_table_default_values_escaped_quotes(fresh_db):
    # SQLite stores string defaults with single quotes doubled, so
    # introspection needs to unescape them again
    fresh_db.execute(
        "create table t (id integer primary key, name text default 'O''Brien')"
    )
    assert "default 'O''Brien'" in fresh_db.table("t").schema
    assert fresh_db.table("t").default_values == {"name": "O'Brien"}


def test_table_default_values_keyword_literals(fresh_db):
    fresh_db.execute(
        "create table t ("
        "enabled integer default TRUE, "
        "disabled integer default false, "
        "nullable text default NULL"
        ")"
    )
    assert fresh_db.table("t").default_values == {
        "enabled": True,
        "disabled": False,
        "nullable": None,
    }


def test_pks_use_primary_key_declaration_order(fresh_db):
    # PRIMARY KEY (a, b) declared against columns stored in order (b, a) -
    # pks must follow the declaration order, which is what SQLite uses to
    # resolve implicit foreign key references and compound pk lookups
    fresh_db.execute("create table t (b text, a text, primary key (a, b))")
    assert fresh_db.table("t").pks == ["a", "b"]


def test_transform_preserves_compound_pk_declaration_order(fresh_db):
    fresh_db.execute("create table t (a text, b text, c text, primary key (b, a))")
    fresh_db.table("t").transform(drop={"c"})
    assert fresh_db.table("t").pks == ["b", "a"]
    assert 'PRIMARY KEY ("b", "a")' in fresh_db.table("t").schema

```

### `tests/test_list_mode.py`

```py
"""
Tests for list-based iteration in insert_all and upsert_all
"""

import pytest

from sqlite_utils import Database


def test_insert_all_list_mode_basic():
    """Test basic insert_all with list-based iteration"""
    db = Database(memory=True)

    def data_generator():
        # First yield column names
        yield ["id", "name", "age"]
        # Then yield data rows
        yield [1, "Alice", 30]
        yield [2, "Bob", 25]
        yield [3, "Charlie", 35]

    db.table("people").insert_all(data_generator())

    rows = list(db.table("people").rows)
    assert len(rows) == 3
    assert rows[0] == {"id": 1, "name": "Alice", "age": 30}
    assert rows[1] == {"id": 2, "name": "Bob", "age": 25}
    assert rows[2] == {"id": 3, "name": "Charlie", "age": 35}


def test_insert_all_list_mode_with_pk():
    """Test insert_all with list mode and primary key"""
    db = Database(memory=True)

    def data_generator():
        yield ["id", "name", "score"]
        yield [1, "Alice", 95]
        yield [2, "Bob", 87]

    db.table("scores").insert_all(data_generator(), pk="id")

    assert db.table("scores").pks == ["id"]
    rows = list(db.table("scores").rows)
    assert len(rows) == 2


def test_upsert_all_list_mode():
    """Test upsert_all with list-based iteration"""
    db = Database(memory=True)

    # Initial insert
    def initial_data():
        yield ["id", "name", "value"]
        yield [1, "Alice", 100]
        yield [2, "Bob", 200]

    db.table("data").insert_all(initial_data(), pk="id")

    # Upsert with some updates and new records
    def upsert_data():
        yield ["id", "name", "value"]
        yield [1, "Alice", 150]  # Update existing
        yield [3, "Charlie", 300]  # Insert new

    db.table("data").upsert_all(upsert_data(), pk="id")

    rows = list(db.table("data").rows_where(order_by="id"))
    assert len(rows) == 3
    assert rows[0] == {"id": 1, "name": "Alice", "value": 150}
    assert rows[1] == {"id": 2, "name": "Bob", "value": 200}
    assert rows[2] == {"id": 3, "name": "Charlie", "value": 300}


def test_list_mode_with_various_types():
    """Test list mode with different data types"""
    db = Database(memory=True)

    def data_generator():
        yield ["id", "name", "score", "active"]
        yield [1, "Alice", 95.5, True]
        yield [2, "Bob", 87.3, False]
        yield [3, "Charlie", None, True]

    db.table("mixed").insert_all(data_generator())

    rows = list(db.table("mixed").rows)
    assert len(rows) == 3
    assert rows[0]["score"] == 95.5
    assert rows[1]["active"] == 0  # SQLite stores boolean as int
    assert rows[2]["score"] is None


def test_list_mode_error_non_string_columns():
    """Test that non-string column names raise an error"""
    db = Database(memory=True)

    def bad_data():
        yield [1, 2, 3]  # Non-string column names
        yield ["a", "b", "c"]

    with pytest.raises(ValueError, match="must be a list of column name strings"):
        db.table("bad").insert_all(bad_data())  # type: ignore[arg-type]


def test_list_mode_error_mixed_types():
    """Test that mixing list and dict raises an error"""
    db = Database(memory=True)

    def bad_data():
        yield ["id", "name"]
        yield {"id": 1, "name": "Alice"}  # Should be a list, not dict

    with pytest.raises(ValueError, match="must also be lists"):
        db.table("bad").insert_all(bad_data())  # type: ignore[arg-type]


def test_list_mode_empty_after_headers():
    """Test that only headers without data works gracefully"""
    db = Database(memory=True)

    def data_generator():
        yield ["id", "name", "age"]
        # No data rows

    result = db.table("people").insert_all(data_generator())
    assert result is not None
    assert not db.table("people").exists()


def test_list_mode_batch_processing():
    """Test list mode with large dataset requiring batching"""
    db = Database(memory=True)

    def large_data():
        yield ["id", "value"]
        for i in range(1000):
            yield [i, f"value_{i}"]

    db.table("large").insert_all(large_data(), batch_size=100)

    count = db.execute("SELECT COUNT(*) as c FROM large").fetchone()[0]
    assert count == 1000


def test_list_mode_shorter_rows():
    """Test that rows shorter than column list get NULL values"""
    db = Database(memory=True)

    def data_generator():
        yield ["id", "name", "age", "city"]
        yield [1, "Alice", 30, "NYC"]
        yield [2, "Bob"]  # Missing age and city
        yield [3, "Charlie", 35]  # Missing city

    db.table("people").insert_all(data_generator())

    rows = list(db.table("people").rows_where(order_by="id"))
    assert rows[0] == {"id": 1, "name": "Alice", "age": 30, "city": "NYC"}
    assert rows[1] == {"id": 2, "name": "Bob", "age": None, "city": None}
    assert rows[2] == {"id": 3, "name": "Charlie", "age": 35, "city": None}


def test_backwards_compatibility_dict_mode():
    """Ensure dict mode still works (backward compatibility)"""
    db = Database(memory=True)

    # Traditional dict-based insert
    data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
    ]

    db.table("people").insert_all(data)

    rows = list(db.table("people").rows)
    assert len(rows) == 2
    assert rows[0] == {"id": 1, "name": "Alice", "age": 30}


def test_insert_all_tuple_mode_basic():
    """Test basic insert_all with tuple-based iteration"""
    db = Database(memory=True)

    def data_generator():
        # First yield column names as tuple
        yield ("id", "name", "age")
        # Then yield data rows as tuples
        yield (1, "Alice", 30)
        yield (2, "Bob", 25)
        yield (3, "Charlie", 35)

    db.table("people").insert_all(data_generator())

    rows = list(db.table("people").rows)
    assert len(rows) == 3
    assert rows[0] == {"id": 1, "name": "Alice", "age": 30}
    assert rows[1] == {"id": 2, "name": "Bob", "age": 25}
    assert rows[2] == {"id": 3, "name": "Charlie", "age": 35}


def test_insert_all_mixed_list_tuple():
    """Test insert_all with mixed lists and tuples for data rows"""
    db = Database(memory=True)

    def data_generator():
        # Column names as list
        yield ["id", "name", "age"]
        # Mix of list and tuple data rows
        yield [1, "Alice", 30]
        yield (2, "Bob", 25)
        yield [3, "Charlie", 35]
        yield (4, "Diana", 40)

    db.table("people").insert_all(data_generator())

    rows = list(db.table("people").rows)
    assert len(rows) == 4
    assert rows[0] == {"id": 1, "name": "Alice", "age": 30}
    assert rows[1] == {"id": 2, "name": "Bob", "age": 25}
    assert rows[2] == {"id": 3, "name": "Charlie", "age": 35}
    assert rows[3] == {"id": 4, "name": "Diana", "age": 40}


def test_upsert_all_tuple_mode():
    """Test upsert_all with tuple-based iteration"""
    db = Database(memory=True)

    # Initial insert with tuples
    def initial_data():
        yield ("id", "name", "value")
        yield (1, "Alice", 100)
        yield (2, "Bob", 200)

    db.table("data").insert_all(initial_data(), pk="id")

    # Upsert with tuples
    def upsert_data():
        yield ("id", "name", "value")
        yield (1, "Alice", 150)  # Update existing
        yield (3, "Charlie", 300)  # Insert new

    db.table("data").upsert_all(upsert_data(), pk="id")

    rows = list(db.table("data").rows_where(order_by="id"))
    assert len(rows) == 3
    assert rows[0] == {"id": 1, "name": "Alice", "value": 150}
    assert rows[1] == {"id": 2, "name": "Bob", "value": 200}
    assert rows[2] == {"id": 3, "name": "Charlie", "value": 300}


def test_tuple_mode_shorter_rows():
    """Test that tuple rows shorter than column list get NULL values"""
    db = Database(memory=True)

    def data_generator():
        yield "id", "name", "age", "city"
        yield 1, "Alice", 30, "NYC"
        yield 2, "Bob"  # Missing age and city
        yield 3, "Charlie", 35  # Missing city

    db.table("people").insert_all(data_generator())

    rows = list(db.table("people").rows_where(order_by="id"))
    assert rows[0] == {"id": 1, "name": "Alice", "age": 30, "city": "NYC"}
    assert rows[1] == {"id": 2, "name": "Bob", "age": None, "city": None}
    assert rows[2] == {"id": 3, "name": "Charlie", "age": 35, "city": None}


def test_list_mode_single_record_upsert_last_pk():
    """Test that last_pk is populated correctly for single-record upserts in list mode"""
    db = Database(memory=True)

    # Create table first
    db.table("data").insert({"id": 1, "name": "Alice", "value": 100}, pk="id")

    # Now upsert a single record using list mode
    def upsert_data():
        yield ["id", "name", "value"]
        yield [1, "Alice", 150]  # Update existing

    table = db.table("data")
    table.upsert_all(upsert_data(), pk="id")

    # Verify the data was updated
    rows = list(db.table("data").rows)
    assert rows == [{"id": 1, "name": "Alice", "value": 150}]

    # Verify last_pk is populated correctly
    assert table.last_pk == 1

```

### `tests/test_lookup.py`

```py
import pytest

from sqlite_utils.db import Index


def test_lookup_new_table(fresh_db):
    species = fresh_db.table("species")
    palm_id = species.lookup({"name": "Palm"})
    oak_id = species.lookup({"name": "Oak"})
    cherry_id = species.lookup({"name": "Cherry"})
    assert palm_id == species.lookup({"name": "Palm"})
    assert oak_id == species.lookup({"name": "Oak"})
    assert cherry_id == species.lookup({"name": "Cherry"})
    assert palm_id != oak_id != cherry_id
    # Ensure the correct indexes were created
    assert [
        Index(
            seq=0,
            name="idx_species_name",
            unique=1,
            origin="c",
            partial=0,
            columns=["name"],
        )
    ] == species.indexes


def test_lookup_new_table_compound_key(fresh_db):
    species = fresh_db.table("species")
    palm_id = species.lookup({"name": "Palm", "type": "Tree"})
    oak_id = species.lookup({"name": "Oak", "type": "Tree"})
    assert palm_id == species.lookup({"name": "Palm", "type": "Tree"})
    assert oak_id == species.lookup({"name": "Oak", "type": "Tree"})
    assert [
        Index(
            seq=0,
            name="idx_species_name_type",
            unique=1,
            origin="c",
            partial=0,
            columns=["name", "type"],
        )
    ] == species.indexes


def test_lookup_adds_unique_constraint_to_existing_table(fresh_db):
    species = fresh_db.table("species", pk="id")
    palm_id = species.insert({"name": "Palm"}).last_pk
    species.insert({"name": "Oak"})
    assert [] == species.indexes
    assert palm_id == species.lookup({"name": "Palm"})
    assert [
        Index(
            seq=0,
            name="idx_species_name",
            unique=1,
            origin="c",
            partial=0,
            columns=["name"],
        )
    ] == species.indexes


def test_lookup_fails_if_constraint_cannot_be_added(fresh_db):
    species = fresh_db.table("species", pk="id")
    species.insert_all([{"id": 1, "name": "Palm"}, {"id": 2, "name": "Palm"}])
    # This will fail because the name column is not unique
    with pytest.raises(Exception, match="UNIQUE constraint failed"):
        species.lookup({"name": "Palm"})


def test_lookup_with_extra_values(fresh_db):
    species = fresh_db.table("species")
    id = species.lookup({"name": "Palm", "type": "Tree"}, {"first_seen": "2020-01-01"})
    assert species.get(id) == {
        "id": 1,
        "name": "Palm",
        "type": "Tree",
        "first_seen": "2020-01-01",
    }
    # A subsequent lookup() should ignore the second dictionary
    id2 = species.lookup({"name": "Palm", "type": "Tree"}, {"first_seen": "2021-02-02"})
    assert id2 == id
    assert species.get(id2) == {
        "id": 1,
        "name": "Palm",
        "type": "Tree",
        "first_seen": "2020-01-01",
    }


def test_lookup_with_extra_insert_parameters(fresh_db):
    other_table = fresh_db.table("other_table")
    other_table.insert({"id": 1, "name": "Name"}, pk="id")
    species = fresh_db.table("species")
    id = species.lookup(
        {"name": "Palm", "type": "Tree"},
        {
            "first_seen": "2020-01-01",
            "make_not_null": 1,
            "fk_to_other": 1,
            "default_is_dog": "cat",
            "extract_this": "This is extracted",
            "convert_to_upper": "upper",
            "make_this_integer": "2",
            "this_at_front": 1,
        },
        pk="renamed_id",
        foreign_keys=(("fk_to_other", "other_table", "id"),),
        column_order=("this_at_front",),
        not_null={"make_not_null"},
        defaults={"default_is_dog": "dog"},
        extracts=["extract_this"],
        conversions={"convert_to_upper": "upper(?)"},
        columns={"make_this_integer": int},
    )
    assert species.schema == (
        'CREATE TABLE "species" (\n'
        '   "renamed_id" INTEGER PRIMARY KEY,\n'
        '   "this_at_front" INTEGER,\n'
        '   "name" TEXT,\n'
        '   "type" TEXT,\n'
        '   "first_seen" TEXT,\n'
        '   "make_not_null" INTEGER NOT NULL,\n'
        '   "fk_to_other" INTEGER REFERENCES "other_table"("id"),\n'
        "   \"default_is_dog\" TEXT DEFAULT 'dog',\n"
        '   "extract_this" INTEGER REFERENCES "extract_this"("id"),\n'
        '   "convert_to_upper" TEXT,\n'
        '   "make_this_integer" INTEGER\n'
        ")"
    )
    assert species.get(id) == {
        "renamed_id": id,
        "this_at_front": 1,
        "name": "Palm",
        "type": "Tree",
        "first_seen": "2020-01-01",
        "make_not_null": 1,
        "fk_to_other": 1,
        "default_is_dog": "cat",
        "extract_this": 1,
        "convert_to_upper": "UPPER",
        "make_this_integer": 2,
    }
    assert species.indexes == [
        Index(
            seq=0,
            name="idx_species_name_type",
            unique=1,
            origin="c",
            partial=0,
            columns=["name", "type"],
        )
    ]


@pytest.mark.parametrize("strict", (False, True))
def test_lookup_new_table_strict(fresh_db, strict):
    fresh_db.table("species").lookup({"name": "Palm"}, strict=strict)
    assert fresh_db.table("species").strict == strict or not fresh_db.supports_strict


def test_lookup_null_value_idempotent(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/186
    # Repeated lookups of a null value should return the same row,
    # not insert a duplicate row each time
    species = fresh_db.table("species")
    first_id = species.lookup({"name": None})
    second_id = species.lookup({"name": None})
    assert first_id == second_id
    assert list(species.rows) == [{"id": first_id, "name": None}]


def test_lookup_compound_key_with_null_idempotent(fresh_db):
    species = fresh_db.table("species")
    palm_id = species.lookup({"name": "Palm", "type": None})
    oak_id = species.lookup({"name": "Oak", "type": "Tree"})
    assert palm_id == species.lookup({"name": "Palm", "type": None})
    assert oak_id == species.lookup({"name": "Oak", "type": "Tree"})
    assert palm_id != oak_id
    assert list(species.rows) == [
        {"id": palm_id, "name": "Palm", "type": None},
        {"id": oak_id, "name": "Oak", "type": "Tree"},
    ]

```

### `tests/test_m2m.py`

```py
import pytest

from sqlite_utils.db import ForeignKey, NoObviousTable


def test_insert_m2m_single(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id").m2m(
        "humans", {"id": 1, "name": "Natalie D"}, pk="id"
    )
    assert {"dogs_humans", "humans", "dogs"} == set(fresh_db.table_names())
    humans = fresh_db.table("humans")
    dogs_humans = fresh_db.table("dogs_humans")
    assert [{"id": 1, "name": "Natalie D"}] == list(humans.rows)
    assert [{"humans_id": 1, "dogs_id": 1}] == list(dogs_humans.rows)


def test_insert_m2m_alter(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id").m2m(
        "humans", {"id": 1, "name": "Natalie D"}, pk="id"
    )
    dogs.update(1).m2m(
        "humans", {"id": 2, "name": "Simon W", "nerd": True}, pk="id", alter=True
    )
    assert list(fresh_db.table("humans").rows) == [
        {"id": 1, "name": "Natalie D", "nerd": None},
        {"id": 2, "name": "Simon W", "nerd": 1},
    ]
    assert list(fresh_db.table("dogs_humans").rows) == [
        {"humans_id": 1, "dogs_id": 1},
        {"humans_id": 2, "dogs_id": 1},
    ]


def test_insert_m2m_list(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id").m2m(
        "humans",
        [{"id": 1, "name": "Natalie D"}, {"id": 2, "name": "Simon W"}],
        pk="id",
    )
    assert {"dogs", "humans", "dogs_humans"} == set(fresh_db.table_names())
    humans = fresh_db.table("humans")
    dogs_humans = fresh_db.table("dogs_humans")
    assert [{"humans_id": 1, "dogs_id": 1}, {"humans_id": 2, "dogs_id": 1}] == list(
        dogs_humans.rows
    )
    assert [{"id": 1, "name": "Natalie D"}, {"id": 2, "name": "Simon W"}] == list(
        humans.rows
    )
    assert [
        ForeignKey(
            table="dogs_humans", column="dogs_id", other_table="dogs", other_column="id"
        ),
        ForeignKey(
            table="dogs_humans",
            column="humans_id",
            other_table="humans",
            other_column="id",
        ),
    ] == dogs_humans.foreign_keys


def test_insert_m2m_iterable(fresh_db):
    iterable_records = ({"id": 1, "name": "Phineas"}, {"id": 2, "name": "Ferb"})

    def iterable():
        yield from iterable_records

    platypuses = fresh_db.table("platypuses")
    platypuses.insert({"id": 1, "name": "Perry"}, pk="id").m2m(
        "humans",
        iterable(),
        pk="id",
    )

    assert {"platypuses", "humans", "humans_platypuses"} == set(fresh_db.table_names())
    humans = fresh_db.table("humans")
    humans_platypuses = fresh_db.table("humans_platypuses")
    assert [
        {"humans_id": 1, "platypuses_id": 1},
        {"humans_id": 2, "platypuses_id": 1},
    ] == list(humans_platypuses.rows)
    assert [{"id": 1, "name": "Phineas"}, {"id": 2, "name": "Ferb"}] == list(
        humans.rows
    )
    assert [
        ForeignKey(
            table="humans_platypuses",
            column="platypuses_id",
            other_table="platypuses",
            other_column="id",
        ),
        ForeignKey(
            table="humans_platypuses",
            column="humans_id",
            other_table="humans",
            other_column="id",
        ),
    ] == humans_platypuses.foreign_keys


def test_m2m_with_table_objects(fresh_db):
    dogs = fresh_db.table("dogs", pk="id")
    humans = fresh_db.table("humans", pk="id")
    dogs.insert({"id": 1, "name": "Cleo"}).m2m(
        humans, [{"id": 1, "name": "Natalie D"}, {"id": 2, "name": "Simon W"}]
    )
    expected_tables = {"dogs", "humans", "dogs_humans"}
    assert expected_tables == set(fresh_db.table_names())
    assert dogs.count == 1
    assert humans.count == 2
    assert fresh_db.table("dogs_humans").count == 2


def test_m2m_lookup(fresh_db):
    people = fresh_db.table("people", pk="id")
    people.insert({"name": "Wahyu"}).m2m("tags", lookup={"tag": "Coworker"})
    people_tags = fresh_db.table("people_tags")
    tags = fresh_db.table("tags")
    assert people_tags.exists()
    assert tags.exists()
    assert [
        ForeignKey(
            table="people_tags",
            column="people_id",
            other_table="people",
            other_column="id",
        ),
        ForeignKey(
            table="people_tags", column="tags_id", other_table="tags", other_column="id"
        ),
    ] == people_tags.foreign_keys
    assert [{"people_id": 1, "tags_id": 1}] == list(people_tags.rows)
    assert [{"id": 1, "name": "Wahyu"}] == list(people.rows)
    assert [{"id": 1, "tag": "Coworker"}] == list(tags.rows)


def test_m2m_requires_either_records_or_lookup(fresh_db):
    people = fresh_db.table("people", pk="id").insert({"name": "Wahyu"})
    with pytest.raises(ValueError):
        people.m2m("tags")
    with pytest.raises(ValueError):
        people.m2m("tags", {"tag": "hello"}, lookup={"foo": "bar"})


def test_m2m_explicit_table_name_argument(fresh_db):
    people = fresh_db.table("people", pk="id")
    people.insert({"name": "Wahyu"}).m2m(
        "tags", lookup={"tag": "Coworker"}, m2m_table="tagged"
    )
    assert fresh_db.table("tags").exists
    assert fresh_db.table("tagged").exists
    assert not fresh_db.table("people_tags").exists()


def test_m2m_table_candidates(fresh_db):
    fresh_db.create_table("one", {"id": int, "name": str}, pk="id")
    fresh_db.create_table("two", {"id": int, "name": str}, pk="id")
    fresh_db.create_table("three", {"id": int, "name": str}, pk="id")
    # No candidates at first
    assert [] == fresh_db.m2m_table_candidates("one", "two")
    # Create a candidate
    fresh_db.create_table(
        "one_m2m_two", {"one_id": int, "two_id": int}, foreign_keys=["one_id", "two_id"]
    )
    assert ["one_m2m_two"] == fresh_db.m2m_table_candidates("one", "two")
    # Add another table and there should be two candidates
    fresh_db.create_table(
        "one_m2m_two_and_three",
        {"one_id": int, "two_id": int, "three_id": int},
        foreign_keys=["one_id", "two_id", "three_id"],
    )
    assert {"one_m2m_two", "one_m2m_two_and_three"} == set(
        fresh_db.m2m_table_candidates("one", "two")
    )


def test_uses_existing_m2m_table_if_exists(fresh_db):
    # Code should look for an existing table with fks to both tables
    # and use that if it exists.
    people = fresh_db.create_table("people", {"id": int, "name": str}, pk="id")
    fresh_db.table("tags").lookup({"tag": "Coworker"})
    fresh_db.create_table(
        "tagged",
        {"people_id": int, "tags_id": int},
        foreign_keys=["people_id", "tags_id"],
    )
    people.insert({"name": "Wahyu"}).m2m("tags", lookup={"tag": "Coworker"})
    assert fresh_db.table("tags").exists()
    assert fresh_db.table("tagged").exists()
    assert not fresh_db.table("people_tags").exists()
    assert not fresh_db.table("tags_people").exists()
    assert [{"people_id": 1, "tags_id": 1}] == list(fresh_db.table("tagged").rows)


def test_requires_explicit_m2m_table_if_multiple_options(fresh_db):
    # If the code scans for m2m tables and finds more than one candidate
    # it should require that the m2m_table=x argument is used
    people = fresh_db.create_table("people", {"id": int, "name": str}, pk="id")
    fresh_db.table("tags").lookup({"tag": "Coworker"})
    fresh_db.create_table(
        "tagged",
        {"people_id": int, "tags_id": int},
        foreign_keys=["people_id", "tags_id"],
    )
    fresh_db.create_table(
        "tagged2",
        {"people_id": int, "tags_id": int},
        foreign_keys=["people_id", "tags_id"],
    )
    with pytest.raises(NoObviousTable):
        people.insert({"name": "Wahyu"}).m2m("tags", lookup={"tag": "Coworker"})

```

### `tests/test_migrations.py`

```py
import pytest

import sqlite_utils
from sqlite_utils import Migrations


@pytest.fixture
def migrations():
    migrations = Migrations("test")

    @migrations()
    def m001(db):
        db.table("dogs").insert({"name": "Cleo"})

    @migrations()
    def m002(db):
        db.table("cats").create({"name": str})
        db.execute("insert into dogs (name) values ('Pancakes')")

    return migrations


@pytest.fixture
def migrations_not_ordered_alphabetically():
    # Names order alphabetically in the wrong direction but this
    # should still be applied correctly.
    migrations = Migrations("test")

    @migrations()
    def m002(db):
        db.table("dogs").insert({"name": "Cleo"})

    @migrations()
    def m001(db):
        db.table("cats").create({"name": str})
        db.execute("insert into dogs (name) values ('Pancakes')")

    return migrations


@pytest.fixture
def migrations2():
    migrations = Migrations("test2")

    @migrations()
    def m001(db):
        db.table("dogs2").insert({"name": "Cleo"})

    return migrations


def test_basic(migrations):
    db = sqlite_utils.Database(memory=True)
    assert db.table_names() == []
    migrations.apply(db)
    assert set(db.table_names()) == {"_sqlite_migrations", "dogs", "cats"}


def test_stop_before(migrations):
    db = sqlite_utils.Database(memory=True)
    assert db.table_names() == []
    migrations.apply(db, stop_before="m002")
    assert set(db.table_names()) == {"_sqlite_migrations", "dogs"}
    migrations.apply(db)
    assert set(db.table_names()) == {"_sqlite_migrations", "dogs", "cats"}


def test_two_migration_sets(migrations, migrations2):
    db = sqlite_utils.Database(memory=True)
    assert db.table_names() == []
    migrations.apply(db)
    migrations2.apply(db)
    assert set(db.table_names()) == {"_sqlite_migrations", "dogs", "cats", "dogs2"}


def test_order_does_not_matter(migrations, migrations_not_ordered_alphabetically):
    db1 = sqlite_utils.Database(memory=True)
    db2 = sqlite_utils.Database(memory=True)
    migrations.apply(db1)
    migrations_not_ordered_alphabetically.apply(db2)
    assert db1.schema == db2.schema


def test_applied_at_is_a_string(migrations):
    db = sqlite_utils.Database(memory=True)
    migrations.apply(db)
    applied = migrations.applied(db)
    assert len(applied) == 2
    for migration in applied:
        # applied_at is the TEXT timestamp straight from the
        # _sqlite_migrations table, e.g. "2026-07-04 12:00:00.000000+00:00"
        assert isinstance(migration.applied_at, str)
        assert migration.applied_at.endswith("+00:00")


def test_failing_migration_rolls_back(migrations):
    @migrations()
    def m003(db):
        db.table("birds").create({"name": str})
        db.execute("insert into dogs (name) values ('Dozer')")
        raise ValueError("boom")

    db = sqlite_utils.Database(memory=True)
    with pytest.raises(ValueError):
        migrations.apply(db)
    # m001 and m002 committed before the failure and stay applied
    assert set(db.table_names()) == {"_sqlite_migrations", "dogs", "cats"}
    assert [r["name"] for r in db.table("dogs").rows] == ["Cleo", "Pancakes"]
    assert [m.name for m in migrations.applied(db)] == ["m001", "m002"]
    # Everything m003 did was rolled back and it is still pending
    assert [m.name for m in migrations.pending(db)] == ["m003"]


def test_rerun_after_failure_applies_each_migration_once():
    state = {"fail": True}
    migrations = Migrations("test")

    @migrations()
    def m001(db):
        db.table("dogs").insert({"name": "Cleo"})

    @migrations()
    def m002(db):
        db.table("dogs").insert({"name": "Pancakes"})
        if state["fail"]:
            raise ValueError("boom")

    db = sqlite_utils.Database(memory=True)
    with pytest.raises(ValueError):
        migrations.apply(db)
    state["fail"] = False
    migrations.apply(db)
    # m001 must not have been re-applied, m002 applied exactly once
    assert [r["name"] for r in db.table("dogs").rows] == ["Cleo", "Pancakes"]
    assert [m.name for m in migrations.applied(db)] == ["m001", "m002"]


def test_non_transactional_migration_allows_vacuum(tmpdir):
    path = str(tmpdir / "test.db")
    db = sqlite_utils.Database(path)
    migrations = Migrations("test")

    @migrations()
    def m001(db):
        db.table("dogs").insert({"name": "Cleo"})

    @migrations(transactional=False)
    def m002(db):
        db.execute("VACUUM")

    migrations.apply(db)
    assert [m.name for m in migrations.applied(db)] == ["m001", "m002"]
    db.close()


def test_apply_composes_inside_outer_transaction(migrations):
    db = sqlite_utils.Database(memory=True)
    with pytest.raises(ZeroDivisionError), db.atomic():
        migrations.apply(db)
        raise ZeroDivisionError
    # The outer transaction rolled back, taking the migrations with it
    assert db.table_names() == []


@pytest.mark.parametrize(
    "create_table,pk",
    (
        (
            {
                "migration_set": str,
                "name": str,
                "applied_at": str,
            },
            "name",
        ),
        (
            {
                "migration_set": str,
                "name": str,
                "applied_at": str,
            },
            ("migration_set", "name"),
        ),
    ),
)
def test_upgrades_sqlite_migrations(migrations, create_table, pk):
    db = sqlite_utils.Database(memory=True)
    db.table("_sqlite_migrations").create(create_table, pk=pk)
    assert db.table_names() == ["_sqlite_migrations"]
    assert db.table("_sqlite_migrations").pks == (
        [pk] if isinstance(pk, str) else list(pk)
    )
    migrations.apply(db)
    assert db.table("_sqlite_migrations").pks == ["id"]


def test_pending_and_applied_are_read_only(migrations):
    db = sqlite_utils.Database(memory=True)
    assert [m.name for m in migrations.pending(db)] == ["m001", "m002"]
    assert migrations.applied(db) == []
    # Neither call should have created the tracking table
    assert db.table_names() == []


def test_duplicate_migration_name_errors():
    migrations = Migrations("test")

    @migrations()
    def m001(db):
        pass

    with pytest.raises(ValueError) as ex:

        @migrations(name="m001")
        def m001_again(db):
            pass

    assert "m001" in str(ex.value)


def test_stop_before_applied_migration_errors(migrations):
    # Stopping before a migration that has already been applied is
    # impossible to honor - previously the stop name was only checked
    # against pending migrations, so everything after it was applied
    db = sqlite_utils.Database(memory=True)
    migrations.apply(db, stop_before="m002")  # applies m001 only
    with pytest.raises(ValueError) as ex:
        migrations.apply(db, stop_before="m001")
    assert "m001" in str(ex.value)
    assert "already been applied" in str(ex.value)
    # Nothing else was applied
    assert not db.table("cats").exists()


def test_stop_before_applied_migration_errors_before_any_apply(migrations):
    # The error fires before any pending migration runs, even those that
    # come before the already-applied stop target in registration order
    db = sqlite_utils.Database(memory=True)
    only_second = Migrations("test")

    @only_second()
    def m002(db):
        db.table("cats").create({"name": str})

    only_second.apply(db)  # m002 applied, m001 still pending
    with pytest.raises(ValueError):
        migrations.apply(db, stop_before="m002")
    assert not db.table("dogs").exists()

```

### `tests/test_mutator_transactions.py`

```py
import pytest

from sqlite_utils import Database
from sqlite_utils.utils import sqlite3

BASELINE_ROWS = [(1, "one"), (2, "two")]


def insert(table):
    table.insert({"id": 3, "value": "three"}, pk="id")


def insert_all(table):
    table.insert_all(
        [
            {"id": 3, "value": "three"},
            {"id": 4, "value": "four"},
        ],
        pk="id",
        batch_size=1,
    )


def upsert(table):
    table.upsert({"id": 2, "value": "TWO"}, pk="id")


def upsert_all(table):
    table.upsert_all(
        [
            {"id": 2, "value": "TWO"},
            {"id": 3, "value": "three"},
        ],
        pk="id",
        batch_size=1,
    )


def update(table):
    table.update(2, {"value": "TWO"})


def delete(table):
    table.delete(2)


def delete_where(table):
    table.delete_where("id > ?", [1])


MUTATOR_CASES = (
    pytest.param(
        insert,
        [(1, "one"), (2, "two"), (3, "three")],
        id="insert",
    ),
    pytest.param(
        insert_all,
        [(1, "one"), (2, "two"), (3, "three"), (4, "four")],
        id="insert_all",
    ),
    pytest.param(
        upsert,
        [(1, "one"), (2, "TWO")],
        id="upsert",
    ),
    pytest.param(
        upsert_all,
        [(1, "one"), (2, "TWO"), (3, "three")],
        id="upsert_all",
    ),
    pytest.param(
        update,
        [(1, "one"), (2, "TWO")],
        id="update",
    ),
    pytest.param(delete, [(1, "one")], id="delete"),
    pytest.param(delete_where, [(1, "one")], id="delete_where"),
)


class RollbackTest(Exception):
    pass


def seed_database(path):
    conn = sqlite3.connect(str(path))
    try:
        conn.execute("create table items (id integer primary key, value text)")
        conn.executemany("insert into items values (?, ?)", BASELINE_ROWS)
        conn.commit()
    finally:
        conn.close()
    return Database(path)


def current_rows(db):
    return db.conn.execute("select id, value from items order by id").fetchall()


def persisted_rows(path):
    conn = sqlite3.connect(str(path))
    try:
        return conn.execute("select id, value from items order by id").fetchall()
    finally:
        conn.close()


@pytest.mark.parametrize("mutate,expected_rows", MUTATOR_CASES)
def test_mutator_commits_by_default(tmp_path, mutate, expected_rows):
    path = tmp_path / "default.db"
    db = seed_database(path)

    assert not db.conn.in_transaction
    mutate(db.table("items"))
    assert current_rows(db) == expected_rows
    assert not db.conn.in_transaction

    db.close()
    assert persisted_rows(path) == expected_rows


@pytest.mark.parametrize("mutate,expected_rows", MUTATOR_CASES)
def test_mutator_commits_with_outer_atomic(tmp_path, mutate, expected_rows):
    path = tmp_path / "atomic.db"
    db = seed_database(path)

    with db.atomic():
        assert db.conn.in_transaction
        mutate(db.table("items"))
        assert current_rows(db) == expected_rows
        assert db.conn.in_transaction

    assert current_rows(db) == expected_rows
    assert not db.conn.in_transaction
    db.close()
    assert persisted_rows(path) == expected_rows


@pytest.mark.parametrize("mutate,expected_rows", MUTATOR_CASES)
def test_mutator_rolls_back_outer_atomic(tmp_path, mutate, expected_rows):
    path = tmp_path / "rollback.db"
    db = seed_database(path)

    with pytest.raises(RollbackTest), db.atomic():
        mutate(db.table("items"))
        assert current_rows(db) == expected_rows
        assert db.conn.in_transaction
        raise RollbackTest

    assert current_rows(db) == BASELINE_ROWS
    assert not db.conn.in_transaction
    db.close()
    assert persisted_rows(path) == BASELINE_ROWS

```

### `tests/test_plugins.py`

```py
import importlib
import sqlite3
import sys

import click
import pytest
from click.testing import CliRunner

from sqlite_utils import Database, cli, hookimpl, plugins


def _supports_pragma_function_list():
    db = Database(memory=True)
    try:
        db.execute("select * from pragma_function_list()")
        return True
    except sqlite3.DatabaseError:
        return False
    finally:
        db.close()


def test_get_plugins_loads_setuptools_entrypoints_once(monkeypatch):
    calls = []
    monkeypatch.delattr(sys, "_called_from_test", raising=False)
    monkeypatch.setattr(plugins, "_plugins_loaded", False)
    monkeypatch.setattr(
        plugins.pm,
        "load_setuptools_entrypoints",
        lambda group: calls.append(group) or 0,
    )

    plugins.get_plugins()
    plugins.get_plugins()

    assert calls == ["sqlite_utils"]


def test_get_plugins_does_not_load_setuptools_entrypoints_in_tests(monkeypatch):
    calls = []
    monkeypatch.setattr(sys, "_called_from_test", True, raising=False)
    monkeypatch.setattr(plugins, "_plugins_loaded", False)
    monkeypatch.setattr(
        plugins.pm,
        "load_setuptools_entrypoints",
        lambda group: calls.append(group) or 0,
    )

    assert plugins.get_plugins() == []
    assert calls == []


def test_register_commands():
    importlib.reload(cli)
    assert plugins.get_plugins() == []

    class HelloWorldPlugin:
        __name__ = "HelloWorldPlugin"

        @hookimpl
        def register_commands(self, cli):
            @cli.command(name="hello-world")
            def hello_world():
                "Print hello world"
                click.echo("Hello world!")

    try:
        plugins.pm.register(HelloWorldPlugin(), name="HelloWorldPlugin")
        importlib.reload(cli)

        assert plugins.get_plugins() == [
            {"name": "HelloWorldPlugin", "hooks": ["register_commands"]}
        ]

        runner = CliRunner()
        result = runner.invoke(cli.cli, ["hello-world"])
        assert result.exit_code == 0
        assert result.output == "Hello world!\n"

    finally:
        plugins.pm.unregister(name="HelloWorldPlugin")
        importlib.reload(cli)
        assert plugins.get_plugins() == []


@pytest.mark.skipif(
    not _supports_pragma_function_list(),
    reason="Needs SQLite version that supports pragma_function_list()",
)
def test_prepare_connection():
    importlib.reload(cli)
    assert plugins.get_plugins() == []

    class HelloFunctionPlugin:
        __name__ = "HelloFunctionPlugin"

        @hookimpl
        def prepare_connection(self, conn):
            conn.create_function("hello", 1, lambda name: f"Hello, {name}!")

    db = Database(memory=True)

    def _functions(db):
        return [
            row[0]
            for row in db.execute(
                "select distinct name from pragma_function_list() order by 1"
            ).fetchall()
        ]

    assert "hello" not in _functions(db)

    try:
        plugins.pm.register(HelloFunctionPlugin(), name="HelloFunctionPlugin")

        assert plugins.get_plugins() == [
            {"name": "HelloFunctionPlugin", "hooks": ["prepare_connection"]}
        ]

        db = Database(memory=True)
        assert "hello" in _functions(db)
        result = db.execute('select hello("world")').fetchone()[0]
        assert result == "Hello, world!"

        # Test execute_plugins=False
        db2 = Database(memory=True, execute_plugins=False)
        assert "hello" not in _functions(db2)

    finally:
        plugins.pm.unregister(name="HelloFunctionPlugin")
        assert plugins.get_plugins() == []

```

### `tests/test_query.py`

```py
import types

import pytest

from sqlite_utils.utils import sqlite3


def test_query(fresh_db):
    fresh_db.table("dogs").insert_all([{"name": "Cleo"}, {"name": "Pancakes"}])
    results = fresh_db.query("select * from dogs order by name desc")
    assert isinstance(results, types.GeneratorType)
    assert list(results) == [{"name": "Pancakes"}, {"name": "Cleo"}]


def test_query_executes_eagerly(fresh_db):
    # The SQL runs when query() is called, not when the result is iterated,
    # so errors are raised at the call site
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.query("select * from missing_table")


def test_query_rejects_statements_that_return_no_rows(fresh_db):
    fresh_db.table("dogs").insert({"name": "Cleo"})
    with pytest.raises(ValueError) as ex:
        fresh_db.query("update dogs set name = 'Cleopaws'")
    assert "execute()" in str(ex.value)
    # The rejected update was rolled back, and no transaction is left open
    assert not fresh_db.conn.in_transaction
    assert [row["name"] for row in fresh_db.table("dogs").rows] == ["Cleo"]


def test_query_rejected_ddl_is_rolled_back(fresh_db):
    with pytest.raises(ValueError):
        fresh_db.query("create table dogs (id integer primary key)")
    assert not fresh_db.conn.in_transaction
    assert fresh_db.table_names() == []


def test_query_rejected_write_inside_transaction_is_rolled_back(fresh_db):
    fresh_db.table("dogs").insert({"name": "Cleo"})
    fresh_db.begin()
    fresh_db.execute("insert into dogs (name) values ('Pancakes')")
    with pytest.raises(ValueError):
        fresh_db.query("update dogs set name = 'Cleopaws'")
    # The transaction is still open and the earlier insert is intact
    assert fresh_db.conn.in_transaction
    fresh_db.commit()
    assert [row["name"] for row in fresh_db.table("dogs").rows] == ["Cleo", "Pancakes"]


@pytest.mark.parametrize(
    "sql",
    [
        "begin",
        "commit",
        "rollback",
        "vacuum",
        "detach database foo",
        "/* comment */ commit",
        "-- comment\nbegin",
        "/* multi\nline */ -- and another\n  vacuum",
        "\t /* a */ /* b */ savepoint s1",
        "; commit",
        ";;\n ; rollback",
        "; /* comment */ vacuum",
        "\ufeffbegin",
    ],
)
def test_query_rejects_transaction_control_and_vacuum(fresh_db, sql):
    with pytest.raises(ValueError) as ex:
        fresh_db.query(sql)
    assert "execute()" in str(ex.value)
    assert not fresh_db.conn.in_transaction


def test_query_comment_prefixed_commit_does_not_commit_transaction(fresh_db):
    # A COMMIT hidden behind a leading comment must not slip past the
    # keyword check - previously it committed the caller's open
    # transaction before the ValueError was raised
    fresh_db.table("dogs").insert({"name": "Cleo"})
    fresh_db.begin()
    fresh_db.execute("insert into dogs (name) values ('Pancakes')")
    with pytest.raises(ValueError):
        fresh_db.query("/* comment */ COMMIT")
    # The explicit transaction is still open and can still be rolled back
    assert fresh_db.conn.in_transaction
    fresh_db.rollback()
    assert [row["name"] for row in fresh_db.table("dogs").rows] == ["Cleo"]


@pytest.mark.parametrize("sql", ["; COMMIT", "\ufeffCOMMIT"])
def test_query_prefixed_commit_does_not_commit_transaction(fresh_db, sql):
    # sqlite3 tolerates empty statements and a UTF-8 BOM before the first
    # real token, so the keyword scanner must skip them too - previously
    # '; COMMIT' slipped past the check and committed the caller's open
    # transaction before raising OperationalError
    fresh_db.table("dogs").insert({"name": "Cleo"})
    fresh_db.begin()
    fresh_db.execute("insert into dogs (name) values ('Pancakes')")
    with pytest.raises(ValueError):
        fresh_db.query(sql)
    # The explicit transaction is still open and can still be rolled back
    assert fresh_db.conn.in_transaction
    fresh_db.rollback()
    assert [row["name"] for row in fresh_db.table("dogs").rows] == ["Cleo"]


def test_query_error_leaves_no_transaction_open(fresh_db):
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.query("select * from missing_table")
    assert not fresh_db.conn.in_transaction


def test_query_pragma(tmpdir):
    from sqlite_utils import Database

    db = Database(str(tmpdir / "test.db"))
    # A row-returning PRAGMA works, including one that cannot run in a transaction
    assert list(db.query("pragma journal_mode = wal")) == [{"journal_mode": "wal"}]
    # A PRAGMA that returns no rows raises ValueError
    with pytest.raises(ValueError):
        db.query("pragma user_version = 5")
    db.close()


def test_query_rejected_pragma_still_takes_effect(fresh_db):
    # Documented limitation: PRAGMAs run outside the savepoint guard,
    # because some of them refuse to run inside a transaction - so a
    # row-less PRAGMA takes effect even though it raises ValueError.
    # If this test starts failing because the pragma was rolled back,
    # the limitation has been fixed - update the docs in python-api.rst
    # and the query() docstring to remove the carve-out
    with pytest.raises(ValueError):
        fresh_db.query("pragma user_version = 5")
    assert fresh_db.execute("pragma user_version").fetchone()[0] == 5


def test_query_comment_prefixed_pragma(tmpdir):
    from sqlite_utils import Database

    db = Database(str(tmpdir / "test.db"))
    # A leading comment must not stop a PRAGMA being recognized as one -
    # previously it was executed inside the savepoint guard, where
    # journal mode changes are refused
    assert list(db.query("-- set WAL mode\npragma journal_mode = wal")) == [
        {"journal_mode": "wal"}
    ]
    db.close()


def test_query_comment_prefixed_pragma_inside_transaction(fresh_db):
    fresh_db.begin()
    assert list(fresh_db.query("-- check version\npragma user_version")) == [
        {"user_version": 0}
    ]
    assert fresh_db.conn.in_transaction
    fresh_db.rollback()


@pytest.mark.parametrize(
    "sql,expected",
    [
        ("select 1", "SELECT"),
        ("  \t\n select 1", "SELECT"),
        ("-- comment\nbegin", "BEGIN"),
        ("/* one */ /* two */ pragma user_version", "PRAGMA"),
        ("/* multi\nline */vacuum", "VACUUM"),
        ("insert into t values (1)", "INSERT"),
        ("-- only a comment", ""),
        ("/* unterminated", ""),
        ("", ""),
        ("   ", ""),
        ("123", ""),
        ("; commit", "COMMIT"),
        (";;\n ; rollback", "ROLLBACK"),
        ("; -- comment\n begin", "BEGIN"),
        ("\ufeffcommit", "COMMIT"),
        ("\ufeff ; select 1", "SELECT"),
        (";", ""),
    ],
)
def test_first_keyword(sql, expected):
    from sqlite_utils.db import _first_keyword

    assert _first_keyword(sql) == expected


@pytest.mark.skipif(
    sqlite3.sqlite_version_info < (3, 35, 0),
    reason="RETURNING requires SQLite 3.35.0 or higher",
)
def test_query_insert_returning(fresh_db):
    fresh_db.table("dogs").insert({"name": "Cleo"})
    rows = list(
        fresh_db.query("insert into dogs (name) values ('Pancakes') returning name")
    )
    assert rows == [{"name": "Pancakes"}]
    assert fresh_db.table("dogs").count == 2


@pytest.mark.skipif(
    sqlite3.sqlite_version_info < (3, 35, 0),
    reason="RETURNING requires SQLite 3.35.0 or higher",
)
def test_query_insert_returning_commits_without_iteration(tmpdir):
    from sqlite_utils import Database

    path = str(tmpdir / "test.db")
    db = Database(path)
    db.table("dogs").insert({"name": "Cleo"})
    # Never iterate over the results
    db.query("insert into dogs (name) values ('Pancakes') returning name")
    assert not db.conn.in_transaction
    # A completely separate connection sees the new row straight away
    other = sqlite3.connect(path)
    assert other.execute("select count(*) from dogs").fetchone()[0] == 2
    other.close()
    db.close()


@pytest.mark.skipif(
    sqlite3.sqlite_version_info < (3, 35, 0),
    reason="RETURNING requires SQLite 3.35.0 or higher",
)
def test_query_insert_returning_partial_iteration_still_commits(tmpdir):
    from sqlite_utils import Database

    path = str(tmpdir / "test.db")
    db = Database(path)
    db.table("dogs").insert({"name": "Cleo"})
    row = next(
        db.query(
            "insert into dogs (name) values ('Pancakes'), ('Marnie') returning name"
        )
    )
    assert row == {"name": "Pancakes"}
    assert not db.conn.in_transaction
    other = sqlite3.connect(path)
    assert other.execute("select count(*) from dogs").fetchone()[0] == 3
    other.close()
    db.close()


@pytest.mark.skipif(
    sqlite3.sqlite_version_info < (3, 35, 0),
    reason="RETURNING requires SQLite 3.35.0 or higher",
)
def test_query_insert_returning_respects_explicit_transaction(fresh_db):
    fresh_db.table("dogs").insert({"name": "Cleo"})
    fresh_db.begin()
    rows = list(
        fresh_db.query("insert into dogs (name) values ('Pancakes') returning name")
    )
    assert rows == [{"name": "Pancakes"}]
    # Still inside the explicit transaction - not committed
    assert fresh_db.conn.in_transaction
    fresh_db.rollback()
    assert [row["name"] for row in fresh_db.table("dogs").rows] == ["Cleo"]


def test_query_duplicate_column_names_are_deduped(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/624
    fresh_db.table("one").insert({"id": 1, "value": "left"})
    fresh_db.table("two").insert({"id": 2, "value": "right"})
    rows = list(
        fresh_db.query("select one.id, two.id, one.value, two.value from one, two")
    )
    assert rows == [{"id": 1, "id_2": 2, "value": "left", "value_2": "right"}]


def test_query_deduped_column_avoids_existing_names(fresh_db):
    # The renamed duplicate must not overwrite a real column called id_2
    rows = list(fresh_db.query("select 1 as id, 2 as id, 3 as id_2"))
    assert rows == [{"id": 1, "id_3": 2, "id_2": 3}]


def test_execute_returning_dicts(fresh_db):
    # Like db.query() but returns a list, included for backwards compatibility
    # see https://github.com/simonw/sqlite-utils/issues/290
    fresh_db.table("test").insert({"id": 1, "bar": 2}, pk="id")
    assert fresh_db.execute_returning_dicts("select * from test") == [
        {"id": 1, "bar": 2}
    ]


@pytest.mark.skipif(
    sqlite3.sqlite_version_info < (3, 35, 0),
    reason="RETURNING requires SQLite 3.35.0 or higher",
)
def test_query_preserves_error_from_transaction_destroying_trigger(fresh_db):
    # RAISE(ROLLBACK) destroys the savepoint guard - the original
    # IntegrityError must propagate, not "no such savepoint"
    fresh_db.execute("create table t (id integer primary key, v text)")
    fresh_db.execute("""
        create trigger no_bad before insert on t
        when new.v = 'bad'
        begin
            select raise(rollback, 'trigger says no');
        end
    """)
    with pytest.raises(sqlite3.IntegrityError, match="trigger says no"):
        fresh_db.query("insert into t (id, v) values (1, 'bad') returning id")
    assert not fresh_db.conn.in_transaction
    assert fresh_db.execute("select count(*) from t").fetchone()[0] == 0

```

### `tests/test_recipes.py`

```py
import json

import pytest

from sqlite_utils import recipes
from sqlite_utils.utils import sqlite3


@pytest.fixture
def dates_db(fresh_db):
    fresh_db.table("example").insert_all(
        [
            {"id": 1, "dt": "5th October 2019 12:04"},
            {"id": 2, "dt": "6th October 2019 00:05:06"},
            {"id": 3, "dt": ""},
            {"id": 4, "dt": None},
        ],
        pk="id",
    )
    return fresh_db


def test_parsedate(dates_db):
    dates_db.table("example").convert("dt", recipes.parsedate)
    assert list(dates_db.table("example").rows) == [
        {"id": 1, "dt": "2019-10-05"},
        {"id": 2, "dt": "2019-10-06"},
        {"id": 3, "dt": ""},
        {"id": 4, "dt": None},
    ]


def test_parsedatetime(dates_db):
    dates_db.table("example").convert("dt", recipes.parsedatetime)
    assert list(dates_db.table("example").rows) == [
        {"id": 1, "dt": "2019-10-05T12:04:00"},
        {"id": 2, "dt": "2019-10-06T00:05:06"},
        {"id": 3, "dt": ""},
        {"id": 4, "dt": None},
    ]


@pytest.mark.parametrize(
    "recipe,kwargs,expected",
    (
        ("parsedate", {}, "2005-03-04"),
        ("parsedate", {"dayfirst": True}, "2005-04-03"),
        ("parsedatetime", {}, "2005-03-04T00:00:00"),
        ("parsedatetime", {"dayfirst": True}, "2005-04-03T00:00:00"),
    ),
)
def test_dayfirst_yearfirst(fresh_db, recipe, kwargs, expected):
    fresh_db.table("example").insert_all(
        [
            {"id": 1, "dt": "03/04/05"},
        ],
        pk="id",
    )
    fresh_db.table("example").convert(
        "dt", lambda value: getattr(recipes, recipe)(value, **kwargs)
    )
    assert list(fresh_db.table("example").rows) == [
        {"id": 1, "dt": expected},
    ]


@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
@pytest.mark.parametrize("fn", ("parsedate", "parsedatetime"))
def test_dateparse_errors_raises(fresh_db, fn):
    """Test that invalid dates raise errors when errors=None"""
    fresh_db.table("example").insert_all(
        [
            {"id": 1, "dt": "invalid"},
        ],
        pk="id",
    )
    # Exception in SQLite callback surfaces as OperationalError
    with pytest.raises(sqlite3.OperationalError):
        fresh_db.table("example").convert(
            "dt", lambda value: getattr(recipes, fn)(value)
        )


@pytest.mark.parametrize("fn", ("parsedate", "parsedatetime"))
@pytest.mark.parametrize("errors", (recipes.SET_NULL, recipes.IGNORE))
def test_dateparse_errors_handled(fresh_db, fn, errors):
    """Test error handling modes for invalid dates"""
    fresh_db.table("example").insert_all(
        [
            {"id": 1, "dt": "invalid"},
        ],
        pk="id",
    )
    fresh_db.table("example").convert(
        "dt", lambda value: getattr(recipes, fn)(value, errors=errors)
    )
    rows = list(fresh_db.table("example").rows)
    expected = [{"id": 1, "dt": None if errors is recipes.SET_NULL else "invalid"}]
    assert rows == expected


@pytest.mark.parametrize("delimiter", [None, ";", "-"])
def test_jsonsplit(fresh_db, delimiter):
    fresh_db.table("example").insert_all(
        [
            {"id": 1, "tags": (delimiter or ",").join(["foo", "bar"])},
            {"id": 2, "tags": (delimiter or ",").join(["bar", "baz"])},
        ],
        pk="id",
    )
    if delimiter is not None:

        def fn(value):
            return recipes.jsonsplit(value, delimiter=delimiter)

    else:
        fn = recipes.jsonsplit

    fresh_db.table("example").convert("tags", fn)
    assert list(fresh_db.table("example").rows) == [
        {"id": 1, "tags": '["foo", "bar"]'},
        {"id": 2, "tags": '["bar", "baz"]'},
    ]


@pytest.mark.parametrize(
    "type,expected",
    (
        (None, ["1", "2", "3"]),
        (float, [1.0, 2.0, 3.0]),
        (int, [1, 2, 3]),
    ),
)
def test_jsonsplit_type(fresh_db, type, expected):
    fresh_db.table("example").insert_all(
        [
            {"id": 1, "records": "1,2,3"},
        ],
        pk="id",
    )
    if type is not None:

        def fn(value):
            return recipes.jsonsplit(value, type=type)

    else:
        fn = recipes.jsonsplit

    fresh_db.table("example").convert("records", fn)
    assert json.loads(fresh_db.table("example").get(1)["records"]) == expected

```

### `tests/test_recreate.py`

```py
import pathlib
import sqlite3

import pytest

from sqlite_utils import Database


def test_recreate_ignored_for_in_memory():
    # None of these should raise an exception:
    Database(memory=True, recreate=False)
    Database(memory=True, recreate=True)
    Database(":memory:", recreate=False)
    Database(":memory:", recreate=True)


def test_recreate_not_allowed_for_connection():
    conn = sqlite3.connect(":memory:")
    try:
        with pytest.raises(ValueError):
            Database(conn, recreate=True)
    finally:
        conn.close()


@pytest.mark.parametrize(
    "use_path,create_file_first",
    [(True, True), (True, False), (False, True), (False, False)],
)
def test_recreate(tmp_path, use_path, create_file_first):
    filepath = str(tmp_path / "data.db")
    if use_path:
        filepath = pathlib.Path(filepath)
    if create_file_first:
        db = Database(filepath)
        db.table("t1").insert({"foo": "bar"})
        assert ["t1"] == db.table_names()
        db.close()
    Database(filepath, recreate=True).table("t2").insert({"foo": "bar"})
    assert ["t2"] == Database(filepath).table_names()

```

### `tests/test_register_function.py`

```py
# flake8: noqa
import pytest
import sys
from unittest.mock import MagicMock, call
from sqlite_utils.utils import sqlite3


def test_register_function(fresh_db):
    @fresh_db.register_function
    def reverse_string(s):
        return "".join(reversed(list(s)))

    result = fresh_db.execute('select reverse_string("hello")').fetchone()[0]
    assert result == "olleh"


def test_register_function_custom_name(fresh_db):
    @fresh_db.register_function(name="revstr")
    def reverse_string(s):
        return "".join(reversed(list(s)))

    result = fresh_db.execute('select revstr("hello")').fetchone()[0]
    assert result == "olleh"


def test_register_function_multiple_arguments(fresh_db):
    @fresh_db.register_function
    def a_times_b_plus_c(a, b, c):
        return a * b + c

    result = fresh_db.execute("select a_times_b_plus_c(2, 3, 4)").fetchone()[0]
    assert result == 10


def test_register_function_deterministic(fresh_db):
    @fresh_db.register_function(deterministic=True)
    def to_lower(s):
        return s.lower()

    result = fresh_db.execute("select to_lower('BOB')").fetchone()[0]
    assert result == "bob"


def test_register_function_deterministic_tries_again_if_exception_raised(fresh_db):
    # Save the original connection so we can close it later
    original_conn = fresh_db.conn
    fresh_db.conn = MagicMock()
    fresh_db.conn.create_function = MagicMock()

    try:

        @fresh_db.register_function(deterministic=True)
        def to_lower_2(s):
            return s.lower()

        fresh_db.conn.create_function.assert_called_with(
            "to_lower_2", 1, to_lower_2, deterministic=True
        )

        first = True

        def side_effect(*args, **kwargs):
            # Raise exception only first time this is called
            nonlocal first
            if first:
                first = False
                raise sqlite3.NotSupportedError()

        # But if sqlite3.NotSupportedError is raised, it tries again
        fresh_db.conn.create_function.reset_mock()
        fresh_db.conn.create_function.side_effect = side_effect

        @fresh_db.register_function(deterministic=True)
        def to_lower_3(s):
            return s.lower()

        # Should have been called once with deterministic=True and once without
        assert fresh_db.conn.create_function.call_args_list == [
            call("to_lower_3", 1, to_lower_3, deterministic=True),
            call("to_lower_3", 1, to_lower_3),
        ]
    finally:
        # Close the original connection that was replaced with the mock
        original_conn.close()


def test_register_function_replace(fresh_db):
    @fresh_db.register_function()
    def one():  # pyright: ignore[reportRedeclaration]
        return "one"

    assert "one" == fresh_db.execute("select one()").fetchone()[0]

    # This will silently fail to replaec the function
    @fresh_db.register_function()
    def one():  # pyright: ignore[reportRedeclaration]
        return "two"

    assert "one" == fresh_db.execute("select one()").fetchone()[0]

    # This will replace it
    @fresh_db.register_function(replace=True)
    def one():  # pyright: ignore[reportRedeclaration]
        return "two"

    assert "two" == fresh_db.execute("select one()").fetchone()[0]

```

### `tests/test_rows_from_file.py`

```py
from io import BytesIO, StringIO

import pytest

from sqlite_utils.utils import Format, RowError, rows_from_file


@pytest.mark.parametrize(
    "input,expected_format",
    (
        (b"id,name\n1,Cleo", Format.CSV),
        (b"id\tname\n1\tCleo", Format.TSV),
        (b'[{"id": "1", "name": "Cleo"}]', Format.JSON),
    ),
)
def test_rows_from_file_detect_format(input, expected_format):
    rows, format = rows_from_file(BytesIO(input))
    assert format == expected_format
    rows_list = list(rows)
    assert rows_list == [{"id": "1", "name": "Cleo"}]


@pytest.mark.parametrize("input", (b"", b" \n\t"))
def test_rows_from_file_empty_input(input):
    rows, format = rows_from_file(BytesIO(input))
    assert format == Format.CSV
    assert list(rows) == []


@pytest.mark.parametrize(
    "ignore_extras,extras_key,expected",
    (
        (True, None, [{"id": "1", "name": "Cleo"}]),
        (False, "_rest", [{"id": "1", "name": "Cleo", "_rest": ["oops"]}]),
        # expected of None means expect an error:
        (False, False, None),
    ),
)
def test_rows_from_file_extra_fields_strategies(ignore_extras, extras_key, expected):
    try:
        rows, _format = rows_from_file(
            BytesIO(b"id,name\r\n1,Cleo,oops"),
            format=Format.CSV,
            ignore_extras=ignore_extras,
            extras_key=extras_key,
        )
        list_rows = list(rows)
    except RowError:
        if expected is None:
            # This is fine,
            return
        else:
            # We did not expect an error
            raise
    assert list_rows == expected


def test_rows_from_file_error_on_string_io():
    with pytest.raises(TypeError) as ex:
        rows_from_file(StringIO("id,name\r\n1,Cleo"))  # type: ignore[arg-type]
    assert ex.value.args == (
        "rows_from_file() requires a file-like object that supports peek(), such as io.BytesIO",
    )

```

### `tests/test_rows.py`

```py
import pytest


def test_rows(existing_db):
    assert [{"text": "one"}, {"text": "two"}, {"text": "three"}] == list(
        existing_db.table("foo").rows
    )


@pytest.mark.parametrize(
    "where,where_args,expected_ids",
    [
        ("name = ?", ["Pancakes"], {2}),
        ("age > ?", [3], {1}),
        ("age > :age", {"age": 3}, {1}),
        ("name is not null", [], {1, 2}),
        ("is_good = ?", [True], {1, 2}),
    ],
)
def test_rows_where(where, where_args, expected_ids, fresh_db):
    table = fresh_db.table("dogs")
    table.insert_all(
        [
            {"id": 1, "name": "Cleo", "age": 4, "is_good": True},
            {"id": 2, "name": "Pancakes", "age": 3, "is_good": True},
        ],
        pk="id",
    )
    assert expected_ids == {
        r["id"] for r in table.rows_where(where, where_args, select="id")
    }


@pytest.mark.parametrize(
    "where,order_by,expected_ids",
    [
        (None, None, [1, 2, 3]),
        (None, "id desc", [3, 2, 1]),
        (None, "age", [3, 2, 1]),
        ("id > 1", "age", [3, 2]),
    ],
)
def test_rows_where_order_by(where, order_by, expected_ids, fresh_db):
    table = fresh_db.table("dogs")
    table.insert_all(
        [
            {"id": 1, "name": "Cleo", "age": 4},
            {"id": 2, "name": "Pancakes", "age": 3},
            {"id": 3, "name": "Bailey", "age": 2},
        ],
        pk="id",
    )
    assert expected_ids == [r["id"] for r in table.rows_where(where, order_by=order_by)]


@pytest.mark.parametrize(
    "offset,limit,expected",
    [
        (None, 3, [1, 2, 3]),
        (0, 3, [1, 2, 3]),
        (3, 3, [4, 5, 6]),
        # offset without limit should return every remaining row
        (97, None, [98, 99, 100]),
        (0, None, list(range(1, 101))),
    ],
)
def test_rows_where_offset_limit(fresh_db, offset, limit, expected):
    table = fresh_db.table("rows")
    table.insert_all([{"id": id} for id in range(1, 101)], pk="id")
    assert table.count == 100
    assert expected == [
        r["id"] for r in table.rows_where(offset=offset, limit=limit, order_by="id")
    ]


def test_pks_and_rows_where_offset_without_limit(fresh_db):
    table = fresh_db.table("rows")
    table.insert_all([{"id": id} for id in range(1, 6)], pk="id")
    assert [pk for pk, _ in table.pks_and_rows_where(offset=3, order_by="id")] == [4, 5]


def test_pks_and_rows_where_rowid(fresh_db):
    table = fresh_db.table("rowid_table")
    table.insert_all({"number": i + 10} for i in range(3))
    pks_and_rows = list(table.pks_and_rows_where())
    assert pks_and_rows == [
        (1, {"rowid": 1, "number": 10}),
        (2, {"rowid": 2, "number": 11}),
        (3, {"rowid": 3, "number": 12}),
    ]


def test_pks_and_rows_where_simple_pk(fresh_db):
    table = fresh_db.table("simple_pk_table")
    table.insert_all(({"id": i + 10} for i in range(3)), pk="id")
    pks_and_rows = list(table.pks_and_rows_where())
    assert pks_and_rows == [
        (10, {"id": 10}),
        (11, {"id": 11}),
        (12, {"id": 12}),
    ]


def test_pks_and_rows_where_compound_pk(fresh_db):
    table = fresh_db.table("compound_pk_table")
    table.insert_all(
        ({"type": "number", "number": i, "plusone": i + 1} for i in range(3)),
        pk=("type", "number"),
    )
    pks_and_rows = list(table.pks_and_rows_where())
    assert pks_and_rows == [
        (("number", 0), {"type": "number", "number": 0, "plusone": 1}),
        (("number", 1), {"type": "number", "number": 1, "plusone": 2}),
        (("number", 2), {"type": "number", "number": 2, "plusone": 3}),
    ]


def test_rows_where_duplicate_select_columns_are_deduped(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/624
    fresh_db.table("t").insert({"id": 1, "name": "Cleo"})
    rows = list(fresh_db.table("t").rows_where(select="id, id, name"))
    assert rows == [{"id": 1, "id_2": 1, "name": "Cleo"}]


def test_pks_and_rows_where_view(fresh_db):
    # pks_and_rows_where() lives on Queryable so views expose it, but
    # SQLite views have no rowid. Modern SQLite (3.36+) raises an
    # OperationalError from the generated SQL; older versions returned
    # NULL for a view's rowid. Either way it must not fail earlier with
    # an AttributeError from View lacking Table-only properties
    from sqlite_utils.utils import sqlite3

    fresh_db.table("dogs").insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.create_view("dog_names", "select name from dogs")
    try:
        result = list(fresh_db.view("dog_names").pks_and_rows_where())
    except sqlite3.OperationalError:
        pass  # SQLite 3.36+: no such column: rowid
    else:
        # Older SQLite returns NULL rowids for views
        assert result == [(None, {"rowid": None, "name": "Cleo"})]


def test_pks_and_rows_where_compound_pk_declaration_order(fresh_db):
    # Compound pks are returned in PRIMARY KEY declaration order
    fresh_db.execute("create table t (b text, a text, primary key (a, b))")
    fresh_db.table("t").insert({"a": "A", "b": "B"})
    pks_and_rows = list(fresh_db.table("t").pks_and_rows_where())
    assert pks_and_rows == [(("A", "B"), {"b": "B", "a": "A"})]

```

### `tests/test_sniff.py`

```py
import pathlib

import pytest
from click.testing import CliRunner

from sqlite_utils import Database, cli

sniff_dir = pathlib.Path(__file__).parent / "sniff"


@pytest.mark.parametrize("filepath", sorted(sniff_dir.glob("example*")))
def test_sniff(tmpdir, filepath):
    db_path = str(tmpdir / "test.db")
    runner = CliRunner()
    result = runner.invoke(
        cli.cli,
        ["insert", db_path, "creatures", str(filepath), "--sniff", "--no-detect-types"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.stdout
    db = Database(db_path)
    assert list(db.table("creatures").rows) == [
        {"id": "1", "species": "dog", "name": "Cleo", "age": "5"},
        {"id": "2", "species": "dog", "name": "Pancakes", "age": "4"},
        {"id": "3", "species": "cat", "name": "Mozie", "age": "8"},
        {"id": "4", "species": "spider", "name": "Daisy, the tarantula", "age": "6"},
    ]

```

### `tests/test_suggest_column_types.py`

```py
from collections import OrderedDict

import pytest

from sqlite_utils.utils import suggest_column_types


@pytest.mark.parametrize(
    "records,types",
    [
        ([{"a": 1}], {"a": int}),
        ([{"a": 1}, {"a": None}], {"a": int}),
        ([{"a": "baz"}], {"a": str}),
        ([{"a": "baz"}, {"a": None}], {"a": str}),
        ([{"a": 1.2}], {"a": float}),
        ([{"a": 1.2}, {"a": None}], {"a": float}),
        ([{"a": [1]}], {"a": str}),
        ([{"a": [1]}, {"a": None}], {"a": str}),
        ([{"a": (1,)}], {"a": str}),
        ([{"a": {"b": 1}}], {"a": str}),
        ([{"a": {"b": 1}}, {"a": None}], {"a": str}),
        ([{"a": OrderedDict({"b": 1})}], {"a": str}),
        ([{"a": 1}, {"a": 1.1}], {"a": float}),
        ([{"a": b"b"}], {"a": bytes}),
        ([{"a": b"b"}, {"a": None}], {"a": bytes}),
        ([{"a": "a", "b": None}], {"a": str, "b": str}),
    ],
)
def test_suggest_column_types(records, types):
    assert types == suggest_column_types(records)

```

### `tests/test_tracer.py`

```py
from sqlite_utils import Database


def test_tracer():
    collected = []
    db = Database(
        memory=True, tracer=lambda sql, params: collected.append((sql, params))
    )
    dogs = db.table("dogs")
    dogs.insert({"name": "Cleopaws"})
    dogs.enable_fts(["name"])
    dogs.search("Cleopaws")
    assert collected == [
        ("PRAGMA recursive_triggers=on;", None),
        ("select name from sqlite_master where type = 'view'", None),
        ("select name from sqlite_master where type = 'table'", None),
        ("select name from sqlite_master where type = 'view'", None),
        ("select name from sqlite_master where type = 'view'", None),
        ("select name from sqlite_master where type = 'table'", None),
        ("select name from sqlite_master where type = 'view'", None),
        ('CREATE TABLE "dogs" (\n   "name" TEXT\n);\n        ', None),
        ("select name from sqlite_master where type = 'view'", None),
        ('INSERT INTO "dogs" ("name") VALUES (?)', ["Cleopaws"]),
        (
            'CREATE VIRTUAL TABLE "dogs_fts" USING FTS5 (\n    "name",\n    content="dogs"\n)',
            None,
        ),
        (
            'INSERT INTO "dogs_fts" (rowid, "name")\n    SELECT rowid, "name" FROM "dogs";',
            None,
        ),
    ]


def test_with_tracer():
    collected = []

    def tracer(sql, params):
        return collected.append((sql, params))

    db = Database(memory=True)

    dogs = db.table("dogs")

    dogs.insert({"name": "Cleopaws"})
    dogs.enable_fts(["name"])

    assert len(collected) == 0

    with db.tracer(tracer):
        list(dogs.search("Cleopaws"))

    assert len(collected) == 4
    assert collected == [
        (
            (
                "SELECT name FROM sqlite_master\n"
                "    WHERE rootpage = 0\n"
                "    AND (\n"
                "        sql LIKE :like\n"
                "        OR sql LIKE :like2\n"
                "        OR (\n"
                "            tbl_name = :table\n"
                "            AND sql LIKE '%VIRTUAL TABLE%USING FTS%'\n"
                "        )\n"
                "    )"
            ),
            {
                "like": "%VIRTUAL TABLE%USING FTS%content=[dogs]%",
                "like2": '%VIRTUAL TABLE%USING FTS%content="dogs"%',
                "table": "dogs",
            },
        ),
        ("select name from sqlite_master where type = 'view'", None),
        ("select sql from sqlite_master where name = ?", ("dogs_fts",)),
        (
            (
                'with "original" as (\n'
                "    select\n"
                "        rowid,\n"
                "        *\n"
                '    from "dogs"\n'
                ")\n"
                "select\n"
                '    "original".*\n'
                "from\n"
                '    "original"\n'
                '    join "dogs_fts" on "original".rowid = "dogs_fts".rowid\n'
                "where\n"
                '    "dogs_fts" match :query\n'
                "order by\n"
                '    "dogs_fts".rank'
            ),
            {"query": "Cleopaws"},
        ),
    ]

    # Outside the with block collected should not be appended to
    dogs.insert({"name": "Cleopaws"})
    assert len(collected) == 4

```

### `tests/test_transform.py`

```py
import sqlite3

import pytest

from sqlite_utils import ANY
from sqlite_utils.db import Check, ForeignKey, TransactionError, TransformError
from sqlite_utils.utils import OperationalError


@pytest.mark.parametrize(
    "params,expected_sql",
    [
        # Identity transform - nothing changes
        (
            {},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" TEXT\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "age")\n   SELECT "rowid", "id", "name", "age" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Change column type
        (
            {"types": {"age": int}},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" INTEGER\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "age")\n   SELECT "rowid", "id", "name", NULLIF("age", \'\') FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Rename a column
        (
            {"rename": {"age": "dog_age"}},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "dog_age" TEXT\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "dog_age")\n   SELECT "rowid", "id", "name", "age" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Drop a column
        (
            {"drop": ["age"]},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name")\n   SELECT "rowid", "id", "name" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Convert type AND rename column
        (
            {"types": {"age": int}, "rename": {"age": "dog_age"}},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "dog_age" INTEGER\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "dog_age")\n   SELECT "rowid", "id", "name", NULLIF("age", \'\') FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Change primary key
        (
            {"pk": "age"},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER,\n   "name" TEXT,\n   "age" TEXT PRIMARY KEY\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "age")\n   SELECT "rowid", "id", "name", "age" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Change primary key to a compound pk
        (
            {"pk": ("age", "name")},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER,\n   "name" TEXT,\n   "age" TEXT,\n   PRIMARY KEY ("age", "name")\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "age")\n   SELECT "rowid", "id", "name", "age" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Remove primary key, creating a rowid table
        (
            {"pk": None},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER,\n   "name" TEXT,\n   "age" TEXT\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "age")\n   SELECT "rowid", "id", "name", "age" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Keeping the table
        (
            {"drop": ["age"], "keep_table": "kept_table"},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name")\n   SELECT "rowid", "id", "name" FROM "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs" RENAME TO "kept_table";',
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
    ],
)
@pytest.mark.parametrize("use_pragma_foreign_keys", [False, True])
def test_transform_sql_table_with_primary_key(
    fresh_db, params, expected_sql, use_pragma_foreign_keys
):
    captured = []

    def tracer(sql, params):
        return captured.append((sql, params))

    dogs = fresh_db.table("dogs")
    if use_pragma_foreign_keys:
        fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    dogs.insert({"id": 1, "name": "Cleo", "age": "5"}, pk="id")
    sql = dogs.transform_sql(**{**params, "tmp_suffix": "suffix"})
    assert sql == expected_sql
    # Check that .transform() runs without exceptions:
    with fresh_db.tracer(tracer):
        dogs.transform(**params)
    # If use_pragma_foreign_keys, check that we did the right thing
    if use_pragma_foreign_keys:
        assert ("PRAGMA foreign_keys=0;", None) in captured
        assert captured[-2] == ("PRAGMA foreign_key_check;", None)
        assert captured[-1] == ("PRAGMA foreign_keys=1;", None)
    else:
        assert ("PRAGMA foreign_keys=0;", None) not in captured
        assert ("PRAGMA foreign_keys=1;", None) not in captured


@pytest.mark.parametrize(
    "params,expected_sql",
    [
        # Identity transform - nothing changes
        (
            {},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER,\n   "name" TEXT,\n   "age" TEXT\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "age")\n   SELECT "rowid", "id", "name", "age" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Change column type
        (
            {"types": {"age": int}},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER,\n   "name" TEXT,\n   "age" INTEGER\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "age")\n   SELECT "rowid", "id", "name", NULLIF("age", \'\') FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Rename a column
        (
            {"rename": {"age": "dog_age"}},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER,\n   "name" TEXT,\n   "dog_age" TEXT\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "dog_age")\n   SELECT "rowid", "id", "name", "age" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
        # Make ID a primary key
        (
            {"pk": "id"},
            [
                'CREATE TABLE "dogs_new_suffix" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" TEXT\n);',
                'INSERT INTO "dogs_new_suffix" ("rowid", "id", "name", "age")\n   SELECT "rowid", "id", "name", "age" FROM "dogs";',
                'DROP TABLE "dogs";',
                "PRAGMA legacy_alter_table=ON;",
                'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";',
                "PRAGMA legacy_alter_table=OFF;",
            ],
        ),
    ],
)
@pytest.mark.parametrize("use_pragma_foreign_keys", [False, True])
def test_transform_sql_table_with_no_primary_key(
    fresh_db, params, expected_sql, use_pragma_foreign_keys
):
    captured = []

    def tracer(sql, params):
        return captured.append((sql, params))

    dogs = fresh_db.table("dogs")
    if use_pragma_foreign_keys:
        fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    dogs.insert({"id": 1, "name": "Cleo", "age": "5"})
    sql = dogs.transform_sql(**{**params, "tmp_suffix": "suffix"})
    assert sql == expected_sql
    # Check that .transform() runs without exceptions:
    with fresh_db.tracer(tracer):
        dogs.transform(**params)
    # If use_pragma_foreign_keys, check that we did the right thing
    if use_pragma_foreign_keys:
        assert ("PRAGMA foreign_keys=0;", None) in captured
        assert captured[-2] == ("PRAGMA foreign_key_check;", None)
        assert captured[-1] == ("PRAGMA foreign_keys=1;", None)
    else:
        assert ("PRAGMA foreign_keys=0;", None) not in captured
        assert ("PRAGMA foreign_keys=1;", None) not in captured


def test_transform_sql_with_no_primary_key_to_primary_key_of_id(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": "5"})
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER,\n   "name" TEXT,\n   "age" TEXT\n)'
    )
    dogs.transform(pk="id")
    # Slight oddity: [dogs] becomes "dogs" during the rename:
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" TEXT\n)'
    )


def test_transform_rename_pk(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": "5"}, pk="id")
    dogs.transform(rename={"id": "pk"})
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "pk" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" TEXT\n)'
    )


def test_transform_preserves_keyword_literal_defaults(fresh_db):
    # transform() used to requote keyword-literal defaults (DEFAULT TRUE became
    # DEFAULT 'TRUE'), so a default insert stored the text 'TRUE' instead of the
    # integer 1 -- silent value corruption on every rebuilt table.
    fresh_db.execute(
        "CREATE TABLE t ("
        " id INTEGER PRIMARY KEY,"
        " is_active INTEGER DEFAULT TRUE,"
        " flag INTEGER DEFAULT FALSE,"
        " note TEXT DEFAULT NULL"
        ")"
    )
    table = fresh_db.table("t")
    table.insert({"id": 1})
    before = fresh_db.execute("SELECT is_active, flag, note FROM t").fetchone()
    assert before == (1, 0, None)

    # Rebuild the table via an unrelated change.
    table.transform(rename={"note": "note2"})

    # The keyword literals stay unquoted in the schema ...
    assert "DEFAULT TRUE" in table.schema
    assert "DEFAULT FALSE" in table.schema
    assert "DEFAULT NULL" in table.schema
    assert "'TRUE'" not in table.schema

    # ... and a fresh default insert still yields 1 / 0 / NULL, not strings.
    table.insert({"id": 2})
    after = fresh_db.execute(
        "SELECT is_active, flag, note2 FROM t WHERE id = 2"
    ).fetchone()
    assert after == (1, 0, None)


def test_transform_not_null(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": "5"}, pk="id")
    dogs.transform(not_null={"name"})
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT NOT NULL,\n   "age" TEXT\n)'
    )


def test_transform_remove_a_not_null(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": "5"}, not_null={"age"}, pk="id")
    dogs.transform(not_null={"name": True, "age": False})
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT NOT NULL,\n   "age" TEXT\n)'
    )


@pytest.mark.parametrize("not_null", [{"age"}, {"age": True}])
def test_transform_add_not_null_with_rename(fresh_db, not_null):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": "5"}, pk="id")
    dogs.transform(not_null=not_null, rename={"age": "dog_age"})
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "dog_age" TEXT NOT NULL\n)'
    )


def test_transform_defaults(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": 5}, pk="id")
    dogs.transform(defaults={"age": 1})
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" INTEGER DEFAULT 1\n)'
    )


def test_transform_defaults_and_rename_column(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": 5}, pk="id")
    dogs.transform(rename={"age": "dog_age"}, defaults={"age": 1})
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "dog_age" INTEGER DEFAULT 1\n)'
    )


def test_remove_defaults(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": 5}, defaults={"age": 1}, pk="id")
    dogs.transform(defaults={"age": None})
    assert (
        dogs.schema
        == 'CREATE TABLE "dogs" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT,\n   "age" INTEGER\n)'
    )


@pytest.fixture
def authors_db(fresh_db):
    books = fresh_db.table("books")
    authors = fresh_db.table("authors")
    authors.insert({"id": 5, "name": "Jane McGonical"}, pk="id")
    books.insert(
        {"id": 2, "title": "Reality is Broken", "author_id": 5},
        foreign_keys=("author_id",),
        pk="id",
    )
    return fresh_db


def test_transform_foreign_keys_persist(authors_db):
    assert authors_db.table("books").foreign_keys == [
        ForeignKey(
            table="books", column="author_id", other_table="authors", other_column="id"
        )
    ]
    authors_db.table("books").transform(rename={"title": "book_title"})
    assert authors_db.table("books").foreign_keys == [
        ForeignKey(
            table="books", column="author_id", other_table="authors", other_column="id"
        )
    ]


@pytest.mark.parametrize("use_pragma_foreign_keys", [False, True])
def test_transform_foreign_keys_survive_renamed_column(
    authors_db, use_pragma_foreign_keys
):
    if use_pragma_foreign_keys:
        authors_db.conn.execute("PRAGMA foreign_keys=ON")
    authors_db.table("books").transform(rename={"author_id": "author_id_2"})
    assert authors_db.table("books").foreign_keys == [
        ForeignKey(
            table="books",
            column="author_id_2",
            other_table="authors",
            other_column="id",
        )
    ]


def _add_country_city_continent(db):
    db.table("country").insert({"id": 1, "name": "France"}, pk="id")
    db.table("continent").insert({"id": 2, "name": "Europe"}, pk="id")
    db.table("city").insert({"id": 24, "name": "Paris"}, pk="id")


_CAVEAU = {
    "id": 32,
    "name": "Caveau de la Huchette",
    "country": 1,
    "continent": 2,
    "city": 24,
}


@pytest.mark.parametrize("use_pragma_foreign_keys", [False, True])
def test_transform_drop_foreign_keys(fresh_db, use_pragma_foreign_keys):
    if use_pragma_foreign_keys:
        fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    # Create table with three foreign keys so we can drop two of them
    _add_country_city_continent(fresh_db)
    fresh_db.table("places").insert(
        _CAVEAU,
        foreign_keys=("country", "continent", "city"),
    )
    assert fresh_db.table("places").foreign_keys == [
        ForeignKey(
            table="places", column="city", other_table="city", other_column="id"
        ),
        ForeignKey(
            table="places",
            column="continent",
            other_table="continent",
            other_column="id",
        ),
        ForeignKey(
            table="places", column="country", other_table="country", other_column="id"
        ),
    ]
    # Drop two of those foreign keys
    fresh_db.table("places").transform(drop_foreign_keys=("country", "continent"))
    # Should be only one foreign key now
    assert fresh_db.table("places").foreign_keys == [
        ForeignKey(table="places", column="city", other_table="city", other_column="id")
    ]
    if use_pragma_foreign_keys:
        assert fresh_db.conn.execute("PRAGMA foreign_keys").fetchone()[0]


def test_transform_verify_foreign_keys(fresh_db):
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.table("authors").insert({"id": 3, "name": "Tina"}, pk="id")
    fresh_db.table("books").insert(
        {"id": 1, "title": "Book", "author_id": 3}, pk="id", foreign_keys={"author_id"}
    )
    # Renaming the id column on authors should break everything
    with pytest.raises(OperationalError) as e:
        fresh_db.table("authors").transform(rename={"id": "id2"})
    assert e.value.args[0] == 'foreign key mismatch - "books" referencing "authors"'
    # This should have rolled us back
    assert (
        fresh_db.table("authors").schema
        == 'CREATE TABLE "authors" (\n   "id" INTEGER PRIMARY KEY,\n   "name" TEXT\n)'
    )
    assert fresh_db.conn.execute("PRAGMA foreign_keys").fetchone()[0]


@pytest.mark.parametrize("use_pragma_foreign_keys", [False, True])
def test_transform_on_delete_cascade_does_not_delete_records(
    fresh_db, use_pragma_foreign_keys
):
    # Transforming a table drops and recreates it - if another table references
    # it with ON DELETE CASCADE and PRAGMA foreign_keys is on, that drop must
    # not cascade and delete the referencing records
    if use_pragma_foreign_keys:
        fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.executescript("""
        CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE
        );
        """)
    fresh_db.table("authors").insert({"id": 1, "name": "Ursula K. Le Guin"})
    fresh_db.table("books").insert(
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    )
    # Transform the table on the other end of the cascading foreign key
    fresh_db.table("authors").transform(rename={"name": "author_name"})
    assert list(fresh_db.table("authors").rows) == [
        {"id": 1, "author_name": "Ursula K. Le Guin"}
    ]
    assert list(fresh_db.table("books").rows) == [
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    ]
    # Transforming the table with the cascading foreign key should not
    # delete its records either
    fresh_db.table("books").transform(rename={"title": "book_title"})
    assert list(fresh_db.table("books").rows) == [
        {"id": 1, "book_title": "The Dispossessed", "author_id": 1}
    ]
    if use_pragma_foreign_keys:
        assert fresh_db.conn.execute("PRAGMA foreign_keys").fetchone()[0]


@pytest.mark.parametrize("on_delete", ["CASCADE", "SET NULL", "SET DEFAULT", "cascade"])
def test_transform_in_transaction_refuses_destructive_on_delete(fresh_db, on_delete):
    # PRAGMA foreign_keys is a no-op inside a transaction, so transforming a
    # table referenced by ON DELETE CASCADE / SET NULL / SET DEFAULT foreign
    # keys inside an open transaction would fire those actions when the old
    # table is dropped - transform() should refuse instead
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.executescript(f"""
        CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER REFERENCES authors(id) ON DELETE {on_delete}
        );
        """)
    fresh_db.table("authors").insert({"id": 1, "name": "Ursula K. Le Guin"})
    fresh_db.table("books").insert(
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    )
    previous_schema = fresh_db.table("authors").schema
    with fresh_db.atomic(), pytest.raises(TransactionError) as excinfo:
        fresh_db.table("authors").transform(rename={"name": "author_name"})
    message = str(excinfo.value)
    assert "books" in message
    assert f"ON DELETE {on_delete.upper()}" in message
    # Nothing should have changed
    assert fresh_db.table("authors").schema == previous_schema
    assert list(fresh_db.table("books").rows) == [
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    ]
    assert fresh_db.conn.execute("PRAGMA foreign_keys").fetchone()[0]


def test_transform_in_transaction_refuses_self_referential_cascade(fresh_db):
    # The copied table carries a foreign key referencing the original table
    # name, so a self-referential cascade would wipe the copy too
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.executescript("""
        CREATE TABLE categories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            parent_id INTEGER REFERENCES categories(id) ON DELETE CASCADE
        );
        """)
    fresh_db.table("categories").insert_all(
        [
            {"id": 1, "name": "Fiction", "parent_id": None},
            {"id": 2, "name": "Science Fiction", "parent_id": 1},
        ]
    )
    with fresh_db.atomic(), pytest.raises(TransactionError) as excinfo:
        fresh_db.table("categories").transform(rename={"name": "title"})
    assert "categories" in str(excinfo.value)
    assert fresh_db.table("categories").count == 2


def test_transform_in_transaction_allowed_with_no_action_foreign_key(fresh_db):
    # An inbound foreign key without a destructive ON DELETE action is safe
    # inside a transaction thanks to PRAGMA defer_foreign_keys
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.executescript("""
        CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER REFERENCES authors(id)
        );
        """)
    fresh_db.table("authors").insert({"id": 1, "name": "Ursula K. Le Guin"})
    fresh_db.table("books").insert(
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    )
    with fresh_db.atomic():
        fresh_db.table("authors").transform(rename={"name": "author_name"})
    assert list(fresh_db.table("authors").rows) == [
        {"id": 1, "author_name": "Ursula K. Le Guin"}
    ]
    assert list(fresh_db.table("books").rows) == [
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    ]
    assert fresh_db.conn.execute("PRAGMA foreign_keys").fetchone()[0]


def test_transform_in_transaction_allowed_for_child_table(fresh_db):
    # The table being transformed only has an outbound foreign key - dropping
    # it fires no ON DELETE actions, so this is allowed inside a transaction
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    fresh_db.executescript("""
        CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE
        );
        """)
    fresh_db.table("authors").insert({"id": 1, "name": "Ursula K. Le Guin"})
    fresh_db.table("books").insert(
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    )
    with fresh_db.atomic():
        fresh_db.table("books").transform(rename={"title": "book_title"})
    assert list(fresh_db.table("books").rows) == [
        {"id": 1, "book_title": "The Dispossessed", "author_id": 1}
    ]


def test_transform_in_transaction_allowed_with_foreign_keys_off(fresh_db):
    # With PRAGMA foreign_keys off (the default) no cascades can fire, so
    # transform inside a transaction is safe even with a CASCADE schema
    fresh_db.executescript("""
        CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE
        );
        """)
    fresh_db.table("authors").insert({"id": 1, "name": "Ursula K. Le Guin"})
    fresh_db.table("books").insert(
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    )
    with fresh_db.atomic():
        fresh_db.table("authors").transform(rename={"name": "author_name"})
    assert list(fresh_db.table("books").rows) == [
        {"id": 1, "title": "The Dispossessed", "author_id": 1}
    ]


def test_transform_add_foreign_keys_from_scratch(fresh_db):
    _add_country_city_continent(fresh_db)
    fresh_db.table("places").insert(_CAVEAU)
    # Should have no foreign keys
    assert fresh_db.table("places").foreign_keys == []
    # Now add them using .transform()
    fresh_db.table("places").transform(
        add_foreign_keys=("country", "continent", "city")
    )
    # Should now have all three:
    assert fresh_db.table("places").foreign_keys == [
        ForeignKey(
            table="places", column="city", other_table="city", other_column="id"
        ),
        ForeignKey(
            table="places",
            column="continent",
            other_table="continent",
            other_column="id",
        ),
        ForeignKey(
            table="places", column="country", other_table="country", other_column="id"
        ),
    ]
    assert fresh_db.table("places").schema == (
        'CREATE TABLE "places" (\n'
        '   "id" INTEGER,\n'
        '   "name" TEXT,\n'
        '   "country" INTEGER REFERENCES "country"("id"),\n'
        '   "continent" INTEGER REFERENCES "continent"("id"),\n'
        '   "city" INTEGER REFERENCES "city"("id")\n'
        ")"
    )


@pytest.mark.parametrize(
    "add_foreign_keys",
    (
        ("country", "continent"),
        # Fully specified
        (
            ("country", "country", "id"),
            ("continent", "continent", "id"),
        ),
    ),
)
def test_transform_add_foreign_keys_from_partial(fresh_db, add_foreign_keys):
    _add_country_city_continent(fresh_db)
    fresh_db.table("places").insert(
        _CAVEAU,
        foreign_keys=("city",),
    )
    # Should have one foreign keys
    assert fresh_db.table("places").foreign_keys == [
        ForeignKey(table="places", column="city", other_table="city", other_column="id")
    ]
    # Now add three more using .transform()
    fresh_db.table("places").transform(add_foreign_keys=add_foreign_keys)
    # Should now have all three:
    assert fresh_db.table("places").foreign_keys == [
        ForeignKey(
            table="places", column="city", other_table="city", other_column="id"
        ),
        ForeignKey(
            table="places",
            column="continent",
            other_table="continent",
            other_column="id",
        ),
        ForeignKey(
            table="places", column="country", other_table="country", other_column="id"
        ),
    ]


@pytest.mark.parametrize(
    "foreign_keys",
    (
        ("country", "continent"),
        # Fully specified
        (
            ("country", "country", "id"),
            ("continent", "continent", "id"),
        ),
    ),
)
def test_transform_replace_foreign_keys(fresh_db, foreign_keys):
    _add_country_city_continent(fresh_db)
    fresh_db.table("places").insert(
        _CAVEAU,
        foreign_keys=("city",),
    )
    assert len(fresh_db.table("places").foreign_keys) == 1
    # Replace with two different ones
    fresh_db.table("places").transform(foreign_keys=foreign_keys)
    assert fresh_db.table("places").schema == (
        'CREATE TABLE "places" (\n'
        '   "id" INTEGER,\n'
        '   "name" TEXT,\n'
        '   "country" INTEGER REFERENCES "country"("id"),\n'
        '   "continent" INTEGER REFERENCES "continent"("id"),\n'
        '   "city" INTEGER\n'
        ")"
    )


@pytest.mark.parametrize("table_type", ("id_pk", "rowid", "compound_pk"))
def test_transform_preserves_rowids(fresh_db, table_type):
    pk = None
    if table_type == "id_pk":
        pk = "id"
    elif table_type == "compound_pk":
        pk = ("id", "name")
    elif table_type == "rowid":
        pk = None
    fresh_db.table("places").insert_all(
        [
            {"id": "1", "name": "Paris", "country": "France"},
            {"id": "2", "name": "London", "country": "UK"},
            {"id": "3", "name": "New York", "country": "USA"},
        ],
        pk=pk,
    )
    # Now delete and insert a row to mix up the `rowid` sequence
    fresh_db.table("places").delete_where("id = ?", ["2"])
    fresh_db.table("places").insert({"id": "4", "name": "London", "country": "UK"})
    previous_rows = [
        tuple(row) for row in fresh_db.execute("select rowid, id, name from places")
    ]
    # Transform it
    fresh_db.table("places").transform(column_order=("country", "name"))
    # Should be the same
    next_rows = [
        tuple(row) for row in fresh_db.execute("select rowid, id, name from places")
    ]
    assert previous_rows == next_rows


@pytest.mark.parametrize(
    "initial_strict,transform_strict,expected_strict",
    (
        (False, None, False),
        (True, None, True),
        (False, True, True),
        (True, False, False),
    ),
)
def test_transform_strict(fresh_db, initial_strict, transform_strict, expected_strict):
    if not fresh_db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    dogs = fresh_db.table("dogs", strict=initial_strict)
    dogs.insert({"id": 1, "name": "Cleo"})
    assert dogs.strict is initial_strict
    dogs.transform(strict=transform_strict)
    assert dogs.strict is expected_strict


def test_transform_to_strict_with_invalid_data(fresh_db):
    if not fresh_db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    dogs = fresh_db.table("dogs")
    dogs.create({"id": int})
    dogs.insert({"id": "not-an-integer"})

    with pytest.raises(sqlite3.IntegrityError):
        dogs.transform(strict=True)

    assert dogs.strict is False
    assert list(dogs.rows) == [{"id": "not-an-integer"}]
    assert fresh_db.table_names() == ["dogs"]


def test_transform_strict_updates_default(fresh_db):
    if not fresh_db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    table = fresh_db.table("items", strict=True)
    table.create({"id": int})

    table.transform(strict=False)
    assert table.strict is False

    table.create({"id": int}, replace=True)
    assert table.strict is False


@pytest.mark.parametrize("method_name", ("transform", "transform_sql"))
def test_transform_to_strict_not_supported(fresh_db, method_name):
    table = fresh_db.table("items")
    table.create({"id": int})
    fresh_db._supports_strict = False

    with pytest.raises(TransformError, match="SQLite does not support STRICT tables"):
        getattr(table, method_name)(strict=True)

    assert table.strict is False


def test_transform_preserves_any_column_in_strict_table(fresh_db):
    if not fresh_db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    fresh_db.execute("create table items (id integer primary key, data any) strict")
    fresh_db.conn.executemany(
        "insert into items values (?, ?)",
        [
            (1, 42),
            (2, "000123"),
            (3, 3.14),
            (4, b"bytes"),
            (5, None),
        ],
    )
    table = fresh_db["items"]

    table.transform()

    assert table.strict is True
    assert table.columns_dict == {"id": int, "data": ANY}
    assert fresh_db.execute(
        "select typeof(data), data from items order by id"
    ).fetchall() == [
        ("integer", 42),
        ("text", "000123"),
        ("real", 3.14),
        ("blob", b"bytes"),
        ("null", None),
    ]


def test_transform_any_column_from_strict_to_non_strict(fresh_db):
    if not fresh_db.supports_strict:
        pytest.skip("SQLite version does not support strict tables")
    fresh_db.execute("create table items (data any) strict")
    fresh_db.execute("insert into items values (?)", ("000123",))
    table = fresh_db["items"]

    table.transform(strict=False)

    assert table.strict is False
    assert table.columns_dict == {"data": ANY}
    # Ordinary non-STRICT ANY columns apply NUMERIC affinity
    assert fresh_db.execute("select typeof(data), data from items").fetchone() == (
        "integer",
        123,
    )


@pytest.mark.parametrize(
    "indexes, transform_params",
    [
        ([["name"]], {"types": {"age": str}}),
        ([["name"], ["age", "breed"]], {"types": {"age": str}}),
        ([], {"types": {"age": str}}),
        ([["name"]], {"types": {"age": str}, "keep_table": "old_dogs"}),
    ],
)
def test_transform_indexes(fresh_db, indexes, transform_params):
    # https://github.com/simonw/sqlite-utils/issues/633
    # New table should have same indexes as old table after transformation
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": 5, "breed": "Labrador"}, pk="id")

    for index in indexes:
        dogs.create_index(index)

    indexes_before_transform = dogs.indexes

    dogs.transform(**transform_params)

    assert sorted(
        [
            {k: v for k, v in idx._asdict().items() if k != "seq"}
            for idx in dogs.indexes
        ],
        key=lambda x: x["name"],
    ) == sorted(
        [
            {k: v for k, v in idx._asdict().items() if k != "seq"}
            for idx in indexes_before_transform
        ],
        key=lambda x: x["name"],
    ), f"Indexes before transform: {indexes_before_transform}\nIndexes after transform: {dogs.indexes}"
    if "keep_table" in transform_params:
        assert all(
            index.origin == "pk"
            for index in fresh_db.table(transform_params["keep_table"]).indexes
        )


def test_transform_retains_indexes_with_foreign_keys(fresh_db):
    dogs = fresh_db.table("dogs")
    owners = fresh_db.table("owners")

    dogs.insert({"id": 1, "name": "Cleo", "owner_id": 1}, pk="id")
    owners.insert({"id": 1, "name": "Alice"}, pk="id")

    dogs.create_index(["name"])

    indexes_before_transform = dogs.indexes

    fresh_db.add_foreign_keys([("dogs", "owner_id", "owners", "id")])  # calls transform

    assert sorted(
        [
            {k: v for k, v in idx._asdict().items() if k != "seq"}
            for idx in dogs.indexes
        ],
        key=lambda x: x["name"],
    ) == sorted(
        [
            {k: v for k, v in idx._asdict().items() if k != "seq"}
            for idx in indexes_before_transform
        ],
        key=lambda x: x["name"],
    ), f"Indexes before transform: {indexes_before_transform}\nIndexes after transform: {dogs.indexes}"


def test_transform_with_indexes_errors(fresh_db):
    # Should error with a compound (name, age) index if age is dropped
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "age": 5}, pk="id")

    dogs.create_index(["name", "age"])

    with pytest.raises(TransformError) as excinfo:
        dogs.transform(drop=["age"])

    assert (
        "Index 'idx_dogs_name_age' column 'age' is not in updated table 'dogs'. "
        "You must manually drop this index prior to running this transformation"
        in str(excinfo.value)
    )


@pytest.mark.parametrize(
    ("table_name", "index_name"),
    (("name", "idx_name"), ("t", "name")),
)
def test_transform_rename_column_with_index(fresh_db, table_name, index_name):
    # https://github.com/simonw/sqlite-utils/issues/822
    # Use the same name for the table, column and index to ensure only the
    # indexed column changes.
    table = fresh_db.table(table_name)
    table.insert({"id": 1, "name": "Cleo"}, pk="id")
    table.create_index(["name"], index_name=index_name)

    sqls = table.transform_sql(rename={"name": "full_name"}, tmp_suffix="suffix")
    drop_index_sql = f'DROP INDEX IF EXISTS "{index_name}";'
    assert drop_index_sql in sqls
    assert sqls.index(drop_index_sql) < sqls.index(f'DROP TABLE "{table_name}";')

    table.transform(rename={"name": "full_name"})

    assert [column.name for column in table.columns] == ["id", "full_name"]
    assert [(index.name, index.columns) for index in table.indexes] == [
        (index_name, ["full_name"])
    ]


def test_transform_recreates_renamed_index_from_metadata(fresh_db):
    table = fresh_db.table("t")
    table.insert({"alpha": "one", "beta": "two"})
    # Deliberately use unquoted SQL and index details that need to survive the
    # reconstruction. Renaming both columns also guards against cascading
    # string substitutions.
    fresh_db.execute(
        "CREATE UNIQUE INDEX swap_idx ON t(alpha COLLATE NOCASE DESC, beta)"
    )

    table.transform(rename={"alpha": "beta", "beta": "alpha"})

    assert table.columns_dict == {"beta": str, "alpha": str}
    assert [(index.name, index.unique, index.columns) for index in table.indexes] == [
        ("swap_idx", 1, ["beta", "alpha"])
    ]
    key_columns = [column for column in table.xindexes[0].columns if column.key]
    assert [(column.name, column.desc, column.coll) for column in key_columns] == [
        ("beta", 1, "NOCASE"),
        ("alpha", 0, "BINARY"),
    ]


@pytest.mark.parametrize(
    "index_sql",
    (
        "CREATE INDEX idx_t_name ON t(lower(name))",
        "CREATE INDEX idx_t_name ON t(name) WHERE name IS NOT NULL",
    ),
)
def test_transform_rename_complex_index_errors(fresh_db, index_sql):
    table = fresh_db.table("t")
    table.insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.execute(index_sql)

    with pytest.raises(TransformError, match="partial or expression index"):
        table.transform(rename={"name": "full_name"})

    assert table.columns_dict == {"id": int, "name": str}
    assert [index.name for index in table.indexes] == ["idx_t_name"]


def test_transform_with_unique_constraint_implicit_index(fresh_db):
    dogs = fresh_db.table("dogs")
    # Create a table with a UNIQUE constraint on 'name', which creates an implicit index
    fresh_db.execute("""
        CREATE TABLE dogs (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE ON CONFLICT IGNORE,
            age INTEGER
        );
    """)
    dogs.insert({"id": 1, "name": "Cleo", "age": 5})

    dogs.transform(types={"age": str}, rename={"name": "dog_name"})

    assert 'dog_name" TEXT UNIQUE ON CONFLICT IGNORE' in dogs.schema
    dogs.insert({"id": 2, "dog_name": "Cleo", "age": "6"})
    assert list(dogs.rows) == [{"id": 1, "dog_name": "Cleo", "age": "5"}]


def test_transform_preserves_composite_unique_constraint(fresh_db):
    fresh_db.execute("""
        CREATE TABLE memberships (
            account_id INTEGER,
            email TEXT,
            note TEXT,
            CONSTRAINT unique_membership
                UNIQUE (account_id DESC, email COLLATE NOCASE)
                ON CONFLICT ABORT
        )
    """)
    memberships = fresh_db.table("memberships")
    memberships.insert({"account_id": 1, "email": "one@example.com", "note": "x"})

    memberships.transform(rename={"account_id": "organization_id"}, types={"note": str})

    assert (
        'CONSTRAINT "unique_membership" UNIQUE '
        '("organization_id" DESC, "email" COLLATE "NOCASE") ON CONFLICT ABORT'
        in memberships.schema
    )
    with pytest.raises(sqlite3.IntegrityError):
        memberships.insert(
            {"organization_id": 1, "email": "ONE@example.com", "note": "y"}
        )


def test_transform_preserves_column_unique_collation(fresh_db):
    fresh_db.execute("""
        CREATE TABLE people (
            id INTEGER PRIMARY KEY,
            name TEXT COLLATE NOCASE UNIQUE
        )
    """)
    people = fresh_db.table("people")
    people.insert({"id": 1, "name": "Cleo"})

    people.transform(rename={"name": "full_name"})

    assert 'UNIQUE ("full_name" COLLATE "NOCASE")' in people.schema
    with pytest.raises(sqlite3.IntegrityError):
        people.insert({"id": 2, "full_name": "cleo"})


def test_transform_drops_entire_composite_unique_constraint(fresh_db):
    fresh_db.execute("""
        CREATE TABLE memberships (
            account_id INTEGER,
            email TEXT,
            UNIQUE (account_id, email)
        )
    """)
    memberships = fresh_db.table("memberships")
    memberships.insert({"account_id": 1, "email": "one@example.com"})

    memberships.transform(drop={"email"})

    assert "UNIQUE" not in memberships.schema
    memberships.insert({"account_id": 1})


def test_transform_preserves_autoincrement_and_sequence(fresh_db):
    fresh_db.execute(
        "CREATE TABLE entries (id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT)"
    )
    entries = fresh_db.table("entries")
    entries.insert_all(({"value": "one"}, {"value": "two"}))
    entries.delete(2)

    entries.transform(rename={"value": "label"})

    assert "PRIMARY KEY AUTOINCREMENT" in entries.schema
    entries.insert({"label": "three"})
    assert list(entries.rows) == [
        {"id": 1, "label": "one"},
        {"id": 3, "label": "three"},
    ]


@pytest.mark.parametrize(
    "new_type,expected_value,expected_type",
    [
        (int, 42, int),
        (float, 42.0, float),
        ("integer", 42, int),
        ("float", 42.0, float),
        ("REAL", 42.0, float),
    ],
)
def test_transform_empty_string_to_null_for_numeric_types(
    fresh_db, new_type, expected_value, expected_type
):
    fresh_db["test"].insert_all(
        [
            {"id": 1, "value": "42"},
            {"id": 2, "value": ""},
            {"id": 3, "value": None},
            {"id": 4, "value": " "},
        ]
    )
    fresh_db["test"].transform(types={"value": new_type})
    rows = {r["id"]: r["value"] for r in fresh_db["test"].rows}
    assert rows[1] == expected_value
    assert type(rows[1]) is expected_type
    assert rows[2] is None
    assert rows[3] is None
    assert rows[4] == " "


def test_transform_preserves_view(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/831
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.execute("create view dogs_view as select id, name from dogs")
    view_sql_before = fresh_db.execute(
        "select sql from sqlite_master where name = 'dogs_view'"
    ).fetchone()[0]
    dogs.transform(rename={"name": "title"})
    view_sql_after = fresh_db.execute(
        "select sql from sqlite_master where name = 'dogs_view'"
    ).fetchone()[0]
    assert view_sql_before == view_sql_after


@pytest.mark.parametrize(
    "transform_params",
    [
        {"types": {"name": int}},
        {"pk": "name"},
        {"add_foreign_keys": [("other_id", "other", "id")]},
        {"drop_foreign_keys": ["other_id"]},
    ],
)
def test_transform_variants_preserve_view(fresh_db, transform_params):
    # Covers retyping, changing primary key and foreign key modifications,
    # with a view whose columns are untouched by the transform
    fresh_db.table("other").insert({"id": 1}, pk="id")
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo", "other_id": 1}, pk="id")
    if "drop_foreign_keys" in transform_params:
        dogs.transform(add_foreign_keys=[("other_id", "other", "id")])
    fresh_db.execute("create view dogs_view as select id, name from dogs")
    view_sql_before = fresh_db.execute(
        "select sql from sqlite_master where name = 'dogs_view'"
    ).fetchone()[0]
    dogs.transform(**transform_params)
    view_sql_after = fresh_db.execute(
        "select sql from sqlite_master where name = 'dogs_view'"
    ).fetchone()[0]
    assert view_sql_before == view_sql_after
    assert list(fresh_db.view("dogs_view").rows) == [{"id": 1, "name": "Cleo"}]


def test_transform_view_referencing_renamed_column(fresh_db):
    # The view survives but querying it raises "no such column" - inherent
    # to SQLite views, whose SQL is stored as text
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.execute("create view dogs_view as select id, name from dogs")
    dogs.transform(rename={"name": "title"})
    with pytest.raises(OperationalError, match="no such column"):
        fresh_db.execute("select * from dogs_view")


def test_transform_view_on_view(fresh_db):
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.execute("create view v1 as select id, name from dogs")
    fresh_db.execute("create view v2 as select name from v1")
    sqls_before = fresh_db.execute(
        "select sql from sqlite_master where type = 'view' order by name"
    ).fetchall()
    dogs.transform(types={"id": str})
    sqls_after = fresh_db.execute(
        "select sql from sqlite_master where type = 'view' order by name"
    ).fetchall()
    assert sqls_before == sqls_after
    assert list(fresh_db.view("v2").rows) == [{"name": "Cleo"}]


def test_transform_keep_table_does_not_repoint_view(fresh_db):
    # Without legacy_alter_table the ALTER TABLE dogs RENAME TO dogs_backup
    # step would rewrite the view to select from "dogs_backup"
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.execute("create view dogs_view as select id, name from dogs")
    dogs.transform(types={"name": str}, keep_table="dogs_backup")
    view_sql = fresh_db.execute(
        "select sql from sqlite_master where name = 'dogs_view'"
    ).fetchone()[0]
    assert "dogs_backup" not in view_sql
    # View reads from the live table, not the frozen backup
    dogs.insert({"id": 2, "name": "Pancakes"})
    assert list(fresh_db.view("dogs_view").rows) == [
        {"id": 1, "name": "Cleo"},
        {"id": 2, "name": "Pancakes"},
    ]


def test_transform_sql_standalone_statements_work_with_view(fresh_db):
    # The documented "run these statements yourself" workflow should be
    # standalone-correct, so the pragmas must come from transform_sql()
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.execute("create view dogs_view as select id, name from dogs")
    sqls = dogs.transform_sql(types={"name": str}, tmp_suffix="suffix")
    assert sqls[-3] == "PRAGMA legacy_alter_table=ON;"
    assert sqls[-2] == 'ALTER TABLE "dogs_new_suffix" RENAME TO "dogs";'
    assert sqls[-1] == "PRAGMA legacy_alter_table=OFF;"
    for sql in sqls:
        fresh_db.execute(sql)
    assert list(fresh_db.view("dogs_view").rows) == [{"id": 1, "name": "Cleo"}]


def test_transform_with_view_in_open_transaction(fresh_db):
    fresh_db.conn.execute("PRAGMA foreign_keys=ON")
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id")
    fresh_db.execute("create view dogs_view as select id, name from dogs")
    with fresh_db.conn:
        fresh_db.execute("insert into dogs (id, name) values (2, 'Pancakes')")
        dogs.transform(rename={"name": "title"})
    assert dogs.columns_dict == {"id": int, "title": str}
    view_sql = fresh_db.execute(
        "select sql from sqlite_master where name = 'dogs_view'"
    ).fetchone()[0]
    assert view_sql == "CREATE VIEW dogs_view as select id, name from dogs"


def test_transform_restores_legacy_alter_table_setting(fresh_db):
    if sqlite3.sqlite_version_info < (3, 25, 0):
        pytest.skip("legacy_alter_table pragma requires SQLite 3.25 or higher")
    dogs = fresh_db.table("dogs")
    dogs.insert({"id": 1, "name": "Cleo"}, pk="id")
    # Default is OFF, reset to OFF afterwards
    dogs.transform(types={"name": str})
    assert fresh_db.execute("PRAGMA legacy_alter_table").fetchone()[0] == 0
    # If the connection has it ON, it should be restored to ON
    fresh_db.execute("PRAGMA legacy_alter_table=ON")
    sqls = dogs.transform_sql(types={"name": str}, tmp_suffix="suffix")
    assert sqls[-1] == "PRAGMA legacy_alter_table=ON;"
    dogs.transform(types={"name": str})
    assert fresh_db.execute("PRAGMA legacy_alter_table").fetchone()[0] == 1


def test_transform_preserves_check_constraints(fresh_db):
    fresh_db.execute("""
        CREATE TABLE scores (
            id INTEGER PRIMARY KEY,
            score INTEGER CONSTRAINT valid_score CHECK(score BETWEEN 0 AND 100),
            CONSTRAINT nonzero_id CHECK(id != 0)
        )
    """)
    scores = fresh_db.table("scores")
    scores.insert({"id": 1, "score": 50})
    scores.transform()
    assert scores.checks == [
        Check("score BETWEEN 0 AND 100", name="valid_score", column="score"),
        Check("id != 0", name="nonzero_id"),
    ]
    with pytest.raises(sqlite3.IntegrityError, match="CHECK constraint failed"):
        scores.insert({"id": 2, "score": 101})


def test_transform_preserves_check_ending_in_line_comment(fresh_db):
    fresh_db.execute("""
        CREATE TABLE inventory (
            quantity INTEGER,
            CHECK (
                quantity >= 0 -- Quantity cannot be negative
            )
        )
    """)
    inventory = fresh_db.table("inventory")
    inventory.transform(types={"quantity": float})
    assert inventory.checks == [Check("quantity >= 0 -- Quantity cannot be negative")]
    with pytest.raises(sqlite3.IntegrityError, match="CHECK constraint failed"):
        inventory.insert({"quantity": -1})


def test_transform_preserves_comments_owned_by_columns(fresh_db):
    fresh_db.execute("""
        CREATE TABLE people (
            -- Primary identifier
            id INTEGER PRIMARY KEY /* IDs are stable */,
            /* Displayed to users */
            name TEXT /* May contain spaces */,
            -- Age in years
            age INTEGER -- May be NULL
        )
    """)
    people = fresh_db.table("people")
    people.insert({"id": 1, "name": "Cleo", "age": 5})
    people.transform(
        rename={"name": "display_name"},
        types={"age": float},
        column_order=("age", "id", "name"),
    )
    assert people.get(1) == {"age": 5.0, "id": 1, "display_name": "Cleo"}
    schema = people.schema
    assert schema.index("-- Age in years") < schema.index('"age" REAL')
    assert schema.index('"age" REAL') < schema.index("-- May be NULL")
    assert schema.index("-- Primary identifier") < schema.index('"id" INTEGER')
    assert schema.index('"id" INTEGER') < schema.index("/* IDs are stable */")
    assert schema.index("/* Displayed to users */") < schema.index(
        '"display_name" TEXT'
    )
    assert schema.index('"display_name" TEXT') < schema.index(
        "/* May contain spaces */"
    )


def test_transform_drops_comments_owned_by_dropped_column(fresh_db):
    fresh_db.execute("""
        CREATE TABLE t (
            /* Keep this explanation */
            id INTEGER,
            /* Drop this explanation */
            obsolete TEXT /* Drop this too */
        )
    """)
    fresh_db.table("t").transform(drop={"obsolete"})
    schema = fresh_db.table("t").schema
    assert "Keep this explanation" in schema
    assert "Drop this explanation" not in schema
    assert "Drop this too" not in schema


def test_transform_renames_columns_inside_check_constraints(fresh_db):
    fresh_db.execute("""
        CREATE TABLE inventory (
            quantity INTEGER CONSTRAINT positive
                CHECK(quantity > 0 AND 'quantity' != ''),
            maximum INTEGER,
            CONSTRAINT within_maximum CHECK(quantity <= maximum)
        )
    """)
    inventory = fresh_db.table("inventory")
    inventory.insert({"quantity": 2, "maximum": 3})
    inventory.transform(rename={"quantity": "amount"})
    assert inventory.checks == [
        Check(
            "amount > 0 AND 'quantity' != ''",
            name="positive",
            column="amount",
        ),
        Check("amount <= maximum", name="within_maximum"),
    ]
    with pytest.raises(sqlite3.IntegrityError, match="CHECK constraint failed"):
        inventory.insert({"amount": 4, "maximum": 3})


def test_transform_check_rewrite_preserves_functions_and_quotes(fresh_db):
    fresh_db.execute("""
        CREATE TABLE items (
            length TEXT,
            "old name" TEXT,
            CHECK(length("old name") > 0 AND length != '')
        )
    """)
    items = fresh_db.table("items")
    items.insert({"length": "label", "old name": "hello"})
    items.transform(rename={"length": "description", "old name": "new name"})
    assert items.checks == [Check("length(\"new name\") > 0 AND description != ''")]


def test_transform_check_rewrite_quotes_keyword_column(fresh_db):
    fresh_db.execute("CREATE TABLE t(old_name TEXT CHECK(old_name != ''))")
    fresh_db.table("t").insert({"old_name": "value"})
    fresh_db.table("t").transform(rename={"old_name": "select"})
    assert fresh_db.table("t").checks == [Check("\"select\" != ''", column="select")]


def test_transform_check_rewrite_does_not_rename_collations_or_cast_types(fresh_db):
    fresh_db.execute("""
        CREATE TABLE t (
            nocase TEXT,
            kind TEXT,
            other TEXT,
            CHECK(
                other COLLATE nocase != ''
                AND CAST(other AS kind) != ''
                AND nocase != ''
                AND kind != ''
            )
        )
    """)
    fresh_db.table("t").insert({"nocase": "n", "kind": "k", "other": "o"})
    fresh_db.table("t").transform(rename={"nocase": "label", "kind": "category"})
    check = fresh_db.table("t").checks[0].check
    assert "COLLATE nocase" in check
    assert "AS kind" in check
    assert "AND label != ''" in check
    assert "AND category != ''" in check


def test_transform_drops_check_owned_by_dropped_column(fresh_db):
    fresh_db.execute("""
        CREATE TABLE t (
            id INTEGER,
            obsolete INTEGER CHECK(obsolete > 0),
            CHECK(id > 0)
        )
    """)
    fresh_db.table("t").insert({"id": 1, "obsolete": 2})
    fresh_db.table("t").transform(drop={"obsolete"})
    assert fresh_db.table("t").checks == [Check("id > 0")]


def test_transform_refuses_to_drop_column_used_by_remaining_check(fresh_db):
    fresh_db.execute("""
        CREATE TABLE ranges (
            minimum INTEGER,
            maximum INTEGER,
            CHECK(minimum <= maximum)
        )
    """)
    ranges = fresh_db.table("ranges")
    ranges.insert({"minimum": 1, "maximum": 2})
    schema_before = ranges.schema
    with pytest.raises(
        TransformError,
        match="Cannot drop column 'maximum'.*CHECK constraint",
    ):
        ranges.transform(drop={"maximum"})
    assert ranges.schema == schema_before

```

### `tests/test_update.py`

```py
import collections
import json

import pytest

from sqlite_utils.db import NotFoundError


def test_update_rowid_table(fresh_db):
    table = fresh_db.table("table")
    rowid = table.insert({"foo": "bar"}).last_pk
    table.update(rowid, {"foo": "baz"})
    assert [{"foo": "baz"}] == list(table.rows)


def test_update_pk_table(fresh_db):
    table = fresh_db.table("table")
    pk = table.insert({"foo": "bar", "id": 5}, pk="id").last_pk
    assert 5 == pk
    table.update(pk, {"foo": "baz"})
    assert [{"id": 5, "foo": "baz"}] == list(table.rows)


def test_update_compound_pk_table(fresh_db):
    table = fresh_db.table("table")
    pk = table.insert({"id1": 5, "id2": 3, "v": 1}, pk=("id1", "id2")).last_pk
    assert (5, 3) == pk
    table.update(pk, {"v": 2})
    assert [{"id1": 5, "id2": 3, "v": 2}] == list(table.rows)


@pytest.mark.parametrize(
    "pk,update_pk",
    (
        (None, 2),
        (None, None),
        ("id1", None),
        ("id1", 4),
        (("id1", "id2"), None),
        (("id1", "id2"), 4),
        (("id1", "id2"), (4, 5)),
    ),
)
def test_update_invalid_pk(fresh_db, pk, update_pk):
    table = fresh_db.table("table")
    table.insert({"id1": 5, "id2": 3, "v": 1}, pk=pk)
    with pytest.raises(NotFoundError):
        table.update(update_pk, {"v": 2})


def test_update_alter(fresh_db):
    table = fresh_db.table("table")
    rowid = table.insert({"foo": "bar"}).last_pk
    table.update(rowid, {"new_col": 1.2}, alter=True)
    assert [{"foo": "bar", "new_col": 1.2}] == list(table.rows)
    # Let's try adding three cols at once
    table.update(
        rowid,
        {"str_col": "str", "bytes_col": b"\xa0 has bytes", "int_col": -10},
        alter=True,
    )
    assert [
        {
            "foo": "bar",
            "new_col": 1.2,
            "str_col": "str",
            "bytes_col": b"\xa0 has bytes",
            "int_col": -10,
        }
    ] == list(table.rows)


def test_update_alter_with_special_column_characters(fresh_db):
    # With double-quote escaping, columns with special characters are now valid
    table = fresh_db.table("table")
    rowid = table.insert({"foo": "bar"}).last_pk
    table.update(rowid, {"new_col[abc]": 1.2}, alter=True)
    assert list(table.rows) == [{"foo": "bar", "new_col[abc]": 1.2}]


def test_update_with_no_values_sets_last_pk(fresh_db):
    table = fresh_db.table("dogs", pk="id")
    table.insert_all([{"id": 1, "name": "Cleo"}, {"id": 2, "name": "Pancakes"}])
    table.update(1)
    assert table.last_pk == 1
    table.update(2)
    assert table.last_pk == 2
    with pytest.raises(NotFoundError):
        table.update(3)


@pytest.mark.parametrize(
    "data_structure",
    (
        ["list with one item"],
        ["list with", "two items"],
        {"dictionary": "simple"},
        {"dictionary": {"nested": "complex"}},
        collections.OrderedDict(
            [
                ("key1", {"nested": "complex"}),
                ("key2", "foo"),
            ]
        ),
        [{"list": "of"}, {"two": "dicts"}],
    ),
)
def test_update_dictionaries_and_lists_as_json(fresh_db, data_structure):
    fresh_db.table("test").insert({"id": 1, "data": ""}, pk="id")
    fresh_db.table("test").update(1, {"data": data_structure})
    row = fresh_db.execute("select id, data from test").fetchone()
    assert row[0] == 1
    assert data_structure == json.loads(row[1])

```

### `tests/test_upsert.py`

```py
import pytest

from sqlite_utils import Database
from sqlite_utils.db import PrimaryKeyRequired


@pytest.mark.parametrize("use_old_upsert", (False, True))
def test_upsert(use_old_upsert):
    db = Database(memory=True, use_old_upsert=use_old_upsert)
    table = db.table("table")
    table.insert_all([{"id": 1, "name": "Cleo"}], pk="id", replace=True)
    table.upsert({"id": 1, "age": 5}, pk="id", alter=True)
    assert list(table.rows) == [{"id": 1, "name": "Cleo", "age": 5}]
    assert table.last_pk == 1


def test_upsert_all(fresh_db):
    table = fresh_db.table("table")
    table.upsert_all([{"id": 1, "name": "Cleo"}, {"id": 2, "name": "Nixie"}], pk="id")
    table.upsert_all([{"id": 1, "age": 5}, {"id": 2, "age": 5}], pk="id", alter=True)
    assert list(table.rows) == [
        {"id": 1, "name": "Cleo", "age": 5},
        {"id": 2, "name": "Nixie", "age": 5},
    ]
    assert table.last_pk is None


def test_upsert_all_single_column(fresh_db):
    table = fresh_db.table("table")
    table.upsert_all([{"name": "Cleo"}], pk="name")
    assert list(table.rows) == [{"name": "Cleo"}]
    assert table.pks == ["name"]


def test_upsert_all_not_null(fresh_db):
    # https://github.com/simonw/sqlite-utils/issues/538
    fresh_db.table("comments").upsert_all(
        [{"id": 1, "name": "Cleo"}],
        pk="id",
        not_null=["name"],
    )
    assert list(fresh_db.table("comments").rows) == [{"id": 1, "name": "Cleo"}]


def test_upsert_error_if_no_pk(fresh_db):
    table = fresh_db.table("table")
    with pytest.raises(PrimaryKeyRequired):
        table.upsert_all([{"id": 1, "name": "Cleo"}])
    with pytest.raises(PrimaryKeyRequired):
        table.upsert({"id": 1, "name": "Cleo"})


@pytest.mark.parametrize("use_old_upsert", (False, True))
def test_upsert_empty_record_errors(use_old_upsert):
    db = Database(memory=True, use_old_upsert=use_old_upsert)
    table = db.table("table")
    table.insert({"id": 1, "name": "Cleo"}, pk="id")
    with pytest.raises(PrimaryKeyRequired):
        table.upsert({}, pk="id")
    with pytest.raises(PrimaryKeyRequired):
        table.upsert_all([{}, {}], pk="id")
    # No rows can have been inserted
    assert table.count == 1


@pytest.mark.parametrize("use_old_upsert", (False, True))
def test_upsert_missing_pk_value_errors(use_old_upsert):
    db = Database(memory=True, use_old_upsert=use_old_upsert)
    table = db.table("table")
    table.insert({"id": 1, "name": "Cleo"}, pk="id")
    # Records that omit the pk column entirely
    with pytest.raises(PrimaryKeyRequired):
        table.upsert_all([{"name": "Pancakes"}, {"name": "Marnie"}], pk="id")
    # A record with an explicit None pk value can never conflict
    with pytest.raises(PrimaryKeyRequired):
        table.upsert({"id": None, "name": "Pancakes"}, pk="id")
    assert list(table.rows) == [{"id": 1, "name": "Cleo"}]


def test_upsert_missing_compound_pk_value_errors(fresh_db):
    table = fresh_db.table("table")
    table.insert({"a": "x", "b": "y", "v": 1}, pk=("a", "b"))
    # Missing one component of the detected compound primary key
    with pytest.raises(PrimaryKeyRequired):
        table.upsert({"a": "x", "v": 2})
    assert list(table.rows) == [{"a": "x", "b": "y", "v": 1}]


def test_upsert_error_if_existing_table_has_no_pk(fresh_db):
    table = fresh_db.create_table("table", {"id": int, "name": str})
    with pytest.raises(PrimaryKeyRequired):
        table.upsert({"id": 1, "name": "Cleo"})


@pytest.mark.parametrize("use_old_upsert", (False, True))
def test_upsert_uses_compound_pk_from_existing_table(use_old_upsert):
    # https://github.com/simonw/sqlite-utils/issues/629
    db = Database(memory=True, use_old_upsert=use_old_upsert)
    db.execute("""
        create table summary (
            Source text,
            Object text,
            Category text,
            Count integer,
            primary key (Source, Object, Category)
        )
        """)
    table = db.table("summary")
    table.upsert(
        {
            "Source": "Client A",
            "Object": "Accounts",
            "Category": "All",
            "Count": 3,
        }
    )
    assert table.last_pk == ("Client A", "Accounts", "All")
    table.upsert(
        {
            "Source": "Client A",
            "Object": "Accounts",
            "Category": "All",
            "Count": 4,
        }
    )
    assert list(table.rows) == [
        {
            "Source": "Client A",
            "Object": "Accounts",
            "Category": "All",
            "Count": 4,
        }
    ]


def test_upsert_with_hash_id(fresh_db):
    table = fresh_db.table("table")
    table.upsert({"foo": "bar"}, hash_id="pk")
    assert [{"pk": "a5e744d0164540d33b1d7ea616c28f2fa97e754a", "foo": "bar"}] == list(
        table.rows
    )
    assert "a5e744d0164540d33b1d7ea616c28f2fa97e754a" == table.last_pk


@pytest.mark.parametrize("hash_id", (None, "custom_id"))
def test_upsert_with_hash_id_columns(fresh_db, hash_id):
    table = fresh_db.table("table")
    table.upsert({"a": 1, "b": 2, "c": 3}, hash_id=hash_id, hash_id_columns=("a", "b"))
    assert list(table.rows) == [
        {
            hash_id or "id": "4acc71e0547112eb432f0a36fb1924c4a738cb49",
            "a": 1,
            "b": 2,
            "c": 3,
        }
    ]
    assert table.last_pk == "4acc71e0547112eb432f0a36fb1924c4a738cb49"
    table.upsert({"a": 1, "b": 2, "c": 4}, hash_id=hash_id, hash_id_columns=("a", "b"))
    assert list(table.rows) == [
        {
            hash_id or "id": "4acc71e0547112eb432f0a36fb1924c4a738cb49",
            "a": 1,
            "b": 2,
            "c": 4,
        }
    ]


def test_upsert_compound_primary_key(fresh_db):
    table = fresh_db.table("table")
    table.upsert_all(
        [
            {"species": "dog", "id": 1, "name": "Cleo", "age": 4},
            {"species": "cat", "id": 1, "name": "Catbag"},
        ],
        pk=("species", "id"),
    )
    assert table.last_pk is None
    table.upsert({"species": "dog", "id": 1, "age": 5}, pk=("species", "id"))
    assert ("dog", 1) == table.last_pk
    assert [
        {"species": "dog", "id": 1, "name": "Cleo", "age": 5},
        {"species": "cat", "id": 1, "name": "Catbag", "age": None},
    ] == list(table.rows)
    # .upsert_all() with a single item should set .last_pk
    table.upsert_all([{"species": "cat", "id": 1, "age": 5}], pk=("species", "id"))
    assert ("cat", 1) == table.last_pk

```

### `tests/test_utils.py`

```py
import csv
import io

import pytest

from sqlite_utils import utils


@pytest.mark.parametrize(
    "input,expected,should_be_is",
    [
        ({}, None, True),
        ({"foo": "bar"}, None, True),
        (
            {"content": {"$base64": True, "encoded": "aGVsbG8="}},
            {"content": b"hello"},
            False,
        ),
    ],
)
def test_decode_base64_values(input, expected, should_be_is):
    actual = utils.decode_base64_values(input)
    if should_be_is:
        assert actual is input
    else:
        assert actual == expected


@pytest.mark.parametrize(
    "size,expected",
    (
        (1, [["a"], ["b"], ["c"], ["d"]]),
        (2, [["a", "b"], ["c", "d"]]),
        (3, [["a", "b", "c"], ["d"]]),
        (4, [["a", "b", "c", "d"]]),
    ),
)
def test_chunks(size, expected):
    input = ["a", "b", "c", "d"]
    chunks = list(map(list, utils.chunks(input, size)))
    assert chunks == expected


def test_hash_record():
    expected = "d383e7c0ba88f5ffcdd09be660de164b3847401a"
    assert utils.hash_record({"name": "Cleo", "twitter": "CleoPaws"}) == expected
    assert (
        utils.hash_record(
            {"name": "Cleo", "twitter": "CleoPaws", "age": 7}, keys=("name", "twitter")
        )
        == expected
    )
    assert (
        utils.hash_record({"name": "Cleo", "twitter": "CleoPaws", "age": 7}) != expected
    )


def test_maximize_csv_field_size_limit():
    # Reset to default in case other tests have changed it
    csv.field_size_limit(utils.ORIGINAL_CSV_FIELD_SIZE_LIMIT)
    long_value = "a" * 131073
    long_csv = f"id,text\n1,{long_value}"
    fp = io.BytesIO(long_csv.encode("utf-8"))
    # Using rows_from_file should error
    with pytest.raises(csv.Error):
        rows, _ = utils.rows_from_file(fp, utils.Format.CSV)
        list(rows)
    # But if we call maximize_csv_field_size_limit() first it should be OK:
    utils.maximize_csv_field_size_limit()
    fp2 = io.BytesIO(long_csv.encode("utf-8"))
    rows2, _ = utils.rows_from_file(fp2, utils.Format.CSV)
    rows_list2 = list(rows2)
    assert len(rows_list2) == 1
    assert rows_list2[0]["id"] == "1"
    assert rows_list2[0]["text"] == long_value


@pytest.mark.parametrize(
    "input,expected",
    (
        ({"foo": {"bar": 1}}, {"foo_bar": 1}),
        ({"foo": {"bar": [1, 2, {"baz": 3}]}}, {"foo_bar": [1, 2, {"baz": 3}]}),
        ({"foo": {"bar": 1, "baz": {"three": 3}}}, {"foo_bar": 1, "foo_baz_three": 3}),
    ),
)
def test_flatten(input, expected):
    assert utils.flatten(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    (
        ([], []),
        (["id", "name"], ["id", "name"]),
        (["id", "id"], ["id", "id_2"]),
        (["id", "id", "id"], ["id", "id_2", "id_3"]),
        # A renamed duplicate must not clobber a real column called id_2
        (["id", "id", "id_2"], ["id", "id_3", "id_2"]),
        (["id_2", "id", "id"], ["id_2", "id", "id_3"]),
        (["id", "id", "id_2", "id_2"], ["id", "id_3", "id_2", "id_2_2"]),
    ),
)
def test_dedupe_keys(input, expected):
    assert utils.dedupe_keys(input) == expected

```

### `tests/test_wal.py`

```py
import pytest

from sqlite_utils import Database
from sqlite_utils.db import TransactionError


@pytest.fixture
def db_path_tmpdir(tmpdir):
    path = tmpdir / "test.db"
    db = Database(str(path))
    return db, path, tmpdir


def test_enable_disable_wal(db_path_tmpdir):
    db, _path, tmpdir = db_path_tmpdir
    assert len(tmpdir.listdir()) == 1
    assert "delete" == db.journal_mode
    assert "test.db-wal" not in [f.basename for f in tmpdir.listdir()]
    db.enable_wal()
    assert "wal" == db.journal_mode
    db.table("test").insert({"foo": "bar"})
    assert "test.db-wal" in [f.basename for f in tmpdir.listdir()]
    db.disable_wal()
    assert "delete" == db.journal_mode
    assert "test.db-wal" not in [f.basename for f in tmpdir.listdir()]


def test_enable_wal_inside_transaction_raises(db_path_tmpdir):
    db, _path, _tmpdir = db_path_tmpdir
    db.table("test").insert({"id": 1}, pk="id")
    with pytest.raises(TransactionError), db.atomic():
        db.table("test").insert({"id": 2}, pk="id")
        db.enable_wal()
    # The atomic() block must have rolled back cleanly and the
    # journal mode must be unchanged
    assert db.journal_mode == "delete"
    assert [r["id"] for r in db.table("test").rows] == [1]


def test_disable_wal_inside_transaction_raises(db_path_tmpdir):
    db, _path, _tmpdir = db_path_tmpdir
    db.enable_wal()
    db.table("test").insert({"id": 1}, pk="id")
    with pytest.raises(TransactionError), db.atomic():
        db.table("test").insert({"id": 2}, pk="id")
        db.disable_wal()
    assert db.journal_mode == "wal"
    assert [r["id"] for r in db.table("test").rows] == [1]


def test_ensure_autocommit_on(db_path_tmpdir):
    db, _path, _tmpdir = db_path_tmpdir
    previous_isolation_level = db.conn.isolation_level
    assert previous_isolation_level is not None
    with db.ensure_autocommit_on():
        # isolation_level of None means driver-level autocommit mode
        assert db.conn.isolation_level is None
    # Restored afterwards
    assert db.conn.isolation_level == previous_isolation_level


def test_enable_wal_noop_inside_transaction_is_allowed(db_path_tmpdir):
    # Calling enable_wal() when WAL is already enabled is a no-op,
    # so it is fine inside a transaction
    db, _path, _tmpdir = db_path_tmpdir
    db.enable_wal()
    with db.atomic():
        db.table("test").insert({"id": 1}, pk="id")
        db.enable_wal()
    assert [r["id"] for r in db.table("test").rows] == [1]


def test_ensure_autocommit_on_inside_transaction_raises(db_path_tmpdir):
    # Setting isolation_level commits any pending transaction as a side
    # effect, silently breaking the caller's rollback guarantee - so
    # entering autocommit mode with a transaction open is an error
    db, _path, _tmpdir = db_path_tmpdir
    db.table("test").insert({"id": 1}, pk="id")
    db.begin()
    db.execute("insert into test (id) values (2)")
    with pytest.raises(TransactionError), db.ensure_autocommit_on():
        pass
    # The transaction is still open and can still be rolled back
    assert db.conn.in_transaction
    db.rollback()
    assert [r["id"] for r in db.table("test").rows] == [1]

```
