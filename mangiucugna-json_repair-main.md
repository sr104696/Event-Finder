# mangiucugna/json_repair@main

- Files included: 85
- Files skipped: 2
- Total size: 500.7 KB
- Estimated tokens: ~126,125

## Directory Structure

```
├── .agents
│   ├── skills
│   │   └── docs-demo-local-test
│   │       ├── agents
│   │       │   └── openai.yaml
│   │       └── SKILL.md
│   └── specs
│       └── docs-demo-ui
│           └── SPEC.md
├── .github
│   ├── ISSUE_TEMPLATE
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   └── feature_request.yml
│   ├── workflows
│   │   ├── mypy.yml
│   │   ├── pytest.yml
│   │   ├── python-package.yml
│   │   ├── python-publish.yml
│   │   ├── pythonanywhere-sync.yml
│   │   └── ruff.yml
│   ├── dependabot.yml
│   ├── FUNDING.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── docs
│   ├── __init__.py
│   ├── app.py
│   ├── index.html
│   ├── index.js
│   ├── index.zh.html
│   └── styles.css
├── examples
│   ├── __init__.py
│   ├── chinese_llm_output.py
│   ├── fastapi_app.py
│   ├── pydantic_schema.py
│   ├── README.md
│   ├── repair_llm_output.py
│   └── stream_stable.py
├── src
│   └── json_repair
│       ├── parse_string_helpers
│       │   ├── __init__.py
│       │   ├── object_value_context.py
│       │   ├── parse_boolean_or_null.py
│       │   └── parse_json_llm_block.py
│       ├── utils
│       │   ├── __init__.py
│       │   ├── constants.py
│       │   ├── json_context.py
│       │   ├── object_comparer.py
│       │   ├── pattern_properties.py
│       │   └── string_file_wrapper.py
│       ├── __init__.py
│       ├── __main__.py
│       ├── json_parser.py
│       ├── json_repair.py
│       ├── parse_array.py
│       ├── parse_comment.py
│       ├── parse_number.py
│       ├── parse_object.py
│       ├── parse_string.py
│       ├── parser_parenthesized.py
│       ├── parser_schema.py
│       ├── py.typed
│       └── schema_repair.py
├── tests
│   ├── utils
│   │   ├── __init__.py
│   │   ├── test_pattern_properties.py
│   │   └── test_string_file_wrapper.py
│   ├── __init__.py
│   ├── invalid.json
│   ├── profiler.py
│   ├── test_docs_app_schema.py
│   ├── test_json_repair.py
│   ├── test_parse_array.py
│   ├── test_parse_comment.py
│   ├── test_parse_number.py
│   ├── test_parse_object.py
│   ├── test_parse_string.py
│   ├── test_performance.py
│   ├── test_repair_json_cli.py
│   ├── test_repair_json_from_file.py
│   ├── test_schema_guided_parse.py
│   ├── test_schema_parser_paths.py
│   ├── test_schema_repairer.py
│   ├── test_strict_mode.py
│   ├── test_type_inference.py
│   └── valid.json
├── .gitignore
├── .pre-commit-config.yaml
├── AGENTS.md
├── banner.png
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── README.zh.md
├── SECURITY.md
└── uv.lock
```

## Code Digest

### `.agents/skills/docs-demo-local-test/agents/openai.yaml`

```yaml
interface:
  display_name: "Docs Demo Local Test"
  short_description: "Validate docs demo locally before deploys"
  default_prompt: "Run local docs demo API+UI and verify schema behavior against local code."

```

### `.agents/skills/docs-demo-local-test/SKILL.md`

```md
---
name: docs-demo-local-test
description: Test the docs JSON repair demo against local backend changes before publishing. Use this when modifying docs/app.py or docs UI files and you need local end-to-end verification.
---

# Docs Demo Local Test

## Overview

Use this workflow to validate docs demo behavior with local code only, without relying on the deployed PythonAnywhere API. This is the default verification path for `docs/app.py`, `docs/index.js`, `docs/index.html`, `docs/index.zh.html`, and `docs/styles.css` changes.

## Workflow

1. Start the local demo API server:
```bash
UV_CACHE_DIR=/tmp/uv-cache uv run --with flask --with flask-cors python docs/app.py
```
2. Start the local static site server:
```bash
python3 -m http.server 4173 --directory docs
```
3. Open `http://127.0.0.1:4173/index.html`.
4. In browser devtools, patch `fetch` so the page hits local API instead of PythonAnywhere:
```javascript
() => {
  const target = "https://mangiucugna.pythonanywhere.com/api/repair-json";
  const local = "http://127.0.0.1:5000/api/repair-json";
  const originalFetch = window.fetch.bind(window);
  window.fetch = (input, init) => {
    let nextInput = input;
    if (typeof input === "string" && input === target) {
      nextInput = local;
    } else if (input instanceof Request && input.url === target) {
      nextInput = new Request(local, input);
    }
    return originalFetch(nextInput, init);
  };
  return "fetch patched";
}
```
5. Run a schema coercion check:
- Input JSON: `{"value":"1",}`
- Schema: `{"type":"object","properties":{"value":{"type":"integer"}},"required":["value"]}`
- Expected output JSON: `{"value": 1}`
- Expected log contains: `Coerced string to integer`
6. Confirm network request target is local:
- `POST http://127.0.0.1:5000/api/repair-json`
7. Capture screenshot if needed.
8. Stop both local servers with `Ctrl+C`.

## Troubleshooting

- If `uv run` fails with cache permission errors, rerun with `UV_CACHE_DIR=/tmp/uv-cache`.
- If Flask modules are missing, keep using `uv run --with flask --with flask-cors ...`.
- If output still matches production behavior, the fetch patch did not apply; reload and patch again before typing input.

```

### `.agents/specs/docs-demo-ui/SPEC.md`

```md
# Demo UI Test Spec

Status: Active

## Overview

- This spec defines when the docs demo needs browser-level validation and what a comprehensive run must prove.
- It applies only to the demo site:
  - `docs/app.py`
  - `docs/index.js`
  - `docs/index.html`
  - `docs/index.zh.html`
  - `docs/styles.css`
- It complements, but does not replace, repo-wide validation such as `uv run pytest` and `pre-commit run --all-files`.
- The intended style is spec-first and agent-executable: the decision to test, the required workflow, and the acceptance criteria must be explicit enough that an agent can follow them without improvising policy.
- The repo already has a dedicated skill for local demo verification:
  - `.agents/skills/docs-demo-local-test/SKILL.md`
- When this spec calls for a demo UI test, that skill is the required entrypoint for local setup and baseline verification.

## Requirements

- The agent MUST choose one of three demo validation levels for every task that touches the demo site:
  - `Level 0`: no demo UI test
  - `Level 1`: local smoke test
  - `Level 2`: comprehensive local UI test
- The agent MUST use `Level 0` when the task does not affect the demo site.
- The agent MUST use `Level 1` for narrow, low-risk demo changes such as copy-only or small CSS-only edits.
- The agent MUST use `Level 2` when any of the following is true:
  - `docs/index.js` changed
  - URL, history, hash/query parsing, local storage, clipboard, reload, or share-link behavior changed
  - schema input, schema mode, or client-side validation behavior changed
  - locale switching or localized UI behavior changed
  - `docs/app.py` changed in a way that affects demo requests or responses
  - the user explicitly asks for UI testing
  - a demo-site bug is being fixed or investigated
  - a docs demo change is being prepared for release and confidence matters
- The agent MUST use Chrome MCP for `Level 1` and `Level 2` browser verification.
- The agent MUST use `.agents/skills/docs-demo-local-test/SKILL.md` as the setup guide for `Level 1` and `Level 2`.
- The agent MUST run demo UI tests against the local demo API and local static site, not the deployed site, unless the user explicitly asks otherwise.
- The agent MUST run `Level 2` in a fresh isolated browser context so prior local storage, stale requests, and previous test state do not contaminate results.
- The agent MUST patch browser `fetch` to target `http://127.0.0.1:5000/api/repair-json` before testing request-driven behavior.
- The agent MUST verify, during `Level 1` and `Level 2`, that at least one request actually hits the local API target.
- The agent MUST verify the visible local docs URL after any hydration or editing flow; tests for URL behavior are incomplete if they only inspect rendered content.
- The agent MUST treat large-example share behavior as a first-class contract when URL or sharing code changes.
- The agent MUST explicitly report any skipped required scenario in the final response.

## Design

### Test Levels

- `Level 0`
  - No browser work.
  - Typical cases:
    - parser-only or library-only changes under `src/` or `tests/`
    - packaging or release-only changes
    - Markdown-only changes outside the demo UI

- `Level 1`
  - Run the repo-local demo flow from `.agents/skills/docs-demo-local-test/SKILL.md`.
  - Minimum smoke coverage:
    1. Start the local docs API:
       - `UV_CACHE_DIR=/tmp/uv-cache uv run --with flask --with flask-cors python docs/app.py`
    2. Start the local static site:
       - `python3 -m http.server 4173 --directory docs`
    3. Open `http://127.0.0.1:4173/index.html` in Chrome MCP.
    4. Patch `fetch` to target the local API.
    5. Run the baseline schema coercion case:
       - Input JSON: `{"value":"1",}`
       - Schema: `{"type":"object","properties":{"value":{"type":"integer"}},"required":["value"]}`
       - Expected output contains `"value": 1`
       - Expected log contains `Coerced string to integer`
    6. Confirm the request target is `POST http://127.0.0.1:5000/api/repair-json`

- `Level 2`
  - Use the same local-server setup as `Level 1`.
  - Run in a fresh isolated Chrome MCP context.
  - The following matrix is required.

### Comprehensive Matrix

1. Baseline schema-guided repair
   - Run the same coercion case as the smoke test.
   - Confirm the local API request body contains both `malformedJSON` and `schema`.
   - Confirm the response body matches the repaired object and logs.

2. Client-side validation
   - Invalid schema text:
     - enter malformed schema JSON
     - confirm the UI shows the client-side schema error
     - confirm no demo API request is sent
   - Invalid schema mode:
     - if the mode is manipulated to an unsupported value, confirm the UI reports the mode error and does not send the request
   - Salvage without schema:
     - set `schemaRepairMode` to `salvage` with no schema
     - confirm the UI reports the missing-schema error
     - confirm no request is sent

3. Draft persistence
   - Enter non-empty input and optional schema.
   - Confirm draft state is written to local storage.
   - Reload the page.
   - Confirm the input and schema rehydrate from local storage.
   - Confirm the visible page URL reflects the current state as a compressed hash permalink.

4. Small share-link flow
   - Use a small reproducible example.
   - Click the share-link button.
   - Confirm the clipboard write succeeds or the UI reports success.
   - Read the copied URL when possible.
   - Open the copied URL in a fresh isolated context.
   - Confirm input and schema hydrate correctly.
   - Confirm the visible URL remains a usable compressed hash permalink after hydration.

5. Large share-state flow
   - Use a realistically large payload and a matching schema.
   - The example MUST not be a toy payload. It SHOULD resemble actual demo usage:
     - nested objects and arrays
     - long string fields such as explanations or model output
     - enough size to exceed the readable plain-URL path
     - schema present, not omitted
   - Confirm the page remains usable and the visible URL stays as a compressed hash permalink during editing.
   - Use the share-link button.
   - Confirm the large example follows the intended large-share behavior:
     - if large share links are supported, the copied link is produced in the documented large-share format and can be reopened
     - if large share links are intentionally unsupported, the UI clearly says so and does not poison the visible URL
   - If a large link is copied, open it in a fresh isolated context and confirm:
     - state hydrates correctly
     - the local API receives the request with schema included
     - the visible URL remains a usable compressed hash permalink after hydration
   - This scenario is mandatory whenever URL, share, history, compression, storage, or clipboard behavior changed.

6. Legacy-link compatibility
   - If older share-link formats are still supported, open at least one legacy link.
   - Confirm state hydrates correctly.
   - Confirm the page rewrites the visible URL into the current compressed hash format after hydration.

7. Chinese-page smoke
   - Open `http://127.0.0.1:4173/index.zh.html`.
   - Confirm:
     - the page loads
     - inputs are present
     - share/status copy is rendered in Chinese
     - there is no obvious broken layout or missing control
   - This remains a smoke check unless the bug specifically targets localization.

### Evidence

- A comprehensive run MUST capture enough evidence to audit the result.
- Capture at least:
  - one screenshot of a repaired state
  - one screenshot or network capture showing the large-share case
  - the exact local API request URL
  - the local API request body for at least one schema-guided call
  - any copied share-URL length or share-format details when share behavior is under test
- Save screenshots to a local temporary path and report those paths in the final response.

### Cleanup

- Stop both local servers after the run.

### Reporting

- The final response for a demo UI run should include:
  - whether the run was `Level 1` or `Level 2`
  - whether Chrome MCP was used
  - whether the API target was local
  - which required scenarios passed
  - which required scenarios failed or were left unverified
  - screenshot paths, if captured

### Maintenance

- Update this spec whenever any of the following changes:
  - the demo share-state format
  - the required local-server commands
  - the expected behavior for large examples
  - the minimum comprehensive test matrix
  - the browser tool or local validation workflow

```

### `.github/dependabot.yml`

```yml
version: 2
updates:
  - package-ecosystem: "uv"
    directory: "/"
    schedule:
      interval: "weekly"
    cooldown:
      default-days: 7
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    cooldown:
      default-days: 7

```

### `.github/FUNDING.yml`

```yml
# These are supported funding model platforms

github: mangiucugna

```

### `.github/ISSUE_TEMPLATE/bug_report.yml`

```yml
name: Bug Report
description: File a bug report.
title: "[Bug]: "
labels: ["bug"]
assignees:
  - mangiucugna
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  - type: input
    id: version
    attributes:
      label: Version of the library
      description: Please test with latest before reporting a bug
    validations:
      required: true
  - type: textarea
    id: description
    attributes:
      label: Describe the bug
      description: Describe the bug in detail
    validations:
      required: true
  - type: textarea
    id: reproduce
    attributes:
      label: How to reproduce
      description: A step-by-step guide on how to reproduce
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
      description: A clear and concise description of what you expected to happen
    validations:
      required: true

```

### `.github/ISSUE_TEMPLATE/config.yml`

```yml
blank_issues_enabled: false

```

### `.github/ISSUE_TEMPLATE/feature_request.yml`

```yml
name: Feature Request
description: File a feature request
title: "[Feature Request]: "
labels: ["feature"]
assignees:
  - mangiucugna
body:
  - type: markdown
    attributes:
      value: |
        Please test this feature does not exist in the latest before reporting a bug
  - type: textarea
    id: description
    attributes:
      label: Describe the solution you'd like
      description: A clear and concise description of what you want to happen.
    validations:
      required: true
  - type: textarea
    id: reproduce
    attributes:
      label: Context
      description: Why is this feature important for you?
    validations:
      required: true

```

### `.github/PULL_REQUEST_TEMPLATE.md`

```md
## Proposed changes

Describe the big picture of your changes here to communicate to the maintainers why we should accept this pull request. If it fixes a bug or resolves a feature request, be sure to link to that issue.

## Types of changes

What types of changes does your code introduce?
_Put an `x` in the boxes that apply_

- [ ] Bugfix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Minor Update (if none of the other choices apply)

## Checklist

- [ ] I have read the [CONTRIBUTING](https://github.com/mangiucugna/json_repair/blob/master/CONTRIBUTING.md) doc
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] I have run pre-commit and unit tests and all pass locally with my changes

## Further comments

If this is a relatively large or complex change, kick off the discussion by explaining why you chose the solution you did and what alternatives you considered, etc...

```

### `.github/workflows/mypy.yml`

```yml
name: Mypy Type Check

permissions:
  contents: read

on:
  workflow_dispatch:
  pull_request:

jobs:
  type-check:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1

    - name: Install the latest version of uv
      uses: astral-sh/setup-uv@20cfd1bf945f4377ade1205e4dbc17946fc9a30d
      with:
        activate-environment: true

    - name: Run mypy
      run: uv run --no-default-groups --group typecheck --frozen mypy src/

    - name: Run ty
      run: uv run --no-default-groups --group typecheck --group test --frozen ty check src/ tests/

```

### `.github/workflows/pytest.yml`

```yml
name: Pytest and Coverage

permissions:
  contents: read

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
    - master

jobs:
  pytest:
    name: Pytest and Coverage
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
    - name: Set up Python
      uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97
      with:
        python-version: '3.13'    # or match your `.python-version`

    - name: Install the latest version of uv
      uses: astral-sh/setup-uv@20cfd1bf945f4377ade1205e4dbc17946fc9a30d
      with:
        activate-environment: true

    - name: Run pytest
      run: PYTHONPATH=. uv run --no-default-groups --group test --group schema --frozen coverage run -m pytest

    - name: Run coverage
      run: PYTHONPATH=. uv run --no-default-groups --group test --group schema --frozen coverage report -m --fail-under=100

```

### `.github/workflows/python-package.yml`

```yml
# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python package

on:
  workflow_dispatch:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
      # https://github.com/actions/python-versions/blob/main/versions-manifest.json
        python-version: ["3.10", "3.11", "3.12", "3.13", "3.14", "3.15.0-beta.3"]

    steps:
    - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install the latest version of uv
      uses: astral-sh/setup-uv@20cfd1bf945f4377ade1205e4dbc17946fc9a30d
      with:
        activate-environment: true
    - name: Test with pytest
      run: |
        uv run --no-default-groups --group test --frozen pytest tests/test_json_repair.py

```

### `.github/workflows/python-publish.yml`

```yml
# This workflow will upload the package to PyPi when a release is created
# It uses the trusted publisher authentication model, no more secrets and api keys

name: Upload Python Package

on:
  release:
    types: [published]

permissions:
  contents: read

jobs:
  deploy:

    runs-on: ubuntu-latest

    permissions:
      # IMPORTANT: this permission is mandatory for Trusted Publishing
      id-token: write
    steps:
    - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1

    - name: Install the latest version of uv
      uses: astral-sh/setup-uv@20cfd1bf945f4377ade1205e4dbc17946fc9a30d
      with:
        activate-environment: true

    - name: Build package
      run: uv build
    - name: Check package metadata
      run: uvx twine check dist/*

    - name: Publish package distributions to PyPI
      uses: pypa/gh-action-pypi-publish@dc37677b2e1c63e2034f94d8a5b11f265b73ba33
      with:
        verbose: true

```

### `.github/workflows/pythonanywhere-sync.yml`

```yml
name: Sync PythonAnywhere Demo API

on:
  workflow_run:
    workflows: ["pages-build-deployment"]
    types: [completed]

permissions:
  contents: read

jobs:
  sync:
    name: Upload docs app.py to PythonAnywhere
    if: github.event.workflow_run.conclusion == 'success' && github.event.workflow_run.head_branch == 'main'
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1

    - name: Upload docs/app.py
      env:
        PA_API_TOKEN: ${{ secrets.PYTHONANYWHERE_API_TOKEN }}
        PA_HOST: "www.pythonanywhere.com"
        PA_PATH: "/home/mangiucugna/json_repair/app.py"
        PA_USERNAME: "mangiucugna"
      run: |
        set -euo pipefail
        curl --fail-with-body --silent --show-error \
          -X POST "https://${PA_HOST}/api/v0/user/${PA_USERNAME}/files/path${PA_PATH}" \
          -H "Authorization: Token ${PA_API_TOKEN}" \
          -F "content=@docs/app.py"

    - name: Reload PythonAnywhere web app
      env:
        PA_API_TOKEN: ${{ secrets.PYTHONANYWHERE_API_TOKEN }}
        PA_HOST: "www.pythonanywhere.com"
        PA_USERNAME: "mangiucugna"
        PA_WEBAPP_DOMAIN: "mangiucugna.pythonanywhere.com"
      run: |
        set -euo pipefail
        curl --fail-with-body --silent --show-error \
          -X POST "https://${PA_HOST}/api/v0/user/${PA_USERNAME}/webapps/${PA_WEBAPP_DOMAIN}/reload/" \
          -H "Authorization: Token ${PA_API_TOKEN}"

```

### `.github/workflows/ruff.yml`

```yml
name: Ruff Lint and Format

permissions:
  contents: read

on:
  workflow_dispatch:
  pull_request:

jobs:
  ruff:
    name: Ruff Lint and Format
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1

    - name: Install Ruff
      uses: astral-sh/ruff-action@278981a28ce3188b1e39527901f38254bf3aac89

    - name: Run Ruff Format
      run: ruff format --check --diff

```

### `.gitignore`

```gitignore
.benchmarks
.DS_Store
.venv
.vscode
__pycache__
.gitattributes
.pytest_cache
.coverage
.mypy_cache
build/
dist/
src/json_repair.egg-info/
htmlcov/
.ruff_cache
.cache

```

### `.pre-commit-config.yaml`

```yaml
repos:
- repo: local
  hooks:
  - id: uv-lock-upgrade
    name: Run uv lock --upgrade
    entry: uv lock --upgrade
    language: system
    pass_filenames: false
  - id: pre-commit autoupdate
    name: autoupdate pre-commit
    entry: env -u GIT_INDEX_FILE pre-commit autoupdate
    language: system
    pass_filenames: false
- repo: https://github.com/mangiucugna/gha-updater-pre-commit
  rev: v0.1
  hooks:
  - id: gha-update
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.16.4
  hooks:
    # Run the linter.
    - id: ruff-check
      args: [--fix]
      types: [python]
    # Run the formatter.
    - id: ruff-format
      types: [python]
- repo: local
  hooks:
  - id: mypy
    name: mypy
    entry: uv run mypy src/
    language: system
    pass_filenames: false
    types: [python]
  - id: ty
    name: ty
    entry: uv run ty check src/ tests/
    language: system
    pass_filenames: false
    types: [python]
  - id: run-tests
    name: run tests
    entry: uv run coverage run -m pytest
    language: system
    pass_filenames: false
    types: [python]
  - id: check-coverage
    name: Check Coverage
    entry: uv run coverage report -m --fail-under=100
    language: system
    pass_filenames: false
    types: [python]
- repo: https://github.com/semgrep/pre-commit
  rev: "v1.174.0"
  hooks:
    - id: semgrep
      args:
        - --config
        - p/ci
        - --error
        - --skip-unknown-extensions
        - --metrics
        - 'off'
- repo: https://github.com/Yelp/detect-secrets
  rev: "v1.5.0"
  hooks:
  - id: detect-secrets

```

### `AGENTS.md`

```md
# Repo Notes for Codex

## Environment
- Use the uv-managed environment at `.venv`; install dev dependencies with `uv sync --group dev`.
- Prefer `uv run ...` for Python tooling.
- Dependency groups live in `pyproject.toml`; update `uv.lock` when dependencies change.

## Validation
- Run the full test suite with `uv run pytest`.
- Run the full hook stack with `pre-commit run --all-files`.
- The hook stack may rewrite `uv.lock` or `.pre-commit-config.yaml`; if hook-managed files change during commit flows, restage the resulting updates instead of repeatedly restoring them.
- Keep CI's direct `ruff format` invocation aligned with the Python-only `ruff-format` pre-commit hook; Markdown is globally excluded because documentation code examples are not formatter input.

## Release And Packaging
- Project version lives in `pyproject.toml` under `[project].version`; use semantic versioning, with patch bumps for bug fixes.
- Keep `CITATION.cff` aligned with the released version metadata in `pyproject.toml`.
- Keep `MANIFEST.in` pruning `tests` so test modules are not shipped in the sdist.
- In `[tool.setuptools.package-data]`, use the real package key `json_repair` so `py.typed` remains included.
- Run `uvx twine check dist/*` after building and before publishing.

## Docs
- Keep `README.zh.md` aligned with `README.md` when behavior or contributor guidance changes.
- `README.md` is the PyPI long description via `pyproject.toml`; avoid relative file or image links there.
- Keep docs demo share state in the URL hash, not query params.

## Durable Implementation Notes
- Keep valid-JSON fast paths on the standard library path; `strict=True` must not second-guess inputs that `json.loads` already accepts.
- Treat `skip_json_loads=True` as an explicit opt-out for inputs already known to be invalid; do not assume behavior must match the stdlib-preserving path for valid JSON.
- `load(fd)` should behave like `json.load(fd)` and repair from the descriptor's current position.
- When adding repair heuristics, keep `strict=True` conservative and emit parser logs for automatic corrections.
- When a schema is provided, apply schema repair and validation for both valid and invalid JSON inputs.
- Keep schema-guided dispatch centralized in `JSONParser.parse_json(schema, path)`.
- `patternProperties` matching is intentionally limited to a safe subset; do not execute user-supplied regexes.
- Preserve schema dict identity in `SchemaRepairer.resolve_schema` whenever possible so validator caching remains effective.
- When validating a detached `anyOf` or `oneOf` branch, retain the original root schema's resolver scope so root-relative `$ref` values can resolve `$defs`.
- `schema_repair_mode` supports only `standard` and opt-in `salvage`; salvage may recover strongly evidenced structural mismatches, but must not silently coerce or infer semantic property renames (for example, `results` to `patterns`).
- For sequential top-level fragments, salvage may skip candidates that fail schema repair or validation and return the first schema-valid fragment; never select an item from an actual top-level JSON array.
- Treat user-supplied schemas as an attacker-controlled input surface: deep nesting in schema normalization, validation, and repair paths needs an explicit depth limit or controlled `ValueError`, not an uncaught `RecursionError`.

## Refactor Pitfalls
- In `repair_json`, keep a single shared output-finalization path for logging, `return_objects`, empty-string handling, and `json.dumps`.
- Parser refactors are sensitive to context lifetimes and heuristic branch ordering; preserve malformed-input behavior when restructuring `parse_string` or `parse_object`.
- Recognize unquoted literals only as complete tokens followed by a JSON separator or end-of-input; support case-insensitive `none` as null, but keep quoted values and other barewords as strings.
- Treat comma-separated parenthesized sequences as Python-style tuples that normalize to arrays, while preserving a single parenthesized value as a scalar; Python-style literals are supported only within arrays, objects, and tuples, not as bare top-level values.
- Preserve bare quotes inside compact regex character classes such as `['"]` and `[^'"]`; do not let them split the enclosing JSON value into separate top-level elements.
- For an object value beginning with a doubled quote, retain the second quote only when non-whitespace inner content and a distinct valid outer terminator evidence a quoted span; preserve ordinary redundant-leading-quote and doubled-ending normalization.
- When an object property contains an unclosed array of scalar values followed by a quoted `key: value` member, close the array and resume the enclosing object; preserve direct-array and pre-scalar missing-object recovery (`["key": "value"] -> [{"key": "value"}]`).
- Top-level raw decoding may discard a valid prefix only when non-comma garbage follows; preserve complete-input heuristics and defer comma-prefixed continuations to structural object repair.
- Performance regressions often hide in repeated `parse_string` lookahead scans on long malformed object values; include cases with many commas or `}` characters before a far quote, and retain only inputs with a meaningful baseline slowdown (roughly one second or more).
- Normalize top-level `RecursionError` into `ValueError`.

```

### `CITATION.cff`

```cff
cff-version: 1.2.0
message: "If you use this software, please cite it using the metadata from this file."
type: software
title: "json_repair"
authors:
- family-names: "Baccianella"
  given-names: "Stefano"
  orcid: "https://orcid.org/0009-0005-7654-4471"
version: "0.63.4"
date-released: 2026-08-25
license: "MIT"
abstract: "A Python package to repair broken JSON strings, including malformed JSON commonly produced by LLMs."
keywords:
  - "JSON"
  - "repair"
  - "LLM"
  - "parser"
repository-code: "https://github.com/mangiucugna/json_repair"
repository-artifact: "https://pypi.org/project/json-repair/"
url: "https://github.com/mangiucugna/json_repair"

```

### `CODE_OF_CONDUCT.md`

```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### `CONTRIBUTING.md`

```md
# How to contribute
Please make sure to make a change grounded in the reality of production code and not based on theoretical issues that might never arises. The code is complex already as it is.

## Step 1. Open an Issue to describe what you intend to do
So that everyone is aware of the intention before getting a surprise PR

## Step 2. Work in a branch
Make sure to work in a branch to make it easier to create a new PR.

**Important: Update the unit tests each time!**
We use TDD for this project.

## Step 3. Run pre-commit
Install the dev dependencies with `uv sync --group dev`, then run `uv run pre-commit run --all-files`.
This will run all the necessary tests and linters, saving lots of time to the reviewers.

## Step 4. Open a PR to review
Refer the Issue number in your PR

```

### `docs/__init__.py`

```py
"""Docs application package marker for linting."""

```

### `docs/app.py`

```py
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

from json_repair import loads

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


@app.route("/api/repair-json", methods=["POST"])
def format_json():
    try:
        data = request.get_json()
        if not isinstance(data, dict):
            raise ValueError("Request JSON must be an object.")
        malformed_json = data.get("malformedJSON")
        if not isinstance(malformed_json, str):
            raise ValueError("malformedJSON must be a string.")

        schema = data.get("schema")
        if schema is not None and not isinstance(schema, (dict, bool)):
            raise ValueError("schema must be a JSON object or boolean.")
        schema_repair_mode = data.get("schemaRepairMode", "standard")
        if not isinstance(schema_repair_mode, str):
            raise ValueError("schemaRepairMode must be a string.")
        if schema_repair_mode not in ("standard", "salvage"):
            raise ValueError("schemaRepairMode must be 'standard' or 'salvage'.")
        if schema_repair_mode == "salvage" and schema is None:
            raise ValueError("schemaRepairMode='salvage' requires schema.")

        # Repair the malformed JSON
        loads_kwargs = {"logging": True, "schema_repair_mode": schema_repair_mode}
        if schema is not None:
            loads_kwargs["schema"] = schema
        parsed_json = loads(malformed_json, **loads_kwargs)

        return jsonify(parsed_json)
    except (BadRequest, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run()

```

### `docs/index.html`

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="google-site-verification" content="8U1Z8NsGTRyRhB9MJqZGREeby67Q4jv1Y82FMtwLjws" /> <!-- pragma: allowlist secret -->
        <title>JSON Repair & Schema Validator — Fix Broken JSON Online</title>
        <meta name="description" content="Repair malformed JSON online, validate with optional JSON Schema, and format output with json_repair. Fix syntax errors and enforce schema-guided types/defaults.">
        <meta name="keywords" content="json repair, json fixer, json validator, json schema validator, json schema validation, fix malformed json, json formatter, llm json, json linter">
        <meta name="robots" content="index, follow">
        <link rel="canonical" href="https://mangiucugna.github.io/json_repair/">
        <link rel="alternate" hreflang="en" href="https://mangiucugna.github.io/json_repair/">
        <link rel="alternate" hreflang="zh-CN" href="https://mangiucugna.github.io/json_repair/index.zh.html">
        <link rel="alternate" hreflang="x-default" href="https://mangiucugna.github.io/json_repair/">
        <meta property="og:type" content="website">
        <meta property="og:title" content="JSON Repair & Schema Validator — Fix Broken JSON Online">
        <meta property="og:description" content="Free online JSON repair, formatting, and JSON Schema validation. Paste malformed JSON and optionally enforce schema-guided fixes with full logs.">
        <meta property="og:url" content="https://mangiucugna.github.io/json_repair/">
        <meta property="og:image" content="https://raw.githubusercontent.com/mangiucugna/json_repair/main/banner.png">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="JSON Repair & Schema Validator — Fix Broken JSON Online">
        <meta name="twitter:description" content="Validate malformed JSON with optional JSON Schema, repair it, and format it directly in your browser.">
        <meta name="twitter:image" content="https://raw.githubusercontent.com/mangiucugna/json_repair/main/banner.png">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@exampledev/new.css@1.1.2/new.min.css">
        <link rel="stylesheet" href="styles.css">
        <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "WebSite",
                        "name": "JSON Repair Demo",
                        "url": "https://mangiucugna.github.io/json_repair/",
                        "description": "Free online JSON repair, formatting, and JSON Schema validation tool powered by the json_repair Python package.",
                        "inLanguage": "en",
                        "potentialAction": {
                            "@type": "SearchAction",
                            "target": "https://mangiucugna.github.io/json_repair/?json={json}",
                            "query-input": "required name=json"
                        }
                    },
                    {
                        "@type": "SoftwareApplication",
                        "name": "json_repair",
                        "applicationCategory": "DeveloperApplication",
                        "applicationSubCategory": "JSON validator, JSON Schema validator, and fixer",
                        "operatingSystem": "Any",
                        "softwareVersion": "0.55.0",
                        "description": "Python utility to repair malformed JSON strings and apply schema-guided validation/coercion for API payloads and LLM responses.",
                        "downloadUrl": "https://pypi.org/project/json-repair/",
                        "offers": {
                            "@type": "Offer",
                            "price": "0",
                            "priceCurrency": "USD"
                        },
                        "url": "https://github.com/mangiucugna/json_repair"
                    }
                ]
            }
        </script>
    </head>
    <body>
        <noscript>
            <div class="notice">JavaScript is required to repair and format JSON in real time.</div>
        </noscript>
        <div class="language-switch">
            <strong>English</strong> | <a href="index.zh.html" rel="alternate" hreflang="zh-CN">中文</a>
        </div>
        <div id="locale-banner" class="language-banner hidden" role="status" aria-live="polite">
            <span id="locale-text">We noticed your browser is in Chinese. Switch to the Chinese version?</span>
            <div class="banner-actions">
                <a id="locale-switch" class="button" href="index.zh.html" rel="alternate" hreflang="zh-CN">Switch to 中文</a>
                <button type="button" id="dismiss-locale">No thanks</button>
            </div>
        </div>
        <header>
            <p class="eyebrow">Open source · Free · No signup</p>
            <h1>JSON Repair & Schema Validation — fix malformed JSON online</h1>
            <p class="lede">Paste broken JSON (even messy LLM output), optionally provide a JSON Schema, and instantly get valid, formatted output with a detailed log of every fix.</p>
            <div class="hero-actions">
                <a class="button-like primary" href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">Star on GitHub</a>
                <a class="button-like secondary" href="https://github.com/mangiucugna/json_repair/issues/new/choose" target="_blank" rel="noopener">Share a bad sample</a>
            </div>
            <p class="hero-note">If this demo solves a real problem for you, a GitHub Star is the clearest way to help more people find it.</p>
        </header>
        <main>
            <section>
                <h2>What the JSON Repair demo does</h2>
                <ul>
                    <li>Repairs malformed JSON: fixes trailing commas, missing quotes, stray comments, and incomplete objects.</li>
                    <li>Validates with JSON Schema: enforce expected types, defaults, and structural constraints when schema guidance is provided.</li>
                    <li>Validates and formats: outputs pretty-printed JSON you can copy straight into your code or API calls.</li>
                    <li>Transparent logging: see every repair step and context so you can trust the output.</li>
                    <li>Built on <a href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">json_repair</a>, the Python package available on <a href="https://pypi.org/project/json-repair/" target="_blank" rel="noopener">PyPI</a>.</li>
                </ul>
                <p class="disclaimer">API is hosted on PythonAnywhere’s free tier; if you hit quota, try again later or run the package locally.</p>
            </section>
            <section class="how-to">
                <h2>How to repair JSON online</h2>
                <ol>
                    <li>Paste malformed JSON (from webhooks, logs, or LLM responses) into the left box.</li>
                    <li>Optionally paste a JSON Schema to validate/coerce fields (for example string-to-integer conversion).</li>
                    <li>We validate, repair, and format automatically as you type.</li>
                    <li>Copy the valid JSON on the right or review the “repair actions” log for debugging.</li>
                </ol>
            </section>
            <section>
                <h2>JSON Schema validation online</h2>
                <p>Use the optional JSON Schema input to validate repaired JSON against required properties, value types, and constraints before you copy results into production systems.</p>
                <ul>
                    <li>Useful for API contracts, typed pipelines, and AI extraction workflows.</li>
                    <li>Supports schema-guided coercion (for example, converting <code>"1"</code> into <code>1</code> for integer fields).</li>
                    <li>Keeps behavior transparent with repair logs that show what changed and where.</li>
                </ul>
            </section>
            <section class="feature-grid">
                <div>
                    <h3>Why developers use json_repair</h3>
                    <ul>
                        <li>Handles common AI issues: hallucinated text in JSON, wrong booleans/null, broken arrays.</li>
                        <li>Drop-in replacement for <code>json.loads()</code> when you need resilient parsing.</li>
                        <li>Ideal for webhook payloads, schema-validated pipelines, and prompt engineering workflows.</li>
                    </ul>
                </div>
                <div>
                    <h3>Prefer code?</h3>
                    <p>Install the package locally and bypass API limits.</p>
                    <pre><code>pip install json-repair
python -m json_repair</code></pre>
                </div>
            </section>
            <div class="container">
                <div class="textarea-container">
                    <label for="input-json">Input JSON (broken, partial, or LLM output)</label>
                    <textarea id="input-json" aria-label="Input JSON" placeholder="Paste malformed JSON here..."></textarea>
                    <p class="helper-text">Examples we fix: trailing commas, missing quotes, stray comments, invalid true/false/null, incomplete objects.</p>
                </div>
                <div class="textarea-container">
                    <label for="output-json">Repaired JSON (validated + formatted)</label>
                    <textarea id="output-json" aria-label="Repaired JSON" readonly placeholder="Formatted JSON will appear here..."></textarea>
                </div>
            </div>
            <section id="success-support" class="support-card hidden" aria-live="polite">
                <h2>Did this save you time?</h2>
                <p>If this repair solved a real problem, the fastest way to help is to star the repo, share it, or send a broken sample we can learn from.</p>
                <div class="support-actions">
                    <a class="button-like primary" href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">Star on GitHub</a>
                    <button type="button" id="copy-repo-link">Copy repo link</button>
                    <a class="button-like secondary" href="https://github.com/mangiucugna/json_repair/issues/new/choose" target="_blank" rel="noopener">Report a bad sample</a>
                </div>
                <p id="support-copy-status" class="helper-text support-status"></p>
                <p class="helper-text">If your team relies on it in production, GitHub Sponsors helps keep maintenance predictable.</p>
            </section>
            <div class="textarea-container schema-container">
                <label for="schema-json">Optional JSON Schema (object or boolean)</label>
                <textarea id="schema-json" aria-label="JSON Schema" placeholder='{"type":"object","properties":{"value":{"type":"integer"}},"required":["value"]}'></textarea>
                <label for="schema-repair-mode">Schema repair mode</label>
                <select id="schema-repair-mode" aria-label="Schema repair mode">
                    <option value="standard" selected>standard (default)</option>
                    <option value="salvage">salvage (best-effort array/object salvage)</option>
                </select>
                <p class="helper-text">Optional. Provide a JSON Schema to guide coercions, defaults, and validation. Leave empty to use normal repair mode.</p>
                <p class="schema-note">Use the share button to copy a reproducible permalink. The address bar updates live as you edit.</p>
                <div class="helper-actions">
                    <button type="button" id="copy-share-link">Copy share link</button>
                    <p id="share-copy-status" class="helper-text share-status" aria-live="polite"></p>
                </div>
            </div>
            <div class="textarea-container">
                <label for="log-output">Repair actions performed</label>
                <textarea id="log-output" aria-label="Repair actions log" readonly placeholder="Logs will appear here..."></textarea>
            </div>
            <section>
                <h2>FAQ: fixing JSON for production</h2>
                <div class="faq">
                    <h3>Does this work for AI/LLM responses?</h3>
                    <p>Yes. json_repair is tuned for messy model output: it removes prose, repairs syntax, and keeps structured data intact.</p>
                    <h3>Can I validate against a JSON Schema here?</h3>
                    <p>Yes. Paste a JSON Schema in the optional schema box to apply schema-guided validation and type coercion while repairing malformed JSON.</p>
                    <h3>Can I trust the repaired JSON?</h3>
                    <p>Every action is logged so you can review context before sending payloads to production systems.</p>
                    <h3>What if I need offline or private processing?</h3>
                    <p>Install the library locally (<code>pip install json-repair</code>) to repair sensitive JSON without hitting the public API.</p>
                    <h3>How do I report issues or request features?</h3>
                    <p>Open an issue on <a href="https://github.com/mangiucugna/json_repair/issues" target="_blank" rel="noopener">GitHub</a> and include a sample payload; this page URL is a permalink you can reference.</p>
                </div>
            </section>
        </main>
        <footer>
            <p><strong>Support:</strong> <a href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">Star the repo</a> · <a href="https://github.com/mangiucugna/json_repair/issues/new/choose" target="_blank" rel="noopener">Report a bad sample</a> · <a href="https://github.com/sponsors/mangiucugna" target="_blank" rel="noopener">Sponsor maintenance</a> · <strong>Source:</strong> <a href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">json_repair on GitHub</a></p>
        </footer>
        <script src="index.js"></script>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-B77ZM0PG9W"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-B77ZM0PG9W');
        </script>
        <script>
            (function() {
                const banner = document.getElementById('locale-banner');
                const dismissBtn = document.getElementById('dismiss-locale');
                const localeText = document.getElementById('locale-text');
                const localeSwitch = document.getElementById('locale-switch');
                if (!banner || !dismissBtn) return;
                const dismissed = localStorage.getItem('jsonRepairLocalePromptDismissed') === '1';
                const userLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
                if (!dismissed && userLang.startsWith('zh')) {
                    if (localeText) {
                        localeText.textContent = '检测到您的浏览器语言为中文，是否切换到中文版？';
                    }
                    if (localeSwitch) {
                        localeSwitch.textContent = '切换到中文版';
                    }
                    if (dismissBtn) {
                        dismissBtn.textContent = '暂不切换';
                        dismissBtn.setAttribute('aria-label', '暂不切换到中文版');
                    }
                    banner.classList.remove('hidden');
                }
                dismissBtn.addEventListener('click', () => {
                    banner.classList.add('hidden');
                    localStorage.setItem('jsonRepairLocalePromptDismissed', '1');
                });
            })();
        </script>
    </body>
</html>

```

### `docs/index.js`

```js
let timeoutId;
let controller;
const DEBOUNCE_MS = 500;
const API_URL = "https://mangiucugna.pythonanywhere.com/api/repair-json";
const DEFAULT_SCHEMA_MODE = 'standard';
const SALVAGE_SCHEMA_MODE = 'salvage';
const SCHEMA_REPAIR_MODES = new Set([DEFAULT_SCHEMA_MODE, SALVAGE_SCHEMA_MODE]);
const URL_STATE_HASH_KEY = 'jr';
const URL_STATE_VERSION = 'v1';
const RAW_URL_STATE_CODEC = 'u';
const DRAFT_STORAGE_KEY = 'jsonRepairDraft.v1';
const URL_STATE_CODECS = [
    { id: 'd', format: 'deflate' },
    { id: 'g', format: 'gzip' },
];
const inputEl = document.getElementById('input-json');
const schemaEl = document.getElementById('schema-json');
const modeEl = document.getElementById('schema-repair-mode');
const outputEl = document.getElementById('output-json');
const logEl = document.getElementById('log-output');
const successSupportEl = document.getElementById('success-support');
const copyRepoLinkBtn = document.getElementById('copy-repo-link');
const supportCopyStatusEl = document.getElementById('support-copy-status');
const copyShareLinkBtn = document.getElementById('copy-share-link');
const shareCopyStatusEl = document.getElementById('share-copy-status');
const isChinese = (document.documentElement.lang || '').toLowerCase().startsWith('zh');
const textEncoder = new TextEncoder();
const textDecoder = new TextDecoder();
const supportedURLStateCodec = getSupportedURLStateCodec();
const REPO_URL = "https://github.com/mangiucugna/json_repair/";
let urlUpdateSequence = 0;

const messages = isChinese
    ? {
        noRepairNeeded: "无需修复，输入已经是有效 JSON。",
        schemaParseError: "Schema 必须是有效的 JSON 文本。",
        schemaTypeError: "Schema 顶层只能是 JSON 对象或布尔值（true/false）。",
        schemaHint: "请修正 Schema 后重试；当前未向 API 发送请求。",
        schemaClientErrorPrefix: "Schema 输入错误：",
        schemaModeError: "Schema 修复模式只能是 standard 或 salvage。",
        schemaModeNeedsSchema: "salvage 模式必须提供 Schema。",
        formatErrorPrefix: "JSON 修复失败：",
        unexpectedResponse: "服务器返回了无法解析的响应。",
        httpErrorPrefix: "请求失败，状态码：",
        contextLabel: "上下文",
        messageLabel: "信息",
        supportCopySuccess: "仓库链接已复制，欢迎发给同事或朋友。",
        supportCopyUnavailable: "当前浏览器不支持自动复制，请手动复制仓库链接。",
        supportCopyFailure: "复制失败，请手动复制仓库链接。",
        shareCopySuccess: "分享链接已复制，可直接发给同事或贴到 Issue 里。",
        shareCopyUnavailable: "当前浏览器不支持自动复制分享链接。",
        shareCopyFailure: "生成或复制分享链接失败，请重试。",
        shareCopyEmpty: "先输入 JSON 或 Schema，再复制分享链接。",
    }
    : {
        noRepairNeeded: "Nothing to do, this was already valid JSON.",
        schemaParseError: "Schema must be valid JSON.",
        schemaTypeError: "Schema must be a top-level JSON object or boolean (true/false).",
        schemaHint: "Fix the schema and try again; no API request was sent.",
        schemaClientErrorPrefix: "Schema input error: ",
        schemaModeError: "Schema repair mode must be standard or salvage.",
        schemaModeNeedsSchema: "salvage mode requires a schema.",
        formatErrorPrefix: "Error formatting JSON: ",
        unexpectedResponse: "The server returned an unreadable response.",
        httpErrorPrefix: "Request failed with status ",
        contextLabel: "Context",
        messageLabel: "Message",
        supportCopySuccess: "Repository link copied. Share it with someone who needs it.",
        supportCopyUnavailable: "Clipboard access is unavailable. Copy the repository link manually.",
        supportCopyFailure: "Could not copy the repository link. Copy it manually instead.",
        shareCopySuccess: "Share link copied. Send it to someone who needs the exact same example.",
        shareCopyUnavailable: "Clipboard access is unavailable for share links in this browser.",
        shareCopyFailure: "Could not create or copy the share link. Try again.",
        shareCopyEmpty: "Enter JSON or a schema before copying a share link.",
    };

function setSupportVisibility(isVisible) {
    if (!successSupportEl) {
        return;
    }
    successSupportEl.classList.toggle('hidden', !isVisible);
}

function setSupportCopyStatus(message = '') {
    if (supportCopyStatusEl) {
        supportCopyStatusEl.textContent = message;
    }
}

function setShareCopyStatus(message = '') {
    if (shareCopyStatusEl) {
        shareCopyStatusEl.textContent = message;
    }
}

async function writeTextToClipboard(text) {
    if (!navigator.clipboard || typeof navigator.clipboard.writeText !== 'function') {
        return 'unavailable';
    }

    try {
        await navigator.clipboard.writeText(text);
        return 'success';
    } catch {
        return 'failure';
    }
}

async function copyRepositoryLink() {
    const result = await writeTextToClipboard(REPO_URL);
    if (result === 'success') {
        setSupportCopyStatus(messages.supportCopySuccess);
        return;
    }

    setSupportCopyStatus(
        result === 'unavailable'
            ? messages.supportCopyUnavailable
            : messages.supportCopyFailure
    );
}

function getSupportedURLStateCodec() {
    if (typeof CompressionStream !== 'function' || typeof DecompressionStream !== 'function') {
        return null;
    }

    for (const codec of URL_STATE_CODECS) {
        try {
            new CompressionStream(codec.format);
            new DecompressionStream(codec.format);
            return codec;
        } catch {
            continue;
        }
    }

    return null;
}

function encodeBase64URL(bytes) {
    let binary = '';
    const chunkSize = 0x8000;
    for (let index = 0; index < bytes.length; index += chunkSize) {
        const chunk = bytes.subarray(index, index + chunkSize);
        binary += String.fromCharCode(...chunk);
    }
    return btoa(binary)
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=+$/u, '');
}

function decodeBase64URL(value) {
    const padding = (4 - (value.length % 4)) % 4;
    const paddedValue = `${value}${'='.repeat(padding)}`
        .replace(/-/g, '+')
        .replace(/_/g, '/');
    const binary = atob(paddedValue);
    const bytes = new Uint8Array(binary.length);
    for (let index = 0; index < binary.length; index += 1) {
        bytes[index] = binary.charCodeAt(index);
    }
    return bytes;
}

async function transformBytes(bytes, streamFactory) {
    const stream = new Blob([bytes]).stream().pipeThrough(streamFactory());
    const buffer = await new Response(stream).arrayBuffer();
    return new Uint8Array(buffer);
}

async function compressURLState(rawBytes) {
    if (!supportedURLStateCodec) {
        return { codec: RAW_URL_STATE_CODEC, bytes: rawBytes };
    }

    const compressedBytes = await transformBytes(
        rawBytes,
        () => new CompressionStream(supportedURLStateCodec.format)
    );
    if (compressedBytes.length >= rawBytes.length) {
        return { codec: RAW_URL_STATE_CODEC, bytes: rawBytes };
    }

    return { codec: supportedURLStateCodec.id, bytes: compressedBytes };
}

function buildCleanURL() {
    const url = new URL(window.location.href);
    url.search = '';
    url.hash = '';
    return url;
}

function getCurrentState() {
    return {
        inputJSON: inputEl.value,
        schemaJSON: schemaEl ? schemaEl.value : '',
        schemaMode: modeEl ? modeEl.value : DEFAULT_SCHEMA_MODE,
    };
}

function buildURLState(inputJSON, schemaJSON, schemaMode) {
    const state = {};

    if (inputJSON !== '') {
        state.j = inputJSON;
    }
    if (schemaJSON.trim() !== '') {
        state.s = schemaJSON;
    }
    if (schemaMode !== DEFAULT_SCHEMA_MODE) {
        state.m = schemaMode;
    }

    return state;
}

function hasURLState(state) {
    return Object.keys(state).length > 0;
}

function hasStateContent(state) {
    return !!state && (
        state.inputJSON !== ''
        || state.schemaJSON.trim() !== ''
        || state.schemaMode !== DEFAULT_SCHEMA_MODE
    );
}

async function encodeURLState(state) {
    const rawBytes = textEncoder.encode(JSON.stringify(state));
    const { codec, bytes } = await compressURLState(rawBytes);
    return `${URL_STATE_VERSION}.${codec}.${encodeBase64URL(bytes)}`;
}

function parseURLState(state) {
    if (!state || typeof state !== 'object' || Array.isArray(state)) {
        return null;
    }

    return {
        inputJSON: typeof state.j === 'string' ? state.j : '',
        schemaJSON: typeof state.s === 'string' ? state.s : '',
        schemaMode: typeof state.m === 'string' && SCHEMA_REPAIR_MODES.has(state.m)
            ? state.m
            : DEFAULT_SCHEMA_MODE,
    };
}

async function decodeURLState(payload) {
    try {
        const parts = payload.split('.');
        if (parts.length !== 3) {
            return null;
        }

        const [version, codecId, encodedValue] = parts;
        if (version !== URL_STATE_VERSION || encodedValue === '') {
            return null;
        }

        let bytes = decodeBase64URL(encodedValue);
        if (codecId !== RAW_URL_STATE_CODEC) {
            const codec = URL_STATE_CODECS.find((candidate) => candidate.id === codecId);
            if (!codec || typeof DecompressionStream !== 'function') {
                return null;
            }
            bytes = await transformBytes(bytes, () => new DecompressionStream(codec.format));
        }

        return parseURLState(JSON.parse(textDecoder.decode(bytes)));
    } catch {
        return null;
    }
}

function getLegacyValueFromURL(param) {
    const urlParams = new URLSearchParams(window.location.search);
    const rawValue = urlParams.get(param);
    return rawValue ? decodeURIComponent(rawValue) : '';
}

function getLegacyStateFromURL() {
    return parseURLState({
        j: getLegacyValueFromURL('json'),
        s: getLegacyValueFromURL('schema'),
        m: getLegacyValueFromURL('schema_mode'),
    });
}

async function getStateFromURL() {
    const hashPrefix = `#${URL_STATE_HASH_KEY}=`;
    if (window.location.hash.startsWith(hashPrefix)) {
        const hashState = await decodeURLState(window.location.hash.slice(hashPrefix.length));
        if (hasStateContent(hashState)) {
            return hashState;
        }
    }

    const legacyState = getLegacyStateFromURL();
    return hasStateContent(legacyState) ? legacyState : null;
}

function getDraftState() {
    try {
        const serializedState = window.localStorage.getItem(DRAFT_STORAGE_KEY);
        if (!serializedState) {
            return null;
        }
        const draftState = parseURLState(JSON.parse(serializedState));
        return hasStateContent(draftState) ? draftState : null;
    } catch {
        return null;
    }
}

function persistDraftState(inputJSON, schemaJSON, schemaMode) {
    try {
        const nextState = buildURLState(inputJSON, schemaJSON, schemaMode);
        if (!hasURLState(nextState)) {
            window.localStorage.removeItem(DRAFT_STORAGE_KEY);
            return;
        }
        window.localStorage.setItem(DRAFT_STORAGE_KEY, JSON.stringify(nextState));
    } catch {
        return;
    }
}

async function buildShareURL(inputJSON, schemaJSON, schemaMode) {
    const state = buildURLState(inputJSON, schemaJSON, schemaMode);
    if (!hasURLState(state)) {
        return null;
    }

    const url = buildCleanURL();
    const encodedState = await encodeURLState(state);
    // Store shared state in the fragment so large payloads do not hit static-host query limits.
    url.hash = `${URL_STATE_HASH_KEY}=${encodedState}`;
    return url.toString();
}

async function updateURL(inputJSON, schemaJSON, schemaMode) {
    const requestId = ++urlUpdateSequence;
    const nextState = buildURLState(inputJSON, schemaJSON, schemaMode);
    const url = buildCleanURL();

    if (hasURLState(nextState)) {
        try {
            const encodedState = await encodeURLState(nextState);
            if (requestId !== urlUpdateSequence) {
                return;
            }
            url.hash = `${URL_STATE_HASH_KEY}=${encodedState}`;
        } catch {
            return;
        }
    }

    if (requestId !== urlUpdateSequence) {
        return;
    }

    window.history.replaceState({}, '', url);
}

async function copyShareLink() {
    const { inputJSON, schemaJSON, schemaMode } = getCurrentState();
    const state = buildURLState(inputJSON, schemaJSON, schemaMode);
    if (!hasURLState(state)) {
        setShareCopyStatus(messages.shareCopyEmpty);
        return;
    }

    let shareURL;
    try {
        shareURL = await buildShareURL(inputJSON, schemaJSON, schemaMode);
    } catch {
        setShareCopyStatus(messages.shareCopyFailure);
        return;
    }

    const result = await writeTextToClipboard(shareURL);
    if (result === 'success') {
        setShareCopyStatus(messages.shareCopySuccess);
        return;
    }

    setShareCopyStatus(
        result === 'unavailable'
            ? messages.shareCopyUnavailable
            : messages.shareCopyFailure
    );
}

function showClientError(message, details = '') {
    outputEl.value = message;
    logEl.value = details;
}

function formatLogs(logs) {
    if (!Array.isArray(logs) || logs.length === 0) {
        return messages.noRepairNeeded;
    }
    return logs
        .map((log) => `${messages.contextLabel}: ${log.context}\n${messages.messageLabel}: ${log.text}`)
        .join('\n\n');
}

function parseSchema(schemaText) {
    const trimmedSchema = schemaText.trim();
    if (trimmedSchema === '') {
        return { schema: undefined, error: null };
    }

    let parsedSchema;
    try {
        parsedSchema = JSON.parse(trimmedSchema);
    } catch {
        return { schema: undefined, error: messages.schemaParseError };
    }

    const topLevelType = typeof parsedSchema;
    const isValidTopLevel = (topLevelType === 'object' && parsedSchema !== null && !Array.isArray(parsedSchema))
        || topLevelType === 'boolean';
    if (!isValidTopLevel) {
        return { schema: undefined, error: messages.schemaTypeError };
    }

    return { schema: parsedSchema, error: null };
}

function parseSchemaRepairMode(modeText) {
    const trimmedMode = modeText.trim();
    if (trimmedMode === '') {
        return { schemaMode: DEFAULT_SCHEMA_MODE, error: null };
    }
    if (!SCHEMA_REPAIR_MODES.has(trimmedMode)) {
        return { schemaMode: DEFAULT_SCHEMA_MODE, error: messages.schemaModeError };
    }
    return { schemaMode: trimmedMode, error: null };
}

function handleInputChange() {
    const { inputJSON, schemaJSON, schemaMode } = getCurrentState();
    persistDraftState(inputJSON, schemaJSON, schemaMode);
    setShareCopyStatus('');
    void updateURL(inputJSON, schemaJSON, schemaMode);
    processInput(inputJSON, schemaJSON, schemaMode);
}

document.addEventListener('DOMContentLoaded', async () => {
    const urlState = await getStateFromURL();
    const draftState = urlState ? null : getDraftState();
    const initialState = urlState || draftState;
    const initialJSON = initialState ? initialState.inputJSON : '';
    const initialSchema = initialState ? initialState.schemaJSON : '';
    const initialSchemaMode = initialState ? initialState.schemaMode : DEFAULT_SCHEMA_MODE;
    const resolvedSchemaMode = SCHEMA_REPAIR_MODES.has(initialSchemaMode)
        ? initialSchemaMode
        : DEFAULT_SCHEMA_MODE;

    if (initialJSON !== '') {
        inputEl.value = initialJSON;
    }
    if (schemaEl && initialSchema !== '') {
        schemaEl.value = initialSchema;
    }
    if (modeEl) {
        modeEl.value = resolvedSchemaMode;
    }

    if (initialState) {
        persistDraftState(initialJSON, initialSchema, resolvedSchemaMode);
        void updateURL(initialJSON, initialSchema, resolvedSchemaMode);
    }

    if (initialJSON) {
        processInput(initialJSON, initialSchema, resolvedSchemaMode);
    }
});

inputEl.addEventListener('input', handleInputChange);
if (schemaEl) {
    schemaEl.addEventListener('input', handleInputChange);
}
if (modeEl) {
    modeEl.addEventListener('change', handleInputChange);
}
if (copyRepoLinkBtn) {
    copyRepoLinkBtn.addEventListener('click', () => {
        void copyRepositoryLink();
    });
}
if (copyShareLinkBtn) {
    copyShareLinkBtn.addEventListener('click', () => {
        void copyShareLink();
    });
}

function processInput(inputJSON, schemaJSON = '', schemaMode = DEFAULT_SCHEMA_MODE) {
    if (inputJSON.trim() === '') {
        outputEl.value = '';
        logEl.value = '';
        setSupportVisibility(false);
        setSupportCopyStatus('');
        return;
    }

    if (timeoutId) {
        clearTimeout(timeoutId);
    }

    if (controller) {
        controller.abort();
    }

    setSupportVisibility(false);
    setSupportCopyStatus('');

    const { schema, error } = parseSchema(schemaJSON);
    if (error) {
        showClientError(
            `${messages.schemaClientErrorPrefix}${error}`,
            messages.schemaHint
        );
        return;
    }
    const { schemaMode: parsedSchemaMode, error: schemaModeError } = parseSchemaRepairMode(schemaMode);
    if (schemaModeError) {
        showClientError(
            `${messages.schemaClientErrorPrefix}${schemaModeError}`,
            messages.schemaHint
        );
        return;
    }
    if (parsedSchemaMode === SALVAGE_SCHEMA_MODE && schema === undefined) {
        showClientError(
            `${messages.schemaClientErrorPrefix}${messages.schemaModeNeedsSchema}`,
            messages.schemaHint
        );
        return;
    }

    timeoutId = setTimeout(() => {
        controller = new AbortController();
        const requestBody = { malformedJSON: inputJSON };
        if (schema !== undefined) {
            requestBody.schema = schema;
        }
        requestBody.schemaRepairMode = parsedSchemaMode;

        fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody),
            signal: controller.signal
        })
        .then(async (response) => {
            let data;
            try {
                data = await response.json();
            } catch {
                throw new Error(messages.unexpectedResponse);
            }

            if (!response.ok) {
                if (data && typeof data.error === 'string') {
                    throw new Error(data.error);
                }
                throw new Error(`${messages.httpErrorPrefix}${response.status}`);
            }

            if (data && typeof data === 'object' && !Array.isArray(data) && typeof data.error === 'string') {
                throw new Error(data.error);
            }

            return data;
        })
        .then((data) => {
            let formattedJSON = data;
            let logs = [];
            if (Array.isArray(data)) {
                [formattedJSON, logs] = data;
            }

            outputEl.value = JSON.stringify(formattedJSON, null, 4);
            logEl.value = formatLogs(logs);
            setSupportVisibility(true);
            setSupportCopyStatus('');
        })
        .catch((error) => {
            if (error.name !== 'AbortError') {
                setSupportVisibility(false);
                showClientError(`${messages.formatErrorPrefix}${error.message}`);
            }
        });
    }, DEBOUNCE_MS);
}

```

### `docs/index.zh.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="google-site-verification" content="8U1Z8NsGTRyRhB9MJqZGREeby67Q4jv1Y82FMtwLjws" /> <!-- pragma: allowlist secret -->
        <title>JSON 修复器与 Schema 校验 — 在线修复损坏 JSON</title>
        <meta name="description" content="在线修复格式错误的 JSON，并使用可选 JSON Schema 做校验与类型约束。json_repair 演示支持语法修复、Schema 引导修复与格式化输出。">
        <meta name="keywords" content="json 修复,json 修复器,json 校验,json schema 校验,json schema 验证,json 修复工具,json 格式化,修复坏 json,大模型 json">
        <meta name="robots" content="index, follow">
        <link rel="canonical" href="https://mangiucugna.github.io/json_repair/index.zh.html">
        <link rel="alternate" hreflang="en" href="https://mangiucugna.github.io/json_repair/">
        <link rel="alternate" hreflang="zh-CN" href="https://mangiucugna.github.io/json_repair/index.zh.html">
        <link rel="alternate" hreflang="x-default" href="https://mangiucugna.github.io/json_repair/">
        <meta property="og:type" content="website">
        <meta property="og:title" content="JSON 修复器与 Schema 校验 — 在线修复损坏 JSON">
        <meta property="og:description" content="免费在线 JSON 修复、格式化与 JSON Schema 校验。粘贴有问题的 JSON，并可选提供 Schema 获取可追踪修复结果。">
        <meta property="og:url" content="https://mangiucugna.github.io/json_repair/index.zh.html">
        <meta property="og:image" content="https://raw.githubusercontent.com/mangiucugna/json_repair/main/banner.png">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="JSON 修复器与 Schema 校验 — 在线修复损坏 JSON">
        <meta name="twitter:description" content="在浏览器中修复损坏 JSON，并使用可选 JSON Schema 做校验与类型引导。">
        <meta name="twitter:image" content="https://raw.githubusercontent.com/mangiucugna/json_repair/main/banner.png">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@exampledev/new.css@1.1.2/new.min.css">
        <link rel="stylesheet" href="styles.css">
        <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "WebSite",
                        "name": "JSON Repair Demo",
                        "url": "https://mangiucugna.github.io/json_repair/index.zh.html",
                        "description": "json_repair Python 包的在线 JSON 修复、格式化与 JSON Schema 校验工具。",
                        "inLanguage": "zh-CN",
                        "potentialAction": {
                            "@type": "SearchAction",
                            "target": "https://mangiucugna.github.io/json_repair/index.zh.html?json={json}",
                            "query-input": "required name=json"
                        }
                    },
                    {
                        "@type": "SoftwareApplication",
                        "name": "json_repair",
                        "applicationCategory": "DeveloperApplication",
                        "applicationSubCategory": "JSON validator, JSON Schema validator, and fixer",
                        "operatingSystem": "Any",
                        "softwareVersion": "0.55.0",
                        "description": "修复格式错误 JSON 并支持 Schema 引导校验/类型转换的 Python 工具，适合 API 负载和大模型响应。",
                        "downloadUrl": "https://pypi.org/project/json-repair/",
                        "offers": {
                            "@type": "Offer",
                            "price": "0",
                            "priceCurrency": "USD"
                        },
                        "url": "https://github.com/mangiucugna/json_repair"
                    }
                ]
            }
        </script>
    </head>
    <body>
        <noscript>
            <div class="notice">需要启用 JavaScript 才能实时修复和格式化 JSON。</div>
        </noscript>
        <div class="language-switch">
            <a href="index.html">English</a> | <strong>中文</strong>
        </div>
        <header>
            <p class="eyebrow">开源 · 免费 · 无需注册</p>
            <h1>JSON 修复器与 Schema 校验 — 在线修复损坏 JSON</h1>
            <p class="lede">粘贴损坏的 JSON（包括大模型输出），并可选提供 JSON Schema，即可获得有效、格式化结果与每一步修复日志。</p>
            <div class="hero-actions">
                <a class="button-like primary" href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">去 GitHub 点 Star</a>
                <a class="button-like secondary" href="https://github.com/mangiucugna/json_repair/issues/new/choose" target="_blank" rel="noopener">提交坏样例</a>
            </div>
            <p class="hero-note">如果这个演示帮你解决了真实问题，给仓库点个 Star 是最直接、最有用的支持方式。</p>
        </header>
        <main>
            <section>
                <h2>这个演示能做什么</h2>
                <ul>
                    <li>修复常见错误：拖尾逗号、缺少引号、注释、未完成的对象/数组。</li>
                    <li>支持 JSON Schema 校验：在提供 Schema 时按字段类型、默认值和结构约束进行引导修复。</li>
                    <li>校验并格式化：输出可直接用于代码或 API 的漂亮 JSON。</li>
                    <li>透明日志：记录每一步修复，方便查看上下文。</li>
                    <li>基于 <a href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">json_repair</a> Python 包，已发布到 <a href="https://pypi.org/project/json-repair/" target="_blank" rel="noopener">PyPI</a>。</li>
                </ul>
                <p class="disclaimer">API 部署在 PythonAnywhere 免费配额上；如果频率过高可能限流，可稍后再试或本地运行包。</p>
            </section>
            <section class="how-to">
                <h2>如何在线修复 JSON</h2>
                <ol>
                    <li>将损坏的 JSON（来自 webhook、日志或大模型）粘贴到左侧。</li>
                    <li>可选粘贴 JSON Schema，用于字段校验与类型引导（例如字符串转整数）。</li>
                    <li>我们自动校验、修复并格式化。</li>
                    <li>复制右侧的有效 JSON，或查看“修复日志”用于调试。</li>
                </ol>
            </section>
            <section>
                <h2>在线 JSON Schema 校验</h2>
                <p>通过可选 Schema 输入框，你可以在修复 JSON 的同时校验必填字段、类型与结构约束，再将结果用于生产系统。</p>
                <ul>
                    <li>适合 API 合同校验、类型化数据管线和大模型结构化输出场景。</li>
                    <li>支持 Schema 引导的类型转换（例如把 <code>"1"</code> 转为整型 <code>1</code>）。</li>
                    <li>配合修复日志可追踪每一步变化，方便审计与调试。</li>
                </ul>
            </section>
            <section class="feature-grid">
                <div>
                    <h3>开发者为何选择 json_repair</h3>
                    <ul>
                        <li>处理大模型常见问题：输出混入文本、错误的 true/false/null、损坏的数组。</li>
                        <li>作为 <code>json.loads()</code> 的韧性替代，防止因格式错误而中断。</li>
                        <li>适合 webhook 负载、Schema 校验管线和提示工程工作流。</li>
                    </ul>
                </div>
                <div>
                    <h3>需要本地代码？</h3>
                    <p>安装包即可跳过 API 限制。</p>
                    <pre><code>pip install json-repair
python -m json_repair</code></pre>
                </div>
            </section>
            <div class="container">
                <div class="textarea-container">
                    <label for="input-json">输入 JSON（损坏、缺失或大模型输出）</label>
                    <textarea id="input-json" aria-label="输入 JSON" placeholder="在此粘贴损坏的 JSON..."></textarea>
                    <p class="helper-text">常见修复：拖尾逗号、缺少引号、注释、错误的 true/false/null、未完成对象。</p>
                </div>
                <div class="textarea-container">
                    <label for="output-json">修复后的 JSON（已校验与格式化）</label>
                    <textarea id="output-json" aria-label="修复后的 JSON" readonly placeholder="格式化后的 JSON 将显示在此..."></textarea>
                </div>
            </div>
            <section id="success-support" class="support-card hidden" aria-live="polite">
                <h2>这个结果帮到你了吗？</h2>
                <p>如果这次修复帮你省了时间，最有效的支持方式通常不是立刻赞助，而是先让更多人知道这个项目。</p>
                <div class="support-actions">
                    <a class="button-like primary" href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">去 GitHub 点 Star</a>
                    <button type="button" id="copy-repo-link">复制仓库链接</button>
                    <a class="button-like secondary" href="https://github.com/mangiucugna/json_repair/issues/new/choose" target="_blank" rel="noopener">提交坏样例</a>
                </div>
                <p id="support-copy-status" class="helper-text support-status"></p>
                <p class="helper-text">如果你的团队长期在生产环境使用它，再考虑 Sponsors 支持维护会更自然。</p>
            </section>
            <div class="textarea-container schema-container">
                <label for="schema-json">可选 JSON Schema（对象或布尔值）</label>
                <textarea id="schema-json" aria-label="JSON Schema" placeholder='{"type":"object","properties":{"value":{"type":"integer"}},"required":["value"]}'></textarea>
                <label for="schema-repair-mode">Schema 修复模式</label>
                <select id="schema-repair-mode" aria-label="Schema 修复模式">
                    <option value="standard" selected>standard（默认）</option>
                    <option value="salvage">salvage（尽力返回可用数组/对象）</option>
                </select>
                <p class="helper-text">可选。提供 JSON Schema 可引导类型转换、默认值填充和校验；留空则使用普通修复模式。</p>
                <p class="schema-note">使用下方按钮复制可复现实例链接；编辑过程中地址栏会实时更新。</p>
                <div class="helper-actions">
                    <button type="button" id="copy-share-link">复制分享链接</button>
                    <p id="share-copy-status" class="helper-text share-status" aria-live="polite"></p>
                </div>
            </div>
            <div class="textarea-container">
                <label for="log-output">修复步骤日志</label>
                <textarea id="log-output" aria-label="修复日志" readonly placeholder="日志将显示在此..."></textarea>
            </div>
            <section>
                <h2>常见问题</h2>
                <div class="faq">
                    <h3>能处理 AI / 大模型输出吗？</h3>
                    <p>可以。json_repair 针对混入文本和语法错误的输出进行了优化，尽量保留结构化数据。</p>
                    <h3>可以在这里做 JSON Schema 校验吗？</h3>
                    <p>可以。把 JSON Schema 粘贴到可选 Schema 输入框后，修复过程会同时执行 Schema 引导的校验和类型转换。</p>
                    <h3>修复后的 JSON 可靠吗？</h3>
                    <p>每一步修复都有日志，发送到生产系统前可先审核。</p>
                    <h3>需要离线或私有环境？</h3>
                    <p>本地安装（<code>pip install json-repair</code>）即可在私有环境修复敏感 JSON。</p>
                    <h3>如何反馈问题或提需求？</h3>
                    <p>在 <a href="https://github.com/mangiucugna/json_repair/issues" target="_blank" rel="noopener">GitHub</a> 提 Issue，并附示例负载；此页面 URL 可作为固定链接引用。</p>
                </div>
            </section>
        </main>
        <footer>
            <p><strong>这个工具帮到你了？</strong> <a href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">给仓库点 Star</a> · <a href="https://github.com/mangiucugna/json_repair/issues/new/choose" target="_blank" rel="noopener">提交坏样例</a> · <a href="https://github.com/sponsors/mangiucugna" target="_blank" rel="noopener">赞助维护</a> · <strong>源码：</strong> <a href="https://github.com/mangiucugna/json_repair/" target="_blank" rel="noopener">json_repair on GitHub</a></p>
            <p><a href="index.html" rel="alternate">Switch to English</a></p>
        </footer>
        <script src="index.js"></script>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-B77ZM0PG9W"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-B77ZM0PG9W');
        </script>
    </body>
</html>

```

### `docs/styles.css`

```css
body {
    max-width: 1100px;
    margin: 0 auto;
    padding: 20px;
}

header {
    margin-bottom: 24px;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.8rem;
    margin: 0 0 6px 0;
    color: #4c566a;
}

.lede {
    font-size: 1.1rem;
    color: #2e3440;
    margin-top: 8px;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 18px;
}

.hero-note {
    font-size: 0.95rem;
    color: #4b5563;
    margin-top: 10px;
    margin-bottom: 0;
}

.notice {
    background: #fef3c7;
    border: 1px solid #f59e0b;
    padding: 8px 12px;
    margin-bottom: 12px;
    border-radius: 6px;
}

.language-switch {
    display: flex;
    justify-content: flex-end;
    gap: 8px;
    font-size: 0.95rem;
    margin-bottom: 8px;
}

.language-banner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #ecfeff;
    border: 1px solid #06b6d4;
    padding: 10px 12px;
    border-radius: 8px;
    margin-bottom: 14px;
    gap: 12px;
}

.language-banner .button {
    background: #06b6d4;
    color: white;
    padding: 6px 10px;
    border-radius: 6px;
    text-decoration: none;
}

.banner-actions {
    display: flex;
    gap: 8px;
    align-items: center;
}

.banner-actions button {
    padding: 6px 10px;
}

.hidden {
    display: none;
}

section {
    border-bottom: solid 1px #d8dee9;
    padding-bottom: 14px;
    margin-bottom: 18px;
}

.how-to ol {
    padding-left: 20px;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 18px;
}

.disclaimer {
    font-size: 0.95rem;
    color: #6b7280;
}

.container {
    display: flex;
    width: 100%;
    gap: 16px;
    flex-wrap: wrap;
}

.textarea-container {
    flex: 1;
    min-width: 280px;
    display: flex;
    flex-direction: column;
}

.textarea-container label {
    font-weight: 600;
}

textarea {
    width: 100%;
    height: 400px;
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    box-sizing: border-box;
}

textarea:focus {
    outline: none;
    border-color: #4CAF50;
    box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
}

select {
    width: 100%;
    margin-top: 10px;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    box-sizing: border-box;
}

.helper-text {
    font-size: 0.9rem;
    color: #4b5563;
    margin-top: 6px;
}

.helper-actions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 10px 14px;
    margin-top: 10px;
}

.schema-container {
    margin-top: 4px;
}

#schema-json {
    height: 220px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

.schema-note {
    font-size: 0.9rem;
    color: #6b7280;
    margin-top: 6px;
    margin-bottom: 0;
}

#log-output {
    height: 200px;
}

.faq h3 {
    margin-bottom: 4px;
}

.faq p {
    margin-top: 0;
    margin-bottom: 12px;
}

.support-card {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    padding: 18px;
}

.support-card h2 {
    margin-top: 0;
    margin-bottom: 8px;
}

.support-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 14px 0 10px;
}

.button-like,
.support-actions button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 40px;
    padding: 8px 14px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    border: 1px solid #cbd5e1;
    background: white;
    color: #1f2937;
}

.button-like.primary {
    background: #0f766e;
    border-color: #0f766e;
    color: white;
}

.button-like.secondary,
.support-actions button {
    background: white;
    color: #1f2937;
}

.support-actions button {
    cursor: pointer;
    font-size: 1rem;
}

.support-status {
    min-height: 1.2em;
}

.share-status {
    min-height: 1.2em;
    margin: 0;
}

footer {
    margin-top: 24px;
}

@media (max-width: 900px) {
    body {
        padding: 16px;
    }

    textarea {
        height: 260px;
    }

    #schema-json {
        height: 220px;
    }
}

```

### `examples/__init__.py`

```py
"""Runnable integration examples for json_repair."""

```

### `examples/chinese_llm_output.py`

```py
"""Repair Chinese-language LLM output and preserve the original characters."""

from __future__ import annotations

import json
import sys

from json_repair import loads

LLM_OUTPUT = """
以下是整理后的结构化结果:

```json
{
  标题: "退款申请处理结果",
  "摘要": "客户确认已经收到退款",
  "标签": ["账单", "已解决",],
  "是否升级": false,
}
```

如果你需要, 我也可以补充英文摘要。
"""


def main() -> None:
    repaired = loads(LLM_OUTPUT)
    sys.stdout.write(json.dumps(repaired, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()

```

### `examples/fastapi_app.py`

```py
"""Repair and validate LLM output inside a FastAPI endpoint."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from json_repair import loads

app = FastAPI()


class IncomingLLMResponse(BaseModel):
    raw_output: str


class SupportTicket(BaseModel):
    customer_id: int
    sentiment: str
    summary: str
    tags: list[str] = Field(default_factory=list)


@app.post("/parse-ticket", response_model=SupportTicket)
def parse_ticket(body: IncomingLLMResponse) -> SupportTicket:
    try:
        repaired = loads(
            body.raw_output,
            skip_json_loads=True,
            schema=SupportTicket,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=f"Could not repair JSON payload: {exc}") from exc

    return SupportTicket.model_validate(repaired)

```

### `examples/pydantic_schema.py`

```py
"""Repair malformed JSON with Pydantic v2 schema guidance."""

from __future__ import annotations

import sys

from pydantic import BaseModel, Field

from json_repair import repair_json

BAD_OUTPUT = """
{
  "customer_id": "42",
  "sentiment": "positive",
  "summary": "Customer confirmed the fix worked",
  "tags": ,
}
"""


class SupportTicket(BaseModel):
    customer_id: int
    sentiment: str
    summary: str
    tags: list[str] = Field(default_factory=list)


def main() -> None:
    repaired = repair_json(
        BAD_OUTPUT,
        return_objects=True,
        schema=SupportTicket,
        skip_json_loads=True,
    )
    payload = SupportTicket.model_validate(repaired)
    sys.stdout.write(payload.model_dump_json(indent=2) + "\n")


if __name__ == "__main__":
    main()

```

### `examples/README.md`

```md
# Examples

These examples show how to use `json_repair` in common integration points without changing the library itself.

## Quick start

Run the standard-library-only examples with:

```bash
uv run python examples/repair_llm_output.py
uv run python examples/chinese_llm_output.py
uv run python examples/pydantic_schema.py
uv run python examples/stream_stable.py
```

The FastAPI example needs extra dependencies:

```bash
uv add --group dev fastapi uvicorn
uv run uvicorn examples.fastapi_app:app --reload
```

## Included examples

- [repair_llm_output.py](repair_llm_output.py): Repair JSON wrapped in markdown fences, comments, or extra prose from an LLM response.
- [chinese_llm_output.py](chinese_llm_output.py): Repair Chinese-language JSON while preserving non-Latin characters in the final output.
- [pydantic_schema.py](pydantic_schema.py): Use a Pydantic v2 model as schema guidance, then validate the repaired object.
- [stream_stable.py](stream_stable.py): Keep a stable best-effort JSON snapshot while a streamed response is still incomplete.
- [fastapi_app.py](fastapi_app.py): Repair and validate model output inside a FastAPI endpoint before returning a typed response.

```

### `examples/repair_llm_output.py`

```py
"""Repair JSON wrapped in extra prose from an LLM response."""

from __future__ import annotations

import json
import sys

from json_repair import loads

LLM_OUTPUT = """
I analyzed the ticket and extracted the fields you asked for.

```json
{
  customer_id: 42,
  "sentiment": "positive",
  "summary": "Customer confirmed the fix worked",
  "tags": ["billing", "vip",],
}
```

Let me know if you want the confidence score too.
"""


def main() -> None:
    repaired = loads(LLM_OUTPUT)
    sys.stdout.write(json.dumps(repaired, indent=2) + "\n")


if __name__ == "__main__":
    main()

```

### `examples/stream_stable.py`

```py
"""Keep a stable snapshot while a JSON response is still streaming."""

from __future__ import annotations

import json
import sys

from json_repair import repair_json

CHUNKS = [
    '{"items":[{"id":1,"name":"Ada"},',
    '{"id":2,"name":"Grace"},',
    '{"id":3,"name":"Linus"',
    '],"complete":tr',
    "ue}",
]


def main() -> None:
    partial = ""
    snapshots = []

    for chunk in CHUNKS:
        partial += chunk
        snapshots.append(repair_json(partial, return_objects=True, stream_stable=True))

    sys.stdout.write(json.dumps(snapshots, indent=2) + "\n")


if __name__ == "__main__":
    main()

```

### `LICENSE`

```
MIT License

Copyright (c) 2023 Stefano Baccianella

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

### `MANIFEST.in`

```in
prune tests

```

### `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
[project]
name = "json_repair"
version = "0.63.4"
license = "MIT"
license-files = ["LICENSE"]
authors = [
  { name="Stefano Baccianella", email="4247706+mangiucugna@users.noreply.github.com" },
]
description = "A package to repair broken json strings"
keywords = ["JSON", "REPAIR", "LLM", "PARSER"]
readme = "README.md"
requires-python = ">=3.10"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
[project.urls]
"Homepage" = "https://github.com/mangiucugna/json_repair/"
"Bug Tracker" = "https://github.com/mangiucugna/json_repair/issues"
"Live demo" = "https://mangiucugna.github.io/json_repair/"
[project.optional-dependencies]
# Skip Rust-backed schema extras on Python 3.15 prereleases until upstream wheels land.
schema = [
  "jsonschema>=4.21; python_full_version < '3.15.0a0' or python_full_version >= '3.15.0'",
  "pydantic>=2; python_full_version < '3.15.0a0' or python_full_version >= '3.15.0'",
]
[dependency-groups]
dev = [
    { include-group = "schema" },
    { include-group = "test" },
    { include-group = "typecheck" },
    "pre-commit",
]
schema = [
    "jsonschema",
    "pydantic",
]
test = [
    "coverage",
    "pytest",
    "pytest-benchmark",
]
typecheck = [
    "mypy",
    "ty",
]
[tool.pytest.ini_options]
pythonpath = [
  "."
]
[tool.coverage.run]
source = ["src"]
omit = [
    "*/.cursor/extensions/*",
    "*/pythonFiles/lib/python/*",
    "*/site-packages/*",
    "src/json_repair/__main__.py",
]
[tool.coverage.report]
include = [
    "src/json_repair/*",
]
exclude_also = [
    'def __repr__',
    'if self.debug:',
    'if settings.DEBUG',
    'raise AssertionError',
    'raise NotImplementedError',
    'if 0:',
    'if __name__ == .__main__.:',
    'if TYPE_CHECKING:',
    'class .*\bProtocol\):',
    '@(abc\.)?abstractmethod',
]
[tool.setuptools.package-data]
"json_repair" = ["py.typed"]
[tool.setuptools.packages.find]
where = ["src"]
[project.scripts]
json_repair = "json_repair.__main__:cli"
[tool.ruff]
# Same as Black.
indent-width = 4
line-length = 120
# Keep documentation code examples outside Ruff's formatter scope.
extend-exclude = ["*.md"]
# Assume Python 3.13
target-version = "py313"
[tool.ruff.lint]
# Read more here https://docs.astral.sh/ruff/rules/
# By default, Ruff enables Flake8's E and F rules
# FastAPI - FAST
# Flake8-no-pep420 - INP
# Flake8-bandit - S
# Flake8-bugbear – catches real-world Python footguns - B
# Flake8-builtins - A
# Flake8-comprehensions  - C4
# Flake8-blind-except - BLE
# Flake8-commas - COM
# Flake8-implicit-str-concat - ISC
# Flake8-print - T20
# Flake8-quotes - Q
# Flake8-raise - RSE
# Flake8-return - RET
# Flake8-tidy-imports - TID
# Flake8-type-checking - TC
# Flake8-unused-arguments - ARG
# Refurb - FURB
# Isort - I
# Mccabe – code complexity warnings - C90
# PEP 8 Naming convention - N
# Perflint - PERF
# Pygrep-hooks - PGH
# flake8-pie - PIE
# Flake8-use-pathlib - PTH
# Pycodestyle - E, W
# Pyflakes - F
# Pylint - PLC, PLE, PLR, PLW
# PyTest - PT
# Pyupgrade – safe modernization (e.g., str() → f"") - UP
# Ruff specific - RUF
# Simplifications (e.g., if x == True → if x) - SIM
select = ['A', 'ARG', 'B', 'BLE', 'C4', 'COM', 'C90', 'E', 'F', 'FURB', 'I', 'INP', 'ISC', 'N', 'PERF', 'PGH', 'PIE', 'PLC', 'PLE', 'PLW', 'PT', 'PTH', 'Q', 'RET', 'RSE', 'S', 'SIM', 'T20', 'TC', 'TID', 'UP', 'W']
# Only enable these RUF rules
extend-select = [
  "RUF001",  # ambiguous Unicode
  "RUF100",  # unused noqa
  "RUF012",  # mutable default arguments
  "RUF013",  # unnecessary super()
  "RUF016",  # unnecessary else after return (optional)
  "RUF018",  # unnecessary else after raise (optional)
  "RUF005",  # avoid list concatenation in membership checks
  "RUF010",  # prefer explicit conversion flags in f-strings
  "RUF019",  # prefer dict.get over redundant key checks
  "RUF022",  # keep __all__ sorted
  "RUF043",  # make pytest.raises regex intent explicit
  "TRY300",  # keep returns out of try blocks
]
ignore = [
  "S101",   # assert: Use of assert detected. We like assert
  "COM812", # Ruff: The following rule may cause conflicts when used with the formatter
  "E501",   # Line too long
  "C901",   # `function` is too complex
]
# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []
[tool.ruff.format]
# Like Black, use double quotes for strings.
quote-style = "double"

# Like Black, indent with spaces, rather than tabs.
indent-style = "space"

# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false

# Like Black, automatically detect the appropriate line ending.
line-ending = "auto"

[tool.ruff.lint.per-file-ignores]
# Explicit re-exports is fine in __init__.py, still a code smell elsewhere.
"__init__.py" = ["PLC0414"]
"src/json_repair/json_repair.py" = ["T201"]
"tests/profiler.py" = ["T201"]
[tool.mypy]
strict = true

```

### `README.md`

```md
[![PyPI](https://img.shields.io/pypi/v/json-repair)](https://pypi.org/project/json-repair/)
![Python version](https://img.shields.io/badge/python-3.10+-important)
[![PyPI downloads](https://img.shields.io/pypi/dm/json-repair)](https://pypi.org/project/json-repair/)
[![PyPI Downloads](https://static.pepy.tech/badge/json-repair)](https://pepy.tech/projects/json-repair)
[![Github Sponsors](https://img.shields.io/github/sponsors/mangiucugna)](https://github.com/sponsors/mangiucugna)
[![GitHub Repo stars](https://img.shields.io/github/stars/mangiucugna/json_repair?style=flat)](https://github.com/mangiucugna/json_repair/stargazers)

English | [中文](https://github.com/mangiucugna/json_repair/blob/main/README.zh.md)

# json_repair

Repair malformed JSON from LLMs, APIs, logs, and user input in Python.

- Fix missing quotes, commas, brackets, comments, stray prose, and truncated values.
- Use it as a drop-in fallback for `json.loads()` or as a schema-guided repair step.
- Install with `pip install json-repair` or try the [live demo](https://mangiucugna.github.io/json_repair/).

![banner](https://raw.githubusercontent.com/mangiucugna/json_repair/main/banner.png)

---

## Quick example

```python
import json_repair

bad_json = '{"users":[{"name":"Ada","role":"admin",}],"ok":true'
decoded_object = json_repair.loads(bad_json)

# {'users': [{'name': 'Ada', 'role': 'admin'}], 'ok': True}
```

If `json_repair` saves you time, [star the repository](https://github.com/mangiucugna/json_repair) so more people can find it.

---

# Demo
If you are unsure whether this library will fix your specific problem, or simply want your JSON validated online, try one of these:

- Live demo: https://mangiucugna.github.io/json_repair/
- Audio overview: [NotebookLM introduction](https://notebooklm.google.com/notebook/05312bb3-f6f3-4e49-a99b-bd51db64520b/audio)

## Premium sponsors
- [Icana-AI](https://github.com/Icana-AI) Makers of CallCoach, the world's best Call Centre AI Coach. Visit [https://www.icana.ai/](https://www.icana.ai/)
- [mjharte](https://github.com/mjharte)

---

# Think about sponsoring this library!
This library is free for everyone and is maintained as a side project, so if it helps your work, consider becoming a sponsor: https://github.com/sponsors/mangiucugna

---

# Motivation
Some LLMs are a bit iffy when it comes to returning well formed JSON data, sometimes they skip a parentheses and sometimes they add some words in it, because that's what an LLM does.
Luckily, the mistakes LLMs make are simple enough to be fixed without destroying the content.

I searched for a lightweight python package that was able to reliably fix this problem but couldn't find any.

*So I wrote one*

# Supported use cases

### Fixing Syntax Errors in JSON

- Missing quotes, misplaced commas, unescaped characters, and incomplete key-value pairs.
- Missing quotation marks, improperly formatted values (true, false, null), and repairs corrupted key-value structures.
- Python-style tuples: comma-separated parenthesized sequences become JSON arrays, while a single parenthesized value remains a scalar. Within arrays, objects, and tuples, `true`/`false`/`null` and `None` are recognized case-insensitively as JSON booleans or null.

### Repairing Malformed JSON Arrays and Objects

- Incomplete or broken arrays/objects by adding necessary elements (e.g., commas, brackets) or default values (null, "").
- The library can process JSON that includes extra non-JSON characters like comments or improperly placed characters, cleaning them up while maintaining valid structure.

### Auto-Completion for Missing JSON Values

- Automatically completes missing values in JSON fields with reasonable defaults (like empty strings or null), ensuring validity.

# How to use

Install the library with pip

    pip install json-repair

then you can use use it in your code like this

    from json_repair import repair_json

    good_json_string = repair_json(bad_json_string)
    # If the string was super broken this will return an empty string


You can use this library to completely replace `json.loads()`:

    import json_repair

    decoded_object = json_repair.loads(json_string)

or just

    import json_repair

    decoded_object = json_repair.repair_json(json_string, return_objects=True)

### Avoid this antipattern
Some users of this library adopt the following pattern:

    obj = {}
    try:
        obj = json.loads(string)
    except json.JSONDecodeError as e:
        obj = json_repair.loads(string)
        ...

This is wasteful because `json_repair` already does that strict `json.loads()` check for you by default. The normal flow is:

- try the built-in `json.loads()` / `json.load()` first
- if that succeeds, return the decoded object
- if that fails, run the repair parser

Use the default call unless you explicitly want to skip that initial validation step:

```python
import json_repair

decoded_object = json_repair.loads(json_string)
```

### Read json from a file or file descriptor

JSON repair provides also a drop-in replacement for `json.load()`:

    import json_repair

    try:
        file_descriptor = open(fname, 'rb')
    except OSError:
        ...

    with file_descriptor:
        decoded_object = json_repair.load(file_descriptor)

and another method to read from a file:

    import json_repair

    try:
        decoded_object = json_repair.from_file(json_file)
    except OSError:
        ...
    except IOError:
        ...

Keep in mind that the library will not catch any IO-related exception and those will need to be managed by you

### Non-Latin characters

When working with non-Latin characters (such as Chinese, Japanese, or Korean), you need to pass `ensure_ascii=False` to `repair_json()` in order to preserve the non-Latin characters in the output.

Here's an example using Chinese characters:

    repair_json("{'test_chinese_ascii':'统一码'}")

will return

    {"test_chinese_ascii": "\u7edf\u4e00\u7801"}

Instead passing `ensure_ascii=False`:

    repair_json("{'test_chinese_ascii':'统一码'}", ensure_ascii=False)

will return

    {"test_chinese_ascii": "统一码"}

### JSON dumps parameters

More in general, `repair_json` will accept all parameters that `json.dumps` accepts and just pass them through (for example indent)

### Performance considerations
By default, `json_repair` first tries the standard-library JSON loader and only falls back to the repair parser when strict JSON parsing fails.

If you already know the input is invalid JSON and want to skip that initial validation step, pass `skip_json_loads=True`:

    from json_repair import repair_json

    good_json_string = repair_json(bad_json_string, skip_json_loads=True)

This is an explicit tradeoff:

- default behavior: validate with stdlib JSON first, then repair only if needed
- `skip_json_loads=True`: skip the validation fast path and go straight to the repair parser

Important: `skip_json_loads=True` is only for inputs you already know are invalid. If you force already-valid JSON through the repair parser, `json_repair` may still "repair" it and can change the resulting structure or values. If you need valid JSON to be preserved as-is, keep `skip_json_loads=False`.

`json_repair` intentionally keeps the validation path on the standard library. It does not auto-detect or auto-use third-party JSON libraries, which keeps behavior predictable and avoids extra overhead on the common path.

Some rules of thumb to use:
- Setting `return_objects=True` will always be faster because the parser returns an object already and it doesn't have serialize that object to JSON
- `skip_json_loads=True` is faster only if you 100% know that the string is not a valid JSON
- `skip_json_loads=True` is not a "faster but equivalent" mode for valid JSON; it intentionally bypasses the stdlib success path, so valid inputs should use the default behavior
- If you are having issues with escaping pass the string as **raw** string like: `r"string with escaping\""`

### When to use your own JSON library

If you want non-stdlib JSON semantics or a different performance profile, use your preferred JSON library yourself instead of expecting `json_repair` to switch parsers automatically. `orjson` is a common example people ask about, and the same pattern applies to any other JSON library.

Recommended patterns:

Strict JSON first, repair only if needed:

```python
import json_repair

decoded_object = json_repair.loads(json_string)
```

Known-bad input, so skip the validation step:

```python
from json_repair import repair_json

decoded_object = repair_json(bad_json_string, return_objects=True, skip_json_loads=True)
```

`orjson` first, `json_repair` only as a fallback:

```python
import json_repair
import orjson

try:
    decoded_object = orjson.loads(json_string)
except orjson.JSONDecodeError:
    decoded_object = json_repair.loads(json_string, skip_json_loads=True)
```

### Strict mode

By default `json_repair` does its best to “fix” input, even when the JSON is far from valid.  
In some scenarios you want the opposite behavior and need the parser to error out instead of repairing; pass `strict=True` to `repair_json`, `loads`, `load`, or `from_file` to enable that mode:

```
from json_repair import repair_json

repair_json(bad_json_string, strict=True)
```

The CLI exposes the same behavior with `json_repair --strict input.json` (or piping data via stdin).

In strict mode the parser raises `ValueError` as soon as it encounters structural issues such as duplicate keys, missing `:` separators, empty keys/values introduced by stray commas, multiple top-level elements, or other ambiguous constructs. This is useful when you just need validation with friendlier error messages while still benefiting from json_repair’s resilience elsewhere in your stack.

Strict mode still honors `skip_json_loads=True`; combining them lets you skip the initial `json.loads` check but still enforce strict parsing rules.

### Schema-guided repairs

Schema-guided repairs are currently considered in beta. Bugs are to be expected.

You can guide repairs with a JSON Schema (or a Pydantic v2 model). When enabled, the parser will:

- Fill missing values (defaults, required fields).
- Coerce scalars where safe (e.g., `"1"` → `1` for integer fields, and `"yes"`/`"no"`/`1`/`0` for booleans).
- Drop properties/items that the schema disallows.

Schema mode can be selected with `schema_repair_mode`:

- `standard` (default): existing schema-guided behavior.
- `salvage`: includes `standard` and also:
  - drops invalid array items when individual items cannot be repaired;
  - maps arrays to objects by property order when schema/object shape is unambiguous.
  - unwraps a root single-item array to an object when the root schema expects an object (`[{...}] -> {...}`);
  - fills missing required fields only when a safe value can be inferred (`default`, `const`, first `enum`, or empty array/object when allowed by schema constraints).
  - for sequential top-level fragments, skips schema-invalid fragments and returns the first fragment that satisfies the schema.

This is especially useful when you need deterministic, schema-valid outputs for downstream validation, storage, or typed processing. If the input cannot be repaired to satisfy the schema, `json_repair` raises `ValueError`.

Install the optional dependencies:

    pip install 'json-repair[schema]'

(For CLI usage, you can also use `pipx install 'json-repair[schema]'`.)

When `schema` is provided, schema guidance is always applied (for both valid and invalid JSON). Schema guidance is mutually exclusive with `strict=True`.

```
from json_repair import repair_json

schema = {
    "type": "object",
    "properties": {"value": {"type": "integer"}},
    "required": ["value"],
}

repair_json('{"value": "1"}', schema=schema, return_objects=True)

repair_json(
    '{"items":[{"id":1,"score":85.6},{"id":2,"score":"N/A"}]}',
    schema={
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"id": {"type": "integer"}, "score": {"type": "number"}},
                    "required": ["id", "score"],
                },
            }
        },
        "required": ["items"],
    },
    schema_repair_mode="salvage",
    return_objects=True,
)
```

Pydantic v2 model example:

```
from pydantic import BaseModel, Field
from json_repair import repair_json


class Payload(BaseModel):
    value: int
    tags: list[str] = Field(default_factory=list)


repair_json(
    '{"value": "1", "tags": }',
    schema=Payload,
    skip_json_loads=True,
    return_objects=True,
)
```

### Use json_repair with streaming

Sometimes you are streaming some data and want to repair the JSON coming from it. Normally this won't work but you can pass `stream_stable` to `repair_json()` or `loads()` to make it work:

```
stream_output = repair_json(stream_input, stream_stable=True)
```

### More integration examples

If you want copy-paste examples for real applications, see [examples/README.md](https://github.com/mangiucugna/json_repair/blob/main/examples/README.md):

- [repair_llm_output.py](https://github.com/mangiucugna/json_repair/blob/main/examples/repair_llm_output.py) repairs markdown-wrapped or prose-wrapped model output.
- [pydantic_schema.py](https://github.com/mangiucugna/json_repair/blob/main/examples/pydantic_schema.py) uses a Pydantic v2 model as schema guidance.
- [stream_stable.py](https://github.com/mangiucugna/json_repair/blob/main/examples/stream_stable.py) keeps partial JSON stable during streaming.
- [fastapi_app.py](https://github.com/mangiucugna/json_repair/blob/main/examples/fastapi_app.py) drops the repair step into a FastAPI endpoint.

### Use json_repair from CLI

Install the library for command-line with:
```
pipx install json-repair
```
to know all options available:
```
$ json_repair -h
usage: json_repair [-h] [-i] [-o TARGET] [--ensure_ascii] [--indent INDENT]
                   [--skip-json-loads] [--schema SCHEMA] [--schema-model MODEL]
                   [--strict] [--schema-repair-mode {standard,salvage}] [filename]

Repair and parse JSON files.

positional arguments:
  filename              The JSON file to repair (if omitted, reads from stdin)

options:
  -h, --help            show this help message and exit
  -i, --inline          Replace the file inline instead of returning the output to stdout
  -o TARGET, --output TARGET
                        If specified, the output will be written to TARGET filename instead of stdout
  --ensure_ascii        Pass ensure_ascii=True to json.dumps()
  --indent INDENT       Number of spaces for indentation (Default 2)
  --skip-json-loads     Skip initial json.loads validation
  --schema SCHEMA       Path to a JSON Schema file that guides repairs
  --schema-model MODEL  Pydantic v2 model in 'module:ClassName' form that guides repairs
  --strict              Raise on duplicate keys, missing separators, empty keys/values, and similar structural issues instead of repairing them
  --schema-repair-mode {standard,salvage}
                        Schema repair mode: standard (default) or salvage (best-effort array/object salvage)
```

## Adding to requirements
**Please pin this library only on the major version!**

We use TDD and strict semantic versioning, there will be frequent updates and no breaking changes in minor and patch versions.
To ensure that you only pin the major version of this library in your `requirements.txt`, specify the package name followed by the major version and a wildcard for minor and patch versions. For example:

    json_repair==0.*

In this example, any version that starts with `0.` will be acceptable, allowing for updates on minor and patch versions.

---
# How to cite
If you are using this library in your academic work (as I know many folks are) please find the BibTex here:

    @software{Baccianella_JSON_Repair_-_2025,
        author  = "Stefano {Baccianella}",
        month   = "feb",
        title   = "JSON Repair - A python module to repair invalid JSON, commonly used to parse the output of LLMs",
        url     = "https://github.com/mangiucugna/json_repair",
        version = "0.39.1",
        year    = 2025
    }

Thank you for citing my work and please send me a link to the paper if you can!

---

# How it works
This module will parse the JSON file following the BNF definition:

    <json> ::= <primitive> | <container>

    <primitive> ::= <number> | <string> | <boolean>
    ; Where:
    ; <number> is a valid real number expressed in one of a number of given formats
    ; <string> is a string of valid characters enclosed in quotes
    ; <boolean> is one of the literal strings 'true', 'false', or 'null' (unquoted)

    <container> ::= <object> | <array>
    <array> ::= '[' [ <json> *(', ' <json>) ] ']' ; A sequence of JSON values separated by commas
    <object> ::= '{' [ <member> *(', ' <member>) ] '}' ; A sequence of 'members'
    <member> ::= <string> ': ' <json> ; A pair consisting of a name, and a JSON value

If something is wrong (a missing parentheses or quotes for example) it will use a few simple heuristics to fix the JSON string:
- Add the missing parentheses if the parser believes that the array or object should be closed
- Quote strings or add missing single quotes
- Adjust whitespaces and remove line breaks

I am sure some corner cases will be missing, if you have examples please open an issue or even better push a PR

# Contributing
If you want to contribute, start with `CONTRIBUTING.md` and read the Code Wiki writeup for a tour of the codebase and key entry points: https://codewiki.google/github.com/mangiucugna/json_repair

# How to develop
Use `uv` to set up the dev environment and run tooling:

    uv sync --group dev
    uv run pre-commit run --all-files
    uv run pytest

Make sure that the Github Actions running after pushing a new commit don't fail as well.

# How to release
You will need owner access to this repository
- Edit `pyproject.toml` and update the version number appropriately using `semver` notation
- **Commit and push all changes to the repository before continuing or the next steps will fail**
- Run `python -m build`
- Create a new release in Github, making sure to tag all the issues solved and contributors. Create the new tag, same as the one in the build configuration
- Once the release is created, a new Github Actions workflow will start to publish on Pypi, make sure it didn't fail

## Docs demo API deployment (PythonAnywhere)
- The docs site is deployed by GitHub Pages (`pages-build-deployment`).
- After a successful Pages deployment on `main`, `.github/workflows/pythonanywhere-sync.yml` uploads `docs/app.py` to PythonAnywhere at `/home/mangiucugna/json_repair/app.py` and reloads `mangiucugna.pythonanywhere.com`.
- Required repository Actions secret: PythonAnywhere API token (`PYTHONANYWHERE_API_TOKEN`).

---
# Repair JSON in other programming languages
- Typescript: https://github.com/josdejong/jsonrepair
- Go: https://github.com/RealAlexandreAI/json-repair
- Ruby: https://github.com/sashazykov/json-repair-rb
- Rust: https://github.com/oramasearch/llm_json
- R: https://github.com/cgxjdzz/jsonRepair
- Java: https://github.com/du00cs/json-repairj
---
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=mangiucugna/json_repair&type=Date)](https://star-history.com/#mangiucugna/json_repair&Date)

```

### `README.zh.md`

```md
# json_repair — 修复损坏的 JSON（Python 工具包）

[![PyPI](https://img.shields.io/pypi/v/json-repair)](https://pypi.org/project/json-repair/) ![Python version](https://img.shields.io/badge/python-3.10+-important) [![PyPI downloads](https://img.shields.io/pypi/dm/json-repair)](https://pypi.org/project/json-repair/) [![PyPI Downloads](https://static.pepy.tech/badge/json-repair)](https://pepy.tech/projects/json-repair) [![Github Sponsors](https://img.shields.io/github/sponsors/mangiucugna)](https://github.com/sponsors/mangiucugna) [![GitHub Repo stars](https://img.shields.io/github/stars/mangiucugna/json_repair?style=flat)](https://github.com/mangiucugna/json_repair/stargazers)

> 本文档由 AI 翻译，如有疏漏欢迎指正。

[English](README.md) | **中文**

这个 Python 工具包可以修复来自 LLM、API、日志和人工编辑输入中的损坏 JSON。

- 可修复缺失引号、逗号、括号、注释、夹杂说明文字和被截断的值。
- 既可以作为 `json.loads()` 的兜底解析器，也可以配合 schema 做引导修复。
- 可直接安装 `pip install json-repair`，也可以先试用在线演示。

![banner](https://raw.githubusercontent.com/mangiucugna/json_repair/main/banner.png)

---

## 快速示例

```python
import json_repair

bad_json = '{"users":[{"name":"Ada","role":"admin",}],"ok":true'
decoded_object = json_repair.loads(bad_json)

# {'users': [{'name': 'Ada', 'role': 'admin'}], 'ok': True}
```

如果 `json_repair` 帮你省下了调试时间，欢迎给仓库点个 Star：https://github.com/mangiucugna/json_repair

---

## 如果这个项目帮到你了

- 最简单的支持方式：给仓库点个 Star，让更多人能搜到它。
- 如果身边有人也在处理大模型或脏数据 JSON，把仓库或在线演示链接发给他们。
- 如果你遇到了修不好的样例，欢迎在 GitHub 提 Issue 并附上最小复现输入。
- 如果你的团队在生产环境长期使用它，再考虑通过 Sponsors 支持维护会更自然。

---

## 高级赞助商
- [Icana-AI](https://github.com/Icana-AI) —— CallCoach（全球领先的呼叫中心 AI 教练）的开发者。访问 [https://www.icana.ai/](https://www.icana.ai/)
- [mjharte](https://github.com/mjharte)

---

# 演示
- 中文提示的在线演示（GitHub Pages）：https://mangiucugna.github.io/json_repair/index.zh.html
- 英文演示：https://mangiucugna.github.io/json_repair/
- Google NotebookLM 英文音频介绍：https://notebooklm.google.com/notebook/05312bb3-f6f3-4e49-a99b-bd51db64520b/audio

---

# 想支持这个项目？
这个库免费且由作者业余维护。如果它帮到了你的工作，欢迎在 GitHub Sponsors 支持：https://github.com/sponsors/mangiucugna

---

# 动机
许多大模型输出的 JSON 并不规范：有时缺一个括号，有时多出文本。幸运的是，大部分错误足够简单，可以在不破坏内容的情况下修复。找不到一个轻量、可靠的 Python 包能处理这些问题，于是就写了 json_repair。

# 支持的用例

### 修复 JSON 语法错误
- 缺失引号、逗号错误、未转义字符、不完整的键值对。
- 布尔/空值写错（true/false/null），修复损坏的键值结构。
- Python 风格元组：带逗号的圆括号序列会转换为 JSON 数组，而单个圆括号值仍保持为标量。在数组、对象和元组内，`true`/`false`/`null` 与 `None` 不区分大小写地识别为 JSON 布尔值或 null。

### 修复损坏的数组和对象
- 补全/修复未完成的数组或对象，添加必要的元素（逗号、括号）或默认值（null、""）。
- 清理包含额外非 JSON 字符（如注释、杂项文本）的字符串，尽量保持结构。

### 自动补全缺失值
- 自动为缺失的字段补充合理默认值（如空字符串或 null），保证可解析。

# 如何使用

安装：
```
pip install json-repair
```

基础用法：
```python
from json_repair import repair_json

good_json_string = repair_json(bad_json_string)
# 如果输入极度损坏，可能返回空字符串
```

替代 `json.loads()`：
```python
import json_repair

decoded_object = json_repair.loads(json_string)
# 或者
decoded_object = json_repair.repair_json(json_string, return_objects=True)
```

### 避免反模式
有些用户会先手动调用一次 `json.loads()`，失败后再回退到 `json_repair`。这通常是重复工作，因为 `json_repair` 默认就会先做一次严格的 `json.loads()` / `json.load()` 检查。它的正常流程是：

- 先尝试标准库 `json.loads()` / `json.load()`
- 如果成功，直接返回解析结果
- 如果失败，再进入修复解析器

默认推荐直接这样调用：

```python
import json_repair

obj = json_repair.loads(json_string)
```

只有在你明确想跳过这一步验证时，才使用 `skip_json_loads=True`。

如果确定输入损坏，直接传 `skip_json_loads=True`：
```python
obj = repair_json(bad_json_string, skip_json_loads=True)
```

### 从文件读取
json_repair 也提供 `json.load()` 的替代：
```python
from json_repair import load, from_file

decoded_object = load(open(fname, "rb"))
decoded_object = from_file(fname)
```
I/O 异常不会被库捕获，需要由调用方处理。

### 非拉丁字符
处理中文/日文/韩文等时，传入 `ensure_ascii=False` 保留原文：
```python
repair_json("{'test_chinese_ascii':'统一码'}", ensure_ascii=False)
```

### 透传 json.dumps 参数
`repair_json` 支持并透传 `json.dumps` 的参数（如 `indent`）。

### 性能提示
- 默认情况下，`json_repair` 会先尝试标准库 JSON 解析，只有严格解析失败时才会进入修复解析器。
- 如果你已经确定输入不是有效 JSON，可以传 `skip_json_loads=True`，直接跳过这一步验证。
- `return_objects=True` 更快，因为直接返回对象。
- `skip_json_loads=True` 只适合你 100% 确定输入不是有效 JSON 的场景。
- `skip_json_loads=True` 不是“更快但对有效 JSON 等价”的模式；它会绕过标准库成功路径，因此有效输入应使用默认行为。
- 如有转义问题，传入原始字符串（如 `r"string with escaping\""`）。

这是一个明确的取舍：

- 默认行为：先走标准库 JSON 校验路径，失败后再修复
- `skip_json_loads=True`：直接跳过校验路径，进入修复解析器

重要：`skip_json_loads=True` 只适用于你已经确定输入无效的场景。如果把本来就是有效的 JSON 强行送进修复解析器，`json_repair` 仍可能尝试“修复”，从而改变结果的结构或值。如果你需要保证有效 JSON 原样保留，请保持 `skip_json_loads=False`。

`json_repair` 故意保持标准库 JSON 作为默认验证路径，不会自动探测或切换到第三方 JSON 库。这样可以避免常见路径上的额外开销，也能让行为更可预测。

### 什么时候自己使用其他 JSON 库

如果你需要标准库之外的 JSON 语义，或者想自己控制性能取舍，请显式使用你偏好的 JSON 库，而不是期待 `json_repair` 自动切换解析器。很多人会问到 `orjson`，它也是同样的用法。

推荐模式：

严格 JSON 优先，只有失败时才修复：

```python
import json_repair

obj = json_repair.loads(json_string)
```

已知输入损坏，直接跳过验证：

```python
from json_repair import repair_json

obj = repair_json(bad_json_string, return_objects=True, skip_json_loads=True)
```

先用 `orjson`，失败后再回退到 `json_repair`：

```python
import json_repair
import orjson

try:
    obj = orjson.loads(json_string)
except orjson.JSONDecodeError:
    obj = json_repair.loads(json_string, skip_json_loads=True)
```

### 严格模式
默认尽量修复；若需要严格校验而非修复，可传 `strict=True`：
```python
from json_repair import repair_json
repair_json(bad_json_string, strict=True)
```
严格模式会在发现结构问题（重复键、缺少冒号、空键/值、多个顶层元素等）时立刻抛出 `ValueError`。CLI 也支持 `json_repair --strict input.json`。

严格模式可与 `skip_json_loads=True` 组合：跳过初始 `json.loads` 检查，但仍执行严格解析规则。

### Schema 引导修复
Schema 引导修复目前处于 beta 阶段，仍可能出现 bug。

可使用 JSON Schema（或 Pydantic v2 模型）指导修复。开启后解析器会：

- 补齐缺失值（默认值、必填字段）
- 在安全范围内做类型转换（例如 `"1"` → `1`，布尔支持 `"yes"`/`"no"`/`1`/`0`）
- 移除 schema 明确禁止的字段/数组项

可通过 `schema_repair_mode` 选择模式：

- `standard`（默认）：当前 schema 引导行为。
- `salvage`：包含 `standard`，并额外启用：
  - 数组项无法修复时按项丢弃（而不是整体失败）；
  - 当 schema 结构明确时，按属性顺序把数组映射为对象。
  - 当根 schema 期望对象且输入为单元素对象数组时，可在根节点解包（`[{...}] -> {...}`）；
  - 仅在可安全推断时补齐缺失必填字段（`default`、`const`、首个 `enum`，或在约束允许时补空数组/空对象）。
  - 对连续的顶层片段，会跳过不符合 schema 的片段，并返回第一个符合 schema 的片段。

适用于需要稳定、可验证输出（下游校验、落库、类型化处理等）的场景。若无法修复到满足 schema，将抛出 `ValueError`。

安装可选依赖：
```
pip install 'json-repair[schema]'
```
（CLI 可用 `pipx install 'json-repair[schema]'`。）

注意：只要传了 `schema`，无论输入 JSON 本身是否有效，都会执行 schema 引导。Schema 与 `strict=True` 互斥。

```python
from json_repair import repair_json

schema = {
    "type": "object",
    "properties": {"value": {"type": "integer"}},
    "required": ["value"],
}

repair_json('{"value": "1"}', schema=schema, return_objects=True)

repair_json(
    '{"items":[{"id":1,"score":85.6},{"id":2,"score":"N/A"}]}',
    schema={
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"id": {"type": "integer"}, "score": {"type": "number"}},
                    "required": ["id", "score"],
                },
            }
        },
        "required": ["items"],
    },
    schema_repair_mode="salvage",
    return_objects=True,
)
```

Pydantic v2 模型示例：

```python
from pydantic import BaseModel, Field
from json_repair import repair_json


class Payload(BaseModel):
    value: int
    tags: list[str] = Field(default_factory=list)


repair_json(
    '{"value": "1", "tags": }',
    schema=Payload,
    skip_json_loads=True,
    return_objects=True,
)
```

### 流式处理
需要在流式数据上修复 JSON 时，可传 `stream_stable=True`：
```python
stream_output = repair_json(stream_input, stream_stable=True)
```

### 更多集成示例

如果你想直接复制到实际项目里使用，可查看 [examples/README.md](https://github.com/mangiucugna/json_repair/blob/main/examples/README.md)：

- [repair_llm_output.py](https://github.com/mangiucugna/json_repair/blob/main/examples/repair_llm_output.py)：修复带 Markdown 代码块或额外说明文字的模型输出。
- [chinese_llm_output.py](https://github.com/mangiucugna/json_repair/blob/main/examples/chinese_llm_output.py)：修复包含中文字段和值的模型输出，并保留原始中文字符。
- [pydantic_schema.py](https://github.com/mangiucugna/json_repair/blob/main/examples/pydantic_schema.py)：使用 Pydantic v2 模型做 schema 引导修复。
- [stream_stable.py](https://github.com/mangiucugna/json_repair/blob/main/examples/stream_stable.py)：在流式输出尚未完成时保持稳定的部分 JSON。
- [fastapi_app.py](https://github.com/mangiucugna/json_repair/blob/main/examples/fastapi_app.py)：在 FastAPI 接口中完成修复和校验。

### CLI 使用
安装命令行工具：
```bash
pipx install json-repair
```
查看选项：
```
$ json_repair -h
usage: json_repair [-h] [-i] [-o TARGET] [--ensure_ascii] [--indent INDENT]
                   [--skip-json-loads] [--schema SCHEMA] [--schema-model MODEL]
                   [--strict] [--schema-repair-mode {standard,salvage}] [filename]

Repair and parse JSON files.

positional arguments:
  filename              The JSON file to repair (if omitted, reads from stdin)

options:
  -h, --help            show this help message and exit
  -i, --inline          Replace the file inline instead of returning the output to stdout
  -o TARGET, --output TARGET
                        If specified, the output will be written to TARGET filename instead of stdout
  --ensure_ascii        Pass ensure_ascii=True to json.dumps()
  --indent INDENT       Number of spaces for indentation (Default 2)
  --skip-json-loads     Skip initial json.loads validation
  --schema SCHEMA       Path to a JSON Schema file that guides repairs
  --schema-model MODEL  Pydantic v2 model in 'module:ClassName' form that guides repairs
  --strict              Raise on duplicate keys, missing separators, empty keys/values, and similar structural issues instead of repairing them
  --schema-repair-mode {standard,salvage}
                        Schema 修复模式：standard（默认）或 salvage（尽力返回可用数组/对象）
```

---

## 在 requirements 中依赖
**请只固定大版本号！**  
采用严格语义化版本与 TDD，次版本/补丁版本不会引入破坏性更新，更新频繁。建议在 `requirements.txt` 里使用：
```
json_repair==0.*
```

---
# 如何引用
如果你在学术工作中使用了本库，BibTex 如下：
```
@software{Baccianella_JSON_Repair_-_2025,
    author  = "Stefano {Baccianella}",
    month   = "feb",
    title   = "JSON Repair - A python module to repair invalid JSON, commonly used to parse the output of LLMs",
    url     = "https://github.com/mangiucugna/json_repair",
    version = "0.39.1",
    year    = 2025
}
```
欢迎引用并分享论文链接！

---

# 工作原理
模块按照 BNF 解析 JSON，并在发现问题时使用启发式修复：
```
<json> ::= <primitive> | <container>

<primitive> ::= <number> | <string> | <boolean>
; 其中:
; <number> 是合法的实数
; <string> 是用引号包裹的字符串
; <boolean> 为 'true' / 'false' / 'null'

<container> ::= <object> | <array>
<array> ::= '[' [ <json> *(', ' <json>) ] ']'
<object> ::= '{' [ <member> *(', ' <member>) ] '}'
<member> ::= <string> ': ' <json>
```
若解析出错（如缺少括号或引号），将尝试：
- 补充缺失的括号/大括号。
- 为字符串补引号或补单引号。
- 调整空白并移除多余换行。

如有遗漏的边界情况，欢迎提交 Issue 或 PR。

# 贡献
想要参与贡献，请先阅读 `CONTRIBUTING.md`，再浏览 Code Wiki 的代码库导览与入口说明：https://codewiki.google/github.com/mangiucugna/json_repair

# 开发指南
使用 `uv` 配置开发环境并运行工具：

    uv sync --group dev
    uv run pre-commit run --all-files
    uv run pytest

提交后请确认 GitHub Actions 通过。

# 发布指南
需要仓库 owner 权限：
- 修改 `pyproject.toml`，按照 semver 更新版本。
- **先提交并推送所有改动，否则后续步骤会失败。**
- 运行 `python -m build`。
- 在 GitHub 创建 Release，标记已解决的 Issue 与贡献者，Tag 与版本一致。
- Release 创建后会触发 GitHub Actions 发布到 PyPI，确认任务通过。

## 文档演示 API 部署（PythonAnywhere）
- 文档站点由 GitHub Pages 工作流 `pages-build-deployment` 发布。
- 当 `main` 上 Pages 发布成功后，`.github/workflows/pythonanywhere-sync.yml` 会把 `docs/app.py` 上传到 PythonAnywhere 的 `/home/mangiucugna/json_repair/app.py`，并重载 `mangiucugna.pythonanywhere.com`。
- 需要仓库 Actions 密钥：PythonAnywhere API token（`PYTHONANYWHERE_API_TOKEN`）。

---
# 其他语言的 JSON 修复
- Typescript: https://github.com/josdejong/jsonrepair
- Go: https://github.com/RealAlexandreAI/json-repair
- Ruby: https://github.com/sashazykov/json-repair-rb
- Rust: https://github.com/oramasearch/llm_json
- R: https://github.com/cgxjdzz/jsonRepair
- Java: https://github.com/du00cs/json-repairj

---
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=mangiucugna/json_repair&type=Date)](https://star-history.com/#mangiucugna/json_repair&Date)

```

### `SECURITY.md`

```md
# Security Policy

## Reporting a Vulnerability

Please open an Issue with tag "Security" or propose a PR yourself

```

### `src/json_repair/__init__.py`

```py
from .json_repair import from_file, load, loads, repair_json
from .utils.constants import JSONReturnType

__all__ = ["JSONReturnType", "from_file", "load", "loads", "repair_json"]

```

### `src/json_repair/__main__.py`

```py
import sys

from .json_repair import cli

if __name__ == "__main__":
    sys.exit(cli())

```

### `src/json_repair/json_parser.py`

```py
import json
from collections.abc import Callable
from contextlib import ExitStack
from typing import TYPE_CHECKING, Any, TextIO

from .parse_array import parse_array as _parse_array
from .parse_comment import parse_comment as _parse_comment
from .parse_number import parse_number as _parse_number
from .parse_object import parse_object as _parse_object
from .parse_string import parse_string as _parse_string
from .parser_parenthesized import parenthesized_is_explicit_tuple, top_level_parenthesized_can_start_value
from .utils.constants import STRING_DELIMITERS, JSONReturnType
from .utils.json_context import ContextValues, JsonContext
from .utils.object_comparer import ObjectComparer
from .utils.string_file_wrapper import StringFileWrapper

if TYPE_CHECKING:
    from .schema_repair import SchemaRepairer


class JSONParser:
    # Split the parse methods into separate files because this one was like 3000 lines
    def parse_array(
        self,
        schema: dict[str, Any] | bool | None = None,
        path: str = "$",
        closing_delimiter: str = "]",
    ) -> list[JSONReturnType]:
        return _parse_array(self, schema, path, closing_delimiter)

    def parse_comment(self, record_top_level_value: bool = False) -> JSONReturnType:
        return _parse_comment(self, record_top_level_value=record_top_level_value)

    def parse_number(self) -> JSONReturnType:
        return _parse_number(self)

    def parse_object(
        self,
        schema: dict[str, Any] | bool | None = None,
        path: str = "$",
    ) -> JSONReturnType:
        return _parse_object(self, schema, path)

    def parse_string(self) -> JSONReturnType:
        return _parse_string(self)

    def __init__(
        self,
        json_str: str | StringFileWrapper,
        json_fd: TextIO | None,
        logging: bool | None,
        json_fd_chunk_length: int = 0,
        stream_stable: bool = False,
        strict: bool = False,
        try_valid_json_suffix: bool = False,
    ) -> None:
        # The string to parse
        self.json_str: str | StringFileWrapper = json_str
        # Alternatively, the file description with a json file in it
        if json_fd:
            # This is a trick we do to treat the file wrapper as an array
            self.json_str = StringFileWrapper(json_fd, json_fd_chunk_length)
        # Index is our iterator that will keep track of which character we are looking at right now
        self.index: int = 0
        # This is used in the object member parsing to manage the special cases of missing quotes in key or value
        self.context = JsonContext()
        self.deferred_contexts: list[ContextValues] = []
        # Use this to log the activity, but only if logging is active

        # This is a trick but a beautiful one. We call self.log in the code over and over even if it's not needed.
        # We could add a guard in the code for each call but that would make this code unreadable, so here's this neat trick
        # Replace self.log with a noop
        self.logging = logging
        self.logger: list[dict[str, str]] = []
        if logging:
            self.log = self._log
        else:
            # No-op
            self.log = lambda *args, **kwargs: None  # noqa: ARG005
        # When the json to be repaired is the accumulation of streaming json at a certain moment.
        # e.g. json obtained from llm response.
        # If this parameter to True will keep the repair results stable. For example:
        #   case 1:  '{"key": "val\\' => '{"key": "val"}'
        #   case 2:  '{"key": "val\\n' => '{"key": "val\\n"}'
        #   case 3:  '{"key": "val\\n123,`key2:value2' => '{"key": "val\\n123,`key2:value2"}'
        #   case 4:  '{"key": "val\\n123,`key2:value2`"}' => '{"key": "val\\n123,`key2:value2`"}'
        self.stream_stable = stream_stable
        # Over time the library got more and more complex heuristics to repair JSON. Some of these heuristics
        # may not be desirable in some use cases and the user would prefer json_repair to return an exception.
        # So strict mode was added to disable some of those heuristics.
        self.strict = strict
        self.try_valid_json_suffix = try_valid_json_suffix
        self.has_tried_valid_json_suffix = False
        self._last_parse_found_value = False
        self.schema_repairer: SchemaRepairer | None = None

    def parse(
        self,
    ) -> JSONReturnType:
        return self._parse_top_level(self.parse_json)

    def parse_with_schema(
        self,
        repairer: "SchemaRepairer",
        schema: dict[str, Any] | bool,
    ) -> JSONReturnType:
        """Parse with schema guidance enabled for all nested values."""
        self.schema_repairer = repairer
        if repairer.schema_repair_mode == "salvage":
            return self._parse_top_level_salvage_with_schema(repairer, schema)
        return self._parse_top_level(lambda: self.parse_json(schema, "$"))

    def _parse_top_level_salvage_with_schema(
        self,
        repairer: "SchemaRepairer",
        schema: dict[str, Any] | bool,
    ) -> JSONReturnType:
        """Return the first schema-valid top-level fragment while salvaging."""
        last_error: ValueError | None = None
        while self.index < len(self.json_str):
            self.context.clear()
            self.deferred_contexts.clear()
            value = self.parse_json(schema, "$", finalize_schema=False, record_top_level_value=True)
            if not self._last_parse_found_value:
                break
            try:
                repaired = repairer.repair_value(value, schema, "$")
                repairer.validate(repaired, schema)
            except ValueError as exc:
                last_error = exc
                if self.index >= len(self.json_str):
                    break
                self.log("Skipped top-level fragment that did not match schema while salvaging")
                continue
            else:
                return repaired
        if last_error is not None:
            raise last_error
        return ""

    # Consolidate top-level parsing so we handle multiple sequential JSON values consistently
    # (including update semantics and strict-mode validation).
    def _parse_top_level(self, parse_element: Callable[[], JSONReturnType]) -> JSONReturnType:
        json = parse_element()
        if self.index < len(self.json_str):
            self.log(
                "The parser returned early, checking if there's more json elements",
            )
            json = [json]
            while self.index < len(self.json_str):
                self.context.clear()
                self.deferred_contexts.clear()
                is_comma_separated = self._next_top_level_value_is_comma_separated()
                element_start_index = self.index
                j = parse_element()
                if self.strict and self.index > element_start_index:
                    self.log(
                        "Multiple top-level JSON elements found in strict mode, raising an error",
                    )
                    raise ValueError("Multiple top-level JSON elements found in strict mode.")
                if j:
                    if not is_comma_separated and ObjectComparer.is_same_object(json[-1], j):
                        # Treat repeated objects as updates: keep the newest value.
                        json.pop()
                    else:
                        if not json[-1]:
                            json.pop()
                    json.append(j)
                else:
                    self.index += 1
            if len(json) == 1:
                self.log(
                    "There were no more elements, returning the element without the array",
                )
                json = json[0]
        return json

    def _next_top_level_value_is_comma_separated(self) -> bool:
        idx = self.scroll_whitespaces()
        if self.get_char_at(idx) == ",":
            return True

        idx = self.index - 1
        while idx >= 0 and self.json_str[idx].isspace():
            idx -= 1
        return idx >= 0 and self.json_str[idx] == ","

    def _initial_container_has_non_comma_trailing_content(self) -> bool:
        if self.index != 0 or not isinstance(self.json_str, str):
            return True

        containers: list[str] = []
        in_string = False
        escaped = False
        closing_delimiters = {"{": "}", "[": "]"}
        for index, char in enumerate(self.json_str):
            if in_string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    in_string = False
                continue

            if char == '"':
                in_string = True
            elif char in closing_delimiters:
                containers.append(char)
            elif char in ["}", "]"]:
                if not containers or char != closing_delimiters[containers.pop()]:
                    return False
                if not containers:
                    trailing_index = index + 1
                    while trailing_index < len(self.json_str) and self.json_str[trailing_index].isspace():
                        trailing_index += 1
                    return trailing_index < len(self.json_str) and self.json_str[trailing_index] != ","

        return False

    def _try_parse_valid_json_value(self) -> tuple[bool, JSONReturnType]:
        if (
            not self.try_valid_json_suffix
            or self.has_tried_valid_json_suffix
            or not self.context.empty
            or not isinstance(self.json_str, str)
        ):
            return False, ""

        self.has_tried_valid_json_suffix = True
        try:
            value, end_idx = json.JSONDecoder().raw_decode(self.json_str[self.index :])
        except json.JSONDecodeError:
            return False, ""

        self.index += end_idx
        return True, value

    def parse_json(
        self,
        schema: dict[str, Any] | bool | None = None,
        path: str = "$",
        finalize_schema: bool = True,
        record_top_level_value: bool = False,
    ) -> JSONReturnType:
        """Parse the next JSON value and, when configured, enforce schema constraints."""
        if record_top_level_value:
            self._last_parse_found_value = False
        if self.deferred_contexts:
            deferred_contexts, self.deferred_contexts = self.deferred_contexts, []
            with ExitStack() as stack:
                for context_value in deferred_contexts:
                    stack.enter_context(self.context.enter(context_value))
                return self.parse_json(schema, path, finalize_schema, record_top_level_value)

        repairer, schema = self._resolve_schema_for_parse(schema)

        while True:
            char = self.get_char_at()
            # None means that we are at the end of the string provided
            if char is None:
                return ""
            if (
                self.try_valid_json_suffix
                and char in ["{", "["]
                and self._initial_container_has_non_comma_trailing_content()
            ):
                parsed_suffix, value = self._try_parse_valid_json_value()
                if parsed_suffix:
                    return self._finalize_parsed_value(
                        value, repairer, schema, path, finalize_schema, record_top_level_value
                    )
            # <object> starts with '{'
            if char == "{":
                self.index += 1
                value = self.parse_object(schema, path) if repairer else self.parse_object()
                return self._finalize_parsed_value(
                    value, repairer, schema, path, finalize_schema, record_top_level_value
                )
            # <array> starts with '['
            if char == "[":
                self.index += 1
                value = self.parse_array(schema, path) if repairer else self.parse_array()
                return self._finalize_parsed_value(
                    value, repairer, schema, path, finalize_schema, record_top_level_value
                )
            # Python tuple literals and grouped values start with '('
            if char == "(":
                # Keep top-level tuple detection conservative so inline prose like
                # "note (clarification):" does not hijack later JSON blocks.
                if not self.context.empty or self.top_level_parenthesized_can_start_value():
                    value = self.parse_parenthesized(schema, path) if repairer else self.parse_parenthesized()
                    return self._finalize_parsed_value(
                        value, repairer, schema, path, finalize_schema, record_top_level_value
                    )
                self.index += 1
                continue
            # <string> starts with a quote
            if not self.context.empty and (char in STRING_DELIMITERS or char.isalpha()):
                value = self.parse_string()
                return self._finalize_parsed_value(
                    value, repairer, schema, path, finalize_schema, record_top_level_value
                )
            # <number> starts with [0-9] or minus
            if not self.context.empty and (char.isdigit() or char == "-" or char == "."):
                value = self.parse_number()
                return self._finalize_parsed_value(
                    value, repairer, schema, path, finalize_schema, record_top_level_value
                )
            if char in ["#", "/"]:
                value = self.parse_comment(record_top_level_value)
                return self._finalize_parsed_value(value, repairer, schema, path, finalize_schema)
            # If everything else fails, we just ignore and move on
            self.index += 1

    def _resolve_schema_for_parse(
        self,
        schema: dict[str, Any] | bool | None,
    ) -> tuple["SchemaRepairer | None", dict[str, Any] | bool | None]:
        repairer = self.schema_repairer if self.schema_repairer is not None and schema not in (None, True) else None
        if repairer is None:
            return None, schema

        schema = repairer.resolve_schema(schema)
        if schema is True:
            return None, schema
        if schema is False:
            raise ValueError("Schema does not allow any values.")
        return repairer, schema

    def _finalize_parsed_value(
        self,
        value: JSONReturnType,
        repairer: "SchemaRepairer | None",
        schema: dict[str, Any] | bool | None,
        path: str,
        finalize_schema: bool = True,
        record_top_level_value: bool = False,
    ) -> JSONReturnType:
        if record_top_level_value:
            self._last_parse_found_value = True
        if repairer is None or not finalize_schema:
            return value
        return repairer.repair_value(value, schema, path)

    def get_char_at(self, count: int = 0) -> str | None:
        # Why not use something simpler? Because try/except in python is a faster alternative to an "if" statement that is often True
        try:
            return self.json_str[self.index + count]
        except IndexError:
            return None

    def skip_whitespaces(self) -> None:
        """
        This function quickly iterates on whitespaces, moving the self.index forward
        """
        try:
            char = self.json_str[self.index]
            while char.isspace():
                self.index += 1
                char = self.json_str[self.index]
        except IndexError:
            pass

    def scroll_whitespaces(self, idx: int = 0) -> int:
        """
        This function quickly iterates on whitespaces. Doesn't move the self.index and returns the offset from self.index
        """
        try:
            char = self.json_str[self.index + idx]
            while char.isspace():
                idx += 1
                char = self.json_str[self.index + idx]
        except IndexError:
            pass
        return idx

    def skip_to_character(self, character: str | list[str], idx: int = 0) -> int:
        """
        Advance from (self.index + idx) until we hit an *unescaped* target character.
        Returns the offset (idx) from self.index to that position, or the distance to the end if not found.
        """
        targets = set(character) if isinstance(character, list) else {character}
        i = self.index + idx
        n = len(self.json_str)
        backslashes = 0  # count of consecutive '\' immediately before current char

        while i < n:
            ch = self.json_str[i]

            if ch == "\\":
                backslashes += 1
                i += 1
                continue

            # ch is not a backslash; if it's a target and not escaped (even backslashes), we're done
            if ch in targets and (backslashes % 2 == 0):
                return i - self.index

            # reset backslash run when we see a non-backslash
            backslashes = 0
            i += 1

        # not found; return distance to end
        return n - self.index

    def parenthesized_is_explicit_tuple(self) -> bool:
        return parenthesized_is_explicit_tuple(self)

    def top_level_parenthesized_can_start_value(self) -> bool:
        return top_level_parenthesized_can_start_value(self)

    def parse_parenthesized(
        self,
        schema: dict[str, Any] | bool | None = None,
        path: str = "$",
    ) -> JSONReturnType:
        explicit_tuple = self.parenthesized_is_explicit_tuple()
        self.index += 1
        values = self.parse_array(schema, path, closing_delimiter=")")
        if explicit_tuple or len(values) != 1:
            return values
        return values[0]

    def _log(self, text: str) -> None:
        window: int = 10
        start: int = max(self.index - window, 0)
        end: int = min(self.index + window, len(self.json_str))
        context: str = self.json_str[start:end]
        self.logger.append(
            {
                "text": text,
                "context": context,
            }
        )

```

### `src/json_repair/json_repair.py`

```py
"""
This module will parse the JSON file following the BNF definition:

    <json> ::= <container>

    <primitive> ::= <number> | <string> | <boolean>
    ; Where:
    ; <number> is a valid real number expressed in one of a number of given formats
    ; <string> is a string of valid characters enclosed in quotes
    ; <boolean> is one of the literal strings 'true', 'false', or 'null' (unquoted)

    <container> ::= <object> | <array>
    <array> ::= '[' [ <json> *(', ' <json>) ] ']' ; A sequence of JSON values separated by commas
    <object> ::= '{' [ <member> *(', ' <member>) ] '}' ; A sequence of 'members'
    <member> ::= <string> ': ' <json> ; A pair consisting of a name, and a JSON value

If something is wrong (a missing parentheses or quotes for example) it will use a few simple heuristics to fix the JSON string:
- Add the missing parentheses if the parser believes that the array or object should be closed
- Quote strings or add missing single quotes
- Adjust whitespaces and remove line breaks

All supported use cases are in the unit tests
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Literal, TextIO, overload

from .json_parser import JSONParser
from .schema_repair import SchemaRepairer, load_schema_model, normalize_schema_repair_mode, schema_from_input
from .utils.constants import JSONReturnType


@overload
def repair_json(
    json_str: str = "",
    return_objects: Literal[False] = False,
    skip_json_loads: bool = False,
    logging: Literal[False] = False,
    json_fd: TextIO | None = None,
    chunk_length: int = 0,
    stream_stable: bool = False,
    strict: bool = False,
    schema: Any | None = None,
    schema_repair_mode: Literal["standard", "salvage"] = "standard",
    **json_dumps_args: Any,
) -> str: ...


@overload
def repair_json(
    json_str: str = "",
    return_objects: Literal[True] = True,
    skip_json_loads: bool = False,
    logging: Literal[False] = False,
    json_fd: TextIO | None = None,
    chunk_length: int = 0,
    stream_stable: bool = False,
    strict: bool = False,
    schema: Any | None = None,
    schema_repair_mode: Literal["standard", "salvage"] = "standard",
    **json_dumps_args: Any,
) -> JSONReturnType: ...


@overload
def repair_json(
    json_str: str = "",
    return_objects: bool = False,
    skip_json_loads: bool = False,
    logging: Literal[True] = True,
    json_fd: TextIO | None = None,
    chunk_length: int = 0,
    stream_stable: bool = False,
    strict: bool = False,
    schema: Any | None = None,
    schema_repair_mode: Literal["standard", "salvage"] = "standard",
    **json_dumps_args: Any,
) -> tuple[JSONReturnType, list[dict[str, str]]]: ...


@overload
def repair_json(
    json_str: str = "",
    return_objects: bool = False,
    skip_json_loads: bool = False,
    logging: bool = False,
    json_fd: TextIO | None = None,
    chunk_length: int = 0,
    stream_stable: bool = False,
    strict: bool = False,
    schema: Any | None = None,
    schema_repair_mode: Literal["standard", "salvage"] = "standard",
    **json_dumps_args: Any,
) -> str | JSONReturnType | tuple[JSONReturnType, list[dict[str, str]]]: ...


def repair_json(
    json_str: str = "",
    return_objects: bool = False,
    skip_json_loads: bool = False,
    logging: bool = False,
    json_fd: TextIO | None = None,
    chunk_length: int = 0,
    stream_stable: bool = False,
    strict: bool = False,
    schema: Any | None = None,
    schema_repair_mode: Literal["standard", "salvage"] = "standard",
    **json_dumps_args: Any,
) -> JSONReturnType | tuple[JSONReturnType, list[dict[str, str]]]:
    """
    Given a json formatted string, it will try to decode it and, if it fails, it will try to fix it.

    Args:
        json_str (str, optional): The JSON string to repair. Defaults to an empty string.
        return_objects (bool, optional): If True, return the decoded data structure. Defaults to False.
        skip_json_loads (bool, optional): If True, skip calling the built-in json.loads() function to verify that the json is valid before attempting to repair. Defaults to False.
        logging (bool, optional): If True, return a tuple with the repaired json and a log of all repair actions. Defaults to False. When no repairs were required, the repair log will be an empty list.
        json_fd (Optional[TextIO], optional): File descriptor for JSON input. Do not use! Use `from_file` or `load` instead. Defaults to None.
        ensure_ascii (bool, optional): Set to False to avoid converting non-latin characters to ascii (for example when using chinese characters). Defaults to True. Ignored if `skip_json_loads` is True.
        chunk_length (int, optional): Size in bytes of the file chunks to read at once. Ignored if `json_fd` is None. Do not use! Use `from_file` or `load` instead. Defaults to 1MB.
        stream_stable (bool, optional): When the json to be repaired is the accumulation of streaming json at a certain moment.If this parameter to True will keep the repair results stable.
        strict (bool, optional): If True, surface structural problems (duplicate keys, missing separators, empty keys/values, etc.) as ValueError instead of repairing them.
        schema (Any, optional): JSON Schema dict, boolean schema, or pydantic v2 model used to guide repairs and validation for both valid and invalid JSON inputs.
        schema_repair_mode (Literal["standard", "salvage"], optional): Schema repair mode. "standard" keeps default schema behavior; "salvage" enables best-effort schema salvage heuristics for arrays/objects.
    Returns:
        Union[JSONReturnType, Tuple[JSONReturnType, List[Dict[str, str]]]]: The repaired JSON or a tuple with the repaired JSON and repair log when logging is True.
    """
    schema_repair_mode = normalize_schema_repair_mode(schema_repair_mode)
    if schema is None and schema_repair_mode == "salvage":
        raise ValueError("schema_repair_mode='salvage' requires schema.")

    # Schema-guided repairs and strict mode are mutually exclusive to avoid conflicting behavior.
    if schema is not None and strict:
        raise ValueError("schema and strict cannot be used together.")

    parser: JSONParser | None = None
    repair_log: list[dict[str, str]] = []
    # ``skip_json_loads`` only skips the initial whole-input validation.  Once
    # the parser has found a top-level value after a prefix, raw decoding that
    # value is still a safe, targeted fast path.
    try_valid_json_suffix = json_fd is None
    if json_fd is not None:
        parser = JSONParser(
            json_str,
            json_fd,
            logging,
            chunk_length,
            stream_stable,
            strict,
        )
        if logging:
            repair_log = parser.logger
    schema_obj = schema_from_input(schema) if schema is not None else None
    repairer = (
        SchemaRepairer(schema_obj, repair_log if logging else None, schema_repair_mode=schema_repair_mode)
        if schema_obj is not None
        else None
    )

    # Fast path for valid JSON: schema-aware mode still applies repair+validation.
    parsed_json: JSONReturnType = None
    is_valid_json = False
    try:
        if not skip_json_loads:
            parsed_json = json.load(json_fd) if json_fd else json.loads(json_str)
            if repairer is not None and schema_obj is not None:
                # Validate here to ensure that we reject values that cannot satisfy the schema and fall back to the more expensive parser+schema repair if needed, instead of just returning the valid but schema-noncompliant JSON.
                try:
                    if repairer.is_valid(parsed_json, schema_obj):
                        is_valid_json = True
                    else:
                        try:
                            # repair_value may mutate containers in place; if validate fails we still
                            # fall back to parser.parse_with_schema, which fully replaces parsed_json.
                            repaired_value = repairer.repair_value(parsed_json, schema_obj, "$")
                            if repairer.is_valid(repaired_value, schema_obj):
                                parsed_json = repaired_value
                                is_valid_json = True
                        except ValueError:
                            pass
                except RecursionError as exc:
                    raise ValueError("Input schema nesting exceeds the supported schema recursion depth.") from exc
            else:
                is_valid_json = True
    except (json.JSONDecodeError, TypeError, ValueError):
        pass
    if not is_valid_json:
        if parser is None:
            parser = JSONParser(
                json_str,
                json_fd,
                logging,
                chunk_length,
                stream_stable,
                strict,
                try_valid_json_suffix=try_valid_json_suffix,
            )
            if logging:
                parser.logger = repair_log
        try:
            if repairer is not None and schema_obj is not None:
                # If schema-guided, we want to attempt repairs even on valid JSON that fails schema validation.
                try:
                    parsed_json = parser.parse_with_schema(repairer, schema_obj)
                    repairer.validate(parsed_json, schema_obj)
                except RecursionError as exc:
                    raise ValueError("Input schema nesting exceeds the supported schema recursion depth.") from exc
            else:
                # Otherwise, we can skip the more expensive schema-aware parsing and just do a normal parse.
                parsed_json = parser.parse()
        except RecursionError as exc:
            raise ValueError("Input nesting exceeds the supported parser recursion depth.") from exc

    # It's useful to return the actual object instead of the json string,
    # it allows this lib to be a replacement of the json library
    if logging:
        return parsed_json, repair_log
    if return_objects:
        return parsed_json
    # Avoid returning only a pair of quotes if it's an empty string
    if parsed_json == "":
        return ""
    return json.dumps(parsed_json, **json_dumps_args)


def loads(
    json_str: str,
    skip_json_loads: bool = False,
    logging: bool = False,
    stream_stable: bool = False,
    strict: bool = False,
    schema: Any | None = None,
    schema_repair_mode: Literal["standard", "salvage"] = "standard",
) -> JSONReturnType | tuple[JSONReturnType, list[dict[str, str]]] | str:
    """
    This function works like `json.loads()` except that it will fix your JSON in the process.
    It is a wrapper around the `repair_json()` function with `return_objects=True`.

    Args:
        json_str (str): The JSON string to load and repair.
        skip_json_loads (bool, optional): If True, skip calling the built-in json.loads() function to verify that the json is valid before attempting to repair. Defaults to False.
        logging (bool, optional): If True, return a tuple with the repaired json and a log of all repair actions. Defaults to False.
        strict (bool, optional): If True, surface structural problems (duplicate keys, missing separators, empty keys/values, etc.) as ValueError instead of repairing them.
        schema (Any, optional): JSON Schema dict, boolean schema, or pydantic v2 model used to guide repairs and validation for both valid and invalid JSON inputs.
        schema_repair_mode (Literal["standard", "salvage"], optional): Schema repair mode. "salvage" requires schema.

    Returns:
        Union[JSONReturnType, Tuple[JSONReturnType, List[Dict[str, str]]], str]: The repaired JSON object or a tuple with the repaired JSON object and repair log.
    """
    return repair_json(
        json_str=json_str,
        return_objects=True,
        skip_json_loads=skip_json_loads,
        logging=logging,
        stream_stable=stream_stable,
        strict=strict,
        schema=schema,
        schema_repair_mode=schema_repair_mode,
    )


def load(
    fd: TextIO,
    skip_json_loads: bool = False,
    logging: bool = False,
    chunk_length: int = 0,
    strict: bool = False,
    schema: Any | None = None,
    schema_repair_mode: Literal["standard", "salvage"] = "standard",
) -> JSONReturnType | tuple[JSONReturnType, list[dict[str, str]]]:
    """
    This function works like `json.load()` except that it will fix your JSON in the process.
    It is a wrapper around the `repair_json()` function with `json_fd=fd` and `return_objects=True`.

    Args:
        fd (TextIO): File descriptor for JSON input.
        skip_json_loads (bool, optional): If True, skip calling the built-in json.loads() function to verify that the json is valid before attempting to repair. Defaults to False.
        logging (bool, optional): If True, return a tuple with the repaired json and a log of all repair actions. Defaults to False.
        chunk_length (int, optional): Size in bytes of the file chunks to read at once. Defaults to 1MB.
        strict (bool, optional): If True, surface structural problems (duplicate keys, missing separators, empty keys/values, etc.) as ValueError instead of repairing them.
        schema (Any, optional): JSON Schema dict, boolean schema, or pydantic v2 model used to guide repairs and validation for both valid and invalid JSON inputs.
        schema_repair_mode (Literal["standard", "salvage"], optional): Schema repair mode. "salvage" requires schema.

    Returns:
        Union[JSONReturnType, Tuple[JSONReturnType, List[Dict[str, str]]]]: The repaired JSON object or a tuple with the repaired JSON object and repair log.
    """
    return repair_json(
        json_fd=fd,
        chunk_length=chunk_length,
        return_objects=True,
        skip_json_loads=skip_json_loads,
        logging=logging,
        strict=strict,
        schema=schema,
        schema_repair_mode=schema_repair_mode,
    )


def from_file(
    filename: str | Path,
    skip_json_loads: bool = False,
    logging: bool = False,
    chunk_length: int = 0,
    strict: bool = False,
    schema: Any | None = None,
    schema_repair_mode: Literal["standard", "salvage"] = "standard",
) -> JSONReturnType | tuple[JSONReturnType, list[dict[str, str]]]:
    """
    This function is a wrapper around `load()` so you can pass the filename as string

    Args:
        filename (str | Path): The name of the file containing JSON data to load and repair.
        skip_json_loads (bool, optional): If True, skip calling the built-in json.loads() function to verify that the json is valid before attempting to repair. Defaults to False.
        logging (bool, optional): If True, return a tuple with the repaired json and a log of all repair actions. Defaults to False.
        chunk_length (int, optional): Size in bytes of the file chunks to read at once. Defaults to 1MB.
        strict (bool, optional): If True, surface structural problems (duplicate keys, missing separators, empty keys/values, etc.) as ValueError instead of repairing them.
        schema (Any, optional): JSON Schema dict, boolean schema, or pydantic v2 model used to guide repairs and validation for both valid and invalid JSON inputs.
        schema_repair_mode (Literal["standard", "salvage"], optional): Schema repair mode. "salvage" requires schema.

    Returns:
        Union[JSONReturnType, Tuple[JSONReturnType, List[Dict[str, str]]]]: The repaired JSON object or a tuple with the repaired JSON object and repair log.
    """
    with Path(filename).open() as fd:
        return load(
            fd=fd,
            skip_json_loads=skip_json_loads,
            logging=logging,
            chunk_length=chunk_length,
            strict=strict,
            schema=schema,
            schema_repair_mode=schema_repair_mode,
        )


def cli(inline_args: list[str] | None = None) -> int:
    """
    Command-line interface for repairing and parsing JSON files.

    Args:
        inline_args (Optional[List[str]]): List of command-line arguments for testing purposes. Defaults to None.
            - filename (str): The JSON file to repair. If omitted, the JSON is read from stdin.
            - -i, --inline (bool): Replace the file inline instead of returning the output to stdout.
            - -o, --output TARGET (str): If specified, the output will be written to TARGET filename instead of stdout.
            - --ensure_ascii (bool): Pass ensure_ascii=True to json.dumps(). Will pass False otherwise.
            - --indent INDENT (int): Number of spaces for indentation (Default 2).
            - --skip-json-loads (bool): Skip initial json.loads validation.
            - --schema SCHEMA (str): Path to a JSON Schema file that guides repairs.
            - --schema-model MODEL (str): Pydantic v2 model in 'module:ClassName' form that guides repairs.
            - --strict (bool): Raise on duplicate keys, missing separators, empty keys/values, and other unrecoverable structures instead of repairing them.

    Returns:
        int: Exit code of the CLI operation.

    Raises:
        Exception: Any exception that occurs during file processing.

    Example:
        >>> cli(['example.json', '--indent', '4'])
        >>> cat json.txt | json_repair
    """
    parser = argparse.ArgumentParser(description="Repair and parse JSON files.")
    # Make the filename argument optional; if omitted, we will read from stdin.
    parser.add_argument(
        "filename",
        nargs="?",
        help="The JSON file to repair (if omitted, reads from stdin)",
    )
    parser.add_argument(
        "-i",
        "--inline",
        action="store_true",
        help="Replace the file inline instead of returning the output to stdout",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="TARGET",
        help="If specified, the output will be written to TARGET filename instead of stdout",
    )
    parser.add_argument(
        "--ensure_ascii",
        action="store_true",
        help="Pass ensure_ascii=True to json.dumps()",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Number of spaces for indentation (Default 2)",
    )
    parser.add_argument(
        "--skip-json-loads",
        action="store_true",
        help="Skip initial json.loads validation",
    )
    parser.add_argument(
        "--schema",
        metavar="SCHEMA",
        help="Path to a JSON Schema file that guides repairs",
    )
    parser.add_argument(
        "--schema-model",
        metavar="MODEL",
        help="Pydantic v2 model in 'module:ClassName' form that guides repairs",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Raise on duplicate keys, missing separators, empty keys/values, and other unrecoverable structures instead of repairing them",
    )
    parser.add_argument(
        "--schema-repair-mode",
        choices=["standard", "salvage"],
        default="standard",
        help="Schema repair mode: 'standard' (default) or 'salvage' (best-effort array/object salvage).",
    )

    args = parser.parse_args(inline_args)

    # Inline mode requires a filename, so error out if none was provided.
    if args.inline and not args.filename:  # pragma: no cover
        print("Error: Inline mode requires a filename", file=sys.stderr)
        sys.exit(1)

    if args.inline and args.output:  # pragma: no cover
        print("Error: You cannot pass both --inline and --output", file=sys.stderr)
        sys.exit(1)

    if args.schema and args.schema_model:
        print("Error: You cannot pass both --schema and --schema-model", file=sys.stderr)
        sys.exit(1)

    if args.strict and (args.schema or args.schema_model):
        print("Error: --strict cannot be used with --schema or --schema-model", file=sys.stderr)
        sys.exit(1)
    if args.schema_repair_mode == "salvage" and not (args.schema or args.schema_model):
        print("Error: --schema-repair-mode salvage requires --schema or --schema-model", file=sys.stderr)
        sys.exit(1)

    ensure_ascii = args.ensure_ascii

    try:
        schema = None
        if args.schema:
            with Path(args.schema).open() as fd:
                schema = json.load(fd)
        elif args.schema_model:
            schema = load_schema_model(args.schema_model)

        # Use from_file if a filename is provided; otherwise read from stdin.
        if args.filename:
            result = from_file(
                args.filename,
                skip_json_loads=args.skip_json_loads,
                strict=args.strict,
                schema=schema,
                schema_repair_mode=args.schema_repair_mode,
            )
        else:
            data = sys.stdin.read()
            result = loads(
                data,
                skip_json_loads=args.skip_json_loads,
                strict=args.strict,
                schema=schema,
                schema_repair_mode=args.schema_repair_mode,
            )
        if args.inline or args.output:
            with Path(args.output or args.filename).open(mode="w") as fd:
                json.dump(result, fd, indent=args.indent, ensure_ascii=ensure_ascii)
        else:
            print(json.dumps(result, indent=args.indent, ensure_ascii=ensure_ascii))
    except (OSError, TypeError, ValueError) as e:  # pragma: no cover
        print(f"Error: {e!s}", file=sys.stderr)
        return 1

    return 0  # Success


if __name__ == "__main__":  # pragma: no cover
    sys.exit(cli())

```

### `src/json_repair/parse_array.py`

```py
from typing import TYPE_CHECKING, Any, cast

from .parser_schema import ArraySchemaConfig, resolve_parser_array_schema
from .utils.constants import STRING_DELIMITERS, JSONReturnType
from .utils.json_context import ContextValues
from .utils.object_comparer import ObjectComparer

if TYPE_CHECKING:
    from .json_parser import JSONParser


def _resolve_array_item_schema(
    schema_config: ArraySchemaConfig | None,
    idx: int,
) -> tuple[dict[str, Any] | bool | None, bool]:
    if schema_config is None:
        return None, False

    item_schema: dict[str, Any] | bool | None = None
    drop_item = False
    if isinstance(schema_config.items_schema, list):
        if idx < len(schema_config.items_schema):
            raw_schema = schema_config.items_schema[idx]
            if raw_schema is not None and not isinstance(raw_schema, (dict, bool)):
                raise ValueError("Schema must be an object.")
            item_schema = cast("dict[str, Any] | bool | None", raw_schema)
        elif schema_config.additional_items is False:
            drop_item = True
        elif isinstance(schema_config.additional_items, dict):
            item_schema = cast("dict[str, Any]", schema_config.additional_items)
        else:
            item_schema = True
    elif isinstance(schema_config.items_schema, dict):
        item_schema = cast("dict[str, Any]", schema_config.items_schema)
    else:
        item_schema = True

    return item_schema, drop_item


def parse_array(
    self: "JSONParser",
    schema: dict[str, Any] | bool | None = None,
    path: str = "$",
    closing_delimiter: str = "]",
) -> list[JSONReturnType]:
    # <array> ::= '[' [ <json> *(', ' <json>) ] ']' ; A sequence of JSON values separated by commas
    schema_repairer, _schema, schema_config = resolve_parser_array_schema(self.schema_repairer, schema)
    salvage_mode = schema_repairer is not None and schema_repairer.schema_repair_mode == "salvage"
    array_is_object_value = self.context.current == ContextValues.OBJECT_VALUE
    closed_before_parent_member = False

    arr: list[JSONReturnType] = []
    with self.context.enter(ContextValues.ARRAY):
        self.skip_whitespaces()
        char = self.get_char_at()
        idx = 0
        while char and char not in [closing_delimiter, "}"]:
            item_schema, drop_item = _resolve_array_item_schema(schema_config, idx)
            item_path = f"{path}[{idx}]"
            active_schema_repairer = (
                schema_repairer if schema_repairer is not None and not drop_item and not salvage_mode else None
            )

            if char in STRING_DELIMITERS:
                # A string followed by ':' is often a missing object start; treat it as an object.
                i = 1
                i = self.skip_to_character(char, i)
                i = self.scroll_whitespaces(idx=i + 1)
                if self.get_char_at(i) == ":":
                    if array_is_object_value and arr and all(not isinstance(item, (dict, list)) for item in arr):
                        self.log("Closed unclosed array before object member after scalar items")
                        closed_before_parent_member = True
                        break
                    if active_schema_repairer is not None:
                        # Schema-guided object parsing, then enforce schema on the parsed object.
                        value = self.parse_object(item_schema, item_path)
                        value = active_schema_repairer.repair_value(value, item_schema, item_path)
                    else:
                        # No schema (or dropping): still parse to keep the cursor in sync.
                        value = self.parse_object()
                else:
                    value = self.parse_string()
                    if active_schema_repairer is not None:
                        # Apply schema constraints/coercions to scalar values when configured.
                        value = active_schema_repairer.repair_value(value, item_schema, item_path)
            else:
                # Use schema-aware parsing to guide nested repairs when configured.
                value = (
                    self.parse_json(item_schema, item_path) if active_schema_repairer is not None else self.parse_json()
                )

            if ObjectComparer.is_strictly_empty(value) and self.get_char_at() not in [closing_delimiter, ","]:
                self.index += 1
            elif value == "..." and self.get_char_at(-1) == ".":
                self.log(
                    "While parsing an array, found a stray '...'; ignoring it",
                )
            elif not drop_item:
                arr.append(value)
            elif schema_repairer is not None:
                # Record drops for visibility when schema forbids extra tuple items.
                schema_repairer._log("Dropped extra array item not covered by schema", item_path)

            idx += 1
            char = self.get_char_at()
            while char and char != closing_delimiter and (char.isspace() or char == ","):
                self.index += 1
                char = self.get_char_at()

        if char != closing_delimiter:
            self.log(
                f"While parsing an array we missed the closing {closing_delimiter}, ignoring it",
            )

        if not closed_before_parent_member:
            self.index += 1

    return arr

```

### `src/json_repair/parse_comment.py`

```py
from typing import TYPE_CHECKING

from .utils.constants import JSONReturnType
from .utils.json_context import ContextValues

if TYPE_CHECKING:
    from .json_parser import JSONParser


def parse_comment(self: "JSONParser", record_top_level_value: bool = False) -> JSONReturnType:
    """
    Parse code-like comments:

    - "# comment": A line comment that continues until a newline.
    - "// comment": A line comment that continues until a newline.
    - "/* comment */": A block comment that continues until the closing delimiter "*/".

    The comment is skipped over and an empty string is returned so that comments do not interfere
    with the actual JSON elements.
    """
    while True:
        char = self.get_char_at()
        termination_characters = ["\n", "\r"]
        if ContextValues.ARRAY in self.context.context:
            termination_characters.append("]")
        if ContextValues.OBJECT_VALUE in self.context.context:
            termination_characters.append("}")
        if ContextValues.OBJECT_KEY in self.context.context:
            termination_characters.append(":")
        # Line comment starting with #
        if char == "#":
            comment = ""
            while char and char not in termination_characters:
                comment += char
                self.index += 1
                char = self.get_char_at()
            self.log(f"Found line comment: {comment}, ignoring")
        # Comments starting with '/'
        elif char == "/":
            next_char = self.get_char_at(1)
            # Handle line comment starting with //
            if next_char == "/":
                comment = "//"
                self.index += 2  # Skip both slashes.
                char = self.get_char_at()
                while char and char not in ["\n", "\r"]:
                    comment += char
                    self.index += 1
                    char = self.get_char_at()
                self.log(f"Found line comment: {comment}, ignoring")
            # Handle block comment starting with /*
            elif next_char == "*":
                comment = "/*"
                self.index += 2  # Skip '/*'
                while True:
                    char = self.get_char_at()
                    if not char:
                        self.log("Reached end-of-string while parsing block comment; unclosed block comment.")
                        break
                    comment += char
                    self.index += 1
                    if comment.endswith("*/"):
                        break
                self.log(f"Found block comment: {comment}, ignoring")
            else:
                # Skip standalone '/' characters that are not part of a comment
                # to avoid getting stuck in an infinite loop
                self.index += 1
        if self.context.empty:
            # Avoid a parse_json -> parse_comment -> parse_json chain for long runs of
            # top-level comments; re-enter only once after we have consumed them all.
            self.skip_whitespaces()
            if self.get_char_at() in ["#", "/"]:
                continue
            return self.parse_json(record_top_level_value=record_top_level_value)
        break
    return ""

```

### `src/json_repair/parse_number.py`

```py
from typing import TYPE_CHECKING

from .utils.constants import JSONReturnType
from .utils.json_context import ContextValues

NUMBER_CHARS: set[str] = set("0123456789-.eE/,_")


if TYPE_CHECKING:
    from .json_parser import JSONParser


def parse_number(self: "JSONParser") -> JSONReturnType:
    # <number> is a valid real number expressed in one of a number of given formats
    number_str = ""
    char = self.get_char_at()
    is_array = self.context.current == ContextValues.ARRAY
    while char and char in NUMBER_CHARS and (not is_array or char != ","):
        if char != "_":
            number_str += char
        self.index += 1
        char = self.get_char_at()
    if (self.get_char_at() or "").isalpha():
        # this was a string instead, sorry
        self.index -= len(number_str)
        return self.parse_string()
    if number_str and number_str[-1] in "-eE/,":
        # The number ends with a non valid character for a number/currency, rolling back one
        number_str = number_str[:-1]
        self.index -= 1
    try:
        if "," in number_str:
            return number_str
        if "." in number_str or "e" in number_str or "E" in number_str:
            return float(number_str)
        return int(number_str)
    except ValueError:
        return number_str

```

### `src/json_repair/parse_object.py`

```py
from typing import TYPE_CHECKING, Any, cast

from .parser_schema import ObjectSchemaConfig, resolve_parser_object_schema
from .utils.constants import MISSING_VALUE, STRING_DELIMITERS, JSONReturnType
from .utils.json_context import ContextValues
from .utils.pattern_properties import match_pattern_properties

if TYPE_CHECKING:
    from .json_parser import JSONParser
    from .schema_repair import SchemaRepairer


def _finalize_object(
    obj: dict[str, JSONReturnType],
    schema_repairer: "SchemaRepairer | None",
    schema_config: ObjectSchemaConfig | None,
    path: str,
) -> dict[str, JSONReturnType]:
    if schema_repairer is None or schema_config is None:
        return obj

    missing_required = [key for key in schema_config.required if key not in obj]
    if missing_required and schema_repairer.schema_repair_mode != "salvage":
        raise ValueError(f"Missing required properties at {path}: {', '.join(missing_required)}")

    for key, prop_schema in schema_config.properties.items():
        if key in obj or key in schema_config.required:
            continue
        if isinstance(prop_schema, dict) and "default" in prop_schema:
            obj[key] = schema_repairer._copy_json_value(prop_schema["default"], f"{path}.{key}", "default")
            schema_repairer._log("Inserted default value for missing property", f"{path}.{key}")
    return obj


def _strip_comments_for_empty_object_classification(body: str) -> str:
    stripped = []
    in_quote: str | None = None
    backslashes = 0
    index = 0
    while index < len(body):
        char = body[index]
        next_char = body[index + 1] if index + 1 < len(body) else ""

        if char == "\\":
            backslashes += 1
            stripped.append(char)
            index += 1
            continue
        if in_quote is not None:
            stripped.append(char)
            if char == in_quote and backslashes % 2 == 0:
                in_quote = None
            backslashes = 0
            index += 1
            continue
        if char in STRING_DELIMITERS and backslashes % 2 == 0:
            in_quote = char
            stripped.append(char)
            backslashes = 0
            index += 1
            continue
        backslashes = 0

        if char == "#" or (char == "/" and next_char == "/"):
            index += 2 if char == "/" else 1
            while index < len(body) and body[index] not in ["\n", "\r"]:
                index += 1
            continue
        if char == "/" and next_char == "*":
            index += 2
            while index < len(body) - 1 and body[index : index + 2] != "*/":
                index += 1
            index = min(index + 2, len(body))
            continue

        stripped.append(char)
        index += 1

    return "".join(stripped)


def _classify_empty_object_repair(
    self: "JSONParser",
    start_index: int,
    schema: dict[str, Any] | bool | None,
    schema_repairer: "SchemaRepairer | None",
) -> tuple[str, str | None]:
    attempted_object = self.json_str[start_index - 1 : self.index + 1]
    body = attempted_object[1:]
    body = body.removesuffix("}")
    body = body.lstrip()
    if not body:
        return "keep", None
    if (body.startswith('\\"') and '\\":' in body) or (body.startswith("\\'") and "\\':" in body):
        normalized_object = attempted_object.replace('\\"', '"').replace("\\'", "'")
        self.log(
            "Parsed object is empty but the input starts like an escaped object key, normalizing and reparsing it as an object",
        )
        return "object", normalized_object
    body = _strip_comments_for_empty_object_classification(body).lstrip()
    if not body:
        return "keep", None

    in_quote: str | None = None
    backslashes = 0
    for char in body:
        if char == "\\":
            backslashes += 1
            continue
        if in_quote is not None:
            if char == in_quote and backslashes % 2 == 0:
                in_quote = None
        elif char in STRING_DELIMITERS and backslashes % 2 == 0:
            in_quote = char
        elif char == ":" and backslashes % 2 == 0:
            self.log(
                "Parsed object is empty but the input still contains an object-style separator, keeping object repair",
            )
            return "keep", None
        backslashes = 0
    if (
        schema_repairer is not None
        and schema_repairer.schema_repair_mode == "salvage"
        and isinstance(schema, dict)
        and schema_repairer.is_object_schema(schema)
        and not schema_repairer.is_array_schema(schema)
    ):
        return "schema_set_object", None
    return "array", None


def _merge_object_array_continuation(
    self: "JSONParser",
    obj: dict[str, JSONReturnType],
) -> bool:
    prev_key = list(obj.keys())[-1] if obj else None
    if not prev_key or not isinstance(obj[prev_key], list) or self.strict:
        return False

    self.index += 1
    new_array = self.parse_array()
    if isinstance(new_array, list):
        prev_value = obj[prev_key]
        if isinstance(prev_value, list):
            list_lengths = [len(item) for item in prev_value if isinstance(item, list)]
            expected_len = (
                list_lengths[0] if list_lengths and all(length == list_lengths[0] for length in list_lengths) else None
            )
            if expected_len:
                tail = []
                while prev_value and not isinstance(prev_value[-1], list):
                    tail.append(prev_value.pop())
                if tail:
                    tail.reverse()
                    if len(tail) % expected_len == 0:
                        self.log(
                            "While parsing an object we found row values without an inner array, grouping them into rows",
                        )
                        for i in range(0, len(tail), expected_len):
                            prev_value.append(tail[i : i + expected_len])
                    else:
                        prev_value.extend(tail)
                if new_array:
                    if all(isinstance(item, list) for item in new_array):
                        self.log(
                            "While parsing an object we found additional rows, appending them without flattening",
                        )
                        prev_value.extend(new_array)
                    else:
                        prev_value.append(new_array)
            else:
                prev_value.extend(new_array[0] if len(new_array) == 1 and isinstance(new_array[0], list) else new_array)

    self.skip_whitespaces()
    if self.get_char_at() == ",":
        self.index += 1
    self.skip_whitespaces()
    return True


def _parse_object_key(
    self: "JSONParser",
    obj: dict[str, JSONReturnType],
) -> tuple[str, int]:
    key = ""
    rollback_index = self.index
    self.context.set(ContextValues.OBJECT_KEY)
    try:
        while self.get_char_at():
            rollback_index = self.index
            if self.get_char_at() == "[" and key == "" and _merge_object_array_continuation(self, obj):
                continue

            raw_key = self.parse_string()
            assert isinstance(raw_key, str)
            key = raw_key
            if key == "":
                self.skip_whitespaces()
            if key != "" or (key == "" and self.get_char_at() in [":", "}"]):
                if key == "" and self.strict:
                    self.log(
                        "Empty key found in strict mode while parsing object, raising an error",
                    )
                    raise ValueError("Empty key found in strict mode while parsing object.")
                break
    finally:
        self.context.reset()
    return key, rollback_index


def _should_split_duplicate_object(self: "JSONParser", rollback_index: int) -> bool:
    lookback_idx = rollback_index - self.index - 1
    prev_non_whitespace = self.get_char_at(lookback_idx)
    while prev_non_whitespace and prev_non_whitespace.isspace():
        lookback_idx -= 1
        prev_non_whitespace = self.get_char_at(lookback_idx)
    key_start_char = self.get_char_at(rollback_index - self.index)
    next_non_whitespace = self.get_char_at(self.scroll_whitespaces())
    return not (key_start_char in STRING_DELIMITERS and prev_non_whitespace == "," and next_non_whitespace == ":")


def _split_object_on_duplicate_key(self: "JSONParser", rollback_index: int) -> None:
    self.index = rollback_index - 1
    self.json_str = self.json_str[: self.index + 1] + "{" + self.json_str[self.index + 1 :]


def _resolve_object_property_schema(
    self: "JSONParser",
    schema_repairer: "SchemaRepairer | None",
    schema_config: ObjectSchemaConfig | None,
    key: str,
) -> tuple[dict[str, Any] | bool | None, list[dict[str, Any] | bool | None], bool]:
    if schema_repairer is None or schema_config is None:
        return None, [], False

    prop_schema: dict[str, Any] | bool | None = None
    extra_schemas: list[dict[str, Any] | bool | None] = []
    if key in schema_config.properties:
        schema_value = schema_config.properties[key]
        if schema_value is not None and not isinstance(schema_value, (dict, bool)):
            raise ValueError("Schema must be an object.")
        prop_schema = cast("dict[str, Any] | bool | None", schema_value)
        return prop_schema, extra_schemas, False

    matched: list[Any] = []
    unsupported_patterns: list[str] = []
    if schema_config.pattern_properties:
        matched, unsupported_patterns = match_pattern_properties(schema_config.pattern_properties, key)
    for pattern in unsupported_patterns:
        self.log(
            f"Skipped unsupported patternProperties regex '{pattern}' while parsing object key '{key}'",
        )
    if matched:
        primary_schema = matched[0]
        if primary_schema is not None and not isinstance(primary_schema, (dict, bool)):
            raise ValueError("Schema must be an object.")
        prop_schema = cast("dict[str, Any] | bool | None", primary_schema)
        for extra_schema in matched[1:]:
            if extra_schema is not None and not isinstance(extra_schema, (dict, bool)):
                raise ValueError("Schema must be an object.")
            extra_schemas.append(cast("dict[str, Any] | bool | None", extra_schema))
        return prop_schema, extra_schemas, False

    if schema_config.additional_properties is False:
        return None, [], True
    if isinstance(schema_config.additional_properties, dict):
        return cast("dict[str, Any]", schema_config.additional_properties), [], False
    return True, [], False


def _parse_object_value(
    self: "JSONParser",
    schema_repairer: "SchemaRepairer | None",
    prop_schema: dict[str, Any] | bool | None,
    key_path: str,
) -> JSONReturnType:
    self.context.set(ContextValues.OBJECT_VALUE)
    try:
        self.skip_whitespaces()
        char = self.get_char_at()
        if char in [",", "}"]:
            self.log(
                f"While parsing an object value we found a stray {char}, ignoring it",
            )
            if schema_repairer is not None:
                return schema_repairer.repair_value(MISSING_VALUE, prop_schema, key_path)
            return ""

        if schema_repairer is not None:
            return self.parse_json(prop_schema, key_path)
        return self.parse_json()
    finally:
        self.context.reset()


def _repair_empty_object_result(
    self: "JSONParser",
    obj: dict[str, JSONReturnType],
    start_index: int,
    schema: dict[str, Any] | bool | None,
    path: str,
    schema_repairer: "SchemaRepairer | None",
) -> tuple[bool, JSONReturnType]:
    if obj or self.index - start_index <= 2:
        return False, None

    if self.strict:
        self.log(
            "Parsed object is empty but contains extra characters in strict mode, raising an error",
        )
        raise ValueError("Parsed object is empty but contains extra characters in strict mode.")

    empty_object_repair, normalized_object = _classify_empty_object_repair(self, start_index, schema, schema_repairer)
    if empty_object_repair == "object" and normalized_object is not None:
        end_index = self.index + 1
        self.json_str = self.json_str[: start_index - 1] + normalized_object + self.json_str[end_index:]
        self.index = start_index
        with self.context.enter(ContextValues.OBJECT_KEY):
            repaired_value = self.parse_object(schema, path)
        self.deferred_contexts.append(ContextValues.OBJECT_KEY)
        return True, repaired_value
    if empty_object_repair == "schema_set_object":
        self.log(
            "Parsed object is empty but salvage schema expects an object, reparsing set-like members as null-valued object keys",
        )
        self.index = start_index
        with self.context.enter(ContextValues.OBJECT_KEY):
            set_items = self.parse_array()
        self.deferred_contexts.append(ContextValues.OBJECT_KEY)
        if isinstance(set_items, list):
            key_candidates: list[str] = [item for item in set_items if isinstance(item, str) and item]
            if len(key_candidates) == len(set_items):
                return True, cast("JSONReturnType", dict.fromkeys(key_candidates))
        return True, set_items
    if empty_object_repair == "array":
        self.log("Parsed object is empty, we will try to parse this as an array instead")
        self.index = start_index
        with self.context.enter(ContextValues.OBJECT_KEY):
            repaired_array = self.parse_array()
        self.deferred_contexts.append(ContextValues.OBJECT_KEY)
        return True, repaired_array
    return False, None


def _complete_object_parse(
    self: "JSONParser",
    obj: dict[str, JSONReturnType],
    schema: dict[str, Any] | bool | None,
    path: str,
    schema_repairer: "SchemaRepairer | None",
    schema_config: ObjectSchemaConfig | None,
) -> JSONReturnType:
    if not self.context.empty:
        if self.get_char_at() == "}" and self.context.current not in [
            ContextValues.OBJECT_KEY,
            ContextValues.OBJECT_VALUE,
        ]:
            self.log(
                "Found an extra closing brace that shouldn't be there, skipping it",
            )
            self.index += 1
        return obj

    self.skip_whitespaces()
    if self.get_char_at() == ",":
        self.index += 1
        self.skip_whitespaces()
        if self.get_char_at() in STRING_DELIMITERS and not self.strict:
            self.log(
                "Found a comma and string delimiter after object closing brace, checking for additional key-value pairs",
            )
            additional_obj = self.parse_object(schema, path)
            if isinstance(additional_obj, dict):
                obj.update(additional_obj)

    return _finalize_object(obj, schema_repairer, schema_config, path)


def parse_object(
    self: "JSONParser",
    schema: dict[str, Any] | bool | None = None,
    path: str = "$",
) -> JSONReturnType:
    # <object> ::= '{' [ <member> *(', ' <member>) ] '}' ; A sequence of 'members'
    obj: dict[str, JSONReturnType] = {}
    start_index = self.index
    parsing_object_value = self.context.current == ContextValues.OBJECT_VALUE
    schema_repairer, schema, schema_config = resolve_parser_object_schema(self.schema_repairer, schema)

    while (self.get_char_at() or "}") != "}":
        self.skip_whitespaces()

        if self.get_char_at() == ":":
            self.log(
                "While parsing an object we found a : before a key, ignoring",
            )
            self.index += 1

        key, rollback_index = _parse_object_key(self, obj)
        if ContextValues.ARRAY in self.context.context and key in obj:
            if self.strict:
                self.log("Duplicate key found in strict mode while parsing object, raising an error")
                raise ValueError("Duplicate key found in strict mode while parsing object.")
            if not parsing_object_value:
                if _should_split_duplicate_object(self, rollback_index):
                    self.log(
                        "While parsing an object we found a duplicate key, closing the object here and rolling back the index",
                    )
                    _split_object_on_duplicate_key(self, rollback_index)
                    break
                self.log(
                    "While parsing an object we found a duplicate key with a normal comma separator, keeping duplicate-key overwrite behavior",
                )

        self.skip_whitespaces()
        if (self.get_char_at() or "}") == "}":
            continue

        self.skip_whitespaces()
        if self.get_char_at() != ":":
            if self.strict:
                self.log(
                    "Missing ':' after key in strict mode while parsing object, raising an error",
                )
                raise ValueError("Missing ':' after key in strict mode while parsing object.")
            self.log(
                "While parsing an object we missed a : after a key",
            )

        self.index += 1
        prop_schema, extra_schemas, drop_property = _resolve_object_property_schema(
            self,
            schema_repairer,
            schema_config,
            key,
        )
        key_path = f"{path}.{key}"
        value = _parse_object_value(self, schema_repairer, prop_schema, key_path)

        if schema_repairer is not None:
            for extra_schema in extra_schemas:
                value = schema_repairer.repair_value(value, extra_schema, key_path)

        if schema_repairer is None and value == "" and self.strict and self.get_char_at(-1) not in STRING_DELIMITERS:
            self.log(
                "Parsed value is empty in strict mode while parsing object, raising an error",
            )
            raise ValueError("Parsed value is empty in strict mode while parsing object.")

        if schema_repairer is None or not drop_property:
            obj[key] = value
        else:
            schema_repairer._log("Dropped extra property not covered by schema", key_path)

        if self.get_char_at() in [",", "'", '"']:
            self.index += 1
        if self.get_char_at() == "]" and ContextValues.ARRAY in self.context.context:
            self.log(
                "While parsing an object we found a closing array bracket, closing the object here and rolling back the index"
            )
            self.index -= 1
            break
        self.skip_whitespaces()

    self.index += 1

    repaired_empty_object, repaired_value = _repair_empty_object_result(
        self,
        obj,
        start_index,
        schema,
        path,
        schema_repairer,
    )
    if repaired_empty_object:
        return repaired_value

    return _complete_object_parse(
        self,
        obj,
        schema,
        path,
        schema_repairer,
        schema_config,
    )

```

### `src/json_repair/parse_string_helpers/__init__.py`

```py
"""Helpers used by string parsing."""

```

### `src/json_repair/parse_string_helpers/object_value_context.py`

```py
from collections.abc import Callable
from typing import TYPE_CHECKING, Literal

from ..utils.constants import STRING_DELIMITERS  # noqa: TID252

if TYPE_CHECKING:
    from ..json_parser import JSONParser  # noqa: TID252


ObjectValueCommaClassification = Literal["container", "member", "string", "string_no_future_delimiter"]


def _bare_member_has_recoverable_value(
    parser: "JSONParser",
    value_idx: int,
    skip_to_character: Callable[[str | list[str], int], int],
) -> bool:
    value_start_idx = parser.scroll_whitespaces(idx=value_idx)
    value_start = parser.get_char_at(value_start_idx)
    if value_start in [*STRING_DELIMITERS, "{", "[", "-"]:
        return True
    if value_start and value_start.isdigit():
        return True

    for literal in ["true", "false", "null"]:
        if all(parser.get_char_at(value_start_idx + offset) == char for offset, char in enumerate(literal)):
            value_end = parser.get_char_at(value_start_idx + len(literal))
            if value_end is None or value_end.isspace() or value_end in [",", "}", "]"]:
                return True

    # An unquoted value is only a safe member boundary when its object closes
    # before the current string can close. Otherwise prose such as
    # `, floof: explanation` is more likely to belong to the string.
    value_end_idx = skip_to_character([*STRING_DELIMITERS, "}"], value_start_idx)
    return parser.get_char_at(value_end_idx) == "}"


def classify_object_value_comma(
    parser: "JSONParser",
    cached_skip_to_character: Callable[[str | list[str], int], int] | None = None,
) -> ObjectValueCommaClassification:
    skip_to_character = cached_skip_to_character or parser.skip_to_character
    next_idx = parser.scroll_whitespaces(idx=1)
    next_c = parser.get_char_at(next_idx)
    if next_c in ["}", None]:
        return "member"

    if next_c in STRING_DELIMITERS:
        key_end_idx = parser.skip_to_character(character=next_c, idx=next_idx + 1)
        if not parser.get_char_at(key_end_idx):
            return "string"
        key_end_idx = parser.scroll_whitespaces(idx=key_end_idx + 1)
        return "member" if parser.get_char_at(key_end_idx) == ":" else "string"

    if next_c == "`":
        bare_key_idx = next_idx + 1
        while True:
            key_char = parser.get_char_at(bare_key_idx)
            if not key_char or not (key_char.isalnum() or key_char in ["_", "-"]):
                break
            bare_key_idx += 1
        bare_key_idx = parser.scroll_whitespaces(idx=bare_key_idx)
        return "member" if parser.get_char_at(bare_key_idx) == ":" else "string"

    if next_c and (next_c.isalnum() or next_c == "_"):
        bare_key_idx = next_idx
        while True:
            key_char = parser.get_char_at(bare_key_idx)
            if not key_char or not (key_char.isalnum() or key_char in ["_", "-"]):
                break
            bare_key_idx += 1
        bare_key_idx = parser.scroll_whitespaces(idx=bare_key_idx)
        if parser.get_char_at(bare_key_idx) == ":" and _bare_member_has_recoverable_value(
            parser,
            bare_key_idx + 1,
            skip_to_character,
        ):
            return "member"

    if next_c in ["{", "["]:
        return "container"

    next_special_idx = skip_to_character([*STRING_DELIMITERS, "{", "["], next_idx)
    next_special = parser.get_char_at(next_special_idx)
    if not next_special:
        return "string_no_future_delimiter"
    if next_special in ["{", "["]:
        return "string"

    key_end_idx = skip_to_character(next_special, next_special_idx + 1)
    if not parser.get_char_at(key_end_idx):
        return "string"
    key_end_idx = parser.scroll_whitespaces(idx=key_end_idx + 1)
    return "member" if parser.get_char_at(key_end_idx) == ":" else "string"


def update_inline_container_stack(
    char: str,
    pending_inline_container: bool,
    inline_container_stack: list[str],
) -> tuple[bool, bool]:
    if char in ["{", "["]:
        if pending_inline_container:
            inline_container_stack.append(char)
            return False, False
        if inline_container_stack:
            inline_container_stack.append(char)

    if inline_container_stack and (
        (char == "}" and inline_container_stack[-1] == "{") or (char == "]" and inline_container_stack[-1] == "[")
    ):
        inline_container_stack.pop()
        return pending_inline_container, True

    return pending_inline_container, False

```

### `src/json_repair/parse_string_helpers/parse_boolean_or_null.py`

```py
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..json_parser import JSONParser  # noqa: TID252


LITERAL_VALUES: dict[str, bool | None] = {
    "true": True,
    "false": False,
    "null": None,
    "none": None,
}


def parse_boolean_or_null(parser: "JSONParser") -> tuple[bool, bool | None]:
    """Return whether an unquoted complete literal was found and its value."""
    char = (parser.get_char_at() or "").lower()
    starting_index = parser.index
    for literal, value in LITERAL_VALUES.items():
        if char != literal[0]:
            continue
        parser.index = starting_index
        for expected_char in literal:
            if (parser.get_char_at() or "").lower() != expected_char:
                break
            parser.index += 1
        else:
            next_char = parser.get_char_at()
            if next_char is None or next_char.isspace() or next_char in {",", ")", "]", "}"}:
                if literal == "none":
                    parser.log("Converted unquoted Python None literal to JSON null")
                return True, value

    parser.index = starting_index
    return False, None

```

### `src/json_repair/parse_string_helpers/parse_json_llm_block.py`

```py
from typing import TYPE_CHECKING

from ..utils.constants import JSONReturnType  # noqa: TID252

if TYPE_CHECKING:
    from ..json_parser import JSONParser  # noqa: TID252


def parse_json_llm_block(parser: "JSONParser") -> JSONReturnType:
    """
    Extracts and normalizes JSON enclosed in ```json ... ``` blocks.
    """
    # Try to find a ```json ... ``` block
    if parser.json_str[parser.index : parser.index + 7] == "```json":
        i = parser.skip_to_character("`", idx=7)
        if parser.json_str[parser.index + i : parser.index + i + 3] == "```":
            parser.index += 7  # Move past ```json
            return parser.parse_json()
    return False

```

### `src/json_repair/parse_string.py`

```py
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, cast

from .parse_string_helpers.object_value_context import classify_object_value_comma, update_inline_container_stack
from .parse_string_helpers.parse_boolean_or_null import parse_boolean_or_null
from .parse_string_helpers.parse_json_llm_block import parse_json_llm_block
from .utils.constants import STRING_DELIMITERS, JSONReturnType
from .utils.json_context import ContextValues

if TYPE_CHECKING:
    from .json_parser import JSONParser


NO_DIRECT_RESULT = object()
INLINE_CONTAINER_CLOSING_DELIMITERS = {"[": "]", "{": "}", "(": ")"}
INLINE_CONTAINER_OPENERS = tuple(INLINE_CONTAINER_CLOSING_DELIMITERS)
LOW_SMART_QUOTE_SENTINEL = "\0"


@dataclass
class StringParseState:
    missing_quotes: bool = False
    doubled_quotes: bool = False
    lstring_delimiter: str = '"'
    rstring_delimiter: str = '"'
    string_acc: str = ""
    unmatched_delimiter: bool = False
    pending_inline_container: bool = False
    inline_container_stack: list[str] = field(default_factory=list)
    object_value_has_no_future_delimiter: bool = False
    lookahead_cache: dict[tuple[str, ...], tuple[int, int | None]] = field(default_factory=dict)
    object_value_unmatched_opening_braces: int = 0
    regex_character_class_start: int | None = None


def _outer_rstring_delimiter(state: StringParseState) -> str:
    return state.rstring_delimiter[0]


def _active_rstring_delimiter(state: StringParseState) -> str:
    return state.rstring_delimiter[-1]


def _in_low_smart_quote_span(state: StringParseState) -> bool:
    return _active_rstring_delimiter(state) == LOW_SMART_QUOTE_SENTINEL


def _push_low_smart_quote_span(state: StringParseState) -> None:
    state.rstring_delimiter += LOW_SMART_QUOTE_SENTINEL


def _pop_low_smart_quote_span(state: StringParseState) -> None:
    state.rstring_delimiter = state.rstring_delimiter[:-1]


def _try_parse_simple_quoted_string(self: "JSONParser") -> str | None:
    if self.get_char_at() != '"':
        return None

    start = self.index + 1
    json_str = self.json_str
    if isinstance(json_str, str):
        end = json_str.find('"', start)
        if end == -1:
            return None
        value = json_str[start:end]
        if "\\" in value or "\n" in value or "\r" in value:
            return None
    else:
        end = start
        limit = len(json_str)
        while end < limit:
            char = json_str[end]
            if char == '"':
                break
            if char in {"\\", "\n", "\r"}:
                return None
            end += 1
        if end >= limit:
            return None
        value = json_str[start:end]

    next_index = end + 1
    limit = len(json_str)
    while next_index < limit and self.json_str[next_index].isspace():
        next_index += 1
    next_char = self.json_str[next_index] if next_index < limit else None

    current_context = self.context.current
    if current_context == ContextValues.OBJECT_KEY:
        if next_char != ":":
            return None
    elif current_context == ContextValues.OBJECT_VALUE:
        if next_char not in {",", "}", None}:
            return None
    elif current_context == ContextValues.ARRAY:
        if next_char not in {",", "]", None}:
            return None
    elif next_char is not None:
        return None

    self.index = end + 1
    return value


def _append_literal_char(
    self: "JSONParser",
    state: StringParseState,
    current_char: str,
) -> str | None:
    _append_string_content(state, current_char)
    self.index += 1
    return self.get_char_at()


def _append_string_content(state: StringParseState, content: str) -> None:
    start_index = len(state.string_acc)
    state.string_acc += content
    for offset, char in enumerate(content):
        if char == "{":
            state.object_value_unmatched_opening_braces += 1
        elif char == "}" and state.object_value_unmatched_opening_braces:
            state.object_value_unmatched_opening_braces -= 1
        elif char == "[":
            state.regex_character_class_start = start_index + offset + 1
        elif char == "]":
            state.regex_character_class_start = None


def _quote_belongs_to_regex_character_class(
    self: "JSONParser",
    state: StringParseState,
) -> bool:
    """Return whether the current quote is inside a compact ``[...]`` character class."""
    start = state.regex_character_class_start
    if start is None or any(char.isspace() for char in state.string_acc[start:]):
        return False

    closing_bracket_idx = self.skip_to_character("]", idx=1)
    return self.get_char_at(closing_bracket_idx) == "]"


def _rebuild_unmatched_opening_braces(state: StringParseState) -> None:
    state.object_value_unmatched_opening_braces = 0
    state.regex_character_class_start = None
    for index, char in enumerate(state.string_acc):
        if char == "{":
            state.object_value_unmatched_opening_braces += 1
        elif char == "}" and state.object_value_unmatched_opening_braces:
            state.object_value_unmatched_opening_braces -= 1
        elif char == "[":
            state.regex_character_class_start = index + 1
        elif char == "]":
            state.regex_character_class_start = None


def _cached_skip_to_character(
    self: "JSONParser",
    state: StringParseState,
    character: str | list[str],
    idx: int = 0,
) -> int:
    targets = (character,) if isinstance(character, str) else tuple(character)
    start_index = self.index + idx
    cached = state.lookahead_cache.get(targets)
    if cached is not None:
        cached_start, cached_match = cached
        if cached_match is None and start_index >= cached_start:
            return len(self.json_str) - self.index
        if cached_match is not None and cached_start <= start_index <= cached_match:
            return cached_match - self.index

    match_offset = self.skip_to_character(character, idx)
    match = self.get_char_at(match_offset)
    if not match:
        state.lookahead_cache[targets] = (start_index, None)
        return match_offset

    match_index = self.index + match_offset
    if match_index == 0 or self.json_str[match_index - 1] != "\\":
        state.lookahead_cache[targets] = (start_index, match_index)
    return match_offset


def _prepare_string_entry(
    self: "JSONParser",
) -> tuple[StringParseState | None, object]:
    char = self.get_char_at()
    if char in ["#", "/"]:
        return None, self.parse_comment()

    while char and char not in STRING_DELIMITERS and not char.isalnum():
        self.index += 1
        char = self.get_char_at()

    if not char:
        return None, ""

    fast_path_value = _try_parse_simple_quoted_string(self)
    if fast_path_value is not None:
        return None, fast_path_value

    state = StringParseState()

    if char == "'":
        state.lstring_delimiter = state.rstring_delimiter = "'"
    elif char == "“":
        state.lstring_delimiter = "“"
        state.rstring_delimiter = "”"
    elif char.isalnum():
        if char.lower() in ["t", "f", "n"] and self.context.current != ContextValues.OBJECT_KEY:
            found_literal, value = parse_boolean_or_null(self)
            if found_literal:
                return state, value
        self.log(
            "While parsing a string, we found a literal instead of a quote",
        )
        state.missing_quotes = True

    if not state.missing_quotes:
        self.index += 1
    if self.get_char_at() == "`":
        ret_val = parse_json_llm_block(self)
        if ret_val is not False:
            return state, ret_val
        self.log(
            "While parsing a string, we found code fences but they did not enclose valid JSON, continuing parsing the string",
        )

    if self.get_char_at() == state.lstring_delimiter:
        if (
            (self.context.current == ContextValues.OBJECT_KEY and self.get_char_at(1) == ":")
            or (self.context.current == ContextValues.OBJECT_VALUE and self.get_char_at(1) in [",", "}"])
            or (self.context.current == ContextValues.ARRAY and self.get_char_at(1) in [",", "]"])
        ):
            self.index += 1
            return state, ""
        if self.get_char_at(1) == state.lstring_delimiter:
            self.log(
                "While parsing a string, we found a doubled quote and then a quote again, ignoring it",
            )
            if self.strict:
                raise ValueError("Found doubled quotes followed by another quote.")
            return state, ""
        i = self.skip_to_character(character=state.rstring_delimiter, idx=1)
        if self.get_char_at(i + 1) == state.rstring_delimiter:
            self.log(
                "While parsing a string, we found a valid starting doubled quote",
            )
            state.doubled_quotes = True
            self.index += 1
        else:
            if self.get_char_at(i) == state.rstring_delimiter:
                outer_quote_idx = self.skip_to_character(character=state.rstring_delimiter, idx=i + 1)
                after_outer_quote_idx = self.scroll_whitespaces(idx=outer_quote_idx + 1)
                after_outer_quote = self.get_char_at(after_outer_quote_idx)
                if (
                    self.context.current == ContextValues.OBJECT_VALUE
                    and not _only_whitespace_until(self, i)
                    and self.get_char_at(outer_quote_idx) == state.rstring_delimiter
                    and after_outer_quote in [",", "}", None]
                ):
                    self.log(
                        "While parsing a string, we found a leading quote that starts a quoted span, keeping it",
                    )
                    _append_string_content(state, state.lstring_delimiter)
                    state.unmatched_delimiter = True
                    self.index += 1
                    return state, NO_DIRECT_RESULT
            i = self.scroll_whitespaces(idx=1)
            next_c = self.get_char_at(i)
            if next_c in [*STRING_DELIMITERS, "{", "["]:
                self.log(
                    "While parsing a string, we found a doubled quote but also another quote afterwards, ignoring it",
                )
                if self.strict:
                    raise ValueError(
                        "Found doubled quotes followed by another quote while parsing a string.",
                    )
                self.index += 1
                return state, ""
            if next_c not in [",", "]", "}"]:
                self.log(
                    "While parsing a string, we found a doubled quote but it was a mistake, removing one quote",
                )
                self.index += 1

    return state, NO_DIRECT_RESULT


def _normalize_escape_sequence(
    self: "JSONParser",
    state: StringParseState,
    char: str,
) -> tuple[bool, str | None]:
    self.log("Found a stray escape sequence, normalizing it")
    active_rstring_delimiter = _active_rstring_delimiter(state)
    if _in_low_smart_quote_span(state) and char == '"':
        state.string_acc = state.string_acc[:-1] + char
        _rebuild_unmatched_opening_braces(state)
        _pop_low_smart_quote_span(state)
        self.index += 1
        return True, self.get_char_at()
    if char == "\\":
        run_start = self.index - 1
        run_end = self.index + 1
        while run_end < len(self.json_str) and self.json_str[run_end] == "\\":
            run_end += 1
        run_length = run_end - run_start
        next_char = self.get_char_at(run_end - self.index)
        if run_length % 2 == 0 and next_char != active_rstring_delimiter:
            state.string_acc = state.string_acc[:-1] + ("\\" * (run_length // 2))
            _rebuild_unmatched_opening_braces(state)
            self.index = run_end
            return True, self.get_char_at()
    if char in [active_rstring_delimiter, "t", "n", "r", "b", "\\"]:
        state.string_acc = state.string_acc[:-1]
        escape_seqs = {"t": "\t", "n": "\n", "r": "\r", "b": "\b"}
        state.string_acc += escape_seqs.get(char, char)
        _rebuild_unmatched_opening_braces(state)
        self.index += 1
        next_char = self.get_char_at()
        while (
            next_char
            and state.string_acc
            and state.string_acc[-1] == "\\"
            and next_char in [active_rstring_delimiter, "\\"]
        ):
            state.string_acc = state.string_acc[:-1] + next_char
            _rebuild_unmatched_opening_braces(state)
            self.index += 1
            next_char = self.get_char_at()
        return True, next_char
    if char in ["u", "x"]:
        num_chars = 4 if char == "u" else 2
        next_chars = self.json_str[self.index + 1 : self.index + 1 + num_chars]
        if len(next_chars) == num_chars and all(c in "0123456789abcdefABCDEF" for c in next_chars):
            self.log("Found a unicode escape sequence, normalizing it")
            state.string_acc = state.string_acc[:-1] + chr(int(next_chars, 16))
            _rebuild_unmatched_opening_braces(state)
            self.index += 1 + num_chars
            return True, self.get_char_at()
    elif char == "„" or char in STRING_DELIMITERS and char != active_rstring_delimiter:
        self.log("Found a delimiter that was escaped but shouldn't be escaped, removing the escape")
        state.string_acc = state.string_acc[:-1] + char
        _rebuild_unmatched_opening_braces(state)
        self.index += 1
        return True, self.get_char_at()
    return False, char


def _brace_before_code_fence_belongs_to_string(
    self: "JSONParser",
    state: StringParseState,
    fence_idx: int,
) -> bool:
    # Distinguish trailing wrapper fences from literal fenced snippets inside the current string.
    quote_search_idx = fence_idx + 3
    next_content_idx = _scroll_comment_prefixed_member_start(self, quote_search_idx)
    keep_post_fence_container = False
    if self.get_char_at(next_content_idx) in INLINE_CONTAINER_OPENERS:
        container_end_idx = _skip_inline_container(self, next_content_idx)
        if container_end_idx is not None:
            if _post_fence_container_starts_next_member(self, container_end_idx):
                return False
            keep_post_fence_container = True
            quote_search_idx = container_end_idx

    outer_rstring_delimiter = _outer_rstring_delimiter(state)
    quote_idx = self.skip_to_character(character=outer_rstring_delimiter, idx=quote_search_idx)
    while self.get_char_at(quote_idx) == outer_rstring_delimiter:
        after_quote_idx = self.scroll_whitespaces(idx=quote_idx + 1)
        after_quote = self.get_char_at(after_quote_idx)
        if after_quote in [",", "}", "]", None]:
            if keep_post_fence_container:
                state.pending_inline_container = True
            return True
        quote_idx = self.skip_to_character(character=outer_rstring_delimiter, idx=quote_idx + 1)
    return False


def _matching_string_delimiter(delimiter: str) -> str:
    return "”" if delimiter == "“" else delimiter


def _bare_key_is_followed_by_colon(
    self: "JSONParser",
    key_idx: int,
) -> bool:
    key_char = self.get_char_at(key_idx)
    if not key_char or not (key_char.isalnum() or key_char == "_"):
        return False

    while True:
        key_char = self.get_char_at(key_idx)
        if not key_char or not (key_char.isalnum() or key_char in ["_", "-"]):
            break
        key_idx += 1

    key_idx = self.scroll_whitespaces(idx=key_idx)
    return self.get_char_at(key_idx) == ":"


def _post_fence_container_starts_next_member(
    self: "JSONParser",
    container_end_idx: int,
) -> bool:
    after_container_idx = self.scroll_whitespaces(idx=container_end_idx)
    after_container = self.get_char_at(after_container_idx)
    if after_container in ["}", None]:
        return True
    if after_container != ",":
        return False

    next_member_idx = _scroll_comment_prefixed_member_start(self, after_container_idx + 1)
    return self.get_char_at(next_member_idx) in ["}", None] or _object_member_starts_at(self, next_member_idx)


def _starts_nested_inline_container(
    self: "JSONParser",
    idx: int,
) -> bool:
    opening_delimiter = self.get_char_at(idx)
    prev_idx = idx - 1
    while prev_idx >= 0:
        prev_char = self.get_char_at(prev_idx)
        if prev_char is None:
            return True
        if not prev_char.isspace():
            if prev_char in INLINE_CONTAINER_OPENERS:
                return True
            if prev_char not in [",", ":"]:
                return False

            next_idx = self.scroll_whitespaces(idx=idx + 1)
            next_char = self.get_char_at(next_idx)
            if opening_delimiter in ["[", "("]:
                return next_char in ["]", ")", *STRING_DELIMITERS, "-", *INLINE_CONTAINER_OPENERS, "t", "f", "n"] or (
                    next_char is not None and next_char.isdigit()
                )
            if opening_delimiter != "{":
                return False
            if next_char in ["}", *STRING_DELIMITERS]:
                return True
            return prev_char == ":" and _bare_key_is_followed_by_colon(self, next_idx)
        prev_idx -= 1
    return True


def _skip_inline_container(
    self: "JSONParser",
    idx: int,
) -> int | None:
    opening_delimiter = self.get_char_at(idx)
    if opening_delimiter not in INLINE_CONTAINER_CLOSING_DELIMITERS:
        return idx

    stack = [INLINE_CONTAINER_CLOSING_DELIMITERS[opening_delimiter]]
    i = idx + 1
    while stack:
        char = self.get_char_at(i)
        if not char:
            return None
        if char in STRING_DELIMITERS:
            end_delimiter = _matching_string_delimiter(char)
            i = self.skip_to_character(character=end_delimiter, idx=i + 1)
            if self.get_char_at(i) != end_delimiter:
                return None
        elif char in INLINE_CONTAINER_CLOSING_DELIMITERS and _starts_nested_inline_container(self, i):
            stack.append(INLINE_CONTAINER_CLOSING_DELIMITERS[char])
        elif char == stack[-1]:
            stack.pop()
            if not stack:
                return i + 1
        i += 1

    return None  # pragma: no cover


def _scroll_comment_prefixed_member_start(
    self: "JSONParser",
    idx: int,
) -> int:
    idx = self.scroll_whitespaces(idx=idx)
    while True:
        char = self.get_char_at(idx)
        if char == "#":
            while char and char not in ["\n", "\r"]:
                idx += 1
                char = self.get_char_at(idx)
            idx = self.scroll_whitespaces(idx=idx)
            continue
        if char == "/":
            next_char = self.get_char_at(idx + 1)
            if next_char == "/":
                idx += 2
                char = self.get_char_at(idx)
                while char and char not in ["\n", "\r"]:
                    idx += 1
                    char = self.get_char_at(idx)
                idx = self.scroll_whitespaces(idx=idx)
                continue
            if next_char == "*":
                idx += 2
                while True:
                    char = self.get_char_at(idx)
                    if not char:
                        return idx
                    if char == "*" and self.get_char_at(idx + 1) == "/":
                        idx += 2
                        break
                    idx += 1
                idx = self.scroll_whitespaces(idx=idx)
                continue
        return idx


def _quoted_object_member_follows(
    self: "JSONParser",
    quote_idx: int,
) -> bool:
    comma_idx = self.scroll_whitespaces(idx=quote_idx + 1)
    if self.get_char_at(comma_idx) != ",":
        return False

    next_member_idx = _scroll_comment_prefixed_member_start(self, comma_idx + 1)
    return _object_member_starts_at(self, next_member_idx)


def _object_member_starts_at(
    self: "JSONParser",
    next_member_idx: int,
) -> bool:
    if self.get_char_at(next_member_idx) in ["}", None]:
        return False

    next_member = self.get_char_at(next_member_idx)
    if next_member in STRING_DELIMITERS:
        key_end_delimiter = _matching_string_delimiter(next_member)
        key_end_idx = self.skip_to_character(character=key_end_delimiter, idx=next_member_idx + 1)
        if self.get_char_at(key_end_idx) != key_end_delimiter:
            return False
        after_key_idx = self.scroll_whitespaces(idx=key_end_idx + 1)
        return self.get_char_at(after_key_idx) == ":"

    if next_member and (next_member.isalnum() or next_member == "_"):
        return _bare_key_is_followed_by_colon(self, next_member_idx)

    return False


def _handle_right_delimiter_candidate(
    self: "JSONParser",
    state: StringParseState,
    char: str,
) -> tuple[bool, str | None, bool]:
    outer_rstring_delimiter = _outer_rstring_delimiter(state)

    if state.doubled_quotes and self.get_char_at(1) == outer_rstring_delimiter:
        self.log("While parsing a string, we found a doubled quote, ignoring it")
        self.index += 1
        return True, char, False

    if state.missing_quotes and self.context.current == ContextValues.OBJECT_VALUE:
        i = 1
        next_c = self.get_char_at(i)
        while next_c and next_c not in [
            outer_rstring_delimiter,
            state.lstring_delimiter,
        ]:
            i += 1
            next_c = self.get_char_at(i)
        if next_c:
            i += 1
            i = self.scroll_whitespaces(idx=i)
            if self.get_char_at(i) == ":":
                self.index -= 1
                next_char = self.get_char_at()
                self.log(
                    "In a string with missing quotes and object value context, I found a delimeter but it turns out it was the beginning on the next key. Stopping here.",
                )
                return False, next_char, True
        return False, char, False

    if state.unmatched_delimiter:
        state.unmatched_delimiter = False
        next_char = _append_literal_char(self, state, char)
        return True, next_char, False

    i = 1
    next_c = self.get_char_at(i)
    check_comma_in_object_value = True
    while next_c and next_c not in [
        outer_rstring_delimiter,
        state.lstring_delimiter,
    ]:
        if check_comma_in_object_value and next_c.isalpha():
            check_comma_in_object_value = False
        if (
            (ContextValues.OBJECT_KEY in self.context.context and next_c in [":", "}"])
            or (ContextValues.OBJECT_VALUE in self.context.context and next_c == "}")
            or (ContextValues.ARRAY in self.context.context and next_c in ["]", ","])
            or (check_comma_in_object_value and self.context.current == ContextValues.OBJECT_VALUE and next_c == ",")
        ):
            break
        i += 1
        next_c = self.get_char_at(i)
    if next_c == "," and self.context.current == ContextValues.OBJECT_VALUE:
        i += 1
        i = self.skip_to_character(character=outer_rstring_delimiter, idx=i)
        next_c = self.get_char_at(i)
        i += 1
        i = self.scroll_whitespaces(idx=i)
        next_c = self.get_char_at(i)
        if next_c in ["}", ","]:
            self.log(
                "While parsing a string, we found a misplaced quote that would have closed the string but has a different meaning here, ignoring it",
            )
            next_char = _append_literal_char(self, state, char)
            return True, next_char, False
    elif next_c == outer_rstring_delimiter and self.get_char_at(i - 1) != "\\":
        if _only_whitespace_until(self, i) and not (
            self.context.current == ContextValues.OBJECT_VALUE and _quoted_object_member_follows(self, i)
        ):
            return False, char, True
        if self.context.current == ContextValues.OBJECT_VALUE:
            if _quoted_object_member_follows(self, i):
                self.log(
                    "While parsing a string, we found a misplaced quote that would have closed the string but has a different meaning here, ignoring it",
                )
                next_char = _append_literal_char(self, state, char)
                return True, next_char, False
            i = self.skip_to_character(character=outer_rstring_delimiter, idx=i + 1)
            i += 1
            next_c = self.get_char_at(i)
            while next_c and next_c != ":":
                if next_c in [",", "]", "}"] or (next_c == outer_rstring_delimiter and self.get_char_at(i - 1) != "\\"):
                    break
                i += 1
                next_c = self.get_char_at(i)
            if next_c != ":":
                self.log(
                    "While parsing a string, we found a misplaced quote that would have closed the string but has a different meaning here, ignoring it",
                )
                state.unmatched_delimiter = not state.unmatched_delimiter
                next_char = _append_literal_char(self, state, char)
                return True, next_char, False
        elif self.context.current == ContextValues.ARRAY:
            even_delimiters = next_c == outer_rstring_delimiter
            while next_c == outer_rstring_delimiter:
                i = self.skip_to_character(character=[outer_rstring_delimiter, "]"], idx=i + 1)
                next_c = self.get_char_at(i)
                if next_c != outer_rstring_delimiter:
                    even_delimiters = False
                    break
                i = self.skip_to_character(character=[outer_rstring_delimiter, "]"], idx=i + 1)
                next_c = self.get_char_at(i)
            if even_delimiters:
                self.log(
                    "While parsing a string in Array context, we detected a quoted section that would have closed the string but has a different meaning here, ignoring it",
                )
                state.unmatched_delimiter = not state.unmatched_delimiter
                next_char = _append_literal_char(self, state, char)
                return True, next_char, False
            return False, char, True
        elif self.context.current == ContextValues.OBJECT_KEY:
            self.log(
                "While parsing a string in Object Key context, we detected a quoted section that would have closed the string but has a different meaning here, ignoring it",
            )
            next_char = _append_literal_char(self, state, char)
            return True, next_char, False

    return False, char, False


def _scan_string_body(
    self: "JSONParser",
    state: StringParseState,
) -> str | None:
    outer_rstring_delimiter = _outer_rstring_delimiter(state)

    def cached_skip_to_character(character: str | list[str], idx: int = 0) -> int:
        return _cached_skip_to_character(self, state, character, idx)

    char = self.get_char_at()
    while char and (char != outer_rstring_delimiter or _in_low_smart_quote_span(state)):
        if state.missing_quotes:
            if self.context.current == ContextValues.OBJECT_KEY and (char == ":" or char.isspace()):
                self.log(
                    "While parsing a string missing the left delimiter in object key context, we found a :, stopping here",
                )
                break
            if self.context.current == ContextValues.ARRAY and char in ["]", ","]:
                self.log(
                    "While parsing a string missing the left delimiter in array context, we found a ] or ,, stopping here",
                )
                break
        if char == "„" and (not state.string_acc or state.string_acc[-1] != "\\"):
            _push_low_smart_quote_span(state)
            char = _append_literal_char(self, state, char)
            continue
        if _in_low_smart_quote_span(state) and char == "”":
            _pop_low_smart_quote_span(state)
            char = _append_literal_char(self, state, char)
            continue
        if (
            (
                state.pending_inline_container
                or (
                    self.context.current == ContextValues.OBJECT_VALUE
                    and char == "{"
                    and self.get_char_at(-1) != "\\"
                    and _bare_key_is_followed_by_colon(self, self.scroll_whitespaces(idx=1))
                )
            )
            and char in INLINE_CONTAINER_OPENERS
            and (not state.string_acc or state.string_acc[-1] != "\\")
        ):
            container_end_idx = _skip_inline_container(self, 0)
            if container_end_idx is not None:
                self.log(
                    "While parsing a string in object value context, we found a balanced inline container that belongs to the string, keeping it",
                )
                state.pending_inline_container = False
                state.inline_container_stack.clear()
                _append_string_content(state, self.json_str[self.index : self.index + container_end_idx])
                self.index += container_end_idx
                char = self.get_char_at()
                continue
        if (
            not self.stream_stable
            and self.context.current == ContextValues.OBJECT_VALUE
            and char == ","
            and not state.pending_inline_container
            and not state.inline_container_stack
        ):
            comma_classification = (
                "string"
                if state.object_value_has_no_future_delimiter
                else classify_object_value_comma(
                    self,
                    cached_skip_to_character,
                )
            )
            if comma_classification == "member":
                self.log(
                    "While parsing a string missing the right delimiter in object value context, we found a comma that starts the next object member. Stopping here",
                )
                break
            if comma_classification == "string_no_future_delimiter":
                state.object_value_has_no_future_delimiter = True
            state.pending_inline_container = comma_classification == "container"
            self.log(
                "While parsing a string in object value context, we found a comma that belongs to the string, keeping it",
            )
            char = _append_literal_char(self, state, char)
            continue
        state.pending_inline_container, keep_inline_container_char = update_inline_container_stack(
            char,
            state.pending_inline_container,
            state.inline_container_stack,
        )
        if keep_inline_container_char:
            char = _append_literal_char(self, state, char)
            continue
        if (
            not self.stream_stable
            and self.context.current == ContextValues.OBJECT_VALUE
            and char == "}"
            and (not state.string_acc or state.string_acc[-1] != outer_rstring_delimiter)
        ):
            if state.object_value_unmatched_opening_braces:
                char = _append_literal_char(self, state, char)
                continue
            rstring_delimiter_missing = True
            self.skip_whitespaces()
            if self.get_char_at(1) == "\\":
                rstring_delimiter_missing = False
            i = _cached_skip_to_character(self, state, outer_rstring_delimiter, idx=1)
            next_c = self.get_char_at(i)
            if next_c:
                i += 1
                i = self.scroll_whitespaces(idx=i)
                next_c = self.get_char_at(i)
                if not next_c or next_c in [",", "}"]:
                    rstring_delimiter_missing = False
                else:
                    i = self.skip_to_character(character=state.lstring_delimiter, idx=i)
                    next_c = self.get_char_at(i)
                    if not next_c:
                        rstring_delimiter_missing = False
                    else:
                        i = self.scroll_whitespaces(idx=i + 1)
                        next_c = self.get_char_at(i)
                        if next_c and next_c != ":":
                            rstring_delimiter_missing = False
            else:
                i = self.skip_to_character(character=":", idx=1)
                next_c = self.get_char_at(i)
                if next_c:
                    break
                i = self.scroll_whitespaces(idx=1)
                j = self.skip_to_character(character="}", idx=i)
                if j - i > 1:
                    rstring_delimiter_missing = False
            if rstring_delimiter_missing:
                self.log(
                    "While parsing a string missing the left delimiter in object value context, we found a , or } and we couldn't determine that a right delimiter was present. Stopping here",
                )
                break
        if (
            not self.stream_stable
            and char == "]"
            and ContextValues.ARRAY in self.context.context
            and (not state.string_acc or state.string_acc[-1] != outer_rstring_delimiter)
        ):
            i = self.skip_to_character(outer_rstring_delimiter)
            if not self.get_char_at(i):
                break
        if self.context.current == ContextValues.OBJECT_VALUE and char == "}":
            i = self.scroll_whitespaces(idx=1)
            next_c = self.get_char_at(i)
            if next_c == "`" and self.get_char_at(i + 1) == "`" and self.get_char_at(i + 2) == "`":
                if _brace_before_code_fence_belongs_to_string(self, state, i):
                    self.log(
                        "While parsing a string in object value context, we found a literal fenced snippet after }, keeping it in the string",
                    )
                    char = _append_literal_char(self, state, char)
                    continue
                self.log(
                    "While parsing a string in object value context, we found a } that closes the object before code fences, stopping here",
                )
                break
            if not next_c:
                self.log(
                    "While parsing a string in object value context, we found a } that closes the object, stopping here",
                )
                break
        assert char is not None
        _append_string_content(state, char)
        self.index += 1
        char = self.get_char_at()
        if char is None:
            if self.stream_stable and state.string_acc and state.string_acc[-1] == "\\":
                state.string_acc = state.string_acc[:-1]
                _rebuild_unmatched_opening_braces(state)
            break
        if state.string_acc and state.string_acc[-1] == "\\":
            handled_escape, char = _normalize_escape_sequence(self, state, char)
            if handled_escape:
                continue
        if char == ":" and not state.missing_quotes and self.context.current == ContextValues.OBJECT_KEY:
            i = self.skip_to_character(character=state.lstring_delimiter, idx=1)
            next_c = self.get_char_at(i)
            if next_c:
                i += 1
                i = self.skip_to_character(character=outer_rstring_delimiter, idx=i)
                next_c = self.get_char_at(i)
                if next_c:
                    i += 1
                    i = self.scroll_whitespaces(idx=i)
                    ch = self.get_char_at(i)
                    if ch in [",", "}"]:
                        self.log(
                            f"While parsing a string missing the right delimiter in object key context, we found a {ch} stopping here",
                        )
                        break
            else:
                self.log(
                    "While parsing a string missing the right delimiter in object key context, we found a :, stopping here",
                )
                break
        if _in_low_smart_quote_span(state) and char == '"':
            _pop_low_smart_quote_span(state)
            char = _append_literal_char(self, state, char)
            continue
        if (
            char == outer_rstring_delimiter
            and self.context.current == ContextValues.OBJECT_VALUE
            and _quote_belongs_to_regex_character_class(self, state)
        ):
            self.log(
                "While parsing a string, we found a bare quote inside a regex character class, keeping it",
            )
            assert char is not None
            char = _append_literal_char(self, state, char)
            continue
        if char == outer_rstring_delimiter and state.string_acc and state.string_acc[-1] != "\\":
            assert char is not None
            handled_delimiter, char, should_break = _handle_right_delimiter_candidate(self, state, char)
            if should_break:
                break
            if handled_delimiter:
                continue
    return char


def _finalize_string_result(
    self: "JSONParser",
    state: StringParseState,
    char: str | None,
) -> str:
    outer_rstring_delimiter = _outer_rstring_delimiter(state)
    if char and state.missing_quotes and self.context.current == ContextValues.OBJECT_KEY and char.isspace():
        self.log(
            "While parsing a string, handling an extreme corner case in which the LLM added a comment instead of valid string, invalidate the string and return an empty value",
        )
        self.skip_whitespaces()
        if self.get_char_at() not in [":", ","]:
            return ""

    if char != outer_rstring_delimiter:
        if not self.stream_stable:
            self.log(
                "While parsing a string, we missed the closing quote, ignoring",
            )
            state.string_acc = state.string_acc.rstrip()
    else:
        self.index += 1

    if not self.stream_stable and (state.missing_quotes or (state.string_acc and state.string_acc[-1] == "\n")):
        state.string_acc = state.string_acc.rstrip()

    return state.string_acc


def parse_string(self: "JSONParser") -> JSONReturnType:
    state, direct_result = _prepare_string_entry(self)
    if direct_result is not NO_DIRECT_RESULT:
        return cast("JSONReturnType", direct_result)
    assert state is not None

    char = _scan_string_body(self, state)
    return _finalize_string_result(self, state, char)


def _only_whitespace_until(self: "JSONParser", end: int) -> bool:
    for j in range(1, end):
        c = self.get_char_at(j)
        if c is not None and not c.isspace():
            return False
    return True

```

### `src/json_repair/parser_parenthesized.py`

```py
from typing import TYPE_CHECKING

from .utils.constants import STRING_DELIMITERS

if TYPE_CHECKING:
    from .json_parser import JSONParser


def parenthesized_is_explicit_tuple(parser: "JSONParser") -> bool:
    """
    Return True when the current '(' starts an explicit Python tuple literal.

    Empty parentheses count as a tuple. A single grouped value like ``(1)`` does not.
    """
    i = parser.index + 1
    n = len(parser.json_str)
    nested_parentheses = 0
    square_brackets = 0
    braces = 0
    in_quote: str | None = None
    backslashes = 0
    saw_top_level_content = False

    while i < n:
        ch = parser.json_str[i]

        if ch == "\\":
            backslashes += 1
            i += 1
            continue

        if in_quote is not None:
            if ch == in_quote and backslashes % 2 == 0:
                in_quote = None
            backslashes = 0
            i += 1
            continue

        if ch in STRING_DELIMITERS and backslashes % 2 == 0:
            in_quote = ch
            saw_top_level_content = saw_top_level_content or (
                nested_parentheses == 0 and square_brackets == 0 and braces == 0
            )
            backslashes = 0
            i += 1
            continue

        backslashes = 0

        if (
            not ch.isspace()
            and ch not in [",", ")"]
            and nested_parentheses == 0
            and square_brackets == 0
            and braces == 0
        ):
            saw_top_level_content = True

        if ch == "(":
            nested_parentheses += 1
        elif ch == ")":
            if nested_parentheses == 0 and square_brackets == 0 and braces == 0:
                return not saw_top_level_content
            if nested_parentheses > 0:
                nested_parentheses -= 1
        elif ch == "[":
            square_brackets += 1
        elif ch == "]" and square_brackets > 0:
            square_brackets -= 1
        elif ch == "{":
            braces += 1
        elif ch == "}" and braces > 0:
            braces -= 1
        elif ch == "," and nested_parentheses == 0 and square_brackets == 0 and braces == 0:
            return True

        i += 1

    return not saw_top_level_content


def top_level_parenthesized_can_start_value(parser: "JSONParser") -> bool:
    """
    Return True when a top-level '(' looks like a standalone value rather than inline prose.

    This keeps tuple support available for direct inputs and fenced blocks while avoiding
    regressions on surrounding explanatory text like ``foo (clarification): {...}``.
    """
    i = parser.index - 1
    while i >= 0:
        ch = parser.json_str[i]
        if ch in "\n\r":
            break
        if not ch.isspace():
            return False
        i -= 1

    idx = parser.scroll_whitespaces(idx=1)
    first_inner_char = parser.get_char_at(idx)
    if first_inner_char is None:
        return False

    inner_text = parser.json_str[parser.index + idx :].lower()
    if (
        first_inner_char not in [")", "{", "[", "(", *STRING_DELIMITERS]
        and not first_inner_char.isdigit()
        and first_inner_char not in ["-", "."]
        and inner_text[:4] not in ["true", "null", "none"]
        and inner_text[:5] != "false"
    ):
        return False

    i = parser.index + 1
    n = len(parser.json_str)
    nested_parentheses = 0
    square_brackets = 0
    braces = 0
    in_quote: str | None = None
    backslashes = 0

    while i < n:
        ch = parser.json_str[i]

        if ch == "\\":
            backslashes += 1
            i += 1
            continue

        if in_quote is not None:
            if ch == in_quote and backslashes % 2 == 0:
                in_quote = None
            backslashes = 0
            i += 1
            continue

        if ch in STRING_DELIMITERS and backslashes % 2 == 0:
            in_quote = ch
            backslashes = 0
            i += 1
            continue

        backslashes = 0

        if ch == "(":
            nested_parentheses += 1
        elif ch == ")":
            if nested_parentheses == 0 and square_brackets == 0 and braces == 0:
                i += 1
                while i < n:
                    trailer = parser.json_str[i]
                    if trailer in "\n\r":
                        return True
                    if not trailer.isspace():
                        return False
                    i += 1
                return True
            nested_parentheses -= 1
        elif ch == "[":
            square_brackets += 1
        elif ch == "]" and square_brackets > 0:
            square_brackets -= 1
        elif ch == "{":
            braces += 1
        elif ch == "}" and braces > 0:
            braces -= 1

        i += 1

    return True

```

### `src/json_repair/parser_schema.py`

```py
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .schema_repair import SchemaRepairer


@dataclass(frozen=True)
class ObjectSchemaConfig:
    properties: dict[str, Any]
    pattern_properties: dict[str, Any]
    additional_properties: object | None
    required: set[str]


@dataclass(frozen=True)
class ArraySchemaConfig:
    items_schema: object | None
    additional_items: object | None


def resolve_parser_object_schema(
    repairer: SchemaRepairer | None,
    schema: dict[str, Any] | bool | None,
) -> tuple[SchemaRepairer | None, dict[str, Any] | bool | None, ObjectSchemaConfig | None]:
    if repairer is None or schema in (None, True):
        return None, schema, None

    schema = repairer.resolve_schema(schema)
    if schema is False:
        raise ValueError("Schema does not allow any values.")
    if schema is True or not repairer.is_object_schema(schema):
        return None, schema, None
    return repairer, schema, object_schema_config(schema)


def resolve_parser_array_schema(
    repairer: SchemaRepairer | None,
    schema: dict[str, Any] | bool | None,
) -> tuple[SchemaRepairer | None, dict[str, Any] | bool | None, ArraySchemaConfig | None]:
    if repairer is None or schema in (None, True):
        return None, schema, None

    schema = repairer.resolve_schema(schema)
    if schema is False:
        raise ValueError("Schema does not allow any values.")
    if schema is True or not repairer.is_array_schema(schema):
        return None, schema, None
    return repairer, schema, array_schema_config(schema)


def object_schema_config(schema: dict[str, Any]) -> ObjectSchemaConfig:
    properties = schema.get("properties", {})
    if not isinstance(properties, dict):
        properties = {}
    pattern_properties = schema.get("patternProperties", {})
    if not isinstance(pattern_properties, dict):
        pattern_properties = {}
    return ObjectSchemaConfig(
        properties=properties,
        pattern_properties=pattern_properties,
        additional_properties=schema.get("additionalProperties"),
        required=set(schema.get("required", [])),
    )


def array_schema_config(schema: dict[str, Any]) -> ArraySchemaConfig:
    return ArraySchemaConfig(
        items_schema=schema.get("items"),
        additional_items=schema.get("additionalItems"),
    )

```

### `src/json_repair/py.typed`

```typed

```

### `src/json_repair/schema_repair.py`

```py
from __future__ import annotations

import copy
import importlib
import json
from typing import Any, Literal, cast

from .parser_schema import array_schema_config, object_schema_config
from .utils.constants import MISSING_VALUE, JSONReturnType, MissingValueType
from .utils.pattern_properties import match_pattern_properties

SchemaRepairMode = Literal["standard", "salvage"]
SUPPORTED_SCHEMA_REPAIR_MODES: tuple[SchemaRepairMode, ...] = ("standard", "salvage")


class SchemaDefinitionError(ValueError):
    """Raised when schema metadata is invalid or unsupported."""


def normalize_schema_repair_mode(mode: str | None) -> SchemaRepairMode:
    if mode is None:
        return "standard"
    if mode == "standard":
        return "standard"
    if mode == "salvage":
        return "salvage"
    expected = ", ".join(SUPPORTED_SCHEMA_REPAIR_MODES)
    raise ValueError(f"schema_repair_mode must be one of: {expected}.")


def _require_jsonschema() -> Any:
    try:
        return importlib.import_module("jsonschema")
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise ValueError("jsonschema is required when using schema-aware repair.") from exc


def _require_pydantic() -> Any:
    try:
        return importlib.import_module("pydantic")
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise ValueError("pydantic is required when using schema models.") from exc


def _prepare_schema_for_validation_node(node: Any) -> Any:
    if isinstance(node, dict):
        normalized = {key: _prepare_schema_for_validation_node(value) for key, value in node.items()}
        items = normalized.get("items")
        if isinstance(items, list):
            normalized.pop("items", None)
            normalized["prefixItems"] = items
            additional_items = normalized.pop("additionalItems", None)
            if additional_items is False:
                normalized["items"] = False
            elif isinstance(additional_items, dict):
                normalized["items"] = additional_items
        return normalized
    if isinstance(node, list):
        return [_prepare_schema_for_validation_node(item) for item in node]
    return node


def load_schema_model(path: str) -> type[Any]:
    if ":" not in path:
        raise ValueError("Schema model must be in the form 'module:ClassName'.")
    module_name, class_name = path.split(":", 1)
    module = importlib.import_module(module_name)
    model: object | None = module.__dict__.get(class_name)
    if model is None or not isinstance(model, type):
        raise ValueError(f"Schema model '{class_name}' not found in module '{module_name}'.")
    return model


def normalize_missing_values(value: object) -> JSONReturnType:
    if value is MISSING_VALUE or isinstance(value, MissingValueType):
        return ""
    if isinstance(value, dict):
        normalized: dict[str, JSONReturnType] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError("Object keys must be strings.")
            normalized[key] = normalize_missing_values(item)
        return normalized
    if isinstance(value, list):
        return [normalize_missing_values(item) for item in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise ValueError("Value is not JSON compatible.")


def schema_from_input(schema: Any) -> dict[str, Any] | bool:
    if isinstance(schema, dict):
        return schema
    if schema is True or schema is False:
        return schema
    if hasattr(schema, "model_json_schema"):
        pydantic = _require_pydantic()
        version = getattr(pydantic, "VERSION", getattr(pydantic, "__version__", "0"))
        if int(version.split(".")[0]) < 2:
            raise ValueError("pydantic v2 is required for schema models.")
        schema_dict: dict[str, Any] = schema.model_json_schema()
        if hasattr(schema, "model_fields"):
            properties = schema_dict.setdefault("properties", {})
            if not isinstance(properties, dict):
                properties = {}
                schema_dict["properties"] = properties
            for name, field in schema.model_fields.items():
                if field.is_required():
                    continue
                property_schema = properties.setdefault(name, {})
                if not isinstance(property_schema, dict):
                    property_schema = {}
                    properties[name] = property_schema
                if "default" in property_schema:
                    continue
                if field.default_factory is not None:
                    property_schema["default"] = field.default_factory()
                else:
                    property_schema["default"] = field.default
        return schema_dict
    raise ValueError("Schema must be a JSON Schema dict, boolean schema, or pydantic v2 model.")


class SchemaRepairer:
    def __init__(
        self,
        schema: dict[str, Any] | bool,
        log: list[dict[str, str]] | None,
        schema_repair_mode: str = "standard",
    ) -> None:
        self.root_schema = schema
        self.log = log
        self.schema_repair_mode = normalize_schema_repair_mode(schema_repair_mode)
        self._validator_cache: dict[int, tuple[dict[str, Any], Any]] = {}
        self._root_validator: Any | None = None

    def _log(self, text: str, path: str) -> None:
        if self.log is not None:
            self.log.append({"text": text, "context": path})

    def _get_validator(self, schema: dict[str, Any]) -> Any:
        cache_key = id(schema)
        cached_validator = self._validator_cache.get(cache_key)
        if cached_validator is not None and cached_validator[0] is schema:
            return cached_validator[1]

        prepared_schema = self._prepare_schema_for_validation(schema)
        root_validator = self._get_root_validator()
        validator = root_validator if schema is self.root_schema else root_validator.evolve(schema=prepared_schema)
        self._validator_cache[cache_key] = (schema, validator)
        return validator

    def _get_root_validator(self) -> Any:
        if self._root_validator is not None:
            return self._root_validator

        prepared_root_schema = self._prepare_schema_for_validation(self.root_schema)
        jsonschema = _require_jsonschema()
        validator_cls = jsonschema.validators.validator_for(prepared_root_schema)
        self._root_validator = validator_cls(prepared_root_schema)
        return self._root_validator

    def is_valid(self, value: JSONReturnType, schema: dict[str, Any] | bool) -> bool:
        schema = self.resolve_schema(schema)
        if schema is True:
            return True
        if schema is False:
            return False
        validator = self._get_validator(schema)
        return bool(validator.is_valid(value))

    def validate(self, value: JSONReturnType, schema: dict[str, Any] | bool) -> None:
        schema = self.resolve_schema(schema)
        if schema is True:
            return
        if schema is False:
            raise ValueError("Schema does not allow any values.")
        jsonschema = _require_jsonschema()
        validator = self._get_validator(schema)
        try:
            validator.validate(value)
        except jsonschema.exceptions.ValidationError as exc:
            raise ValueError(exc.message) from exc

    def resolve_schema(self, schema: object | None) -> dict[str, Any] | bool:
        if schema is None:
            return True
        if isinstance(schema, bool):
            return schema
        if not isinstance(schema, dict):
            raise SchemaDefinitionError("Schema must be an object.")
        for key in schema:
            if not isinstance(key, str):
                raise SchemaDefinitionError("Schema keys must be strings.")
        schema_dict = cast("dict[str, Any]", schema)
        seen_schema_ids: set[int] = set()
        while "$ref" in schema_dict:
            ref = schema_dict["$ref"]
            if not isinstance(ref, str):
                raise SchemaDefinitionError("$ref must be a string.")
            schema_id = id(schema_dict)
            if schema_id in seen_schema_ids:
                raise SchemaDefinitionError(f"Circular $ref detected: {ref}")
            seen_schema_ids.add(schema_id)
            resolved = self._resolve_ref(ref)
            if isinstance(resolved, bool):
                return resolved
            schema_dict = resolved
        return schema_dict

    def is_object_schema(self, schema: dict[str, Any] | bool | None) -> bool:
        schema = self.resolve_schema(schema)
        if not isinstance(schema, dict):
            return False
        schema_type = schema.get("type")
        if schema_type == "object":
            return True
        if isinstance(schema_type, list) and "object" in schema_type:
            return True
        return any(key in schema for key in ("properties", "patternProperties", "additionalProperties", "required"))

    def is_array_schema(self, schema: dict[str, Any] | bool | None) -> bool:
        schema = self.resolve_schema(schema)
        if not isinstance(schema, dict):
            return False
        schema_type = schema.get("type")
        if schema_type == "array":
            return True
        if isinstance(schema_type, list) and "array" in schema_type:
            return True
        return "items" in schema

    def _allows_schema_type(self, schema: dict[str, Any], schema_type: str) -> bool:
        declared_type = schema.get("type")
        if isinstance(declared_type, str):
            return declared_type == schema_type
        if isinstance(declared_type, list):
            return schema_type in declared_type
        if schema_type == "object":
            return self.is_object_schema(schema)
        # This helper is only used for object/array checks in _can_salvage_list_as_object.
        return self.is_array_schema(schema)

    def _can_salvage_list_as_object(self, schema: dict[str, Any]) -> bool:
        return self._allows_schema_type(schema, "object") and not self._allows_schema_type(schema, "array")

    def repair_value(self, value: Any, schema: dict[str, Any] | bool | None, path: str) -> JSONReturnType:
        """Apply schema rules to a parsed value, including unions, coercions, and defaults."""
        schema = self.resolve_schema(schema)
        if schema is True:
            return normalize_missing_values(value)
        if schema is False:
            raise ValueError("Schema does not allow any values.")
        if not schema:
            return normalize_missing_values(value)

        if value is MISSING_VALUE:
            return self._fill_missing(schema, path)

        if "allOf" in schema:
            subschemas = schema["allOf"]
            if not subschemas:
                return normalize_missing_values(value)
            repaired = self.repair_value(value, subschemas[0], path)
            for subschema in subschemas[1:]:
                repaired = self.repair_value(repaired, subschema, path)
            return repaired

        if "oneOf" in schema:
            return self._repair_union(value, schema["oneOf"], path)
        if "anyOf" in schema:
            return self._repair_union(value, schema["anyOf"], path)

        expected_type = schema.get("type")
        if expected_type is None:
            if self.is_object_schema(schema):
                expected_type = "object"
            elif self.is_array_schema(schema):
                expected_type = "array"

        if isinstance(expected_type, list):
            return self._repair_type_union(value, expected_type, schema, path)

        if expected_type == "object":
            repaired = self._repair_object(value, schema, path)
        elif expected_type == "array":
            repaired = self._repair_array(value, schema, path)
        elif isinstance(expected_type, str):
            repaired = self._coerce_scalar(value, expected_type, path)
        else:
            repaired = normalize_missing_values(value)

        return self._apply_enum_const(repaired, schema, path)

    def _repair_union(self, value: Any, schemas: list[dict[str, Any] | bool], path: str) -> JSONReturnType:
        last_error: Exception | None = None
        for subschema in schemas:
            try:
                candidate = self.repair_value(copy.deepcopy(value), subschema, path)
                self.validate(candidate, subschema)
            except ValueError as exc:
                last_error = exc
            else:
                return candidate
        if last_error:
            raise ValueError(str(last_error)) from last_error
        raise ValueError("No schema matched the value.")

    def _repair_type_union(
        self,
        value: Any,
        types: list[str],
        schema: dict[str, Any],
        path: str,
    ) -> JSONReturnType:
        last_error: Exception | None = None
        for schema_type in types:
            branch_schema = {**schema, "type": schema_type}
            try:
                # Keep structural schema context for repair heuristics, but validate against the narrowed branch type.
                candidate = self._repair_by_type(copy.deepcopy(value), schema_type, schema, path)
                candidate = self._apply_enum_const(candidate, branch_schema, path)
                self.validate(candidate, branch_schema)
            except ValueError as exc:
                last_error = exc
            else:
                return candidate
        if last_error:
            raise ValueError(str(last_error)) from last_error
        raise ValueError("No schema type matched the value.")

    def _repair_by_type(self, value: Any, schema_type: str, schema: dict[str, Any], path: str) -> JSONReturnType:
        if schema_type == "array":
            return self._repair_array(value, schema, path)
        if schema_type == "object":
            return self._repair_object(value, schema, path)
        return self._coerce_scalar(value, schema_type, path)

    def _load_json_string_container(
        self,
        value: Any,
        expected_type: type[object],
        path: str,
        unwrap_log_message: str,
        salvage_log_message: str,
    ) -> Any:
        if not isinstance(value, str):
            return value
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            if self.schema_repair_mode != "salvage":
                return value
            json_repair_module = importlib.import_module(f"{__package__}.json_repair")
            repaired = json_repair_module.loads(value, skip_json_loads=True)
            if isinstance(repaired, expected_type):
                self._log(salvage_log_message, path)
                return repaired
            return value
        if isinstance(parsed, expected_type):
            self._log(unwrap_log_message, path)
            return parsed
        return value

    def _repair_array(self, value: Any, schema: dict[str, Any], path: str) -> JSONReturnType:
        value = self._load_json_string_container(
            value,
            list,
            path,
            "Unwrapped JSON string to array to match schema",
            "Repaired malformed JSON string to array to match schema",
        )
        if isinstance(value, list):
            items: list[JSONReturnType] = value
        else:
            self._log("Wrapped value in array to match schema", path)
            items = [normalize_missing_values(value)]
        salvage_mode = self.schema_repair_mode == "salvage"
        schema_config = array_schema_config(schema)

        def repair_or_drop(raw_item: Any, item_schema: Any, item_path: str) -> tuple[bool, JSONReturnType]:
            try:
                return True, self.repair_value(raw_item, item_schema, item_path)
            except SchemaDefinitionError:
                raise
            except ValueError:
                if not salvage_mode:
                    raise
                self._log("Dropped invalid array item while salvaging", item_path)
                return False, None

        if schema_config.items_schema is not None:
            if isinstance(schema_config.items_schema, list):
                repaired_items: list[JSONReturnType] = []
                for idx, item_schema in enumerate(schema_config.items_schema):
                    if idx >= len(items):
                        break
                    item_path = f"{path}[{idx}]"
                    keep_item, repaired_value = repair_or_drop(items[idx], item_schema, item_path)
                    if keep_item:
                        repaired_items.append(repaired_value)
                if len(items) > len(schema_config.items_schema):
                    tail = items[len(schema_config.items_schema) :]
                    if isinstance(schema_config.additional_items, dict):
                        for offset, item in enumerate(tail, start=len(schema_config.items_schema)):
                            item_path = f"{path}[{offset}]"
                            keep_item, repaired_value = repair_or_drop(item, schema_config.additional_items, item_path)
                            if keep_item:
                                repaired_items.append(repaired_value)
                    elif schema_config.additional_items is True or schema_config.additional_items is None:
                        repaired_items.extend(normalize_missing_values(item) for item in tail)
                    else:
                        for offset, _item in enumerate(tail, start=len(schema_config.items_schema)):
                            self._log("Dropped extra array item not covered by schema", f"{path}[{offset}]")
                items = repaired_items
            else:
                repaired_items = []
                for idx, item in enumerate(items):
                    item_path = f"{path}[{idx}]"
                    keep_item, repaired_value = repair_or_drop(item, schema_config.items_schema, item_path)
                    if keep_item:
                        repaired_items.append(repaired_value)
                items = repaired_items
        min_items = schema.get("minItems")
        if min_items is not None and len(items) < min_items:
            raise ValueError(f"Array at {path} does not meet minItems.")
        return items

    def _repair_object(self, value: Any, schema: dict[str, Any], path: str) -> JSONReturnType:
        if (
            self.schema_repair_mode == "salvage"
            and isinstance(value, list)
            and self._can_salvage_list_as_object(schema)
        ):
            mapped = self._map_list_to_object(value, schema, path)
            if mapped is not None:
                value = mapped
            elif path == "$" and len(value) == 1 and isinstance(value[0], dict):
                # Conservatively unwrap the common root wrapper shape: [{...}] -> {...}.
                value = value[0]
                self._log("Unwrapped single-item root array to object while salvaging", path)
        value = self._load_json_string_container(
            value,
            dict,
            path,
            "Unwrapped JSON string to object to match schema",
            "Repaired malformed JSON string to object to match schema",
        )
        if not isinstance(value, dict):
            raise ValueError(f"Expected object at {path}, got {type(value).__name__}.")

        schema_config = object_schema_config(schema)

        if self.schema_repair_mode == "salvage" and schema_config.required:
            value_with_salvage_fills = dict(value)
            for key in schema_config.required:
                if key in value_with_salvage_fills:
                    continue
                prop_schema = schema_config.properties.get(key)
                if prop_schema is None:
                    continue
                key_path = f"{path}.{key}"
                filled, filled_value = self._fill_missing_required_for_salvage(prop_schema, key_path)
                if filled:
                    value_with_salvage_fills[key] = filled_value
                    self._log("Filled missing required property while salvaging", key_path)
            value = value_with_salvage_fills

        missing_required = [key for key in schema_config.required if key not in value]
        if missing_required:
            raise ValueError(f"Missing required properties at {path}: {', '.join(missing_required)}")

        repaired: dict[str, JSONReturnType] = {}

        for key, prop_schema in schema_config.properties.items():
            key_path = f"{path}.{key}"
            if key in value:
                repaired[key] = self.repair_value(value[key], prop_schema, key_path)
            elif isinstance(prop_schema, dict) and "default" in prop_schema and key not in schema_config.required:
                repaired[key] = self._copy_json_value(prop_schema["default"], key_path, "default")
                self._log("Inserted default value for missing property", key_path)

        for key, raw_value in value.items():
            if key in schema_config.properties:
                continue
            key_path = f"{path}.{key}"
            matched: list[Any] = []
            unsupported_patterns: list[str] = []
            if schema_config.pattern_properties:
                matched, unsupported_patterns = match_pattern_properties(schema_config.pattern_properties, key)
            for pattern in unsupported_patterns:
                self._log(f"Skipped unsupported patternProperties regex '{pattern}'", key_path)
            if matched:
                repaired_value = self.repair_value(raw_value, matched[0], key_path)
                for prop_schema in matched[1:]:
                    repaired_value = self.repair_value(repaired_value, prop_schema, key_path)
                repaired[key] = repaired_value
                continue
            if isinstance(schema_config.additional_properties, dict):
                repaired[key] = self.repair_value(
                    raw_value,
                    cast("dict[str, Any]", schema_config.additional_properties),
                    key_path,
                )
                continue
            if schema_config.additional_properties is True or schema_config.additional_properties is None:
                repaired[key] = normalize_missing_values(raw_value)
                continue
            self._log("Dropped extra property not covered by schema", key_path)

        min_properties = schema.get("minProperties")
        if min_properties is not None and len(repaired) < min_properties:
            raise ValueError(f"Object at {path} does not meet minProperties.")
        return repaired

    def _map_list_to_object(
        self, value: list[Any], schema: dict[str, Any], path: str
    ) -> dict[str, JSONReturnType] | None:
        properties = schema.get("properties")
        if not isinstance(properties, dict) or not properties:
            return None

        typed_properties: dict[str, Any] = {}
        for key, prop_schema in properties.items():
            if not isinstance(key, str):
                raise SchemaDefinitionError("Schema object property names must be strings.")
            typed_properties[key] = prop_schema

        keys = list(typed_properties.keys())
        if len(value) != len(keys):
            return None

        mapped: dict[str, JSONReturnType] = {}
        for idx, key in enumerate(keys):
            key_path = f"{path}.{key}"
            try:
                mapped[key] = self.repair_value(value[idx], typed_properties[key], key_path)
            except SchemaDefinitionError:
                raise
            except ValueError:
                return None

        self._log("Mapped array to object by schema property order", path)
        return mapped

    def _fill_missing_required_for_salvage(self, schema: object, path: str) -> tuple[bool, JSONReturnType]:
        resolved_schema = self.resolve_schema(schema)
        if not isinstance(resolved_schema, dict):
            return False, ""

        if "default" in resolved_schema:
            return True, self._copy_json_value(resolved_schema["default"], path, "default")
        if "const" in resolved_schema:
            return True, self._copy_json_value(resolved_schema["const"], path, "const")
        enum_values = resolved_schema.get("enum")
        if enum_values:
            return True, self._copy_json_value(enum_values[0], path, "enum")

        expected_type = resolved_schema.get("type")
        if expected_type is None:
            if self.is_array_schema(resolved_schema):
                expected_type = "array"
            elif self.is_object_schema(resolved_schema):
                expected_type = "object"

        if expected_type == "array" and not resolved_schema.get("minItems"):
            return True, []
        if expected_type == "object" and not resolved_schema.get("minProperties"):
            return True, {}

        return False, ""

    def _fill_missing(self, schema: dict[str, Any], path: str) -> JSONReturnType:
        if "const" in schema:
            # Const/enum/default have priority over type inference.
            self._log("Filled missing value with const", path)
            return self._copy_json_value(schema["const"], path, "const")
        if "enum" in schema:
            enum_values = schema["enum"]
            if not enum_values:
                raise ValueError(f"Enum at {path} has no values.")
            self._log("Filled missing value with first enum value", path)
            return self._copy_json_value(enum_values[0], path, "enum")
        if "default" in schema:
            self._log("Filled missing value with default", path)
            return self._copy_json_value(schema["default"], path, "default")

        expected_type = schema.get("type")
        if isinstance(expected_type, list):
            for schema_type in expected_type:
                try:
                    return self._fill_missing({**schema, "type": schema_type}, path)
                except ValueError:
                    continue
            raise ValueError(f"Cannot infer missing value at {path}.")

        if expected_type is None:
            # Infer container types based on schema shape if type is omitted.
            if self.is_object_schema(schema):
                expected_type = "object"
            elif self.is_array_schema(schema):
                expected_type = "array"

        if expected_type == "string":
            self._log("Filled missing value with empty string", path)
            return ""
        if expected_type in ("integer", "number"):
            self._log("Filled missing value with 0", path)
            return 0
        if expected_type == "boolean":
            self._log("Filled missing value with false", path)
            return False
        if expected_type == "array":
            min_items = schema.get("minItems")
            if min_items:
                raise ValueError(f"Array at {path} requires at least {min_items} items.")
            self._log("Filled missing value with empty array", path)
            return []
        if expected_type == "object":
            min_properties = schema.get("minProperties")
            if min_properties:
                raise ValueError(f"Object at {path} requires at least {min_properties} properties.")
            self._log("Filled missing value with empty object", path)
            return {}
        if expected_type == "null":
            self._log("Filled missing value with null", path)
            return None

        raise ValueError(f"Cannot infer missing value at {path}.")

    def _coerce_scalar(self, value: Any, schema_type: str, path: str) -> JSONReturnType:
        if schema_type == "string":
            if isinstance(value, str):
                return value
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                self._log("Coerced number to string", path)
                return str(value)
            raise ValueError(f"Expected string at {path}.")

        if schema_type == "integer":
            if isinstance(value, bool):
                raise ValueError(f"Expected integer at {path}.")
            if isinstance(value, int):
                return value
            if isinstance(value, float):
                if value.is_integer():
                    self._log("Coerced number to integer", path)
                    return int(value)
                raise ValueError(f"Expected integer at {path}.")
            if isinstance(value, str):
                try:
                    int_value = int(value)
                except ValueError:
                    int_value = None
                if int_value is not None:
                    self._log("Coerced string to integer", path)
                    return int_value
                try:
                    num = float(value)
                except ValueError as exc:
                    raise ValueError(f"Expected integer at {path}.") from exc
                if not num.is_integer():
                    raise ValueError(f"Expected integer at {path}.")
                self._log("Coerced number to integer", path)
                return int(num)
            raise ValueError(f"Expected integer at {path}.")

        if schema_type == "number":
            if isinstance(value, bool):
                raise ValueError(f"Expected number at {path}.")
            if isinstance(value, (int, float)):
                return value
            if isinstance(value, str):
                try:
                    float_value = float(value)
                except ValueError as exc:
                    raise ValueError(f"Expected number at {path}.") from exc
                self._log("Coerced string to number", path)
                return float_value
            raise ValueError(f"Expected number at {path}.")

        if schema_type == "boolean":
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                lowered = value.lower()
                if lowered in ("true", "yes", "y", "on", "1"):
                    self._log("Coerced string to boolean", path)
                    return True
                if lowered in ("false", "no", "n", "off", "0"):
                    self._log("Coerced string to boolean", path)
                    return False
            if isinstance(value, (int, float)) and not isinstance(value, bool) and value in (0, 1):
                self._log("Coerced number to boolean", path)
                return bool(value)
            raise ValueError(f"Expected boolean at {path}.")

        if schema_type == "null":
            if value is None:
                return None
            raise ValueError(f"Expected null at {path}.")

        raise SchemaDefinitionError(f"Unsupported schema type {schema_type} at {path}.")

    def _apply_enum_const(self, value: JSONReturnType, schema: dict[str, Any], path: str) -> JSONReturnType:
        if "const" in schema and value != schema["const"]:
            raise ValueError(f"Value at {path} does not match const.")
        if "enum" in schema and value not in schema["enum"]:
            raise ValueError(f"Value at {path} does not match enum.")
        return value

    def _resolve_ref(self, ref: str) -> dict[str, Any] | bool:
        if not ref.startswith("#/"):
            raise SchemaDefinitionError(f"Unsupported $ref: {ref}")
        parts = ref.lstrip("#/").split("/")
        current: Any = self.root_schema
        for part in parts:
            resolved_part = part.replace("~1", "/").replace("~0", "~")
            if not isinstance(current, dict) or resolved_part not in current:
                raise SchemaDefinitionError(f"Unresolvable $ref: {ref}")
            current = current[resolved_part]
        if isinstance(current, dict):
            return current
        if current is True:
            return True
        if current is False:
            return False
        raise SchemaDefinitionError(f"Unresolvable $ref: {ref}")

    def _copy_json_value(self, value: Any, path: str, label: str) -> JSONReturnType:
        if value is None or isinstance(value, (str, int, float, bool)):
            return value
        if isinstance(value, list):
            return [self._copy_json_value(item, f"{path}[{idx}]", label) for idx, item in enumerate(value)]
        if isinstance(value, dict):
            copied: dict[str, JSONReturnType] = {}
            for key, item in value.items():
                if not isinstance(key, str):
                    raise ValueError(f"{label.capitalize()} value at {path} contains a non-string key.")
                copied[key] = self._copy_json_value(item, f"{path}.{key}", label)
            return copied
        raise ValueError(f"{label.capitalize()} value at {path} is not JSON compatible.")

    def _prepare_schema_for_validation(self, schema: object) -> dict[str, Any]:
        normalized = _prepare_schema_for_validation_node(schema)
        if not isinstance(normalized, dict):
            raise ValueError("Schema must be an object.")
        return normalized

```

### `src/json_repair/utils/__init__.py`

```py
"""Internal utility helpers for json_repair."""

```

### `src/json_repair/utils/constants.py`

```py
from typing import Any


class MissingValueType:
    def __repr__(self) -> str:
        return "<MISSING_VALUE>"

    def __deepcopy__(self, memo: dict[int, Any]) -> "MissingValueType":
        return self


MISSING_VALUE = MissingValueType()

JSONReturnType = dict[str, Any] | list[Any] | str | float | int | bool | None
STRING_DELIMITERS: list[str] = ['"', "'", "“", "”"]

```

### `src/json_repair/utils/json_context.py`

```py
from enum import Enum, auto
from types import TracebackType
from typing import Literal


class ContextValues(Enum):
    OBJECT_KEY = auto()
    OBJECT_VALUE = auto()
    ARRAY = auto()


class _JsonContextEntry:
    __slots__ = ("context", "value")

    def __init__(self, context: "JsonContext", value: ContextValues) -> None:
        self.context = context
        self.value = value

    def __enter__(self) -> None:
        self.context.set(self.value)

    def __exit__(
        self,
        _exc_type: type[BaseException] | None,
        _exc: BaseException | None,
        _traceback: TracebackType | None,
    ) -> Literal[False]:
        self.context.reset()
        return False


class JsonContext:
    def __init__(self) -> None:
        self.context: list[ContextValues] = []
        self.current: ContextValues | None = None
        self.empty: bool = True

    def enter(self, value: ContextValues) -> _JsonContextEntry:
        return _JsonContextEntry(self, value)

    def set(self, value: ContextValues) -> None:
        """
        Set a new context value.

        Args:
            value (ContextValues): The context value to be added.

        Returns:
            None
        """
        self.context.append(value)
        self.current = value
        self.empty = False

    def reset(self) -> None:
        """
        Remove the most recent context value.

        Returns:
            None
        """
        try:
            self.context.pop()
            self.current = self.context[-1]
        except IndexError:
            self.current = None
            self.empty = True

    def clear(self) -> None:
        """
        Remove all context values.

        Returns:
            None
        """
        self.context.clear()
        self.current = None
        self.empty = True

```

### `src/json_repair/utils/object_comparer.py`

```py
from typing import Any


class ObjectComparer:  # pragma: no cover
    def __init__(self) -> None:
        pass  # No operation performed in the constructor

    @staticmethod
    def is_same_object(obj1: Any, obj2: Any) -> bool:
        """
        Recursively compares two objects and ensures that:
        - Their types match
        - Their keys/structure match
        """
        if type(obj1) is not type(obj2):
            # Fail immediately if the types don't match
            return False

        if isinstance(obj1, dict):
            # Check that both are dicts and same length
            if not isinstance(obj2, dict) or len(obj1) != len(obj2):
                return False
            for key in obj1:
                if key not in obj2:
                    return False
                # Recursively compare each value
                if not ObjectComparer.is_same_object(obj1[key], obj2[key]):
                    return False
            return True

        if isinstance(obj1, list):
            # Check that both are lists and same length
            if not isinstance(obj2, list) or len(obj1) != len(obj2):
                return False
            # Recursively compare each item
            return all(ObjectComparer.is_same_object(obj1[i], obj2[i]) for i in range(len(obj1)))

        # For atomic values: types already match, so return True
        return True

    @staticmethod
    def is_strictly_empty(value: Any) -> bool:
        """
        Returns True if value is an empty container (str, list, dict, set, tuple).
        Returns False for non-containers like None, 0, False, etc.
        """
        return isinstance(value, str | list | dict | set | tuple) and len(value) == 0

```

### `src/json_repair/utils/pattern_properties.py`

```py
from collections.abc import Mapping
from typing import Any

_UNSUPPORTED_REGEX_TOKENS = frozenset({".", "^", "$", "*", "+", "?", "{", "}", "[", "]", "|", "(", ")", "\\"})


def match_pattern_properties(
    pattern_properties: Mapping[str, Any],
    key: str,
) -> tuple[list[Any], list[str]]:
    """Match JSON Schema patternProperties using a safe literal+anchor subset.

    Supported forms:
    - "token"      -> key contains token
    - "^token"     -> key starts with token
    - "token$"     -> key ends with token
    - "^token$"    -> key equals token

    Any pattern using additional regex tokens is treated as unsupported and skipped.
    The caller can log unsupported patterns using the returned list.
    """

    if not pattern_properties:
        return [], []

    matched_schemas: list[Any] = []
    unsupported_patterns: list[str] = []

    for pattern, schema in pattern_properties.items():
        anchored_start = pattern.startswith("^")
        anchored_end = pattern.endswith("$")
        literal = pattern[1 if anchored_start else 0 : -1 if anchored_end else None]

        if any(token in literal for token in _UNSUPPORTED_REGEX_TOKENS):
            unsupported_patterns.append(pattern)
            continue

        if anchored_start and anchored_end:
            is_match = key == literal
        elif anchored_start:
            is_match = key.startswith(literal)
        elif anchored_end:
            is_match = key.endswith(literal)
        else:
            is_match = literal in key

        if is_match:
            matched_schemas.append(schema)

    return matched_schemas, unsupported_patterns

```

### `src/json_repair/utils/string_file_wrapper.py`

```py
import os
from typing import TextIO


class StringFileWrapper:
    # This is a trick to simplify the code, transform the filedescriptor handling into a string handling
    def __init__(self, fd: TextIO, chunk_length: int) -> None:
        """
        Initialize the StringFileWrapper with a file descriptor and chunk length.

        Args:
            fd (TextIO): The file descriptor to wrap.
            CHUNK_LENGTH (int): The length of each chunk to read from the file.

        Attributes:
            fd (TextIO): The wrapped file descriptor.
            length (int): The total length of the file content.
            buffers (dict[int, str]): Dictionary to store chunks of file content.
            buffer_length (int): The length of each buffer chunk.
        """
        self.fd = fd
        # Buffers are chunks of text read from the file and cached to reduce disk access.
        self.buffers: dict[int, str] = {}
        if not chunk_length or chunk_length < 2:
            chunk_length = 1_000_000
        # chunk_length now refers to the number of characters per chunk.
        self.buffer_length = chunk_length
        # Keep track of the starting file position ("cookie") for each chunk so we can
        # seek safely without landing in the middle of a multibyte code point.
        self._initial_position = fd.tell()
        self._chunk_positions: list[int] = [self._initial_position]
        self.length: int | None = None

    def get_buffer(self, index: int) -> str:
        """
        Retrieve or load a buffer chunk from the file.

        Args:
            index (int): The index of the buffer chunk to retrieve.

        Returns:
            str: The buffer chunk at the specified index.
        """
        if index < 0:
            raise IndexError("Negative indexing is not supported")

        cached = self.buffers.get(index)
        if cached is not None:
            return cached

        self._ensure_chunk_position(index)
        start_pos = self._chunk_positions[index]
        self.fd.seek(start_pos)
        chunk = self.fd.read(self.buffer_length)
        if not chunk:
            raise IndexError("Chunk index out of range")
        end_pos = self.fd.tell()
        if len(self._chunk_positions) <= index + 1:
            self._chunk_positions.append(end_pos)
        if len(chunk) < self.buffer_length:
            self.length = index * self.buffer_length + len(chunk)

        self.buffers[index] = chunk
        # Save memory by keeping max 2MB buffer chunks and min 2 chunks
        max_buffers = max(2, int(2_000_000 / self.buffer_length))
        if len(self.buffers) > max_buffers:
            oldest_key = next(iter(self.buffers))
            if oldest_key != index:
                self.buffers.pop(oldest_key)
        return chunk

    def __getitem__(self, index: int | slice) -> str:
        """
        Retrieve a character or a slice of characters from the file.

        Args:
            index (Union[int, slice]): The index or slice of characters to retrieve.

        Returns:
            str: The character(s) at the specified index or slice.
        """
        # The buffer is an array that is seek like a RAM:
        # self.buffers[index]: the row in the array of length 1MB, index is `i` modulo CHUNK_LENGTH
        # self.buffures[index][j]: the column of the row that is `i` remainder CHUNK_LENGTH
        if isinstance(index, slice):
            start, stop, step = self._normalize_slice(index)

            if step == 0:
                raise ValueError("slice step cannot be zero")
            if step != 1:
                return "".join(self[i] for i in range(start, stop, step))

            if start >= stop:
                return ""
            return self._slice_from_buffers(start, stop)
        if index < 0:
            index += len(self)
        if index < 0:
            raise IndexError("string index out of range")
        buffer_index = index // self.buffer_length
        buffer = self.get_buffer(buffer_index)
        return buffer[index % self.buffer_length]

    def __len__(self) -> int:
        """
        Get the total length of the file.

        Returns:
            int: The total number of characters in the file.
        """
        if self.length is None:
            while self.length is None:
                chunk_index = len(self._chunk_positions)
                self._ensure_chunk_position(chunk_index)
        assert self.length is not None
        return self.length

    def _normalize_slice(self, index: slice) -> tuple[int, int, int]:
        total_len = len(self)
        start = 0 if index.start is None else index.start
        stop = total_len if index.stop is None else index.stop
        step = 1 if index.step is None else index.step

        if start < 0:
            start += total_len
        if stop < 0:
            stop += total_len

        start = max(start, 0)
        stop = min(stop, total_len)
        return start, stop, step

    def _slice_from_buffers(self, start: int, stop: int) -> str:
        buffer_index = start // self.buffer_length
        buffer_end = (stop - 1) // self.buffer_length
        start_mod = start % self.buffer_length
        stop_mod = stop % self.buffer_length
        if stop_mod == 0 and stop > start:
            stop_mod = self.buffer_length
        if buffer_index == buffer_end:
            buffer = self.get_buffer(buffer_index)
            return buffer[start_mod:stop_mod]

        start_slice = self.get_buffer(buffer_index)[start_mod:]
        end_slice = self.get_buffer(buffer_end)[:stop_mod]
        middle_slices = [self.get_buffer(i) for i in range(buffer_index + 1, buffer_end)]
        return start_slice + "".join(middle_slices) + end_slice

    def __setitem__(self, index: int | slice, value: str) -> None:  # pragma: no cover
        """
        Set a character or a slice of characters in the file.

        Args:
            index (slice): The slice of characters to set.
            value (str): The value to set at the specified index or slice.
        """
        start = index.start or 0 if isinstance(index, slice) else index or 0

        if start < 0:
            start += len(self)

        current_position = self.fd.tell()
        self.fd.seek(self._initial_position + start)
        self.fd.write(value)
        self.fd.seek(current_position)

    def _ensure_chunk_position(self, chunk_index: int) -> None:
        """
        Ensure that we know the starting file position for the given chunk index.
        """
        while len(self._chunk_positions) <= chunk_index:
            prev_index = len(self._chunk_positions) - 1
            start_pos = self._chunk_positions[-1]
            self.fd.seek(start_pos, os.SEEK_SET)
            chunk = self.fd.read(self.buffer_length)
            end_pos = self.fd.tell()
            if len(chunk) < self.buffer_length:
                self.length = prev_index * self.buffer_length + len(chunk)
            self._chunk_positions.append(end_pos)
            if not chunk:
                break
        if len(self._chunk_positions) <= chunk_index:
            raise IndexError("Chunk index out of range")

```

### `tests/__init__.py`

```py
"""Test package markers for Ruff package checks."""

```

### `tests/invalid.json`

```json
[
    {
      "_id": "655b66256574f09bdae8abe8",
      "index": 0,
      "guid": "31082ae3-b0f3-4406-90f4-cc450bd4379d",
      "isActive": false,
      "balance": "$2,562.78",
      "picture": "http://placehold.it/32x32",
      "age": 32,
      "eyeColor": "brown",
      "name": "Glover Rivas",
      "gender": "male",
      "company": "EMPIRICA",
      "email": "gloverrivas@empirica.com",
      "phone": "+1 (842) 507-3063",
      "address": "536 Montague Terrace, Jenkinsville, Kentucky, 2235",
      "about": "Mollit consectetur excepteur voluptate tempor dolore ullamco enim irure ullamco non enim officia. Voluptate occaecat proident laboris ea Lorem cupidatat reprehenderit nisi nisi aliqua. Amet nulla ipsum deserunt excepteur amet ad aute aute ex. Et enim minim sit veniam est quis dolor nisi sunt quis eiusmod in. Amet eiusmod cillum sunt occaecat dolor laboris voluptate in eiusmod irure aliqua duis.",
      "registered": "2023-11-18T09:32:36 -01:00",
      "latitude": 36.26102,
      "longitude": -91.304608,
      "tags": [
        "non",
        "tempor",
        "do",
        "ullamco",
        "dolore",
        "sunt",
        "ipsum"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Cara Shepherd"
        },
        {
          "id": 1,
          "name": "Mason Farley"
        },
        {
          "id": 2,
          "name": "Harriet Cochran"
        }
      ],
      "greeting": "Hello, Glover Rivas! You have 7 unread messages.",
      "favoriteFruit": "strawberry"
    },
    {
      "_id": "655b662585364bc57278bb6f",
      "index": 1,
      "guid": "0dea7a3a-f812-4dde-b78d-7a9b58e5da05",
      "isActive": true,
      "balance": "$1,359.48",
      "picture": "http://placehold.it/32x32",
      "age": 38,
      "eyeColor": "brown",
      "name": "Brandi Moreno",
      "gender": "female",
      "company": "MARQET",
      "email": "brandimoreno@marqet.com",
      "phone": "+1 (850) 434-2077",
      "address": "537 Doone Court, Waiohinu, Michigan, 3215",
      "about": "Irure proident adipisicing do Lorem do incididunt in laborum in eiusmod eiusmod ad elit proident. Eiusmod dolor ex magna magna occaecat. Nulla deserunt velit ex exercitation et irure sunt. Cupidatat ut excepteur ea quis labore sint cupidatat incididunt amet eu consectetur cillum ipsum proident. Occaecat exercitation aute laborum dolor proident reprehenderit laborum in voluptate culpa. Exercitation nulla adipisicing culpa aute est deserunt ea nisi deserunt consequat occaecat ut et non. Incididunt ex exercitation dolor dolor anim cillum dolore.",
      "registered": "2015-09-03T11:47:15 -02:00",
      "latitude": -19.768953,
      "longitude": 8.948458,
      "tags": [
        "laboris",
        "occaecat",
        "laborum",
        "laborum",
        "ex",
        "cillum",
        "occaecat"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Erna Kelly"
        },
        {
          "id": 1,
          "name": "Black Mays"
        },
        {
          "id": 2,
          "name": "Davis Buck"
        }
      ],
      "greeting": "Hello, Brandi Moreno! You have 1 unread messages.",
      "favoriteFruit": "apple"
    },
    {
      "_id": "655b6625870da431bcf5e0c2",
      "index": 2,
      "guid": "b17f6e3f-c898-4334-abbf-05cf222f143b",
      "isActive": false,
      "balance": "$1,493.77",
      "picture": "http://placehold.it/32x32",
      "age": 20,
      "eyeColor": "brown",
      "name": "Moody Meadows",
      "gender": "male",
      "company": "OPTIQUE",
      "email": "moodymeadows@optique.com",
      "phone": "+1 (993) 566-3041",
      "address": "766 Osborn Street, Bath, Maine, 7666",
      "about": "Non commodo excepteur nostrud qui adipisicing aliquip dolor minim nulla culpa proident. In ad cupidatat ea mollit ex est do deserunt proident nostrud. Cillum id id eiusmod amet exercitation nostrud cillum sunt deserunt dolore deserunt eiusmod mollit. Ut ex tempor ad laboris voluptate labore id officia fugiat exercitation amet.",
      "registered": "2015-01-16T02:48:28 -01:00",
      "latitude": -25.847327,
      "longitude": 63.95991,
      "tags": [
        "aute",
        "commodo",
        "adipisicing",
        "nostrud",
        "duis",
        "mollit",
        "ut"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Lacey Cash"
        },
        {
          "id": 1,
          "name": "Gabrielle Harmon"
        },
        {
          "id": 2,
          "name": "Ellis Lambert"
        }
      ],
      "greeting": "Hello, Moody Meadows! You have 4 unread messages.",
      "favoriteFruit": "strawberry"
    },
    {
      "_id": "655b6625f3e1bf422220854e",
      "index": 3,
      "guid": "92229883-2bfd-4974-a08c-1b506b372e46",
      "isActive": false,
      "balance": "$2,215.34",
      "picture": "http://placehold.it/32x32",
      "age": 22,
      "eyeColor": "brown",
      "name": "Heath Nguyen",
      "gender": "male",
      "company": "BLEENDOT",
      "email": "heathnguyen@bleendot.com",
      "phone": "+1 (989) 512-2797",
      "address": "135 Milton Street, Graniteville, Nebraska, 276",
      "about": "Consequat aliquip irure Lorem cupidatat nulla magna ullamco nulla voluptate adipisicing anim consectetur tempor aliquip. Magna aliqua nulla eu tempor esse proident. Proident fugiat ad ex Lorem reprehenderit dolor aliquip labore labore aliquip. Deserunt aute enim ea minim officia anim culpa sint commodo. Cillum consectetur excepteur aliqua exercitation Lorem veniam voluptate.",
      "registered": "2016-07-06T01:31:07 -02:00",
      "latitude": -60.997048,
      "longitude": -102.397885,
      "tags": [
        "do",
        "ad",
        "consequat",
        "irure",
        "tempor",
        "elit",
        "minim"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Walker Hernandez"
        },
        {
          "id": 1,
          "name": "Maria Lane"
        },
        {
          "id": 2,
          "name": "Mcknight Barron"
        }
      ],
      "greeting": "Hello, Heath Nguyen! You have 4 unread messages.",
      "favoriteFruit": "apple"
    },
    {
      "_id": "655b6625519a5b5e4b6742bf",
      "index": 4,
      "guid": "c5dc685f-6d0d-4173-b4cf-f5df29a1e8ef",
      "isActive": true,
      "balance": "$1,358.90",
      "picture": "http://placehold.it/32x32",
      "age": 33,
      "eyeColor": "brown",
      "name": "Deidre Duke",
      "gender": "female",
      "company": "OATFARM",
      "email": "deidreduke@oatfarm.com",
      "phone": "+1 (875) 587-3256",
      "address": "487 Schaefer Street, Wattsville, West Virginia, 4506",
      "about": "Laboris eu nulla esse magna sit eu deserunt non est aliqua exercitation commodo. Ad occaecat qui qui laborum dolore anim Lorem. Est qui occaecat irure enim deserunt enim aliqua ex deserunt incididunt esse. Quis in minim laboris proident non mollit. Magna ea do labore commodo. Et elit esse esse occaecat officia ipsum nisi.",
      "registered": "2021-09-12T04:17:08 -02:00",
      "latitude": 68.609781,
      "longitude": -87.509134,
      "tags": [
        "mollit",
        "cupidatat",
        "irure",
        "sit",
        "consequat",
        "anim",
        "fugiat"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Bean Paul"
        },
        {
          "id": 1,
          "name": "Cochran Hubbard"
        },
        {
          "id": 2,
          "name": "Rodgers Atkinson"
        }
      ],
      "greeting": "Hello, Deidre Duke! You have 6 unread messages.",
      "favoriteFruit": "apple"
    },
    {
      "_id": "655b6625a19b3f7e5f82f0ea",
      "index": 5,
      "guid": "75f3c264-baa1-47a0-b21c-4edac23d9935",
      "isActive": true,
      "balance": "$3,554.36",
      "picture": "http://placehold.it/32x32",
      "age": 26,
      "eyeColor": "blue",
      "name": "Lydia Holland",
      "gender": "female",
      "company": "ESCENTA",
      "email": "lydiaholland@escenta.com",
      "phone": "+1 (927) 482-3436",
      "address": "554 Rockaway Parkway, Kohatk, Montana, 6316",
      "about": "Consectetur ea est labore commodo laborum mollit pariatur non enim. Est dolore et non laboris tempor. Ea incididunt ut adipisicing cillum labore officia tempor eiusmod commodo. Cillum fugiat ex consectetur ut nostrud anim nostrud exercitation ut duis in ea. Eu et id fugiat est duis eiusmod ullamco quis officia minim sint ea nisi in.",
      "registered": "2018-03-13T01:48:56 -01:00",
      "latitude": -88.495799,
      "longitude": 71.840667,
      "tags": [
        "veniam",
        "minim",
        "consequat",
        "consequat",
        "incididunt",
        "consequat",
        "elit"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Debra Massey"
        },
        {
          "id": 1,
          "name": Weiss Savage
        },
        {
          "id": 2,
          "name": "Shannon Guerra"
        }
      ],
      "greeting": "Hello, Lydia Holland! You have 5 unread messages.",
      "favoriteFruit": "banana"
    }
```

### `tests/profiler.py`

```py
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pstats
import time
from cProfile import Profile
from pstats import SortKey, Stats

from src.json_repair.json_repair import repair_json

# Hack: Monkey patch pstats to change the formatting method and increase precision
pstats.__dict__["f8"] = lambda x: f"{x:14.9f}"

m = """
[
  {
    "_id": "655b66256574f09bdae8abe8",
    "index": 0,
    "guid": "31082ae3-b0f3-4406-90f4-cc450bd4379d",
    "isActive": false,
    "balance": "$2,562.78",
    "picture": "http://placehold.it/32x32",
    "age": 32,
    "eyeColor": "brown",
    "name": "Glover Rivas",
    "gender": "male",
    "company": "EMPIRICA",
    "email": "gloverrivas@empirica.com",
    "phone": "+1 (842) 507-3063",
    "address": "536 Montague Terrace, Jenkinsville, Kentucky, 2235",
    "about": "Mollit consectetur excepteur voluptate tempor dolore ullamco enim irure ullamco non enim officia. Voluptate occaecat proident laboris ea Lorem cupidatat reprehenderit nisi nisi aliqua. Amet nulla ipsum deserunt excepteur amet ad aute aute ex. Et enim minim sit veniam est quis dolor nisi sunt quis eiusmod in. Amet eiusmod cillum sunt occaecat dolor laboris voluptate in eiusmod irure aliqua duis.",
    "registered": "2023-11-18T09:32:36 -01:00",
    "latitude": 36.26102,
    "longitude": -91.304608,
    "tags": [
      "non",
      "tempor",
      "do",
      "ullamco",
      "dolore",
      "sunt",
      "ipsum"
    ],
    "friends": [ // comment
      {
        "id": 0,
        "name": "Cara Shepherd"
      },
      {
        "id": 1,
        "name": "Mason Farley"
      },
      {
        "id": 2,
        "name": "Harriet Cochran"
      }
    ],
    "greeting": "Hello, Glover Rivas! You have 7 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": "655b662585364bc57278bb6f",
    "index": 1,
    "guid": "0dea7a3a-f812-4dde-b78d-7a9b58e5da05",
    "isActive": true,
    "balance": "$1,359.48",
    "picture": "http://placehold.it/32x32",
    "age": 38,
    "eyeColor": "brown",
    "name": "Brandi Moreno",
    "gender": "female",
    "company": "MARQET",
    "email": "brandimoreno@marqet.com",
    "phone": "+1 (850) 434-2077",
    "address": "537 Doone Court, Waiohinu, Michigan, 3215",
    "about": "Irure proident adipisicing do Lorem do incididunt in laborum in eiusmod eiusmod ad elit proident. Eiusmod dolor ex magna magna occaecat. Nulla deserunt velit ex exercitation et irure sunt. Cupidatat ut excepteur ea quis labore sint cupidatat incididunt amet eu consectetur cillum ipsum proident. Occaecat exercitation aute laborum dolor proident reprehenderit laborum in voluptate culpa. Exercitation nulla adipisicing culpa aute est deserunt ea nisi deserunt consequat occaecat ut et non. Incididunt ex exercitation dolor dolor anim cillum dolore.",
    "registered": "2015-09-03T11:47:15 -02:00",
    "latitude": -19.768953,
    "longitude": 8.948458,
    "tags": [
      "laboris",
      "occaecat",
      "laborum",
      "laborum",
      "ex",
      "cillum",
      "occaecat"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Erna Kelly"
      },
      {
        "id": 1,
        "name": "Black Mays"
      },
      {
        "id": 2,
        "name": "Davis Buck"
      }
    ],
    "greeting": "Hello, Brandi Moreno! You have 1 unread messages.",
    "favoriteFruit": "apple"
  },
  {
    "_id": "655b6625870da431bcf5e0c2",
    "index": 2,
    "guid": "b17f6e3f-c898-4334-abbf-05cf222f143b,
    "isActive": false,
    "balance": "$1,493.77",
    "picture": "http://placehold.it/32x32",
    "age": 20,
    "eyeColor": "brown",
    "name": "Moody Meadows",
    "gender": "male",
    "company": "OPTIQUE",
    "email": "moodymeadows@optique.com",
    "phone": "+1 (993) 566-3041",
    "address": "766 Osborn Street, Bath, Maine, 7666",
    "about": "Non commodo excepteur nostrud qui adipisicing aliquip dolor minim nulla culpa proident. In ad cupidatat ea mollit ex est do deserunt proident nostrud. Cillum id id eiusmod amet exercitation nostrud cillum sunt deserunt dolore deserunt eiusmod mollit. Ut ex tempor ad laboris voluptate labore id officia fugiat exercitation amet.",
    "registered": "2015-01-16T02:48:28 -01:00",
    "latitude": -25.847327,
    "longitude": 63.95991,
    "tags": [
      "aute",
      "commodo",
      "adipisicing",
      "nostrud",
      "duis",
      "mollit",
      "ut"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Lacey Cash"
      },
      {
        "id": 1,
        "name": "Gabrielle Harmon"
      },
      {
        "id": 2,
        "name": "Ellis Lambert"
      }
    ],
    "greeting": "Hello, Moody Meadows! You have 4 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": "655b6625f3e1bf422220854e",
    "index": 3,
    "guid": "92229883-2bfd-4974-a08c-1b506b372e46",
    "isActive": false,
    "balance": "$2,215.34",
    "picture": "http://placehold.it/32x32",
    "age": 22,
    "eyeColor": "brown",
    "name": "Heath Nguyen",
    "gender": "male",
    "company": "BLEENDOT",
    "email": "heathnguyen@bleendot.com",
    "phone": "+1 (989) 512-2797",
    "address": "135 Milton Street, Graniteville, Nebraska, 276",
    "about": "Consequat aliquip irure Lorem cupidatat nulla magna ullamco nulla voluptate adipisicing anim consectetur tempor aliquip. Magna aliqua nulla eu tempor esse proident. Proident fugiat ad ex Lorem reprehenderit dolor aliquip labore labore aliquip. Deserunt aute enim ea minim officia anim culpa sint commodo. Cillum consectetur excepteur aliqua exercitation Lorem veniam voluptate.",
    "registered": "2016-07-06T01:31:07 -02:00",
    "latitude": -60.997048,
    "longitude": -102.397885,
    "tags": [
      "do",
      "ad",
      "consequat",
      "irure",
      "tempor",
      "elit",
      "minim"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Walker Hernandez"
      },
      {
        "id": 1,
        "name": "Maria Lane"
      },
      {
        "id": 2,
        "name": "Mcknight Barron"
      }
    ],
    "greeting": "Hello, Heath Nguyen! You have 4 unread messages.",
    "favoriteFruit": "apple"
  },
  {
    "_id": "655b6625519a5b5e4b6742bf",
    "index": 4,
    "guid": "c5dc685f-6d0d-4173-b4cf-f5df29a1e8ef",
    "isActive": true,
    "balance": "$1,358.90",
    "picture": "http://placehold.it/32x32",
    "age": 33,
    "eyeColor": "brown",
    "name": "Deidre Duke",
    "gender": "female",
    "company": "OATFARM",
    "email": "deidreduke@oatfarm.com",
    "phone": "+1 (875) 587-3256",
    "address": "487 Schaefer Street, Wattsville, West Virginia, 4506",
    "about": "Laboris eu nulla esse magna sit eu deserunt non est aliqua exercitation commodo. Ad occaecat qui qui laborum dolore anim Lorem. Est qui occaecat irure enim deserunt enim aliqua ex deserunt incididunt esse. Quis in minim laboris proident non mollit. Magna ea do labore commodo. Et elit esse esse occaecat officia ipsum nisi.",
    "registered": "2021-09-12T04:17:08 -02:00",
    "latitude": 68.609781,
    "longitude": -87.509134,
    "tags": [
      "mollit",
      "cupidatat",
      "irure",
      "sit",
      "consequat",
      "anim",
      "fugiat"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Bean Paul"
      },
      {
        "id": 1,
        "name": "Cochran Hubbard"
      },
      {
        "id": 2,
        "name": "Rodgers Atkinson"
      }
    ],
    "greeting": "Hello, Deidre Duke! You have 6 unread messages.",
    "favoriteFruit": "apple"
  },
  {
    "_id": "655b6625a19b3f7e5f82f0ea",
    "index": 5,
    "guid": "75f3c264-baa1-47a0-b21c-4edac23d9935",
    "isActive": true,
    "balance": "$3,554.36",
    "picture": "http://placehold.it/32x32",
    "age": 26,
    "eyeColor": "blue",
    "name": "Lydia Holland",
    "gender": "female",
    "company": "ESCENTA",
    "email": "lydiaholland@escenta.com",
    "phone": "+1 (927) 482-3436",
    "address": "554 Rockaway Parkway, Kohatk, Montana, 6316",
    "about": "Consectetur ea est labore commodo laborum mollit pariatur non enim. Est dolore et non laboris tempor. Ea incididunt ut adipisicing cillum labore officia tempor eiusmod commodo. Cillum fugiat ex consectetur ut nostrud anim nostrud exercitation ut duis in ea. Eu et id fugiat est duis eiusmod ullamco quis officia minim sint ea nisi in.",
    "registered": "2018-03-13T01:48:56 -01:00",
    "latitude": -88.495799,
    "longitude": 71.840667,
    "tags": [
      "veniam",
      "minim",
      "consequat",
      "consequat",
      "incididunt",
      "consequat",
      "elit"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Debra Massey"
      },
      {
        "id": 1,
        "name": "Weiss Savage"
      },
      {
        "id": 2,
        "name": "Shannon Guerra"
      }
    ],
    "greeting": "Hello, Lydia Holland! You have 5 unread messages.",
    "favoriteFruit": "banana"
  },
  { "key": "value" "key2": "value }


    """


def benchmark(name, m, ro, sjl):
    start = time.time()
    for _ in range(10000):
        repair_json(json_str=m, return_objects=ro, skip_json_loads=sjl)
    print(f"{name} - {time.time() - start} \n", flush=True)


with Profile() as profile:
    print(f"{benchmark('benchmark', m, sjl=True, ro=False) = }")
    (Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats())

```

### `tests/test_docs_app_schema.py`

```py
import pytest

pytest.importorskip("flask")

from docs.app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as test_client:
        yield test_client


def test_docs_api_without_schema_keeps_existing_behavior(client):
    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": '{"value": "1"}'},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert payload == [{"value": "1"}, []]


def test_docs_api_schema_null_is_treated_as_missing(client):
    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": '{"value": "1"}', "schema": None},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert payload == [{"value": "1"}, []]


def test_docs_api_schema_guides_coercion(client):
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"value": {"type": "integer"}},
        "required": ["value"],
    }

    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": '{"value": "1"}', "schema": schema},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert isinstance(payload, list)
    assert payload[0] == {"value": 1}
    assert isinstance(payload[1], list)
    assert payload[1]


def test_docs_api_rejects_invalid_schema_type(client):
    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": '{"value": "1"}', "schema": []},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "schema must be a JSON object or boolean."}


def test_docs_api_schema_validation_error_returns_400(client):
    pytest.importorskip("jsonschema")
    response = client.post(
        "/api/repair-json",
        json={
            "malformedJSON": '"bbb"',
            "schema": {"type": "string", "pattern": "^a+$"},
        },
    )

    assert response.status_code == 400
    payload = response.get_json()
    assert isinstance(payload, dict)
    assert "error" in payload
    assert "does not match" in payload["error"]


def test_docs_api_rejects_circular_schema_ref(client):
    pytest.importorskip("jsonschema")
    schema = {
        "$ref": "#/definitions/a",
        "definitions": {
            "a": {"$ref": "#/definitions/a"},
        },
    }

    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": "{}", "schema": schema},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Circular $ref detected: #/definitions/a"}


def test_docs_api_rejects_invalid_schema_repair_mode_type(client):
    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": '{"value": "1"}', "schemaRepairMode": True},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "schemaRepairMode must be a string."}


def test_docs_api_rejects_invalid_schema_repair_mode_value(client):
    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": '{"value": "1"}', "schemaRepairMode": "unknown"},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "schemaRepairMode must be 'standard' or 'salvage'."}


def test_docs_api_rejects_salvage_mode_without_schema(client):
    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": '{"value": "1"}', "schemaRepairMode": "salvage"},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "schemaRepairMode='salvage' requires schema."}


def test_docs_api_salvage_mode_drops_invalid_array_items(client):
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "score": {"type": "number"},
                    },
                    "required": ["id", "score"],
                },
            }
        },
        "required": ["items"],
    }

    response = client.post(
        "/api/repair-json",
        json={
            "malformedJSON": '{"items":[{"id":1,"score":85.6},{"id":2,"score":"N/A"}]}',
            "schema": schema,
            "schemaRepairMode": "salvage",
        },
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert isinstance(payload, list)
    assert payload[0] == {"items": [{"id": 1, "score": 85.6}]}


def test_docs_api_deep_schema_returns_400_instead_of_500(client):
    pytest.importorskip("jsonschema")
    schema = {"type": "object"}
    for _ in range(550):
        schema = {"allOf": [schema]}

    response = client.post(
        "/api/repair-json",
        json={"malformedJSON": "{}", "schema": schema},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Input schema nesting exceeds the supported schema recursion depth."}

```

### `tests/test_json_repair.py`

```py
import importlib
import sys

import pytest

from src.json_repair.json_parser import JSONParser
from src.json_repair.json_repair import loads, repair_json

json_repair_module = importlib.import_module("src.json_repair.json_repair")


def test_valid_json():
    assert (
        repair_json('{"name": "John", "age": 30, "city": "New York"}')
        == '{"name": "John", "age": 30, "city": "New York"}'
    )
    assert repair_json('{"employees":["John", "Anna", "Peter"]} ') == '{"employees": ["John", "Anna", "Peter"]}'
    assert repair_json('{"key": "value:value"}') == '{"key": "value:value"}'
    assert repair_json('{"text": "The quick brown fox,"}') == '{"text": "The quick brown fox,"}'
    assert repair_json('{"text": "The quick brown fox won\'t jump"}') == '{"text": "The quick brown fox won\'t jump"}'
    assert repair_json('{"key": ""') == '{"key": ""}'
    assert repair_json('{"key1": {"key2": [1, 2, 3]}}') == '{"key1": {"key2": [1, 2, 3]}}'
    assert repair_json('{"key": 12345678901234567890}') == '{"key": 12345678901234567890}'
    assert repair_json('{"key": "value\u263a"}') == '{"key": "value\\u263a"}'
    assert repair_json('{"key": "value\\nvalue"}') == '{"key": "value\\nvalue"}'


def test_valid_json_fast_path_does_not_initialize_repair_parser(monkeypatch):
    def fail_parser_initialization(*_args, **_kwargs):
        raise AssertionError("valid JSON fast path should not initialize the repair parser")

    monkeypatch.setattr(json_repair_module, "JSONParser", fail_parser_initialization)

    assert json_repair_module.repair_json('{"key": "value"}', return_objects=True) == {"key": "value"}


def test_skip_json_loads_does_not_raw_decode_complete_json(monkeypatch):
    def fail_raw_decode(*_args, **_kwargs):
        raise AssertionError("skip_json_loads must not raw-decode complete JSON")

    monkeypatch.setattr(json_repair_module.json.JSONDecoder, "raw_decode", fail_raw_decode)

    assert repair_json('{"items": [1, 2, 3]}', return_objects=True, skip_json_loads=True) == {"items": [1, 2, 3]}


def test_prefixed_valid_json_uses_value_fast_path_when_json_loads_is_skipped(monkeypatch):
    raw = 'Here is your JSON:\n{"text": "a\\n b c, floof: a\\n ... a b (c), floof: \\n a", "id": 8}'
    expected = {"text": "a\n b c, floof: a\n ... a b (c), floof: \n a", "id": 8}
    original_try_parse = JSONParser._try_parse_valid_json_value
    value_attempts: list[int] = []

    def track_value_parse(self):
        value_attempts.append(self.index)
        return original_try_parse(self)

    monkeypatch.setattr(JSONParser, "_try_parse_valid_json_value", track_value_parse)

    assert repair_json(raw, return_objects=True) == expected
    assert value_attempts

    value_attempts.clear()

    def fail_json_loads(*_args, **_kwargs):
        raise AssertionError("skip_json_loads must not validate the whole input")

    monkeypatch.setattr(json_repair_module.json, "loads", fail_json_loads)
    assert repair_json(raw, return_objects=True, skip_json_loads=True) == expected
    assert value_attempts


def test_prefixed_valid_json_with_trailing_text_uses_value_fast_path(monkeypatch):
    def fail_parse_object(*_args, **_kwargs):
        raise AssertionError("raw decoding should avoid repair parsing")

    monkeypatch.setattr(JSONParser, "parse_object", fail_parse_object)

    raw = 'Here is your JSON:\n{"text": "literal } and ]"}\nAdditional explanation.'

    assert repair_json(raw, return_objects=True) == {"text": "literal } and ]"}


@pytest.mark.parametrize("skip_json_loads", [False, True])
def test_valid_json_with_trailing_garbage_preserves_string_content(skip_json_loads):
    raw = r"""{"tool_args": {"code": "# note\nconfig = {'type': 'object', 'properties': {}, 'additionalProperties': True}"}}}"""

    assert repair_json(raw, return_objects=True, skip_json_loads=skip_json_loads) == {
        "tool_args": {
            "code": "# note\nconfig = {'type': 'object', 'properties': {}, 'additionalProperties': True}",
        },
    }


def test_prefixed_invalid_json_falls_back_to_repair_parser():
    assert repair_json('Here is your JSON: {"key": "value', return_objects=True) == {"key": "value"}


def test_multiple_jsons():
    assert repair_json("[]{}") == "[]"
    assert repair_json('[]{"key":"value"}') == '{"key": "value"}'
    assert repair_json('{"key":"value"}[1,2,3,True]') == '[{"key": "value"}, [1, 2, 3, true]]'
    assert repair_json('{"key":"value"}, {"key":"value_after"}', return_objects=True) == [
        {"key": "value"},
        {"key": "value_after"},
    ]
    assert (
        repair_json('lorem ```json {"key":"value"} ``` ipsum ```json [1,2,3,True] ``` 42')
        == '[{"key": "value"}, [1, 2, 3, true]]'
    )
    assert repair_json('[{"key":"value"}][{"key":"value_after"}]') == '[{"key": "value_after"}]'


def test_top_level_separator_detects_pending_comma():
    parser = JSONParser(' , {"key": "value"}', None, False)

    assert parser._next_top_level_value_is_comma_separated()


def test_initial_container_trailing_content_rejects_mismatched_delimiters():
    parser = JSONParser("{]", None, False)

    assert parser._initial_container_has_non_comma_trailing_content() is False


def test_parenthesized_prose_does_not_hijack_fenced_json():
    assert (
        repair_json(
            """
         **Decision**: bla, bla (some clarification):

        ```json
        {
          "key": "value"
        }
        ```
        """
        )
        == '{"key": "value"}'
    )


def test_numbered_prose_line_does_not_hijack_fenced_json():
    assert (
        repair_json(
            """
        (1) Keep this note in the explanation.

        ```json
        {
          "key": "value"
        }
        ```
        """
        )
        == '{"key": "value"}'
    )


def test_parenthesized_tuple_still_parses_when_it_is_the_fenced_json_payload():
    assert repair_json(
        """
        Here is the tuple payload:

        ```json
        (1, 2)
        ```
        """,
        return_objects=True,
    ) == [1, 2]


def test_repair_json_with_objects():
    # Test with valid JSON strings
    assert repair_json("[]", return_objects=True) == []
    assert repair_json("{}", return_objects=True) == {}
    assert repair_json('{"key": true, "key2": false, "key3": null}', return_objects=True) == {
        "key": True,
        "key2": False,
        "key3": None,
    }
    assert repair_json('{"name": "John", "age": 30, "city": "New York"}', return_objects=True) == {
        "name": "John",
        "age": 30,
        "city": "New York",
    }
    assert repair_json("[1, 2, 3, 4]", return_objects=True) == [1, 2, 3, 4]
    assert repair_json('{"employees":["John", "Anna", "Peter"]} ', return_objects=True) == {
        "employees": ["John", "Anna", "Peter"]
    }
    assert repair_json(
        """
{
  "resourceType": "Bundle",
  "id": "1",
  "type": "collection",
  "entry": [
    {
      "resource": {
        "resourceType": "Patient",
        "id": "1",
        "name": [
          {"use": "official", "family": "Corwin", "given": ["Keisha", "Sunny"], "prefix": ["Mrs."},
          {"use": "maiden", "family": "Goodwin", "given": ["Keisha", "Sunny"], "prefix": ["Mrs."]}
        ]
      }
    }
  ]
}
""",
        return_objects=True,
    ) == {
        "resourceType": "Bundle",
        "id": "1",
        "type": "collection",
        "entry": [
            {
                "resource": {
                    "resourceType": "Patient",
                    "id": "1",
                    "name": [
                        {
                            "use": "official",
                            "family": "Corwin",
                            "given": ["Keisha", "Sunny"],
                            "prefix": ["Mrs."],
                        },
                        {
                            "use": "maiden",
                            "family": "Goodwin",
                            "given": ["Keisha", "Sunny"],
                            "prefix": ["Mrs."],
                        },
                    ],
                }
            }
        ],
    }
    assert repair_json(
        '{\n"html": "<h3 id="aaa">Waarom meer dan 200 Technical Experts - "Passie voor techniek"?</h3>"}',
        return_objects=True,
    ) == {"html": '<h3 id="aaa">Waarom meer dan 200 Technical Experts - "Passie voor techniek"?</h3>'}
    assert repair_json(
        """
        [
            {
                "foo": "Foo bar baz",
                "tag": "#foo-bar-baz"
            },
            {
                "foo": "foo bar "foobar" foo bar baz.",
                "tag": "#foo-bar-foobar"
            }
        ]
        """,
        return_objects=True,
    ) == [
        {"foo": "Foo bar baz", "tag": "#foo-bar-baz"},
        {"foo": 'foo bar "foobar" foo bar baz.', "tag": "#foo-bar-foobar"},
    ]


def test_repair_json_skip_json_loads():
    assert (
        repair_json('{"key": true, "key2": false, "key3": null}', skip_json_loads=True)
        == '{"key": true, "key2": false, "key3": null}'
    )
    assert repair_json(
        '{"key": true, "key2": false, "key3": null}',
        return_objects=True,
        skip_json_loads=True,
    ) == {"key": True, "key2": False, "key3": None}
    assert (
        repair_json('{"key": true, "key2": false, "key3": }', skip_json_loads=True)
        == '{"key": true, "key2": false, "key3": ""}'
    )
    assert loads('{"key": true, "key2": false, "key3": }', skip_json_loads=True) == {
        "key": True,
        "key2": False,
        "key3": "",
    }


def _nested_repair_payload(depth: int) -> str:
    return ("{a: [" * depth) + "1" + ("]}" * depth)


def _find_real_recursion_payload() -> str:
    depth = 1
    recursion_limit = sys.getrecursionlimit()

    while depth <= recursion_limit:
        payload = _nested_repair_payload(depth)
        try:
            JSONParser(payload, None, False).parse()
        except RecursionError:
            return payload
        depth *= 2

    pytest.skip("Could not reproduce parser recursion on this runtime.")
    raise AssertionError("pytest.skip() should raise an exception")


def test_repair_json_normalizes_real_parser_recursion_error():
    payload = _find_real_recursion_payload()

    with pytest.raises(ValueError, match="supported parser recursion depth"):
        repair_json(payload, return_objects=True)


def test_ensure_ascii():
    assert repair_json("{'test_中国人_ascii':'统一码'}", ensure_ascii=False) == '{"test_中国人_ascii": "统一码"}'


def test_stream_stable():
    # default: stream_stable = False
    # When the json to be repaired is the accumulation of streaming json at a certain moment.
    # The default repair result is unstable.
    assert repair_json('{"key": "val\\', stream_stable=False) == '{"key": "val\\\\"}'
    assert repair_json('{"key": "val\\n', stream_stable=False) == '{"key": "val"}'
    assert (
        repair_json('{"key": "val\\n123,`key2:value2', stream_stable=False) == '{"key": "val\\n123", "key2": "value2"}'
    )
    assert repair_json('{"key": "val\\n123,`key2:value2`"}', stream_stable=True) == '{"key": "val\\n123,`key2:value2`"}'
    # stream_stable = True
    assert repair_json('{"key": "val\\', stream_stable=True) == '{"key": "val"}'
    assert repair_json('{"key": "val\\n', stream_stable=True) == '{"key": "val\\n"}'
    assert repair_json('{"key": "val\\n123,`key2:value2', stream_stable=True) == '{"key": "val\\n123,`key2:value2"}'
    assert repair_json('{"key": "val\\n123,`key2:value2`"}', stream_stable=True) == '{"key": "val\\n123,`key2:value2`"}'


def test_logging():
    assert repair_json("{}", logging=True) == ({}, [])
    assert repair_json('{"key": "value}', logging=True) == (
        {"key": "value"},
        [
            {
                "context": 'y": "value}',
                "text": "While parsing a string missing the left delimiter in object value "
                "context, we found a , or } and we couldn't determine that a right "
                "delimiter was present. Stopping here",
            },
            {
                "context": 'y": "value}',
                "text": "While parsing a string, we missed the closing quote, ignoring",
            },
        ],
    )

```

### `tests/test_parse_array.py`

```py
from src.json_repair.json_parser import JSONParser
from src.json_repair.json_repair import repair_json


def test_parse_array():
    assert repair_json("[]", return_objects=True) == []
    assert repair_json("[1, 2, 3, 4]", return_objects=True) == [1, 2, 3, 4]
    assert repair_json("[", return_objects=True) == []
    assert repair_json("[[1\n\n]") == "[[1]]"


def test_parse_array_edge_cases():
    assert repair_json("[{]") == "[]"
    assert repair_json("[") == "[]"
    assert repair_json('["') == "[]"
    assert repair_json("]") == ""
    assert repair_json("[1, 2, 3,") == "[1, 2, 3]"
    assert repair_json("[1, 2, 3, ...]") == "[1, 2, 3]"
    assert repair_json("[1, 2, ... , 3]") == "[1, 2, 3]"
    assert repair_json("[1, 2, '...', 3]") == '[1, 2, "...", 3]'
    assert repair_json("[true, false, null, ...]") == "[true, false, null]"
    assert repair_json('["a" "b" "c" 1') == '["a", "b", "c", 1]'
    assert repair_json('{"employees":["John", "Anna",') == '{"employees": ["John", "Anna"]}'
    assert repair_json('{"employees":["John", "Anna", "Peter') == '{"employees": ["John", "Anna", "Peter"]}'
    assert repair_json('{"key1": {"key2": [1, 2, 3') == '{"key1": {"key2": [1, 2, 3]}}'
    assert repair_json('{"key": ["value]}') == '{"key": ["value"]}'
    assert repair_json('["lorem "ipsum" sic"]') == '["lorem \\"ipsum\\" sic"]'
    assert (
        repair_json('{"key1": ["value1", "value2"}, "key2": ["value3", "value4"]}')
        == '{"key1": ["value1", "value2"], "key2": ["value3", "value4"]}'
    )
    assert (
        repair_json(
            '{"headers": ["A", "B", "C"], "rows": [["r1a", "r1b", "r1c"], ["r2a", "r2b", "r2c"], '
            '"r3a", "r3b", "r3c"], ["r4a", "r4b", "r4c"], ["r5a", "r5b", "r5c"]]}'
        )
        == '{"headers": ["A", "B", "C"], "rows": [["r1a", "r1b", "r1c"], ["r2a", "r2b", "r2c"], '
        '["r3a", "r3b", "r3c"], ["r4a", "r4b", "r4c"], ["r5a", "r5b", "r5c"]]}'
    )
    assert repair_json('{"key": ["value" "value1" "value2"]}') == '{"key": ["value", "value1", "value2"]}'
    assert (
        repair_json('{"key": ["lorem "ipsum" dolor "sit" amet, "consectetur" ", "lorem "ipsum" dolor", "lorem"]}')
        == '{"key": ["lorem \\"ipsum\\" dolor \\"sit\\" amet, \\"consectetur\\" ", "lorem \\"ipsum\\" dolor", "lorem"]}'
    )
    assert repair_json('{"k"e"y": "value"}') == '{"k\\"e\\"y": "value"}'
    assert repair_json('["key":"value"}]') == '[{"key": "value"}]'
    assert repair_json('["key":"value"]') == '[{"key": "value"}]'
    assert repair_json('[ "key":"value"]') == '[{"key": "value"}]'
    assert repair_json('[{"key": "value", "key') == '[{"key": "value"}, ["key"]]'
    assert repair_json("{'key1', 'key2'}") == '["key1", "key2"]'


def test_parse_array_closes_before_object_member_after_scalar_items():
    raw = '{"outer": ["a", "b", "next": "value"}'

    assert repair_json(raw, return_objects=True) == {
        "outer": ["a", "b"],
        "next": "value",
    }


def test_parse_array_contextually_closes_in_strict_mode():
    assert repair_json('{"outer": ["a", "b", "next": "value"}', return_objects=True, strict=True) == {
        "outer": ["a", "b"],
        "next": "value",
    }


def test_parse_array_python_tuple_literals():
    assert repair_json('("a", "b", "c")', return_objects=True) == ["a", "b", "c"]
    assert repair_json("((1, 2), (3, 4))", return_objects=True) == [[1, 2], [3, 4]]
    assert repair_json('{"coords": (1, 2), "ok": true}', return_objects=True) == {"coords": [1, 2], "ok": True}
    assert repair_json('{"empty": ()}', return_objects=True) == {"empty": []}


def test_parse_array_python_tuple_literals_accept_boolean_and_null_values():
    assert repair_json("(true, false, null)", return_objects=True, skip_json_loads=True) == [True, False, None]
    assert repair_json("(True, False, None)", return_objects=True, skip_json_loads=True) == [True, False, None]
    assert repair_json('{"coords": (True, None)}', return_objects=True, skip_json_loads=True) == {
        "coords": [True, None]
    }


def test_parse_array_parenthesized_scalar_keeps_scalar_shape():
    assert repair_json("(1)", return_objects=True) == 1
    assert repair_json('("x")', return_objects=True) == "x"
    assert repair_json('{"scalar_group": (1)}', return_objects=True) == {"scalar_group": 1}
    assert repair_json('{"string_group": ("x")}', return_objects=True) == {"string_group": "x"}


def test_parse_array_mismatched_parenthesis_still_logs_missing_bracket():
    repaired, logs = repair_json("[1, 2)", return_objects=True, logging=True)

    assert repaired == [1, 2]
    assert any("closing ]" in entry["text"] for entry in logs)


def test_parenthesized_tuple_classifier_handles_nested_delimiters_and_missing_close():
    parser = JSONParser('({"text": "a\\\\b", "items": [1]})', None, False)
    assert parser.parenthesized_is_explicit_tuple() is False

    parser = JSONParser("(1", None, False)
    assert parser.parenthesized_is_explicit_tuple() is False


def test_top_level_parenthesized_value_gate_rejects_prose_and_accepts_standalone_jsonish_values():
    parser = JSONParser("(", None, False)
    assert parser.top_level_parenthesized_can_start_value() is False

    parser = JSONParser('(note)\n{"key": 1}', None, False)
    assert parser.top_level_parenthesized_can_start_value() is False

    parser = JSONParser("(1", None, False)
    assert parser.top_level_parenthesized_can_start_value() is True

    parser = JSONParser('(["a\\\\b"], {"k": 1})\n', None, False)
    assert parser.top_level_parenthesized_can_start_value() is True


def test_parse_array_missing_quotes():
    assert repair_json('["value1" value2", "value3"]') == '["value1", "value2", "value3"]'
    assert (
        repair_json('{"bad_one":["Lorem Ipsum", "consectetur" comment" ], "good_one":[ "elit", "sed", "tempor"]}')
        == '{"bad_one": ["Lorem Ipsum", "consectetur", "comment"], "good_one": ["elit", "sed", "tempor"]}'
    )
    assert (
        repair_json('{"bad_one": ["Lorem Ipsum","consectetur" comment],"good_one": ["elit","sed","tempor"]}')
        == '{"bad_one": ["Lorem Ipsum", "consectetur", "comment"], "good_one": ["elit", "sed", "tempor"]}'
    )

```

### `tests/test_parse_comment.py`

```py
from src.json_repair.json_repair import repair_json


def test_parse_comment():
    assert repair_json("/") == ""
    assert repair_json('/* comment */ {"key": "value"}')
    assert repair_json('{ "key": { "key2": "value2" // comment }, "key3": "value3" }') == '{"key": {"key2": "value2"}}'
    assert (
        repair_json('{ "key": { "key2": "value2" // comment\n}, "key3": "value3" }')
        == '{"key": {"key2": "value2"}, "key3": "value3"}'
    )
    assert (
        repair_json('{ "key": { "key2": "value2" # comment }, "key3": "value3" }')
        == '{"key": {"key2": "value2"}, "key3": "value3"}'
    )
    assert (
        repair_json('{ "key": { "key2": "value2" /* comment */ }, "key3": "value3" }')
        == '{"key": {"key2": "value2"}, "key3": "value3"}'
    )
    assert repair_json('[ "value", /* comment */ "value2" ]') == '["value", "value2"]'
    assert repair_json('{ "key": "value" /* comment') == '{"key": "value"}'


def test_line_comment_brackets_do_not_trigger_empty_object_array_fallback():
    repaired, logs = repair_json("{\n// comment ]\n}", return_objects=True, skip_json_loads=True, logging=True)

    assert repaired == {}
    assert all("try to parse this as an array instead" not in entry["text"] for entry in logs)


def test_block_comment_brackets_do_not_trigger_empty_object_array_fallback():
    repaired, logs = repair_json("{/* comment ] */}", return_objects=True, skip_json_loads=True, logging=True)

    assert repaired == {}
    assert all("try to parse this as an array instead" not in entry["text"] for entry in logs)


def test_line_comment_brackets_do_not_close_array_items():
    raw = """
    {
        "Changes": [
            //object a
            {
                "Action": "1"
            },
            //object b ]
            {
                "Action": "2"
            },
            //object c ]
            {
                "Action": "3"
            }
        ]
    }
    """

    assert repair_json(raw, return_objects=True, skip_json_loads=True) == {
        "Changes": [{"Action": "1"}, {"Action": "2"}, {"Action": "3"}]
    }


def test_parse_many_top_level_comments_without_recursion_error():
    comment_count = 600
    raw = ("# comment\n" * comment_count) + '{"key": "value"}'

    repaired, logs = repair_json(raw, return_objects=True, skip_json_loads=True, logging=True)

    assert repaired == {"key": "value"}
    assert len(logs) == comment_count
    assert all(log["text"] == "Found line comment: # comment, ignoring" for log in logs)

```

### `tests/test_parse_number.py`

```py
from src.json_repair.json_repair import repair_json


def test_parse_number():
    assert repair_json("1", return_objects=True) == 1
    assert repair_json("1.2", return_objects=True) == 1.2
    assert repair_json('{"value": 82_461_110}', return_objects=True) == {"value": 82461110}
    assert repair_json('{"value": 1_234.5_6}', return_objects=True) == {"value": 1234.56}


def test_parse_number_edge_cases():
    assert (
        repair_json(' - { "test_key": ["test_value", "test_value2"] }') == '{"test_key": ["test_value", "test_value2"]}'
    )
    assert repair_json('{"key": 1/3}') == '{"key": "1/3"}'
    assert repair_json('{"key": .25}') == '{"key": 0.25}'
    assert repair_json('{"here": "now", "key": 1/3, "foo": "bar"}') == '{"here": "now", "key": "1/3", "foo": "bar"}'
    assert repair_json('{"key": 12345/67890}') == '{"key": "12345/67890"}'
    assert repair_json("[105,12") == "[105, 12]"
    assert repair_json('{"key", 105,12,') == '{"key": "105,12"}'
    assert repair_json('{"key": 1/3, "foo": "bar"}') == '{"key": "1/3", "foo": "bar"}'
    assert repair_json('{"key": 10-20}') == '{"key": "10-20"}'
    assert repair_json('{"key": 1.1.1}') == '{"key": "1.1.1"}'
    assert repair_json("[- ") == "[]"
    assert repair_json('{"key": 1. }') == '{"key": 1.0}'
    assert repair_json('{"key": 1e10 }') == '{"key": 10000000000.0}'
    assert repair_json('{"key": 1e }') == '{"key": 1}'
    assert repair_json('{"key": 1notanumber }') == '{"key": "1notanumber"}'
    assert (
        repair_json('{"rowId": 57eeeeb1-450b-482c-81b9-4be77e95dee2}')
        == '{"rowId": "57eeeeb1-450b-482c-81b9-4be77e95dee2"}'
    )
    assert repair_json("[1, 2notanumber]") == '[1, "2notanumber"]'

```

### `tests/test_parse_object.py`

```py
from src.json_repair.json_repair import repair_json


def test_parse_object():
    assert repair_json("{}", return_objects=True) == {}
    assert repair_json('{ "key": "value", "key2": 1, "key3": True }', return_objects=True) == {
        "key": "value",
        "key2": 1,
        "key3": True,
    }
    assert repair_json("{", return_objects=True) == {}
    assert repair_json('{ "key": value, "key2": 1 "key3": null }', return_objects=True) == {
        "key": "value",
        "key2": 1,
        "key3": None,
    }
    assert repair_json("   {  }   ") == "{}"
    assert repair_json("{") == "{}"
    assert repair_json("}") == ""
    assert repair_json('{"') == "{}"


def test_parse_object_edge_cases():
    assert repair_json("{foo: [}") == '{"foo": []}'
    assert repair_json('{"": "value"') == '{"": "value"}'
    assert repair_json('{"key": "v"alue"}') == '{"key": "v\\"alue\\""}'
    assert repair_json('{"value_1": true, COMMENT "value_2": "data"}') == '{"value_1": true, "value_2": "data"}'
    assert (
        repair_json('{"value_1": true, SHOULD_NOT_EXIST "value_2": "data" AAAA }')
        == '{"value_1": true, "value_2": "data"}'
    )
    assert repair_json('{"" : true, "key2": "value2"}') == '{"": true, "key2": "value2"}'
    assert (
        repair_json("""{""answer"":[{""traits"":''Female aged 60+'',""answer1"":""5""}]}""")
        == '{"answer": [{"traits": "Female aged 60+", "answer1": "5"}]}'
    )
    assert (
        repair_json('{ "words": abcdef", "numbers": 12345", "words2": ghijkl" }')
        == '{"words": "abcdef", "numbers": 12345, "words2": "ghijkl"}'
    )
    assert (
        repair_json("""{"number": 1,"reason": "According...""ans": "YES"}""")
        == '{"number": 1, "reason": "According...", "ans": "YES"}'
    )
    assert repair_json("""{ "a" : "{ b": {} }" }""") == '{"a": "{ b"}'
    assert repair_json("""{"b": "xxxxx" true}""") == '{"b": "xxxxx"}'
    assert repair_json('{"key": "Lorem "ipsum" s,"}') == '{"key": "Lorem \\"ipsum\\" s,"}'
    assert repair_json('{"lorem": ipsum, sic, datum.",}') == '{"lorem": "ipsum, sic, datum."}'
    assert (
        repair_json('{"lorem": sic tamet. "ipsum": sic tamet, quick brown fox. "sic": ipsum}')
        == '{"lorem": "sic tamet.", "ipsum": "sic tamet", "sic": "ipsum"}'
    )
    assert (
        repair_json('{"lorem_ipsum": "sic tamet, quick brown fox. }')
        == '{"lorem_ipsum": "sic tamet, quick brown fox."}'
    )
    assert repair_json('{"key":value, " key2":"value2" }') == '{"key": "value", " key2": "value2"}'
    assert repair_json('{"key":value "key2":"value2" }') == '{"key": "value", "key2": "value2"}'
    assert (
        repair_json("{'text': 'words{words in brackets}more words'}")
        == '{"text": "words{words in brackets}more words"}'
    )
    assert repair_json("{text:words{words in brackets}}") == '{"text": "words{words in brackets}"}'
    assert repair_json("{text:words{words in brackets}m}") == '{"text": "words{words in brackets}m"}'
    assert repair_json('{"key": "value, value2"```') == '{"key": "value, value2"}'
    assert repair_json('{"key": "value}```') == '{"key": "value"}'
    assert repair_json("{key:value,key2:value2}") == '{"key": "value", "key2": "value2"}'
    assert repair_json('{"key:"value"}') == '{"key": "value"}'
    assert repair_json('{"key:value}') == '{"key": "value"}'
    assert (
        repair_json('[{"lorem": {"ipsum": "sic"}, """" "lorem": {"ipsum": "sic"}]')
        == '[{"lorem": {"ipsum": "sic"}}, {"lorem": {"ipsum": "sic"}}]'
    )
    assert (
        repair_json('{ "key": ["arrayvalue"], ["arrayvalue1"], ["arrayvalue2"], "key3": "value3" }')
        == '{"key": ["arrayvalue", "arrayvalue1", "arrayvalue2"], "key3": "value3"}'
    )
    assert (
        repair_json('{ "key": [[1, 2, 3], "a", "b"], [[4, 5, 6], [7, 8, 9]] }')
        == '{"key": [[1, 2, 3], "a", "b", [4, 5, 6], [7, 8, 9]]}'
    )
    assert (
        repair_json('{ "key": ["arrayvalue"], "key3": "value3", ["arrayvalue1"] }')
        == '{"key": ["arrayvalue"], "key3": "value3", "arrayvalue1": ""}'
    )
    assert (
        repair_json('{"key": "{\\\\"key\\\\\\":[\\"value\\\\\\"],\\"key2\\":"value2"}"}')
        == '{"key": "{\\"key\\":[\\"value\\"],\\"key2\\":\\"value2\\"}"}'
    )
    assert repair_json('{"key": , "key2": "value2"}') == '{"key": "", "key2": "value2"}'
    assert (
        repair_json('{"array":[{"key": "value"], "key2": "value2"}')
        == '{"array": [{"key": "value"}], "key2": "value2"}'
    )
    assert repair_json('[{"key":"value"}},{"key":"value"}]') == '[{"key": "value"}, {"key": "value"}]'
    assert (
        repair_json("{'key': ['a':{'duplicated_key': 'duplicated_value', 'duplicated_key': 'duplicated_value'}]}")
        == '{"key": [{"a": {"duplicated_key": "duplicated_value"}}]}'
    )
    assert repair_json('[{"b":"v2","b":"v2"}]', return_objects=True, skip_json_loads=True) == [{"b": "v2"}]
    assert repair_json("{'item1', 'item2', 'item3'}", return_objects=True, skip_json_loads=True) == [
        "item1",
        "item2",
        "item3",
    ]


def test_parse_object_preserves_backslash_escaped_keys():
    raw = '{\\"key\\": \\"value\\"}'

    repaired, logs = repair_json(raw, return_objects=True, skip_json_loads=True, logging=True)

    assert repaired == {"key": "value"}
    assert any("reparsing it as an object" in entry["text"] for entry in logs)
    assert repair_json(raw, skip_json_loads=True) == '{"key": "value"}'


def test_parse_object_empty_object_classifier_keeps_objectish_inputs():
    repaired, logs = repair_json("{:}", return_objects=True, skip_json_loads=True, logging=True)

    assert repaired == {}
    assert any("object-style separator" in entry["text"] for entry in logs)

    repaired, logs = repair_json("{   }", return_objects=True, skip_json_loads=True, logging=True)

    assert repaired == {}
    assert logs == []


def test_parse_object_empty_object_classifier_keeps_array_fallback_for_backslash_noise():
    repaired, logs = repair_json(r"{foo\bar}", return_objects=True, skip_json_loads=True, logging=True)

    assert isinstance(repaired, list)
    assert any("try to parse this as an array instead" in entry["text"] for entry in logs)


def test_parse_object_empty_object_array_fallback_preserves_legacy_key_context():
    assert repair_json("[{5}s ", return_objects=True, skip_json_loads=True) == [[5]]


def test_parse_object_merge_at_the_end():
    assert repair_json('{"key": "value"}, "key2": "value2"}') == '{"key": "value", "key2": "value2"}'
    assert repair_json('{"key": "value"}, "key2": }') == '{"key": "value", "key2": ""}'
    assert repair_json('{"key": "value"}, []') == '{"key": "value"}'
    assert repair_json('{"key": "value"}, ["abc"]') == '[{"key": "value"}, ["abc"]]'
    assert repair_json('{"key": "value"}, {}') == '{"key": "value"}'
    assert repair_json('{"key": "value"}, "" : "value2"}') == '{"key": "value", "": "value2"}'
    assert repair_json('{"key": "value"}, "key2" "value2"}') == '{"key": "value", "key2": "value2"}'
    assert (
        repair_json('{"key1": "value1"}, "key2": "value2", "key3": "value3"}')
        == '{"key1": "value1", "key2": "value2", "key3": "value3"}'
    )

```

### `tests/test_parse_string.py`

```py
from io import StringIO

import pytest

from src.json_repair.json_parser import JSONParser
from src.json_repair.json_repair import repair_json
from src.json_repair.parse_string import (
    StringParseState,
    _brace_before_code_fence_belongs_to_string,
    _quoted_object_member_follows,
    _scan_string_body,
    _skip_inline_container,
    _starts_nested_inline_container,
    _try_parse_simple_quoted_string,
)
from src.json_repair.parse_string_helpers.object_value_context import update_inline_container_stack
from src.json_repair.utils.json_context import ContextValues
from src.json_repair.utils.string_file_wrapper import StringFileWrapper


def _assert_object_repairs(raw: str, expected: dict) -> None:
    assert repair_json(raw, return_objects=True) == expected
    assert repair_json(raw, skip_json_loads=True, return_objects=True) == expected


class CountingParser(JSONParser):
    def __init__(self, json_str: str) -> None:
        super().__init__(json_str, None, False)
        self.skip_to_character_calls = 0

    def skip_to_character(self, character: str | list[str], idx: int = 0) -> int:
        self.skip_to_character_calls += 1
        return super().skip_to_character(character, idx)


def test_parse_string():
    assert repair_json('"') == ""
    assert repair_json("\n") == ""
    assert repair_json(" ") == ""
    assert repair_json("string") == ""
    assert repair_json("stringbeforeobject {}") == "{}"


def test_missing_and_mixed_quotes():
    assert (
        repair_json("{'key': 'string', 'key2': false, \"key3\": null, \"key4\": unquoted}")
        == '{"key": "string", "key2": false, "key3": null, "key4": "unquoted"}'
    )
    assert (
        repair_json('{"name": "John", "age": 30, "city": "New York')
        == '{"name": "John", "age": 30, "city": "New York"}'
    )
    assert (
        repair_json('{"name": "John", "age": 30, city: "New York"}')
        == '{"name": "John", "age": 30, "city": "New York"}'
    )
    assert (
        repair_json('{"name": "John", "age": 30, "city": New York}')
        == '{"name": "John", "age": 30, "city": "New York"}'
    )
    assert (
        repair_json('{"name": John, "age": 30, "city": "New York"}')
        == '{"name": "John", "age": 30, "city": "New York"}'
    )
    assert repair_json('{“slanted_delimiter”: "value"}') == '{"slanted_delimiter": "value"}'
    assert repair_json('{"name": "John", "age": 30, "city": "New') == '{"name": "John", "age": 30, "city": "New"}'
    assert (
        repair_json('{"name": "John", "age": 30, "city": "New York, "gender": "male"}')
        == '{"name": "John", "age": 30, "city": "New York", "gender": "male"}'
    )

    assert (
        repair_json('[{"key": "value", COMMENT "notes": "lorem "ipsum", sic." }]')
        == '[{"key": "value", "notes": "lorem \\"ipsum\\", sic."}]'
    )
    assert repair_json('{"key": ""value"}') == '{"key": "value"}'
    assert repair_json('{"key": "value", 5: "value"}') == '{"key": "value", "5": "value"}'
    assert repair_json('{"foo": "\\"bar\\""') == '{"foo": "\\"bar\\""}'
    assert repair_json('{"" key":"val"') == '{" key": "val"}'
    assert repair_json('{"key": value "key2" : "value2" ') == '{"key": "value", "key2": "value2"}'
    assert (
        repair_json('{"key": "lorem ipsum ... "sic " tamet. ...}') == '{"key": "lorem ipsum ... \\"sic \\" tamet. ..."}'
    )
    assert repair_json('{"key": value , }') == '{"key": "value"}'
    assert (
        repair_json('{"comment": "lorem, "ipsum" sic "tamet". To improve"}')
        == '{"comment": "lorem, \\"ipsum\\" sic \\"tamet\\". To improve"}'
    )
    assert repair_json('{"key": "v"alu"e"} key:') == '{"key": "v\\"alu\\"e"}'
    assert repair_json('{"key": "v"alue", "key2": "value2"}') == '{"key": "v\\"alue", "key2": "value2"}'
    assert repair_json('[{"key": "v"alu,e", "key2": "value2"}]') == '[{"key": "v\\"alu,e", "key2": "value2"}]'


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ('{"title": ""hello" world"}', {"title": '"hello" world'}),
        ('{"title": ""hello" world", "b": "y"}', {"title": '"hello" world', "b": "y"}),
    ],
)
def test_parse_string_preserves_leading_quoted_phrase(raw, expected, strict):
    assert repair_json(raw, return_objects=True, strict=strict) == expected


@pytest.mark.parametrize("strict", [False, True])
def test_parse_string_removes_redundant_leading_quote(strict):
    assert repair_json('{"key": ""value"}', return_objects=True, strict=strict) == {"key": "value"}


def test_object_value_comma_without_future_delimiter_scans_once():
    parser = CountingParser('"value,fragment,fragment,fragment')
    parser.context.set(ContextValues.OBJECT_VALUE)

    assert parser.parse_string() == "value,fragment,fragment,fragment"
    assert parser.skip_to_character_calls == 1


def test_object_value_bare_key_prose_scans_once():
    raw = '"value\\n' + (", floof: prose" * 100) + '"'
    parser = CountingParser(raw)
    parser.context.set(ContextValues.OBJECT_VALUE)

    assert parser.parse_string() == "value\n" + (", floof: prose" * 100)
    assert parser.skip_to_character_calls == 3


def test_parse_string_keeps_colon_prose_inside_wrapped_valid_json():
    raw = r"""Here's your JSON:
{
  "stuff": [
    {
      "a": "foo",
      "blist": [
        {
          "text": "a\n b c, floof: a\n ... a b (c), floof: \n a",
          "id": 8
        }
      ]
    }
  ]
}
"""
    expected = {
        "stuff": [
            {
                "a": "foo",
                "blist": [{"text": "a\n b c, floof: a\n ... a b (c), floof: \n a", "id": 8}],
            }
        ]
    }

    _assert_object_repairs(raw, expected)
    repaired, logs = repair_json(raw, return_objects=True, logging=True)
    assert repaired == expected
    assert not any("comma that starts the next object member" in log["text"] for log in logs)


def test_parse_string_keeps_code_like_content_inside_valid_json():
    raw = r'{"command":"x\nrollback: (registry: Registry, snapshot: EntitySnapshot) => void;"}'
    expected = {"command": "x\nrollback: (registry: Registry, snapshot: EntitySnapshot) => void;"}

    _assert_object_repairs(raw, expected)
    repaired, logs = repair_json(raw, skip_json_loads=True, return_objects=True, logging=True)
    assert repaired == expected
    assert not any("comma that starts the next object member" in log["text"] for log in logs)


def test_parse_string_keeps_pseudo_object_code_inside_valid_json():
    raw = r'{"command":"x\nrollback: {registry: Registry, snapshot: EntitySnapshot}"}'
    expected = {"command": "x\nrollback: {registry: Registry, snapshot: EntitySnapshot}"}

    _assert_object_repairs(raw, expected)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ('{"a": "first, b: "second"}', {"a": "first", "b": "second"}),
        ('{"a": "first, b: 1}', {"a": "first", "b": 1}),
        ('{"a": "first, b: true}', {"a": "first", "b": True}),
        ('{"a": "first, b: [1]}', {"a": "first", "b": [1]}),
        ('{"a": "first, b: prose}', {"a": "first", "b": "prose"}),
    ],
)
def test_parse_string_keeps_bare_member_recovery_for_explicit_and_unclosed_values(raw, expected):
    assert repair_json(raw, skip_json_loads=True, return_objects=True) == expected


def test_escaping():
    assert repair_json("'\"'") == ""
    assert repair_json('{"key": \'string"\n\t\\le\'') == '{"key": "string\\"\\n\\t\\\\le"}'
    assert (
        repair_json(
            r'{"real_content": "Some string: Some other string \t Some string <a href=\"https://domain.com\">Some link</a>"'
        )
        == r'{"real_content": "Some string: Some other string \t Some string <a href=\"https://domain.com\">Some link</a>"}'
    )
    assert repair_json('{"key_1\n": "value"}') == '{"key_1": "value"}'
    assert repair_json('{"key\t_": "value"}') == '{"key\\t_": "value"}'
    assert repair_json("{\"key\": '\u0076\u0061\u006c\u0075\u0065'}") == '{"key": "value"}'
    assert repair_json('{"key": "\\u0076\\u0061\\u006C\\u0075\\u0065"}', skip_json_loads=True) == '{"key": "value"}'
    assert repair_json("""{"key": "valu\\'e"}""") == """{"key": "valu'e"}"""
    assert repair_json('{\'key\': "{\\"key\\": 1, \\"key2\\": 1}"}') == '{"key": "{\\"key\\": 1, \\"key2\\": 1}"}'


def test_markdown():
    assert (
        repair_json('{ "content": "[LINK]("https://google.com")" }')
        == '{"content": "[LINK](\\"https://google.com\\")"}'
    )
    assert repair_json('{ "content": "[LINK](" }') == '{"content": "[LINK]("}'
    assert repair_json('{ "content": "[LINK](", "key": true }') == '{"content": "[LINK](", "key": true}'


@pytest.mark.parametrize(
    "fenced",
    [False, True],
)
def test_parse_string_keeps_bare_quotes_inside_regex_character_classes(fenced):
    raw = """{
        "results": [
            {"regex": "^\\s*path\\(\\s*['\"]([^'\"]+)['\"]\\s*,"},
            {"regex": "^\\s*re_path\\(\\s*[^'\"]+['\"]\\s*,"}
        ]
    }"""
    if fenced:
        raw = f"```json\n{raw}\n```"

    assert repair_json(raw, return_objects=True, skip_json_loads=True) == {
        "results": [
            {"regex": r"""^\s*path\(\s*['"]([^'"]+)['"]\s*,"""},
            {"regex": r"""^\s*re_path\(\s*[^'"]+['"]\s*,"""},
        ]
    }


def test_parse_string_still_closes_regular_object_members_after_quoted_values():
    assert repair_json('{"first": "value", "second": "next"}', return_objects=True, skip_json_loads=True) == {
        "first": "value",
        "second": "next",
    }


def test_leading_trailing_characters():
    assert repair_json('````{ "key": "value" }```') == '{"key": "value"}'
    assert repair_json("""{    "a": "",    "b": [ { "c": 1} ] \n}```""") == '{"a": "", "b": [{"c": 1}]}'
    assert (
        repair_json("Based on the information extracted, here is the filled JSON output: ```json { 'a': 'b' } ```")
        == '{"a": "b"}'
    )
    assert (
        repair_json("""
                       The next 64 elements are:
                       ```json
                       { "key": "value" }
                       ```""")
        == '{"key": "value"}'
    )


def test_fenced_json_wrapper_matches_plain_for_duplicate_keys():
    fenced = """
    ```json
    {
    "k": [
    {
    "b":"v2",
    "b":"v2"
    }
    ]
    }
    ```
    """
    plain = """
    {
    "k": [
    {
    "b":"v2",
    "b":"v2"
    }
    ]
    }
    """
    assert repair_json(fenced, return_objects=True) == repair_json(plain, return_objects=True)


def test_string_json_llm_block():
    assert repair_json('{"key": "``"') == '{"key": "``"}'
    assert repair_json('{"key": "```json"') == '{"key": "```json"}'
    assert (
        repair_json('{"key": "```json {"key": [{"key1": 1},{"key2": 2}]}```"}')
        == '{"key": {"key": [{"key1": 1}, {"key2": 2}]}}'
    )
    assert repair_json('{"response": "```json{}"') == '{"response": "```json{}"}'


def test_parse_string_logs_invalid_code_fences():
    repaired, logs = repair_json('{"key": "```json nope\\n"}', skip_json_loads=True, return_objects=True, logging=True)
    assert repaired == {"key": "```json nope"}
    assert any("did not enclose valid JSON" in log["text"] for log in logs)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ('{\n"a": "\n```{}```\n",\n"b": "x",\n}', {"a": "\n```{}```", "b": "x"}),
        ('{\n"a": "\n```{}```\n"\n",\n"b": "x",\n}', {"a": '\n```{}```\n"', "b": "x"}),
        ('{\n"a": "\n```{}```\n"\n",\n\'b\': "x",\n}', {"a": '\n```{}```\n"', "b": "x"}),
        ('{\n"a": "\n```{}```\n"\n", // c\n"b": "x",\n}', {"a": '\n```{}```\n"', "b": "x"}),
        ('{\n"a": "\n```{}```\n"\n",\n b: "x",\n}', {"a": '\n```{}```\n"', "b": "x"}),
        ('{"a":"```}```"a","b":"x"}', {"a": '```}```"a', "b": "x"}),
        ('{"a":"x}``` [1,2]\n","b":"y"}', {"a": "x}``` [1,2]", "b": "y"}),
        ('{"a":"x}``` [http://x]\n","b":"y"}', {"a": "x}``` [http://x]", "b": "y"}),
        ('{"a":"x}``` [foo[bar]\n","b":"y"}', {"a": "x}``` [foo[bar]", "b": "y"}),
        ('{"a":"x}``` [{\n","b":"y"}', {"a": "x}``` [{", "b": "y"}),
        ('{"a":"x}``` [foo, [bar]\n","b":"y"}', {"a": "x}``` [foo, [bar]", "b": "y"}),
        ('{"a":"x}``` [1,"z"]\n","b":"y"}', {"a": 'x}``` [1,"z"]', "b": "y"}),
        ('{"a":"x}``` [1, [2]]\n","b":"y"}', {"a": "x}``` [1, [2]]", "b": "y"}),
        ('{"a":"x}``` [1,[2],k:v]\n","b":"y"}', {"a": "x}``` [1,[2],k:v]", "b": "y"}),
        ('{"a":"x}``` (1,(2),k:v)\n","b":"y"}', {"a": "x}``` (1,(2),k:v)", "b": "y"}),
        ('{"a":"x}``` [1,2],\n","b":"y"}', {"a": "x}``` [1,2],", "b": "y"}),
        ('{"a":"x}``` // c\n [1,2]\n","b":"y"}', {"a": "x}``` // c\n [1,2]", "b": "y"}),
        ('{"a":"x}``` // c\n [1,2],\n","b":"y"}', {"a": "x}``` // c\n [1,2],", "b": "y"}),
        (
            '{\n"a": "\n```c\nint main() {\n}\n```\nImplementation: "xxx", xxx\n",\n"b": "x",\n}',
            {"a": '\n```c\nint main() {\n}\n```\nImplementation: "xxx", xxx', "b": "x"},
        ),
    ],
    ids=[
        "multiline-object-value",
        "stray-quote-line",
        "single-quoted-next-key",
        "comment-prefixed-next-key",
        "bare-next-key",
        "inline-quoted-prose",
        "inline-array-literal",
        "url-like-inline-array",
        "unmatched-inner-delimiter",
        "unbalanced-inline-array-like-prose",
        "unmatched-inner-delimiter-after-comma",
        "quoted-item-inline-array",
        "balanced-nested-inline-array",
        "nested-numeric-inline-array-with-bare-key-like-prose",
        "nested-numeric-parenthesized-value-with-bare-key-like-prose",
        "inline-array-with-trailing-comma",
        "comment-prefixed-inline-array",
        "comment-prefixed-inline-array-with-trailing-comma",
        "fenced-code-block-before-inline-quoted-prose",
    ],
)
def test_parse_string_keeps_literal_fenced_snippet_cases(raw, expected):
    _assert_object_repairs(raw, expected)


def test_parse_string_stray_quote_line_before_trailing_comma_drops_stray_quote():
    _assert_object_repairs('{"a": "hello\n"\n",}', {"a": "hello"})


def test_parse_string_stray_quote_line_before_trailing_comma_at_eof_drops_stray_quote():
    _assert_object_repairs('{"a": "hello\n"\n",', {"a": "hello"})


def test_parse_string_keeps_multiline_curly_quoted_prose_after_comma():
    _assert_object_repairs('{"x": "a,\n “term”: explanation", "y": 2}', {"x": "a,\n “term”: explanation", "y": 2})


def test_parse_string_keeps_low_smart_quote_span_closed_by_ascii_quote():
    _assert_object_repairs(
        '{"text": "despre „autocritică" și autocompasiune"}',
        {"text": 'despre „autocritică" și autocompasiune'},
    )


def test_parse_string_keeps_low_smart_quote_span_closed_by_unicode_quote():
    _assert_object_repairs(
        '{"text": "despre „autocritică” și autocompasiune"}',
        {"text": "despre „autocritică” și autocompasiune"},
    )


def test_parse_string_keeps_low_smart_quote_span_closed_by_escaped_ascii_quote():
    _assert_object_repairs(
        '{"text": "aplicație „sham\\"), a făcut"}',
        {"text": 'aplicație „sham"), a făcut'},
    )


def test_parse_string_escaped_low_smart_quote_does_not_open_inner_span():
    _assert_object_repairs(
        '{"text": "a \\„ b", "y": 1}',
        {"text": "a „ b", "y": 1},
    )


def test_parse_boolean_or_null():
    assert repair_json("True", return_objects=True) == ""
    assert repair_json("False", return_objects=True) == ""
    assert repair_json("Null", return_objects=True) == ""
    assert repair_json("true", return_objects=True)
    assert not repair_json("false", return_objects=True)
    assert repair_json("null", return_objects=True) is None
    assert repair_json('  {"key": true, "key2": false, "key3": null}') == '{"key": true, "key2": false, "key3": null}'
    assert repair_json('{"key": TRUE, "key2": FALSE, "key3": Null}   ') == '{"key": true, "key2": false, "key3": null}'


def test_parse_literals_require_boundaries_and_support_python_none():
    assert repair_json('{"value": None }', return_objects=True) == {"value": None}
    assert repair_json("[None, TRUE, false, Null]", return_objects=True) == [None, True, False, None]
    assert repair_json("[None", return_objects=True) == [None]
    assert repair_json('{"value": "None"}', return_objects=True) == {"value": "None"}
    assert repair_json('{"value": none}', return_objects=True) == {"value": None}
    assert repair_json('{"value": NONE}', return_objects=True) == {"value": None}
    assert repair_json('{"value": trueblue}', return_objects=True) == {"value": "trueblue"}
    assert repair_json('{"value": falsehood}', return_objects=True) == {"value": "falsehood"}
    assert repair_json('{"value": nullify}', return_objects=True) == {"value": "nullify"}
    assert repair_json('{"value": NoneType}', return_objects=True) == {"value": "NoneType"}

    repaired, logs = repair_json('{"value": None}', return_objects=True, logging=True)
    assert repaired == {"value": None}
    assert any(log["text"] == "Converted unquoted Python None literal to JSON null" for log in logs)


def test_parse_string_fast_path_keeps_clean_values_log_free():
    repaired, logs = repair_json('{"key": "value", "items": ["alpha", "beta"]}', return_objects=True, logging=True)
    assert repaired == {"key": "value", "items": ["alpha", "beta"]}
    assert logs == []


def test_parse_string_fast_path_falls_back_for_escapes_with_logs():
    repaired, logs = repair_json(
        '{"key": "\\u0076\\u0061\\u006C\\u0075\\u0065"}',
        skip_json_loads=True,
        return_objects=True,
        logging=True,
    )
    assert repaired == {"key": "value"}
    assert any(log["text"] == "Found a unicode escape sequence, normalizing it" for log in logs)


def test_parse_string_fast_path_rejects_ambiguous_top_level_trailing_text():
    parser = JSONParser('"value" trailing', None, False)
    assert _try_parse_simple_quoted_string(parser) is None


def test_parse_string_keeps_inline_object_literal_after_comma():
    raw = '{"x": "However, the provided user answer is {"blank_1": "music"}, which is not a plain string"}'
    expected = '{"x": "However, the provided user answer is {\\"blank_1\\": \\"music\\"}, which is not a plain string"}'

    assert repair_json(raw) == expected
    assert repair_json(raw, skip_json_loads=True) == expected


def test_parse_string_keeps_inline_object_literal_before_next_member():
    cases = [
        (
            '{"x": "a, {"k": 1}, "y": 2}',
            '{"x": "a, {\\"k\\": 1}", "y": 2}',
        ),
        (
            '{"x": "a, {"k": {"n": 1}}, "y": 2}',
            '{"x": "a, {\\"k\\": {\\"n\\": 1}}", "y": 2}',
        ),
    ]

    for raw, expected in cases:
        assert repair_json(raw) == expected
        assert repair_json(raw, skip_json_loads=True) == expected


def test_parse_string_object_value_brace_heuristics():
    cases = [
        ('{"key": "value}\\\\\\"more"}', {"key": 'value}"more'}),
        ('{"key": "value} "tail}', {"key": "value} "}),
        ('{"key": "value} "tail" more}', {"key": 'value} "tail" more'}),
        ('{"key": "value} key2: value2}', {"key": "value"}),
    ]

    for raw, expected in cases:
        assert repair_json(raw, return_objects=True, skip_json_loads=True) == expected


def test_parse_string_far_quote_comma_payload_keeps_existing_repair_shape():
    raw = '{"a": "' + ("x," * 10_000) + '" tail'

    assert repair_json(raw, return_objects=True, skip_json_loads=True) == {"a": "x," * 10_000}


def test_parse_string_far_quote_brace_payload_keeps_existing_repair_shape():
    raw = '{"a": "' + ("x}" * 5_000) + '" tail'

    assert repair_json(raw, return_objects=True, skip_json_loads=True) == {"a": "x}" * 5_000}


def test_parse_string_preserves_escaped_braces_after_comma_group():
    raw = r'{ "key": "\\{1,2\\} \\{3\\}" }'

    assert repair_json(raw, return_objects=True, skip_json_loads=True) == {"key": r"\{1,2\} \{3\}"}


@pytest.mark.parametrize(
    ("raw", "expected", "serialized"),
    [
        (r'{"key": "a\\\\b\\\\c",}', r"a\\b\\c", r'{"key": "a\\\\b\\\\c"}'),
        (r'{"key": "1\\\\2\\\\3",}', r"1\\2\\3", r'{"key": "1\\\\2\\\\3"}'),
    ],
)
def test_parse_string_preserves_repeated_escaped_backslashes_during_repair(raw, expected, serialized):
    for skip_json_loads in (False, True):
        assert repair_json(raw, return_objects=True, skip_json_loads=skip_json_loads) == {"key": expected}
        assert repair_json(raw, skip_json_loads=skip_json_loads) == serialized


def test_parse_string_preserves_latex_command_after_bracketed_comma():
    raw = r'{ "key": "x [0,2] f(-\\frac{3}{4})" }'

    assert repair_json(raw, return_objects=True, skip_json_loads=True) == {"key": r"x [0,2] f(-\frac{3}{4})"}


def test_parse_string_keeps_latex_braces_before_inline_object_literal():
    raw = r'{ "llm_reason": "curve $C: \\frac{x^2}{m}$ answer is {"blank_1": "5"}, correct is 4.", "llm_answer": "4" }'

    assert repair_json(raw, return_objects=True, skip_json_loads=True) == {
        "llm_reason": r'curve $C: \frac{x^2}{m}$ answer is {"blank_1": "5"}, correct is 4.',
        "llm_answer": "4",
    }


def test_parse_string_missing_quotes_object_value_stops_at_quote_fragment():
    assert repair_json('{0:a"0"', return_objects=True, skip_json_loads=True) == {"0": "a"}


def test_parse_string_fast_path_string_wrapper_fallbacks():
    escaped_parser = JSONParser("", None, False)
    escaped_parser.json_str = StringFileWrapper(StringIO('"va\\lue"'), 2)
    assert _try_parse_simple_quoted_string(escaped_parser) is None

    unterminated_parser = JSONParser("", None, False)
    unterminated_parser.json_str = StringFileWrapper(StringIO('"value'), 2)
    assert _try_parse_simple_quoted_string(unterminated_parser) is None


def test_brace_before_code_fence_helper_rejects_non_delimiter_after_quote():
    parser = JSONParser('}```"oops', None, False)
    assert not _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_rejects_unterminated_container_after_fence():
    parser = JSONParser("}``` [1,2", None, False)
    assert not _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_accepts_unbalanced_container_like_prose_after_fence():
    parser = JSONParser('}``` [{\n", "b": 1', None, False)
    assert _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_accepts_later_closing_quote_after_quoted_prose():
    parser = JSONParser('}```Implementation: "xxx", xxx", "b": 1', None, False)
    assert _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_rejects_container_started_after_fence():
    parser = JSONParser('}``` [1,"z"], "b": 1', None, False)
    assert not _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_rejects_container_closing_object_after_fence():
    parser = JSONParser("}``` [1,2]}", None, False)
    assert not _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_accepts_literal_container_after_fence():
    parser = JSONParser('}``` [1,2]\n", "b": 1', None, False)
    assert _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_rejects_comment_prefixed_container_after_fence():
    parser = JSONParser('}``` // c\n [1,"z"], "b": 1', None, False)
    assert not _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_accepts_comment_prefixed_literal_container_after_fence():
    parser = JSONParser('}``` // c\n [1,2]\n", "b": 1', None, False)
    assert _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_accepts_literal_container_after_fence_with_trailing_comma():
    parser = JSONParser('}``` [1,2],\n", "b": 1', None, False)
    assert _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_brace_before_code_fence_helper_accepts_comment_prefixed_literal_container_after_fence_with_trailing_comma():
    parser = JSONParser('}``` // c\n [1,2],\n", "b": 1', None, False)
    assert _brace_before_code_fence_belongs_to_string(parser, StringParseState(), 1)


def test_skip_inline_container_returns_same_index_for_non_container():
    parser = JSONParser("text", None, False)
    assert _skip_inline_container(parser, 0) == 0


def test_starts_nested_inline_container_accepts_container_at_start():
    parser = JSONParser("[1, 2]", None, False)
    assert _starts_nested_inline_container(parser, 0)


def test_starts_nested_inline_container_accepts_out_of_range_prefix_conservatively():
    parser = JSONParser("[1, 2]", None, False)
    assert _starts_nested_inline_container(parser, 10)


def test_starts_nested_inline_container_rejects_unmatched_inner_array_after_comma():
    parser = JSONParser("[foo, [bar]", None, False)
    assert not _starts_nested_inline_container(parser, 6)


def test_starts_nested_inline_container_accepts_object_with_quoted_key_after_comma():
    parser = JSONParser('[foo, {"k": 1}]', None, False)
    assert _starts_nested_inline_container(parser, 6)


def test_starts_nested_inline_container_accepts_numeric_array_after_comma():
    parser = JSONParser("[foo, [2]]", None, False)
    assert _starts_nested_inline_container(parser, 6)


def test_starts_nested_inline_container_accepts_numeric_parenthesized_value_after_comma():
    parser = JSONParser("(foo, (2))", None, False)
    assert _starts_nested_inline_container(parser, 6)


def test_starts_nested_inline_container_accepts_object_with_bare_key_after_colon():
    parser = JSONParser("{foo: {bar: 1}}", None, False)
    assert _starts_nested_inline_container(parser, 6)


def test_starts_nested_inline_container_rejects_object_with_bare_key_after_comma():
    parser = JSONParser("[foo, {bar}]", None, False)
    assert not _starts_nested_inline_container(parser, 6)


def test_starts_nested_inline_container_rejects_non_container_after_separator():
    parser = JSONParser("[foo, xbar]", None, False)
    assert not _starts_nested_inline_container(parser, 6)


def test_starts_nested_inline_container_rejects_object_with_non_key_start_after_colon():
    parser = JSONParser("{foo: {-bar}}", None, False)
    assert not _starts_nested_inline_container(parser, 6)


def test_skip_inline_container_skips_nested_inline_container():
    parser = JSONParser("[{items: [1, 2]}] tail", None, False)
    assert _skip_inline_container(parser, 0) == 17


def test_skip_inline_container_keeps_hash_like_literal_content():
    parser = JSONParser("[# literal] tail", None, False)
    assert _skip_inline_container(parser, 0) == 11


def test_skip_inline_container_keeps_line_comment_like_literal_content():
    parser = JSONParser("[http://x] tail", None, False)
    assert _skip_inline_container(parser, 0) == 10


def test_skip_inline_container_keeps_block_comment_like_literal_content():
    parser = JSONParser("[a/*b*/c] tail", None, False)
    assert _skip_inline_container(parser, 0) == 9


def test_skip_inline_container_keeps_regex_like_literal_content():
    parser = JSONParser("[/a//b/] tail", None, False)
    assert _skip_inline_container(parser, 0) == 8


def test_skip_inline_container_keeps_unmatched_inner_delimiter_as_literal_content():
    parser = JSONParser("[foo[bar] tail", None, False)
    assert _skip_inline_container(parser, 0) == 9


def test_skip_inline_container_rejects_unterminated_container():
    parser = JSONParser("[1, 2", None, False)
    assert _skip_inline_container(parser, 0) is None


def test_skip_inline_container_rejects_unterminated_string_inside_container():
    parser = JSONParser('["unterminated', None, False)
    assert _skip_inline_container(parser, 0) is None


def test_skip_inline_container_rejects_unterminated_block_comment():
    parser = JSONParser("[/* c", None, False)
    assert _skip_inline_container(parser, 0) is None


def test_update_inline_container_stack_starts_tracking_pending_container():
    inline_container_stack: list[str] = []
    pending_inline_container, keep_inline_container_char = update_inline_container_stack(
        "[", True, inline_container_stack
    )

    assert not pending_inline_container
    assert not keep_inline_container_char
    assert inline_container_stack == ["["]


def test_update_inline_container_stack_tracks_nested_container():
    inline_container_stack = ["["]
    pending_inline_container, keep_inline_container_char = update_inline_container_stack(
        "{", False, inline_container_stack
    )

    assert not pending_inline_container
    assert not keep_inline_container_char
    assert inline_container_stack == ["[", "{"]


def test_update_inline_container_stack_keeps_closing_container_character():
    inline_container_stack = ["["]
    pending_inline_container, keep_inline_container_char = update_inline_container_stack(
        "]", False, inline_container_stack
    )

    assert not pending_inline_container
    assert keep_inline_container_char
    assert inline_container_stack == []


def test_scan_string_body_keeps_closing_inline_container_character():
    parser = JSONParser(']"', None, False)
    parser.context.set(ContextValues.OBJECT_VALUE)
    state = StringParseState(string_acc="x", inline_container_stack=["["])

    char = _scan_string_body(parser, state)

    assert char == '"'
    assert state.string_acc == "x]"
    assert state.inline_container_stack == []


def test_scan_string_body_closes_low_smart_quote_span_with_unicode_quote():
    parser = JSONParser('”"', None, False)
    parser.context.set(ContextValues.OBJECT_VALUE)
    state = StringParseState(rstring_delimiter='"\0', string_acc="prefix")

    char = _scan_string_body(parser, state)

    assert char == '"'
    assert state.string_acc == "prefix”"
    assert state.rstring_delimiter == '"'


def test_quoted_object_member_follows_rejects_unquoted_next_key():
    parser = JSONParser('"\n", bare', None, False)
    assert not _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_rejects_unterminated_next_key():
    parser = JSONParser('"\n", "unterminated', None, False)
    assert not _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_accepts_single_quoted_next_key():
    parser = JSONParser("\"\n\", 'b': 1", None, False)
    assert _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_accepts_curly_quoted_next_key():
    parser = JSONParser('"\n", “b”: 1', None, False)
    assert _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_accepts_comment_before_next_key():
    parser = JSONParser('"\n", // c\n"b": 1', None, False)
    assert _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_accepts_hash_comment_before_next_key():
    parser = JSONParser('"\n", # c\n"b": 1', None, False)
    assert _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_accepts_block_comment_before_next_key():
    parser = JSONParser('"\n", /* c */ "b": 1', None, False)
    assert _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_accepts_comment_before_bare_next_key():
    parser = JSONParser('"\n", // c\n b: 1', None, False)
    assert _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_accepts_bare_next_key():
    parser = JSONParser('"\n",\n b: 1', None, False)
    assert _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_rejects_trailing_comma_endings():
    assert not _quoted_object_member_follows(JSONParser('"\n",}', None, False), 2)
    assert not _quoted_object_member_follows(JSONParser('"\n",', None, False), 2)


def test_quoted_object_member_follows_rejects_unclosed_block_comment_before_next_key():
    parser = JSONParser('"\n", /* c', None, False)
    assert not _quoted_object_member_follows(parser, 2)


def test_quoted_object_member_follows_rejects_array_after_comment():
    parser = JSONParser('"\n", /* c */ [1, 2]', None, False)
    assert not _quoted_object_member_follows(parser, 2)


def test_parse_string_empty_single_quoted_key():
    assert repair_json("{'': 1}") == '{"": 1}'

```

### `tests/test_performance.py`

```py
import os
import pathlib
import time

import pytest

from src.json_repair import repair_json

path = pathlib.Path(__file__).parent.resolve()
CI = os.getenv("CI") is not None

correct_json = (path / "valid.json").read_text()

incorrect_json = (path / "invalid.json").read_text()


def _unclosed_object_string_payload(target_bytes, fragment_factory):
    base = '{"a": "'
    pieces = []
    index = 0
    while len(base) + len(",".join(pieces)) < target_bytes:
        pieces.append(fragment_factory(index))
        index += 1
    return base + ",".join(pieces)


unclosed_object_string_fragments = '{"a": "' + ",".join("fragment" for _ in range(3000))
mixed_quote_object_string_fragments = _unclosed_object_string_payload(
    35000,
    lambda index: 'frag"ment' if index % 3 == 0 else ("'fragment'" if index % 3 == 1 else "fragment"),
)
far_quote_comma_object_string_fragments = '{"a": "' + ("x," * 10_000) + '" tail'
far_quote_brace_object_string_fragments = '{"a": "' + ("x}" * 5_000) + '" tail'

schema_perf = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "_id": {"type": "string"},
            "index": {"type": "integer"},
            "guid": {"type": "string"},
            "isActive": {"type": "boolean"},
            "tags": {"type": "array", "items": {"type": "string"}},
            "friends": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"id": {"type": "integer"}, "name": {"type": "string"}},
                    "required": ["id", "name"],
                },
            },
        },
        "required": ["_id", "index", "guid", "isActive", "tags", "friends"],
        "additionalProperties": True,
    },
}


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_true_true_correct(benchmark):
    benchmark(repair_json, correct_json, return_objects=True, skip_json_loads=True)

    # Retrieve the median execution time
    mean_time = benchmark.stats.get("median")

    # Define your time threshold in seconds
    max_time = 3 / 10**3  # 3 millisecond

    # Assert that the average time is below the threshold
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_true_true_incorrect(benchmark):
    benchmark(repair_json, incorrect_json, return_objects=True, skip_json_loads=True)

    # Retrieve the median execution time
    mean_time = benchmark.stats.get("median")

    # Define your time threshold in seconds
    max_time = 3 / 10**3  # 3 millisecond

    # Assert that the average time is below the threshold
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_true_false_correct(benchmark):
    benchmark(repair_json, correct_json, return_objects=True, skip_json_loads=False)
    # Retrieve the median execution time
    mean_time = benchmark.stats.get("median")

    # Define your time threshold in seconds
    max_time = 30 * (1 / 10**6)  # 30 microsecond

    # Assert that the average time is below the threshold
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_true_false_incorrect(benchmark):
    benchmark(repair_json, incorrect_json, return_objects=True, skip_json_loads=False)
    # Retrieve the median execution time
    mean_time = benchmark.stats.get("median")

    # Define your time threshold in seconds
    max_time = 3 / 10**3  # 3 millisecond

    # Assert that the average time is below the threshold
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_false_true_correct(benchmark):
    benchmark(repair_json, correct_json, return_objects=False, skip_json_loads=True)
    # Retrieve the median execution time
    mean_time = benchmark.stats.get("median")

    # Define your time threshold in seconds
    max_time = 3 / 10**3  # 3 millisecond

    # Assert that the average time is below the threshold
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_false_true_incorrect(benchmark):
    benchmark(repair_json, incorrect_json, return_objects=False, skip_json_loads=True)
    # Retrieve the median execution time
    mean_time = benchmark.stats.get("median")

    # Define your time threshold in seconds
    max_time = 3 / 10**3  # 3 millisecond

    # Assert that the average time is below the threshold
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_false_false_correct(benchmark):
    benchmark(repair_json, correct_json, return_objects=False, skip_json_loads=False)
    # Retrieve the median execution time
    mean_time = benchmark.stats.get("median")

    # Define your time threshold in seconds
    max_time = 60 / 10**6  # 60 microsecond

    # Assert that the average time is below the threshold
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_false_false_incorrect(benchmark):
    benchmark(repair_json, incorrect_json, return_objects=False, skip_json_loads=False)
    # Retrieve the median execution time
    mean_time = benchmark.stats.get("median")

    # Define your time threshold in seconds
    max_time = 3 / 10**3  # 3 millisecond

    # Assert that the average time is below the threshold
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_unclosed_object_string_with_many_comma_fragments(benchmark):
    benchmark(
        repair_json,
        unclosed_object_string_fragments,
        return_objects=True,
        skip_json_loads=True,
    )

    mean_time = benchmark.stats.get("median")
    max_time = 75 / 10**3  # 75 millisecond
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_unclosed_object_string_with_mixed_quote_fragments(benchmark):
    benchmark(
        repair_json,
        mixed_quote_object_string_fragments,
        return_objects=True,
        skip_json_loads=True,
    )

    mean_time = benchmark.stats.get("median")
    max_time = 125 / 10**3  # 125 millisecond
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_far_quote_object_string_with_many_comma_fragments():
    start = time.perf_counter()
    repair_json(far_quote_comma_object_string_fragments, return_objects=True, skip_json_loads=True)
    elapsed = time.perf_counter() - start

    max_time = 250 / 10**3  # 250 millisecond
    assert elapsed < max_time, f"Performance regression: {elapsed:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_far_quote_object_string_with_many_brace_fragments():
    start = time.perf_counter()
    repair_json(far_quote_brace_object_string_fragments, return_objects=True, skip_json_loads=True)
    elapsed = time.perf_counter() - start

    max_time = 250 / 10**3  # 250 millisecond
    assert elapsed < max_time, f"Performance regression: {elapsed:.3f}s > {max_time:.3f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_schema_true_false_correct(benchmark):
    pytest.importorskip("jsonschema")
    benchmark(
        repair_json,
        correct_json,
        schema=schema_perf,
        return_objects=True,
        skip_json_loads=False,
    )

    mean_time = benchmark.stats.get("median")
    max_time = 6 / 10**4  # 600 microsecond
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.6f}s > {max_time:.6f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_schema_false_false_correct(benchmark):
    pytest.importorskip("jsonschema")
    benchmark(
        repair_json,
        correct_json,
        schema=schema_perf,
        return_objects=False,
        skip_json_loads=False,
    )

    mean_time = benchmark.stats.get("median")
    max_time = 8 / 10**4  # 800 microsecond
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.6f}s > {max_time:.6f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_schema_true_true_incorrect(benchmark):
    pytest.importorskip("jsonschema")
    benchmark(
        repair_json,
        incorrect_json,
        schema=schema_perf,
        return_objects=True,
        skip_json_loads=True,
    )

    mean_time = benchmark.stats.get("median")
    max_time = 45 / 10**4  # 4.5 millisecond
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.6f}s > {max_time:.6f}s"


@pytest.mark.skipif(CI, reason="Performance tests are skipped in CI")
def test_schema_false_true_incorrect(benchmark):
    pytest.importorskip("jsonschema")
    benchmark(
        repair_json,
        incorrect_json,
        schema=schema_perf,
        return_objects=False,
        skip_json_loads=True,
    )

    mean_time = benchmark.stats.get("median")
    max_time = 45 / 10**4  # 4.5 millisecond
    assert mean_time < max_time, f"Benchmark exceeded threshold: {mean_time:.6f}s > {max_time:.6f}s"

```

### `tests/test_repair_json_cli.py`

```py
import io
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from src.json_repair.json_repair import cli


def test_cli(capsys):
    # Create a temporary file
    temp_fd, temp_path = tempfile.mkstemp(suffix=".json")
    _, tempout_path = tempfile.mkstemp(suffix=".json")
    temp_path = Path(temp_path)
    tempout_path = Path(tempout_path)
    try:
        # Write content to the temporary file
        with os.fdopen(temp_fd, "w") as tmp:
            tmp.write("{key:value")
        cli(inline_args=[str(temp_path), "--indent", "0", "--ensure_ascii"])
        captured = capsys.readouterr()
        assert captured.out == '{\n"key": "value"\n}\n'

        # Test the output option
        cli(inline_args=[str(temp_path), "--indent", "0", "-o", str(tempout_path)])
        with tempout_path.open() as tmp:
            out = tmp.read()
        assert out == '{\n"key": "value"\n}'

        # Test the inline option
        cli(inline_args=[str(temp_path), "--indent", "0", "-i"])
        with temp_path.open() as tmp:
            out = tmp.read()
        assert out == '{\n"key": "value"\n}'

    finally:
        # Clean up - delete the temporary file
        temp_path.unlink()
        tempout_path.unlink()

    # Prepare a JSON string that needs to be repaired.
    test_input = "{key:value"
    # Expected output when running cli with --indent 0.
    expected_output = '{\n"key": "value"\n}\n'
    # Patch sys.stdin so that cli() reads from it instead of a file.
    with patch("sys.stdin", new=io.StringIO(test_input)):
        cli(inline_args=["--indent", "0"])
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_cli_inline_requires_filename(capsys):
    """cli() should exit with an error when --inline is passed without a filename."""
    with pytest.raises(SystemExit) as exc:
        cli(inline_args=["--inline"])
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: Inline mode requires a filename"
    assert exc.value.code != 0


def test_cli_inline_and_output_error(tmp_path, capsys):
    """cli() should exit with an error when --inline and --output are used together."""
    outfile = tmp_path / "out.json"
    with pytest.raises(SystemExit) as exc:
        cli(inline_args=["dummy.json", "--inline", "--output", str(outfile)])
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: You cannot pass both --inline and --output"
    assert exc.value.code != 0


def test_cli_schema_file_guides_repair(tmp_path, capsys):
    pytest.importorskip("jsonschema")
    schema_path = tmp_path / "schema.json"
    schema = {
        "type": "object",
        "properties": {"value": {"type": "integer"}},
        "required": ["value"],
    }
    schema_path.write_text(json.dumps(schema))
    input_path = tmp_path / "input.json"
    input_path.write_text('{"value": }')

    cli(inline_args=[str(input_path), "--indent", "0", "--schema", str(schema_path)])
    captured = capsys.readouterr()
    assert captured.out == '{\n"value": 0\n}\n'


def test_cli_schema_applies_to_valid_json(tmp_path, capsys):
    pytest.importorskip("jsonschema")
    schema_path = tmp_path / "schema.json"
    schema = {
        "type": "object",
        "properties": {"value": {"type": "integer"}},
        "required": ["value"],
    }
    schema_path.write_text(json.dumps(schema))
    input_path = tmp_path / "input.json"
    input_path.write_text('{"value": "1"}')

    cli(inline_args=[str(input_path), "--indent", "0", "--schema", str(schema_path)])
    captured = capsys.readouterr()
    assert captured.out == '{\n"value": 1\n}\n'

    cli(
        inline_args=[
            str(input_path),
            "--indent",
            "0",
            "--schema",
            str(schema_path),
            "--skip-json-loads",
        ]
    )
    captured = capsys.readouterr()
    assert captured.out == '{\n"value": 1\n}\n'


def test_cli_schema_model_guides_repair(tmp_path, capsys, monkeypatch):
    pytest.importorskip("jsonschema")
    pydantic = pytest.importorskip("pydantic")
    version = getattr(pydantic, "VERSION", getattr(pydantic, "__version__", "0"))
    if int(version.split(".")[0]) < 2:
        pytest.skip("pydantic v2 required")

    module_path = tmp_path / "schema_model.py"
    module_path.write_text("from pydantic import BaseModel\n\n\nclass SchemaModel(BaseModel):\n    value: int\n")
    monkeypatch.syspath_prepend(tmp_path)

    input_path = tmp_path / "input.json"
    input_path.write_text('{"value": "1"}')

    cli(
        inline_args=[
            str(input_path),
            "--indent",
            "0",
            "--schema-model",
            "schema_model:SchemaModel",
            "--skip-json-loads",
        ]
    )
    captured = capsys.readouterr()
    assert captured.out == '{\n"value": 1\n}\n'


def test_cli_schema_and_strict_error(tmp_path, capsys):
    schema_path = tmp_path / "schema.json"
    schema_path.write_text(json.dumps({"type": "integer"}))
    input_path = tmp_path / "input.json"
    input_path.write_text('{"value": }')

    with pytest.raises(SystemExit) as exc:
        cli(inline_args=[str(input_path), "--schema", str(schema_path), "--strict"])
    captured = capsys.readouterr()
    assert "schema" in captured.err.lower()
    assert exc.value.code != 0


def test_cli_schema_and_schema_model_are_mutually_exclusive(tmp_path, capsys):
    schema_path = tmp_path / "schema.json"
    schema_path.write_text(json.dumps({"type": "integer"}))

    with pytest.raises(SystemExit) as exc:
        cli(
            inline_args=[
                "dummy.json",
                "--schema",
                str(schema_path),
                "--schema-model",
                "schema_model:SchemaModel",
            ]
        )
    captured = capsys.readouterr()
    assert "schema" in captured.err.lower()
    assert exc.value.code != 0


def test_cli_schema_repair_mode_salvage_requires_schema(capsys):
    with pytest.raises(SystemExit) as exc:
        cli(inline_args=["--schema-repair-mode", "salvage"])
    captured = capsys.readouterr()
    assert "schema-repair-mode" in captured.err.lower()
    assert exc.value.code != 0


def test_cli_schema_repair_mode_salvage_drops_invalid_items(tmp_path, capsys):
    pytest.importorskip("jsonschema")
    schema_path = tmp_path / "schema.json"
    schema = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "score": {"type": "number"},
                    },
                    "required": ["id", "score"],
                },
            }
        },
        "required": ["items"],
    }
    schema_path.write_text(json.dumps(schema))
    input_path = tmp_path / "input.json"
    input_path.write_text('{"items":[{"id":1,"score":85.6},{"id":2,"score":"N/A"}]}')

    cli(
        inline_args=[
            str(input_path),
            "--indent",
            "0",
            "--schema",
            str(schema_path),
            "--schema-repair-mode",
            "salvage",
        ]
    )
    captured = capsys.readouterr()
    assert captured.out == '{\n"items": [\n{\n"id": 1,\n"score": 85.6\n}\n]\n}\n'

```

### `tests/test_repair_json_from_file.py`

```py
import os
import pathlib
import tempfile
from io import StringIO

from src.json_repair.json_repair import from_file, load


def test_load_repairs_from_current_file_position():
    prefix = '{"stale": true}\n'
    raw = prefix + '{"key": }'

    for skip_json_loads in [False, True]:
        fd = StringIO(raw)
        fd.seek(len(prefix))

        assert load(fd, skip_json_loads=skip_json_loads, chunk_length=2) == {"key": ""}


def test_repair_json_from_file():
    path = pathlib.Path(__file__).parent.resolve()

    # Use chunk_length 2 to test the buffering feature
    assert from_file(filename=path / "invalid.json") == [
        {
            "_id": "655b66256574f09bdae8abe8",
            "index": 0,
            "guid": "31082ae3-b0f3-4406-90f4-cc450bd4379d",
            "isActive": False,
            "balance": "$2,562.78",
            "picture": "http://placehold.it/32x32",
            "age": 32,
            "eyeColor": "brown",
            "name": "Glover Rivas",
            "gender": "male",
            "company": "EMPIRICA",
            "email": "gloverrivas@empirica.com",
            "phone": "+1 (842) 507-3063",
            "address": "536 Montague Terrace, Jenkinsville, Kentucky, 2235",
            "about": "Mollit consectetur excepteur voluptate tempor dolore ullamco enim irure ullamco non enim officia. Voluptate occaecat proident laboris ea Lorem cupidatat reprehenderit nisi nisi aliqua. Amet nulla ipsum deserunt excepteur amet ad aute aute ex. Et enim minim sit veniam est quis dolor nisi sunt quis eiusmod in. Amet eiusmod cillum sunt occaecat dolor laboris voluptate in eiusmod irure aliqua duis.",
            "registered": "2023-11-18T09:32:36 -01:00",
            "latitude": 36.26102,
            "longitude": -91.304608,
            "tags": ["non", "tempor", "do", "ullamco", "dolore", "sunt", "ipsum"],
            "friends": [
                {"id": 0, "name": "Cara Shepherd"},
                {"id": 1, "name": "Mason Farley"},
                {"id": 2, "name": "Harriet Cochran"},
            ],
            "greeting": "Hello, Glover Rivas! You have 7 unread messages.",
            "favoriteFruit": "strawberry",
        },
        {
            "_id": "655b662585364bc57278bb6f",
            "index": 1,
            "guid": "0dea7a3a-f812-4dde-b78d-7a9b58e5da05",
            "isActive": True,
            "balance": "$1,359.48",
            "picture": "http://placehold.it/32x32",
            "age": 38,
            "eyeColor": "brown",
            "name": "Brandi Moreno",
            "gender": "female",
            "company": "MARQET",
            "email": "brandimoreno@marqet.com",
            "phone": "+1 (850) 434-2077",
            "address": "537 Doone Court, Waiohinu, Michigan, 3215",
            "about": "Irure proident adipisicing do Lorem do incididunt in laborum in eiusmod eiusmod ad elit proident. Eiusmod dolor ex magna magna occaecat. Nulla deserunt velit ex exercitation et irure sunt. Cupidatat ut excepteur ea quis labore sint cupidatat incididunt amet eu consectetur cillum ipsum proident. Occaecat exercitation aute laborum dolor proident reprehenderit laborum in voluptate culpa. Exercitation nulla adipisicing culpa aute est deserunt ea nisi deserunt consequat occaecat ut et non. Incididunt ex exercitation dolor dolor anim cillum dolore.",
            "registered": "2015-09-03T11:47:15 -02:00",
            "latitude": -19.768953,
            "longitude": 8.948458,
            "tags": [
                "laboris",
                "occaecat",
                "laborum",
                "laborum",
                "ex",
                "cillum",
                "occaecat",
            ],
            "friends": [
                {"id": 0, "name": "Erna Kelly"},
                {"id": 1, "name": "Black Mays"},
                {"id": 2, "name": "Davis Buck"},
            ],
            "greeting": "Hello, Brandi Moreno! You have 1 unread messages.",
            "favoriteFruit": "apple",
        },
        {
            "_id": "655b6625870da431bcf5e0c2",
            "index": 2,
            "guid": "b17f6e3f-c898-4334-abbf-05cf222f143b",
            "isActive": False,
            "balance": "$1,493.77",
            "picture": "http://placehold.it/32x32",
            "age": 20,
            "eyeColor": "brown",
            "name": "Moody Meadows",
            "gender": "male",
            "company": "OPTIQUE",
            "email": "moodymeadows@optique.com",
            "phone": "+1 (993) 566-3041",
            "address": "766 Osborn Street, Bath, Maine, 7666",
            "about": "Non commodo excepteur nostrud qui adipisicing aliquip dolor minim nulla culpa proident. In ad cupidatat ea mollit ex est do deserunt proident nostrud. Cillum id id eiusmod amet exercitation nostrud cillum sunt deserunt dolore deserunt eiusmod mollit. Ut ex tempor ad laboris voluptate labore id officia fugiat exercitation amet.",
            "registered": "2015-01-16T02:48:28 -01:00",
            "latitude": -25.847327,
            "longitude": 63.95991,
            "tags": [
                "aute",
                "commodo",
                "adipisicing",
                "nostrud",
                "duis",
                "mollit",
                "ut",
            ],
            "friends": [
                {"id": 0, "name": "Lacey Cash"},
                {"id": 1, "name": "Gabrielle Harmon"},
                {"id": 2, "name": "Ellis Lambert"},
            ],
            "greeting": "Hello, Moody Meadows! You have 4 unread messages.",
            "favoriteFruit": "strawberry",
        },
        {
            "_id": "655b6625f3e1bf422220854e",
            "index": 3,
            "guid": "92229883-2bfd-4974-a08c-1b506b372e46",
            "isActive": False,
            "balance": "$2,215.34",
            "picture": "http://placehold.it/32x32",
            "age": 22,
            "eyeColor": "brown",
            "name": "Heath Nguyen",
            "gender": "male",
            "company": "BLEENDOT",
            "email": "heathnguyen@bleendot.com",
            "phone": "+1 (989) 512-2797",
            "address": "135 Milton Street, Graniteville, Nebraska, 276",
            "about": "Consequat aliquip irure Lorem cupidatat nulla magna ullamco nulla voluptate adipisicing anim consectetur tempor aliquip. Magna aliqua nulla eu tempor esse proident. Proident fugiat ad ex Lorem reprehenderit dolor aliquip labore labore aliquip. Deserunt aute enim ea minim officia anim culpa sint commodo. Cillum consectetur excepteur aliqua exercitation Lorem veniam voluptate.",
            "registered": "2016-07-06T01:31:07 -02:00",
            "latitude": -60.997048,
            "longitude": -102.397885,
            "tags": ["do", "ad", "consequat", "irure", "tempor", "elit", "minim"],
            "friends": [
                {"id": 0, "name": "Walker Hernandez"},
                {"id": 1, "name": "Maria Lane"},
                {"id": 2, "name": "Mcknight Barron"},
            ],
            "greeting": "Hello, Heath Nguyen! You have 4 unread messages.",
            "favoriteFruit": "apple",
        },
        {
            "_id": "655b6625519a5b5e4b6742bf",
            "index": 4,
            "guid": "c5dc685f-6d0d-4173-b4cf-f5df29a1e8ef",
            "isActive": True,
            "balance": "$1,358.90",
            "picture": "http://placehold.it/32x32",
            "age": 33,
            "eyeColor": "brown",
            "name": "Deidre Duke",
            "gender": "female",
            "company": "OATFARM",
            "email": "deidreduke@oatfarm.com",
            "phone": "+1 (875) 587-3256",
            "address": "487 Schaefer Street, Wattsville, West Virginia, 4506",
            "about": "Laboris eu nulla esse magna sit eu deserunt non est aliqua exercitation commodo. Ad occaecat qui qui laborum dolore anim Lorem. Est qui occaecat irure enim deserunt enim aliqua ex deserunt incididunt esse. Quis in minim laboris proident non mollit. Magna ea do labore commodo. Et elit esse esse occaecat officia ipsum nisi.",
            "registered": "2021-09-12T04:17:08 -02:00",
            "latitude": 68.609781,
            "longitude": -87.509134,
            "tags": [
                "mollit",
                "cupidatat",
                "irure",
                "sit",
                "consequat",
                "anim",
                "fugiat",
            ],
            "friends": [
                {"id": 0, "name": "Bean Paul"},
                {"id": 1, "name": "Cochran Hubbard"},
                {"id": 2, "name": "Rodgers Atkinson"},
            ],
            "greeting": "Hello, Deidre Duke! You have 6 unread messages.",
            "favoriteFruit": "apple",
        },
        {
            "_id": "655b6625a19b3f7e5f82f0ea",
            "index": 5,
            "guid": "75f3c264-baa1-47a0-b21c-4edac23d9935",
            "isActive": True,
            "balance": "$3,554.36",
            "picture": "http://placehold.it/32x32",
            "age": 26,
            "eyeColor": "blue",
            "name": "Lydia Holland",
            "gender": "female",
            "company": "ESCENTA",
            "email": "lydiaholland@escenta.com",
            "phone": "+1 (927) 482-3436",
            "address": "554 Rockaway Parkway, Kohatk, Montana, 6316",
            "about": "Consectetur ea est labore commodo laborum mollit pariatur non enim. Est dolore et non laboris tempor. Ea incididunt ut adipisicing cillum labore officia tempor eiusmod commodo. Cillum fugiat ex consectetur ut nostrud anim nostrud exercitation ut duis in ea. Eu et id fugiat est duis eiusmod ullamco quis officia minim sint ea nisi in.",
            "registered": "2018-03-13T01:48:56 -01:00",
            "latitude": -88.495799,
            "longitude": 71.840667,
            "tags": [
                "veniam",
                "minim",
                "consequat",
                "consequat",
                "incididunt",
                "consequat",
                "elit",
            ],
            "friends": [
                {"id": 0, "name": "Debra Massey"},
                {"id": 1, "name": "Weiss Savage"},
                {"id": 2, "name": "Shannon Guerra"},
            ],
            "greeting": "Hello, Lydia Holland! You have 5 unread messages.",
            "favoriteFruit": "banana",
        },
    ]
    assert from_file(filename=path / "invalid.json", chunk_length=2) == [
        {
            "_id": "655b66256574f09bdae8abe8",
            "index": 0,
            "guid": "31082ae3-b0f3-4406-90f4-cc450bd4379d",
            "isActive": False,
            "balance": "$2,562.78",
            "picture": "http://placehold.it/32x32",
            "age": 32,
            "eyeColor": "brown",
            "name": "Glover Rivas",
            "gender": "male",
            "company": "EMPIRICA",
            "email": "gloverrivas@empirica.com",
            "phone": "+1 (842) 507-3063",
            "address": "536 Montague Terrace, Jenkinsville, Kentucky, 2235",
            "about": "Mollit consectetur excepteur voluptate tempor dolore ullamco enim irure ullamco non enim officia. Voluptate occaecat proident laboris ea Lorem cupidatat reprehenderit nisi nisi aliqua. Amet nulla ipsum deserunt excepteur amet ad aute aute ex. Et enim minim sit veniam est quis dolor nisi sunt quis eiusmod in. Amet eiusmod cillum sunt occaecat dolor laboris voluptate in eiusmod irure aliqua duis.",
            "registered": "2023-11-18T09:32:36 -01:00",
            "latitude": 36.26102,
            "longitude": -91.304608,
            "tags": ["non", "tempor", "do", "ullamco", "dolore", "sunt", "ipsum"],
            "friends": [
                {"id": 0, "name": "Cara Shepherd"},
                {"id": 1, "name": "Mason Farley"},
                {"id": 2, "name": "Harriet Cochran"},
            ],
            "greeting": "Hello, Glover Rivas! You have 7 unread messages.",
            "favoriteFruit": "strawberry",
        },
        {
            "_id": "655b662585364bc57278bb6f",
            "index": 1,
            "guid": "0dea7a3a-f812-4dde-b78d-7a9b58e5da05",
            "isActive": True,
            "balance": "$1,359.48",
            "picture": "http://placehold.it/32x32",
            "age": 38,
            "eyeColor": "brown",
            "name": "Brandi Moreno",
            "gender": "female",
            "company": "MARQET",
            "email": "brandimoreno@marqet.com",
            "phone": "+1 (850) 434-2077",
            "address": "537 Doone Court, Waiohinu, Michigan, 3215",
            "about": "Irure proident adipisicing do Lorem do incididunt in laborum in eiusmod eiusmod ad elit proident. Eiusmod dolor ex magna magna occaecat. Nulla deserunt velit ex exercitation et irure sunt. Cupidatat ut excepteur ea quis labore sint cupidatat incididunt amet eu consectetur cillum ipsum proident. Occaecat exercitation aute laborum dolor proident reprehenderit laborum in voluptate culpa. Exercitation nulla adipisicing culpa aute est deserunt ea nisi deserunt consequat occaecat ut et non. Incididunt ex exercitation dolor dolor anim cillum dolore.",
            "registered": "2015-09-03T11:47:15 -02:00",
            "latitude": -19.768953,
            "longitude": 8.948458,
            "tags": [
                "laboris",
                "occaecat",
                "laborum",
                "laborum",
                "ex",
                "cillum",
                "occaecat",
            ],
            "friends": [
                {"id": 0, "name": "Erna Kelly"},
                {"id": 1, "name": "Black Mays"},
                {"id": 2, "name": "Davis Buck"},
            ],
            "greeting": "Hello, Brandi Moreno! You have 1 unread messages.",
            "favoriteFruit": "apple",
        },
        {
            "_id": "655b6625870da431bcf5e0c2",
            "index": 2,
            "guid": "b17f6e3f-c898-4334-abbf-05cf222f143b",
            "isActive": False,
            "balance": "$1,493.77",
            "picture": "http://placehold.it/32x32",
            "age": 20,
            "eyeColor": "brown",
            "name": "Moody Meadows",
            "gender": "male",
            "company": "OPTIQUE",
            "email": "moodymeadows@optique.com",
            "phone": "+1 (993) 566-3041",
            "address": "766 Osborn Street, Bath, Maine, 7666",
            "about": "Non commodo excepteur nostrud qui adipisicing aliquip dolor minim nulla culpa proident. In ad cupidatat ea mollit ex est do deserunt proident nostrud. Cillum id id eiusmod amet exercitation nostrud cillum sunt deserunt dolore deserunt eiusmod mollit. Ut ex tempor ad laboris voluptate labore id officia fugiat exercitation amet.",
            "registered": "2015-01-16T02:48:28 -01:00",
            "latitude": -25.847327,
            "longitude": 63.95991,
            "tags": [
                "aute",
                "commodo",
                "adipisicing",
                "nostrud",
                "duis",
                "mollit",
                "ut",
            ],
            "friends": [
                {"id": 0, "name": "Lacey Cash"},
                {"id": 1, "name": "Gabrielle Harmon"},
                {"id": 2, "name": "Ellis Lambert"},
            ],
            "greeting": "Hello, Moody Meadows! You have 4 unread messages.",
            "favoriteFruit": "strawberry",
        },
        {
            "_id": "655b6625f3e1bf422220854e",
            "index": 3,
            "guid": "92229883-2bfd-4974-a08c-1b506b372e46",
            "isActive": False,
            "balance": "$2,215.34",
            "picture": "http://placehold.it/32x32",
            "age": 22,
            "eyeColor": "brown",
            "name": "Heath Nguyen",
            "gender": "male",
            "company": "BLEENDOT",
            "email": "heathnguyen@bleendot.com",
            "phone": "+1 (989) 512-2797",
            "address": "135 Milton Street, Graniteville, Nebraska, 276",
            "about": "Consequat aliquip irure Lorem cupidatat nulla magna ullamco nulla voluptate adipisicing anim consectetur tempor aliquip. Magna aliqua nulla eu tempor esse proident. Proident fugiat ad ex Lorem reprehenderit dolor aliquip labore labore aliquip. Deserunt aute enim ea minim officia anim culpa sint commodo. Cillum consectetur excepteur aliqua exercitation Lorem veniam voluptate.",
            "registered": "2016-07-06T01:31:07 -02:00",
            "latitude": -60.997048,
            "longitude": -102.397885,
            "tags": ["do", "ad", "consequat", "irure", "tempor", "elit", "minim"],
            "friends": [
                {"id": 0, "name": "Walker Hernandez"},
                {"id": 1, "name": "Maria Lane"},
                {"id": 2, "name": "Mcknight Barron"},
            ],
            "greeting": "Hello, Heath Nguyen! You have 4 unread messages.",
            "favoriteFruit": "apple",
        },
        {
            "_id": "655b6625519a5b5e4b6742bf",
            "index": 4,
            "guid": "c5dc685f-6d0d-4173-b4cf-f5df29a1e8ef",
            "isActive": True,
            "balance": "$1,358.90",
            "picture": "http://placehold.it/32x32",
            "age": 33,
            "eyeColor": "brown",
            "name": "Deidre Duke",
            "gender": "female",
            "company": "OATFARM",
            "email": "deidreduke@oatfarm.com",
            "phone": "+1 (875) 587-3256",
            "address": "487 Schaefer Street, Wattsville, West Virginia, 4506",
            "about": "Laboris eu nulla esse magna sit eu deserunt non est aliqua exercitation commodo. Ad occaecat qui qui laborum dolore anim Lorem. Est qui occaecat irure enim deserunt enim aliqua ex deserunt incididunt esse. Quis in minim laboris proident non mollit. Magna ea do labore commodo. Et elit esse esse occaecat officia ipsum nisi.",
            "registered": "2021-09-12T04:17:08 -02:00",
            "latitude": 68.609781,
            "longitude": -87.509134,
            "tags": [
                "mollit",
                "cupidatat",
                "irure",
                "sit",
                "consequat",
                "anim",
                "fugiat",
            ],
            "friends": [
                {"id": 0, "name": "Bean Paul"},
                {"id": 1, "name": "Cochran Hubbard"},
                {"id": 2, "name": "Rodgers Atkinson"},
            ],
            "greeting": "Hello, Deidre Duke! You have 6 unread messages.",
            "favoriteFruit": "apple",
        },
        {
            "_id": "655b6625a19b3f7e5f82f0ea",
            "index": 5,
            "guid": "75f3c264-baa1-47a0-b21c-4edac23d9935",
            "isActive": True,
            "balance": "$3,554.36",
            "picture": "http://placehold.it/32x32",
            "age": 26,
            "eyeColor": "blue",
            "name": "Lydia Holland",
            "gender": "female",
            "company": "ESCENTA",
            "email": "lydiaholland@escenta.com",
            "phone": "+1 (927) 482-3436",
            "address": "554 Rockaway Parkway, Kohatk, Montana, 6316",
            "about": "Consectetur ea est labore commodo laborum mollit pariatur non enim. Est dolore et non laboris tempor. Ea incididunt ut adipisicing cillum labore officia tempor eiusmod commodo. Cillum fugiat ex consectetur ut nostrud anim nostrud exercitation ut duis in ea. Eu et id fugiat est duis eiusmod ullamco quis officia minim sint ea nisi in.",
            "registered": "2018-03-13T01:48:56 -01:00",
            "latitude": -88.495799,
            "longitude": 71.840667,
            "tags": [
                "veniam",
                "minim",
                "consequat",
                "consequat",
                "incididunt",
                "consequat",
                "elit",
            ],
            "friends": [
                {"id": 0, "name": "Debra Massey"},
                {"id": 1, "name": "Weiss Savage"},
                {"id": 2, "name": "Shannon Guerra"},
            ],
            "greeting": "Hello, Lydia Holland! You have 5 unread messages.",
            "favoriteFruit": "banana",
        },
    ]

    # Create a temporary file
    temp_fd, temp_path = tempfile.mkstemp(suffix=".json")
    try:
        # Write content to the temporary file
        with os.fdopen(temp_fd, "w") as tmp:
            tmp.write("{key:value}")
        assert from_file(filename=temp_path, logging=True) == (
            {"key": "value"},
            [
                {
                    "text": "While parsing a string, we found a literal instead of a quote",
                    "context": "{key:value}",
                },
                {
                    "context": "{key:value}",
                    "text": "While parsing a string missing the left delimiter in object key context, we found a :, stopping here",
                },
                {
                    "text": "While parsing a string, we missed the closing quote, ignoring",
                    "context": "{key:value}",
                },
                {
                    "text": "While parsing a string, we found a literal instead of a quote",
                    "context": "{key:value}",
                },
                {
                    "context": "{key:value}",
                    "text": "While parsing a string missing the left delimiter in object value context, we found a , or } and we couldn't determine that a right delimiter was present. Stopping here",
                },
                {
                    "text": "While parsing a string, we missed the closing quote, ignoring",
                    "context": "{key:value}",
                },
            ],
        )
        assert from_file(filename=temp_path, logging=True, chunk_length=2) == (
            {"key": "value"},
            [
                {
                    "text": "While parsing a string, we found a literal instead of a quote",
                    "context": "{key:value}",
                },
                {
                    "context": "{key:value}",
                    "text": "While parsing a string missing the left delimiter in object key context, we found a :, stopping here",
                },
                {
                    "text": "While parsing a string, we missed the closing quote, ignoring",
                    "context": "{key:value}",
                },
                {
                    "text": "While parsing a string, we found a literal instead of a quote",
                    "context": "{key:value}",
                },
                {
                    "context": "{key:value}",
                    "text": "While parsing a string missing the left delimiter in object value context, we found a , or } and we couldn't determine that a right delimiter was present. Stopping here",
                },
                {
                    "text": "While parsing a string, we missed the closing quote, ignoring",
                    "context": "{key:value}",
                },
            ],
        )
    finally:
        # Clean up - delete the temporary file
        pathlib.Path(temp_path).unlink()

    # Create a temporary file
    temp_fd, temp_path = tempfile.mkstemp(suffix=".json")
    try:
        # Write content to the temporary file
        with os.fdopen(temp_fd, "w") as tmp:
            tmp.write("x" * 5 * 1024 * 1024)  # 5 MB
        assert from_file(filename=temp_path, logging=True) == ("", [])

    finally:
        # Clean up - delete the temporary file
        pathlib.Path(temp_path).unlink()

```

### `tests/test_schema_guided_parse.py`

```py
from typing import cast

import pytest

from src.json_repair import repair_json


def repair_with_schema(raw, schema, **kwargs):
    return repair_json(raw, schema=schema, skip_json_loads=True, return_objects=True, **kwargs)


def _two_string_schema() -> dict:
    pytest.importorskip("jsonschema")
    pydantic = pytest.importorskip("pydantic")
    version = getattr(pydantic, "VERSION", getattr(pydantic, "__version__", "0"))
    if int(version.split(".")[0]) < 2:
        pytest.skip("pydantic v2 required")

    class SchemaModel(pydantic.BaseModel):
        a: str
        b: str

    return cast("dict", SchemaModel.model_json_schema())


def _assert_two_string_schema_repairs(raw: str, expected: dict) -> None:
    schema = _two_string_schema()
    assert repair_json(raw, schema=schema, return_objects=True) == expected
    assert repair_json(raw, schema=schema, skip_json_loads=True, return_objects=True) == expected


def test_schema_guides_missing_value_type_defaults():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "text": {"type": "string"},
            "count": {"type": "integer"},
            "ratio": {"type": "number"},
            "flag": {"type": "boolean"},
            "items": {"type": "array", "items": {"type": "string"}},
            "payload": {"type": "object"},
            "nothing": {"type": "null"},
        },
        "required": ["text", "count", "ratio", "flag", "items", "payload", "nothing"],
    }
    raw = '{ "text": , "count": , "ratio": , "flag": , "items": , "payload": , "nothing": }'
    assert repair_with_schema(raw, schema) == {
        "text": "",
        "count": 0,
        "ratio": 0,
        "flag": False,
        "items": [],
        "payload": {},
        "nothing": None,
    }


def test_schema_missing_required_property_raises():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"required_value": {"type": "integer", "default": 1}},
        "required": ["required_value"],
    }
    with pytest.raises(ValueError, match="Missing required properties"):
        repair_with_schema("{}", schema)


def test_schema_salvage_selects_first_matching_top_level_fragment():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
        "required": ["name", "age"],
    }
    raw = """Here is an example: {"foo": 1}

Final answer:
```json
{"name": "Alice", "age": 30}
```

Alternative: {"name": "Bob", "age": 40}"""

    assert repair_with_schema(raw, schema, schema_repair_mode="salvage") == {"name": "Alice", "age": 30}
    repaired, logs = cast(
        "tuple[object, list[dict[str, str]]]",
        repair_json(raw, schema=schema, skip_json_loads=True, logging=True, schema_repair_mode="salvage"),
    )
    assert repaired == {"name": "Alice", "age": 30}
    assert any(log["text"] == "Skipped top-level fragment that did not match schema while salvaging" for log in logs)


def test_schema_salvage_skips_list_fragment_before_matching_object():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
        "required": ["name", "age"],
    }
    raw = """The options are ["a", "b"].

{"name": "Alice", "age": 30}"""

    assert repair_with_schema(raw, schema, schema_repair_mode="salvage") == {"name": "Alice", "age": 30}


def test_schema_standard_still_rejects_invalid_first_top_level_fragment():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
        "required": ["name", "age"],
    }

    with pytest.raises(ValueError, match="Missing required properties"):
        repair_with_schema('{"foo": 1}\n{"name": "Alice", "age": 30}', schema)


def test_schema_salvage_raises_when_no_top_level_fragment_matches():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
        "required": ["name", "age"],
    }

    with pytest.raises(ValueError, match="Missing required properties"):
        repair_with_schema('{"foo": 1}\n{"bar": 2}', schema, schema_repair_mode="salvage")

    with pytest.raises(ValueError, match="Missing required properties"):
        repair_with_schema('{"foo": 1} trailing prose', schema, schema_repair_mode="salvage")

    with pytest.raises(ValueError, match="Missing required properties"):
        repair_with_schema('{"foo": 1} // trailing comment', schema, schema_repair_mode="salvage")

    with pytest.raises(ValueError, match="is not of type 'object'"):
        repair_with_schema("", schema, schema_repair_mode="salvage")


def test_schema_salvage_does_not_select_an_item_from_a_real_top_level_array():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
        "required": ["name", "age"],
    }

    with pytest.raises(ValueError, match="Expected object"):
        repair_with_schema(
            '[{"foo": 1}, {"name": "Alice", "age": 30}]',
            schema,
            schema_repair_mode="salvage",
        )


def test_schema_optional_default_is_inserted():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"note": {"type": "string", "default": "n/a"}},
    }
    assert repair_with_schema("{}", schema) == {"note": "n/a"}


def test_schema_and_strict_are_mutually_exclusive():
    with pytest.raises(ValueError, match="schema and strict"):
        repair_json("{}", schema={}, strict=True, return_objects=True)


def test_schema_applies_to_valid_json_without_skip_json_loads():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"value": {"type": "integer"}},
        "required": ["value"],
    }
    # Fast-path validation fails, then parser+schema fallback repairs.
    assert repair_json('{"value": "1"}', schema=schema, return_objects=True) == {"value": 1}
    # Fast-path validation fails for a scalar, but schema-aware repair can fix it directly.
    assert repair_json('"1"', schema={"type": "integer"}, return_objects=True) == 1
    # Fast-path validation fails for a valid scalar and parser fallback returns empty string.
    assert repair_json("true", schema={"type": "string"}, return_objects=True) == ""

    with pytest.raises(ValueError, match="does not match"):
        repair_json('"bbb"', schema={"type": "string", "pattern": "^a+$"}, return_objects=True)


def test_schema_union_branch_keeps_root_defs_scope_during_repair():
    pytest.importorskip("jsonschema")
    schema = {
        "$defs": {
            "Item": {
                "type": "object",
                "properties": {"name": {"type": "string", "pattern": "^example$"}},
                "required": ["name"],
            }
        },
        "type": "object",
        "properties": {
            "value": {
                "anyOf": [
                    {"type": "array", "items": {"$ref": "#/$defs/Item"}},
                    {"type": "null"},
                ]
            }
        },
        "required": ["value"],
    }

    assert repair_json('{"value": [{"name": "example"}],}', schema=schema, return_objects=True) == {
        "value": [{"name": "example"}]
    }
    with pytest.raises(ValueError, match="Expected null"):
        repair_json('{"value": [{"name": "invalid"}],}', schema=schema, return_objects=True)


def test_schema_valid_fast_path_keeps_logging_empty():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"value": {"type": "integer"}},
        "required": ["value"],
    }
    repaired, logs = repair_json('{"value": 1}', schema=schema, logging=True)
    assert repaired == {"value": 1}
    assert logs == []


def test_schema_unwraps_double_serialized_object_in_all_modes():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "summary": {
                "type": "object",
                "properties": {
                    "verdict": {"type": "string"},
                    "confidence": {"type": "string"},
                },
                "required": ["verdict", "confidence"],
            }
        },
        "required": ["summary"],
    }
    raw = '{"summary": "{\\"verdict\\": \\"malicious\\", \\"confidence\\": \\"high\\"}"}'
    expected = {"summary": {"verdict": "malicious", "confidence": "high"}}

    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="standard") == expected
    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="salvage") == expected

    repaired, logs = repair_json(raw, schema=schema, logging=True, schema_repair_mode="standard")
    assert repaired == expected
    assert any(log["text"] == "Unwrapped JSON string to object to match schema" for log in logs)


def test_schema_salvage_repairs_malformed_double_serialized_object_string():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "summary": {
                "type": "object",
                "properties": {
                    "verdict": {"type": "string"},
                    "confidence": {"type": "string"},
                },
                "required": ["verdict", "confidence"],
            }
        },
        "required": ["summary"],
    }
    raw = '{"summary": "{verdict: malicious, confidence: high}"}'
    expected = {"summary": {"verdict": "malicious", "confidence": "high"}}

    with pytest.raises(ValueError, match=r"Expected object at \$.summary, got str\."):
        repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="standard")

    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="salvage") == expected

    repaired, logs = repair_json(raw, schema=schema, logging=True, schema_repair_mode="salvage")
    assert repaired == expected
    assert any(log["text"] == "Repaired malformed JSON string to object to match schema" for log in logs)


def test_schema_unwraps_double_serialized_array_in_all_modes():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {"type": "string"},
            }
        },
        "required": ["items"],
    }
    raw = '{"items": "[\\"a\\", \\"b\\"]"}'
    expected = {"items": ["a", "b"]}

    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="standard") == expected
    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="salvage") == expected

    repaired, logs = repair_json(raw, schema=schema, logging=True, schema_repair_mode="standard")
    assert repaired == expected
    assert any(log["text"] == "Unwrapped JSON string to array to match schema" for log in logs)


def test_schema_salvage_repairs_malformed_double_serialized_array_string():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {"type": "string"},
            }
        },
        "required": ["items"],
    }
    raw = '{"items": "[a, b]"}'
    standard_expected = {"items": ["[a, b]"]}
    salvage_expected = {"items": ["a", "b"]}

    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="standard") == standard_expected
    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="salvage") == salvage_expected

    repaired, logs = repair_json(raw, schema=schema, logging=True, schema_repair_mode="salvage")
    assert repaired == salvage_expected
    assert any(log["text"] == "Repaired malformed JSON string to array to match schema" for log in logs)


def test_schema_object_string_unwrap_preserves_existing_failures():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "summary": {
                "type": "object",
                "properties": {"verdict": {"type": "string"}},
                "required": ["verdict"],
            }
        },
        "required": ["summary"],
    }

    with pytest.raises(ValueError, match=r"Expected object at \$.summary, got str\."):
        repair_json('{"summary": "not json"}', schema=schema, return_objects=True)

    with pytest.raises(ValueError, match=r"Expected object at \$.summary, got str\."):
        repair_json('{"summary": "[1, 2]"}', schema=schema, return_objects=True)


def test_schema_array_string_unwrap_preserves_existing_fallbacks():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {"type": "string"},
            }
        },
        "required": ["items"],
    }

    assert repair_json('{"items": "not json"}', schema=schema, return_objects=True) == {"items": ["not json"]}
    assert repair_json('{"items": "{\\"a\\": 1}"}', schema=schema, return_objects=True) == {"items": ['{"a": 1}']}
    assert repair_json('{"items": "{a: 1}"}', schema=schema, return_objects=True, schema_repair_mode="salvage") == {
        "items": ["{a: 1}"]
    }


def test_deep_allof_schema_raises_value_error_instead_of_recursion_error():
    pytest.importorskip("jsonschema")
    schema = {"type": "object", "properties": {"value": {"type": "string"}}}
    for _ in range(550):
        schema = {"allOf": [schema]}

    with pytest.raises(ValueError, match="supported schema recursion depth"):
        repair_json('{"value": "ok"}', schema=schema, return_objects=True)


def test_deep_properties_schema_raises_value_error_instead_of_recursion_error():
    pytest.importorskip("jsonschema")
    schema = {"type": "string"}
    for depth in range(550):
        schema = {"type": "object", "properties": {f"level_{depth}": schema}}

    with pytest.raises(ValueError, match="supported schema recursion depth"):
        repair_json("{}", schema=schema, return_objects=True)


def test_schema_applies_to_valid_json_fast_path_outputs_and_logging():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"value": {"type": "integer"}},
        "required": ["value"],
    }
    assert repair_json('{"value": "1"}', schema=schema) == '{"value": 1}'

    repaired, logs = repair_json('{"value": "1"}', schema=schema, logging=True)
    assert repaired == {"value": 1}
    assert logs


def test_schema_preserves_prefixed_valid_json_string_content():
    schema = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"text": {"type": "string"}, "id": {"type": "integer"}},
                    "required": ["text", "id"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["items"],
    }
    raw = 'Preamble\n{"items": [{"text": "a\\n, extra: 1", "id": 8}]}'

    assert repair_json(raw, schema=schema, return_objects=True) == {"items": [{"text": "a\n, extra: 1", "id": 8}]}


def test_schema_applies_to_valid_empty_string():
    pytest.importorskip("jsonschema")
    assert repair_json('""', schema={"type": "string"}) == ""


def test_schema_skip_json_loads_keeps_parser_path_for_scalars():
    pytest.importorskip("jsonschema")
    assert repair_json("True", schema={"type": "string"}, skip_json_loads=True, return_objects=True) == ""
    with pytest.raises(ValueError, match="is not of type"):
        repair_json('"1"', schema={"type": "integer"}, skip_json_loads=True, return_objects=True)


def test_schema_circular_ref_raises_definition_error():
    pytest.importorskip("jsonschema")
    schema = {
        "$ref": "#/definitions/a",
        "definitions": {
            "a": {"$ref": "#/definitions/a"},
        },
    }

    with pytest.raises(ValueError, match=r"Circular \$ref detected"):
        repair_json("{}", schema=schema, return_objects=True)


def test_schema_non_string_ref_raises_definition_error():
    pytest.importorskip("jsonschema")

    with pytest.raises(ValueError, match=r"\$ref must be a string"):
        repair_json("{}", schema={"$ref": 123}, return_objects=True)


def test_schema_pydantic_v2_defaults():
    pydantic = pytest.importorskip("pydantic")
    version = getattr(pydantic, "VERSION", getattr(pydantic, "__version__", "0"))
    if int(version.split(".")[0]) < 2:
        pytest.skip("pydantic v2 required")

    base_model = pydantic.BaseModel
    field = pydantic.Field

    class SchemaModel(base_model):
        evidence_types: list[str] = field(default_factory=list)

    raw = '{ "evidence_types": }'
    assert repair_with_schema(raw, SchemaModel) == {"evidence_types": []}


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ('{\n"a": "\n```{}```\n",\n"b": "x",\n}', {"a": "\n```{}```", "b": "x"}),
        ('{\n"a": "\n```{}```\n"\n",\n"b": "x",\n}', {"a": '\n```{}```\n"', "b": "x"}),
        ('{\n"a": "\n```{}```\n"\n",\n\'b\': "x",\n}', {"a": '\n```{}```\n"', "b": "x"}),
        ('{\n"a": "\n```{}```\n"\n", // c\n"b": "x",\n}', {"a": '\n```{}```\n"', "b": "x"}),
        ('{\n"a": "\n```{}```\n"\n",\n b: "x",\n}', {"a": '\n```{}```\n"', "b": "x"}),
        ('{"a":"```}```"a","b":"x"}', {"a": '```}```"a', "b": "x"}),
        ('{"a":"x}``` [1,2]\n","b":"y"}', {"a": "x}``` [1,2]", "b": "y"}),
        ('{"a":"x}``` [http://x]\n","b":"y"}', {"a": "x}``` [http://x]", "b": "y"}),
        ('{"a":"x}``` [foo[bar]\n","b":"y"}', {"a": "x}``` [foo[bar]", "b": "y"}),
        ('{"a":"x}``` [{\n","b":"y"}', {"a": "x}``` [{", "b": "y"}),
        ('{"a":"x}``` [foo, [bar]\n","b":"y"}', {"a": "x}``` [foo, [bar]", "b": "y"}),
        ('{"a":"x}``` [1,"z"]\n","b":"y"}', {"a": 'x}``` [1,"z"]', "b": "y"}),
        ('{"a":"x}``` [1, [2]]\n","b":"y"}', {"a": "x}``` [1, [2]]", "b": "y"}),
        ('{"a":"x}``` [1,[2],k:v]\n","b":"y"}', {"a": "x}``` [1,[2],k:v]", "b": "y"}),
        ('{"a":"x}``` (1,(2),k:v)\n","b":"y"}', {"a": "x}``` (1,(2),k:v)", "b": "y"}),
        ('{"a":"x}``` [1,2],\n","b":"y"}', {"a": "x}``` [1,2],", "b": "y"}),
        ('{"a":"x}``` // c\n [1,2]\n","b":"y"}', {"a": "x}``` // c\n [1,2]", "b": "y"}),
        ('{"a":"x}``` // c\n [1,2],\n","b":"y"}', {"a": "x}``` // c\n [1,2],", "b": "y"}),
        (
            '{\n"a": "\n```c\nint main() {\n}\n```\nImplementation: "xxx", xxx\n",\n"b": "x",\n}',
            {"a": '\n```c\nint main() {\n}\n```\nImplementation: "xxx", xxx', "b": "x"},
        ),
    ],
    ids=[
        "multiline-string",
        "stray-quote-line",
        "single-quoted-next-key",
        "comment-prefixed-next-key",
        "bare-next-key",
        "inline-quoted-prose",
        "inline-array-literal",
        "url-like-inline-array",
        "unmatched-inner-delimiter",
        "unbalanced-inline-array-like-prose",
        "unmatched-inner-delimiter-after-comma",
        "quoted-item-inline-array",
        "balanced-nested-inline-array",
        "nested-numeric-inline-array-with-bare-key-like-prose",
        "nested-numeric-parenthesized-value-with-bare-key-like-prose",
        "inline-array-with-trailing-comma",
        "comment-prefixed-inline-array",
        "comment-prefixed-inline-array-with-trailing-comma",
        "fenced-code-block-before-inline-quoted-prose",
    ],
)
def test_schema_pydantic_model_keeps_literal_fenced_snippet_cases(raw, expected):
    _assert_two_string_schema_repairs(raw, expected)


def test_schema_boolean_coercion_is_mode_independent():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"flag": {"type": "boolean"}},
        "required": ["flag"],
    }

    raw = '{"flag": "yes"}'
    default_mode = repair_json(raw, schema=schema, skip_json_loads=True, return_objects=True)
    standard_mode = repair_json(
        raw,
        schema=schema,
        skip_json_loads=True,
        return_objects=True,
        schema_repair_mode="standard",
    )
    salvage_mode = repair_json(
        raw,
        schema=schema,
        skip_json_loads=True,
        return_objects=True,
        schema_repair_mode="salvage",
    )
    assert default_mode == {"flag": True}
    assert standard_mode == {"flag": True}
    assert salvage_mode == {"flag": True}


def test_schema_boolean_coercion_accepts_number_tokens():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"flag": {"type": "boolean"}},
        "required": ["flag"],
    }
    assert repair_with_schema('{"flag": 1}', schema) == {"flag": True}
    assert repair_with_schema('{"flag": 0}', schema) == {"flag": False}
    assert repair_with_schema('{"flag": 1.0}', schema) == {"flag": True}
    assert repair_with_schema('{"flag": 0.0}', schema) == {"flag": False}


def test_schema_salvage_mode_drops_invalid_array_items():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "score": {"type": "number"},
                    },
                    "required": ["id", "score"],
                },
            }
        },
        "required": ["items"],
    }
    raw = '{"items":[{"id":1,"score":85.6},{"id":2,"score":"N/A"}]}'

    with pytest.raises(ValueError, match="Expected number"):
        repair_with_schema(raw, schema)

    repaired = repair_json(
        raw,
        schema=schema,
        skip_json_loads=True,
        return_objects=True,
        schema_repair_mode="salvage",
    )
    assert repaired == {"items": [{"id": 1, "score": 85.6}]}

    repaired_with_logs, logs = repair_json(
        raw,
        schema=schema,
        skip_json_loads=True,
        logging=True,
        schema_repair_mode="salvage",
    )
    assert repaired_with_logs == {"items": [{"id": 1, "score": 85.6}]}
    assert isinstance(logs, list)
    assert any(log["text"] == "Dropped invalid array item while salvaging" for log in logs)


def test_schema_salvage_mode_still_enforces_min_items():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "array",
        "items": {"type": "integer"},
        "minItems": 2,
    }
    with pytest.raises(ValueError, match="minItems"):
        repair_json(
            '["1", "bad"]',
            schema=schema,
            skip_json_loads=True,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_does_not_hide_schema_definition_errors():
    pytest.importorskip("jsonschema")
    schema = {"type": "array", "items": {"type": "bogus"}}
    with pytest.raises(ValueError, match="Unsupported schema type bogus"):
        repair_json(
            "[1]",
            schema=schema,
            skip_json_loads=True,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_maps_list_to_object_when_unambiguous():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "tags": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["name", "tags"],
    }
    raw = '["hello", ["a", "b"]]'

    with pytest.raises(ValueError, match="Expected object"):
        repair_json(raw, schema=schema, skip_json_loads=True, return_objects=True)

    assert repair_json(
        raw,
        schema=schema,
        skip_json_loads=True,
        return_objects=True,
        schema_repair_mode="salvage",
    ) == {"name": "hello", "tags": ["a", "b"]}


def test_schema_salvage_mode_maps_set_like_object_members_to_null_valued_keys():
    pytest.importorskip("jsonschema")
    schema = {"type": "object"}
    raw = '{"a", "b"}'

    with pytest.raises(ValueError, match="Expected object"):
        repair_json(raw, schema=schema, skip_json_loads=True, return_objects=True, schema_repair_mode="standard")

    assert repair_json(
        raw,
        schema=schema,
        skip_json_loads=True,
        return_objects=True,
        schema_repair_mode="salvage",
    ) == {"a": None, "b": None}
    assert (
        repair_json(
            raw,
            schema=schema,
            skip_json_loads=True,
            schema_repair_mode="salvage",
        )
        == '{"a": null, "b": null}'
    )

    repaired_with_logs, logs = cast(
        "tuple[object, list[dict[str, str]]]",
        repair_json(
            raw,
            schema=schema,
            skip_json_loads=True,
            logging=True,
            schema_repair_mode="salvage",
        ),
    )
    assert repaired_with_logs == {"a": None, "b": None}
    assert any("set-like members as null-valued object keys" in log["text"] for log in logs)


def test_schema_salvage_mode_set_like_members_do_not_override_mixed_object_array_schema():
    pytest.importorskip("jsonschema")
    schema = {"type": ["object", "array"], "items": {"type": "string"}}
    raw = '{"a", "b"}'

    assert repair_json(
        raw,
        schema=schema,
        skip_json_loads=True,
        return_objects=True,
        schema_repair_mode="salvage",
    ) == ["a", "b"]


def test_schema_salvage_mode_set_like_members_still_fail_incompatible_object_schema():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"count": {"type": "integer"}},
        "required": ["count"],
    }
    raw = '{"a", "b"}'

    with pytest.raises(ValueError, match="Missing required properties"):
        repair_json(
            raw,
            schema=schema,
            skip_json_loads=True,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_set_like_members_require_string_keys():
    pytest.importorskip("jsonschema")
    schema = {"type": "object"}
    raw = "{1, 2}"

    with pytest.raises(ValueError, match="Expected object"):
        repair_json(
            raw,
            schema=schema,
            skip_json_loads=True,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_mapping_rejects_length_mismatch():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "tags": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["name", "tags"],
    }
    with pytest.raises(ValueError, match="Expected object"):
        repair_json(
            '["hello"]',
            schema=schema,
            skip_json_loads=True,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_mapping_rejects_type_mismatch():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "tags": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["name", "tags"],
    }
    with pytest.raises(ValueError, match="Expected object"):
        repair_json(
            '[["a", "b"], "hello"]',
            schema=schema,
            skip_json_loads=True,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_union_object_array_falls_back_to_valid_array_branch():
    pytest.importorskip("jsonschema")
    schema = {
        "type": ["object", "array"],
        "properties": {"name": {"type": "string", "pattern": "^a+$"}},
        "required": ["name"],
        "items": {"type": "string"},
    }
    raw = '["bbb",]'

    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="standard") == ["bbb"]
    assert repair_json(raw, schema=schema, return_objects=True, schema_repair_mode="salvage") == ["bbb"]


def test_schema_salvage_mode_union_object_array_does_not_remap_valid_array():
    pytest.importorskip("jsonschema")
    schema = {
        "type": ["object", "array"],
        "properties": {"x": {"type": "integer"}, "y": {"type": "integer"}},
        "required": ["x", "y"],
        "items": {"type": "integer"},
    }
    raw = "[1,2]"

    assert repair_json(
        raw,
        schema=schema,
        skip_json_loads=True,
        return_objects=True,
        schema_repair_mode="salvage",
    ) == [1, 2]

    repaired_with_logs, logs = cast(
        "tuple[object, list[dict[str, str]]]",
        repair_json(
            raw,
            schema=schema,
            skip_json_loads=True,
            logging=True,
            schema_repair_mode="salvage",
        ),
    )
    assert repaired_with_logs == [1, 2]
    assert not any(
        log["text"]
        in {
            "Mapped array to object by schema property order",
            "Unwrapped single-item root array to object while salvaging",
        }
        for log in logs
    )


def test_schema_salvage_mode_unwraps_root_single_item_array_and_fills_required_array():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "type": {"const": "food_sport_card"},
            "content": {
                "type": "object",
                "required": ["food", "sports"],
                "properties": {
                    "food": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "sports": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
            },
        },
        "required": ["type", "content"],
    }
    raw = """[
    {
        "type": "food_sport_card",
        "content": {
            "food": [
                "mantou"
            ]
        }
    }
"""

    with pytest.raises(ValueError, match=r"Expected object at \$, got list\."):
        repair_json(
            raw,
            schema=schema,
            return_objects=True,
            schema_repair_mode="standard",
        )

    assert repair_json(
        raw,
        schema=schema,
        return_objects=True,
        schema_repair_mode="salvage",
    ) == {
        "type": "food_sport_card",
        "content": {"food": ["mantou"], "sports": []},
    }

    repaired_with_logs, logs = cast(
        "tuple[object, list[dict[str, str]]]",
        repair_json(
            raw,
            schema=schema,
            logging=True,
            schema_repair_mode="salvage",
        ),
    )
    assert repaired_with_logs == {
        "type": "food_sport_card",
        "content": {"food": ["mantou"], "sports": []},
    }
    assert any(log["text"] == "Unwrapped single-item root array to object while salvaging" for log in logs)
    assert any(
        log["text"] == "Filled missing required property while salvaging" and log["context"] == "$.content.sports"
        for log in logs
    )


def test_schema_salvage_mode_fills_required_with_safe_inference_sources():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {
            "from_default": {"default": "x"},
            "from_const": {"const": 7},
            "from_enum": {"enum": ["first", "second"]},
            "from_array_shape": {"items": {"type": "integer"}},
            "from_object_shape": {"properties": {"nested": {"type": "string"}}},
        },
        "required": [
            "from_default",
            "from_const",
            "from_enum",
            "from_array_shape",
            "from_object_shape",
        ],
    }
    assert repair_json(
        "{}",
        schema=schema,
        return_objects=True,
        schema_repair_mode="salvage",
    ) == {
        "from_default": "x",
        "from_const": 7,
        "from_enum": "first",
        "from_array_shape": [],
        "from_object_shape": {},
    }


def test_schema_salvage_mode_missing_required_without_property_schema_still_raises():
    pytest.importorskip("jsonschema")
    schema = {"type": "object", "properties": {}, "required": ["missing"]}
    with pytest.raises(ValueError, match="Missing required properties"):
        repair_json(
            "{}",
            schema=schema,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_missing_required_boolean_schema_still_raises():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"payload": True},
        "required": ["payload"],
    }
    with pytest.raises(ValueError, match="Missing required properties"):
        repair_json(
            "{}",
            schema=schema,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_root_unwrap_requires_single_item():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"value": {"type": "integer"}},
        "required": ["value"],
    }
    with pytest.raises(ValueError, match=r"Expected object at \$, got list\."):
        repair_json(
            '[{"value": 1}, {"value": 2}]',
            schema=schema,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_missing_required_scalar_still_raises():
    pytest.importorskip("jsonschema")
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}},
        "required": ["name"],
    }
    with pytest.raises(ValueError, match="Missing required properties"):
        repair_json(
            "[{}]",
            schema=schema,
            return_objects=True,
            schema_repair_mode="salvage",
        )


def test_schema_salvage_mode_requires_schema():
    with pytest.raises(ValueError, match="schema_repair_mode"):
        repair_json("{}", return_objects=True, schema_repair_mode="salvage")

```

### `tests/test_schema_parser_paths.py`

```py
import pytest

from src.json_repair import repair_json
from src.json_repair.json_parser import JSONParser
from src.json_repair.schema_repair import SchemaRepairer
from src.json_repair.utils.json_context import ContextValues


def parse_object_direct(raw, schema, *, strict=False, context=None):
    parser = JSONParser(raw, None, False, 0, False, strict)
    repairer = SchemaRepairer(schema if isinstance(schema, dict) else {}, None)
    parser.schema_repairer = repairer
    if context is not None:
        parser.context.set(context)
    parser.index = 1
    return parser.parse_object(schema, "$")


def parse_object_direct_with_mode(raw, schema, mode, *, strict=False, context=None):
    parser = JSONParser(raw, None, False, 0, False, strict)
    repairer = SchemaRepairer(schema if isinstance(schema, dict) else {}, None, schema_repair_mode=mode)
    parser.schema_repairer = repairer
    if context is not None:
        parser.context.set(context)
    parser.index = 1
    return parser.parse_object(schema, "$")


def parse_array_direct(raw, schema):
    parser = JSONParser(raw, None, False, 0, False, False)
    repairer = SchemaRepairer(schema if isinstance(schema, dict) else {}, None)
    parser.schema_repairer = repairer
    parser.index = 1
    return parser.parse_array(schema, "$")


def parse_array_direct_with_mode(raw, schema, mode):
    parser = JSONParser(raw, None, False, 0, False, False)
    repairer = SchemaRepairer(schema if isinstance(schema, dict) else {}, None, schema_repair_mode=mode)
    parser.schema_repairer = repairer
    parser.index = 1
    return parser.parse_array(schema, "$")


def test_parse_object_schema_true_false_and_non_object():
    assert parse_object_direct("{}", True) == {}
    with pytest.raises(ValueError, match="Schema does not allow"):
        parse_object_direct("{}", False)
    assert parse_object_direct("{}", {"type": "string"}) == {}


def test_parse_object_schema_property_fallbacks_and_stray_colon():
    schema = {
        "type": "object",
        "properties": [],
        "patternProperties": [],
        "additionalProperties": True,
    }
    assert parse_object_direct("{:a:1}", schema) == {"a": 1}


def test_parse_object_schema_invalid_property_schema_raises():
    schema = {"type": "object", "properties": {"a": "nope"}}
    with pytest.raises(ValueError, match="Schema must be an object"):
        parse_object_direct('{"a": 1}', schema)


def test_parse_object_schema_invalid_pattern_schema_raises():
    schema = {"type": "object", "patternProperties": {"^a": "nope"}}
    with pytest.raises(ValueError, match="Schema must be an object"):
        parse_object_direct('{"a": 1}', schema)


def test_parse_object_schema_invalid_pattern_extra_schema_raises():
    schema = {
        "type": "object",
        "patternProperties": {"^a": {"type": "integer"}, "a$": "nope"},
    }
    with pytest.raises(ValueError, match="Schema must be an object"):
        parse_object_direct('{"a": 1}', schema)


def test_parse_array_schema_missing_object_brace():
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {"a": {"type": "integer"}},
            "required": ["a"],
        },
    }
    assert repair_json('["a": 1]', schema=schema, skip_json_loads=True, return_objects=True) == [{"a": 1}]


def test_parse_object_schema_pattern_extra_schemas():
    schema = {
        "type": "object",
        "patternProperties": {
            "^x": {"type": "integer"},
            "1$": {"type": "integer"},
        },
    }
    assert repair_json('{"x1": "2"}', schema=schema, skip_json_loads=True, return_objects=True) == {"x1": 2}


def test_parse_object_schema_skips_unsupported_pattern_regex_with_log():
    schema = {
        "type": "object",
        "patternProperties": {"^x[0-9]+$": {"type": "integer"}},
        "additionalProperties": True,
    }
    parser = JSONParser('{"x1": 2}', None, True, 0, False, False)
    repairer = SchemaRepairer(schema, parser.logger)
    parser.schema_repairer = repairer
    parser.index = 1

    assert parser.parse_object(schema, "$") == {"x1": 2}
    assert any("Skipped unsupported patternProperties regex '^x[0-9]+$'" in entry["text"] for entry in parser.logger)


def test_parse_object_schema_drop_property_and_additional_schema():
    schema_drop = {
        "type": "object",
        "properties": {"a": {"type": "integer"}},
        "additionalProperties": False,
    }
    assert repair_json('{"a": 1, "extra": "drop"}', schema=schema_drop, skip_json_loads=True, return_objects=True) == {
        "a": 1
    }

    schema_extra = {
        "type": "object",
        "additionalProperties": {"type": "integer"},
    }
    assert repair_json('{"a": "2"}', schema=schema_extra, skip_json_loads=True, return_objects=True) == {"a": 2}


def test_parse_object_schema_closing_array_bracket_and_extra_brace():
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {"a": {"type": "integer"}},
            "required": ["a"],
        },
    }
    assert repair_json('[{"a": 1]', schema=schema, skip_json_loads=True, return_objects=True) == [{"a": 1}]

    schema_obj = {"type": "object", "additionalProperties": True}
    parser = JSONParser('{"a": 1}}', None, False, 0, False, False)
    repairer = SchemaRepairer(schema_obj, None)
    parser.schema_repairer = repairer
    parser.context.set(ContextValues.ARRAY)
    parser.index = 1
    assert parser.parse_object(schema_obj, "$") == {"a": 1}


def test_parse_object_schema_empty_object_falls_back_to_array():
    schema = {"type": "object", "additionalProperties": True}
    assert parse_object_direct("{,,}", schema) == []


def test_parse_object_schema_salvage_set_literal_keeps_non_string_members_as_array():
    schema = {"type": "object"}
    assert parse_object_direct_with_mode("{1, 2}", schema, "salvage") == [1, 2]


def test_parse_array_schema_true_false_and_non_array():
    assert parse_array_direct("[1]", True) == [1]
    with pytest.raises(ValueError, match="Schema does not allow"):
        parse_array_direct("[1]", False)
    assert parse_array_direct("[1]", {"type": "object"}) == [1]


def test_parse_array_schema_items_and_additional_items():
    schema_drop = {"type": "array", "items": [{"type": "integer"}], "additionalItems": False}
    assert parse_array_direct("[1, 2]", schema_drop) == [1]

    schema_extra = {
        "type": "array",
        "items": [{"type": "integer"}],
        "additionalItems": {"type": "integer"},
    }
    assert parse_array_direct('[1, "2"]', schema_extra) == [1, 2]

    schema_open = {
        "type": "array",
        "items": [{"type": "integer"}],
        "additionalItems": True,
    }
    assert parse_array_direct('[1, "x"]', schema_open) == [1, "x"]

    schema_items = {"type": "array", "items": {"type": "integer"}}
    assert parse_array_direct('["1"]', schema_items) == [1]

    schema_any = {"type": "array"}
    assert parse_array_direct("[true]", schema_any) == [True]


def test_parse_array_schema_invalid_items_schema_raises():
    schema = {"type": "array", "items": ["nope"]}
    with pytest.raises(ValueError, match="Schema must be an object"):
        parse_array_direct("[1]", schema)


def test_parse_json_with_schema_branches():
    schema = {"type": "array", "items": {"type": "integer"}}
    parser = JSONParser("[1]", None, False, 0, False, False)
    repairer = SchemaRepairer(schema, None)
    parser.schema_repairer = repairer
    assert parser.parse_json(schema, "$") == [1]

    parser = JSONParser('"1"', None, False, 0, False, False)
    parser.schema_repairer = repairer
    parser.context.set(ContextValues.ARRAY)
    assert parser.parse_json({"type": "integer"}, "$") == 1

    parser = JSONParser("1", None, False, 0, False, False)
    parser.schema_repairer = repairer
    parser.context.set(ContextValues.ARRAY)
    assert parser.parse_json({"type": "integer"}, "$") == 1

    parser = JSONParser("# comment", None, False, 0, False, False)
    parser.schema_repairer = repairer
    assert parser.parse_json({"type": "string"}, "$") == ""

    parser = JSONParser("", None, False, 0, False, False)
    parser.schema_repairer = repairer
    assert parser.parse_json({"type": "string"}, "$") == ""

    parser = JSONParser('"x"', None, False, 0, False, False)
    parser.schema_repairer = repairer
    parser.context.set(ContextValues.ARRAY)
    assert parser.parse_json(True, "$") == "x"
    with pytest.raises(ValueError, match="Schema does not allow"):
        parser.parse_json(False, "$")

    parser = JSONParser('@{"a": 1}', None, False, 0, False, False)
    parser.schema_repairer = SchemaRepairer({"type": "object"}, None)
    assert parser.parse_json({"type": "object"}, "$") == {"a": 1}


def test_schema_ref_to_true_short_circuits():
    schema = {"flag": True}
    repairer = SchemaRepairer(schema, None)

    parser = JSONParser("[1]", None, False, 0, False, False)
    parser.schema_repairer = repairer
    parser.index = 1
    assert parser.parse_array({"$ref": "#/flag"}, "$") == [1]

    parser = JSONParser('{"a": 1}', None, False, 0, False, False)
    parser.schema_repairer = repairer
    parser.index = 1
    assert parser.parse_object({"$ref": "#/flag"}, "$") == {"a": 1}

    parser = JSONParser("1", None, False, 0, False, False)
    parser.schema_repairer = repairer
    parser.context.set(ContextValues.ARRAY)
    assert parser.parse_json({"$ref": "#/flag"}, "$") == 1


def test_parse_array_salvage_mode_parses_even_when_item_schema_would_fail():
    schema = {"type": "array", "items": {"type": "integer"}}
    # In salvage mode parse_array should not fail early on schema mismatch.
    assert parse_array_direct_with_mode('["bad", "2"]', schema, "salvage") == ["bad", "2"]


def test_parse_array_salvage_mode_keeps_object_heuristic_values():
    schema = {"type": "array", "items": {"type": "object", "properties": {"a": {"type": "integer"}}}}
    # In salvage mode, string+colon heuristic should still parse and keep the object value.
    assert parse_array_direct_with_mode('["a": 1]', schema, "salvage") == [{"a": 1}]

```

### `tests/test_schema_repairer.py`

```py
import copy
from typing import Any, ClassVar

import pytest

from src.json_repair import repair_json
from src.json_repair.schema_repair import (
    SchemaRepairer,
    load_schema_model,
    normalize_missing_values,
    normalize_schema_repair_mode,
    schema_from_input,
)
from src.json_repair.utils.constants import MISSING_VALUE


def test_missing_value_deepcopy():
    assert copy.deepcopy(MISSING_VALUE) is MISSING_VALUE


def test_normalize_missing_values_nested_and_invalid():
    assert normalize_missing_values(MISSING_VALUE) == ""
    assert normalize_missing_values({"a": MISSING_VALUE, "b": [MISSING_VALUE, 1]}) == {"a": "", "b": ["", 1]}
    with pytest.raises(ValueError, match="Object keys must be strings"):
        normalize_missing_values({1: "a"})
    with pytest.raises(ValueError, match="JSON compatible"):
        normalize_missing_values(object())


def test_load_schema_model_errors_and_success(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="Schema model must be in the form"):
        load_schema_model("invalid")

    module_path = tmp_path / "schema_mod.py"
    module_path.write_text("class SchemaModel:\n    pass\n")
    monkeypatch.syspath_prepend(tmp_path)

    assert load_schema_model("schema_mod:SchemaModel").__name__ == "SchemaModel"
    with pytest.raises(ValueError, match="not found"):
        load_schema_model("schema_mod:Missing")


def test_schema_from_input_basic_and_invalid():
    assert schema_from_input({"type": "string"}) == {"type": "string"}
    assert schema_from_input(True) is True
    assert schema_from_input(False) is False
    with pytest.raises(ValueError, match="Schema must be a JSON Schema"):
        schema_from_input(1)


def test_schema_repair_mode_validation():
    assert normalize_schema_repair_mode(None) == "standard"
    assert normalize_schema_repair_mode("standard") == "standard"
    assert normalize_schema_repair_mode("salvage") == "salvage"
    with pytest.raises(ValueError, match="schema_repair_mode"):
        normalize_schema_repair_mode("unknown")


def test_schema_from_input_model_defaults_and_required():
    pydantic = pytest.importorskip("pydantic")
    version = getattr(pydantic, "VERSION", getattr(pydantic, "__version__", "0"))
    if int(version.split(".")[0]) < 2:
        pytest.skip("pydantic v2 required")

    class DummyField:
        def __init__(self, default, default_factory=None, required=False):
            self.default = default
            self.default_factory = default_factory
            self._required = required

        def is_required(self):
            return self._required

    class DummyModel:
        @staticmethod
        def model_json_schema():
            return {"properties": {"name": "not-a-dict"}}

        model_fields: ClassVar[dict[str, DummyField]] = {
            "name": DummyField(default="x"),
            "items": DummyField(default=None, default_factory=lambda: ["a"]),
            "required_field": DummyField(default="y", required=True),
        }

    schema = schema_from_input(DummyModel)
    assert isinstance(schema, dict)
    assert schema["properties"]["name"]["default"] == "x"
    assert schema["properties"]["items"]["default"] == ["a"]
    assert "required_field" not in schema["properties"]

    class DummyModelWithDefaults:
        @staticmethod
        def model_json_schema():
            return {"properties": {"name": {"default": "keep"}}}

        model_fields: ClassVar[dict[str, DummyField]] = {"name": DummyField(default="x")}

    schema_with_default = schema_from_input(DummyModelWithDefaults)
    assert isinstance(schema_with_default, dict)
    assert schema_with_default["properties"]["name"]["default"] == "keep"


def test_schema_from_input_non_dict_properties():
    pydantic = pytest.importorskip("pydantic")
    version = getattr(pydantic, "VERSION", getattr(pydantic, "__version__", "0"))
    if int(version.split(".")[0]) < 2:
        pytest.skip("pydantic v2 required")

    class DummyField:
        def __init__(self, default):
            self.default = default
            self.default_factory = None

        def is_required(self):
            return False

    class DummyModel:
        @staticmethod
        def model_json_schema():
            return {"properties": []}

        model_fields: ClassVar[dict[str, DummyField]] = {"value": DummyField(default=1)}

    schema = schema_from_input(DummyModel)
    assert isinstance(schema, dict)
    assert schema["properties"]["value"]["default"] == 1


def test_schema_from_input_requires_pydantic_v2(monkeypatch):
    pydantic = pytest.importorskip("pydantic")
    monkeypatch.setattr(pydantic, "VERSION", "1.0")

    class DummyModel:
        @staticmethod
        def model_json_schema():
            return {}

    with pytest.raises(ValueError, match="pydantic v2"):
        schema_from_input(DummyModel)


def test_schema_repairer_validate_and_prepare():
    pytest.importorskip("jsonschema")
    repairer = SchemaRepairer({}, [])
    assert repairer.is_valid(1, True) is True
    assert repairer.is_valid(1, False) is False
    repairer.validate(1, True)
    with pytest.raises(ValueError, match="Schema does not allow"):
        repairer.validate(1, False)
    integer_schema = {"type": "integer"}
    repairer.validate(1, integer_schema)
    assert repairer._get_validator(integer_schema) is repairer._get_validator(integer_schema)
    repairer.is_valid(1, integer_schema)
    repairer.is_valid(2, integer_schema)
    assert len(repairer._validator_cache) == 1
    with pytest.raises(ValueError, match="is not of type"):
        repairer.validate("x", {"type": "integer"})

    schema = {
        "type": "array",
        "items": [{"type": "integer"}, {"type": "string"}],
        "additionalItems": False,
    }
    repairer.validate([1, "a"], schema)
    prepared = repairer._prepare_schema_for_validation(schema)
    assert prepared["prefixItems"]
    assert prepared["items"] is False

    schema2 = {
        "items": [{"type": "integer"}],
        "additionalItems": {"type": "string"},
    }
    prepared2 = repairer._prepare_schema_for_validation(schema2)
    assert prepared2["items"] == {"type": "string"}

    invalid_schema: Any = True
    with pytest.raises(ValueError, match="Schema must be an object"):
        repairer._prepare_schema_for_validation(invalid_schema)


def test_schema_repairer_resolve_schema_and_refs():
    root = {"defs": {"node": {"type": "string"}}, "flag": True, "flag_false": False, "bad": 1}
    repairer = SchemaRepairer(root, None)
    assert repairer.resolve_schema(None) is True
    assert repairer.resolve_schema(False) is False
    assert repairer.resolve_schema({"$ref": "#/defs/node"}) == {"type": "string"}
    assert repairer.resolve_schema({"$ref": "#/flag"}) is True
    assert repairer.resolve_schema({"$ref": "#/flag_false"}) is False
    invalid_schema: Any = "nope"
    with pytest.raises(ValueError, match="Schema must be an object"):
        repairer.resolve_schema(invalid_schema)
    with pytest.raises(ValueError, match="Schema keys must be strings"):
        repairer.resolve_schema({1: "bad"})

    with pytest.raises(ValueError, match="Unsupported \\$ref"):
        repairer._resolve_ref("http://example.com")
    with pytest.raises(ValueError, match="Unresolvable \\$ref"):
        repairer._resolve_ref("#/missing")
    with pytest.raises(ValueError, match="Unresolvable \\$ref"):
        repairer._resolve_ref("#/bad")


def test_schema_repairer_copy_json_value_edges():
    repairer = SchemaRepairer({}, [])
    assert repairer._copy_json_value({"a": {"b": 1}}, "$", "default") == {"a": {"b": 1}}
    with pytest.raises(ValueError, match="non-string key"):
        repairer._copy_json_value({1: "a"}, "$", "default")
    with pytest.raises(ValueError, match="not JSON compatible"):
        repairer._copy_json_value(object(), "$", "default")


def test_schema_repairer_object_and_array_helpers():
    repairer = SchemaRepairer({}, None)
    assert repairer.is_object_schema({"type": "object"}) is True
    assert repairer.is_object_schema({"type": ["null", "object"]}) is True
    assert repairer.is_object_schema({"properties": {}}) is True
    assert repairer.is_object_schema({"type": "string"}) is False

    assert repairer.is_array_schema({"type": "array"}) is True
    assert repairer.is_array_schema({"type": ["array", "null"]}) is True
    assert repairer.is_array_schema({"items": {"type": "string"}}) is True
    assert repairer.is_array_schema({"type": "object"}) is False

    assert repairer.is_object_schema(True) is False
    assert repairer.is_array_schema(False) is False


def test_repair_value_missing_and_unions():
    repairer = SchemaRepairer({}, [])
    assert repairer.repair_value(MISSING_VALUE, {"const": 1}, "$") == 1
    assert repairer.repair_value(MISSING_VALUE, {"enum": [2, 3]}, "$") == 2
    assert repairer.repair_value(MISSING_VALUE, {"default": "x"}, "$") == "x"
    assert repairer.repair_value(MISSING_VALUE, {"type": "string"}, "$") == ""

    schema_any = {"anyOf": [{"type": "integer"}, {"type": "string"}]}
    assert repairer.repair_value("1", schema_any, "$") == 1

    schema_one = {"oneOf": [{"type": "integer"}, {"type": "boolean"}]}
    with pytest.raises(ValueError, match="Expected boolean"):
        repairer.repair_value("nope", schema_one, "$")

    schema_all = {"allOf": [{"type": "string"}, {"enum": ["a"]}]}
    assert repairer.repair_value("a", schema_all, "$") == "a"
    with pytest.raises(ValueError, match="does not match enum"):
        repairer.repair_value("b", schema_all, "$")

    schema_union = {"type": ["integer", "string"]}
    assert repairer.repair_value("2", schema_union, "$") == 2

    with pytest.raises(ValueError, match="No schema matched"):
        repairer.repair_value("x", {"oneOf": []}, "$")
    with pytest.raises(ValueError, match="Expected boolean"):
        repairer.repair_value("x", {"type": ["integer", "boolean"]}, "$")
    with pytest.raises(ValueError, match="No schema type matched"):
        repairer.repair_value("x", {"type": []}, "$")

    schema_array_union = {"type": ["array", "string"], "items": {"type": "integer"}}
    assert repairer.repair_value(["1"], schema_array_union, "$") == [1]
    schema_obj_union = {"type": ["object", "string"], "properties": {"a": {"type": "integer"}}}
    assert repairer.repair_value({"a": "1"}, schema_obj_union, "$") == {"a": 1}


def test_type_union_validates_branch_before_returning():
    pytest.importorskip("jsonschema")
    standard_repairer = SchemaRepairer({}, [])
    salvage_repairer = SchemaRepairer({}, [], schema_repair_mode="salvage")
    schema = {
        "type": ["object", "array"],
        "properties": {"name": {"type": "string", "pattern": "^a+$"}},
        "required": ["name"],
        "items": {"type": "string"},
    }
    assert standard_repairer.repair_value(["bbb"], schema, "$") == ["bbb"]
    assert salvage_repairer.repair_value(["bbb"], schema, "$") == ["bbb"]


def test_salvage_skips_object_mapping_for_mixed_object_array_schema():
    pytest.importorskip("jsonschema")
    salvage_repairer = SchemaRepairer({}, [], schema_repair_mode="salvage")
    schema = {
        "type": ["object", "array"],
        "properties": {"x": {"type": "integer"}, "y": {"type": "integer"}},
        "required": ["x", "y"],
        "items": {"type": "integer"},
    }
    assert salvage_repairer.repair_value([1, 2], schema, "$") == [1, 2]


def test_can_salvage_list_as_object_requires_object_without_array():
    repairer = SchemaRepairer({}, [], schema_repair_mode="salvage")
    assert repairer._can_salvage_list_as_object({"properties": {"a": {"type": "integer"}}}) is True
    assert repairer._can_salvage_list_as_object({"items": {"type": "integer"}}) is False
    assert (
        repairer._can_salvage_list_as_object({"properties": {"a": {"type": "integer"}}, "items": {"type": "integer"}})
        is False
    )


def test_repair_object_and_array_paths():
    repairer = SchemaRepairer({}, [])
    schema_obj = {
        "type": "object",
        "properties": {
            "a": {"type": "integer"},
            "b": {"type": "string", "default": "x"},
        },
        "required": ["a"],
        "patternProperties": {
            "^x": {"type": "integer"},
            "1$": {"type": "integer"},
        },
        "additionalProperties": False,
    }
    value = {"a": "1", "x1": "2", "extra": "drop"}
    assert repairer.repair_value(value, schema_obj, "$") == {"a": 1, "b": "x", "x1": 2}
    with pytest.raises(ValueError, match="Missing required properties"):
        repairer.repair_value({}, schema_obj, "$")

    schema_obj_extra = {"type": "object", "additionalProperties": {"type": "integer"}}
    assert repairer.repair_value({"a": "1"}, schema_obj_extra, "$") == {"a": 1}

    schema_min_props = {"type": "object", "minProperties": 1}
    with pytest.raises(ValueError, match="minProperties"):
        repairer.repair_value({}, schema_min_props, "$")

    schema_bad_props = {"type": "object", "properties": [], "patternProperties": []}
    assert repairer.repair_value({}, schema_bad_props, "$") == {}
    with pytest.raises(ValueError, match="Expected object"):
        repairer.repair_value([], {"type": "object"}, "$")

    schema_array = {
        "type": "array",
        "items": [{"type": "integer"}],
        "additionalItems": False,
    }
    assert repairer.repair_value([1, 2], schema_array, "$") == [1]
    schema_tuple = {"type": "array", "items": [{"type": "integer"}, {"type": "string"}]}
    assert repairer.repair_value([1], schema_tuple, "$") == [1]

    schema_array_extra = {
        "type": "array",
        "items": [{"type": "integer"}],
        "additionalItems": {"type": "string"},
    }
    assert repairer.repair_value([1, 2], schema_array_extra, "$") == [1, "2"]

    schema_array_open = {
        "type": "array",
        "items": [{"type": "integer"}],
        "additionalItems": True,
    }
    assert repairer.repair_value([1, "x"], schema_array_open, "$") == [1, "x"]

    schema_array_items = {"type": "array", "items": {"type": "integer"}}
    assert repairer.repair_value(["1", 2], schema_array_items, "$") == [1, 2]
    with pytest.raises(ValueError, match="Expected integer"):
        repairer.repair_value(["bad"], schema_array_items, "$")

    schema_array_wrap = {"type": "array"}
    assert repairer.repair_value("a", schema_array_wrap, "$") == ["a"]

    schema_min_items = {"type": "array", "minItems": 1}
    with pytest.raises(ValueError, match="minItems"):
        repairer.repair_value([], schema_min_items, "$")

    schema_tuple_invalid = {"type": "array", "items": [{"type": "integer"}]}
    with pytest.raises(ValueError, match="Expected integer"):
        repairer.repair_value(["bad"], schema_tuple_invalid, "$")

    schema_additional_invalid = {
        "type": "array",
        "items": [{"type": "integer"}],
        "additionalItems": {"type": "integer"},
    }
    with pytest.raises(ValueError, match="Expected integer"):
        repairer.repair_value([1, "bad"], schema_additional_invalid, "$")

    salvage_repairer = SchemaRepairer({}, [], schema_repair_mode="salvage")
    assert salvage_repairer._map_list_to_object([1], {"type": "object"}, "$") is None
    assert salvage_repairer.repair_value(["bad"], schema_tuple_invalid, "$") == []
    assert salvage_repairer.repair_value([1, "bad"], schema_additional_invalid, "$") == [1]
    with pytest.raises(ValueError, match="Unsupported schema type bogus"):
        salvage_repairer.repair_value([1], {"type": "array", "items": [{"type": "bogus"}]}, "$")
    with pytest.raises(ValueError, match="Unsupported schema type bogus"):
        salvage_repairer.repair_value(
            [1, 2],
            {
                "type": "array",
                "items": [{"type": "integer"}],
                "additionalItems": {"type": "bogus"},
            },
            "$",
        )
    with pytest.raises(ValueError, match="Unsupported schema type bogus"):
        salvage_repairer._map_list_to_object([1], {"type": "object", "properties": {"a": {"type": "bogus"}}}, "$")
    with pytest.raises(ValueError, match="property names must be strings"):
        salvage_repairer._map_list_to_object([1], {"type": "object", "properties": {1: {"type": "integer"}}}, "$")


def test_fill_missing_and_coerce_scalar_paths():
    repairer = SchemaRepairer({}, [])
    assert repairer._fill_missing({"type": "integer"}, "$") == 0
    assert repairer._fill_missing({"type": "number"}, "$") == 0
    assert repairer._fill_missing({"type": "boolean"}, "$") is False
    assert repairer._fill_missing({"type": "null"}, "$") is None
    assert repairer._fill_missing({"type": "array"}, "$") == []
    assert repairer._fill_missing({"type": "object"}, "$") == {}
    assert repairer._fill_missing({"type": ["string", "integer"]}, "$") == ""
    assert repairer._fill_missing({"properties": {"a": {"type": "string"}}}, "$") == {}
    assert repairer._fill_missing({"items": {"type": "string"}}, "$") == []
    with pytest.raises(ValueError, match="requires at least"):
        repairer._fill_missing({"type": "array", "minItems": 1}, "$")
    with pytest.raises(ValueError, match="requires at least"):
        repairer._fill_missing({"type": "object", "minProperties": 1}, "$")
    with pytest.raises(ValueError, match="Cannot infer missing value"):
        repairer._fill_missing({"type": "custom"}, "$")
    with pytest.raises(ValueError, match="has no values"):
        repairer._fill_missing({"enum": []}, "$")
    with pytest.raises(ValueError, match="Cannot infer missing value"):
        repairer._fill_missing({"type": ["unsupported"]}, "$")

    assert repairer._coerce_scalar(1, "string", "$") == "1"
    assert repairer._coerce_scalar("2", "integer", "$") == 2
    assert repairer._coerce_scalar("2.0", "integer", "$") == 2
    assert repairer._coerce_scalar(2.0, "integer", "$") == 2
    assert repairer._coerce_scalar("2.5", "number", "$") == 2.5
    assert repairer._coerce_scalar("true", "boolean", "$") is True
    assert repairer._coerce_scalar("false", "boolean", "$") is False
    assert repairer._coerce_scalar("yes", "boolean", "$") is True
    assert repairer._coerce_scalar("no", "boolean", "$") is False
    assert repairer._coerce_scalar("y", "boolean", "$") is True
    assert repairer._coerce_scalar("n", "boolean", "$") is False
    assert repairer._coerce_scalar("on", "boolean", "$") is True
    assert repairer._coerce_scalar("off", "boolean", "$") is False
    assert repairer._coerce_scalar("1", "boolean", "$") is True
    assert repairer._coerce_scalar("0", "boolean", "$") is False
    assert repairer._coerce_scalar(1, "boolean", "$") is True
    assert repairer._coerce_scalar(0, "boolean", "$") is False
    assert repairer._coerce_scalar(1.0, "boolean", "$") is True
    assert repairer._coerce_scalar(0.0, "boolean", "$") is False
    assert repairer._coerce_scalar(None, "null", "$") is None

    with pytest.raises(ValueError, match="Expected string"):
        repairer._coerce_scalar(True, "string", "$")
    with pytest.raises(ValueError, match="Expected integer"):
        repairer._coerce_scalar(True, "integer", "$")
    with pytest.raises(ValueError, match="Expected integer"):
        repairer._coerce_scalar(2.5, "integer", "$")
    with pytest.raises(ValueError, match="Expected integer"):
        repairer._coerce_scalar("2.5", "integer", "$")
    with pytest.raises(ValueError, match="Expected integer"):
        repairer._coerce_scalar({}, "integer", "$")
    with pytest.raises(ValueError, match="Expected number"):
        repairer._coerce_scalar(True, "number", "$")
    with pytest.raises(ValueError, match="Expected number"):
        repairer._coerce_scalar("nope", "number", "$")
    with pytest.raises(ValueError, match="Expected number"):
        repairer._coerce_scalar([], "number", "$")
    with pytest.raises(ValueError, match="Expected boolean"):
        repairer._coerce_scalar("maybe", "boolean", "$")
    with pytest.raises(ValueError, match="Expected boolean"):
        repairer._coerce_scalar(2, "boolean", "$")
    with pytest.raises(ValueError, match="Expected null"):
        repairer._coerce_scalar("x", "null", "$")
    with pytest.raises(ValueError, match="Unsupported schema type"):
        repairer._coerce_scalar("x", "unsupported", "$")

    assert repairer.repair_value({"a": MISSING_VALUE}, {}, "$") == {"a": ""}
    assert repairer.repair_value({"a": MISSING_VALUE}, {"allOf": []}, "$") == {"a": ""}
    assert repairer.repair_value({"a": "1"}, {"properties": {"a": {"type": "integer"}}}, "$") == {"a": 1}
    assert repairer.repair_value(["1"], {"items": {"type": "integer"}}, "$") == [1]
    with pytest.raises(ValueError, match="Schema does not allow"):
        repairer.repair_value(1, False, "$")


def test_repair_object_skips_unsupported_pattern_regex_with_fallback_and_log():
    log: list[dict[str, str]] = []
    repairer = SchemaRepairer({}, log)
    schema = {
        "type": "object",
        "patternProperties": {"^x[0-9]+$": {"type": "integer"}},
        "additionalProperties": {"type": "string"},
    }

    repaired = repairer.repair_value({"x1": 2}, schema, "$")

    assert repaired == {"x1": "2"}
    assert any("Skipped unsupported patternProperties regex '^x[0-9]+$'" in entry["text"] for entry in log)


def test_apply_enum_const_mismatch_raises():
    repairer = SchemaRepairer({}, [])
    with pytest.raises(ValueError, match="does not match const"):
        repairer.repair_value("b", {"const": "a"}, "$")
    with pytest.raises(ValueError, match="does not match enum"):
        repairer.repair_value("b", {"enum": ["a"]}, "$")


def test_repair_json_valid_empty_string_returns_empty():
    assert repair_json('""') == ""

```

### `tests/test_strict_mode.py`

```py
import pytest

from src.json_repair.json_repair import repair_json


def test_strict_rejects_multiple_top_level_values():
    with pytest.raises(ValueError, match="Multiple top-level JSON elements"):
        repair_json('{"key":"value"}["value"]', strict=True)


def test_strict_rejects_comma_separated_same_shape_top_level_objects():
    with pytest.raises(ValueError, match="Multiple top-level JSON elements"):
        repair_json('{"key":"value"}, {"key":"value_after"}', strict=True)


def test_strict_rejects_adjacent_same_shape_top_level_objects():
    with pytest.raises(ValueError, match="Multiple top-level JSON elements"):
        repair_json('{"key":"value"}{"key":"value_after"}', strict=True)


def test_strict_rejects_adjacent_same_shape_top_level_arrays():
    with pytest.raises(ValueError, match="Multiple top-level JSON elements"):
        repair_json("[1][2]", strict=True)


@pytest.mark.parametrize("payload", ['{"key":"value"}[]', '{"key":"value"}{}', "[]{}", "{}[]", "[1]{}"])
def test_strict_rejects_falsy_top_level_values(payload):
    with pytest.raises(ValueError, match="Multiple top-level JSON elements"):
        repair_json(payload, strict=True)


def test_strict_duplicate_keys_inside_array():
    payload = '[{"key": "first", "key": "second"}]'
    with pytest.raises(ValueError, match="Duplicate key found"):
        repair_json(payload, strict=True, skip_json_loads=True)


def test_strict_rejects_empty_keys():
    payload = '{"" : "value"}'
    with pytest.raises(ValueError, match="Empty key found"):
        repair_json(payload, strict=True, skip_json_loads=True)


def test_strict_requires_colon_between_key_and_value():
    with pytest.raises(ValueError, match="Missing ':' after key"):
        repair_json('{"missing" "colon"}', strict=True)


def test_strict_rejects_empty_values():
    payload = '{"key": , "key2": "value2"}'
    with pytest.raises(ValueError, match="Parsed value is empty"):
        repair_json(payload, strict=True, skip_json_loads=True)


def test_strict_rejects_empty_object_with_extra_characters():
    with pytest.raises(ValueError, match="Parsed object is empty"):
        repair_json('{"dangling"}', strict=True)


def test_strict_rejects_empty_escaped_object_with_extra_characters():
    with pytest.raises(ValueError, match="Parsed object is empty"):
        repair_json('{\\"key\\": \\"value\\"}', strict=True, skip_json_loads=True)


def test_strict_detects_immediate_doubled_quotes():
    with pytest.raises(ValueError, match=r"doubled quotes followed by another quote\.$"):
        repair_json('{"key": """"}', strict=True)


def test_strict_detects_doubled_quotes_followed_by_string():
    with pytest.raises(
        ValueError,
        match="doubled quotes followed by another quote while parsing a string",
    ):
        repair_json('{"key": "" "value"}', strict=True)

```

### `tests/test_type_inference.py`

```py
from pathlib import Path

import pytest

mypy_api = pytest.importorskip("mypy.api")

SNIPPET_TEMPLATE = """\
from json_repair import JSONReturnType
from json_repair.json_repair import repair_json

{assignment}
"""


def _run_type_check(tmp_path: Path, assignment: str) -> tuple[int, str, str]:
    snippet = tmp_path / "typecheck_repair_json.py"
    snippet.write_text(SNIPPET_TEMPLATE.format(assignment=assignment), encoding="utf-8")
    stdout, stderr, exit_code = mypy_api.run([str(snippet)])
    return exit_code, stdout, stderr


@pytest.mark.parametrize(
    "assignment",
    [
        'text: str = repair_json("test")',
        'text: str = repair_json("test", return_objects=False)',
        'value: JSONReturnType = repair_json("test", return_objects=True)',
        'logged: tuple[JSONReturnType, list[dict[str, str]]] = repair_json("test", logging=True)',
        'text: str = repair_json("test", logging=False)',
        'logged: tuple[JSONReturnType, list[dict[str, str]]] = repair_json("test", return_objects=True, logging=True)',
    ],
)
def test_repair_json_type_inference(tmp_path: Path, assignment: str) -> None:
    exit_code, stdout, stderr = _run_type_check(tmp_path, assignment)

    assert exit_code == 0, stderr or stdout

```

### `tests/utils/__init__.py`

```py
"""Helpers and tests for test utilities."""

```

### `tests/utils/test_pattern_properties.py`

```py
from src.json_repair.utils.pattern_properties import match_pattern_properties


def test_match_pattern_properties_exact_anchor_contains():
    pattern_properties = {
        "^abc$": {"name": "exact"},
        "bc": {"name": "contains"},
    }

    matched, unsupported = match_pattern_properties(pattern_properties, "abc")

    assert matched == [{"name": "exact"}, {"name": "contains"}]
    assert unsupported == []


def test_match_pattern_properties_marks_unsupported_regex_patterns():
    pattern_properties = {
        "^x[0-9]+$": {"name": "unsupported"},
        "^x": {"name": "supported"},
    }

    matched, unsupported = match_pattern_properties(pattern_properties, "x1")

    assert matched == [{"name": "supported"}]
    assert unsupported == ["^x[0-9]+$"]


def test_match_pattern_properties_empty_mapping():
    matched, unsupported = match_pattern_properties({}, "any-key")
    assert matched == []
    assert unsupported == []

```

### `tests/utils/test_string_file_wrapper.py`

```py
import pytest

from src.json_repair.utils.string_file_wrapper import StringFileWrapper


def test_string_file_wrapper_handles_multibyte(tmp_path):
    text = "\u0800"
    file_path = tmp_path / "multibyte.json"
    file_path.write_text(text, encoding="utf-8")
    with file_path.open("r", encoding="utf-8") as handle:
        wrapper = StringFileWrapper(handle, chunk_length=2)
        assert wrapper[0:1] == text
        assert wrapper[0:2] == text
        assert wrapper[0] == text


def test_string_file_wrapper_invalid_buffer_access(tmp_path):
    file_path = tmp_path / "buffer.json"
    file_path.write_text("ab", encoding="utf-8")
    with file_path.open("r", encoding="utf-8") as handle:
        wrapper = StringFileWrapper(handle, chunk_length=1)
        with pytest.raises(IndexError):
            wrapper.get_buffer(-1)
        # Build chunk metadata and then request the chunk that resides past EOF.
        len(wrapper)
        with pytest.raises(IndexError):
            wrapper.get_buffer(2)


def test_string_file_wrapper_slice_variations(tmp_path):
    file_path = tmp_path / "slice.json"
    file_path.write_text("abcd", encoding="utf-8")
    with file_path.open("r", encoding="utf-8") as handle:
        wrapper = StringFileWrapper(handle, chunk_length=2)
        assert wrapper[-2:4] == "cd"
        assert wrapper[0:-1] == "abc"
        assert wrapper[3:1] == ""
        assert wrapper[0:4:2] == "ac"
        with pytest.raises(ValueError, match="slice step cannot be zero"):
            _ = wrapper[::0]


def test_string_file_wrapper_negative_indices(tmp_path):
    file_path = tmp_path / "index.json"
    file_path.write_text("xyz", encoding="utf-8")
    with file_path.open("r", encoding="utf-8") as handle:
        wrapper = StringFileWrapper(handle, chunk_length=2)
        assert wrapper[-1] == "z"
        with pytest.raises(IndexError):
            _ = wrapper[-10]


def test_string_file_wrapper_ensure_chunk_position_raises(tmp_path):
    file_path = tmp_path / "ensure.json"
    file_path.write_text("foo", encoding="utf-8")
    with file_path.open("r", encoding="utf-8") as handle:
        wrapper = StringFileWrapper(handle, chunk_length=1)
        with pytest.raises(IndexError):
            wrapper._ensure_chunk_position(10)

```

### `tests/valid.json`

```json
[
    {
      "_id": "655b66256574f09bdae8abe8",
      "index": 0,
      "guid": "31082ae3-b0f3-4406-90f4-cc450bd4379d",
      "isActive": false,
      "balance": "$2,562.78",
      "picture": "http://placehold.it/32x32",
      "age": 32,
      "eyeColor": "brown",
      "name": "Glover Rivas",
      "gender": "male",
      "company": "EMPIRICA",
      "email": "gloverrivas@empirica.com",
      "phone": "+1 (842) 507-3063",
      "address": "536 Montague Terrace, Jenkinsville, Kentucky, 2235",
      "about": "Mollit consectetur excepteur voluptate tempor dolore ullamco enim irure ullamco non enim officia. Voluptate occaecat proident laboris ea Lorem cupidatat reprehenderit nisi nisi aliqua. Amet nulla ipsum deserunt excepteur amet ad aute aute ex. Et enim minim sit veniam est quis dolor nisi sunt quis eiusmod in. Amet eiusmod cillum sunt occaecat dolor laboris voluptate in eiusmod irure aliqua duis.",
      "registered": "2023-11-18T09:32:36 -01:00",
      "latitude": 36.26102,
      "longitude": -91.304608,
      "tags": [
        "non",
        "tempor",
        "do",
        "ullamco",
        "dolore",
        "sunt",
        "ipsum"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Cara Shepherd"
        },
        {
          "id": 1,
          "name": "Mason Farley"
        },
        {
          "id": 2,
          "name": "Harriet Cochran"
        }
      ],
      "greeting": "Hello, Glover Rivas! You have 7 unread messages.",
      "favoriteFruit": "strawberry"
    },
    {
      "_id": "655b662585364bc57278bb6f",
      "index": 1,
      "guid": "0dea7a3a-f812-4dde-b78d-7a9b58e5da05",
      "isActive": true,
      "balance": "$1,359.48",
      "picture": "http://placehold.it/32x32",
      "age": 38,
      "eyeColor": "brown",
      "name": "Brandi Moreno",
      "gender": "female",
      "company": "MARQET",
      "email": "brandimoreno@marqet.com",
      "phone": "+1 (850) 434-2077",
      "address": "537 Doone Court, Waiohinu, Michigan, 3215",
      "about": "Irure proident adipisicing do Lorem do incididunt in laborum in eiusmod eiusmod ad elit proident. Eiusmod dolor ex magna magna occaecat. Nulla deserunt velit ex exercitation et irure sunt. Cupidatat ut excepteur ea quis labore sint cupidatat incididunt amet eu consectetur cillum ipsum proident. Occaecat exercitation aute laborum dolor proident reprehenderit laborum in voluptate culpa. Exercitation nulla adipisicing culpa aute est deserunt ea nisi deserunt consequat occaecat ut et non. Incididunt ex exercitation dolor dolor anim cillum dolore.",
      "registered": "2015-09-03T11:47:15 -02:00",
      "latitude": -19.768953,
      "longitude": 8.948458,
      "tags": [
        "laboris",
        "occaecat",
        "laborum",
        "laborum",
        "ex",
        "cillum",
        "occaecat"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Erna Kelly"
        },
        {
          "id": 1,
          "name": "Black Mays"
        },
        {
          "id": 2,
          "name": "Davis Buck"
        }
      ],
      "greeting": "Hello, Brandi Moreno! You have 1 unread messages.",
      "favoriteFruit": "apple"
    },
    {
      "_id": "655b6625870da431bcf5e0c2",
      "index": 2,
      "guid": "b17f6e3f-c898-4334-abbf-05cf222f143b",
      "isActive": false,
      "balance": "$1,493.77",
      "picture": "http://placehold.it/32x32",
      "age": 20,
      "eyeColor": "brown",
      "name": "Moody Meadows",
      "gender": "male",
      "company": "OPTIQUE",
      "email": "moodymeadows@optique.com",
      "phone": "+1 (993) 566-3041",
      "address": "766 Osborn Street, Bath, Maine, 7666",
      "about": "Non commodo excepteur nostrud qui adipisicing aliquip dolor minim nulla culpa proident. In ad cupidatat ea mollit ex est do deserunt proident nostrud. Cillum id id eiusmod amet exercitation nostrud cillum sunt deserunt dolore deserunt eiusmod mollit. Ut ex tempor ad laboris voluptate labore id officia fugiat exercitation amet.",
      "registered": "2015-01-16T02:48:28 -01:00",
      "latitude": -25.847327,
      "longitude": 63.95991,
      "tags": [
        "aute",
        "commodo",
        "adipisicing",
        "nostrud",
        "duis",
        "mollit",
        "ut"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Lacey Cash"
        },
        {
          "id": 1,
          "name": "Gabrielle Harmon"
        },
        {
          "id": 2,
          "name": "Ellis Lambert"
        }
      ],
      "greeting": "Hello, Moody Meadows! You have 4 unread messages.",
      "favoriteFruit": "strawberry"
    },
    {
      "_id": "655b6625f3e1bf422220854e",
      "index": 3,
      "guid": "92229883-2bfd-4974-a08c-1b506b372e46",
      "isActive": false,
      "balance": "$2,215.34",
      "picture": "http://placehold.it/32x32",
      "age": 22,
      "eyeColor": "brown",
      "name": "Heath Nguyen",
      "gender": "male",
      "company": "BLEENDOT",
      "email": "heathnguyen@bleendot.com",
      "phone": "+1 (989) 512-2797",
      "address": "135 Milton Street, Graniteville, Nebraska, 276",
      "about": "Consequat aliquip irure Lorem cupidatat nulla magna ullamco nulla voluptate adipisicing anim consectetur tempor aliquip. Magna aliqua nulla eu tempor esse proident. Proident fugiat ad ex Lorem reprehenderit dolor aliquip labore labore aliquip. Deserunt aute enim ea minim officia anim culpa sint commodo. Cillum consectetur excepteur aliqua exercitation Lorem veniam voluptate.",
      "registered": "2016-07-06T01:31:07 -02:00",
      "latitude": -60.997048,
      "longitude": -102.397885,
      "tags": [
        "do",
        "ad",
        "consequat",
        "irure",
        "tempor",
        "elit",
        "minim"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Walker Hernandez"
        },
        {
          "id": 1,
          "name": "Maria Lane"
        },
        {
          "id": 2,
          "name": "Mcknight Barron"
        }
      ],
      "greeting": "Hello, Heath Nguyen! You have 4 unread messages.",
      "favoriteFruit": "apple"
    },
    {
      "_id": "655b6625519a5b5e4b6742bf",
      "index": 4,
      "guid": "c5dc685f-6d0d-4173-b4cf-f5df29a1e8ef",
      "isActive": true,
      "balance": "$1,358.90",
      "picture": "http://placehold.it/32x32",
      "age": 33,
      "eyeColor": "brown",
      "name": "Deidre Duke",
      "gender": "female",
      "company": "OATFARM",
      "email": "deidreduke@oatfarm.com",
      "phone": "+1 (875) 587-3256",
      "address": "487 Schaefer Street, Wattsville, West Virginia, 4506",
      "about": "Laboris eu nulla esse magna sit eu deserunt non est aliqua exercitation commodo. Ad occaecat qui qui laborum dolore anim Lorem. Est qui occaecat irure enim deserunt enim aliqua ex deserunt incididunt esse. Quis in minim laboris proident non mollit. Magna ea do labore commodo. Et elit esse esse occaecat officia ipsum nisi.",
      "registered": "2021-09-12T04:17:08 -02:00",
      "latitude": 68.609781,
      "longitude": -87.509134,
      "tags": [
        "mollit",
        "cupidatat",
        "irure",
        "sit",
        "consequat",
        "anim",
        "fugiat"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Bean Paul"
        },
        {
          "id": 1,
          "name": "Cochran Hubbard"
        },
        {
          "id": 2,
          "name": "Rodgers Atkinson"
        }
      ],
      "greeting": "Hello, Deidre Duke! You have 6 unread messages.",
      "favoriteFruit": "apple"
    },
    {
      "_id": "655b6625a19b3f7e5f82f0ea",
      "index": 5,
      "guid": "75f3c264-baa1-47a0-b21c-4edac23d9935",
      "isActive": true,
      "balance": "$3,554.36",
      "picture": "http://placehold.it/32x32",
      "age": 26,
      "eyeColor": "blue",
      "name": "Lydia Holland",
      "gender": "female",
      "company": "ESCENTA",
      "email": "lydiaholland@escenta.com",
      "phone": "+1 (927) 482-3436",
      "address": "554 Rockaway Parkway, Kohatk, Montana, 6316",
      "about": "Consectetur ea est labore commodo laborum mollit pariatur non enim. Est dolore et non laboris tempor. Ea incididunt ut adipisicing cillum labore officia tempor eiusmod commodo. Cillum fugiat ex consectetur ut nostrud anim nostrud exercitation ut duis in ea. Eu et id fugiat est duis eiusmod ullamco quis officia minim sint ea nisi in.",
      "registered": "2018-03-13T01:48:56 -01:00",
      "latitude": -88.495799,
      "longitude": 71.840667,
      "tags": [
        "veniam",
        "minim",
        "consequat",
        "consequat",
        "incididunt",
        "consequat",
        "elit"
      ],
      "friends": [
        {
          "id": 0,
          "name": "Debra Massey"
        },
        {
          "id": 1,
          "name": "Weiss Savage"
        },
        {
          "id": 2,
          "name": "Shannon Guerra"
        }
      ],
      "greeting": "Hello, Lydia Holland! You have 5 unread messages.",
      "favoriteFruit": "banana"
    }
  ]
```
