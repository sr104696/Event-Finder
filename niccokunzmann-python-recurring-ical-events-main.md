# niccokunzmann/python-recurring-ical-events@main

- Files included: 237
- Files skipped: 6
- Total size: 935.6 KB
- Estimated tokens: ~239,318

## Directory Structure

```
├── .github
│   ├── ISSUE_TEMPLATE
│   │   └── bug_report.md
│   ├── workflows
│   │   └── tests.yml
│   ├── dependabot.yml
│   └── FUNDING.yml
├── benchmark
│   ├── __init__.py
│   ├── issue42.ics
│   ├── issue42.py
│   ├── issue42.txt
│   └── README.md
├── docs
│   ├── community
│   │   ├── index.md
│   │   ├── maintenance.rst
│   │   └── media.md
│   ├── img
│   │   ├── architecture.png
│   │   └── architecture.svg
│   ├── reference
│   │   ├── api.md
│   │   ├── architecture.rst
│   │   ├── compatibility.md
│   │   ├── dependencies.rst
│   │   ├── documentation.md
│   │   ├── index.md
│   │   ├── license.md
│   │   ├── related-projects.rst
│   │   └── research.rst
│   ├── user-guide
│   │   ├── examples.rst
│   │   └── index.md
│   ├── .gitignore
│   ├── changelog.md
│   ├── conf.py
│   ├── docutils.conf
│   ├── index.md
│   ├── Makefile
│   ├── requirements.in
│   ├── requirements.txt
│   └── security_policy.md
├── recurring_ical_events
│   ├── adapters
│   │   ├── __init__.py
│   │   ├── alarm.py
│   │   ├── component.py
│   │   ├── event.py
│   │   ├── journal.py
│   │   └── todo.py
│   ├── selection
│   │   ├── __init__.py
│   │   ├── alarm.py
│   │   ├── all.py
│   │   ├── base.py
│   │   └── name.py
│   ├── series
│   │   ├── __init__.py
│   │   ├── alarm.py
│   │   └── rrule.py
│   ├── test
│   │   ├── calendars
│   │   │   ├── after_many_events_in_order.ics
│   │   │   ├── alarm_1_week_before_event.ics
│   │   │   ├── alarm_15_min_before_event_snoozed.ics
│   │   │   ├── alarm_absolute_edited.ics
│   │   │   ├── alarm_absolute_repeat.ics
│   │   │   ├── alarm_absolute.ics
│   │   │   ├── alarm_around_event_boundaries.ics
│   │   │   ├── alarm_at_start_of_event.ics
│   │   │   ├── alarm_of_repeated_event.ics
│   │   │   ├── alarm_recurring_and_acknowledged_at_2024_11_27_16_27.ics
│   │   │   ├── alarm_removed_and_moved.ics
│   │   │   ├── alarm_several_in_one.ics
│   │   │   ├── alarms_at_the_same_time.ics
│   │   │   ├── alarms_different_in_same_event.ics
│   │   │   ├── bad_rrule_missing_until_event.ics
│   │   │   ├── date_exclude.txt
│   │   │   ├── daylight_saving_time.ics
│   │   │   ├── discourse_no_dtend.ics
│   │   │   ├── duplicated_rrule.ics
│   │   │   ├── duration_edited.ics
│   │   │   ├── duration.ics
│   │   │   ├── each_week_but_one_deleted.ics
│   │   │   ├── each_week_but_two_deleted.ics
│   │   │   ├── end_before_start_event.ics
│   │   │   ├── event_10_times.ics
│   │   │   ├── fablab_cottbus.ics
│   │   │   ├── Germany_Holidays.ics
│   │   │   ├── Germany.ics
│   │   │   ├── issue_107_omitting_last_event.ics
│   │   │   ├── issue_113_period_in_rdate.ics
│   │   │   ├── issue_113_period_rdate_duration.ics
│   │   │   ├── issue_117_until_before_dtstart.ics
│   │   │   ├── issue_128_only_first_event.ics
│   │   │   ├── issue_132_swapped_start_and_end.ics
│   │   │   ├── issue_148_edge_case_1.ics
│   │   │   ├── issue_148_edge_case_2.ics
│   │   │   ├── issue_148_exdate_and_rdate_unedited.ics
│   │   │   ├── issue_148_exdate_and_rdate_updated.ics
│   │   │   ├── issue_148_ignored_exdate.ics
│   │   │   ├── issue_15_duplicated_events.ics
│   │   │   ├── issue_151_macos_linux_difference.ics
│   │   │   ├── issue_151_macos_linux_difference2.ics
│   │   │   ├── issue_163_deleted_modification.ics
│   │   │   ├── issue_164_duplicated_event.ics
│   │   │   ├── issue_173_only_modifications_error.ics
│   │   │   ├── issue_179_example.ics
│   │   │   ├── issue_18_cancel_status.ics
│   │   │   ├── issue_186_invalid_trigger.ics
│   │   │   ├── issue_20_exdate_ignored.ics
│   │   │   ├── issue_201_mixed_datetime_and_date.ics
│   │   │   ├── issue_201_test_matrix.ics
│   │   │   ├── issue_223_one_event_with_sequence.ics
│   │   │   ├── issue_223_thunderbird.ics
│   │   │   ├── issue_243_recurrence_id_is_not_identical_to_dtstart.ics
│   │   │   ├── issue_253_additional_recurrence_id.ics
│   │   │   ├── issue_253_edge_case_1.ics
│   │   │   ├── issue_253_recurrence_id_included.ics
│   │   │   ├── issue_27_t1.ics
│   │   │   ├── issue_27_t2.ics
│   │   │   ├── issue_28_rrule_with_UTC_endinginZ.ics
│   │   │   ├── issue_36_recurrence_ID_format.ics
│   │   │   ├── issue_4_rrule_until.ics
│   │   │   ├── issue_4_weidenrinde.ics
│   │   │   ├── issue_4.ics
│   │   │   ├── issue_44_double_event.ics
│   │   │   ├── issue_48_daylight_aware_repeats.ics
│   │   │   ├── issue_48_dst.ics
│   │   │   ├── issue_61_time_zone_error.ics
│   │   │   ├── issue_62_moved_event_2.ics
│   │   │   ├── issue_62_moved_event.ics
│   │   │   ├── issue_75_range_parameter.ics
│   │   │   ├── issue_86_x_wr_timezone_without_time_zone_in_dt.ics
│   │   │   ├── issue_97_simple_journal.ics
│   │   │   ├── issue_97_simple_todo.ics
│   │   │   ├── issue_97_todo_nodtstart.ics
│   │   │   ├── machbar_16_feb_2019.ics
│   │   │   ├── multiple_rrule.ics
│   │   │   ├── no_events.ics
│   │   │   ├── one_day_event_repeat_every_day.ics
│   │   │   ├── one_day_event.ics
│   │   │   ├── one_event_repeat_every_3_days.ics
│   │   │   ├── one_event.ics
│   │   │   ├── rdate_falls_on_rrule_until.ics
│   │   │   ├── rdate_hackerpublicradio.ics
│   │   │   ├── rdate.ics
│   │   │   ├── rdate2.ics
│   │   │   ├── recurrence_sequence_number.ics
│   │   │   ├── recurring_events_changed_duration.ics
│   │   │   ├── recurring_events_moved.ics
│   │   │   ├── same_event_recurring_at_same_time.ics
│   │   │   ├── several_events_at_the_same_time.ics
│   │   │   ├── subcomponents.ics
│   │   │   ├── three_events_one_edited.ics
│   │   │   ├── three_events.ics
│   │   │   ├── x_wr_timezone_simple_events_issue_59.ics
│   │   │   └── zero_size_event.ics
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── py.py
│   │   ├── test_after.py
│   │   ├── test_at_function.py
│   │   ├── test_bad_rrule_format.py
│   │   ├── test_convert_inputs.py
│   │   ├── test_count.py
│   │   ├── test_daylight_saving_time.py
│   │   ├── test_deleted_entries.py
│   │   ├── test_duration.py
│   │   ├── test_end_before_start_event.py
│   │   ├── test_event_values_and_edits.py
│   │   ├── test_example_function.py
│   │   ├── test_examples.py
│   │   ├── test_extend_classes.py
│   │   ├── test_issue_101_select_components.py
│   │   ├── test_issue_107_omitting_last_event.py
│   │   ├── test_issue_113_period_in_rdate.py
│   │   ├── test_issue_117_until_before_dtstart.py
│   │   ├── test_issue_128_only_first_event.py
│   │   ├── test_issue_132_swapped_start_and_end.py
│   │   ├── test_issue_139_no_duration.py
│   │   ├── test_issue_148_ignored_exdate_in_higher_sequence.py
│   │   ├── test_issue_15.py
│   │   ├── test_issue_151_macos_linux_difference.py
│   │   ├── test_issue_163_deleted_modification.py
│   │   ├── test_issue_164_duplicated_event.py
│   │   ├── test_issue_173_only_modification_included.py
│   │   ├── test_issue_179_span_in_event.py
│   │   ├── test_issue_18_cancel_status.py
│   │   ├── test_issue_186_alarms.py
│   │   ├── test_issue_186_icalendar_alarm_interface.py
│   │   ├── test_issue_20_exdate_ignored.py
│   │   ├── test_issue_201_incompatible_dates.py
│   │   ├── test_issue_211_pagination.py
│   │   ├── test_issue_217_expose_occurrences_api.py
│   │   ├── test_issue_219_recurrence_id_in_events.py
│   │   ├── test_issue_223_sequence_number.py
│   │   ├── test_issue_243_recurrence_id_is_not_identical_to_dtstart.py
│   │   ├── test_issue_253_additional_recurrence_id.py
│   │   ├── test_issue_27.py
│   │   ├── test_issue_28_timezone_with_z.py
│   │   ├── test_issue_36_recurrence_id_format.py
│   │   ├── test_issue_4.py
│   │   ├── test_issue_44_day_event_reported_twice.py
│   │   ├── test_issue_48_daylight.py
│   │   ├── test_issue_48_dst.py
│   │   ├── test_issue_6_copy_subcomponents.py
│   │   ├── test_issue_61.py
│   │   ├── test_issue_62_moved_event.py
│   │   ├── test_issue_7_datetime_and_date_start_stop.py
│   │   ├── test_issue_75_range_parameter.py
│   │   ├── test_issue_86_x_wr_timezone_but_no_tzid_in_dt.py
│   │   ├── test_issue_97_simple_recurrent_todos_and_journals.py
│   │   ├── test_keep_recurrence_attributes.py
│   │   ├── test_multiple_rrule.py
│   │   ├── test_occurrence.py
│   │   ├── test_properties.py
│   │   ├── test_rdate.py
│   │   ├── test_readme.py
│   │   ├── test_recurrence_sequence_number.py
│   │   ├── test_repeated_properties.py
│   │   ├── test_repetitions_do_not_change.py
│   │   ├── test_simple_recurrent_events.py
│   │   ├── test_single_events.py
│   │   ├── test_skip_bad_events.py
│   │   ├── test_time_arguments.py
│   │   ├── test_time_span_contains_event.py
│   │   ├── test_time_zones_differ.py
│   │   ├── test_timedelta_for_between.py
│   │   ├── test_util_functions.py
│   │   ├── test_with_doctest.py
│   │   ├── test_x_wr_timezone.py
│   │   ├── test_zero_size_events.py
│   │   └── test_zoneinfo_issue_57.py
│   ├── __init__.py
│   ├── .gitignore
│   ├── constants.py
│   ├── errors.py
│   ├── examples.py
│   ├── occurrence.py
│   ├── pages.py
│   ├── query.py
│   ├── types.py
│   ├── util.py
│   └── version.py
├── .cleanup-branches.sh
├── .gitignore
├── .gitlab-ci.yml
├── .pre-commit-config.yaml
├── .readthedocs.yml
├── LICENSE
├── pyproject.toml
├── README.rst
├── rfc5545.html
├── rfc9074.html
├── SECURITY.md
└── tox.ini
```

## Code Digest

### `.cleanup-branches.sh`

```sh
#!/bin/bash
#
# Srcipt to clean up branches that are no longer in use.
#
# Due to gitlab mirroring back and forth, the branches are not
# being deleted but put back in place again.
#

set -e

cd "`dirname \"$0\"`"

remotes=""
branches=""

for remote in `git remote`; do
    echo -n "Choose branches from remote $remote? (Y/n) "
    read
    if [ -z "$REPLY" ] || [ "$REPLY" == "y" ] || [ "$REPLY" == "Y" ]; then
        echo "Using remote $remote."
        remotes="$remotes $remote"
    fi
done

for branch in `git branch -r | grep -oE '[^/]+$' | sort | uniq | grep -vE 'master'`; do
    echo -n "Delete branch $branch? (y/N) "
    read
    if [ "$REPLY" == "y" ] || [ "$REPLY" == "Y" ]; then
        echo "Remembering $branch for deletion."
        branches="$branches $branch"
    else
        echo "Keeping $branch."
    fi
done

echo "Selected remotes to delete branches from: $remotes."
echo "Selected branches to delete: $branches"
echo -n "Start deleting? (Control+C to stop) "
read

for branch in $branches; do
    echo " ---------- deleting $branch ---------- "
    git branch -d "$branch" || true
    for remote in $remotes; do
        git push --delete "$remote" "$branch" || true
    done
done

```

### `.github/dependabot.yml`

```yml
# To get started with Dependabot version updates, you'll need to specify which
# package ecosystems to update and where the package manifests are located.
# Please see the documentation for all configuration options:
# https://docs.github.com/github/administering-a-repository/configuration-options-for-dependency-updates

version: 2
updates:
  - package-ecosystem: "pip" # See documentation for possible values
    directory: "/" # Location of package manifests
    schedule:
      interval: "weekly"
  - package-ecosystem: github-actions
    directory: /
    groups:
      github-actions:
        patterns:
          - "*"  # Group all Actions updates into a single larger pull request
    schedule:
      interval: weekly

```

### `.github/FUNDING.yml`

```yml
# These are supported funding model platforms

github: # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
- niccokunzmann
polar: niccokunzmann/python-recurring-ical-events
patreon: # Replace with a single Patreon username
open_collective: open-web-calendar # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: pypi/recurring-ical-events # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
lfx_crowdfunding: # Replace with a single LFX Crowdfunding project-name e.g., cloud-foundry
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']

```

### `.github/ISSUE_TEMPLATE/bug_report.md`

```md
---
name: Bug report
about: Create a report and help this package improve
title: 'bug: '
labels: bug
assignees: ''
---
<!-- This template is a suggestion. So, you do not have to use it. -->

**Describe the bug**
<!-- A clear and concise description of what the bug is. -->

**To Reproduce**
<!-- Source code to reproduce the behavior. -->

**ICS file**
<!-- Please paste an ICS file here which does not work or attach it with a .txt ending. -->

```ics
```

**Expected behavior**
<!-- A clear and concise description of what you expected to happen. -->

**Console output**
<!-- If applicable, add output/screenshots to help explain your problem. -->

**Version:**
<!-- Which Version do you use? -->
![](https://raster.shields.io/badge/version-3.3.0-brightgreen.png)

<!-- Sometimes, the problems are in other packages. You can provide an overview
     by running this command and passing the output:

     pip list
-->
```shell
pip list
```

**Additional context**
<!-- Add any other context about the problem here. Or maybe related issues. -->

**Suggested implementation**
<!-- If possible, suggest a way of solving this or just let this text down there remain as it is. -->

- [ ] add an ICS file, example:
    https://github.com/niccokunzmann/python-recurring-ical-events/blob/f4a90b211f30bf0522f03514ba50eb69826f0fdb/test/calendars/issue-15-duplicated-events.ics#L1
- [ ] add a test, example:
    https://github.com/niccokunzmann/python-recurring-ical-events/blob/f4a90b211f30bf0522f03514ba50eb69826f0fdb/test/test_issue_15.py#L21
- [ ] fix the bug and ensure the test code passes

```

### `.github/workflows/tests.yml`

```yml
name: tests

on:
  push:
    branches:
    - main
    tags:
    - v*
  pull_request:
  workflow_dispatch:

jobs:
  run-tests:
    strategy:
      matrix:
        config:
        # [Python version, tox env, timezone]
        - ["3.8",   "py38",  "Australia/Sydney"]
        - ["3.9",   "py39",  "UTC"]
        - ["3.10",  "py310", "Asia/Singapore"]
        - ["3.11",  "py311", "Pacific/Bougainville"]
        - ["3.12",  "py312", "Europe/London"]
        - ["3.12",  "build", "Europe/Moscow"]
        - ["3.13",  "py313", "America/Dawson"]
        - ["3.14",  "py314", "Africa/Tunis"]
        - ["3.14",  "docs",  "Europe/Berlin"]

    runs-on: ubuntu-latest
    name: ${{ matrix.config[1] }}
    steps:
    - uses: actions/checkout@v7
    - name: Set up Python
      uses: actions/setup-python@v6
      with:
        python-version: ${{ matrix.config[0] }}
    - name: Pip cache
      uses: actions/cache@v6
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ matrix.config[0] }}-${{ hashFiles('setup.*', 'tox.ini') }}
        restore-keys: |
          ${{ runner.os }}-pip-${{ matrix.config[0] }}-
          ${{ runner.os }}-pip-
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install tox
    - name: Test
      run: |
        export TZ="{{ matrix.config[2] }}"
        # Debug and check the default time zone
        python3 -c 'import time; time.tzset(); print(time.strftime("%X %x %Z"))'
        tox -e ${{ matrix.config[1] }}

  deploy-tag-to-pypi:
    # only deploy on tags, see https://stackoverflow.com/a/58478262/1320237
    if: startsWith(github.ref, 'refs/tags/v')
    needs:
    - run-tests
    runs-on: ubuntu-latest
    # This environment stores the TWINE_USERNAME and TWINE_PASSWORD
    # see https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment
    environment:
      name: PyPI
      url: https://pypi.org/project/recurring-ical-events/
    # after using the environment, we need to make the secrets available
    # see https://docs.github.com/en/actions/security-guides/encrypted-secrets#example-using-bash
    env:
      TWINE_USERNAME: ${{ secrets.TWINE_USERNAME }}
      TWINE_PASSWORD: ${{ secrets.TWINE_PASSWORD }}
    steps:
    - uses: actions/checkout@v7
    - name: Set up Python
      uses: actions/setup-python@v6
      with:
        python-version: "3.12"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install --upgrade wheel twine build
    - name: remove old files
      run: rm -rf dist/*
    - name: build distribution files
      run: python -m build
    - name: deploy to pypi
      run: |
        # You will have to set the variables TWINE_USERNAME and TWINE_PASSWORD
        # You can use a token specific to your project by setting the user name to
        # __token__ and the password to the token given to you by the PyPI project.
        # sources:
        #   - https://shambu2k.hashnode.dev/gitlab-to-pypi
        #   - http://blog.octomy.org/2020/11/deploying-python-pacakges-to-pypi-using.html?m=1
        # Also, set the tags as protected to allow the secrets to be used.
        # see https://docs.gitlab.com/ee/user/project/protected_tags.html
        if [ -z "$TWINE_USERNAME" ]; then
          echo "WARNING: TWINE_USERNAME not set!"
        fi
        if [ -z "$TWINE_PASSWORD" ]; then
          echo "WARNING: TWINE_PASSWORD not set!"
        fi
        twine check dist/*
        twine upload dist/*

  deploy-github-release:
    # only deploy on tags, see https://stackoverflow.com/a/58478262/1320237
    if: startsWith(github.ref, 'refs/tags/v')
    needs:
    - run-tests
    - deploy-tag-to-pypi
    runs-on: ubuntu-latest
    environment:
      name: github-release
    steps:
      - uses: actions/checkout@v7
      - name: Create GitHub release from tag
        uses: ncipollo/release-action@v1
        with:
          allowUpdates: true
          body: "To view the changes, please see the [Changelog](https://recurring-ical-events.readthedocs.io/en/latest/changelog.html). This release can be installed from [PyPI](https://pypi.org/project/recurring-ical-events/#history)."
          generateReleaseNotes: false

```

### `.gitignore`

```gitignore
/ENV
__pycache__
*.pyc
*egg-info
/build
/dist
.pytest_cache/
.vscode/
ENV2
*.swp
env-2
/htmlcov
.coverage
.venv
venv
/requirements.txt

```

### `.gitlab-ci.yml`

```yml
# This file is a template, and might need editing before it works on your project.
# To contribute improvements to CI/CD templates, please follow the Development guide at:
# https://docs.gitlab.com/ee/development/cicd/templates.html
# This specific template is located at:
# https://gitlab.com/gitlab-org/gitlab/-/blob/master/lib/gitlab/ci/templates/Python.gitlab-ci.yml

# Official language image. Look for the different tagged releases at:
# https://hub.docker.com/r/library/python/tags/
image: python:latest

variables:
  # Change pip's cache directory to be inside the project directory since we can
  # only cache local items.
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

# Pip's cache doesn't store the python packages
# https://pip.pypa.io/en/stable/reference/pip_install/#caching
#
# If you want to also cache the installed packages, you have to install
# them in a virtualenv and cache it as well.
cache:
  paths:
    - .cache/pip

stages:
  - build
  - test
  - deploy

build-package:
  stage: build
  script:
    - 'export PATH="$PATH:/root/.local/bin"'
    - python --version  # For debugging
    # install from the zip file to see if files were forgotten
    - python setup.py sdist --dist-dir=dist --formats=zip
    - pip install --user --upgrade pip
    # download packages once and cache them for the others
    - pip install --user -r test-requirements.txt -r requirements.txt virtualenv wheel
  artifacts:
    paths:
      - sdist
    untracked: true

# --------------------------- tests

.run-tests:
  needs:
    - build-package
  stage: test
  before_script:
    - 'export PATH="$PATH:/root/.local/bin"'
    - pip install --user --upgrade pip
    # install the package in a virtual env
    - pip install --user virtualenv
    - virtualenv ENV
    - source ENV/bin/activate
    # install package from build step
    - pip install dist/*.zip
    # test that the example works without the test dependencies
    - python example.py
    # install test requirements
    - pip install -r test-requirements.txt
    # Debug and check the default time zone
    - python3 -c 'import time; time.tzset(); print(time.strftime("%X %x %Z"))'
  script:
    - test/test_code_quality.sh
    # using coverage see
    # - https://docs.gitlab.com/ee/user/project/merge_requests/test_coverage_visualization.html#python-example
    # - https://gitlab.com/gitlab-org/gitlab/-/issues/285086
    - coverage run -m pytest
    - coverage report
    - coverage xml
  artifacts:
    expire_in: 2 days
    reports:
      coverage_report:
        # format thanks to
        # https://stackoverflow.com/a/72138320
        coverage_format: cobertura
        path: coverage.xml

.env1:
  variables:
    TZ: Europe/Berlin

.env2:
  variables:
    TZ: Australia/Sydney

# ----- tests

test-python-2.7-env1:
  image: python:2.7
  extends:
  - .run-tests
  - .env1

test-python-2.7-env2:
  image: python:2.7
  extends:
  - .run-tests
  - .env2

test-python-3.7-env1:
  image: python:3.7
  extends:
  - .run-tests
  - .env1

test-python-3.7-env2:
  image: python:3.7
  extends:
  - .run-tests
  - .env2

test-python-3.8-env1:
  image: python:3.8
  extends:
  - .run-tests
  - .env1

test-python-3.8-env2:
  image: python:3.8
  extends:
  - .run-tests
  - .env2

test-python-3.9-env1:
  image: python:3.9
  extends:
  - .run-tests
  - .env1

test-python-3.9-env2:
  image: python:3.9
  extends:
  - .run-tests
  - .env2

test-python-3.10-env1:
  image: python:3.10
  extends:
  - .run-tests
  - .env1

test-python-3.10-env2:
  image: python:3.10
  extends:
  - .run-tests
  - .env2

# --------------------------- deploy

deploy-package:
  # use python3.9 because piwheels.org build for this version
  image: python:3.9
  stage: deploy
  needs:
    - test-python-2.7-env1
    - test-python-2.7-env2
    - test-python-3.7-env1
    - test-python-3.7-env2
    - test-python-3.8-env1
    - test-python-3.8-env2
    - test-python-3.9-env1
    - test-python-3.9-env2
    - test-python-3.10-env1
    - test-python-3.10-env2
  before_script:
    - 'export PATH="$PATH:/root/.local/bin"'
    - pip install --user --upgrade pip
    # add piwheels so we can build on raspberry pi
    - pip config set global.extra-index-url 'https://www.piwheels.org/simple'
    - pip config list
    - pip install --user wheel twine
  script:
    - PACKAGE_VERSION=`python setup.py --version`
    - TAG_NAME=v$PACKAGE_VERSION
    - echo "Package version $PACKAGE_VERSION with possible tag name $TAG_NAME on $CI_COMMIT_TAG"
    # test that the tag represents the version
    # see https://docs.gitlab.com/ee/ci/variables/predefined_variables.html
    - '( if [ -n "$CI_COMMIT_TAG" ]; then if [ $TAG_NAME != $CI_COMMIT_TAG ]; then echo "This tag is for the wrong version. Got \"$CI_COMMIT_TAG\" expected \"$TAG_NAME\"."; exit 1; fi; fi; )'
    # remove old files
    - rm -rf dist/*
    # build new files
    - python setup.py bdist_wheel sdist
    # You will have to set the variables TWINE_USERNAME and TWINE_PASSWORD
    # You can use a token specific to your project by setting the user name to 
    # __token__ and the password to the token given to you by the PyPI project.
    # sources:
    #   - https://shambu2k.hashnode.dev/gitlab-to-pypi
    #   - http://blog.octomy.org/2020/11/deploying-python-pacakges-to-pypi-using.html?m=1
    # Also, set the tags as protected to allow the secrets to be used.
    # see https://docs.gitlab.com/ee/user/project/protected_tags.html
    - twine check dist/*
    - twine upload dist/*
  artifacts:
    paths:
      - dist/*
  only:
    # run only on tags with a certain name
    # see http://stackoverflow.com/questions/52830653/ddg#52859379
    - /^v[0-9]+\.[0-9]+\.[0-9a-z]+/


```

### `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: debug-statements

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.11.9
    hooks:
      - id: ruff
        args: [--config, "pyproject.toml", --fix]
      - id: ruff-format
        args: [--config, "pyproject.toml"]

```

### `.readthedocs.yml`

```yml
# .readthedocs.yml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Build documentation in the docs/ directory with Sphinx
sphinx:
  configuration: docs/conf.py

# Optionally build your docs in additional formats such as PDF and ePub
formats: all

build:
  os: ubuntu-24.04
  tools:
    python: "3.13"
  commands:
    - git fetch --tags
    - pip install build
    - python -m build
    # Cancel building pull requests when there aren't changes in the docs directory or YAML file.
    # You can add any other files or directories that you'd like here as well,
    # like your docs requirements file, or other files that will change your docs build.
    #
    # If there are no changes (git diff exits with 0) we force the command to return with 183.
    # This is a special exit code on Read the Docs that will cancel the build immediately.
    - |
      if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/main -- . docs/ recurring_ical_events/ *.rst .readthedocs.yaml docs/requirements.txt;
      then
        exit 183;
      fi
    - cd docs && make rtd-pr-preview

```

### `benchmark/__init__.py`

```py

```

### `benchmark/issue42.py`

```py
# py3
#
# This is the benchmark for rrule speed
# see https://github.com/niccokunzmann/python-recurring-ical-events/issues/42
#

import sys
from pathlib import Path

import icalendar

import recurring_ical_events

HERE = Path(__file__).parent or Path()
sys.path.append(HERE.parent)


# read utf
text = []
with Path(HERE / "issue42.ics").open("rb") as fobj:
    text += fobj.readlines()
text_utf = [i.decode("utf-8") for i in text]

ical_string = "".join(text_utf)


calendar = icalendar.Calendar.from_ical(ical_string)

rec_calendar = recurring_ical_events.of(calendar)

for day in range(1, 29):
    print("day", day)  # noqa: T201
    start_date = (2011, 11, day)
    events = rec_calendar.at(start_date)

```

### `benchmark/issue42.txt`

```txt
day 1
day 2
day 3
day 4
day 5
day 6
day 7
day 8
day 9
day 10
day 11
day 12
day 13
day 14
day 15
day 16
day 17
day 18
day 19
day 20
day 21
day 22
day 23
day 24
day 25
day 26
day 27
day 28
         8887586 function calls (8860125 primitive calls) in 20.885 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  141/135    0.002    0.000    0.009    0.000 :0(__build_class__)
    70617    0.071    0.000    0.071    0.000 :0(__contains__)
    67994    0.070    0.000    0.070    0.000 :0(__getitem__)
        6    0.000    0.000    0.002    0.000 :0(__import__)
   141909    0.190    0.000    0.190    0.000 :0(__new__)
        9    0.000    0.000    0.000    0.000 :0(_abc_init)
        4    0.000    0.000    0.000    0.000 :0(_abc_register)
      8/4    0.000    0.000    0.000    0.000 :0(_abc_subclasscheck)
       39    0.000    0.000    0.000    0.000 :0(_fix_co_filename)
        1    0.000    0.000    0.000    0.000 :0(_getframe)
       96    0.000    0.000    0.000    0.000 :0(abs)
     4797    0.006    0.000    0.006    0.000 :0(acquire)
      286    0.000    0.000    0.000    0.000 :0(acquire_lock)
    19762    0.062    0.000    0.082    0.000 :0(add)
       72    0.000    0.000    0.000    0.000 :0(all)
     4877    0.005    0.000    0.005    0.000 :0(allocate_lock)
     4782    0.011    0.000    0.025    0.000 :0(any)
   127574    0.115    0.000    0.115    0.000 :0(append)
        4    0.000    0.000    0.000    0.000 :0(ascii_iscased)
        4    0.000    0.000    0.000    0.000 :0(ascii_tolower)
    38232    0.056    0.000    0.056    0.000 :0(bisect_right)
        1    0.000    0.000    0.000    0.000 :0(bit_length)
        6    0.000    0.000    0.000    0.000 :0(calcsize)
       72    0.000    0.000    0.000    0.000 :0(callable)
        2    0.000    0.000    0.000    0.000 :0(cast)
      596    0.002    0.000    0.002    0.000 :0(close)
     1528    0.004    0.000    0.004    0.000 :0(combine)
       13    0.000    0.000    0.000    0.000 :0(compile)
       44    0.001    0.000    0.010    0.000 :0(copy)
        6    0.000    0.000    0.000    0.000 :0(create_builtin)
        1    0.000    0.000    0.002    0.002 :0(create_dynamic)
       39    0.000    0.000    0.000    0.000 :0(date)
    72212    0.062    0.000    0.062    0.000 :0(decode)
       76    0.000    0.000    0.000    0.000 :0(delattr)
       77    0.000    0.000    0.000    0.000 :0(divmod)
     1743    0.002    0.000    0.002    0.000 :0(encode)
     1820    0.002    0.000    0.002    0.000 :0(endswith)
     42/1    0.000    0.000   20.884   20.884 :0(exec)
        6    0.000    0.000    0.000    0.000 :0(exec_builtin)
        1    0.000    0.000    0.000    0.000 :0(exec_dynamic)
       40    0.001    0.000    0.048    0.001 :0(extend)
      526    0.001    0.000    0.001    0.000 :0(find)
    77533    0.127    0.000    0.127    0.000 :0(findall)
        7    0.000    0.000    0.000    0.000 :0(format)
      117    0.000    0.000    0.000    0.000 :0(from_bytes)
       18    0.000    0.000    0.000    0.000 :0(fromkeys)
     1528    0.005    0.000    0.005    0.000 :0(fromordinal)
     1313    0.001    0.000    0.001    0.000 :0(fspath)
    86048    0.091    0.000    0.091    0.000 :0(get)
      112    0.000    0.000    0.000    0.000 :0(get_ident)
   174035    0.166    0.000    0.166    0.000 :0(getattr)
        1    0.000    0.000    0.000    0.000 :0(globals)
      146    0.000    0.000    0.000    0.000 :0(groupdict)
      414    0.001    0.000    0.001    0.000 :0(groups)
     3189    0.004    0.000    0.004    0.000 :0(hasattr)
     9556    0.012    0.000    0.012    0.000 :0(heapify)
     4854    0.004    0.000    0.004    0.000 :0(heappop)
     1146    0.001    0.000    0.002    0.000 :0(heapreplace)
        5    0.000    0.000    0.000    0.000 :0(insert)
        4    0.000    0.000    0.000    0.000 :0(intern)
        2    0.000    0.000    0.000    0.000 :0(intersection)
       21    0.000    0.000    0.000    0.000 :0(is_builtin)
      144    0.000    0.000    0.000    0.000 :0(is_finite)
       42    0.000    0.000    0.000    0.000 :0(is_frozen)
      360    0.000    0.000    0.000    0.000 :0(isalpha)
     1368    0.001    0.000    0.001    0.000 :0(isdigit)
       12    0.000    0.000    0.000    0.000 :0(isidentifier)
  1279260    1.136    0.000    1.136    0.000 :0(isinstance)
   314422    0.354    0.000    0.354    0.000 :0(items)
    81269    0.118    0.000    0.119    0.000 :0(iter)
     1076    0.005    0.000    0.021    0.000 :0(join)
      170    0.000    0.000    0.000    0.000 :0(keys)
200109/200039    0.230    0.000    0.233    0.000 :0(len)
        7    0.000    0.000    0.000    0.000 :0(listdir)
       39    0.002    0.000    0.002    0.000 :0(loads)
        1    0.000    0.000    0.000    0.000 :0(localtime)
     9722    0.008    0.000    0.008    0.000 :0(locked)
     1607    0.001    0.000    0.001    0.000 :0(lower)
      596    0.001    0.000    0.001    0.000 :0(lstrip)
        2    0.000    0.000    0.000    0.000 :0(maketrans)
      560    0.002    0.000    0.002    0.000 :0(match)
    38238    0.051    0.000    0.051    0.000 :0(max)
      145    0.000    0.000    0.000    0.000 :0(min)
32338/10616    0.058    0.000    0.363    0.000 :0(next)
       72    0.000    0.000    0.000    0.000 :0(now)
      597    0.004    0.000    0.004    0.000 :0(open)
       39    0.000    0.000    0.000    0.000 :0(open_code)
       75    0.000    0.000    0.000    0.000 :0(ord)
    15035    0.021    0.000    0.021    0.000 :0(pop)
       28    0.000    0.000    0.000    0.000 :0(print)
     1269    0.002    0.000    0.002    0.000 :0(read)
        1    0.004    0.004    0.004    0.004 :0(readlines)
      109    0.000    0.000    0.000    0.000 :0(release)
      286    0.000    0.000    0.000    0.000 :0(release_lock)
        2    0.000    0.000    0.000    0.000 :0(remove)
  1419016    1.625    0.000    1.625    0.000 :0(replace)
        1    0.000    0.000    0.000    0.000 :0(repr)
      597    0.001    0.000    0.001    0.000 :0(rfind)
       12    0.000    0.000    0.000    0.000 :0(round)
      358    0.001    0.000    0.001    0.000 :0(rpartition)
     1535    0.001    0.000    0.001    0.000 :0(rstrip)
     3732    0.003    0.000    0.003    0.000 :0(setattr)
        1    0.000    0.000    0.000    0.000 :0(setdefault)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(setter)
     9726    0.013    0.000    0.013    0.000 :0(sort)
      718    0.002    0.000    0.003    0.000 :0(sorted)
     3947    0.042    0.000    0.042    0.000 :0(split)
    29441    0.035    0.000    0.035    0.000 :0(startswith)
      782    0.003    0.000    0.003    0.000 :0(stat)
      175    0.000    0.000    0.000    0.000 :0(strip)
        1    0.078    0.078    0.078    0.078 :0(sub)
       72    0.001    0.000    0.003    0.000 :0(sum)
       41    0.000    0.000    0.000    0.000 :0(timestamp)
      168    0.001    0.000    0.002    0.000 :0(timetuple)
        2    0.000    0.000    0.000    0.000 :0(tolist)
     1416    0.003    0.000    0.003    0.000 :0(toordinal)
        9    0.000    0.000    0.000    0.000 :0(translate)
        5    0.000    0.000    0.000    0.000 :0(unicode_iscased)
        6    0.000    0.000    0.000    0.000 :0(unpack)
        8    0.000    0.000    0.000    0.000 :0(update)
   447889    0.468    0.000    0.468    0.000 :0(upper)
        2    0.000    0.000    0.000    0.000 :0(utcfromtimestamp)
     2353    0.005    0.000    0.005    0.000 :0(weekday)
    22/21    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:1017(_handle_fromlist)
       56    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
       48    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
       48    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:147(__enter__)
       48    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       56    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
       48    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
     56/2    0.000    0.000    0.050    0.025 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
      452    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:232(_requires_builtin_wrapper)
       49    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:342(__init__)
       39    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
       79    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:376(cached)
       66    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:389(parent)
       46    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:397(has_location)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(spec_from_loader)
       46    0.001    0.000    0.003    0.000 <frozen importlib._bootstrap>:477(_init_module_attrs)
    46/45    0.000    0.000    0.005    0.000 <frozen importlib._bootstrap>:549(module_from_spec)
       48    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:613(_load_backward_compatible)
     47/2    0.000    0.000    0.050    0.025 <frozen importlib._bootstrap>:650(_load_unlocked)
       48    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:725(find_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:746(create_module)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:754(exec_module)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:771(is_package)
       56    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
       42    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:800(find_spec)
      182    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:863(__enter__)
      182    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:867(__exit__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:881(_find_spec_legacy)
       48    0.001    0.000    0.011    0.000 <frozen importlib._bootstrap>:890(_find_spec)
     48/2    0.000    0.000    0.051    0.026 <frozen importlib._bootstrap>:956(_find_and_load_unlocked)
     48/2    0.001    0.000    0.051    0.026 <frozen importlib._bootstrap>:986(_find_and_load)
       39    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1010(path_stats)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:104(_path_isdir)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1088(__init__)
        1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap_external>:1099(create_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1107(exec_module)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1252(_path_hooks)
       92    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1265(_path_importer_cache)
       42    0.001    0.000    0.008    0.000 <frozen importlib._bootstrap_external>:1302(_get_spec)
       42    0.000    0.000    0.009    0.000 <frozen importlib._bootstrap_external>:1334(find_spec)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1394(__init__)
       56    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1400(<genexpr>)
       40    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1426(_get_spec)
       78    0.002    0.000    0.007    0.000 <frozen importlib._bootstrap_external>:1431(find_spec)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1479(_fill_cache)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1520(path_hook_for_FileFinder)
       78    0.001    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:294(cache_from_source)
       78    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:40(_relax_case)
       40    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:424(_get_cached)
       39    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:456(_check_name_wrapper)
       39    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:493(_classify_pyc)
      117    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:51(_unpack_uint32)
       39    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:526(_validate_timestamp_pyc)
       39    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:578(_compile_bytecode)
      430    0.001    0.000    0.004    0.000 <frozen importlib._bootstrap_external>:62(_path_join)
       40    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:629(spec_from_file_location)
      430    0.001    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:64(<listcomp>)
       78    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:68(_path_split)
       39    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:774(create_module)
     39/2    0.000    0.000    0.050    0.025 <frozen importlib._bootstrap_external>:777(exec_module)
      186    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:80(_path_stat)
       39    0.001    0.000    0.007    0.000 <frozen importlib._bootstrap_external>:849(get_code)
       62    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:90(_path_is_mode_type)
       39    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:939(__init__)
       39    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:964(get_filename)
       39    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:969(get_data)
       55    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:99(_path_isfile)
        7    0.000    0.000    0.000    0.000 <frozen zipimport>:63(__init__)
        2    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 __future__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 __future__.py:80(_Feature)
       10    0.000    0.000    0.000    0.000 __future__.py:81(__init__)
        1    0.000    0.000    0.004    0.004 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:11(DeprecatedTzFormatWarning)
      594    0.001    0.000    0.047    0.000 __init__.py:1104(<genexpr>)
      593    0.002    0.000    0.046    0.000 __init__.py:111(resource_exists)
      334    0.002    0.000    0.017    0.000 __init__.py:123(timezone)
      334    0.001    0.000    0.002    0.000 __init__.py:186(_unmunge_zone)
      334    0.002    0.000    0.004    0.000 __init__.py:194(_case_insensitive_zone_lookup)
      594    0.001    0.000    0.002    0.000 __init__.py:198(<genexpr>)
        4    0.000    0.000    0.057    0.014 __init__.py:2(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:206(UTC)
        1    0.000    0.000    0.000    0.000 __init__.py:21(__deprecated_private_func)
       31    0.000    0.000    0.000    0.000 __init__.py:223(utcoffset)
        1    0.000    0.000    0.000    0.000 __init__.py:229(dst)
   262817    0.505    0.000    1.016    0.000 __init__.py:235(localize)
        1    0.000    0.000    0.000    0.000 __init__.py:306(_CountryTimezoneDict)
        1    0.000    0.000    0.000    0.000 __init__.py:313(namedtuple)
        3    0.000    0.000    0.000    0.000 __init__.py:36(__deprecate_private_class)
        1    0.000    0.000    0.000    0.000 __init__.py:365(_CountryNameDict)
        4    0.000    0.000    0.000    0.000 __init__.py:385(<genexpr>)
        1    0.000    0.000    0.000    0.000 __init__.py:391(_FixedOffset)
        3    0.000    0.000    0.000    0.000 __init__.py:43(private_class)
      334    0.001    0.000    0.001    0.000 __init__.py:47(ascii)
      596    0.007    0.000    0.043    0.000 __init__.py:78(open_resource)
      596    0.002    0.000    0.006    0.000 _collections_abc.py:657(get)
        2    0.000    0.000    0.000    0.000 _common.py:1(<module>)
       57    0.000    0.000    0.000    0.000 _common.py:13(__call__)
        6    0.000    0.000    0.000    0.000 _common.py:13(tzname_in_python2)
        3    0.000    0.000    0.000    0.000 _common.py:132(_validate_fromutc_inputs)
        1    0.000    0.000    0.000    0.000 _common.py:149(_tzinfo)
        1    0.000    0.000    0.000    0.000 _common.py:267(tzrangebase)
        1    0.000    0.000    0.000    0.000 _common.py:6(weekday)
       75    0.000    0.000    0.000    0.000 _common.py:9(__init__)
        1    0.000    0.000    0.000    0.000 _factories.py:1(<module>)
        1    0.000    0.000    0.000    0.000 _factories.py:13(__call__)
        1    0.000    0.000    0.000    0.000 _factories.py:19(_TzFactory)
        1    0.000    0.000    0.000    0.000 _factories.py:25(_TzOffsetFactory)
        1    0.000    0.000    0.000    0.000 _factories.py:26(__init__)
        1    0.000    0.000    0.000    0.000 _factories.py:55(_TzStrFactory)
        1    0.000    0.000    0.000    0.000 _factories.py:56(__init__)
        1    0.000    0.000    0.000    0.000 _factories.py:8(_TzSingleton)
        1    0.000    0.000    0.000    0.000 _factories.py:9(__init__)
      144    0.000    0.000    0.001    0.000 _parser.py:1062(_could_be_tzname)
      144    0.000    0.000    0.000    0.000 _parser.py:1067(<genexpr>)
       72    0.000    0.000    0.000    0.000 _parser.py:1139(_parsems)
      144    0.001    0.000    0.001    0.000 _parser.py:1147(_to_decimal)
       72    0.000    0.000    0.001    0.000 _parser.py:1183(_build_tzaware)
       72    0.001    0.000    0.002    0.000 _parser.py:1223(_build_naive)
       72    0.000    0.000    0.038    0.001 _parser.py:1276(parse)
        1    0.000    0.000    0.000    0.000 _parser.py:1377(_tzparser)
        1    0.000    0.000    0.000    0.000 _parser.py:1379(_result)
        1    0.000    0.000    0.000    0.000 _parser.py:1384(_attr)
        1    0.000    0.000    0.000    0.000 _parser.py:1595(ParserError)
        1    0.000    0.000    0.000    0.000 _parser.py:1607(UnknownTimezoneWarning)
       72    0.000    0.000    0.000    0.000 _parser.py:192(__iter__)
      360    0.001    0.000    0.012    0.000 _parser.py:195(__next__)
        1    0.000    0.000    0.009    0.009 _parser.py:2(<module>)
       72    0.001    0.000    0.013    0.000 _parser.py:205(split)
      360    0.001    0.000    0.001    0.000 _parser.py:209(isword)
     1152    0.002    0.000    0.003    0.000 _parser.py:214(isnum)
        1    0.000    0.000    0.000    0.000 _parser.py:225(_resultbase)
       72    0.002    0.000    0.002    0.000 _parser.py:227(__init__)
       72    0.000    0.000    0.004    0.000 _parser.py:239(__len__)
      936    0.002    0.000    0.002    0.000 _parser.py:240(<genexpr>)
        1    0.000    0.000    0.000    0.000 _parser.py:247(parserinfo)
        1    0.000    0.000    0.000    0.000 _parser.py:300(__init__)
        7    0.000    0.000    0.000    0.000 _parser.py:315(_convert)
       72    0.000    0.000    0.000    0.000 _parser.py:325(jump)
      144    0.000    0.000    0.000    0.000 _parser.py:328(weekday)
      144    0.000    0.000    0.000    0.000 _parser.py:335(month)
      144    0.000    0.000    0.000    0.000 _parser.py:348(ampm)
       72    0.000    0.000    0.000    0.000 _parser.py:360(tzoffset)
       72    0.000    0.000    0.000    0.000 _parser.py:366(convertyear)
       72    0.000    0.000    0.000    0.000 _parser.py:386(validate)
        1    0.000    0.000    0.000    0.000 _parser.py:400(_ymd)
       72    0.000    0.000    0.000    0.000 _parser.py:401(__init__)
       72    0.000    0.000    0.000    0.000 _parser.py:408(has_year)
      216    0.001    0.000    0.002    0.000 _parser.py:434(append)
       72    0.001    0.000    0.001    0.000 _parser.py:480(resolve_ymd)
       72    0.000    0.000    0.000    0.000 _parser.py:488(<dictcomp>)
        1    0.000    0.000    0.000    0.000 _parser.py:574(parser)
        1    0.000    0.000    0.000    0.000 _parser.py:575(__init__)
       72    0.001    0.000    0.037    0.001 _parser.py:578(parse)
        1    0.000    0.000    0.001    0.001 _parser.py:58(_timelex)
       72    0.000    0.000    0.000    0.000 _parser.py:62(__init__)
        1    0.000    0.000    0.000    0.000 _parser.py:667(_result)
       72    0.003    0.000    0.029    0.000 _parser.py:672(_parse)
      360    0.005    0.000    0.011    0.000 _parser.py:83(get_token)
      144    0.002    0.000    0.006    0.000 _parser.py:881(_parse_numeric_token)
        1    0.000    0.000    0.000    0.000 _version.py:4(<module>)
       48    0.000    0.000    0.000    0.000 _virtualenv.py:51(find_spec)
        1    0.000    0.000    0.000    0.000 abc.py:1(<module>)
      8/4    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
       42    0.000    0.000    0.000    0.000 abc.py:7(abstractmethod)
        9    0.000    0.000    0.000    0.000 abc.py:84(__new__)
        4    0.000    0.000    0.000    0.000 abc.py:89(register)
        1    0.000    0.000    0.000    0.000 base64.py:3(<module>)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
    60425    0.086    0.000    0.086    0.000 cal.py:118(_encode)
    60425    0.412    0.000    1.562    0.000 cal.py:156(add)
        1    0.000    0.000    0.037    0.037 cal.py:2(<module>)
     5206    0.011    0.000    0.016    0.000 cal.py:267(add_component)
   5210/2    0.019    0.000    0.023    0.012 cal.py:272(_walk)
        2    0.000    0.000    0.023    0.012 cal.py:282(walk)
        1    0.000    0.000    0.000    0.000 cal.py:29(ComponentFactory)
        1    0.834    0.834   13.301   13.301 cal.py:319(from_ical)
        1    0.000    0.000    0.000    0.000 cal.py:34(__init__)
        1    0.000    0.000    0.000    0.000 cal.py:443(Event)
        1    0.000    0.000    0.000    0.000 cal.py:468(Todo)
        1    0.000    0.000    0.000    0.000 cal.py:486(Journal)
        1    0.000    0.000    0.000    0.000 cal.py:501(FreeBusy)
        1    0.000    0.000    0.000    0.000 cal.py:513(Timezone)
        2    0.000    0.000    0.016    0.008 cal.py:519(_extract_offsets)
        2    0.000    0.000    0.000    0.000 cal.py:559(<listcomp>)
        1    0.000    0.000    0.016    0.016 cal.py:580(to_tz)
        1    0.000    0.000    0.000    0.000 cal.py:60(Component)
        1    0.000    0.000    0.000    0.000 cal.py:616(<listcomp>)
        1    0.000    0.000    0.000    0.000 cal.py:654(TimezoneStandard)
        1    0.000    0.000    0.000    0.000 cal.py:661(TimezoneDaylight)
        1    0.000    0.000    0.000    0.000 cal.py:668(Alarm)
        1    0.000    0.000    0.000    0.000 cal.py:681(Calendar)
     5289    0.017    0.000    0.051    0.000 cal.py:79(__init__)
    60427    0.053    0.000    0.053    0.000 cal.py:98(__bool__)
        1    0.000    0.000    0.000    0.000 calendar.py:1(<module>)
     2190    0.002    0.000    0.002    0.000 calendar.py:100(isleap)
      177    0.000    0.000    0.001    0.000 calendar.py:113(weekday)
      177    0.000    0.000    0.001    0.000 calendar.py:120(monthrange)
        1    0.000    0.000    0.000    0.000 calendar.py:148(Calendar)
        1    0.000    0.000    0.000    0.000 calendar.py:154(__init__)
      155    0.000    0.000    0.000    0.000 calendar.py:157(getfirstweekday)
        1    0.000    0.000    0.000    0.000 calendar.py:160(setfirstweekday)
        1    0.000    0.000    0.000    0.000 calendar.py:24(IllegalMonthError)
        1    0.000    0.000    0.000    0.000 calendar.py:293(TextCalendar)
        1    0.000    0.000    0.000    0.000 calendar.py:31(IllegalWeekdayError)
        1    0.000    0.000    0.000    0.000 calendar.py:410(HTMLCalendar)
        1    0.000    0.000    0.000    0.000 calendar.py:50(_localized_month)
        1    0.000    0.000    0.000    0.000 calendar.py:52(<listcomp>)
        1    0.000    0.000    0.000    0.000 calendar.py:546(different_locale)
        2    0.000    0.000    0.000    0.000 calendar.py:55(__init__)
        1    0.000    0.000    0.000    0.000 calendar.py:558(LocaleTextCalendar)
        1    0.000    0.000    0.000    0.000 calendar.py:589(LocaleHTMLCalendar)
        1    0.000    0.000    0.000    0.000 calendar.py:69(_localized_day)
        1    0.000    0.000    0.000    0.000 calendar.py:72(<listcomp>)
        2    0.000    0.000    0.000    0.000 calendar.py:74(__init__)
      168    0.000    0.000    0.010    0.000 caselessdict.py:103(sorted_items)
      168    0.000    0.000    0.000    0.000 caselessdict.py:12(<dictcomp>)
      168    0.000    0.000    0.000    0.000 caselessdict.py:13(<listcomp>)
      168    0.000    0.000    0.000    0.000 caselessdict.py:14(<listcomp>)
      398    0.000    0.000    0.000    0.000 caselessdict.py:15(<lambda>)
      168    0.001    0.000    0.009    0.000 caselessdict.py:18(canonsort_items)
        1    0.000    0.000    0.001    0.001 caselessdict.py:2(<module>)
      168    0.001    0.000    0.004    0.000 caselessdict.py:21(<listcomp>)
        1    0.000    0.000    0.000    0.000 caselessdict.py:25(CaselessDict)
   242855    1.050    0.000    1.832    0.000 caselessdict.py:30(__init__)
    67994    0.283    0.000    0.598    0.000 caselessdict.py:40(__getitem__)
    93445    0.365    0.000    0.707    0.000 caselessdict.py:44(__setitem__)
       10    0.000    0.000    0.000    0.000 caselessdict.py:48(__delitem__)
    70612    0.301    0.000    0.629    0.000 caselessdict.py:52(__contains__)
    85251    0.377    0.000    0.781    0.000 caselessdict.py:56(get)
      354    0.003    0.000    0.010    0.000 caselessdict.py:75(update)
      168    0.002    0.000    0.004    0.000 caselessdict.py:8(canonsort_keys)
       41    0.000    0.000    0.023    0.001 caselessdict.py:84(copy)
    71547    0.212    0.000    0.384    0.000 compat.py:12(<lambda>)
        1    0.000    0.000    0.000    0.000 compat.py:2(<module>)
        1    0.000    0.000    0.002    0.002 datetime.py:1(<module>)
        1    0.000    0.000    0.000    0.000 datetime.py:1141(tzinfo)
        1    0.000    0.000    0.000    0.000 datetime.py:1211(time)
        2    0.000    0.000    0.000    0.000 datetime.py:1236(__new__)
        1    0.000    0.000    0.000    0.000 datetime.py:1558(datetime)
        3    0.000    0.000    0.000    0.000 datetime.py:1566(__new__)
        1    0.000    0.000    0.000    0.000 datetime.py:2179(timezone)
        3    0.000    0.000    0.000    0.000 datetime.py:2199(_create)
       35    0.000    0.000    0.000    0.000 datetime.py:379(_check_int_field)
        3    0.000    0.000    0.000    0.000 datetime.py:41(_days_before_year)
        5    0.000    0.000    0.000    0.000 datetime.py:411(_check_date_fields)
        5    0.000    0.000    0.000    0.000 datetime.py:424(_check_time_fields)
        5    0.000    0.000    0.000    0.000 datetime.py:441(_check_tzinfo_arg)
        5    0.000    0.000    0.000    0.000 datetime.py:46(_days_in_month)
        1    0.000    0.000    0.000    0.000 datetime.py:469(timedelta)
       12    0.001    0.000    0.001    0.000 datetime.py:488(__new__)
        2    0.000    0.000    0.000    0.000 datetime.py:661(__neg__)
        1    0.000    0.000    0.000    0.000 datetime.py:789(date)
        2    0.000    0.000    0.000    0.000 datetime.py:819(__new__)
        1    0.000    0.000    0.002    0.002 decimal.py:2(<module>)
       28    0.000    0.000    0.000    0.000 enum.py:278(__call__)
       28    0.000    0.000    0.000    0.000 enum.py:557(__new__)
       11    0.000    0.000    0.000    0.000 enum.py:654(name)
        2    0.000    0.000    0.000    0.000 enum.py:659(value)
        1    0.000    0.000    0.000    0.000 enum.py:785(_missing_)
        1    0.000    0.000    0.000    0.000 enum.py:792(_create_pseudo_member_)
        1    0.000    0.000    0.000    0.000 enum.py:822(__or__)
       13    0.000    0.000    0.000    0.000 enum.py:828(__and__)
        1    0.000    0.000    0.000    0.000 enum.py:847(_high_bit)
        1    0.000    0.000    0.000    0.000 enum.py:864(_decompose)
        1    0.000    0.000    0.000    0.000 enum.py:881(<listcomp>)
        2    0.000    0.000    0.000    0.000 enum.py:893(<lambda>)
        2    0.000    0.000    0.000    0.000 enum.py:899(_power_of_two)
        1    0.000    0.000    0.000    0.000 exceptions.py:1(<module>)
        1    0.000    0.000    0.000    0.000 exceptions.py:11(Error)
        1    0.000    0.000    0.000    0.000 exceptions.py:15(UnknownTimeZoneError)
        1    0.000    0.000    0.000    0.000 exceptions.py:38(InvalidTimeError)
        1    0.000    0.000    0.000    0.000 exceptions.py:42(AmbiguousTimeError)
        1    0.000    0.000    0.000    0.000 exceptions.py:53(NonExistentTimeError)
        8    0.000    0.000    0.000    0.000 functools.py:33(update_wrapper)
        8    0.000    0.000    0.000    0.000 functools.py:63(wraps)
      596    0.001    0.000    0.004    0.000 genericpath.py:16(exists)
        1    0.000    0.000    0.001    0.001 isoparser.py:2(<module>)
        4    0.000    0.000    0.000    0.000 isoparser.py:22(_takes_ascii)
        1    0.000    0.000    0.001    0.001 isoparser.py:42(isoparser)
        1    0.000    0.000    0.000    0.000 isoparser.py:43(__init__)
        1    0.124    0.124   20.884   20.884 issue42.py:7(<module>)
        1    0.000    0.000    0.001    0.001 lazy.py:1(<module>)
        1    0.000    0.000    0.000    0.000 lazy.py:118(<listcomp>)
        1    0.000    0.000    0.000    0.000 lazy.py:121(LazySet)
        2    0.000    0.000    0.001    0.000 lazy.py:139(__new__)
        2    0.000    0.000    0.000    0.000 lazy.py:144(LazySet)
       84    0.000    0.000    0.000    0.000 lazy.py:149(lazy)
        1    0.001    0.001    0.001    0.001 lazy.py:150(_lazy)
        1    0.000    0.000    0.000    0.000 lazy.py:16(LazyDict)
        1    0.000    0.000    0.000    0.000 lazy.py:172(<listcomp>)
        1    0.000    0.000    0.000    0.000 lazy.py:71(LazyList)
        2    0.000    0.000    0.000    0.000 lazy.py:84(__new__)
        2    0.000    0.000    0.000    0.000 lazy.py:91(LazyList)
       62    0.000    0.000    0.000    0.000 lazy.py:96(lazy)
        1    0.000    0.000    0.048    0.048 lazy.py:97(_lazy)
        1    0.000    0.000    0.000    0.000 numbers.py:12(Number)
        1    0.000    0.000    0.000    0.000 numbers.py:147(Real)
        1    0.000    0.000    0.000    0.000 numbers.py:267(Rational)
        1    0.000    0.000    0.000    0.000 numbers.py:294(Integral)
        1    0.000    0.000    0.000    0.000 numbers.py:32(Complex)
        1    0.000    0.000    0.000    0.000 numbers.py:4(<module>)
      596    0.002    0.000    0.005    0.000 os.py:670(__getitem__)
      596    0.002    0.000    0.003    0.000 os.py:748(encode)
    74102    0.229    0.000    0.420    0.000 parser.py:124(validate_token)
     3263    0.007    0.000    0.011    0.000 parser.py:131(validate_param_value)
    77365    0.302    0.000    0.423    0.000 parser.py:154(q_split)
        1    0.000    0.000    0.000    0.000 parser.py:185(Parameters)
        1    0.000    0.000    0.029    0.029 parser.py:2(<module>)
    70839    0.392    0.000    1.186    0.000 parser.py:230(from_ical)
    70839    0.321    0.000    0.576    0.000 parser.py:267(escape_string)
   148204    0.657    0.000    1.158    0.000 parser.py:273(unescape_string)
     3263    0.009    0.000    0.037    0.000 parser.py:278(unescape_list_or_string)
        1    0.000    0.000    0.000    0.000 parser.py:288(Contentline)
    70839    0.272    0.000    0.543    0.000 parser.py:292(__new__)
    70839    1.024    0.000    5.305    0.000 parser.py:321(parts)
    30559    0.252    0.000    0.460    0.000 parser.py:33(unescape_char)
    74102    0.092    0.000    0.155    0.000 parser.py:345(<genexpr>)
        1    0.000    0.000    0.000    0.000 parser.py:372(Contentlines)
        1    0.063    0.063    0.876    0.876 parser.py:382(from_ical)
    70840    0.155    0.000    0.698    0.000 parser.py:390(<genexpr>)
      426    0.001    0.000    0.001    0.000 parser.py:52(tzid_from_dt)
        1    0.000    0.000    0.000    0.000 parser_tools.py:2(<module>)
   477782    0.874    0.000    1.287    0.000 parser_tools.py:9(to_unicode)
      597    0.004    0.000    0.008    0.000 posixpath.py:150(dirname)
     1195    0.002    0.000    0.003    0.000 posixpath.py:41(_get_sep)
      598    0.006    0.000    0.012    0.000 posixpath.py:71(join)
        1    0.000    0.000   20.885   20.885 profile:0(<code object <module> at 0x7f81180a2240, file "benchmark/issue42.py", line 7>)
        0    0.000             0.000          profile:0(profiler)
    60425    0.205    0.000    1.296    0.000 prop.py:1025(for_property)
        1    0.000    0.000    0.000    0.000 prop.py:109(LocalTimezone)
        1    0.000    0.000    0.000    0.000 prop.py:136(vBinary)
        1    0.000    0.000    0.000    0.000 prop.py:158(vBoolean)
        1    0.000    0.000    0.000    0.000 prop.py:181(vCalAddress)
     1148    0.006    0.000    0.016    0.000 prop.py:184(__new__)
      574    0.001    0.000    0.010    0.000 prop.py:196(from_ical)
        1    0.000    0.000    0.023    0.023 prop.py:2(<module>)
        1    0.000    0.000    0.000    0.000 prop.py:201(vFloat)
        1    0.000    0.000    0.000    0.000 prop.py:220(vInt)
     9764    0.045    0.000    0.099    0.000 prop.py:223(__new__)
      101    0.000    0.000    0.000    0.000 prop.py:228(to_ical)
     4885    0.013    0.000    0.065    0.000 prop.py:231(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:239(vDDDLists)
        1    0.000    0.000    0.000    0.000 prop.py:270(vCategory)
     1490    0.006    0.000    0.034    0.000 prop.py:272(__init__)
     1490    0.004    0.000    0.027    0.000 prop.py:275(<listcomp>)
     1490    0.005    0.000    0.029    0.000 prop.py:280(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:286(vDDDTypes)
    24470    0.197    0.000    0.819    0.000 prop.py:291(__init__)
       72    0.000    0.000    0.002    0.000 prop.py:315(to_ical)
    24389    0.171    0.000    0.561    0.000 prop.py:330(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:352(vDate)
      666    0.002    0.000    0.002    0.000 prop.py:365(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:378(vDatetime)
       72    0.000    0.000    0.001    0.000 prop.py:389(__init__)
       72    0.000    0.000    0.001    0.000 prop.py:393(to_ical)
    23309    0.116    0.000    0.278    0.000 prop.py:411(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:444(vDuration)
      414    0.004    0.000    0.006    0.000 prop.py:480(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:499(vPeriod)
        1    0.000    0.000    0.000    0.000 prop.py:571(vWeekday)
      146    0.002    0.000    0.005    0.000 prop.py:578(__new__)
       70    0.000    0.000    0.000    0.000 prop.py:594(to_ical)
       76    0.000    0.000    0.003    0.000 prop.py:597(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:605(vFrequency)
      342    0.003    0.000    0.009    0.000 prop.py:619(__new__)
      168    0.001    0.000    0.001    0.000 prop.py:627(to_ical)
      174    0.001    0.000    0.005    0.000 prop.py:630(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:638(vRecur)
      348    0.002    0.000    0.011    0.000 prop.py:669(__init__)
      168    0.003    0.000    0.036    0.000 prop.py:673(to_ical)
      809    0.002    0.000    0.016    0.000 prop.py:679(<genexpr>)
      416    0.002    0.000    0.019    0.000 prop.py:687(parse_type)
      416    0.001    0.000    0.013    0.000 prop.py:691(<listcomp>)
      174    0.004    0.000    0.033    0.000 prop.py:693(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:712(vText)
    59628    0.320    0.000    0.868    0.000 prop.py:716(__new__)
    29069    0.107    0.000    0.949    0.000 prop.py:729(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:735(vTime)
        1    0.000    0.000    0.000    0.000 prop.py:761(vUri)
       10    0.000    0.000    0.000    0.000 prop.py:765(__new__)
        5    0.000    0.000    0.000    0.000 prop.py:774(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:782(vGeo)
        1    0.000    0.000    0.000    0.000 prop.py:810(vUTCOffset)
       18    0.000    0.000    0.000    0.000 prop.py:819(__init__)
       18    0.000    0.000    0.000    0.000 prop.py:846(from_ical)
        1    0.000    0.000    0.000    0.000 prop.py:866(vInline)
        1    0.000    0.000    0.001    0.001 prop.py:885(TypesFactory)
        1    0.000    0.000    0.000    0.000 prop.py:893(__init__)
        1    0.000    0.000    0.000    0.000 prop.py:92(FixedOffset)
      168    0.001    0.000    0.002    0.000 re.py:231(findall)
       12    0.000    0.000    0.014    0.001 re.py:248(compile)
        1    0.000    0.000    0.000    0.000 re.py:268(escape)
      180    0.001    0.000    0.016    0.000 re.py:287(_compile)
        1    0.000    0.000    0.000    0.000 recurring_ical_events.py:100(UnfoldableCalendar)
        1    0.000    0.000    0.000    0.000 recurring_ical_events.py:102(RepeatedEvent)
        1    0.000    0.000    0.000    0.000 recurring_ical_events.py:105(Repetition)
       41    0.000    0.000    0.000    0.000 recurring_ical_events.py:112(__init__)
       41    0.001    0.000    0.029    0.001 recurring_ical_events.py:117(as_vevent)
       41    0.000    0.000    0.003    0.000 recurring_ical_events.py:128(is_in_span)
        1    0.000    0.000    0.012    0.012 recurring_ical_events.py:13(<module>)
     4778    0.078    0.000    0.649    0.000 recurring_ical_events.py:131(__init__)
      166    0.001    0.000    0.065    0.000 recurring_ical_events.py:165(create_rule_with_start)
     4778    0.050    0.000    0.123    0.000 recurring_ical_events.py:193(make_all_dates_comparable)
     9889    0.014    0.000    0.019    0.000 recurring_ical_events.py:204(<genexpr>)
     4778    0.005    0.000    0.005    0.000 recurring_ical_events.py:212(<listcomp>)
     4778    0.005    0.000    0.005    0.000 recurring_ical_events.py:213(<listcomp>)
       41    0.000    0.000    0.000    0.000 recurring_ical_events.py:215(_unify_exdate)
   133825    0.833    0.000    6.335    0.000 recurring_ical_events.py:223(within)
       82    0.000    0.000    0.000    0.000 recurring_ical_events.py:243(convert_to_original_type)
     4778    0.013    0.000    0.055    0.000 recurring_ical_events.py:249(_get_event_end)
        1    0.019    0.019    0.710    0.710 recurring_ical_events.py:259(__init__)
       84    0.000    0.000    0.000    0.000 recurring_ical_events.py:269(to_datetime)
       28    0.000    0.000    6.573    0.235 recurring_ical_events.py:293(at)
       28    0.201    0.007    6.572    0.235 recurring_ical_events.py:322(between)
       41    0.001    0.000    0.002    0.000 recurring_ical_events.py:329(add_event)
       41    0.000    0.000    0.000    0.000 recurring_ical_events.py:33(timestamp)
        1    0.000    0.000    0.710    0.710 recurring_ical_events.py:354(of)
     5207    0.010    0.000    0.014    0.000 recurring_ical_events.py:37(is_event)
        4    0.000    0.000    0.000    0.000 recurring_ical_events.py:41(convert_to_date)
   544938    1.294    0.000    3.452    0.000 recurring_ical_events.py:45(convert_to_datetime)
       41    0.000    0.000    0.003    0.000 recurring_ical_events.py:58(time_span_contains_event)
   133866    0.460    0.000    1.728    0.000 recurring_ical_events.py:83(make_comparable)
   133866    0.412    0.000    1.138    0.000 recurring_ical_events.py:93(<listcomp>)
   133825    0.310    0.000    2.042    0.000 recurring_ical_events.py:95(compare_greater)
        8    0.000    0.000    0.000    0.000 relativedelta.py:13(<genexpr>)
        1    0.000    0.000    0.000    0.000 relativedelta.py:18(relativedelta)
        1    0.000    0.000    0.000    0.000 relativedelta.py:2(<module>)
     7376    0.009    0.000    0.009    0.000 rrule.py:103(__iter__)
     9722    0.033    0.000    0.049    0.000 rrule.py:111(_invalidate_cache)
        1    0.000    0.000    0.000    0.000 rrule.py:1110(_iterinfo)
      168    0.003    0.000    0.005    0.000 rrule.py:1116(__init__)
     1282    0.018    0.000    0.029    0.000 rrule.py:1121(rebuild)
    15222    0.059    0.000    0.444    0.000 rrule.py:122(_iter_cached)
      992    0.004    0.000    0.004    0.000 rrule.py:1251(ydayset)
      176    0.001    0.000    0.001    0.000 rrule.py:1254(mdayset)
      285    0.002    0.000    0.002    0.000 rrule.py:1261(wdayset)
       41    0.000    0.000    0.000    0.000 rrule.py:1276(ddayset)
        1    0.000    0.000    0.000    0.000 rrule.py:1305(rruleset)
        1    0.000    0.000    0.000    0.000 rrule.py:1313(_genitem)
     9722    0.026    0.000    0.062    0.000 rrule.py:1314(__init__)
     6000    0.017    0.000    0.119    0.000 rrule.py:1323(__next__)
      314    0.000    0.000    0.000    0.000 rrule.py:1335(__lt__)
     4778    0.014    0.000    0.049    0.000 rrule.py:1347(__init__)
      166    0.000    0.000    0.000    0.000 rrule.py:1354(rrule)
     4778    0.009    0.000    0.013    0.000 rrule.py:1360(rdate)
    15560    0.100    0.000    0.345    0.000 rrule.py:1381(_iter)
     4778    0.005    0.000    0.006    0.000 rrule.py:1385(<listcomp>)
     4778    0.005    0.000    0.005    0.000 rrule.py:1390(<listcomp>)
        1    0.000    0.000    0.000    0.000 rrule.py:1416(_rrulestr)
       26    0.000    0.000    0.000    0.000 rrule.py:1472(_handle_int)
       75    0.000    0.000    0.001    0.000 rrule.py:1475(_handle_int_list)
       75    0.000    0.000    0.000    0.000 rrule.py:1476(<listcomp>)
      168    0.000    0.000    0.000    0.000 rrule.py:1490(_handle_FREQ)
       72    0.000    0.000    0.038    0.001 rrule.py:1493(_handle_UNTIL)
       13    0.000    0.000    0.000    0.000 rrule.py:1504(_handle_WKST)
       44    0.001    0.000    0.001    0.000 rrule.py:1507(_handle_BYWEEKDAY)
      168    0.004    0.000    0.058    0.000 rrule.py:1535(_parse_rfc_rrule)
      168    0.003    0.000    0.065    0.000 rrule.py:1613(_parse_rfc)
      168    0.001    0.000    0.066    0.000 rrule.py:1729(__call__)
        1    0.000    0.000    0.002    0.002 rrule.py:2(<module>)
   133784    0.283    0.000    0.761    0.000 rrule.py:269(between)
        1    0.000    0.000    0.000    0.000 rrule.py:303(rrule)
      168    0.006    0.000    0.011    0.000 rrule.py:426(__init__)
      242    0.000    0.000    0.000    0.000 rrule.py:562(<genexpr>)
      121    0.000    0.000    0.000    0.000 rrule.py:563(<genexpr>)
       40    0.000    0.000    0.000    0.000 rrule.py:609(<listcomp>)
        4    0.000    0.000    0.000    0.000 rrule.py:615(<listcomp>)
        1    0.000    0.000    0.000    0.000 rrule.py:65(weekday)
       68    0.000    0.000    0.000    0.000 rrule.py:69(__init__)
        8    0.000    0.000    0.000    0.000 rrule.py:76(<genexpr>)
     1528    0.071    0.000    0.124    0.000 rrule.py:774(_iter)
        4    0.000    0.000    0.000    0.000 rrule.py:79(_invalidates_cache)
     4944    0.017    0.000    0.064    0.000 rrule.py:84(inner_func)
        1    0.000    0.000    0.000    0.000 rrule.py:92(rrulebase)
     4946    0.015    0.000    0.035    0.000 rrule.py:93(__init__)
        1    0.000    0.000    0.000    0.000 six.py:103(MovedModule)
       46    0.000    0.000    0.000    0.000 six.py:105(__init__)
        2    0.000    0.000    0.000    0.000 six.py:114(_resolve)
        1    0.000    0.000    0.000    0.000 six.py:124(_LazyModule)
        6    0.000    0.000    0.000    0.000 six.py:126(__init__)
        1    0.000    0.000    0.000    0.000 six.py:139(MovedAttribute)
       88    0.000    0.000    0.000    0.000 six.py:141(__init__)
        1    0.000    0.000    0.000    0.000 six.py:159(_resolve)
        1    0.000    0.000    0.000    0.000 six.py:164(_SixMetaPathImporter)
        1    0.000    0.000    0.000    0.000 six.py:173(__init__)
       53    0.000    0.000    0.000    0.000 six.py:177(_add_module)
        5    0.000    0.000    0.000    0.000 six.py:181(_get_module)
        2    0.000    0.000    0.000    0.000 six.py:184(find_module)
        2    0.000    0.000    0.000    0.000 six.py:189(__get_module)
        1    0.000    0.000    0.000    0.000 six.py:195(load_module)
        1    0.000    0.000    0.000    0.000 six.py:209(is_package)
        1    0.001    0.001    0.002    0.002 six.py:21(<module>)
        1    0.000    0.000    0.000    0.000 six.py:229(_MovedItems)
        1    0.000    0.000    0.000    0.000 six.py:324(Module_six_moves_urllib_parse)
        1    0.000    0.000    0.000    0.000 six.py:366(Module_six_moves_urllib_error)
        1    0.000    0.000    0.000    0.000 six.py:386(Module_six_moves_urllib_request)
        1    0.000    0.000    0.000    0.000 six.py:438(Module_six_moves_urllib_response)
        1    0.000    0.000    0.000    0.000 six.py:459(Module_six_moves_urllib_robotparser)
        1    0.000    0.000    0.000    0.000 six.py:477(Module_six_moves_urllib)
        8    0.000    0.000    0.000    0.000 six.py:75(_add_doc)
        3    0.000    0.000    0.000    0.000 six.py:80(_import_module)
        1    0.000    0.000    0.000    0.000 six.py:86(_LazyDescr)
        3    0.000    0.000    0.000    0.000 six.py:864(add_metaclass)
        3    0.000    0.000    0.000    0.000 six.py:866(wrapper)
      134    0.000    0.000    0.000    0.000 six.py:88(__init__)
        3    0.000    0.000    0.000    0.000 six.py:91(__get__)
       27    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
       27    0.001    0.000    0.002    0.000 sre_compile.py:276(_optimize_charset)
        8    0.000    0.000    0.000    0.000 sre_compile.py:411(_mk_bitmap)
        8    0.000    0.000    0.000    0.000 sre_compile.py:413(<listcomp>)
        2    0.000    0.000    0.000    0.000 sre_compile.py:416(_bytes_to_codes)
       24    0.000    0.000    0.000    0.000 sre_compile.py:423(_simple)
        2    0.000    0.000    0.000    0.000 sre_compile.py:432(_generate_overlap_table)
       28    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
    17/13    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
       11    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
       13    0.000    0.000    0.002    0.000 sre_compile.py:536(_compile_info)
       26    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
       13    0.000    0.000    0.006    0.000 sre_compile.py:598(_code)
       27    0.000    0.000    0.000    0.000 sre_compile.py:65(_combine_flags)
    63/13    0.002    0.000    0.004    0.000 sre_compile.py:71(_compile)
       13    0.000    0.000    0.014    0.001 sre_compile.py:759(compile)
       70    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
      124    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
      320    0.001    0.000    0.001    0.000 sre_parse.py:164(__getitem__)
       26    0.000    0.000    0.000    0.000 sre_parse.py:168(__setitem__)
       77    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
    81/31    0.000    0.000    0.001    0.000 sre_parse.py:174(getwidth)
       13    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
      549    0.001    0.000    0.001    0.000 sre_parse.py:233(__next)
      196    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
      406    0.001    0.000    0.001    0.000 sre_parse.py:254(get)
        8    0.000    0.000    0.000    0.000 sre_parse.py:267(getuntil)
      110    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        1    0.000    0.000    0.000    0.000 sre_parse.py:288(seek)
        4    0.000    0.000    0.000    0.000 sre_parse.py:295(_class_escape)
        9    0.000    0.000    0.000    0.000 sre_parse.py:355(_escape)
       18    0.000    0.000    0.000    0.000 sre_parse.py:432(_uniq)
    40/13    0.001    0.000    0.008    0.001 sre_parse.py:435(_parse_sub)
    44/13    0.002    0.000    0.008    0.001 sre_parse.py:493(_parse)
       13    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
       62    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
       18    0.000    0.000    0.000    0.000 sre_parse.py:84(opengroup)
        2    0.000    0.000    0.000    0.000 sre_parse.py:861(_parse_flags)
       13    0.000    0.000    0.000    0.000 sre_parse.py:921(fix_flags)
       13    0.000    0.000    0.008    0.001 sre_parse.py:937(parse)
       18    0.000    0.000    0.000    0.000 sre_parse.py:96(closegroup)
        1    0.000    0.000    0.004    0.004 string.py:1(<module>)
        1    0.000    0.000    0.000    0.000 string.py:161(Formatter)
        1    0.000    0.000    0.000    0.000 string.py:57(_TemplateMetaclass)
        1    0.000    0.000    0.004    0.004 string.py:67(__init__)
        1    0.000    0.000    0.000    0.000 string.py:80(Template)
        1    0.000    0.000    0.000    0.000 struct.py:3(<module>)
        1    0.000    0.000    0.000    0.000 threading.py:81(RLock)
        1    0.000    0.000    0.000    0.000 timezone_cache.py:3(<module>)
       13    0.000    0.000    0.000    0.000 types.py:171(__get__)
        1    0.000    0.000    0.000    0.000 tz.py:1036(tzstr)
        1    0.000    0.000    0.000    0.000 tz.py:1156(_tzicalvtzcomp)
        1    0.000    0.000    0.000    0.000 tz.py:1167(_tzicalvtz)
        1    0.000    0.000    0.000    0.000 tz.py:1253(tzical)
        1    0.000    0.000    0.000    0.000 tz.py:132(tzoffset)
        1    0.000    0.000    0.000    0.000 tz.py:1470(__get_gettz)
        1    0.000    0.000    0.000    0.000 tz.py:1475(GettzFunc)
        1    0.000    0.000    0.000    0.000 tz.py:1545(__init__)
        1    0.000    0.000    0.007    0.007 tz.py:2(<module>)
        1    0.000    0.000    0.000    0.000 tz.py:201(tzlocal)
        1    0.000    0.000    0.000    0.000 tz.py:328(_ttinfo)
        1    0.000    0.000    0.000    0.000 tz.py:373(_tzfile)
        1    0.000    0.000    0.000    0.000 tz.py:386(tzfile)
        1    0.000    0.000    0.000    0.000 tz.py:41(tzutc)
      904    0.001    0.000    0.001    0.000 tz.py:74(utcoffset)
        1    0.000    0.000    0.000    0.000 tz.py:874(tzrange)
        4    0.000    0.000    0.000    0.000 tzfile.py:13(_byte_string)
        1    0.000    0.000    0.000    0.000 tzfile.py:2(<module>)
       15    0.000    0.000    0.000    0.000 tzfile.py:20(_std_string)
        3    0.002    0.001    0.006    0.002 tzfile.py:25(build_tzinfo)
        3    0.001    0.000    0.002    0.001 tzfile.py:42(<listcomp>)
        1    0.000    0.000    0.000    0.000 tzinfo.py:1(<module>)
        1    0.000    0.000    0.000    0.000 tzinfo.py:156(DstTzInfo)
     18/4    0.000    0.000    0.000    0.000 tzinfo.py:179(__init__)
       25    0.000    0.000    0.000    0.000 tzinfo.py:18(memorized_timedelta)
    19116    0.110    0.000    0.227    0.000 tzinfo.py:193(fromutc)
    19116    0.067    0.000    0.329    0.000 tzinfo.py:203(normalize)
     9558    0.238    0.000    0.830    0.000 tzinfo.py:258(localize)
      590    0.001    0.000    0.001    0.000 tzinfo.py:31(memorized_datetime)
    54241    0.054    0.000    0.054    0.000 tzinfo.py:396(utcoffset)
      156    0.000    0.000    0.000    0.000 tzinfo.py:427(dst)
      592    0.001    0.000    0.001    0.000 tzinfo.py:45(memorized_ttinfo)
        1    0.000    0.000    0.000    0.000 tzinfo.py:66(BaseTzInfo)
        1    0.000    0.000    0.000    0.000 tzinfo.py:76(StaticTzInfo)
        3    0.000    0.000    0.000    0.000 weakref.py:102(__init__)
        3    0.000    0.000    0.000    0.000 weakref.py:284(update)
        1    0.000    0.000    0.000    0.000 win.py:2(<module>)
        1    0.000    0.000    0.000    0.000 windows_to_olson.py:1(<module>)



```

### `benchmark/README.md`

```md
# speed tests

This folder contains speed tests. Run them from within the root folder (next to the module).

Get the time of a benchmark:
```
time python3 benchmark/issue42.py
```

Profile what takes time during a run:
```
python3 -m profile benchmark/issue42.py | tee benchmark/issue42.txt
```


```

### `docs/.gitignore`

```gitignore
venv
__pycache__
*.pyc
_*

```

### `docs/changelog.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      Versions and changes
---

# Changelog

We use [Semantic Versioning](https://semver.org)

- Breaking changes increase the **major** version number.
- New features increase the **minor** version number.
- Minor changes and bug fixes increase the **patch** version number.

To avoid breaking changes breaking your code, install this library fixed to a specific version.

## v3.9.0

- Add: `Occurrence`-returning query methods on `CalendarQuery` (`occurrences_at`, `occurrences_between`, `occurrences_after`, `occurrences_all`, `occurrences_count`, `first_occurrence`, and `occurrences_paginate`), and `OccurrencePage` / `OccurrencePages` to pair with the existing `Page` / `Pages`. See [Issue 217](https://github.com/niccokunzmann/python-recurring-ical-events/issues/217).

## v3.8.2

- Fix: Prevent additional events when replaced event with lower SEQUENCE has RRULE. See [Issue 253](https://github.com/niccokunzmann/python-recurring-ical-events/issues/253).

## v3.8.1

- Fix: License identifier in pyproject.toml
- Mark as compatible with `icalendar` versions `6.*` and `7.*`. See [Issue 257](https://github.com/niccokunzmann/python-recurring-ical-events/issues/257).
- Test compatibility to Python 3.14.
- Documentation:
  - Fix documentation build dependencies.
  - Build documentation with Python 3.14 and icalendar>=7.0.0.

## v3.8.0

- Fix: Invalid events and todos that swapped start and end are now calculated with start before end. See [Issue 132](https://github.com/niccokunzmann/python-recurring-ical-events/issues/132).

## v3.7.1

- Fix: RECURENCE-ID is now not identical to DTSTART. See [Issue 243](https://github.com/niccokunzmann/python-recurring-ical-events/issues/243).

## v3.7.0

- Set `SEQUENCE` to highest version of any used event in a series. See [Issue 223](https://github.com/niccokunzmann/python-recurring-ical-events/issues/223)

## v3.6.1

- Remove unused files: `requirements.txt` and `setup.py`.
- Use version identifier for PyPI.

## v3.6.0

- Add the `RECURRENCE-ID` to all the occurrences, see [Issue 219](https://github.com/niccokunzmann/python-recurring-ical-events/issues/219)
- Document how to edit one event inside of an existing calendar.

## v3.5.2

- Fix computation of mixed start and end times, see [Issue 201](https://github.com/niccokunzmann/python-recurring-ical-events/issues/201)

## v3.5.1

- Move to `pyproject.toml` format to include directory structure more easily. See [Issue 214](https://github.com/niccokunzmann/python-recurring-ical-events/issues/214)
- Remove release 3.5.0 as it does not contain any source files.

## v3.5.0 - yanked

- Restructure module into package with a file structure.
- Add pagination, see [Issue 211](https://github.com/niccokunzmann/python-recurring-ical-events/issues/211)

## v3.4.1

- Improve Alarm documentation

## v3.4.0

- Add `VALARM` support: Calculate alarm times. See [Issue 186](https://github.com/niccokunzmann/python-recurring-ical-events/issues/186)

## v3.3.4

- Allow `x-wr-timezone` `1.*` and `2.*` for this lib to remove dependency update problems.

## v3.3.3

- Fix: Events with DTSTART of type date have a duration of one day, see [Issue 179](https://github.com/niccokunzmann/python-recurring-ical-events/issues/179)

## v3.3.2

- Update x-wr-timezone

## v3.3.1

- Support RDATE with PERIOD value type where the end is a duration, see [Pull Request 180](https://github.com/niccokunzmann/python-recurring-ical-events/pull/180)
- Support modifying all events in the future (RECURRENCE-ID with RANGE=THISANDFUTURE), see [Issue 75](https://github.com/niccokunzmann/python-recurring-ical-events/issues/75)

## v3.3.0

- Make tests work with `icalendar` version 5
- Restructure README to be tested with `doctest`
- Remove `DURATION` from the result, see [Issue 139](https://github.com/niccokunzmann/python-recurring-ical-events/issues/139)
- Document new way of extending the functionality, see [Issue 133](https://github.com/niccokunzmann/python-recurring-ical-events/issues/133) and [Pull Request 175](https://github.com/niccokunzmann/python-recurring-ical-events/pull/175)

## v3.2.0

- Allow `datetime.timedelta` as second argument to `between(absolute_time, datetime.timedelta())`

## v3.1.1

- Fix: Remove duplication of modification with same sequence number, see [Issue 164](https://github.com/niccokunzmann/python-recurring-ical-events/issues/164)
- Fix: EXDATE now excludes a modified instance for an event with higher `SEQUENCE`, see [Issue](https://github.com/niccokunzmann/python-recurring-ical-events/issues/163)

## v3.1.0

- Add `count() -> int` to count all occurrences within a calendar
- Add `all() -> Generator[icalendar.Component]` to iterate over the whole calendar

## v3.0.0

- Change the architecture and add a diagram
- Add type hints, see [Issue 91](https://github.com/niccokunzmann/python-recurring-ical-events/issues/91)
- Rename `UnfoldableCalendar` to `CalendarQuery`
- Rename `of(skip_bad_events=None)` to `of(skip_bad_series=False)`
- `of(components=[...])` now also takes `ComponentAdapters`
- Fix edit sequence problems, see [Issue 151](https://github.com/niccokunzmann/python-recurring-ical-events/issues/151)

## v2.2.3

- Fix: Edits of whole event are now considering RDATE and EXDATE, see [Issue 148](https://github.com/niccokunzmann/python-recurring-ical-events/issues/148)

## v2.2.2

- Test support for `icalendar==6.*`
- Remove Python 3.7 from tests and compatibility list
- Remove pytz from requirements

## v2.2.1

- Add support for multiple RRULE in events.

## v2.2.0

- Add `after()` method to iterate over upcoming events.

## v2.1.3

- Test and support Python 3.12.
- Change SPDX license header.
- Fix RRULE with negative COUNT, see [Issue 128](https://github.com/niccokunzmann/python-recurring-ical-events/issues/128)

## v2.1.2

- Fix RRULE with EXDATE as DATE, see [Pull Request 121](https://github.com/niccokunzmann/python-recurring-ical-events/pull/121) by Jan Grasnick and [Pull Request 122](https://github.com/niccokunzmann/python-recurring-ical-events/pull/122).

## v2.1.1

- Claim and test support for Python 3.11.
- Support deleting events by setting RRULE UNTIL < DTSTART, see [Issue 117](https://github.com/niccokunzmann/python-recurring-ical-events/issues/117).

## v2.1.0

- Added support for PERIOD values in RDATE. See [Issue 113](https://github.com/niccokunzmann/python-recurring-ical-events/issues/113).
- Fixed `icalendar>=5.0.9` to support `RDATE` of type `PERIOD` with a time zone.
- Fixed `pytz>=2023.3` to assure compatibility.

## v2.0.2

- Fixed omitting last event of `RRULE` with `UNTIL` when using `pytz`, the event starting in winter time and ending in summer time. See [Issue 107](https://github.com/niccokunzmann/python-recurring-ical-events/issues/107).

## v2.0.1

- Fixed crasher with duplicate RRULE. See [Pull Request 104](https://github.com/niccokunzmann/python-recurring-ical-events/pull/104)

## v2.0.0

- Only return `VEVENT` by default. Add `of(... ,components=...)` parameter to select which kinds of components should be returned. See [Issue 101](https://github.com/niccokunzmann/python-recurring-ical-events/issues/101).
- Remove `beta` indicator. This library works okay: Feature requests come in, not so much bug reports.

## v1.1.0b

- Add repeated TODOs and Journals. See [Pull Request 100](https://github.com/niccokunzmann/python-recurring-ical-events/pull/100) and [Issue 97](https://github.com/niccokunzmann/python-recurring-ical-events/issues/97).

## v1.0.3b

- Remove syntax anomalies in README.
- Switch to GitHub actions because GitLab decided to remove support.

## v1.0.2b

- Add support for `X-WR-TIMEZONE` calendars which contain events without an explicit time zone, see [Issue 86](https://github.com/niccokunzmann/python-recurring-ical-events/issues/86).

## v1.0.1b

- Add support for `zoneinfo.ZoneInfo` time zones, see [Issue 57](https://github.com/niccokunzmann/python-recurring-ical-events/issues/57).
- Migrate from Travis CI to Gitlab CI.
- Add code coverage on Gitlab.

## v1.0.0b

- Remove Python 2 support, see [Issue 64](https://github.com/niccokunzmann/python-recurring-ical-events/issues/64).
- Remove support for Python 3.5 and 3.6.
- Note: These deprecated Python versions may still work. We just do not claim they do.
- `X-WR-TIMEZONE` support, see [Issue 71](https://github.com/niccokunzmann/python-recurring-ical-events/issues/71).

## v0.2.4b

- Events with a duration of 0 seconds are correctly returned.
- `between()` and `at()` take the same kind of arguments. These arguments are documented.

## v0.2.3b

- `between()` and `at()` allow arguments with time zones now when calendar events do not have time zones, reported in [Issue 61](https://github.com/niccokunzmann/python-recurring-ical-events/issues/61) and [Issue 52](https://github.com/niccokunzmann/python-recurring-ical-events/issues/52).

## v0.2.2b

- Check that `at()` does not return an event starting at the next day, see [Issue 44](https://github.com/niccokunzmann/python-recurring-ical-events/issues/44).

## v0.2.1b

- Check that recurring events are removed if they are modified to leave the requested time span, see [Issue 62](https://github.com/niccokunzmann/python-recurring-ical-events/issues/62).

## v0.2.0b

- Add ability to keep the recurrence attributes (RRULE, RDATE, EXDATE) on the event copies instead of stripping them. See [Pull Request 54](https://github.com/niccokunzmann/python-recurring-ical-events/pull/54).

## v0.1.21b

- Fix issue with repetitions over DST boundary. See [Issue 48](https://github.com/niccokunzmann/python-recurring-ical-events/issues/48).

## v0.1.20b

- Fix handling of modified recurrences with lower sequence number than their base event [Pull Request 45](https://github.com/niccokunzmann/python-recurring-ical-events/pull/45)

## v0.1.19b

- Benchmark using [@mrx23dot](https://github.com/mrx23dot)'s script and speed up recurrence calculation by factor 4, see [Issue 42](https://github.com/niccokunzmann/python-recurring-ical-events/issues/42).

## v0.1.18b

- Handle [Issue 28](https://github.com/niccokunzmann/python-recurring-ical-events/issues/28) so that EXDATEs match as expected.
- Handle [Issue 27](https://github.com/niccokunzmann/python-recurring-ical-events/issues/27) so that parsing some rrule UNTIL values does not crash.

## v0.1.17b

- Handle [Issue 28](https://github.com/niccokunzmann/python-recurring-ical-events/issues/28) where passed arguments lead to errors where it is expected to work.

## v0.1.16b

- Events with an empty RRULE are handled like events without an RRULE.
- Remove fixed dependency versions, see [Issue 14](https://github.com/niccokunzmann/python-recurring-ical-events/issues/14)

## v0.1.15b

- Repeated events also include subcomponents. [Issue 6](https://github.com/niccokunzmann/python-recurring-ical-events/issues/6)

## v0.1.14b

- Fix compatibility [Issue 20](https://github.com/niccokunzmann/python-recurring-ical-events/issues/20): EXDATEs of different time zones are now supported.

## v0.1.13b

- Remove attributes RDATE, EXDATE, RRULE from repeated events [Issue 23](https://github.com/niccokunzmann/python-recurring-ical-events/issues/23).
- Use vDDDTypes instead of explicit date/datetime type [Pull Request 19](https://github.com/niccokunzmann/python-recurring-ical-events/pull/19).
- Start Changelog

```

### `docs/community/index.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      Documentation for contributors who wish to improve this library.
---

# Contribute

There are various ways in which you can contribute to this library.

## Support this library

Please support the development and upkeep in one of these ways:

- [Support using GitHub Sponsors](https://github.com/sponsors/niccokunzmann)
- [Support using Open Collective](https://opencollective.com/open-web-calendar/)
- [Support using thanks.dev](https://thanks.dev)

We accept donations to sustain our work, once or regular.
Consider donating money to open-source as everyone benefits.

NLNet has supported the development of this library.

## Improve the documentation

Your help with this documentation is very welcome!
Please feel free to edit the pages with the "Edit on GitHub" button on the side.
With a GitHub account, your contribution will be guided towards a [pull request]
and we can have a look and use your suggestions.

For style and formatting, please consult the [documentation reference section].

[documentation reference section]: ../reference/documentation

## Community navigation

```{toctree}
:maxdepth: 1
:caption: Community

media
maintenance
```

## Setup to develop

This section informs you how to work on this project.

### Code style

Please install [pre-commit] before git commit.
It will ensure that the code is formatted and linted as expected using [ruff].

```sh
pre-commit install
```

[pre-commit]: https://pre-commit.com/
[ruff]: https://docs.astral.sh/ruff/

### Testing

This project's development is driven by tests.
Tests assure a consistent interface and less knowledge lost over time.
If you like to change the code, tests help that nothing breaks in the future.
They are required in that sense.
Example code and ics files can be transferred into tests and speed up fixing bugs.

You can view the tests in the [test folder]
If you have a calendar ICS file for which this library does not
generate the desired output, you can add it to the `test/calendars`
folder and write tests for what you expect.
If you like, open an [issue] first, e.g. to discuss the changes and
how to go about it.

To run the tests, we use `tox`.
`tox` tests all different Python versions which we want to  be compatible to.

```sh
pip3 install tox
```

After installing `tox`, run the tests with your current Python version:

```sh
tox -e py
```

.. info::

  With this, you have all the tools to develop and improve this project.
  Please open an [pull request] as soon as you made a change.
  This is not about being perfect, only about doing your part of the communication.
  Your are welcome!

[pull request]: https://github.com/niccokunzmann/python-recurring-ical-events/pull

#### Extended Testing

When you create a pull request, we will run the tests in all Python versions.
You can do that, too.

```sh
tox
```

To run the tests in a specific Python version:

```sh
tox -e py39
```

### Building the documentation

You can build the documentation locally to see your changes.
To view the documentation in a web page and have it update with every edit,
run the following commands:

```sh
cd docs
make livehtml
```

To clean the build folder, run:

```sh
make clean
```

Commits are tested online to check if the documentation does not contain any
errors or warnings.
To run these checks and see if you can publish the changes, run:

```sh
tox -e docs
```

[test folder]: https://github.com/niccokunzmann/python-recurring-ical-events/tree/master/test
[issue]: https://github.com/niccokunzmann/python-recurring-ical-events/issues

```

### `docs/community/maintenance.rst`

```rst

Maintenance
===========

This sets you up for maintenance.

New Releases
------------

You can build the new release by running this command:

.. code-block:: shell

    tox -e build

To release new versions,

1. Edit the Changelog Section.
2. Create a commit and push it.
3. Wait for `GitHub Actions <https://github.com/niccokunzmann/python-recurring-ical-events/actions>`_ to finish the build.
4. Run

   .. code-block:: shell

       git tag v3.5.1
       git push origin v3.5.1

5. Wait for the tag to build. @niccokunzmann or another maintainer needs to approve the push to PyPI.
6. Notify the issues about their release.

```

### `docs/community/media.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      New, talks, tutorials and other media about this library.
---

# Media

Additional to this documentation, there are other sources of information.

## News

You can view current news about this library on [Mastodon](https://toot.wales/tags/RecurringIcalEvents).

## Videos

There are a few videos that cover using this library on [Youtube](https://www.youtube.com/watch?v=nwpS2dCk_Rk&list=PLxMGFFiBKgdb3L550U5EAiCvft2IK08xK).


## Conferences

Nicco Kunzmann talked about this library at the
FOSSASIA 2022 Summit:

[![FOSSASIA 2022 talk by Nicco Kunzmann](https://niccokunzmann.github.io/ical-talk-fossasia-2022/youtube.png)](https://youtu.be/8l3opDdg92I?t=10369)

```

### `docs/conf.py`

```py
# icalendar documentation build configuration file
import datetime
import importlib.metadata
import sys
from pathlib import Path

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    # from pydata-sphix-theme
    "myst_parser",
    # from https://sphinx-toolbox.readthedocs.io/
    "sphinx_tabs.tabs",
    "sphinx-prompt",
    # "sphinx_toolbox",
    # "sphinx_toolbox.more_autodoc"
]
source_suffix = {".rst": "restructuredtext"}
master_doc = "index"

project = "recurring-ical-events"
this_year = datetime.date.today().year
copyright = f"{this_year}, Nicco Kunzmann & recurring-ical-events contributors"
release = version = importlib.metadata.version("recurring-ical-events")


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/niccokunzmann/python-recurring-ical-events",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css",
            },
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/recurring-ical-events",
            "icon": "fa-solid fa-download",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css",
            },
        },
        {
            "name": "Mastodon",
            "url": "https://toot.wales/tags/RecurringIcalEvents",
            "icon": "fa-brands fa-mastodon",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css",
            },
        },
        {
            "name": "Youtube",
            "url": "https://www.youtube.com/watch?v=nwpS2dCk_Rk&list=PLxMGFFiBKgdb3L550U5EAiCvft2IK08xK",
            "icon": "fa-brands fa-youtube",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css",
            },
        },
    ],
    "navigation_with_keys": True,
    "search_bar_text": "Search",
    "show_nav_level": 2,
    "show_toc_level": 2,
    "use_edit_page_button": True,
}
html_context = {
    #     "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "niccokunzmann",
    "github_repo": "python-recurring-ical-events",
    "github_version": "main",
    "doc_path": "docs",
}
htmlhelp_basename = "recurring-ical-events-doc"
pygments_style = "sphinx"


# -- Intersphinx configuration ----------------------------------

# This extension can generate automatic links to the documentation of objects
# in other projects. Usage is simple: whenever Sphinx encounters a
# cross-reference that has no matching target in the current documentation set,
# it looks for targets in the documentation sets configured in
# intersphinx_mapping. A reference like :py:class:`zipfile.ZipFile` can then
# linkto the Python documentation for the ZipFile class, without you having to
# specify where it is located exactly.
#
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "icalendar": ("https://icalendar.readthedocs.io/en/latest", None),
    "dateutil": ("https://dateutil.readthedocs.io/en/stable/", None),
}


man_pages = [
    (
        "index",
        "recurring_ical_events",
        "recurring_ical_events Documentation",
        ["Nicco Kunzmann"],
        1,
    )
]

exclude_patterns = ["venv"]

# we have had issues with linkcheck timing and retries on www.gnu.org
linkcheck_retries = 1
linkcheck_timeout = 5
linkcheck_report_timeouts_as_broken = True

# autodoc
autodoc_typehints_format = "short"
autodoc_preserve_defaults = True
autodoc_type_aliases = {
    "datetime": "datetime.datetime",
    "date": "datetime.date",
    "timedelta": "datetime.timedelta",
    "Time": "recurring_ical_events.types.Time",
    "DateArgument": "recurring_ical_events.types.DateArgument",
    "UID": "recurring_ical_events.types.UID",
    "Timestamp": "recurring_ical_events.types.Timestamp",
    "RecurrenceID": "recurring_ical_events.types.RecurrenceID",
    "RecurrenceIDs": "recurring_ical_events.types.RecurrenceIDs",
    "Component": "icalendar.cal.Component",
    "Calendar": "icalendar.cal.Calendar",
    "T_COMPONENTS": "recurring_ical_events.query.T_COMPONENTS",
    "OccurrenceID": "recurring_ical_events.occurrence.OccurrenceID",
    "icalendar.Calendar": "icalendar.cal.Calendar",
}

# sphinx-toolbox
github_username = "niccokunzmann"
github_repository = "python-recurring-ical-events"


# from https://github.com/sphinx-doc/sphinx/issues/10785
nitpick_ignore = [
    # ignore for now
    ("py:class", "RecurrenceID"),
]

# make title smaller
# see https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_title
html_title = f"{project} {release}"
html_short_title = project

# try reloading the module
# see https://github.com/sphinx-doc/sphinx/issues/4317#issuecomment-353793061
HERE = Path(__file__).parent
sys.path.insert(0, str(Path(HERE).parent))

```

### `docs/docutils.conf`

```conf
[restructuredtext parser]
tab_width: 4

```

### `docs/index.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      Documentation of the recurring-ical-events library for Python.
---

# Python recurring ICal events

```{eval-rst}
.. image:: https://github.com/niccokunzmann/python-recurring-ical-events/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/niccokunzmann/python-recurring-ical-events/actions/workflows/tests.yml
   :alt: GitHub CI build and test status
.. image:: https://badge.fury.io/py/recurring-ical-events.svg
   :target: https://pypi.python.org/pypi/recurring-ical-events
   :alt: Python Package Version on Pypi
.. image:: https://img.shields.io/pypi/dm/recurring-ical-events.svg
   :target: https://pypi.org/project/recurring-ical-events/#files
   :alt: Downloads from Pypi
.. image:: https://img.shields.io/opencollective/all/open-web-calendar?label=support%20on%20open%20collective
   :target: https://opencollective.com/open-web-calendar/
   :alt: Support on Open Collective
.. image:: https://img.shields.io/github/issues/niccokunzmann/python-recurring-ical-events?logo=github&label=issues%20seek%20funding&color=%230062ff
   :target: https://polar.sh/niccokunzmann/python-recurring-ical-events
   :alt: issues seek funding
```

Query [ICS calendars](https://icalendar.readthedocs.io) for occurrences of events, todos, journal entries and alarms.

ICal has some complexity to it:
Events, TODOs, Journal entries and Alarms can be repeated, removed from the feed and edited later on.
This tool takes care of these complexities.

Let's put our expertise together and build the solution solves ICalendar scheduling for Python!

## User Guide

Information about usage.

```{toctree}
:maxdepth: 2
:caption: User guide

user-guide/index
```


## Community

Information about contributing.

```{toctree}
:maxdepth: 2
:caption: Community

community/index
```

## Reference

This is reference material for information.

```{toctree}
:maxdepth: 2
:caption: Reference

reference/index
```

```{toctree}
:maxdepth: 1
:caption: Project information

changelog
security_policy
```

```

### `docs/Makefile`

```
# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS      =
SPHINXBUILD     = venv/bin/sphinx-build
SPHINXAUTOBUILD = venv/bin/sphinx-autobuild
PAPER           =
BUILDDIR        = _build
LOCALESDIR      = _locales

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help cleanhtml clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext livehtml rtd-pr-preview

venv:
	pwd
	git fetch --tags
	python -m venv venv
	venv/bin/pip install -r requirements.txt -e ..

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  livehtml   to view a live preview of standalone HTML files"
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
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

cleanhtml:
	-rm -rf $(BUILDDIR)/*

clean: cleanhtml
	-rm -rf venv

html: venv
	$(SPHINXBUILD) -b html --fresh-env --write-all $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in docs/$(BUILDDIR)/html."
	rm -rf build

latexpdf: venv
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text: venv
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man: venv
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

gettext: venv
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(LOCALESDIR)
	@echo
	@echo "Build finished. The message catalogs are in $(LOCALESDIR)."

linkcheck: venv
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest: venv
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

livehtml: venv
	# rebuild because the modules change
	$(SPHINXAUTOBUILD) \
	--watch .. \
	--port 8050 \
	-b html . "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

rtd-pr-preview: venv ## Build pull request preview on Read the Docs
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) ${READTHEDOCS_OUTPUT}/html/

```

### `docs/reference/api.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      API Reference of functions and classes.
---


# API Reference

This is the public API for this library.

## Core functionality

This is the core of the functionality of the library.

The first step is to customize which components to query with {py:func}`recurring_ical_events.of`.

```{eval-rst}
.. autofunction:: recurring_ical_events.of 
```

## Query

`of()` returns a {py:class}`recurring_ical_events.CalendarQuery` object, which can be used to query the calendar.
For the most common cases, you do not need to look any further.

```{eval-rst}
.. autoclass:: recurring_ical_events.CalendarQuery
    :members:
    :exclude-members: ComponentsWithName
```

### list from `at()` and `between()`

The result of both {py:meth}`recurring_ical_events.CalendarQuery.between` and
{py:meth}`recurring_ical_events.CalendarQuery.at` is a list of {py:class}`icalendar.cal.component.Component`
objects like {py:class}`icalendar.cal.event.Event`.
By default, all attributes of the event with repetitions are copied, like ``UID`` and ``SUMMARY``.
However, these attributes may differ from the source event:

* ``DTSTART`` which is the start of the event instance. (always present)
* ``DTEND`` which is the end of the event instance. (always present)
* ``RDATE``, ``EXDATE``, ``RRULE`` are the rules to create event repetitions.
  They are **not** included in repeated events, see [Issue 23].
  To change this, use ``of(calendar, keep_recurrence_attributes=True)``.

[Issue 23]: https://github.com/niccokunzmann/python-recurring-ical-events/issues/23

### Generator from `after()` and `all()`

If the resulting components are ordered when {py:meth}`recurring_ical_events.CalendarQuery.after` or 
{py:meth}`recurring_ical_events.CalendarQuery.all` is used.
The result is an iterator that returns the events in order.

```python
for event in recurring_ical_events.of(an_icalendar_object).after(datetime.datetime.now()):
    print(event["DTSTART"]) # The start is ordered
```

### Occurrence-returning queries

Every component-returning method has a counterpart that returns
{py:class}`recurring_ical_events.Occurrence` objects instead:
{py:meth}`~recurring_ical_events.CalendarQuery.occurrences_at`,
{py:meth}`~recurring_ical_events.CalendarQuery.occurrences_between`,
{py:meth}`~recurring_ical_events.CalendarQuery.occurrences_after`,
{py:meth}`~recurring_ical_events.CalendarQuery.occurrences_all`,
{py:meth}`~recurring_ical_events.CalendarQuery.occurrences_count`,
{py:attr}`~recurring_ical_events.CalendarQuery.first_occurrence`, and
{py:meth}`~recurring_ical_events.CalendarQuery.occurrences_paginate`.

An {py:class}`~recurring_ical_events.Occurrence` carries an
{py:attr}`~recurring_ical_events.Occurrence.id` you can persist, and only converts
to a component when you call {py:meth}`~recurring_ical_events.Occurrence.as_component`.

## Timezones and floating time

This library makes a distinction between floating time and times with timezones.

Examples:

* Event 1 happes at 12:00 in Singapore and event 2 on the same day at 12:00 in New York.

  * If you query that day without timezone, you will get both events.
  * If you query 12:00 - 13:00 without timezone, you will get both events.
  * If you query 12:00 - 13:00 in `Asia/Singapore`, you will only get event 1.
  * If you query 12:00 - 13:00 in `America/New_York`, you will only get event 2.

* If an event happens at night in floating time (without timezone) and
  you query that day it will appear regardless of the timezone of the query.
  Which is at different times in different timezones.

* {py:class}`icalendar.cal.alarm.Alarm` has a `TRIGGER` which is in UTC.
  The timezone to compute that for alarms relative to floating events will be taken
  from the start and stop arguments.

## Pagination

For ease of use, pagination has been introduced.
These are the pages returned by the query.

```{eval-rst}
.. automodule:: recurring_ical_events.pages
    :members:
```

## Complete API

```{eval-rst}

.. automodule:: recurring_ical_events
    :show-inheritance:
    :members:
    :exclude-members: CalendarQuery, of, OccurrenceID

.. automodule:: recurring_ical_events.types
    :members:
```

## Type aliases

```{eval-rst}
.. autodata:: recurring_ical_events.types.Time
    :no-value:
    :no-index:

.. autodata:: recurring_ical_events.types.UID
    :no-value:
    :no-index:

.. autodata:: recurring_ical_events.types.RecurrenceIDs
    :no-value:
    :no-index:
```

## Occurrence identifiers

```{eval-rst}
.. autoclass:: recurring_ical_events.OccurrenceID

  .. autoattribute:: uid
     :no-index:

  .. automethod:: to_string
  .. automethod:: from_string
  .. automethod:: from_occurrence
```

```

### `docs/reference/architecture.rst`

```rst
Architecture
============

.. image:: ../img/architecture.png
   :alt: Architecture Diagram showing the components interacting

Each icalendar **Calendar** can contain Events, Journal entries,
TODOs and others, called **Components**.
Those entries are grouped by their ``UID``.
Such a ``UID`` defines a **Series** of **Occurrences** that take place at
a given time.
Since each **Component** is different, the **ComponentAdapter** offers a unified
interface to interact with them.
The **Calendar** gets filtered and for each ``UID``,
a **Series** can use one or more **ComponentAdapters** to create 
**Occurrences** of what happens in a time span.
These **Occurrences** are used internally and convert to **Components** for further use.

```

### `docs/reference/compatibility.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      Specifications and compatibility
---

# Compatibility

## RFC Specifications

### RFC 2445 - iCalendar

![RFC 2445 is deprecated](https://img.shields.io/badge/RFC_2445-deprecated-red)

{rfc}`2445` is deprecated and has been replaced by {rfc}`5545` and {rfc}`7529`.

### RFC 5545 - iCalendar

![RFC 5545 is supported](https://img.shields.io/badge/RFC_5545-supported-green)

{rfc}`5545` is fully supported.

This is the core specification for the occurrences that this library computes:
``VEVENT``, ``VTODO``, ``VJOURNAL``, ``VALARM``, ``RRULE``, ``RDATE``,
``EXDATE``, ``RECURRENCE-ID``, and the alarm ``TRIGGER`` rules.

### RFC 7529 - Non-Gregorian Recurrence Rules

![RFC 7529 is not implemented](https://img.shields.io/badge/RFC_7529-todo-red)

{rfc}`7529` is not implemented.

### RFC 7953 - Calendar Availability

![RFC 7953 is not implemented](https://img.shields.io/badge/RFC_7953-todo-red)

{rfc}`7953` is not implemented.

### RFC 9074 - VALARM Extensions for iCalendar

![RFC 9074 is partially supported](https://img.shields.io/badge/RFC_9074-partial-yellow)

{rfc}`9074` updates ``VALARM`` components.
This library computes alarm occurrences from the ``TRIGGER``, ``REPEAT``, and
``DURATION`` rules defined for alarms by {rfc}`5545`.
The extra alarm metadata and interoperability features from {rfc}`9074`, such
as ``UID``, ``ACKNOWLEDGED``, ``RELATED-TO``, and ``PROXIMITY``, do not change
which occurrences are returned.

## RFCs and occurrence calculation

The library computes when supported calendar components occur.
RFCs that change recurrence rules, component time spans, or alarm trigger times
can affect this computation.
RFCs that add descriptive metadata, relationship metadata, or scheduling
protocol semantics can be present in iCalendar data, but they do not by
themselves change the result of ``at()``, ``between()``, ``after()``, or
``all()``.

| RFC | Scope for this library |
| --- | --- |
| {rfc}`5545` | Core recurrence, exception, component, and alarm trigger rules. |
| {rfc}`5546` | iTIP scheduling messages; not used to expand occurrence times. |
| {rfc}`6868` | Parameter value encoding; handled before recurrence logic. |
| {rfc}`7529` | Non-Gregorian ``RRULE`` support; affects recurrence calculation but is not implemented. |
| {rfc}`7953` | ``VAVAILABILITY`` and availability calculation; outside the queried components. |
| {rfc}`7986` | New descriptive properties; no direct effect on occurrence times. |
| {rfc}`9073` | Event publishing properties, components, and structured data; no direct effect on occurrence times. |
| {rfc}`9074` | Alarm extensions; base alarm trigger calculation is supported through {rfc}`5545`, while the added metadata does not change occurrence times. |
| {rfc}`9253` | Relationship and linking properties; not used to expand or filter occurrences. |

## Other Specifications

### X-WR-TIMEZONE

`X-WR-TIMEZONE` is supported through the [X-WR-TIMEZONE] library.

## Feature list

* ✅ day light saving time (DONE)
* ✅ recurring events (DONE)
* ✅ recurring events with edits (DONE)
* ✅ recurring events where events are omitted (DONE)
* ✅ recurring events events where the edit took place later (DONE)
* ✅ normal events (DONE)
* ✅ recurrence of dates but not hours, minutes, and smaller (DONE)
* ✅ endless recurrence (DONE)
* ✅ ending recurrence (DONE)
* ✅ events with start date and no end date (DONE)
* ✅ events with start as date and start as datetime (DONE)
* ✅ [RRULE](https://www.kanzaki.com/docs/ical/rrule.html) (DONE)
* ✅ events with multiple RRULE (DONE)
* ✅ [RDATE](https://www.kanzaki.com/docs/ical/rdate.html) (DONE)
* ✅ [DURATION](https://www.kanzaki.com/docs/ical/duration.html) (DONE)
* ✅ [EXDATE](https://www.kanzaki.com/docs/ical/exdate.html) (DONE)
* ✅ [X-WR-TIMEZONE] compatibility (DONE)
* ✅ RECURRENCE-ID with THISANDFUTURE - modify all future events (DONE)

## Missing features

* ❌ non-gregorian event repetitions (TODO)
* ❌ EXRULE (deprecated), see [8.3.2.  Properties Registry](https://tools.ietf.org/html/rfc5545#section-8.3.2)


[X-WR-TIMEZONE]: https://pypi.org/project/x-wr-timezone

```

### `docs/reference/dependencies.rst`

```rst

Libraries Used
==============

- `python-dateutil <https://pypi.org/project/python-dateutil/>`_ - to compute the recurrences of events using ``rrule``
- `icalendar`_ - the library used to parse ICS files
- `pytz <https://pypi.org/project/pytz/>`_ - for timezones
- `x-wr-timezone <https://github.com/niccokunzmann/x-wr-timezone>`_ for handling the non-standard ``X-WR-TIMEZONE`` property.


.. _icalendar: https://pypi.org/project/icalendar/
```

### `docs/reference/documentation.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      Reference for writing documentation
---
# Documentation

This section contains links and explanations for writing documentation.

## Markdown/MyST files

The documentation files with `.md` are structured using [Markdown] and [MyST].

## reStructuredText files

[reStructuredText] is used for `.rst` files to include the source code using [Sphinx].

## Source code

The source code is written in Python and tested with [doctest].
The format of the docstrings follows [Google's style guide].

[Markdown]: https://www.markdownguide.org/cheat-sheet/
[reStructuredText]: https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
[MyST]: https://mystmd.org/
[Sphinx]: https://www.sphinx-doc.org/
[doctest]: https://docs.python.org/3/library/doctest.html
[Google's style guide]: https://google.github.io/styleguide/pyguide.html#383-functions-and-methods

```

### `docs/reference/index.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      Reference material for writing documentation and understanding the library.
---

# Documentation reference

This section collects the API reference and supporting project notes.

## API and behavior

```{toctree}
:maxdepth: 2
:caption: API and behavior

api
architecture
compatibility
dependencies
```

## Project information

```{toctree}
:maxdepth: 2
:caption: Project information

documentation
related-projects
research
license
```

```

### `docs/reference/license.md`

```md
# License

```{include} ../../LICENSE
```

```

### `docs/reference/related-projects.rst`

```rst


Related Projects
================

These projects either build on ``recurring-ical-events``, solve related
calendar problems, or provide calendar and recurrence functionality that this
project uses.

Core calendar libraries
-----------------------

- `icalendar`_ - parses and writes iCalendar files
- `python-dateutil`_ - computes recurrence rules with ``rrule``
- `x-wr-timezone`_ - handles the non-standard ``X-WR-TIMEZONE`` property
- `tzdata`_ - provides time zone data when the operating system does not

Projects using or similar to recurring-ical-events
--------------------------------------------------

- `icalevents <https://github.com/irgangla/icalevents>`_ - another library for roughly the same use-case
- `Open Web Calendar <https://github.com/niccokunzmann/open-web-calendar>`_ - a web calendar to embed into websites which uses this library
- `icspy <https://icspy.readthedocs.io/>`_ - to create your own calendar events
- `pyICSParser <https://pypi.org/project/pyICSParser/>`_ - parse icalendar files and return event times (`GitHub <https://github.com/oberron/pyICSParser>`__)
- `ics-query`_ - a **command line** implementation of ``recurring-ical-events``
- `icalendar-events-cli`_ - another **command line** implementation of ``recurring-ical-events``
- `caldav`_ - the python caldav client library
- `plann`_ - a **command line** caldav client
- `ics_calendar`_ - Provides a component for ICS (icalendar) calendars for `Home Assistant`_

.. _`icalendar`: https://pypi.org/project/icalendar/
.. _`python-dateutil`: https://pypi.org/project/python-dateutil/
.. _`x-wr-timezone`: https://github.com/niccokunzmann/x-wr-timezone
.. _`tzdata`: https://pypi.org/project/tzdata/
.. _`ics-query`: https://github.com/niccokunzmann/ics-query#readme
.. _`icalendar-events-cli`: https://github.com/waldbaer/icalendar-events-cli#readme
.. _`caldav`:  https://github.com/python-caldav/caldav
.. _`plann`: https://github.com/tobixen/plann
.. _`ics_calendar`: https://github.com/franc6/ics_calendar/
.. _`Home Assistant`: https://www.home-assistant.io/

Command line interface
----------------------

If you would like to use this functionality on the command line or in the shell, you can use
`ics-query`_.

```

### `docs/reference/research.rst`

```rst

Research
========

- `RFC 5545 <https://tools.ietf.org/html/rfc5545>`_
- `RFC 7986 <https://tools.ietf.org/html/rfc7986>`_ -- an update to RFC 5545. It does not change any properties useful for scheduling events.
- `Stackoverflow question this is created for <https://stackoverflow.com/questions/30913824/ical-library-to-iterate-recurring-events-with-specific-instances>`_
- `<https://github.com/oberron/annum>`_

  - `<https://stackoverflow.com/questions/28829261/python-ical-get-events-for-a-day-including-recurring-ones#28829401>`_

- `<https://stackoverflow.com/questions/20268204/ical-get-date-from-recurring-event-by-rrule-and-dtstart>`_
- `<https://github.com/collective/icalendar/issues/162>`_
- `<https://stackoverflow.com/questions/46471852/ical-parsing-reoccuring-events-in-python>`_
- RDATE `<https://stackoverflow.com/a/46709850/1320237>`_

  - `<https://tools.ietf.org/html/rfc5545#section-3.8.5.2>`_


.. _`ics-query`: https://github.com/niccokunzmann/ics-query#readme

```

### `docs/requirements.in`

```in
Sphinx>=7
pydata-sphinx-theme
sphinx-autobuild
sphinx-copybutton
sphinx-sitemap
sphinx-autoapi>=3.0.0
# For examples section
myst-parser
sphinx-autodoc-typehints
sphinx-toolbox
sphinx-tabs

```

### `docs/requirements.txt`

```txt
accessible-pygments==0.0.5
alabaster==1.0.0
anyio==4.12.0
apeye==1.4.1
apeye-core==1.1.5
astroid==4.0.2
autodocsumm==0.2.14
babel==2.17.0
beautifulsoup4==4.14.3
cachecontrol[filecache]==0.14.4
certifi==2025.11.12
charset-normalizer==3.4.4
click==8.3.1
colorama==0.4.6
cssutils==2.11.1
dict2css==0.3.0.post1
docutils==0.21.2
domdf-python-tools==3.10.0
filelock==3.20.3
h11==0.16.0
html5lib==1.1
idna==3.11
imagesize==1.4.1
jinja2==3.1.6
markdown-it-py==3.0.0
markupsafe==3.0.3
mdit-py-plugins==0.5.0
mdurl==0.1.2
more-itertools==10.8.0
msgpack==1.2.1
myst-parser==4.0.1
natsort==8.4.0
packaging==25.0
platformdirs==4.5.1
pydata-sphinx-theme==0.16.1
pygments==2.20.0
pyyaml==6.0.3
requests==2.33.0
roman==5.2
roman-numerals==4.1.0
roman-numerals-py==4.1.0
ruamel-yaml==0.18.17
ruamel-yaml-clib==0.2.15
six==1.17.0
snowballstemmer==3.0.1
soupsieve==2.8.4
sphinx==8.2.3
sphinx-autoapi==3.6.1
sphinx-autobuild==2025.8.25
sphinx-autodoc-typehints==3.5.2
sphinx-copybutton==0.5.2
sphinx-jinja2-compat==0.4.1
sphinx-last-updated-by-git==0.3.8
sphinx-prompt==1.10.2
sphinx-sitemap==2.9.0
sphinx-tabs==3.4.5
sphinx-toolbox==4.1.0
sphinxcontrib-applehelp==2.0.0
sphinxcontrib-devhelp==2.0.0
sphinxcontrib-htmlhelp==2.1.0
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-qthelp==2.0.0
sphinxcontrib-serializinghtml==2.0.0
standard-imghdr==3.10.14
starlette==0.50.0
tabulate==0.9.0
typing-extensions==4.15.0
urllib3==2.7.0
uvicorn==0.38.0
watchfiles==1.1.1
webencodings==0.5.1
websockets==15.0.1

```

### `docs/security_policy.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      The security policy of the recurring-ical-events library for Python.
---

```{include} ../SECURITY.md
```
```

### `docs/user-guide/examples.rst`

```rst

How to
======

Additionally to the examples listed here, you can have a look the 
`API documentation`_.
In the `Media Section`_, you can videos and useful information on social media.

.. _`API documentation`: ../reference/api.html
.. _`Media Section`: ../community/media.html

Read a file and print events
----------------------------

The following example loads a calendar from a file and
prints the events happening between the 1st of January 2017 and the 1st of January 2018.

.. code-block:: python

    >>> import icalendar
    >>> import recurring_ical_events
    >>> from pathlib import Path

    # read the calendar file and parse it
    # CALENDARS = Path("to/your/calendar/directory")
    >>> calendar_file : Path = CALENDARS / "fablab_cottbus.ics"
    >>> ical_string = calendar_file.read_bytes()
    >>> print(ical_string[:28])
    BEGIN:VCALENDAR
    VERSION:2.0
    >>> a_calendar = icalendar.Calendar.from_ical(ical_string)

    # request the events in a specific interval
    # start on the 1st of January 2017 0:00
    >>> start_date = (2017, 1, 1)

    # the event on the 1st of January 2018 is not included
    >>> end_date =   (2018,  1, 1)
    >>> events = recurring_ical_events.of(a_calendar).between(start_date, end_date)
    >>> for event in events:
    ...     start = event["DTSTART"].dt
    ...     summary = event["SUMMARY"]
    ...     print(f"start {start} summary {summary}")
    start 2017-03-11 17:00:00+01:00 summary Vereinssitzung
    start 2017-06-10 10:00:00+02:00 summary Repair und Recycling Café
    start 2017-06-11 16:30:00+02:00 summary Brandenburger Maker-Treffen
    start 2017-07-05 17:45:00+02:00 summary Der Computer-Treff fällt aus
    start 2017-07-29 14:00:00+02:00 summary Sommerfest
    start 2017-10-19 16:00:00+02:00 summary 3D-Modelle programmieren mit OpenSCAD
    start 2017-10-20 16:00:00+02:00 summary Programmier dir deine eigene Crypto-Währung
    start 2017-10-21 13:00:00+02:00 summary Programmiere deine eigene Wetterstation
    start 2017-10-22 13:00:00+02:00 summary Luftqualität: Ein Workshop zum selber messen (Einsteiger)
    start 2017-10-22 13:00:00+02:00 summary Websites selbst programmieren


List events at certain a time
-----------------------------

You can get all events which take place at ``a_date``.
A date can be a year, e.g. ``2023``, a month of a year e.g. January in 2023 ``(2023, 1)``, a day of a certain month e.g. ``(2023, 1, 1)``, an hour e.g. ``(2023, 1, 1, 0)``, a minute e.g. ``(2023, 1, 1, 0, 0)``, or second as well as a `datetime.date <https://docs.python.org/3/library/datetime.html#datetime.date>`_ object and `datetime.datetime <https://docs.python.org/3/library/datetime.html#datetime.datetime>`_.

The start and end are inclusive. As an example: if an event is longer than one day it is still included if it takes place at ``a_date``.

.. code-block:: python

    >>> import datetime

    # save the query object for the calendar
    >>> query = recurring_ical_events.of(a_calendar)
    >>> len(query.at(2023))                      # a year - 2023 has 12 events happening
    12
    >>> len(query.at((2023,)))                   # a year
    12
    >>> len(query.at((2023, 1)))                 # January in 2023 - only one event is in January
    1
    >>> len(query.at((2023, 1, 1)))              # the 1st of January in 2023
    0
    >>> len(query.at("20230101"))                # the 1st of January in 2023
    0
    >>> len(query.at((2023, 1, 1, 0)))           # the first hour of the year 2023
    0
    >>> len(query.at((2023, 1, 1, 0, 0)))        # the first minute in 2023
    0
    >>> len(query.at(datetime.date(2023, 1, 1))) # the first day in 2023
    0

The resulting ``events`` are a list of `icalendar events <https://icalendar.readthedocs.io/en/latest/api.html#icalendar.cal.Event>`_, see below.

List events within a time range
-------------------------------

``between(start, end)`` returns all events happening between a start and an end time. Both arguments can be `datetime.datetime`_, `datetime.date`_, tuples of numbers passed as arguments to `datetime.datetime`_ or strings in the form of
``%Y%m%d`` (``yyyymmdd``) and ``%Y%m%dT%H%M%SZ`` (``yyyymmddThhmmssZ``).
Additionally, the ``end`` argument can be a ``datetime.timedelta`` to express that the end is relative to the ``start``.
For examples of arguments, see ``at(a_date)`` above.

.. code-block:: python

    >>> query = recurring_ical_events.of(a_calendar)

    # What happens in 2016, 2017 and 2018?
    >>> events = recurring_ical_events.of(a_calendar).between(2016, 2019)
    >>> len(events) # quite a lot is happening!
    39

The resulting ``events`` are in a list of `icalendar events`_, see below.

List events after a certain time
--------------------------------

You can retrieve events that happen after a time or date using ``after(earliest_end)``.
Events that are happening during the ``earliest_end`` are included in the iteration.

.. code-block:: python

    >>> earlierst_end = 2023
    >>> for i, event in enumerate(query.after(earlierst_end)):
    ...     print(f"{event['SUMMARY']} ends {event['DTEND'].dt}") # all dates printed are after January 1st 2023
    ...     if i > 10: break  # we might get endless events and a lot of them!
    Repair Café ends 2023-01-07 17:00:00+01:00
    Repair Café ends 2023-02-04 17:00:00+01:00
    Repair Café ends 2023-03-04 17:00:00+01:00
    Repair Café ends 2023-04-01 17:00:00+02:00
    Repair Café ends 2023-05-06 17:00:00+02:00
    Repair Café ends 2023-06-03 17:00:00+02:00
    Repair Café ends 2023-07-01 17:00:00+02:00
    Repair Café ends 2023-08-05 17:00:00+02:00
    Repair Café ends 2023-09-02 17:00:00+02:00
    Repair Café ends 2023-10-07 17:00:00+02:00
    Repair Café ends 2023-11-04 17:00:00+01:00
    Repair Café ends 2023-12-02 17:00:00+01:00


List all events
---------------

If you wish to iterate over all occurrences of the components, then you can use ``all()``.
Since a calendar can define a huge amount of recurring entries, this method generates them
and forgets them, reducing memory overhead.

This example shows the first event that takes place in the calendar:

.. code-block:: python

    >>> first_event = next(query.all()) # not all events are generated
    >>> print(f"The first event is {first_event['SUMMARY']}")
    The first event is Weihnachts Repair-Café

Count events
------------

You can count occurrences of events and other components using ``count()``.

.. code-block:: python

    >>> number_of_TODOs = recurring_ical_events.of(a_calendar, components=["VTODO"]).count()
    >>> print(f"You have {number_of_TODOs} things to do!")
    You have 0 things to do!

    >>> number_of_journal_entries = recurring_ical_events.of(a_calendar, components=["VJOURNAL"]).count()
    >>> print(f"There are {number_of_journal_entries} journal entries in the calendar.")
    There are 0 journal entries in the calendar.

However, this can be very costly!

Split a query into pages
------------------------

Pagination allows you to chop the resulting components into chunks of a certain size.

.. code-block:: python

    # we get a calendar with 10 events and 2 events per page
    >>> ten_events = recurring_ical_events.example_calendar("event_10_times")
    >>> pages = recurring_ical_events.of(ten_events).paginate(2)

    # we can iterate over the pages with 2 events each
    >>> for i, last_page in enumerate(pages):
    ...     print(f"page: {i}")
    ...     for event in last_page:
    ...         print(f"->  {event.start}")
    ...     if i == 1: break
    page: 0
    ->  2020-01-13 07:45:00+01:00
    ->  2020-01-14 07:45:00+01:00
    page: 1
    ->  2020-01-15 07:45:00+01:00
    ->  2020-01-16 07:45:00+01:00

If you run a web service and you would like to continue pagination after a certain page,
this can be done, too. Just hand someone the ``next_page_id`` and continue from there on.

.. code-block:: python

    # resume the same query from the next page
    >>> pages = recurring_ical_events.of(ten_events).paginate(2, next_page_id = last_page.next_page_id)
    >>> for i, last_page in enumerate(pages):
    ...     print(f"page: {i + 2}")
    ...     for event in last_page:
    ...         print(f"->  {event.start}")
    ...     if i == 1: break
    page: 2
    ->  2020-01-17 07:45:00+01:00
    ->  2020-01-18 07:45:00+01:00
    page: 3
    ->  2020-01-19 07:45:00+01:00
    ->  2020-01-20 07:45:00+01:00

The ``last_page.next_page_id`` is a string so that it can be used easily.
It is tested against malicious modification and can safely be passed from a third party source.

Additionally to the page size, you can also pass a ``start`` and an ``end`` to the pages so that
all components are visible within that time.

Work with occurrences directly
------------------------------

By default a query gives you :class:`icalendar.cal.Event` components.
When you want occurrences instead, every query method has an ``occurrences_*`` counterpart.
Use them when you need to identify occurrences across runs, build custom components yourself,
or hand occurrences to another library.

================================  =====================================
Component-returning               Occurrence-returning
================================  =====================================
``at(date)``                      ``occurrences_at(date)``
``between(start, stop)``          ``occurrences_between(start, stop)``
``after(earliest_end)``           ``occurrences_after(earliest_end)``
``all()``                         ``occurrences_all()``
``count()``                       ``occurrences_count()``
``first``                         ``first_occurrence``
``paginate(...)``                 ``occurrences_paginate(...)``
================================  =====================================

Every :class:`~recurring_ical_events.Occurrence` carries an
:attr:`~recurring_ical_events.Occurrence.id` (an
:class:`~recurring_ical_events.OccurrenceID`) you can use as a primary key,
and converts to a component on demand:

.. code-block:: python

    >>> ten_events = recurring_ical_events.example_calendar("event_10_times")
    >>> ten_query = recurring_ical_events.of(ten_events)
    >>> first = ten_query.first_occurrence
    >>> print(first.start)
    2020-01-13 07:45:00+01:00
    >>> print(first.id.uid)
    64374d28-089b-4958-8c95-cdd00e6d8ad3
    >>> event = first.as_component(keep_recurrence_attributes=False)
    >>> print(event["SUMMARY"])
    event 10 times

Pagination has an occurrence-returning counterpart too:

.. code-block:: python

    >>> occurrence_pages = ten_query.occurrences_paginate(2)
    >>> for i, page in enumerate(occurrence_pages):
    ...     print(f"page: {i}")
    ...     for occurrence in page:
    ...         print(f"->  {occurrence.start}")
    ...     if i == 1: break
    page: 0
    ->  2020-01-13 07:45:00+01:00
    ->  2020-01-14 07:45:00+01:00
    page: 1
    ->  2020-01-15 07:45:00+01:00
    ->  2020-01-16 07:45:00+01:00

Get Todos and Journal entries
-----------------------------

By default the ``recurring_ical_events`` only selects events as the name already implies.
However, there are different `components <https://icalendar.readthedocs.io/en/latest/api.html#icalendar.cal.Component>`_ available in a `calendar <https://icalendar.readthedocs.io/en/latest/api.html#icalendar.cal.Calendar>`_.
You can select which components you like to have returned by passing ``components`` to the ``of`` function:

.. code-block:: python

    of(a_calendar, components=["VEVENT"])

Here is a template code for choosing the supported types of components:

.. code-block:: python

    >>> query_events = recurring_ical_events.of(a_calendar)
    >>> query_journals = recurring_ical_events.of(a_calendar, components=["VJOURNAL"])
    >>> query_todos = recurring_ical_events.of(a_calendar, components=["VTODO"])
    >>> query_all = recurring_ical_events.of(a_calendar, components=["VTODO", "VEVENT", "VJOURNAL"])

If a type of component is not listed here, it can be added.
Please create an issue for this in the source code repository.

For further customization, please refer to the section on how to extend the default functionality.

Calculate Alarm times
---------------------

Alarms are subcomponents of events and todos. They only make sense with an event or todo.
Thus the interface is slightly different.

Add ``VALARM`` as the component you would like:

.. code-block:: python

    >>> query_alarms = recurring_ical_events.of(a_calendar, components=["VALARM"])

In the following example, an event has an alarm one week before it starts.
The component returned is not a ``VALARM`` component but instead the ``VEVENT`` with only
one ``VALARM`` in it.

.. code-block:: python

    # read an .ics file with an event with an alarm
    >>> calendar_with_alarm = recurring_ical_events.example_calendar("alarm_1_week_before_event")
    >>> alarm_day = datetime.date(2024, 12, 2)

    # we get the event that has an alarm on that day
    >>> event = recurring_ical_events.of(calendar_with_alarm, components=["VALARM"]).at(alarm_day)[0]
    >>> len(event.alarms.times)
    1
    >>> alarm = event.alarms.times[0]

    # the alarm happens one week before the event
    >>> event.start - alarm.trigger
    datetime.timedelta(days=7)

In the following code, we query the same day for a ``VEVENT`` component and we find nothing.
The event happens a week later.

.. code-block:: python

    # No events on that day. There is only an alarm.
    >>> recurring_ical_events.of(calendar_with_alarm, components=["VEVENT"]).at(alarm_day)
    []

When querying events and todos, they keep their alarms and other subcompnents.
These alarm times can be outside of the dates requested.

In this example, we get an event and find that it has several alarms in it.

.. code-block:: python

    >>> event_day = alarm_day + datetime.timedelta(days=7)
    >>> event = recurring_ical_events.of(calendar_with_alarm, components=["VEVENT"]).at(event_day)[0]

    # The event a week later has more than one alarm.
    >>> len(event.walk("VALARM"))
    2


Edit one event of an existing series
------------------------------------

Editing one event of a series is necessary for calendar invites e.g. via email.

Below, you see how to edit an event that occurs in a series.
It is important that you increase the `sequence number <https://www.rfc-editor.org/rfc/rfc5545#section-3.8.7.4>`_
of the event to indicate the new version.

.. code-block:: python

    >>> calendar = recurring_ical_events.example_calendar("recurring_events_moved")
    >>> event = recurring_ical_events.of(calendar).at("20190309")[0]

    # This event happens on 2019-03-09.
    >>> print(event["SUMMARY"])
    New Event

    # The event can be modified.
    >>> event["SUMMARY"] = "Modified Again!"

    # Make sure to increase the sequence number!
    # If you do not do that, the modification will not appear.
    >>> event["SEQUENCE"] = event.get("SEQUENCE", 0) + 1

    # Add the modified event to the calendar to replace the original.
    >>> calendar.add_component(event)

    # Get the day again and see the modified event.
    >>> event = recurring_ical_events.of(calendar).at("20190309")[0]
    >>> print(event["SUMMARY"])
    Modified Again!


Extend ``recurring-ical-events``
--------------------------------

All the functionality of ``recurring-ical-events`` can be extended and modified.
To understand where to extend, have a look at the `Architecture <../reference/architecture.html>`_.

The first place for extending is the collection of components.
Components are collected into a ``Series``.
A series belongs together because all components have the same ``UID``.
In this example, we collect one VEVENT which matches a certain UID:

.. code-block:: python

    >>> from recurring_ical_events import SelectComponents, EventAdapter, Series
    >>> from icalendar.cal import Component
    >>> from typing import Sequence

    # create the calendar
    >>> calendar_file = CALENDARS / "machbar_16_feb_2019.ics"
    >>> machbar_calendar = icalendar.Calendar.from_ical(calendar_file.read_bytes())

    # Create a collector of components that searches for an event with a specific UID
    >>> class CollectOneUIDEvent(SelectComponents):
    ...     def __init__(self, uid:str) -> None:
    ...         self.uid = uid
    ...     def collect_series_from(self, source: Component, suppress_errors: tuple) -> Sequence[Series]:
    ...         components : list[Component] = []
    ...         for component in source.walk("VEVENT"):
    ...             if component.get("UID") == self.uid:
    ...                 components.append(EventAdapter(component))
    ...         return [Series(components)] if components else []

    # collect only one UID: 4mm2ak3in2j3pllqdk1ubtbp9p@google.com
    >>> one_uid = CollectOneUIDEvent("4mm2ak3in2j3pllqdk1ubtbp9p@google.com")
    >>> uid_query = recurring_ical_events.of(machbar_calendar, components=[one_uid])
    >>> uid_query.count()  # the event has no recurrence and thus there is only one
    1

Several ways of extending the functionality have been created to override internals.
These can be subclassed or composed.

Below, you can choose to collect all components. Subclasses can be created for the
``Series`` and the ``Occurrence``. 

.. code-block:: python

    >>> from recurring_ical_events import AllKnownComponents, Series, Occurrence

    # we create a calendar with one event
    >>> calendar_file = CALENDARS / "one_event.ics"
    >>> one_event = icalendar.Calendar.from_ical(calendar_file.read_bytes())

    # You can override the Occurrence and Series classes for all computable components
    >>> select_all_known = AllKnownComponents(series=Series, occurrence=Occurrence)
    >>> select_all_known.names  # these are the supported types of components
    ['VALARM', 'VEVENT', 'VJOURNAL', 'VTODO']
    >>> query_all_known = recurring_ical_events.of(one_event, components=[select_all_known])

    # There should be exactly one event.
    >>> query_all_known.count()
    1

This example shows that the behavior for specific types of components can be extended.
Additional to the series, you can change the ``ComponentAdapter`` that provides
a unified interface for all the components with the same name (``VEVENT`` for example).

.. code-block:: python

    >>> from recurring_ical_events import ComponentsWithName, EventAdapter, JournalAdapter, TodoAdapter

    # You can also choose to select only specific subcomponents by their name.
    # The default arguments are added to show the extensibility.
    >>> select_events =   ComponentsWithName("VEVENT",   adapter=EventAdapter,   series=Series, occurrence=Occurrence)
    >>> select_todos =    ComponentsWithName("VTODO",    adapter=TodoAdapter,    series=Series, occurrence=Occurrence)
    >>> select_journals = ComponentsWithName("VJOURNAL", adapter=JournalAdapter, series=Series, occurrence=Occurrence)

    # There should be one event happening and nothing else
    >>> recurring_ical_events.of(one_event, components=[select_events]).count()
    1
    >>> recurring_ical_events.of(one_event, components=[select_todos]).count()
    0
    >>> recurring_ical_events.of(one_event, components=[select_journals]).count()
    0

So, if you would like to modify all events that are returned by the query,
you can do that subclassing the ``Occurrence`` class.


.. code-block:: python

    # This occurence changes adds a new attribute to the resulting events
    >>> class MyOccurrence(Occurrence):
    ...     """An occurrence that modifies the component."""
    ...     def as_component(self, keep_recurrence_attributes: bool) -> Component:
    ...         """Return a shallow copy of the source component and modify some attributes."""
    ...         component = super().as_component(keep_recurrence_attributes)
    ...         component["X-MY-ATTRIBUTE"] = "my occurrence"
    ...         return component
    >>> query = recurring_ical_events.of(one_event, components=[ComponentsWithName("VEVENT", occurrence=MyOccurrence)])
    >>> event = next(query.all())
    >>> event["X-MY-ATTRIBUTE"]
    'my occurrence'

This library allows extension of functionality during the selection of components to calculate using these classes:

* ``ComponentsWithName`` - for components of a certain name
* ``AllKnownComponents`` - for all components known
* ``SelectComponents`` - the interface to provide

You can further customize behaviour by subclassing these:

* ``ComponentAdapter`` such as ``EventAdapter``, ``JournalAdapter`` or ``TodoAdapter``.
* ``Series``
* ``Occurrence``
* ``CalendarQuery``


Increase Performance
--------------------

If you use :meth:`recurring_ical_events.CalendarQuery.between` and other queries
several times, it is faster to re-use the object coming from :func:`recurring_ical_events.of`.

.. code-block:: python

    >>> query = recurring_ical_events.of(a_calendar)
    >>> events_of_day_1 = query.at((2019, 2, 1))
    >>> events_of_day_2 = query.at((2019, 2, 2))
    >>> events_of_day_3 = query.at((2019, 2, 3))

    # ... and so on


Skip badly formatted ical events
--------------------------------

Some events may be badly formatted and therefore cannot be handled by ``recurring-ical-events``.
Passing ``skip_bad_series=True`` as ``of()`` argument will totally skip theses events.

.. code-block:: python

    # Create a calendar that contains broken events.
    >>> calendar_file = CALENDARS / "bad_rrule_missing_until_event.ics"
    >>> calendar_with_bad_event = icalendar.Calendar.from_ical(calendar_file.read_bytes())

     # By default, broken events result in errors.
    >>> recurring_ical_events.of(calendar_with_bad_event, skip_bad_series=False).count()
    Traceback (most recent call last):
      ...
    recurring_ical_events.errors.BadRuleStringFormat: UNTIL parameter is missing: FREQ=WEEKLY;BYDAY=TH;WKST=SU;UNTL=20191023

    # With skip_bad_series=True we skip the series that we cannot handle.
    >>> recurring_ical_events.of(calendar_with_bad_event, skip_bad_series=True).count()
    0

```

### `docs/user-guide/index.md`

```md
---
myst:
  html_meta:
    "description lang=en": |
      Documentation for users who wish query calendars for occurrences of events and other components.
---

# Get started

This section gets you started using this library.

## Installation

```{eval-rst}
.. tabs::

   .. tab:: Pip

      .. code-block:: bash

          pip install 'recurring-ical-events==3.*'

   .. tab:: Debian/Ubuntu

      .. code-block:: bash

          sudo apt-get install python-recurring-ical-events

   .. tab:: Alpine Linux

      .. code-block:: bash

          apk add py3-recurring-ical-events

   .. tab:: Fedora

      .. code-block:: bash

        sudo dnf install ???

   .. tab:: Arch Linux

      .. code-block:: bash

        sudo pacman -S python-recurring-ical-events


```

If not listed, this library is available as a package on the following platforms:

[![Packaging status](https://repology.org/badge/vertical-allrepos/python%3Arecurring-ical-events.svg?columns=3)](https://repology.org/project/python%3Arecurring-ical-events/versions)

## Usage

The [icalendar] module is responsible for parsing files with a calendar specification in it.
This library takes such a {py:class}`icalendar.cal.calendar.Calendar` and computes the occurrences.

To import this module, write

```python
>>> import recurring_ical_events

```

If you like to go deeper, have a look at the [API documentation](../reference/api) at this point.
We have a comprehensive list of **[examples]** to get you started.

[icalendar]: https://icalendar.readthedocs.io
[examples]: examples.rst

## User guide navigation

```{toctree}
:maxdepth: 1
:caption: User guide

examples
```

```

### `LICENSE`

```
                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.

```

### `pyproject.toml`

```toml
[build-system]
requires = ["hatchling>=1.27.0", "hatch-vcs"]
build-backend = "hatchling.build"

[project]
name = "recurring-ical-events"
license = "LGPL-3.0-or-later"
license-files = ["LICENSE"]
keywords = ["icalendar", "calendar", "ics", "rfc5545", "scheduling", "events", "todo", "journal", "alarm"]
dynamic = ["urls", "version"]
authors = [
  { name="Nicco Kunzmann", email="niccokunzmann@rambler.ru" },
]
maintainers = [
  { name="Nicco Kunzmann", email="niccokunzmann@rambler.ru" },
]
description = "Calculate recurrence times of events, todos, alarms and journals based on icalendar RFC5545."
readme = "README.rst"
requires-python = ">=3.8"

# see https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Topic :: Office/Business :: Scheduling",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]

# install requirements depending on python version
# see https://www.python.org/dev/peps/pep-0508/#environment-markers
dependencies = [
    'icalendar >= 6.1.0, < 8.0.0',
    'python-dateutil >= 2.8.1, < 3.0.0',
    'x-wr-timezone >= 1.0.0, < 3.0.0; python_version >= "3.9"',
    'x-wr-timezone == 0.*; python_version <= "3.8"',
    'backports.zoneinfo; python_version == "3.7" or python_version == "3.8"',
    'tzdata',
    'typing_extensions; python_version <= "3.9"',
]

[project.optional-dependencies]
test = [
    'pytest',
    'pytest-cov',
    'restructuredtext-lint',
    'pygments',
    'pytz >= 2023.3',
]

[tool.hatch.metadata.hooks.vcs.urls]
#[project.urls]
Homepage = "https://recurring-ical-events.readthedocs.io/"
Repository = "https://github.com/niccokunzmann/python-recurring-ical-events"
"Source Archive" = "https://github.com/niccokunzmann/python-recurring-ical-events/archive/{commit_hash}.zip"
Issues = "https://github.com/niccokunzmann/python-recurring-ical-events/issues"
Documentation = "https://github.com/niccokunzmann/python-recurring-ical-events"
Changelog = "https://github.com/niccokunzmann/python-recurring-ical-events?tab=readme-ov-file#changelog"
"Fund with GitHub Sponsors" = "https://github.com/sponsors/niccokunzmann"
"Fund with Polar" = "https://polar.sh/niccokunzmann/python-recurring-ical-events"
"Fund with Open Collective" = "https://opencollective.com/open-web-calendar"
"Fund with Tidelift" = "https://tidelift.com/funding/github/pypi/recurring-ical-events"

[tool.hatch.version]
source = "vcs"

[tool.hatch.version.raw-options]
# see https://github.com/ofek/hatch-vcs/issues/43#issuecomment-1553065222
local_scheme = "no-local-version"

[tool.hatch.build.hooks.vcs]
version-file = "recurring_ical_events/_version.py"

[tool.hatch.metadata]
allow-direct-references = true

[tool.ruff]
target-version = "py38"

[tool.ruff.lint]
select = ["ALL"]
ignore = [
    "ANN",     # flake8-annotations
    "B020",    # Loop control variable {name} overrides iterable it iterates
    "C401",    # Unnecessary generator (rewrite as a set comprehension)
    "C901",    # {name} is too complex ({complexity} > {max_complexity})
    "COM812",  # Trailing comma missing
    "D1",      # Missing docstring
    "D2",      # docstrings stuffs
    "D4",      # docstrings stuffs
    "EM10",    # Exception string usage
    "ERA001",  # Found commented-out code
    "FBT002",  # Boolean default positional argument in function definition
    "FIX",     # TODO comments
    "ISC001",  # Implicitly concatenated string literals on one line (to avoid with formatter)
    "N818",    # Exception name {name} should be named with an Error suffix
    "PLR091",  # Too many things (complexity, arguments, branches, etc...)
    "PLR2004", # Magic value used in comparison, consider replacing {value} with a constant variable
    "RUF012",  # Mutable class attributes should be annotated with typing.ClassVar
    "RUF015",  # Prefer next({iterable}) over single element slice
    "S101",    # Use of assert detected
    "TD",      # TODO comments
    "TRY003",  # Avoid specifying long messages outside the exception class
    "UP007",   # Use | None instead of Optional
]
extend-safe-fixes = [
    "PT006", # Wrong type passed to first argument of @pytest.mark.parametrize; expected {expected_string}
]

[tool.ruff.lint.per-file-ignores]
"recurring_ical_events/test/*" = [
    "B011",   # Do not assert False (python -O removes these calls), raise AssertionError()
    "DTZ001", # datetime.datetime() called without a tzinfo argument
    "E501",   # Indentation is not a multiple of {indent_size}
    "N802",   # Function name {name} should be lowercase
    "PT011",  # pytest.raises({exception}) is too broad, set the match parameter or use a more specific exception
    "PT012",  # pytest.raises() block should contain a single simple statement
    "PT015",  # Assertion always fails, replace with pytest.fail()
    "T201",   # print found
    "N803",   # ZoneInfo should be lowercase
]
"example.py" = [
    "T201", # print found
]

```

### `README.rst`

```rst
Recurring ICal events for Python
================================

.. image:: https://github.com/niccokunzmann/python-recurring-ical-events/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/niccokunzmann/python-recurring-ical-events/actions/workflows/tests.yml
   :alt: GitHub CI build and test status
.. image:: https://badge.fury.io/py/recurring-ical-events.svg
   :target: https://pypi.python.org/pypi/recurring-ical-events
   :alt: Python Package Version on Pypi
.. image:: https://img.shields.io/pypi/dm/recurring-ical-events.svg
   :target: https://pypi.org/project/recurring-ical-events/#files
   :alt: Downloads from Pypi
.. image:: https://img.shields.io/opencollective/all/open-web-calendar?label=support%20on%20open%20collective
   :target: https://opencollective.com/open-web-calendar/
   :alt: Support on Open Collective
.. image:: https://img.shields.io/github/issues/niccokunzmann/python-recurring-ical-events?logo=github&label=issues%20seek%20funding&color=%230062ff
   :target: https://polar.sh/niccokunzmann/python-recurring-ical-events
   :alt: issues seek funding

ICal has some complexity to it:
Events, TODOs, Journal entries and Alarms can be repeated, removed from the feed and edited later on.
This tool takes care of these complexities.

NLNet has supported the development of this library.

Please have a look here:

- `Documentation`_
- `Changelog`_
- `PyPI package`_
- `GitHub repository`_

.. _Documentation: https://recurring-ical-events.readthedocs.io/
.. _Changelog: https://recurring-ical-events.readthedocs.io/en/latest/changelog.html
.. _PyPI package: https://pypi.org/project/recurring-ical-events/
.. _GitHub repository: https://github.com/niccokunzmann/python-recurring-ical-events

```

### `recurring_ical_events/__init__.py`

```py
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Calculate repetitions of icalendar components."""

from __future__ import annotations

from typing import TYPE_CHECKING

import x_wr_timezone

from recurring_ical_events.adapters import (
    AbsoluteAlarmAdapter,
    ComponentAdapter,
    EventAdapter,
    JournalAdapter,
    TodoAdapter,
)
from recurring_ical_events.constants import DATE_MAX, DATE_MAX_DT, DATE_MIN, DATE_MIN_DT
from recurring_ical_events.errors import (
    BadRuleStringFormat,
    InvalidCalendar,
    PeriodEndBeforeStart,
)
from recurring_ical_events.examples import example_calendar
from recurring_ical_events.query import T_COMPONENTS, CalendarQuery
from recurring_ical_events.selection import (
    Alarms,
    AllKnownComponents,
    ComponentsWithName,
    SelectComponents,
)

from .occurrence import AlarmOccurrence, Occurrence, OccurrenceID
from .pages import OccurrencePage, OccurrencePages, Page, Pages
from .series import (
    AbsoluteAlarmSeries,
    AlarmSeriesRelativeToEnd,
    AlarmSeriesRelativeToStart,
    Series,
)

if TYPE_CHECKING:
    from icalendar.cal import Component


def of(
    a_calendar: Component,
    keep_recurrence_attributes=False,
    components: T_COMPONENTS = ("VEVENT",),
    skip_bad_series: bool = False,  # noqa: FBT001
    calendar_query: type[CalendarQuery] = CalendarQuery,
) -> CalendarQuery:
    """Create a query for recurring components in a_calendar.

    If the argument is a calendar, this will also correct
    times according to ``X-WR-TIMEZONE``.

    Arguments:
        a_calendar: an :class:`icalendar.cal.calendar.Calendar` component like
            :class:`icalendar.cal.calendar.Calendar`.
        keep_recurrence_attributes: Whether to keep attributes that are only used
            to calculate the recurrence (``RDATE``, ``EXDATE``, ``RRULE``).
        components: A list of component type names of which the recurrences
            should be returned. This can also be instances of :class:`SelectComponents`.
            Examples: ``("VEVENT", "VTODO", "VJOURNAL", "VALARM")``
        skip_bad_series: Whether to skip series of components that contain
            errors. You can use :attr:`CalendarQuery.suppressed_errors` to
            specify which errors to skip.
        calendar_query: The :class:`CalendarQuery` class to use.
    """
    a_calendar = x_wr_timezone.to_standard(a_calendar)
    return calendar_query(
        a_calendar, keep_recurrence_attributes, components, skip_bad_series
    )


__all__ = [
    "DATE_MAX",
    "DATE_MAX_DT",
    "DATE_MIN",
    "DATE_MIN_DT",
    "AbsoluteAlarmAdapter",
    "AbsoluteAlarmSeries",
    "AlarmOccurrence",
    "AlarmSeriesRelativeToEnd",
    "AlarmSeriesRelativeToStart",
    "Alarms",
    "AllKnownComponents",
    "BadRuleStringFormat",
    "CalendarQuery",
    "ComponentAdapter",
    "ComponentsWithName",
    "EventAdapter",
    "InvalidCalendar",
    "JournalAdapter",
    "Occurrence",
    "OccurrenceID",
    "OccurrencePage",
    "OccurrencePages",
    "Page",
    "Pages",
    "PeriodEndBeforeStart",
    "SelectComponents",
    "Series",
    "TodoAdapter",
    "example_calendar",
    "of",
]

```

### `recurring_ical_events/.gitignore`

```gitignore
_version.py

```

### `recurring_ical_events/adapters/__init__.py`

```py
"""All adapters for different kinds of components."""

from .alarm import AbsoluteAlarmAdapter
from .component import ComponentAdapter
from .event import EventAdapter
from .journal import JournalAdapter
from .todo import TodoAdapter

__all__ = [
    "AbsoluteAlarmAdapter",
    "ComponentAdapter",
    "EventAdapter",
    "JournalAdapter",
    "TodoAdapter",
]

```

### `recurring_ical_events/adapters/alarm.py`

```py
"""Adapter for VALARM components."""

from __future__ import annotations

from typing import TYPE_CHECKING

from recurring_ical_events.adapters.component import ComponentAdapter

if TYPE_CHECKING:
    from icalendar import Alarm


class AbsoluteAlarmAdapter(ComponentAdapter):  # TODO: remove
    """Adapter for absolute alarms."""

    def __init__(self, alarm: Alarm, parent: ComponentAdapter):
        """Create a new adapter."""
        super().__init__(alarm)
        self.parent = parent


__all__ = ["AbsoluteAlarmAdapter"]

```

### `recurring_ical_events/adapters/component.py`

```py
"""Base class for all adapters."""

from __future__ import annotations

import datetime
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Sequence

from icalendar.prop import vDDDTypes

from recurring_ical_events.util import (
    cached_property,
    make_comparable,
    time_span_contains_event,
    to_recurrence_ids,
)

if TYPE_CHECKING:
    from icalendar import Alarm
    from icalendar.cal import Component

    from recurring_ical_events.series import Series
    from recurring_ical_events.types import UID, RecurrenceIDs, Time


class ComponentAdapter(ABC):
    """A unified interface to work with icalendar components."""

    ATTRIBUTES_TO_DELETE_ON_COPY = ["RRULE", "RDATE", "EXDATE"]

    @staticmethod
    @abstractmethod
    def component_name() -> str:
        """The icalendar component name."""

    def __init__(self, component: Component):
        """Create a new adapter."""
        self._component = component

    @property
    def alarms(self) -> list[Alarm]:
        """The alarms in this component."""
        return self._component.walk("VALARM")

    @property
    def end_property(self) -> str | None:
        """The name of the end property."""
        return None

    @property
    def start(self) -> Time:
        """The start time."""
        return self.span[0]

    @property
    def end(self) -> Time:
        """The end time."""
        return self.span[1]

    @cached_property
    def span(self):
        """Return (start, end)."""
        start, end = make_comparable((self.raw_start, self.raw_end))
        if start > end:
            return end, start
        return start, end

    @property
    @abstractmethod
    def raw_start(self):
        """Return the start property of the component."""

    @property
    @abstractmethod
    def raw_end(self):
        """Return the start property of the component."""

    @property
    def uid(self) -> UID:
        """The UID of a component.

        UID is required by RFC5545.
        If the UID is absent, we use the Python ID.
        """
        return self._component.get("UID", str(id(self._component)))

    @classmethod
    def collect_series_from(
        cls, source: Component, suppress_errors: tuple[Exception]
    ) -> Sequence[Series]:
        """Collect all components for this adapter.

        This is a shortcut.
        """
        from recurring_ical_events.selection.name import ComponentsWithName

        return ComponentsWithName(cls.component_name(), cls).collect_series_from(
            source, suppress_errors
        )

    def as_component(
        self,
        start: Optional[Time] = None,
        stop: Optional[Time] = None,
        keep_recurrence_attributes: bool = True,  # noqa: FBT001
    ):
        """Create a shallow copy of the source event and modify some attributes."""
        copied_component = self._component.copy()
        copied_component["DTSTART"] = vDDDTypes(self.start if start is None else start)
        copied_component.pop("DURATION", None)  # remove duplication in event length
        if self.end_property is not None:
            copied_component[self.end_property] = vDDDTypes(
                self.end if stop is None else stop
            )
        if not keep_recurrence_attributes:
            for attribute in self.ATTRIBUTES_TO_DELETE_ON_COPY:
                if attribute in copied_component:
                    del copied_component[attribute]
        for subcomponent in self._component.subcomponents:
            copied_component.add_component(subcomponent)
        if "RECURRENCE-ID" not in copied_component:
            copied_component["RECURRENCE-ID"] = vDDDTypes(
                copied_component["DTSTART"].dt
            )
        return copied_component

    @cached_property
    def recurrence_ids(self) -> RecurrenceIDs:
        """The recurrence ids of the component that might be used to identify it."""
        recurrence_id = self._component.get("RECURRENCE-ID")
        if recurrence_id is None:
            return ()
        return to_recurrence_ids(recurrence_id.dt)

    @cached_property
    def this_and_future(self) -> bool:
        """The recurrence ids has a thisand future range property"""
        recurrence_id = self._component.get("RECURRENCE-ID")
        if recurrence_id is None:
            return False
        if "RANGE" in recurrence_id.params:
            return recurrence_id.params["RANGE"] == "THISANDFUTURE"
        return False

    def is_modification(self) -> bool:
        """Whether the adapter is a modification."""
        return bool(self.recurrence_ids)

    @cached_property
    def sequence(self) -> int:
        """The sequence in the history of modification.

        The sequence is negative if none was found.
        """
        return self._component.get("SEQUENCE", -1)

    def __repr__(self) -> str:
        """Debug representation with more info."""
        return (
            f"<{self.__class__.__name__} UID={self.uid} start={self.start} "
            f"recurrence_ids={self.recurrence_ids} sequence={self.sequence} "
            f"end={self.end}>"
        )

    @cached_property
    def exdates(self) -> list[Time]:
        """A list of exdates."""
        result: list[Time] = []
        exdates = self._component.get("EXDATE", [])
        for exdates in (exdates,) if not isinstance(exdates, list) else exdates:
            result.extend(exdate.dt for exdate in exdates.dts)
        return result

    @cached_property
    def rrules(self) -> set[str]:
        """A list of rrules of this component."""
        rules = self._component.get("RRULE", None)
        if not rules:
            return set()
        return {
            rrule.to_ical().decode()
            for rrule in (rules if isinstance(rules, list) else [rules])
        }

    @cached_property
    def rdates(self) -> list[Time, tuple[Time, Time]]:
        """A list of rdates, possibly a period."""
        rdates = self._component.get("RDATE", [])
        result = []
        for rdates in (rdates,) if not isinstance(rdates, list) else rdates:
            result.extend(rdate.dt for rdate in rdates.dts)
        return result

    @cached_property
    def duration(self) -> datetime.timedelta:
        """The duration of the component."""
        return self.end - self.start

    def is_in_span(self, span_start: Time, span_stop: Time) -> bool:
        """Return whether the component is in the span."""
        return time_span_contains_event(span_start, span_stop, self.start, self.end)

    @cached_property
    def extend_query_span_by(self) -> tuple[datetime.timedelta, datetime.timedelta]:
        """Calculate how much we extend the query span.

        If an event is long, we need to extend the query span by the event's duration.
        If an event has moved, we need to make sure that that is included, too.

        This is so that the RECURRENCE-ID falls within the modified span.
        Imagine if the span is exactly a second. How much would we need to query
        forward and backward to capture the recurrence id?

        Returns two positive spans: (subtract_from_start, add_to_stop)
        """
        subtract_from_start = self.duration
        add_to_stop = datetime.timedelta(0)
        recurrence_id_prop = self._component.get("RECURRENCE-ID")
        if recurrence_id_prop:
            start, end, recurrence_id = make_comparable(
                (self.start, self.end, recurrence_id_prop.dt)
            )
            if start < recurrence_id:
                add_to_stop = recurrence_id - start
            if start > recurrence_id:
                subtract_from_start = end - recurrence_id
        return subtract_from_start, add_to_stop

    @cached_property
    def move_recurrences_by(self) -> datetime.timedelta:
        """Occurrences of this component should be moved by this amount.

        Usually, the occurrence starts at the new start time.
        However, if we have a RANGE=THISANDFUTURE, we need to move the occurrence.

        RFC 5545:

            When the given recurrence instance is
            rescheduled, all subsequent instances are also rescheduled by the
            same time difference.  For instance, if the given recurrence
            instance is rescheduled to start 2 hours later, then all
            subsequent instances are also rescheduled 2 hours later.
            Similarly, if the duration of the given recurrence instance is
            modified, then all subsequence instances are also modified to have
            this same duration.
        """
        if self.this_and_future:
            recurrence_id_prop = self._component.get("RECURRENCE-ID")
            assert recurrence_id_prop, "RANGE=THISANDFUTURE implies RECURRENCE-ID."
            start, recurrence_id = make_comparable((self.start, recurrence_id_prop.dt))
            return start - recurrence_id
        return datetime.timedelta(0)

    def has_recurrence_rules(self):
        """Whether this has generation rules present."""
        return (
            "RRULE" in self._component
            or "RDATE" in self._component
            or "EXDATE" in self._component
        )


__all__ = ["ComponentAdapter"]

```

### `recurring_ical_events/adapters/event.py`

```py
"""Adapter for VEVENT."""

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from recurring_ical_events.adapters.component import ComponentAdapter
from recurring_ical_events.util import (
    convert_to_datetime,
    is_date,
    normalize_pytz,
)

if TYPE_CHECKING:
    from recurring_ical_events.types import Time


class EventAdapter(ComponentAdapter):
    """An icalendar event adapter."""

    @staticmethod
    def component_name() -> str:
        """The icalendar component name."""
        return "VEVENT"

    @property
    def end_property(self) -> str:
        """DTEND"""
        return "DTEND"

    @property
    def raw_start(self) -> Time:
        """Return DTSTART"""
        # Arguably, it may be considered a feature that this breaks
        # if no DTSTART is set
        return self._component["DTSTART"].dt

    @property
    def raw_end(self) -> Time:
        """Yield DTEND or calculate the end of the event based on
        DTSTART and DURATION.
        """
        ## an even may have DTEND or DURATION, but not both
        end = self._component.get("DTEND")
        if end is not None:
            return end.dt
        duration = self._component.get("DURATION")
        if duration is not None:
            start = self._component["DTSTART"].dt
            if duration.dt.seconds != 0 and is_date(start):
                start = convert_to_datetime(start, None)
            return normalize_pytz(start + duration.dt)
        start = self._component["DTSTART"].dt
        if is_date(start):
            return start + datetime.timedelta(days=1)
        return start


__all__ = ["EventAdapter"]

```

### `recurring_ical_events/adapters/journal.py`

```py
"""Adapter for VJOURNAL."""

from recurring_ical_events.adapters.component import ComponentAdapter
from recurring_ical_events.constants import DATE_MIN_DT
from recurring_ical_events.types import Time
from recurring_ical_events.util import cached_property


class JournalAdapter(ComponentAdapter):
    """Apdater for journal entries."""

    @staticmethod
    def component_name() -> str:
        """The icalendar component name."""
        return "VJOURNAL"

    @property
    def end_property(self) -> None:
        """There is no end property"""

    @property
    def raw_start(self) -> Time:
        """Return DTSTART if it set, do not panic if it's not set."""
        ## according to the specification, DTSTART in a VJOURNAL is optional
        dtstart = self._component.get("DTSTART")
        if dtstart is not None:
            return dtstart.dt
        return DATE_MIN_DT

    @cached_property
    def raw_end(self) -> Time:
        """The end time is the same as the start."""
        ## VJOURNAL cannot have a DTEND.  We should consider a VJOURNAL to
        ## describe one day if DTSTART is a date, and we can probably
        ## consider it to have zero duration if a timestamp is given.
        return self.raw_start


__all__ = ["JournalAdapter"]

```

### `recurring_ical_events/adapters/todo.py`

```py
"""Adapter for VTODO."""

from recurring_ical_events.adapters.component import ComponentAdapter
from recurring_ical_events.constants import DATE_MAX_DT, DATE_MIN_DT
from recurring_ical_events.types import Time
from recurring_ical_events.util import (
    convert_to_datetime,
    is_date,
    normalize_pytz,
)


class TodoAdapter(ComponentAdapter):
    """Unified access to TODOs."""

    @staticmethod
    def component_name() -> str:
        """The icalendar component name."""
        return "VTODO"

    @property
    def end_property(self) -> str:
        """DUE"""
        return "DUE"

    @property
    def raw_start(self) -> Time:
        """Return DTSTART if it set, do not panic if it's not set."""
        ## easy case - DTSTART set
        start = self._component.get("DTSTART")
        if start is not None:
            return start.dt
        ## Tasks may have DUE set, but no DTSTART.
        ## Let's assume 0 duration and return the DUE
        due = self._component.get("DUE")
        if due is not None:
            return due.dt

        ## Assume infinite time span if neither is given
        ## (see the comments under _get_event_end)
        return DATE_MIN_DT

    @property
    def raw_end(self) -> Time:
        """Return DUE or DTSTART+DURATION or something"""
        ## Easy case - DUE is set
        end = self._component.get("DUE")
        if end is not None:
            return end.dt

        dtstart = self._component.get("DTSTART")

        ## DURATION can be specified instead of DUE.
        duration = self._component.get("DURATION")
        ## It is no requirement that DTSTART is set.
        ## Perhaps duration is a time estimate rather than an indirect
        ## way to set DUE.
        if duration is not None and dtstart is not None:
            start = dtstart.dt
            if duration.dt.seconds != 0 and is_date(start):
                start = convert_to_datetime(start, None)
            return normalize_pytz(start + duration.dt)

        ## According to the RFC, a VEVENT without an end/duration
        ## is to be considered to have zero duration.  Assuming the
        ## same applies to VTODO.
        if dtstart:
            return dtstart.dt

        ## The RFC says this about VTODO:
        ## > A "VTODO" calendar component without the "DTSTART" and "DUE" (or
        ## > "DURATION") properties specifies a to-do that will be associated
        ## > with each successive calendar date, until it is completed.
        ## It can be interpreted in different ways, though probably it may
        ## be considered equivalent with a DTSTART in the infinite past and DUE
        ## in the infinite future?
        return DATE_MAX_DT


__all__ = ["TodoAdapter"]

```

### `recurring_ical_events/constants.py`

```py
"""Constants for recurring_ical_events."""

import datetime
import re
from pathlib import Path

# The minimum value accepted as date (pytz + zoneinfo)
DATE_MIN = (1970, 1, 1)
DATE_MIN_DT = datetime.date(*DATE_MIN)
# The maximum value accepted as date (pytz + zoneinfo)
DATE_MAX = (2038, 1, 1)
DATE_MAX_DT = datetime.date(*DATE_MAX)

# the location of this file
HERE = Path(__file__).parent

# the directory with all example calendars
CALENDARS = HERE / "test" / "calendars"

NEGATIVE_RRULE_COUNT_REGEX = re.compile(r"COUNT=-\d+;?")

__all__ = [
    "CALENDARS",
    "DATE_MAX",
    "DATE_MAX_DT",
    "DATE_MIN",
    "DATE_MIN_DT",
    "NEGATIVE_RRULE_COUNT_REGEX",
]

```

### `recurring_ical_events/errors.py`

```py
"""All the errors."""

from recurring_ical_events.types import Time


class InvalidCalendar(ValueError):
    """Exception thrown for bad icalendar content."""

    def __init__(self, message: str):
        """Create a new error with a message."""
        self._message = message
        super().__init__(self.message)

    @property
    def message(self) -> str:
        """The error message."""
        return self._message


class PeriodEndBeforeStart(InvalidCalendar):
    """An event or component starts before it ends."""

    def __init__(self, message: str, start: Time, end: Time):
        """Create a new PeriodEndBeforeStart error."""
        super().__init__(message)
        self._start = start
        self._end = end

    @property
    def start(self) -> Time:
        """The start of the component's period."""
        return self._start

    @property
    def end(self) -> Time:
        """The end of the component's period."""
        return self._end


class BadRuleStringFormat(InvalidCalendar):
    """An iCal rule string is badly formatted."""

    def __init__(self, message: str, rule: str):
        """Create an error with a bad rule string."""
        super().__init__(message + ": " + rule)
        self._rule = rule

    @property
    def rule(self) -> str:
        """The malformed rule string"""
        return self._rule


__all__ = ["BadRuleStringFormat", "InvalidCalendar", "PeriodEndBeforeStart"]

```

### `recurring_ical_events/examples.py`

```py
"""Functionality for smaller examples."""

import icalendar

from recurring_ical_events.constants import CALENDARS


def example_calendar(name: str = "") -> icalendar.Calendar:
    """Return an example calendar.

    Args:
        name (str): The name of the example file.

    Returns:
        icalendar.cal.Calendar: The parsed calendar example.
    """
    if not name.endswith(".ics"):
        name += ".ics"
    path = CALENDARS / name
    try:
        return icalendar.Calendar.from_ical(path.read_bytes())
    except FileNotFoundError:
        raise ValueError(  # noqa: B904
            f"File {name!r} not found. "
            f"Use one of {', '.join(p.name for p in CALENDARS.glob('*.ics'))!r}."
        )


__all__ = ["example_calendar"]

```

### `recurring_ical_events/occurrence.py`

```py
"""Occurrences of events and other components."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import TYPE_CHECKING, NamedTuple, Optional

from icalendar import Alarm

from recurring_ical_events.adapters.component import ComponentAdapter
from recurring_ical_events.util import (
    cached_property,
    make_comparable,
    time_span_contains_event,
)

if TYPE_CHECKING:
    from icalendar import Alarm
    from icalendar.cal import Component

    from recurring_ical_events.adapters.component import ComponentAdapter
    from recurring_ical_events.types import UID, RecurrenceIDs, Time


class OccurrenceID(NamedTuple):
    """The ID of a component's occurrence to identify it clearly.

    Attributes:
        name: The name of the component, e.g. "VEVENT"
        uid: The UID of the component.
        recurrence_id: The Recurrence-ID of the component in UTC but without tzinfo.
        start: The start of the component

    """

    name: str
    uid: UID
    recurrence_id: Optional[Time]
    start: Time

    def to_string(self) -> str:
        """Return a string representation of this id."""
        return "#".join(
            [
                self.name,
                self.recurrence_id.isoformat() if self.recurrence_id else "",
                self.start.isoformat(),
                self.uid,
            ]
        )

    @staticmethod
    def _dt_from_string(iso_string: str) -> Time:
        """Create a datetime from the string representation."""
        if len(iso_string) == 10:
            return date.fromisoformat(iso_string)
        return datetime.fromisoformat(iso_string)

    @classmethod
    def from_string(cls, string_id: str) -> OccurrenceID:
        """Parse a string and return the component id."""
        name, recurrence_id, start, uid = string_id.split("#", 3)
        return cls(
            name,
            uid,
            cls._dt_from_string(recurrence_id) if recurrence_id else None,
            cls._dt_from_string(start),
        )

    @classmethod
    def from_occurrence(
        cls, name: str, uid: str, recurrence_ids: RecurrenceIDs, start: Time
    ):
        """Create a new OccurrenceID from the given values.

        Args:
            name: The component name.
            uid: The UID string.
            recurrence_ids: The recurrence ID tuple.
                This is expected as UTC with tzinfo being None.
            start: start time of the component either with or without timezone
        """
        return cls(name, uid, recurrence_ids[0] if recurrence_ids else None, start)


class Occurrence:
    """A repetition of an event."""

    def __init__(
        self,
        adapter: ComponentAdapter,
        start: Time | None = None,
        end: Time | None | timedelta = None,
        sequence: int = -1,
    ):
        """Create an event repetition.

        - source - the icalendar Event
        - start - the start date/datetime to replace
        - stop - the end date/datetime to replace
        - sequence - if positive or 0, this sets the SEQUENCE property
        """
        self._adapter = adapter
        self.start = adapter.start if start is None else start
        self.end = adapter.end if end is None else end
        self.sequence = sequence

    def __repr__(self) -> str:
        """The string representation."""
        return (
            f"<{self.__class__.__name__} "
            f"adapter={self._adapter.__class__.__name__} "
            f"UID={self.uid} "
            f"start={self.start} "
            f"sequence={self.sequence} "
            f"component.sequence={self._adapter.sequence} "
            ">"
        )

    def as_component(self, keep_recurrence_attributes: bool) -> Component:  # noqa: FBT001
        """Create a shallow copy of the source component and modify some attributes."""
        component = self._adapter.as_component(
            self.start, self.end, keep_recurrence_attributes
        )
        if self.sequence >= 0:
            component["SEQUENCE"] = self.sequence
        return component

    def is_in_span(self, span_start: Time, span_stop: Time) -> bool:
        """Return whether the component is in the span."""
        return time_span_contains_event(span_start, span_stop, self.start, self.end)

    def __lt__(self, other: Occurrence) -> bool:
        """Compare two occurrences for sorting.

        See https://stackoverflow.com/a/4010558/1320237
        """
        self_start, other_start = make_comparable((self.start, other.start))
        return self_start < other_start

    @cached_property
    def id(self) -> OccurrenceID:
        """The id of the component."""
        return OccurrenceID.from_occurrence(
            self._adapter.component_name(),
            self._adapter.uid,
            self._adapter.recurrence_ids,
            self.start,
        )

    def __hash__(self) -> int:
        """Hash this for an occurrence."""
        return hash(self.id)

    def __eq__(self, other: Occurrence) -> bool:
        """self == other"""
        return self.id == other.id

    def component_name(self) -> str:
        """The name of this component."""
        return self._adapter.component_name()

    @property
    def uid(self) -> str:
        """The UID of this occurrence."""
        return self._adapter.uid

    def has_alarm(self, alarm: Alarm) -> bool:
        """Wether this alarm is in this occurrence."""
        return alarm in self._adapter.alarms

    @property
    def recurrence_ids(self) -> RecurrenceIDs:
        """The recurrence ids."""
        return self._adapter.recurrence_ids


class AlarmOccurrence(Occurrence):
    """Adapter for absolute alarms."""

    def __init__(
        self,
        trigger: datetime,
        alarm: Alarm,
        parent: ComponentAdapter | Occurrence,
    ) -> None:
        super().__init__(alarm, trigger, trigger)
        self.parent = parent
        self.alarm = alarm

    def as_component(self, keep_recurrence_attributes):
        """Return the alarm's parent as a modified component."""
        parent = self.parent.as_component(
            keep_recurrence_attributes=keep_recurrence_attributes
        )
        alarm_once = self.alarm.copy()
        alarm_once.TRIGGER = self.start
        alarm_once.REPEAT = 0
        parent.subcomponents = [alarm_once]
        return parent

    @cached_property
    def id(self) -> OccurrenceID:
        """The id of the component."""
        return OccurrenceID.from_occurrence(
            self.parent.component_name(),
            self.parent.uid,
            self.parent.recurrence_ids,
            self.start,
        )

    def __repr__(self) -> str:
        """repr(self)"""
        return (
            f"<{self.__class__.__name__} at {self.start} of"
            f" {self.alarm} in {self.parent}"
        )


__all__ = [
    "AlarmOccurrence",
    "Occurrence",
    "OccurrenceID",
]

```

### `recurring_ical_events/pages.py`

```py
"""Pagination for recurring ical events.

See

- https://github.com/niccokunzmann/python-recurring-ical-events/issues/211
- https://github.com/niccokunzmann/python-recurring-ical-events/issues/217
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Iterator, Optional, TypeVar

from recurring_ical_events.util import compare_greater

if TYPE_CHECKING:
    from icalendar import Component

    from recurring_ical_events.occurrence import Occurrence
    from recurring_ical_events.types import Time

T = TypeVar("T")


class _PageBase(Generic[T]):
    """Shared behaviour for :class:`Page` and :class:`OccurrencePage`."""

    def __init__(self, items: list[T], next_page_id: str = ""):
        self._items = items
        self._next_page_id = next_page_id

    def has_next_page(self) -> bool:
        """Wether there is a page following this one."""
        return self._next_page_id != ""

    @property
    def next_page_id(self) -> str:
        """The id of the next page or ``''``."""
        return self._next_page_id

    def is_last(self) -> bool:
        """Wether this is the last page and there is no other page following."""
        return self._next_page_id == ""

    def __len__(self) -> int:
        """The number of items on this page."""
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        """Return an iterator over the items."""
        return iter(self._items)


class Page(_PageBase["Component"]):
    """One page in a series of pages.

    Examples:
        Check if the page has components.

        .. code-block:: python

            if page:
                print(f"We have {len(page)} components.")

        Go though the components:

        .. code-block:: python

            for component in page:
                print(component)
    """

    def __init__(self, components: list[Component], next_page_id: str = ""):
        """ "Create a new page."""
        super().__init__(components, next_page_id)

    @property
    def components(self) -> list[Component]:
        """All the components of this page."""
        return self._items


class OccurrencePage(_PageBase["Occurrence"]):
    """One page of occurrences in a series of pages.

    Examples:
        Check if the page has occurrences.

        .. code-block:: python

            if page:
                print(f"We have {len(page)} occurrences.")

        Go though the occurrences:

        .. code-block:: python

            for occurrence in page:
                print(occurrence)
    """

    def __init__(self, occurrences: list[Occurrence], next_page_id: str = ""):
        """Create a new occurrence page."""
        super().__init__(occurrences, next_page_id)

    @property
    def occurrences(self) -> list[Occurrence]:
        """All the occurrences of this page."""
        return self._items


class _PagesBase(Generic[T]):
    """Shared iteration state for :class:`Pages` and :class:`OccurrencePages`."""

    def __init__(
        self,
        occurrence_iterator: Iterator[Occurrence],
        size: int,
        stop: Optional[Time] = None,
    ):
        self._iterator = occurrence_iterator
        self._stop = stop
        self._size = size
        if self._size <= 0:
            raise ValueError(f"A page must have at least one item, not {self._size}.")
        self._next_occurrence: Optional[Occurrence] = None
        for occurrence in self._iterator:
            if self._stop is None or compare_greater(self._stop, occurrence.start):
                self._next_occurrence = occurrence
            break

    @property
    def size(self) -> int:
        """The maximum number of items per page."""
        return self._size

    def generate_next_page(self) -> T:
        """Generate the next page.

        In contrast to ``next(pages)``, this does not raise :class:`StopIteration`.
        But it works the same: the next page is generated and returned.
        The last page is empty.
        """
        for page in self:
            return page
        return self._empty_page()

    def _empty_page(self) -> T:
        """The empty page returned past the end of the iterator."""
        raise NotImplementedError

    def _collect_next_page(self) -> list[Occurrence]:
        """Pull the next page-worth of occurrences from the source iterator."""
        if self._next_occurrence is None:
            raise StopIteration
        last_occurrence = self._next_occurrence
        occurrences = [last_occurrence]
        for occurrence in self._iterator:
            if self._stop is not None and compare_greater(occurrence.start, self._stop):
                break
            last_occurrence = occurrence
            if len(occurrences) < self._size:
                occurrences.append(occurrence)
            else:
                break
        if occurrences[-1] == last_occurrence:
            self._next_occurrence = None
        else:
            self._next_occurrence = last_occurrence
        return occurrences

    def _next_page_id_string(self) -> str:
        """The id of the page following the one we just emitted, or ``''``."""
        return (
            self._next_occurrence.id.to_string()
            if self._next_occurrence is not None
            else ""
        )


class Pages(_PagesBase["Page"]):
    """A pagination configuration to iterate over pages.

    This is an :class:`Iterator` that returns :class:`Page` objects.
    """

    def __init__(
        self,
        occurrence_iterator: Iterator[Occurrence],
        size: int,
        stop: Optional[Time] = None,
        keep_recurrence_attributes: bool = False,  # noqa: FBT001
    ):
        """Create a new paginated iterator over components."""
        super().__init__(occurrence_iterator, size, stop)
        self._keep_recurrence_attributes = keep_recurrence_attributes

    def _empty_page(self) -> Page:
        return Page([])

    def __next__(self) -> Page:
        """Return the next page."""
        occurrences = self._collect_next_page()
        return Page(
            [
                occurrence.as_component(self._keep_recurrence_attributes)
                for occurrence in occurrences
            ],
            next_page_id=self._next_page_id_string(),
        )

    def __iter__(self) -> Pages:
        """Return the iterator."""
        return self


class OccurrencePages(_PagesBase["OccurrencePage"]):
    """A pagination configuration to iterate over pages of occurrences.

    This is an :class:`Iterator` that returns :class:`OccurrencePage` objects.
    """

    def _empty_page(self) -> OccurrencePage:
        return OccurrencePage([])

    def __next__(self) -> OccurrencePage:
        """Return the next page."""
        occurrences = self._collect_next_page()
        return OccurrencePage(occurrences, next_page_id=self._next_page_id_string())

    def __iter__(self) -> OccurrencePages:
        """Return the iterator."""
        return self


__all__ = ["OccurrencePage", "OccurrencePages", "Page", "Pages"]

```

### `recurring_ical_events/query.py`

```py
"""Core functionality: querying the calendar for occurrences."""

from __future__ import annotations

import contextlib
import datetime
import itertools
import sys
from typing import TYPE_CHECKING, ClassVar, Generator, Iterator, Optional, Sequence

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

import icalendar

from recurring_ical_events.adapters.component import ComponentAdapter
from recurring_ical_events.constants import DATE_MAX_DT, DATE_MIN_DT
from recurring_ical_events.errors import (
    BadRuleStringFormat,
    InvalidCalendar,
    PeriodEndBeforeStart,
)
from recurring_ical_events.occurrence import OccurrenceID
from recurring_ical_events.pages import OccurrencePages, Pages
from recurring_ical_events.selection.base import SelectComponents
from recurring_ical_events.util import compare_greater

if TYPE_CHECKING:
    from icalendar import Component

    from recurring_ical_events.occurrence import Occurrence
    from recurring_ical_events.series import Series
    from recurring_ical_events.types import (
        DateArgument,
        Time,
    )

if sys.version_info >= (3, 10):
    T_COMPONENTS: TypeAlias = Sequence[str | type[ComponentAdapter] | SelectComponents]
else:
    # see https://github.com/python/cpython/issues/86399#issuecomment-1093889925
    T_COMPONENTS: TypeAlias = Sequence[str]


class CalendarQuery:
    """Query a calendar for occurrences.

    Functions like :meth:`at`, :meth:`between` andm :meth:`after`
    can be used to query the selected components.
    If any malformed icalendar information is found,
    an :class:`InvalidCalendar` exception is raised.
    For other bad arguments, you should expect a :class:`ValueError`.

    Attributes:
        suppressed_errors: a list of errors to suppress when
            skip_bad_series is True
    """

    suppressed_errors: ClassVar[type[Exception]] = [
        BadRuleStringFormat,
        PeriodEndBeforeStart,
        icalendar.InvalidCalendar,
    ]
    from recurring_ical_events.selection.name import ComponentsWithName

    def __init__(
        self,
        calendar: Component,
        keep_recurrence_attributes: bool = False,  # noqa: FBT001
        components: T_COMPONENTS = ("VEVENT",),
        skip_bad_series: bool = False,  # noqa: FBT001
    ):
        """Create an unfoldable calendar from a given calendar.

        Arguments:
            calendar: an :class:`icalendar.cal.Calendar` component like
                :class:`icalendar.cal.Calendar`.
            keep_recurrence_attributes: Whether to keep attributes that are only used
                to calculate the recurrence (``RDATE``, ``EXDATE``, ``RRULE``).
            components: A list of component type names of which the recurrences
                should be returned. This can also be instances of
                :class:`SelectComponents`.
                Examples: ``("VEVENT", "VTODO", "VJOURNAL", "VALARM")``
            skip_bad_series: Whether to skip series of components that contain
                errors. You can use :attr:`CalendarQuery.suppressed_errors` to
                specify which errors to skip.
        """
        self.keep_recurrence_attributes = keep_recurrence_attributes
        if calendar.get("CALSCALE", "GREGORIAN") != "GREGORIAN":
            # https://www.kanzaki.com/docs/ical/calscale.html
            raise InvalidCalendar("Only Gregorian calendars are supported.")

        self.series: list[Series] = []  # component
        self._skip_errors = tuple(self.suppressed_errors) if skip_bad_series else ()
        for component_adapter_id in components:
            if isinstance(component_adapter_id, str):
                component_adapter = self.ComponentsWithName(component_adapter_id)
            else:
                component_adapter = component_adapter_id
            self.series.extend(
                component_adapter.collect_series_from(calendar, self._skip_errors)
            )

    @staticmethod
    def to_datetime(date: DateArgument):
        """Convert date inputs of various sorts into a datetime object.

        Arguments:
            date: A date specification.

        Date Specification:

        - a year like ``(2019,)`` or ``2019`` (:class:`int`)
        - a month like ``(2019, 1)`` for January of 2019
        - a day like ``(2019, 1, 19)`` for the first of January 2019
        - a day with hours, ``(2019, 1, 19, 1)``
        - a day with minutes, ``(2019, 1, 19, 13, 30 )``
        - a day with seconds, ``(2019, 1, 19, 13, 30, 59)``
        - a :class:`datetime.datetime` or :class:`datetime.date`
        - a :class:`str` in the format ``yyyymmdd``
        - a :class:`str` in the format ``yyyymmddThhmmssZ``

        """
        if isinstance(date, int):
            date = (date,)
        if isinstance(date, tuple):
            date += (1,) * (3 - len(date))
            return datetime.datetime(*date)  # noqa: DTZ001
        if isinstance(date, str):
            # see https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
            if len(date) == 8:
                return datetime.datetime.strptime(date, "%Y%m%d")  # noqa: DTZ007
            return datetime.datetime.strptime(date, "%Y%m%dT%H%M%SZ")  # noqa: DTZ007
        return date

    def all(self) -> Generator[Component]:
        """Generate all Components.

        The Components are sorted from the first to the last Occurrence.
        Calendars can contain millions of Occurrences. This iterates
        safely across all of them.
        """
        # MAX and MIN values may change in the future
        return self.after(DATE_MIN_DT)

    def occurrences_all(self) -> Generator[Occurrence]:
        """Yield every :class:`Occurrence` in the calendar, ordered by start time."""
        # MAX and MIN values may change in the future
        return self.occurrences_after(DATE_MIN_DT)

    _DELTAS = [
        datetime.timedelta(days=1),
        datetime.timedelta(hours=1),
        datetime.timedelta(minutes=1),
        datetime.timedelta(seconds=1),
    ]

    def at(self, date: DateArgument):
        """Return all events within the next 24 hours of starting at the given day.

        Arguments:
            date: A date specification, see :meth:`to_datetime`.

        This is translated to :meth:`between` in the following way:

        - A year returns all occurrences within that year.
            Example: ``(2019,)``, ``2019``
        - A month returns all occurrences within that month.
            Example: ``(2019, 1)``
        - A day returns all occurrences within that day.
            Examples:

            - ``(2019, 1, 19)``
            - ``datetime.date(2019, 1, 19)``
            - ``"20190101"``

        - An hour returns all occurrences within that hour.
            Example: ``(2019, 1, 19, 1)``
        - A minute returns all occurrences within that minute.
            Example: ``(2019, 1, 19, 13, 30 )``
        - A second returns all occurrences at that exact second.
            Examples:

            - ``(2019, 1, 19, 13, 30, 59)``
            - ``datetime.datetime(2019, 1, 19, 13, 30, 59)``
            - ``datetime.datetime(2019, 1, 19, tzinfo=datetime.timezone.utc)``,
            - ``datetime.datetime(2019, 1, 19, 13, 30, 59, tzinfo=ZoneInfo('Europe/London'))``
            - ``"20190119T133059Z"``
        """  # noqa: E501
        start, stop = self._at_span(date)
        return self._between(start, stop)

    def occurrences_at(self, date: DateArgument) -> list[Occurrence]:
        """Return the :class:`Occurrence` objects covered by ``date``.

        ``date`` is interpreted the same way as in :meth:`at`.

        Arguments:
            date: A date specification, see :meth:`to_datetime`.
        """
        start, stop = self._at_span(date)
        return self._occurrences_between(start, stop)

    def _at_span(self, date: DateArgument) -> tuple[Time, Time]:
        """Translate an :meth:`at` date specification into a (start, stop) span."""
        if isinstance(date, int):
            date = (date,)
        if isinstance(date, str):
            if len(date) != 8 or not date.isdigit():
                raise ValueError(f"Format yyyymmdd expected for {date!r}.")
            date = (int(date[:4], 10), int(date[4:6], 10), int(date[6:]))
        if isinstance(date, datetime.datetime):
            return date, date
        if isinstance(date, datetime.date):
            return date, date + datetime.timedelta(days=1)
        if len(date) == 1:
            return (
                self.to_datetime((date[0], 1, 1)),
                self.to_datetime((date[0] + 1, 1, 1)),
            )
        if len(date) == 2:
            year, month = date
            if month == 12:
                return (
                    self.to_datetime((year, 12, 1)),
                    self.to_datetime((year + 1, 1, 1)),
                )
            return (
                self.to_datetime((year, month, 1)),
                self.to_datetime((year, month + 1, 1)),
            )
        dt = self.to_datetime(date)
        return dt, dt + self._DELTAS[len(date) - 3]

    def between(self, start: DateArgument, stop: DateArgument | datetime.timedelta):
        """Return events at a time between start (inclusive) and end (inclusive)

        Arguments:
            start: A date specification. See :meth:`to_datetime`.
            stop: A date specification or a :class:`datetime.timedelta`
                relative to start.

        .. warning::

            If you pass a :class:`datetime.datetime` to both ``start`` and
            ``stop``, make sure the :attr:`datetime.datetime.tzinfo` is
            the same.
        """
        start, stop = self._between_span(start, stop)
        return self._between(start, stop)

    def occurrences_between(
        self, start: DateArgument, stop: DateArgument | datetime.timedelta
    ) -> list[Occurrence]:
        """Return the :class:`Occurrence` objects in ``[start, stop]``.

        The :class:`Occurrence`-returning sibling of :meth:`between`.

        Arguments:
            start: A date specification. See :meth:`to_datetime`.
            stop: A date specification or a :class:`datetime.timedelta`
                relative to start.

        .. warning::

            If you pass a :class:`datetime.datetime` to both ``start`` and
            ``stop``, make sure the :attr:`datetime.datetime.tzinfo` is
            the same.
        """
        start, stop = self._between_span(start, stop)
        return self._occurrences_between(start, stop)

    def _between_span(
        self, start: DateArgument, stop: DateArgument | datetime.timedelta
    ) -> tuple[Time, Time]:
        """Normalize the (start, stop) arguments of :meth:`between`."""
        start = self.to_datetime(start)
        stop = (
            start + stop
            if isinstance(stop, datetime.timedelta)
            else self.to_datetime(stop)
        )
        return start, stop

    def _occurrences_to_components(
        self, occurrences: list[Occurrence]
    ) -> list[Component]:
        """Map occurrences to components."""
        return [
            occurrence.as_component(self.keep_recurrence_attributes)
            for occurrence in occurrences
        ]

    def _between(self, start: Time, end: Time) -> list[Component]:
        """Return the occurrences between the start and the end."""
        return self._occurrences_to_components(self._occurrences_between(start, end))

    def _occurrences_between(self, start: Time, end: Time) -> list[Occurrence]:
        """Return the components between the start and the end."""
        occurrences: list[Occurrence] = []
        for series in self.series:
            with contextlib.suppress(self._skip_errors):
                occurrences.extend(series.between(start, end))
        return occurrences

    def after(self, earliest_end: DateArgument) -> Generator[Component]:
        """Iterate over components happening during or after earliest_end.

        Arguments:
            earliest_end: A date specification. See :meth:`to_datetime`.
                Anything happening during or after earliest_end is returned
                in the order of start time.
        """
        earliest_end = self.to_datetime(earliest_end)
        for occurrence in self._after(earliest_end):
            yield occurrence.as_component(self.keep_recurrence_attributes)

    def occurrences_after(self, earliest_end: DateArgument) -> Generator[Occurrence]:
        """Iterate over :class:`Occurrence` objects happening during or after ``earliest_end``.

        Arguments:
            earliest_end: A date specification. See :meth:`to_datetime`.
                Anything happening during or after earliest_end is returned
                in the order of start time.
        """  # noqa: E501
        earliest_end = self.to_datetime(earliest_end)
        yield from self._after(earliest_end)

    def _after(self, earliest_end: Time) -> Generator[Occurrence]:
        """Iterate over occurrences happening during or after earliest_end."""
        time_span = datetime.timedelta(days=1)
        min_time_span = datetime.timedelta(minutes=15)
        done = False
        result_ids: set[OccurrenceID] = set()

        while not done:
            try:
                next_end = earliest_end + time_span
            except OverflowError:
                # We ran to the end
                next_end = DATE_MAX_DT
                if compare_greater(earliest_end, next_end):
                    return  # we might run too far
                done = True
            occurrences = self._occurrences_between(earliest_end, next_end)
            occurrences.sort()
            for occurrence in occurrences:
                if occurrence.id not in result_ids:
                    yield occurrence
                    result_ids.add(occurrence.id)
            # prepare next query
            time_span = max(
                time_span / 2 if occurrences else time_span * 2,
                min_time_span,
            )  # binary search to improve speed
            earliest_end = next_end

    def count(self) -> int:
        """Return the amount of recurring components in this calendar.

        .. warning::

            Do not use this in production as it generates all occurrences.
        """
        return sum(1 for _ in self.all())

    def occurrences_count(self) -> int:
        """Return the amount of recurring occurrences in this calendar.

        .. warning::

            Do not use this in production as it generates all occurrences.
        """
        return sum(1 for _ in self.occurrences_all())

    @property
    def first(self) -> Component:
        """Return the first recurring component in this calendar.

        Returns:
            The first recurring component in this calendar.

        Raises:
            IndexError: if the calendar is empty
        """
        return self._first(self.all(), "No components found.")

    @property
    def first_occurrence(self) -> Occurrence:
        """Return the first recurring occurrence in this calendar.

        Returns:
            The first recurring occurrence in this calendar.

        Raises:
            IndexError: if the calendar is empty
        """
        return self._first(self.occurrences_all(), "No occurrences found.")

    @staticmethod
    def _first(iterator: Iterator, not_found_message: str):
        """Return the first item of an iterator, or raise :class:`IndexError`."""
        for item in iterator:
            return item
        raise IndexError(not_found_message)

    def paginate(
        self,
        page_size: int,
        earliest_end: Optional[DateArgument] = None,
        latest_start: Optional[DateArgument] = None,
        next_page_id: str = "",
    ) -> Pages:
        """Return pages for pagination.

        Args:
            page_size: the number of components per page
            earliest_end: the start of the first page
                All components occur after this date.
                See :meth:`to_datetime` for possible values.
            latest_start: the end of the last page
                All components occur before this date.
                See :meth:`to_datetime` for possible values.
            next_page_id: The id of the next page.
                This is optional for the first page.
                These are safe to pass outside of the application and back in.
        """
        latest_start = None if latest_start is None else self.to_datetime(latest_start)
        iterator = self._paginate_iterator(earliest_end, next_page_id)
        return Pages(
            occurrence_iterator=iterator,
            size=page_size,
            stop=latest_start,
            keep_recurrence_attributes=self.keep_recurrence_attributes,
        )

    def occurrences_paginate(
        self,
        page_size: int,
        earliest_end: Optional[DateArgument] = None,
        latest_start: Optional[DateArgument] = None,
        next_page_id: str = "",
    ) -> OccurrencePages:
        """Return pages of :class:`Occurrence` objects.

        Same shape as :meth:`paginate`, but each page holds occurrences
        rather than components.

        Args:
            page_size: the number of occurrences per page
            earliest_end: the start of the first page.
                All occurrences happen after this date.
                See :meth:`to_datetime` for possible values.
            latest_start: the end of the last page.
                All occurrences happen before this date.
                See :meth:`to_datetime` for possible values.
            next_page_id: The id of the next page.
                This is optional for the first page.
                These are safe to pass outside of the application and back in.
        """
        latest_start = None if latest_start is None else self.to_datetime(latest_start)
        iterator = self._paginate_iterator(earliest_end, next_page_id)
        return OccurrencePages(
            occurrence_iterator=iterator,
            size=page_size,
            stop=latest_start,
        )

    def _paginate_iterator(
        self,
        earliest_end: Optional[DateArgument],
        next_page_id: str,
    ) -> Iterator[Occurrence]:
        """Build the occurrence iterator used by paginated queries."""
        earliest_end = (
            DATE_MIN_DT if earliest_end is None else self.to_datetime(earliest_end)
        )
        if next_page_id:
            first_occurrence_id = OccurrenceID.from_string(next_page_id)
            if not compare_greater(earliest_end, first_occurrence_id.start):
                iterator = self._after(first_occurrence_id.start)
                lost_occurrences = []  # in case the resume id isn't found
                for occurrence in iterator:
                    lost_occurrences.append(occurrence)
                    oid = occurrence.id
                    if oid == first_occurrence_id:
                        return itertools.chain([occurrence], iterator)
                    if compare_greater(oid.start, first_occurrence_id.start):
                        return itertools.chain(lost_occurrences, iterator)
                return iterator
        return self._after(earliest_end)


__all__ = ["T_COMPONENTS", "CalendarQuery"]

```

### `recurring_ical_events/selection/__init__.py`

```py
"""Select components for calculation."""

from .alarm import Alarms
from .all import AllKnownComponents
from .base import SelectComponents
from .name import ComponentsWithName

__all__ = [
    "Alarms",
    "AllKnownComponents",
    "ComponentsWithName",
    "SelectComponents",
]

```

### `recurring_ical_events/selection/alarm.py`

```py
"""Selection for alarms."""

from __future__ import annotations

import contextlib
import datetime
from typing import TYPE_CHECKING, Sequence

from recurring_ical_events.adapters.event import EventAdapter
from recurring_ical_events.adapters.todo import TodoAdapter
from recurring_ical_events.selection.base import SelectComponents

if TYPE_CHECKING:
    from icalendar.cal import Component

    from recurring_ical_events.adapters.component import ComponentAdapter
    from recurring_ical_events.series import Series


class Alarms(SelectComponents):
    """Select alarms and find their times.

    By default, alarms from TODOs and events are collected.
    You can use this to change which alarms are collected:

        Alarms((EventAdapter,))
        Alarms((TodoAdapter,))
    """

    def __init__(
        self,
        parents: tuple[type[ComponentAdapter] | SelectComponents] = (
            EventAdapter,
            TodoAdapter,
        ),
    ):
        self.parents = parents

    @staticmethod
    def component_name():
        """The name of the component we calculate."""
        return "VALARM"

    def collect_parent_series_from(
        self, source: Component, suppress_errors: tuple[Exception]
    ) -> Sequence[Series]:
        """Collect the parent components of alarms."""
        return [
            s
            for parent in self.parents
            for s in parent.collect_series_from(source, suppress_errors)
        ]

    def collect_series_from(
        self, source: Component, suppress_errors: tuple[Exception]
    ) -> Sequence[Series]:
        """Collect all TODOs and Alarms from VEVENTs and VTODOs.

        suppress_errors - a list of errors that should be suppressed.
            A Series of events with such an error is removed from all results.
        """
        from recurring_ical_events.series.alarm import (
            AbsoluteAlarmSeries,
            AlarmSeriesRelativeToEnd,
            AlarmSeriesRelativeToStart,
        )

        absolute_alarms = AbsoluteAlarmSeries()
        result = []
        # alarms might be copied several times. We only compute them once.
        for series in self.collect_parent_series_from(source, suppress_errors):
            used_alarms = []
            for component in series.components:
                for alarm in component.alarms:
                    with contextlib.suppress(suppress_errors):
                        trigger = alarm.TRIGGER
                        if trigger is None or alarm in used_alarms:
                            continue
                        if isinstance(trigger, datetime.datetime):
                            absolute_alarms.add(alarm, component)
                            used_alarms.append(alarm)
                        elif alarm.TRIGGER_RELATED == "START":
                            result.append(AlarmSeriesRelativeToStart(alarm, series))
                            used_alarms.append(alarm)
                        elif alarm.TRIGGER_RELATED == "END":
                            result.append(AlarmSeriesRelativeToEnd(alarm, series))
                            used_alarms.append(alarm)
        if not absolute_alarms.is_empty():
            result.append(absolute_alarms)
        return result


__all__ = ["Alarms"]

```

### `recurring_ical_events/selection/all.py`

```py
"""Selection of all components with the correct adapters."""

from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from recurring_ical_events.occurrence import Occurrence
from recurring_ical_events.selection.base import SelectComponents
from recurring_ical_events.selection.name import ComponentsWithName
from recurring_ical_events.series import Series

if TYPE_CHECKING:
    from icalendar.cal import Component

    from recurring_ical_events.adapters.component import ComponentAdapter


class AllKnownComponents(SelectComponents):
    """Group all known components into series."""

    @property
    def _component_adapters(self) -> Sequence[ComponentAdapter]:
        """Return all known component adapters."""
        return ComponentsWithName.component_adapters

    @property
    def names(self) -> list[str]:
        """Return the names of the components to collect."""
        result = [adapter.component_name() for adapter in self._component_adapters]
        result.sort()
        return result

    def __init__(
        self,
        series: type[Series] = Series,
        occurrence: type[Occurrence] = Occurrence,
        collector: type[ComponentsWithName] = ComponentsWithName,
    ) -> None:
        """Collect all known components and overide the series and occurrence.

        series - the Series class to override that is queried for Occurrences
        occurrence - the occurrence class that creates the resulting components
        collector - if you want to override the SelectComponentsByName class
        """
        self._series = series
        self._occurrence = occurrence
        self._collector = collector

    def collect_series_from(
        self, source: Component, suppress_errors: tuple[Exception]
    ) -> Sequence[Series]:
        """Collect the components from the source groups into a series."""
        result = []
        for name in self.names:
            collector = self._collector(
                name, series=self._series, occurrence=self._occurrence
            )
            result.extend(collector.collect_series_from(source, suppress_errors))
        return result


__all__ = ["AllKnownComponents"]

```

### `recurring_ical_events/selection/base.py`

```py
"""Base interface for selection of components."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from icalendar.cal import Component

    from recurring_ical_events.series import Series


class SelectComponents(ABC):
    """Abstract class to select components from a calendar."""

    @staticmethod
    def component_name():
        """The name of the component if there is only one."""
        raise NotImplementedError("This should be implemented in subclasses.")

    @abstractmethod
    def collect_series_from(
        self, source: Component, suppress_errors: tuple[Exception]
    ) -> Sequence[Series]:
        """Collect all components from the source grouped together into a series.

        suppress_errors - a list of errors that should be suppressed.
            A Series of events with such an error is removed from all results.
        """


__all__ = ["SelectComponents"]

```

### `recurring_ical_events/selection/name.py`

```py
"""Selecting components by name."""

from __future__ import annotations

import contextlib
from collections import defaultdict
from typing import TYPE_CHECKING, Sequence

from recurring_ical_events.adapters.event import EventAdapter
from recurring_ical_events.adapters.journal import JournalAdapter
from recurring_ical_events.adapters.todo import TodoAdapter
from recurring_ical_events.occurrence import Occurrence
from recurring_ical_events.selection.alarm import Alarms
from recurring_ical_events.selection.base import SelectComponents
from recurring_ical_events.series import Series
from recurring_ical_events.util import cached_property

if TYPE_CHECKING:
    from icalendar.cal import Component

    from recurring_ical_events.adapters.component import ComponentAdapter


class ComponentsWithName(SelectComponents):
    """This is a component collecttion strategy.

    Components can be collected in different ways.
    This class allows extension of the functionality by
    - subclassing to filter the resulting components
    - composition to combine collection behavior (see AllKnownComponents)
    """

    component_adapters: list[type[ComponentAdapter] | SelectComponents] = [
        EventAdapter,
        TodoAdapter,
        JournalAdapter,
        Alarms(),
    ]

    @cached_property
    def _component_adapters(self) -> dict[str : type[ComponentAdapter]]:
        """A mapping of component adapters."""
        return {
            adapter.component_name(): adapter for adapter in self.component_adapters
        }

    def __init__(
        self,
        name: str,
        adapter: type[ComponentAdapter] | None = None,
        series: type[Series] = Series,
        occurrence: type[Occurrence] = Occurrence,
    ) -> None:
        """Create a new way of collecting components.

        name - the name of the component to collect ("VEVENT", "VTODO", "VJOURNAL")
        adapter - the adapter to use for these components with that name
        series - the series class that hold a series of components
        occurrence - the occurrence class that creates the resulting components
        """
        if adapter is None:
            if name not in self._component_adapters:
                raise ValueError(
                    f'"{name}" is an unknown name for a '
                    "recurring component. "
                    f"I only know these: {', '.join(self._component_adapters)}."
                )
            adapter = self._component_adapters[name]
        if occurrence is not Occurrence:
            _occurrence = occurrence

            class series(series):  # noqa: N801
                occurrence = _occurrence

        self._name = name
        self._series = series
        self._adapter = adapter

    def collect_series_from(
        self, source: Component, suppress_errors: tuple[Exception]
    ) -> Sequence[Series]:
        """Collect all components from the source component.

        suppress_errors - a list of errors that should be suppressed.
            A Series of events with such an error is removed from all results.
        """
        if isinstance(self._adapter, SelectComponents):
            return self._adapter.collect_series_from(source, suppress_errors)
        components: dict[str, list[Component]] = defaultdict(list)  # UID -> components
        for component in source.walk(self._name):
            adapter = self._adapter(component)
            components[adapter.uid].append(adapter)
        result = []
        for components in components.values():
            with contextlib.suppress(suppress_errors):
                result.append(self._series(components))
        return result


__all__ = ["ComponentsWithName"]

```

### `recurring_ical_events/series/__init__.py`

```py
"""Calculation of occurrences in a series."""

from .alarm import (
    AbsoluteAlarmSeries,
    AlarmSeriesRelativeToEnd,
    AlarmSeriesRelativeToStart,
)
from .rrule import Series

__all__ = [
    "AbsoluteAlarmSeries",
    "AlarmSeriesRelativeToEnd",
    "AlarmSeriesRelativeToStart",
    "Series",
]

```

### `recurring_ical_events/series/alarm.py`

```py
"""Series calculation for alarms."""

import datetime
from collections import defaultdict
from typing import Generator

from dateutil.rrule import rruleset
from icalendar import Alarm

from recurring_ical_events.adapters.component import ComponentAdapter
from recurring_ical_events.occurrence import AlarmOccurrence, Occurrence
from recurring_ical_events.series.rrule import Series
from recurring_ical_events.types import Time
from recurring_ical_events.util import convert_to_datetime


class AbsoluteAlarmSeries:
    """A series of absolute alarms."""

    tzinfo = datetime.timezone.utc

    def __init__(self):
        """Create a new series of absolute alarms."""
        self.times = rruleset(cache=True)
        self.times2occurence: dict[datetime.datetime, list[Occurrence]] = defaultdict(
            list
        )

    def add(self, alarm: Alarm, parent: ComponentAdapter):
        """Add an absolute alarm with a parent component."""
        trigger = alarm.TRIGGER
        self._add(trigger, alarm, parent)
        for _ in range(alarm.REPEAT):
            trigger += alarm.DURATION
            self._add(trigger, alarm, parent)

    def _add(self, dt: datetime.datetime, alarm: Alarm, parent: ComponentAdapter):
        """Add an alarm at a specific time."""
        self.times.rdate(dt)
        self.times2occurence[dt].append(self.occurrence(dt, alarm, parent))

    def between(
        self, span_start: Time, span_stop: Time
    ) -> Generator[Occurrence, None, None]:
        """Components between the start (inclusive) and end (exclusive).

        The result does not need to be ordered.
        """
        span_start_dt = convert_to_datetime(span_start, self.tzinfo)
        span_stop_dt = convert_to_datetime(span_stop, self.tzinfo)
        for dt in self.times.between(span_start_dt, span_stop_dt, inc=True):
            for occurrence in self.times2occurence[dt]:
                if occurrence.is_in_span(span_start_dt, span_stop_dt):
                    yield occurrence

    def occurrence(
        self, dt: datetime.datetime, alarm: Alarm, parent: ComponentAdapter
    ) -> Occurrence:
        """Create a new occurrence."""
        return AlarmOccurrence(dt, alarm, parent)

    def is_empty(self) -> bool:
        """Whether this series is empty."""
        return not self.times2occurence


class AlarmSeriesRelativeToStart:
    """A series of alarms relative to the start of a component."""

    def __init__(self, alarm: Alarm, series: Series) -> None:
        """Create a series of alarms that are relative to the start of a series."""
        self._alarm = alarm
        self._series = series
        self._offsets: list[datetime.timedelta] = [alarm.TRIGGER]
        for _ in range(alarm.REPEAT):
            self._offsets.append(self._offsets[-1] + alarm.DURATION)

    def between(
        self, span_start: Time, span_stop: Time
    ) -> Generator[Occurrence, None, None]:
        """Components between the start (inclusive) and end (exclusive).

        The result does not need to be ordered.
        """
        # TODO: Reduce time span to reduce occurrences
        for offset in self._offsets:
            # If we are before the event start (negative offset),
            # we have to add the time span to request the event later.
            for parent in self._series.between(span_start - offset, span_stop - offset):
                if parent.has_alarm(self._alarm):
                    occurrence = self.occurrence(offset, self._alarm, parent)
                    if occurrence.is_in_span(span_start, span_stop):
                        yield occurrence

    def occurrence(
        self, offset: datetime.timedelta, alarm: Alarm, parent: Occurrence
    ) -> Occurrence:
        """Create a new occurrence."""
        return AlarmOccurrence(offset + parent.start, alarm, parent)

    def __repr__(self) -> str:
        """repr()"""
        return (
            f"<{self.__class__.__name__} "
            f"of {self._alarm} in {self._series} "
            f"with offsets {', '.join(map(str, self._offsets))}>"
        )


class AlarmSeriesRelativeToEnd(AlarmSeriesRelativeToStart):
    """A series of alarms relative to the start of a component."""

    def between(self, span_start, span_stop):
        """Components between the start (inclusive) and end (exclusive).

        The result does not need to be ordered.
        """
        # The end is exclusive. We must adjust the timespan to include it.
        return super().between(span_start - datetime.timedelta(seconds=1), span_stop)

    def occurrence(
        self, offset: datetime.timedelta, alarm: Alarm, parent: Occurrence
    ) -> Occurrence:
        """Create a new occurrence."""
        return AlarmOccurrence(offset + parent.end, alarm, parent)


__all__ = [
    "AbsoluteAlarmSeries",
    "AlarmSeriesRelativeToEnd",
    "AlarmSeriesRelativeToStart",
]

```

### `recurring_ical_events/series/rrule.py`

```py
"""Calculation of series based on rrule."""

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Generator, Sequence

from dateutil.rrule import rrule, rruleset, rrulestr
from icalendar.prop import vDDDTypes

from recurring_ical_events.constants import NEGATIVE_RRULE_COUNT_REGEX
from recurring_ical_events.errors import BadRuleStringFormat
from recurring_ical_events.occurrence import Occurrence
from recurring_ical_events.util import (
    compare_greater,
    convert_to_date,
    convert_to_date_range,
    convert_to_datetime,
    get_any,
    is_date,
    is_pytz,
    is_pytz_dt,
    normalize_pytz,
    to_recurrence_ids,
    with_highest_sequence,
)

if TYPE_CHECKING:
    from recurring_ical_events.adapters.component import ComponentAdapter
    from recurring_ical_events.types import RecurrenceID, Time


class Series:
    """Base class for components that result in a series of occurrences."""

    def occurrence(
        self,
        adapter: ComponentAdapter,
        start: Time | None = None,
        end: Time | None | datetime.timedelta = None,
    ) -> Occurrence:
        """A way to override the occurrence class."""
        return Occurrence(adapter, start, end, sequence=self.sequence)

    class NoRecurrence:
        """A strategy to deal with not having a core with rrules."""

        check_exdates_datetime: set[RecurrenceID] = set()
        check_exdates_date: set[datetime.date] = set()
        replace_ends: dict[RecurrenceID, Time] = {}
        sequence = -1

        def as_occurrence(
            self,
            start: Time,
            stop: Time,
            occurrence: type[Occurrence],
            core: ComponentAdapter,
        ) -> Occurrence:
            raise NotImplementedError("This code should never be reached.")

        @property
        def core(self) -> ComponentAdapter:
            raise NotImplementedError("This code should never be reached.")

        def rrule_between(
            self,
            span_start: Time,  # noqa: ARG002
            span_stop: Time,  # noqa: ARG002
        ) -> Generator[Time, None, None]:
            """No repetition."""
            yield from []

        has_core = False
        extend_query_span_by = (datetime.timedelta(0), datetime.timedelta(0))
        components = []

    class RecurrenceRules:
        """A strategy if we have an actual core with recurrences."""

        has_core = True

        @property
        def sequence(self) -> int:
            """The sequence of the code component."""
            return self.core.sequence

        def __init__(self, core: ComponentAdapter):
            self.core = core
            # Setup complete. We create the attribtues
            self.start = self.original_start = self.core.start
            self.end = self.original_end = self.core.end
            self.exdates: set[Time] = set()
            self.check_exdates_datetime: set[RecurrenceID] = set()  # should be in UTC
            self.check_exdates_date: set[datetime.date] = set()  # should be in UTC
            self.rdates: set[Time] = set()
            self.replace_ends: dict[
                RecurrenceID, datetime.timedelta
            ] = {}  # for periods, in UTC
            # fill the attributes
            for exdate in self.core.exdates:
                self.exdates.add(exdate)
                self.check_exdates_datetime.update(to_recurrence_ids(exdate))
                if is_date(exdate):
                    self.check_exdates_date.add(exdate)
            for rdate in self.core.rdates:
                if isinstance(rdate, tuple):
                    # we have a period as rdate
                    self.rdates.add(rdate[0])
                    for recurrence_id in to_recurrence_ids(rdate[0]):
                        self.replace_ends[recurrence_id] = (
                            rdate[1]
                            if isinstance(rdate[1], datetime.timedelta)
                            else rdate[1] - rdate[0]
                        )
                else:
                    # we have a date/datetime
                    self.rdates.add(rdate)

            # We make sure that all dates and times mentioned here are either:
            # - a date
            # - a datetime with None is tzinfo
            # - a datetime with a timezone
            self.make_all_dates_comparable()

            # Calculate the rules with the same timezones
            rule_set = rruleset(cache=True)
            rule_set.until = None
            self.rrules = [rule_set]
            last_until: Time | None = None
            for rrule_string in self.core.rrules:
                rule = self.create_rule_with_start(rrule_string)
                self.rrules.append(rule)
                if rule.until and (
                    not last_until or compare_greater(rule.until, last_until)
                ):
                    last_until = rule.until

            for exdate in self.exdates:
                self.check_exdates_datetime.add(exdate)
            for rdate in self.rdates:
                rule_set.rdate(rdate)

            if not last_until or not compare_greater(self.start, last_until):
                rule_set.rdate(self.start)

        @property
        def extend_query_span_by(self) -> tuple[datetime.timedelta, datetime.timedelta]:
            """The extension of the time span we need for this component's core."""
            return self.core.extend_query_span_by

        def create_rule_with_start(self, rule_string: str) -> rrule:
            """Helper to create an rrule from a rule_string

            The rrule is starting at the start of the component.
            Since the creation is a bit more complex,
            this function handles special cases.
            """
            try:
                return self.rrulestr(rule_string)
            except ValueError:
                # string: FREQ=WEEKLY;UNTIL=20191023;BYDAY=TH;WKST=SU
                # start: 2019-08-01 14:00:00+01:00
                # ValueError: RRULE UNTIL values must be specified in UTC
                # when DTSTART is timezone-aware
                rule_list = rule_string.split(";UNTIL=")
                if len(rule_list) != 2:
                    raise BadRuleStringFormat(
                        "UNTIL parameter is missing", rule_string
                    ) from None
                date_end_index = rule_list[1].find(";")
                if date_end_index == -1:
                    date_end_index = len(rule_list[1])
                until_string = rule_list[1][:date_end_index]
                if self.is_all_dates:
                    until_string = until_string[:8]
                elif self.tzinfo is None:
                    # remove the Z from the time zone
                    until_string = until_string[:-1]
                else:
                    # we assume the start is timezone aware but the until value
                    # is not, see the comment above
                    if len(until_string) == 8:
                        until_string += "T000000"
                    if len(until_string) != 15:
                        raise BadRuleStringFormat(
                            "UNTIL parameter has a bad format", rule_string
                        ) from None
                    until_string += "Z"  # https://stackoverflow.com/a/49991809
                new_rule_string = (
                    rule_list[0]
                    + rule_list[1][date_end_index:]
                    + ";UNTIL="
                    + until_string
                )
                return self.rrulestr(new_rule_string)

        def rrulestr(self, rule_string) -> rrule:
            """Return an rrulestr with a start. This might fail."""
            rule_string = NEGATIVE_RRULE_COUNT_REGEX.sub("", rule_string)  # Issue 128
            rule = rrulestr(rule_string, dtstart=self.start, cache=True)
            rule.string = rule_string
            rule.until = until = self._get_rrule_until(rule)
            if is_pytz(self.start.tzinfo) and rule.until:
                # when starting in a time zone that is one hour off to the end,
                # we might miss the last occurrence
                # see issue 107 and test/test_issue_107_omitting_last_event.py
                rule = rule.replace(until=rule.until + datetime.timedelta(hours=1))
                rule.until = until
            return rule

        def _get_rrule_until(self, rrule) -> None | Time:
            """Return the UNTIL datetime of the rrule or None if absent."""
            rule_list = rrule.string.split(";UNTIL=")
            if len(rule_list) == 1:
                return None
            if len(rule_list) != 2:
                raise BadRuleStringFormat("There should be only one UNTIL", rrule)
            date_end_index = rule_list[1].find(";")
            if date_end_index == -1:
                date_end_index = len(rule_list[1])
            until_string = rule_list[1][:date_end_index]
            return vDDDTypes.from_ical(until_string)

        def make_all_dates_comparable(self):
            """Make sure we can use all dates with eachother.

            Dates may be mixed and we have many of them.
            - date
            - datetime without timezone
            - datetime with timezone
            These three are not comparable but can be converted.
            """
            self.tzinfo = None
            dates = [self.start, self.end, *self.exdates, *self.rdates]
            self.is_all_dates = not any(
                isinstance(date, datetime.datetime) for date in dates
            )
            for date in dates:
                if isinstance(date, datetime.datetime) and date.tzinfo is not None:
                    self.tzinfo = date.tzinfo
                    break
            self.start = convert_to_datetime(self.start, self.tzinfo)

            self.end = convert_to_datetime(self.end, self.tzinfo)
            self.rdates = {
                convert_to_datetime(rdate, self.tzinfo) for rdate in self.rdates
            }
            self.exdates = {
                convert_to_datetime(exdate, self.tzinfo) for exdate in self.exdates
            }

        def rrule_between(self, span_start: Time, span_stop: Time) -> Generator[Time]:
            """Recalculate the rrules so that minor mistakes are corrected."""
            # make dates comparable, rrule converts them to datetimes
            span_start_dt = convert_to_datetime(span_start, self.tzinfo)
            span_stop_dt = convert_to_datetime(span_stop, self.tzinfo)
            # we have to account for pytz timezones not being properly calculated
            # at the timezone changes. This is a heuristic:
            #   most changes are only 1 hour.
            # This will still create problems at the fringes of
            #   timezone definition changes.
            if is_pytz(self.tzinfo):
                span_start_dt = normalize_pytz(
                    span_start_dt - datetime.timedelta(hours=1)
                )
                span_stop_dt = normalize_pytz(
                    span_stop_dt + datetime.timedelta(hours=1)
                )
            for rule in self.rrules:
                for start in rule.between(span_start_dt, span_stop_dt, inc=True):
                    if is_pytz_dt(start):
                        # update the time zone in case of summer/winter time change
                        start = start.tzinfo.localize(start.replace(tzinfo=None))  # noqa: PLW2901
                    # We could now well be out of bounce of the end of the UNTIL
                    # value. This is tested by test/test_issue_20_exdate_ignored.py.
                    if rule.until is None or not compare_greater(start, rule.until):
                        yield start

        def convert_to_original_type(self, date):
            """Convert a date back if this is possible.

            Dates may get converted to datetimes to make calculations possible.
            This reverts the process where possible so that Repetitions end
            up with the type (date/datetime) that was specified in the icalendar
            component.
            """
            if not isinstance(
                self.original_start, datetime.datetime
            ) and not isinstance(
                self.original_end,
                datetime.datetime,
            ):
                return convert_to_date(date)
            return date

        def as_occurrence(
            self,
            start: Time,
            stop: Time,
            occurrence: type[Occurrence],
            core: ComponentAdapter,
        ) -> Occurrence:
            """Return this as an occurrence at a specific time."""
            return occurrence(
                core,
                self.convert_to_original_type(start),
                self.convert_to_original_type(stop),
            )

        @property
        def components(self) -> list[ComponentAdapter]:
            """The components in this recurrence calculation."""
            return [self.core]

    def __init__(self, components: Sequence[ComponentAdapter]):
        """Create an component which may have repetitions in it."""
        if len(components) == 0:
            raise ValueError("No components given to calculate a series.")
        # We identify recurrences with a timestamp as all recurrence values
        # should be the same in UTC either way and we want to omit
        # inequality because of timezone implementation mismatches.
        self.recurrence_id_to_modification: dict[
            RecurrenceID, ComponentAdapter
        ] = {}  # RECURRENCE-ID -> adapter
        self.this_and_future = []
        self._uid = components[0].uid
        core: ComponentAdapter | None = None
        for component in components:
            if component.is_modification():
                recurrence_ids = component.recurrence_ids
                for recurrence_id in recurrence_ids:
                    self.recurrence_id_to_modification[recurrence_id] = (
                        with_highest_sequence(
                            self.recurrence_id_to_modification.get(recurrence_id),
                            component,
                        )
                    )
                if component.this_and_future:
                    self.this_and_future.append(recurrence_ids[0])
            else:
                core = with_highest_sequence(core, component)
        self.modifications: set[ComponentAdapter] = set(
            self.recurrence_id_to_modification.values()
        )
        del component
        self.recurrence = (
            self.NoRecurrence() if core is None else self.RecurrenceRules(core)
        )
        self.this_and_future.sort()
        self.sequence = max(component.sequence for component in self.components)
        self.compute_span_extension()

    def compute_span_extension(self):
        """Compute how much to extend the span for the rrule to cover all events."""
        self._subtract_from_start, self._add_to_stop = (
            self.recurrence.extend_query_span_by
        )
        for adapter in self.this_and_future_components:
            subtract_from_start, add_to_stop = adapter.extend_query_span_by
            self._subtract_from_start = max(
                subtract_from_start, self._subtract_from_start
            )
            self._add_to_stop = max(add_to_stop, self._add_to_stop)

    @property
    def components(self) -> list[ComponentAdapter]:
        """All the components in this sequence.

        Components with the same UID might not occur if the SEQUENCE
        number suggests that they are obsolete.
        """
        return self.recurrence.components + list(self.modifications)

    @property
    def this_and_future_components(self) -> Generator[ComponentAdapter]:
        """All components that influence future events."""
        if self.recurrence.has_core:
            yield self.recurrence.core
        for recurrence_id in self.this_and_future:
            yield self.recurrence_id_to_modification[recurrence_id]

    def get_component_for_recurrence_id(
        self, recurrence_id: RecurrenceID
    ) -> ComponentAdapter:
        """Get the component which contains all information for the recurrence id.

        This concerns this modifications that have RANGE=THISANDFUTURE set.
        """
        # We assume the the recurrence_id is of the correct timezone.
        component = self.recurrence.core
        for modification_id in self.this_and_future:
            if modification_id < recurrence_id:
                component = self.recurrence_id_to_modification[modification_id]
            else:
                break
        return component

    def rrule_between(self, span_start: Time, span_stop: Time) -> Generator[Time]:
        """Modify the rrule generation span and yield recurrences."""
        expanded_start = normalize_pytz(span_start - self._subtract_from_start)
        expanded_stop = normalize_pytz(span_stop + self._add_to_stop)
        yield from self.recurrence.rrule_between(
            expanded_start,
            expanded_stop,
        )

    def between(self, span_start: Time, span_stop: Time) -> Generator[Occurrence]:
        """Components between the start (inclusive) and end (exclusive).

        The result does not need to be ordered.
        """
        returned_starts: set[Time] = set()
        returned_modifications: set[ComponentAdapter] = set()
        # NOTE: If in the following line, we get an error, datetime and date
        # may still be mixed because RDATE, EXDATE, start and rule.
        for start in self.rrule_between(span_start, span_stop):
            recurrence_ids = to_recurrence_ids(start)
            if (
                start in returned_starts
                or convert_to_date(start) in self.recurrence.check_exdates_date
                or self.recurrence.check_exdates_datetime & set(recurrence_ids)
            ):
                continue
            adapter: ComponentAdapter = get_any(
                self.recurrence_id_to_modification, recurrence_ids, self.recurrence.core
            )
            if adapter is self.recurrence.core:
                # We have no modification for this recurrence, so we record the date
                returned_starts.add(start)
                # This component is the base for this occurrence.
                # It usually is the core. However, we may also find a modification
                # with RANGE=THISANDFUTURE.
                component = self.get_component_for_recurrence_id(recurrence_ids[0])
                occurrence_start = normalize_pytz(start + component.move_recurrences_by)
                # Consider the RDATE with a PERIOD value
                occurrence_end = normalize_pytz(
                    occurrence_start
                    + get_any(
                        self.recurrence.replace_ends,
                        recurrence_ids,
                        component.duration,
                    )
                )
                occurrence = self.recurrence.as_occurrence(
                    occurrence_start, occurrence_end, self.occurrence, component
                )
            else:
                # We found a modification, so we record the modification
                if adapter in returned_modifications:
                    continue
                returned_modifications.add(adapter)
                occurrence = self.occurrence(adapter)
            if occurrence.is_in_span(span_start, span_stop):
                yield occurrence
        for modification in self.modifications:
            # we assume that the modifications are actually included
            if (
                modification in returned_modifications
                or self.recurrence.check_exdates_datetime
                & set(modification.recurrence_ids)
                or self.skip_core_modification(modification)
            ):
                continue
            if modification.is_in_span(span_start, span_stop):
                returned_modifications.add(modification)
                yield self.occurrence(modification)

    def skip_core_modification(self, modification: ComponentAdapter) -> bool:
        """Wether to skip this occurrence.

        See Issues:
        - https://github.com/niccokunzmann/python-recurring-ical-events/issues/253
        - https://github.com/niccokunzmann/python-recurring-ical-events/issues/148
        - https://github.com/niccokunzmann/python-recurring-ical-events/issues/164
        """
        if modification.has_recurrence_rules() and modification.is_modification():
            if modification.sequence < self.recurrence.sequence:
                return self.has_recurrence_id_in_rrule(modification)
            return False
        return False

    def has_recurrence_id_in_rrule(self, modification: ComponentAdapter) -> bool:
        """Wether this occurrence ID is part of the RRULE."""
        modification_recurrence_ids = modification.recurrence_ids
        if not modification_recurrence_ids:
            return False
        span_start, span_stop = convert_to_date_range(modification_recurrence_ids[0])
        for start in self.rrule_between(span_start, span_stop):
            start_recurrence_ids = to_recurrence_ids(start)
            if (
                convert_to_date(start) in self.recurrence.check_exdates_date
                or self.recurrence.check_exdates_datetime & set(start_recurrence_ids)
            ):
                continue
            if set(start_recurrence_ids) & set(modification_recurrence_ids):
                return False
        return True

    @property
    def uid(self):
        """The UID that identifies this series."""
        return self._uid

    def __repr__(self):
        """A string representation."""
        return (
            f"<{self.__class__.__name__} uid={self.uid} "
            f"modifications:{len(self.recurrence_id_to_modification)}>"
        )


___all__ = ["Series"]

```

### `recurring_ical_events/test/__init__.py`

```py

```

### `recurring_ical_events/test/calendars/after_many_events_in_order.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20240330T161324Z
LAST-MODIFIED:20240330T161327Z
DTSTAMP:20240330T161327Z
UID:b23d11e6-a296-44a1-b51b-8ab651ec7d13
SUMMARY:event 1
DTSTART;TZID=Europe/London:20240326T010000
DTEND;TZID=Europe/London:20240330T070000
TRANSP:OPAQUE
X-MOZ-GENERATION:1
END:VEVENT
BEGIN:VEVENT
CREATED:20240330T161511Z
LAST-MODIFIED:20240330T161514Z
DTSTAMP:20240330T161514Z
UID:bcec4006-050a-43d2-9f81-4cc35f77a1d1
SUMMARY:event 4
DTSTART;TZID=Europe/London:20240327T040000
DTEND;TZID=Europe/London:20240328T160000
TRANSP:OPAQUE
X-MOZ-GENERATION:1
END:VEVENT
BEGIN:VEVENT
CREATED:20240330T161330Z
LAST-MODIFIED:20240330T161457Z
DTSTAMP:20240330T161457Z
UID:ba53fb81-aeac-42d4-9046-534f76653647
SUMMARY:event 2
RRULE:FREQ=DAILY;UNTIL=20240402T020000Z
EXDATE;TZID=Europe/London:20240328T030000
EXDATE;TZID=Europe/London:20240331T030000
EXDATE;TZID=Europe/London:20240330T030000
EXDATE;TZID=Europe/London:20240401T030000
EXDATE;TZID=Europe/London:20240402T030000
DTSTART;TZID=Europe/London:20240326T030000
DTEND;TZID=Europe/London:20240326T070000
TRANSP:OPAQUE
X-MOZ-GENERATION:9
SEQUENCE:6
END:VEVENT
BEGIN:VEVENT
CREATED:20240330T161421Z
LAST-MODIFIED:20240330T161430Z
DTSTAMP:20240330T161430Z
UID:ba53fb81-aeac-42d4-9046-534f76653647
SUMMARY:event 3
RECURRENCE-ID;TZID=Europe/London:20240327T030000
DTSTART;TZID=Europe/London:20240327T030000
DTEND;TZID=Europe/London:20240327T070000
TRANSP:OPAQUE
X-MOZ-GENERATION:9
SEQUENCE:6
END:VEVENT
BEGIN:VEVENT
CREATED:20240330T161430Z
LAST-MODIFIED:20240330T161457Z
DTSTAMP:20240330T161457Z
UID:ba53fb81-aeac-42d4-9046-534f76653647
SUMMARY:event 5
RECURRENCE-ID;TZID=Europe/London:20240329T030000
DTSTART;TZID=Europe/London:20240327T160000
DTEND;TZID=Europe/London:20240327T200000
TRANSP:OPAQUE
X-MOZ-GENERATION:9
SEQUENCE:7
END:VEVENT
BEGIN:VEVENT
CREATED:20240330T161524Z
LAST-MODIFIED:20240330T161610Z
DTSTAMP:20240330T161610Z
UID:49c1ccdb-5afa-4fed-a416-024070e97984
SUMMARY:event 6
RRULE:FREQ=DAILY;COUNT=2
DTSTART;VALUE=DATE:20240328
DTEND;VALUE=DATE:20240329
TRANSP:TRANSPARENT
SEQUENCE:1
X-MOZ-GENERATION:2
END:VEVENT
BEGIN:VEVENT
CREATED:20240330T161557Z
LAST-MODIFIED:20240330T161610Z
DTSTAMP:20240330T161610Z
UID:49c1ccdb-5afa-4fed-a416-024070e97984
SUMMARY:event 7
RECURRENCE-ID;VALUE=DATE:20240329
DTSTART;VALUE=DATE:20240329
DTEND;VALUE=DATE:20240330
TRANSP:TRANSPARENT
SEQUENCE:1
X-MOZ-GENERATION:2
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_1_week_before_event.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T120758Z
LAST-MODIFIED:20241002T120908Z
DTSTAMP:20241002T120908Z
UID:a26289e0-8739-488b-b706-77c9364193c1
SUMMARY:Event with an alarm 1 week before this starts
X-MOZ-LASTACK:20241002T120844Z
DTSTART;TZID=Europe/London:20241209T110000
DTEND;TZID=Europe/London:20241209T120000
TRANSP:OPAQUE
X-MOZ-GENERATION:4
DESCRIPTION:Event
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-P1W
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-P2D
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_15_min_before_event_snoozed.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T120758Z
LAST-MODIFIED:20241002T120908Z
DTSTAMP:20241002T120908Z
UID:a26289e0-8739-488b-b706-77c9364193c1
SUMMARY:event
X-MOZ-LASTACK:20241002T120844Z
DTSTART;TZID=Europe/London:20241002T110000
DTEND;TZID=Europe/London:20241002T120000
TRANSP:OPAQUE
X-MOZ-GENERATION:4
DESCRIPTION;ALTREP="data:text/html,alarm%2015%20minutes%20before%20snoozed"
 :alarm 15 minutes before snoozed
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT15M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_absolute_edited.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T121843Z
LAST-MODIFIED:20241002T121918Z
DTSTAMP:20241002T121918Z
UID:cd047c29-d904-47eb-bdba-ab7abafee025
SUMMARY:event
DTSTART;TZID=Europe/London:20241004T110000
DTEND;TZID=Europe/London:20241004T120000
TRANSP:OPAQUE
X-MOZ-GENERATION:2
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:20241003T130000Z
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
BEGIN:VEVENT
SEQUENCE:1
CREATED:20241002T121843Z
LAST-MODIFIED:20241002T121918Z
DTSTAMP:20241002T121918Z
UID:cd047c29-d904-47eb-bdba-ab7abafee025
SUMMARY:event
DTSTART;TZID=Europe/London:20241004T110000
DTEND;TZID=Europe/London:20241004T120000
TRANSP:OPAQUE
X-MOZ-GENERATION:2
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:20241004T130000Z
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_absolute_repeat.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T121843Z
LAST-MODIFIED:20241002T121918Z
DTSTAMP:20241002T121918Z
UID:cd047c29-d904-47eb-bdba-ab7abafee025
SUMMARY:event
DTSTART;TZID=Europe/London:20241004T110000
DTEND;TZID=Europe/London:20241004T120000
TRANSP:OPAQUE
X-MOZ-GENERATION:2
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:20241003T130000Z
REPEAT:2
DURATION:PT45M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_absolute.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T121843Z
LAST-MODIFIED:20241002T121918Z
DTSTAMP:20241002T121918Z
UID:cd047c29-d904-47eb-bdba-ab7abafee025
SUMMARY:event
DTSTART;TZID=Europe/London:20241004T110000
DTEND;TZID=Europe/London:20241004T120000
TRANSP:OPAQUE
X-MOZ-GENERATION:2
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:20241003T130000Z
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_around_event_boundaries.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T121351Z
LAST-MODIFIED:20241002T121603Z
DTSTAMP:20241002T121603Z
UID:592b9fba-c3a3-4d26-b91e-db7852e59f3e
SUMMARY:event with 4 alarms
DTSTART;TZID=Europe/London:20241004T110000
DTEND;TZID=Europe/London:20241004T114500
TRANSP:OPAQUE
X-MOZ-GENERATION:2
DESCRIPTION;ALTREP="data:text/html,15min%20before%20start%26amp%3Bend%3Cbr%
 3E15min%20after%20start%26amp%3Bend":15min before start&end\n15min after st
 art&end
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT15M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;RELATED=END:-PT15M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:PT15M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;RELATED=END:PT15M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_at_start_of_event.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:America/Los_Angeles
X-TZINFO:America/Los_Angeles[2024a]
BEGIN:STANDARD
TZOFFSETTO:-080000
TZOFFSETFROM:-075258
TZNAME:America/Los_Angeles(STD)
DTSTART:18831118T120702
RDATE:18831118T120702
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19180331T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19190330T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:-080000
TZOFFSETFROM:-070000
TZNAME:America/Los_Angeles(STD)
DTSTART:19181027T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19191026T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19420209T020000
RDATE:19420209T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:-080000
TZOFFSETFROM:-070000
TZNAME:America/Los_Angeles(STD)
DTSTART:19450930T020000
RDATE:19450930T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19480314T020100
RDATE:19480314T020100
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:-080000
TZOFFSETFROM:-070000
TZNAME:America/Los_Angeles(STD)
DTSTART:19490101T020000
RDATE:19490101T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:-080000
TZOFFSETFROM:-070000
TZNAME:America/Los_Angeles(STD)
DTSTART:19500924T020000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1SU;UNTIL=19610924T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19500430T010000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=-1SU;UNTIL=19660424T010000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19670430T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=-1SU;UNTIL=19730429T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19740106T020000
RDATE:19740106T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19750223T020000
RDATE:19750223T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19760425T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=-1SU;UNTIL=19860427T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:19870405T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=1SU;UNTIL=20060402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:-080000
TZOFFSETFROM:-070000
TZNAME:America/Los_Angeles(STD)
DTSTART:19621028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=20061029T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:America/Los_Angeles(DST)
DTSTART:20070311T020000
RDATE:20070311T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:-080000
TZOFFSETFROM:-070000
TZNAME:America/Los_Angeles(STD)
DTSTART:20071104T020000
RDATE:20071104T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:-070000
TZOFFSETFROM:-080000
TZNAME:(DST)
DTSTART:20080309T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:-080000
TZOFFSETFROM:-070000
TZNAME:(STD)
DTSTART:20081102T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T121035Z
LAST-MODIFIED:20241002T121131Z
DTSTAMP:20241002T121131Z
UID:a6b8cf4d-b7fa-4939-a039-003db08bf7a7
SUMMARY:event
DTSTART;TZID=America/Los_Angeles:20241004T030000
DTEND;TZID=America/Los_Angeles:20241004T040000
TRANSP:OPAQUE
X-MOZ-GENERATION:2
DESCRIPTION;ALTREP="data:text/html,alarm%20at%20start%20of%20event":alarm a
 t start of event
SEQUENCE:1
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:PT0S
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_of_repeated_event.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T121651Z
LAST-MODIFIED:20241002T121810Z
DTSTAMP:20241002T121810Z
UID:77646b28-edc7-4b4e-b396-9f2e64075baf
SUMMARY:repeated event
RRULE:FREQ=WEEKLY;UNTIL=20241106T100000Z
X-MOZ-LASTACK:20241002T121743Z
DTSTART;TZID=Europe/London:20241001T100000
DTEND;TZID=Europe/London:20241001T110000
TRANSP:OPAQUE
X-MOZ-GENERATION:4
SEQUENCE:1
DESCRIPTION;ALTREP="data:text/html,first%20alarm%20snoozed%20of%20repeated%
 20event":first alarm snoozed of repeated event
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-P1D
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_recurring_and_acknowledged_at_2024_11_27_16_27.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241127T162727Z
LAST-MODIFIED:20241127T162755Z
DTSTAMP:20241127T162755Z
UID:b17e7979-ecef-4aa1-9ec7-e0d2c3891fbe
SUMMARY:recurring event with alarm
RRULE:FREQ=DAILY;UNTIL=20241130T140000Z
X-MOZ-LASTACK:20241127T162755Z
DTSTART;TZID=Europe/London:20241126T140000
DTEND;TZID=Europe/London:20241126T150000
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:1
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT1H
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_removed_and_moved.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241216T080857Z
LAST-MODIFIED:20241218T215721Z
DTSTAMP:20241218T215721Z
UID:ee30acc4-b8c8-4bc2-affb-ff1e971e4fd9
SUMMARY:event with alarm
RRULE:FREQ=DAILY;UNTIL=20241223T090000Z
X-MOZ-LASTACK:20241218T215721Z
DTSTART;TZID=Europe/London:20241218T090000
DTEND;TZID=Europe/London:20241218T100000
TRANSP:OPAQUE
X-MOZ-GENERATION:8
SEQUENCE:2
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT1H
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
BEGIN:VEVENT
CREATED:20241216T080948Z
LAST-MODIFIED:20241216T080953Z
DTSTAMP:20241216T080953Z
UID:ee30acc4-b8c8-4bc2-affb-ff1e971e4fd9
SUMMARY:event with alarm
RECURRENCE-ID;TZID=Europe/London:20241219T090000
DTSTART;TZID=Europe/London:20241219T120000
DTEND;TZID=Europe/London:20241219T130000
TRANSP:OPAQUE
X-MOZ-GENERATION:7
SEQUENCE:3
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT1H
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
BEGIN:VEVENT
CREATED:20241216T080953Z
LAST-MODIFIED:20241216T081425Z
DTSTAMP:20241216T081425Z
UID:ee30acc4-b8c8-4bc2-affb-ff1e971e4fd9
SUMMARY:event without alarm
RECURRENCE-ID;TZID=Europe/London:20241221T090000
DTSTART;TZID=Europe/London:20241221T090000
DTEND;TZID=Europe/London:20241221T100000
TRANSP:OPAQUE
X-MOZ-GENERATION:7
SEQUENCE:2
END:VEVENT
BEGIN:VEVENT
CREATED:20241216T081011Z
LAST-MODIFIED:20241216T081411Z
DTSTAMP:20241216T081411Z
UID:ee30acc4-b8c8-4bc2-affb-ff1e971e4fd9
SUMMARY:event with alarm 30 min before
RECURRENCE-ID;TZID=Europe/London:20241222T090000
DTSTART;TZID=Europe/London:20241222T090000
DTEND;TZID=Europe/London:20241222T100000
TRANSP:OPAQUE
X-MOZ-GENERATION:7
SEQUENCE:2
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT30M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
BEGIN:VTODO
CREATED:20241216T084041Z
LAST-MODIFIED:20241216T084333Z
DTSTAMP:20241216T084333Z
UID:2e8666fe-a370-4c2c-acfb-b0352a1ebae2
SUMMARY:todo with alarm after end
X-MOZ-LASTACK:20241216T084333Z
DUE;TZID=Europe/London:20231216T090000
PERCENT-COMPLETE:0
X-MOZ-GENERATION:3
SEQUENCE:1
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;RELATED=END:PT1H
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VTODO
BEGIN:VTODO
CREATED:20241216T084116Z
LAST-MODIFIED:20241218T221059Z
DTSTAMP:20241218T221059Z
UID:8f9e0f14-a130-4270-88b1-045c5cd799a2
SUMMARY:todo with alarm absolute 18:00
DUE;TZID=Europe/London:20231116T090000
PERCENT-COMPLETE:0
X-MOZ-GENERATION:4
SEQUENCE:1
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:20231213T180000Z
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VTODO
BEGIN:VTODO
CREATED:20241216T083919Z
LAST-MODIFIED:20241218T215542Z
DTSTAMP:20241218T215542Z
UID:efc08fc4-c843-4ce0-b02b-c4fd0a2b42b6
SUMMARY:todo with alarm
RRULE:FREQ=DAILY;UNTIL=20231223T090000Z
X-MOZ-LASTACK:20241216T083953Z
DTSTART;TZID=Europe/London:20231217T090000
PERCENT-COMPLETE:0
X-MOZ-GENERATION:4
SEQUENCE:3
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT1H
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VTODO
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarm_several_in_one.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241219T221254Z
LAST-MODIFIED:20241219T221358Z
DTSTAMP:20241219T221358Z
UID:2f1c5db0-6491-4fe4-bcaf-c8f83533ba93
SUMMARY:several alarms
DTSTART;TZID=Europe/London:20241220T130000
DTEND;TZID=Europe/London:20241220T140000
TRANSP:OPAQUE
X-MOZ-GENERATION:1
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT15M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT1H
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:PT15M
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:PT1H
DESCRIPTION:Mozilla Standardbeschreibung
DURATION:PT1H
REPEAT:2
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarms_at_the_same_time.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241219T222953Z
LAST-MODIFIED:20241219T223757Z
DTSTAMP:20241219T223757Z
UID:090ed38a-b759-4acd-b45e-6977c60e1271
SUMMARY:event with alarm at the same time
RRULE:FREQ=DAILY;UNTIL=20241222T130000Z
DTSTART;TZID=Europe/London:20241220T130000
DTEND;TZID=Europe/London:20241220T140000
TRANSP:OPAQUE
X-MOZ-GENERATION:15
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
CREATED:20241219T223025Z
LAST-MODIFIED:20241219T223208Z
DTSTAMP:20241219T223208Z
UID:090ed38a-b759-4acd-b45e-6977c60e1271
SUMMARY:event with alarm at the same time 1
RECURRENCE-ID;TZID=Europe/London:20241220T130000
DTSTART;TZID=Europe/London:20241220T130000
DTEND;TZID=Europe/London:20241220T140000
TRANSP:OPAQUE
X-MOZ-GENERATION:15
SEQUENCE:1
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT1H
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
BEGIN:VEVENT
CREATED:20241219T223208Z
LAST-MODIFIED:20241219T223547Z
DTSTAMP:20241219T223547Z
UID:090ed38a-b759-4acd-b45e-6977c60e1271
SUMMARY:event with alarm at the same time 2
RECURRENCE-ID;TZID=Europe/London:20241221T130000
DTSTART;TZID=Europe/London:20241221T120000
DTEND;TZID=Europe/London:20241221T130000
TRANSP:OPAQUE
X-MOZ-GENERATION:15
SEQUENCE:2
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-P1D
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
BEGIN:VEVENT
CREATED:20241219T223254Z
LAST-MODIFIED:20241219T223757Z
DTSTAMP:20241219T223757Z
UID:090ed38a-b759-4acd-b45e-6977c60e1271
SUMMARY:event with alarm at the same time 3
RECURRENCE-ID;TZID=Europe/London:20241222T130000
DTSTART;TZID=Europe/London:20241222T130000
DTEND;TZID=Europe/London:20241222T140000
TRANSP:OPAQUE
X-MOZ-GENERATION:15
SEQUENCE:4
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:20241220T230000Z
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-P2DT1H
DESCRIPTION:Mozilla Standardbeschreibung
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/alarms_different_in_same_event.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241220T090844Z
LAST-MODIFIED:20241220T091243Z
DTSTAMP:20241220T091243Z
UID:3e2471e6-af53-4ee5-bf64-fed13a01a61a
SUMMARY:Event with different alarms at the same time
RRULE:FREQ=DAILY;UNTIL=20241222T130000Z
DTSTART;TZID=Europe/London:20241220T130000
DTEND;TZID=Europe/London:20241220T150000
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:1
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT1H
DESCRIPTION:Alarm 1
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;RELATED=END:-PT3H
DESCRIPTION:Alarm 2
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT1H
DESCRIPTION:Alarm 3
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:20241220T120000Z
DESCRIPTION:Alarm 4
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/bad_rrule_missing_until_event.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
SUMMARY:blabla
DTSTART;TZID=Europe/London:20190801T140000
DTEND;TZID=Europe/London:20190801T150000
DTSTAMP:20190801T083416Z
UID:blabla
SEQUENCE:0
RRULE:FREQ=WEEKLY;UNTL=20191023;BYDAY=TH;WKST=SU
CREATED:20190729T105342Z
DESCRIPTION:blabla
LAST-MODIFIED:20190801T064315Z
LOCATION:
STATUS:CONFIRMED
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/date_exclude.txt`

```txt
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//PYVOBJECT//NONSGML Version 1//EN
BEGIN:VEVENT
UID:d9b8ba07-1d4a-40ec-bdb5-c4f538d261af
DTSTART:20231215T060000Z
DTEND:20231215T070000Z
CATEGORIES:Kategorie
CLASS:PUBLIC
CREATED:20231215T070936Z
DESCRIPTION:La concha de su madre
DTSTAMP:20231215T154916Z
EXDATE;VALUE=DATE:20231216
LAST-MODIFIED:20231215T154916Z
RRULE:FREQ=DAILY;UNTIL=20231218T023000Z;FREQ=DAILY
SEQUENCE:35
SUMMARY:Tag ausgeschlossen
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/daylight_saving_time.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:machBar - Öffentlich
X-WR-TIMEZONE:Europe/Berlin
X-WR-CALDESC:Alle öffentlichen Termine der Potsdamer machBar dem fabLab vom
  Wissenschaftsladen Potsdam e.V.
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTART:20190228T190000Z
DTEND:20190228T200000Z
DTSTAMP:20190304T172911Z
UID:4pudsugalsbuqetcfdns8demti@google.com
CREATED:20190226T145646Z
DESCRIPTION:Kennenlernen der machBar facilities zum Thema Bioökonomie
LAST-MODIFIED:20190226T145646Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:"Bioökonomie-Tag"
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190304T140000
DTEND;TZID=Europe/Berlin:20190304T180000
RRULE:FREQ=WEEKLY;WKST=SU;COUNT=6;BYDAY=MO,TU,WE
DTSTAMP:20190304T172911Z
UID:37jkbgv9regint2hqhlmd9risn@google.com
CREATED:20190226T140104Z
DESCRIPTION:
LAST-MODIFIED:20190226T140529Z
LOCATION:
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:Open Health HACKademy - freie Termine
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20190309T083000Z
DTEND:20190310T160000Z
DTSTAMP:20190304T172911Z
UID:3po7fj93mq7keq9qgqcckcm6la@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CREATED:20190226T135643Z
DESCRIPTION:In machBar und offenem Atelier\nhttps://be-able.info/de/projekt
 e/HACKademy/
LAST-MODIFIED:20190226T140317Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Open Health HACKademy
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190228T083000
DTEND;TZID=Europe/Berlin:20190228T143000
RRULE:FREQ=WEEKLY;BYDAY=TH
EXDATE;TZID=Europe/Berlin:20190307T083000
DTSTAMP:20190304T172911Z
UID:7g6502aejkun96i5fenfu6hvc1@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CREATED:20190226T134933Z
DESCRIPTION:Mario mit einer Klasse der Montessori Schule
LAST-MODIFIED:20190226T140308Z
LOCATION:machBar
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Montessori Schulklasse
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190301T083000
DTEND;TZID=Europe/Berlin:20190301T143000
RRULE:FREQ=WEEKLY;BYDAY=FR
EXDATE;TZID=Europe/Berlin:20190308T083000
DTSTAMP:20190304T172911Z
UID:1djkkpk5edlt8ocfscsd8a52et@google.com
CREATED:20190226T134824Z
DESCRIPTION:Mario mit einer Kasse der Montessori Schule
LAST-MODIFIED:20190226T140257Z
LOCATION:machBar
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:Montessori Schulklasse
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20190316T083000Z
DTEND:20190317T180000Z
DTSTAMP:20190304T172911Z
UID:0d9qpsgmsglque6b3tfquqo805@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CREATED:20190226T135810Z
DESCRIPTION:In machBar und Offenem Atelier\nhttps://be-able.info/de/projekt
 e/HACKademy/
LAST-MODIFIED:20190226T140220Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Open Health HACKademy
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20190301T163000Z
DTEND:20190303T170000Z
DTSTAMP:20190304T172911Z
UID:5v18ih724kes1sf1eeu27dsq5n@google.com
CREATED:20190226T135342Z
DESCRIPTION:HACKademy in machBar und offenem Atelier\nhttps://be-able.info/
 de/projekte/HACKademy/
LAST-MODIFIED:20190226T135342Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Open Health HACKademy
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20190228T140000Z
DTEND:20190228T170000Z
DTSTAMP:20190304T172911Z
UID:4mm2ak3in2j3pllqdk1ubtbp9p@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CREATED:20190226T134810Z
DESCRIPTION:\nWorkshop: Hemp as a sustainable material in a bio-based socie
 ty\n-closed workshop-\nyou can join us afterwards from 18:30 to 21:00 @open
 Lab- machBar Potsdam
LAST-MODIFIED:20190226T135130Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Workshop DiReBio
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190213T190000
DTEND;TZID=Europe/Berlin:20190213T210000
RRULE:FREQ=WEEKLY;BYDAY=WE
DTSTAMP:20190304T172911Z
UID:7uartkcnhf0elbvs8md0itrf6c@google.com
CREATED:20180430T161057Z
DESCRIPTION:Alle Lebensformen die sich den Werten und Inhalten der Hackeret
 hik und der Galaktischen Gemeinschaft verbunden fühlen sind eingeladen zum 
 Chaostreff! <br>Von Comics\, Code bis Netzpolitik und Datensparsamkeit steh
 en verschiedenste Themen im Fokus.<br>Hackt mit!<br><br><a href="http://www
 .ccc-p.org" target="_blank" id="ow314" __is_owner="true">www.ccc-p.org</a>
LAST-MODIFIED:20190212T124850Z
LOCATION:
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Chaostreff - CCCP
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190116T190000
DTEND;TZID=Europe/Berlin:20190116T210000
RRULE:FREQ=WEEKLY;UNTIL=20190212T225959Z;INTERVAL=2;BYDAY=WE
DTSTAMP:20190304T172911Z
UID:4m856r43sj4i6g0vat9dn4gtui_R20190116T180000@google.com
CREATED:20180430T161057Z
DESCRIPTION:Alle Lebensformen die sich den Werten und Inhalten der Hackeret
 hik und der Galaktischen Gemeinschaft verbunden fühlen sind eingeladen zum 
 Chaostreff! <br>Von Comics\, Code bis Netzpolitik und Datensparsamkeit steh
 en verschiedenste Themen im Fokus.<br>Hackt mit!<br><br><a href="http://www
 .ccc-p.de" id="ow328" __is_owner="true">www.ccc-p.de</a>
LAST-MODIFIED:20190212T124850Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Chaostreff - CCCP
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180425T190000
DTEND;TZID=Europe/Berlin:20180425T210000
RRULE:FREQ=WEEKLY;UNTIL=20190115T225959Z;INTERVAL=2;BYDAY=WE
DTSTAMP:20190304T172911Z
UID:4m856r43sj4i6g0vat9dn4gtui@google.com
CREATED:20180430T161057Z
DESCRIPTION:Alle Lebensformen die sich den Werten und Inhalten der Hackeret
 hik und der Galaktischen Gemeinschaft verbunden fühlen sind eingeladen zum 
 Chaostreff! \nVon Comics\, Code bis Netzpolitik und Datensparsamkeit stehen
  verschiedenste Themen im Fokus.\nHackt mit!\n\nhttp://chaostreff-potsdam.g
 ithub.io
LAST-MODIFIED:20190212T124850Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Chaostreff
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180212T150000
DTEND;TZID=Europe/Berlin:20180212T180000
RRULE:FREQ=WEEKLY;UNTIL=20180729T215959Z;BYDAY=MO
DTSTAMP:20190304T172911Z
UID:3gp01pk48e95mmonkqef47qtpb_R20180212T140000@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:#tec (Hashtec) ist ein Jugendlab\, welches Neugier auf Wissen u
 nd die Makerszene für sich schafft und weiter entwickelt und probiert.
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#TEC - Jugendlab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180115T150000
DTEND;TZID=Europe/Berlin:20180115T180000
RRULE:FREQ=WEEKLY;UNTIL=20180211T225959Z;BYDAY=MO
DTSTAMP:20190304T172911Z
UID:3gp01pk48e95mmonkqef47qtpb@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:#tec (Hashtec) ist ein Jugendlab\, welches Neugier auf Wissen u
 nd die Makerszene für sich schafft und weiter entwickelt und probiert.
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#tec - Jugendlab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190117T150000
DTEND;TZID=Europe/Berlin:20190117T170000
RRULE:FREQ=WEEKLY;BYDAY=TH
DTSTAMP:20190304T172911Z
UID:ctfr0ikn17n8okmi83au0qfuhs@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:\nJetzt neu immer Donnerstags!\n#tec (Hashtec) ist ein Treffpun
 kt für Jugendliche\, welche sich kreativ mit Technik beschäftigen wollen. G
 emeinsam hacken\, programmieren lernen und Spaß haben steht an erster Stell
 e. \n\nIhr braucht keine Clubmitgliedschaft und es ist kostenfrei. Kommt vo
 rbei!\n\nhttps://hashtec-potsdam.github.io/
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:#TEC - für Jugendliche
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180910T150000
DTEND;TZID=Europe/Berlin:20180910T170000
RRULE:FREQ=WEEKLY;UNTIL=20190113T225959Z;BYDAY=MO
DTSTAMP:20190304T172911Z
UID:3gp01pk48e95mmonkqef47qtpb_R20180910T130000@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:#tec (Hashtec) ist ein Treffpunkt für Jugendliche\, welche sich
  mit Technik kreativ beschäftigen wollen. Gemeinsam hacken und Spaß haben s
 teht an erster Stelle. \n\nWir erheben keine Clubmitgliedschaften und sind 
 kostenfrei.\n\nhttps://hashtec-potsdam.github.io/
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#TEC - für Jugendliche
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180730T150000
DTEND;TZID=Europe/Berlin:20180730T170000
RRULE:FREQ=WEEKLY;UNTIL=20180909T215959Z;BYDAY=MO
DTSTAMP:20190304T172911Z
UID:3gp01pk48e95mmonkqef47qtpb_R20180730T130000@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:#tec (Hashtec) ist ein Jugendlab\, welches Neugier auf Wissen u
 nd die Makerszene für sich schafft und weiter entwickelt und probiert.\n\nh
 ttps://hashtec-potsdam.github.io/
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#TEC - Fällt aus bis September
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190622T110000
DTEND;TZID=Europe/Berlin:20190622T150000
RRULE:FREQ=DAILY;COUNT=1
DTSTAMP:20190304T172911Z
UID:4oe7e40bbf492tbp6eilvg9naj@google.com
CREATED:20181108T044402Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044402Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190525T110000
DTEND;TZID=Europe/Berlin:20190525T150000
RRULE:FREQ=DAILY;COUNT=1
DTSTAMP:20190304T172911Z
UID:1p5ldilgr9dtls02s3k196pbnl@google.com
CREATED:20181108T044347Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044347Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190427T110000
DTEND;TZID=Europe/Berlin:20190427T150000
RRULE:FREQ=DAILY;COUNT=1
DTSTAMP:20190304T172911Z
UID:4h75rere9lgo3atvkc810587jp@google.com
CREATED:20181108T044331Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044331Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190323T110000
DTEND;TZID=Europe/Berlin:20190323T150000
RRULE:FREQ=DAILY;COUNT=1
DTSTAMP:20190304T172911Z
UID:3r2hi43bkab7h35rb13eu3t6b6@google.com
CREATED:20181108T044307Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044307Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190224T110000
DTEND;TZID=Europe/Berlin:20190224T150000
DTSTAMP:20190304T172911Z
UID:ome5r9735mpdoo3n6lpf8oi0c4@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20190216T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044241Z
LOCATION:Treffpunkt Freizeit\, Am Neuen Garten 64\, 14469 Potsdam\, Deutsch
 land
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190127T110000
DTEND;TZID=Europe/Berlin:20190127T150000
DTSTAMP:20190304T172911Z
UID:ome5r9735mpdoo3n6lpf8oi0c4@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20190119T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044241Z
LOCATION:Treffpunkt Freizeit\, Am Neuen Garten 64\, 14469 Potsdam\, Deutsch
 land
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20181208T110000
DTEND;TZID=Europe/Berlin:20181208T150000
DTSTAMP:20190304T172911Z
UID:ome5r9735mpdoo3n6lpf8oi0c4@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20181215T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044241Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20181117T110000
DTEND;TZID=Europe/Berlin:20181117T150000
RRULE:FREQ=MONTHLY;UNTIL=20190315T225959Z;BYDAY=3SA
DTSTAMP:20190304T172911Z
UID:ome5r9735mpdoo3n6lpf8oi0c4@google.com
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044241Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190112T110000
DTEND;TZID=Europe/Berlin:20190112T150000
RRULE:FREQ=MONTHLY;UNTIL=20190308T225959Z;BYDAY=2SA
DTSTAMP:20190304T172911Z
UID:3761q5bsqtnh74ckejfgfrailt@google.com
CREATED:20181108T043904Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044217Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20170912T180000
DTEND;TZID=Europe/Berlin:20170912T210000
RRULE:FREQ=WEEKLY;UNTIL=20181008T215959Z;INTERVAL=2;BYDAY=TU
EXDATE;TZID=Europe/Berlin:20171121T180000
DTSTAMP:20190304T172911Z
UID:5m2ic2qqn1fo43ebfp7ucovj6p@google.com
CLASS:PUBLIC
CREATED:20170908T082339Z
DESCRIPTION:Öffentliches Treffen des Freifunk Potsdam e.V.\n
LAST-MODIFIED:20180925T164518Z
LOCATION:Seminarraum
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Freifunktreffen
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20181020T110000
DTEND;TZID=Europe/Berlin:20181020T150000
DTSTAMP:20190304T172911Z
UID:52uuaoruefesorque1gpjabr6t@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20181027T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20180607T182041Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180922T110000
DTEND;TZID=Europe/Berlin:20180922T150000
DTSTAMP:20190304T172911Z
UID:52uuaoruefesorque1gpjabr6t@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20180929T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20180607T182041Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180630T110000
DTEND;TZID=Europe/Berlin:20180630T150000
RRULE:FREQ=MONTHLY;UNTIL=20181123T225959Z;BYDAY=-1SA
EXDATE;TZID=Europe/Berlin:20180825T110000
EXDATE;TZID=Europe/Berlin:20180728T110000
DTSTAMP:20190304T172911Z
UID:52uuaoruefesorque1gpjabr6t@google.com
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20180607T182041Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20180526
DTEND;VALUE=DATE:20180528
DTSTAMP:20190304T172911Z
UID:05b6u5vfdih0cdr6q3msgemss2@google.com
CREATED:20180503T161745Z
DESCRIPTION:Das mobile Fablab auf der Maker Fair.
LAST-MODIFIED:20180503T161745Z
LOCATION:FEZ-Berlin\, Str. zum FEZ 2\, 12459 Berlin\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB - OnTour: Maker Fair
TRANSP:TRANSPARENT
END:VEVENT
BEGIN:VEVENT
DTSTART:20180530T070000Z
DTEND:20180530T100000Z
DTSTAMP:20190304T172911Z
UID:4ajj1k6g3vbq38rrbfe653nge4@google.com
CREATED:20180503T161414Z
DESCRIPTION:Hauptziel des Projektes FABULANDLABS ist es\, dass Betroffene s
 ich ihre Hilfsmittel mit Kostengünstigen Technologien in offen zugänglichen
  Werkstätten - sogenannten FabLabs- selbst anpassen oder herstellen.
LAST-MODIFIED:20180503T161414Z
LOCATION:Seminarrraum Haus 5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Fabulandlabs Ideen Workshop
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20181014T080000Z
DTEND:20181014T160000Z
DTSTAMP:20190304T172911Z
UID:3akehbu0brcbrno9njieufcan4@google.com
CREATED:20180430T163433Z
DESCRIPTION:Angebot im Rahmen des Eltern Medien Tag von der Medienwerkstatt
LAST-MODIFIED:20180430T163433Z
LOCATION:Treffpunkt Freizeit\, Am Neuen Garten 64\, 14469 Potsdam\, Germany
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:EXTERN: Eltern Medien Tag 
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180502T190000
DTEND;TZID=Europe/Berlin:20180502T210000
DTSTAMP:20190304T172911Z
UID:2o60r26f5pq7muep7htdi4r01n@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20180501T190000
CLASS:PUBLIC
CREATED:20171126T091145Z
DESCRIPTION:Treffen der offenen OK Lab Gruppe. Informationen auf&nbsp\;<a h
 ref="https://www.google.com/url?q=http%3A%2F%2Fwww.oklab-potsdam.de&amp\;sa
 =D&amp\;usd=2&amp\;usg=AFQjCNH4ia7HdoVhwjLJiSfSMu46bTzIxA" target="_blank">
 www.oklab-potsdam.de</a><br>Themen sind: Open Data\, Civic Tech\, Programmi
 erung<br>
LAST-MODIFIED:20180423T073355Z
LOCATION:machBar Seminarraum
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:OK Lab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180411T170000Z
DTEND:20180411T190000Z
DTSTAMP:20190304T172911Z
UID:54e37ogvp0u4bcsssmr6nvklur@google.com
CREATED:20180321T073604Z
DESCRIPTION:Erstes Chaostreff in Potsdam in der machBar. \n\nWird es einen 
 neuen Erfa geben?
LAST-MODIFIED:20180323T140809Z
LOCATION:Seminarraum
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Chaostreff
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180418T160000Z
DTEND:20180418T190000Z
DTSTAMP:20190304T172911Z
UID:5it6in3t9a6bkm6sra1ei44hcd@google.com
CREATED:20180323T140717Z
DESCRIPTION:Treffen der Potsdamer Bienenmenschen.
LAST-MODIFIED:20180323T140748Z
LOCATION:Seminarraum
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Imkertreffen
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20181007T110000Z
DTEND:20181007T150000Z
DTSTAMP:20190304T172911Z
UID:7gubjda7233nr0aic7nau87ojq@google.com
CREATED:20180321T074052Z
DESCRIPTION:Reparieren\, modifizieren oder erweitern mit der machBar auf de
 m Solimarkt im freiLand
LAST-MODIFIED:20180321T074052Z
LOCATION:Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar@Solimarkt
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180909T110000Z
DTEND:20180909T150000Z
DTSTAMP:20190304T172911Z
UID:5tatrcit8g1mhaal5aecr07muo@google.com
CREATED:20180321T074031Z
DESCRIPTION:Reparieren\, modifizieren oder erweitern mit der machBar auf de
 m Solimarkt im freiLand
LAST-MODIFIED:20180321T074032Z
LOCATION:Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar@Solimarkt
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180624T110000Z
DTEND:20180624T150000Z
DTSTAMP:20190304T172911Z
UID:34umj4pa5g3ubmgpg84l57op7t@google.com
CREATED:20180321T074006Z
DESCRIPTION:Reparieren\, modifizieren oder erweitern mit der machBar auf de
 m Solimarkt im freiLand
LAST-MODIFIED:20180321T074006Z
LOCATION:Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar@Solimarkt
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180415T110000Z
DTEND:20180415T150000Z
DTSTAMP:20190304T172911Z
UID:17uhb8mltk8akncompll76d47l@google.com
CREATED:20180321T073935Z
DESCRIPTION:Reparieren\, modifizieren oder erweitern mit der machBar auf de
 m Solimarkt im freiLand
LAST-MODIFIED:20180321T073935Z
LOCATION:Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar@Solimarkt
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180317T130000Z
DTEND:20180317T170000Z
DTSTAMP:20190304T172911Z
UID:55btcmdmcp3iicf65tdjfmpaj1@google.com
CLASS:PUBLIC
CREATED:20180220T070337Z
DESCRIPTION:<span>Interessierte Kopterpiloten und Leute dies es werden woll
 en. Kommt zum 2.Koptertreffen in der Potsdamer "Machbar".<br> Neben dem Erf
 ahrungsaustausch haben wir Platz zum Fachsimpeln\, reparieren\, Getränke tr
 inken und fliegen. Auch stehen die Maschinen des Wissenschaftsladen Potsdam
  zur Verfügung<br> (3D Drucker\, CNC-Fräser\, Lasercutter\, Lötstationen)</
 span>
LAST-MODIFIED:20180220T070337Z
LOCATION:freiLand Potsdam Haus 5\, Friedrich-Engels-Straße 22\, 14473 Potsd
 am\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:2.Koptertreffen 2018
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180217T120000Z
DTEND:20180217T170000Z
DTSTAMP:20190304T172911Z
UID:08g4pq8igtt7itfud1giriscp2@google.com
CREATED:20180201T054523Z
DESCRIPTION:Haus 5\nAm Boden bleiben war gestern.
LAST-MODIFIED:20180215T191735Z
LOCATION:freiLand Potsdam\, Friedrich-Engels-Straße 22\, 14473 Potsdam\, De
 utschland
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:1. Koptertreffen 2018
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180221T190000Z
DTEND:20180221T210000Z
DTSTAMP:20190304T172911Z
UID:6lp9jql7gkfd848f1sglpe7qei@google.com
CLASS:PUBLIC
CREATED:20180215T113957Z
DESCRIPTION:Potsdamer Jungimker treffen sich zum Austausch von aktuellen En
 twicklungen in der Bienenhaltung\, Erfahrungen zu Betriebsweisen\, saisonal
 en Maßnahmen\, technischer Umsetzung von Monitoring-Lösungen für Bienenbeut
 en sowie Herstellung von Bienenbehausungen und Restaurierung von älteren im
 kerlichen Gerätschaften.
LAST-MODIFIED:20180215T155232Z
LOCATION:freiLand Potsdam Haus 5\, Friedrich-Engels-Straße 22\, 14473 Potsd
 am\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Jungimker-Treffen
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180209T090000Z
DTEND:20180209T150000Z
DTSTAMP:20190304T172911Z
UID:0k3eu4imuol19pn1160lb7fnf2@google.com
CREATED:20180131T072126Z
DESCRIPTION:Workshop für die partizipative Prototypenentwicklung für Mensch
 en mit besonderen Bedürfnissen
LAST-MODIFIED:20180131T072254Z
LOCATION:freiLand Potsdam\, Friedrich-Engels-Straße 22\, 14473 Potsdam\, De
 utschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Fabulandlabs Workshop Tag2
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180208T090000Z
DTEND:20180208T150000Z
DTSTAMP:20190304T172911Z
UID:31hegve2b4bpkhua6i7s4tpal0@google.com
CREATED:20180131T072058Z
DESCRIPTION:Workshop für die partizipative Prototypenentwicklung für Mensch
 en mit besonderen Bedürfnissen
LAST-MODIFIED:20180131T072247Z
LOCATION:freiLand Potsdam\, Friedrich-Engels-Straße 22\, 14473 Potsdam\, De
 utschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Fabulandlabs Workshop Tag1
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20171212T190000
DTEND;TZID=Europe/Berlin:20171212T210000
RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=TU
DTSTAMP:20190304T172911Z
UID:2o60r26f5pq7muep7htdi4r01n@google.com
CLASS:PUBLIC
CREATED:20171126T091145Z
DESCRIPTION:Treffen der offenen OK Lab Gruppe. Informationen auf&nbsp\;<a h
 ref="https://www.google.com/url?q=http%3A%2F%2Fwww.oklab-potsdam.de&amp\;sa
 =D&amp\;usd=2&amp\;usg=AFQjCNH4ia7HdoVhwjLJiSfSMu46bTzIxA" target="_blank">
 www.oklab-potsdam.de</a><br>Themen sind: Open Data\, Civic Tech\, Programmi
 erung<br>
LAST-MODIFIED:20180114T091342Z
LOCATION:machBar Seminarraum
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:OK Lab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20170824T180000
DTEND;TZID=Europe/Berlin:20170824T200000
RRULE:FREQ=WEEKLY;BYDAY=TH
DTSTAMP:20190304T172911Z
UID:5neh1ktep3uqvjk197abrb0gio@google.com
CLASS:PUBLIC
CREATED:20170823T154208Z
DESCRIPTION:Offener Abend der machBar - Jeder ist Willkommen - <a href="htt
 ps://www.google.com/url?q=http%3A%2F%2Fwww.machbar-potsdam.de&amp\;sa=D&amp
 \;usd=2&amp\;usg=AFQjCNHgkYi-CBwfAjzxhtvkRZXlROswdg" target="_blank">www.ma
 chbar-potsdam.de</a>
LAST-MODIFIED:20180114T091318Z
LOCATION:machBar im Freiland Haus 5 - Potsdam
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:OpenLab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180123T170000
DTEND;TZID=Europe/Berlin:20180123T190000
RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=TU
DTSTAMP:20190304T172911Z
UID:646brirtu83g18fhg5jtmf1dac@google.com
CLASS:PUBLIC
CREATED:20180114T085716Z
DESCRIPTION:Plenum der machBar
LAST-MODIFIED:20180114T090813Z
LOCATION:Haus 5 - Seminarraum
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar Plenum
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171215T180000Z
DTEND:20171215T220000Z
DTSTAMP:20190304T172911Z
UID:1h64qnkskd7nl9l3c9qo5f4i24@google.com
CREATED:20171207T192459Z
DESCRIPTION:Öffentliche Wihnachtsfeier der machBar\, zu der alle Freundinne
 n und Freunde der machBar eingeladen sind.\n
LAST-MODIFIED:20171211T125822Z
LOCATION:machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Weihnachtsfeier
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20171227
DTEND;VALUE=DATE:20171228
DTSTAMP:20190304T172911Z
UID:27sgrcdu4099mtq830biaal87d@google.com
CREATED:20171211T125726Z
DESCRIPTION:Die Freifunker laden zum Livestream schauen vom 34c3 in die mac
 hBar ein. \n
LAST-MODIFIED:20171211T125726Z
LOCATION:machBar Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:34c3 in der machBar
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171202T100000Z
DTEND:20171202T190000Z
DTSTAMP:20190304T172911Z
UID:3auqqsk9ik7as92h61ipubamrm@google.com
CREATED:20171110T061505Z
DESCRIPTION:Umbau in Maschinenraum und Labor
LAST-MODIFIED:20171126T092204Z
LOCATION:machBar im freiLand Potsdam
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Arbeitseinsatz Part2
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171202T090000Z
DTEND:20171202T160000Z
DTSTAMP:20190304T172911Z
UID:2umrmkbncl3urpfd6k8ib7t0di@google.com
CREATED:20171126T091658Z
DESCRIPTION:Umbau in Maschinenraum und Labor\n
LAST-MODIFIED:20171126T091658Z
LOCATION:machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Arbeitseinsatz
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171119T090000Z
DTEND:20171119T170000Z
DTSTAMP:20190304T172911Z
UID:06r0tidq486ajl21l9snb3r7jh@google.com
CREATED:20171110T061418Z
DESCRIPTION:Vorbereitende Maßnahmen für den Umbau von Maschinenraum und Lab
 or
LAST-MODIFIED:20171110T061418Z
LOCATION:machBar im freiLand Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Arbeitseinsatz Part1
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171125T130000Z
DTEND:20171125T170000Z
DTSTAMP:20190304T172911Z
UID:5ek97lmft4h681a4bpf1g66i69@google.com
CREATED:20171110T061231Z
DESCRIPTION:
LAST-MODIFIED:20171110T061249Z
LOCATION:machBar im freiLand Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Drohnentreffen
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171116T193000Z
DTEND:20171116T203000Z
DTSTAMP:20190304T172911Z
UID:3e21t1trks34rdhttbvje5t7ng@google.com
CREATED:20171110T061029Z
DESCRIPTION:
LAST-MODIFIED:20171110T061137Z
LOCATION:Haus 5\, Friedrich-Engels-Str. 22\, 14473 Potsdam
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:machBar Plenum 
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171118T090000Z
DTEND:20171118T193000Z
DTSTAMP:20190304T172911Z
UID:6jv9nk3nps25428ppffa2eueod@google.com
CREATED:20170907T210759Z
DESCRIPTION:
LAST-MODIFIED:20170907T210759Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:OpenDataBarCamp - www.potsdam.io
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171118T100000Z
DTEND:20171118T140000Z
DTSTAMP:20190304T172911Z
UID:5cvfnchqjfa8a831jj8qifdm79@google.com
CREATED:20170907T210717Z
DESCRIPTION:
LAST-MODIFIED:20170907T210717Z
LOCATION:Stadt- Und Landesbibliothek\, Am Kanal 47\, 14467 Potsdam\, German
 y
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:(Stadt- und Landesbibliothek) repairCafe
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171021T090000Z
DTEND:20171021T130000Z
DTSTAMP:20190304T172911Z
UID:69isdq0hnjfp13ovf1jr23luij@google.com
CREATED:20170907T210439Z
DESCRIPTION:
LAST-MODIFIED:20170907T210617Z
LOCATION:Stadt- und Landesbibliothek Potsdam\, Am Kanal 47\, 14467 Potsdam\
 , Germany
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:(Stadt- und Landesbibliothek) repairCafe
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20170923T090000Z
DTEND:20170923T130000Z
DTSTAMP:20190304T172911Z
UID:1gv09kcmibh8q2j2scht2j14tq@google.com
CLASS:PUBLIC
CREATED:20170823T161342Z
DESCRIPTION:www.bibliothek.potsdam.de/repair-cafe-reparieren-statt-wegwerfe
 n-2
LAST-MODIFIED:20170907T210321Z
LOCATION:Stadt- und Landesbibliothek Potsdam\, Am Kanal 47\, 14467 Potsdam\
 , Germany
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:(Stadt- und Landesbibliothek) repairCafe
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20170823T180000
DTEND;TZID=Europe/Berlin:20170823T200000
RRULE:FREQ=WEEKLY;COUNT=8;BYDAY=MO,WE
DTSTAMP:20190304T172911Z
UID:34c0eggrc3qi4te2g3km1jl05g@google.com
CLASS:PUBLIC
CREATED:20170823T161131Z
DESCRIPTION:
LAST-MODIFIED:20170823T161131Z
LOCATION:Freiland Haus 5 - Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Uni Potsdam - Drohnenseminar
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20171007
DTEND;VALUE=DATE:20171023
DTSTAMP:20190304T172911Z
UID:71vvvsbcjb3b4gsfmsjel6aqtb@google.com
CLASS:PUBLIC
CREATED:20170823T154828Z
DESCRIPTION:www.codeweek.eu
LAST-MODIFIED:20170823T154828Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:CODEWEEK
TRANSP:TRANSPARENT
END:VEVENT
BEGIN:VEVENT
DTSTART:20171006T150000Z
DTEND:20171006T200000Z
DTSTAMP:20190304T172911Z
UID:3j9e90dlt1fiah7f9upt3iimks@google.com
CLASS:PUBLIC
CREATED:20170823T154740Z
DESCRIPTION:Vernetzungstreffen von Aktiven aus Brandenburger FabLabs\, offe
 nen Werkstätten\, Hacker Spaces\, Makerspaces\, Garagen\, Hobbyräumen...
LAST-MODIFIED:20170823T154740Z
LOCATION:Freiland Haus 5 - Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Vernetzungstreffen Brandenburger FabLabs
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20170822T160000Z
DTEND:20170822T190000Z
DTSTAMP:20190304T172911Z
UID:0lkrmhsgfmq1bgaf54qs91a595@google.com
CREATED:20170823T154534Z
DESCRIPTION:www.machbar-potsdam.de
LAST-MODIFIED:20170823T154534Z
LOCATION:Freiland Haus 5 - Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Vorstellung Sensorkit für aquatische Vor-Ort-Parameter
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20170822T190000
DTEND;TZID=Europe/Berlin:20170822T210000
RRULE:FREQ=WEEKLY;UNTIL=20170904T215959Z;INTERVAL=2;BYDAY=TU
DTSTAMP:20190304T172911Z
UID:7kk7rorknhett094id0k0gc3mj@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CLASS:PUBLIC
CREATED:20170823T153811Z
DESCRIPTION:Treffen der offenen OK Lab Gruppe. Informationen auf www.oklab-
 potsdam.de\nThemen sind: Open Data\, Civic Tech\, Programmierung
LAST-MODIFIED:20170823T153941Z
LOCATION:machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:OK Lab Potsdam
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20170629T170000Z
DTEND:20170629T200000Z
DTSTAMP:20190304T172911Z
UID:557so5mpmiubtg38jihapek2o5@google.com
CREATED:20170628T085452Z
DESCRIPTION:
LAST-MODIFIED:20170628T085503Z
LOCATION:
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Open Lab
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/discourse_no_dtend.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:icalendar-ruby
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:WiLaP - machBar Events
X-WR-TIMEZONE:Europe/Berlin
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
DTSTART:20190331T030000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
TZNAME:CEST
END:DAYLIGHT
BEGIN:STANDARD
DTSTART:20181028T020000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
TZNAME:CET
END:STANDARD
END:VTIMEZONE
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
DTSTART:20190331T030000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
TZNAME:CEST
END:DAYLIGHT
BEGIN:STANDARD
DTSTART:20181028T020000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
TZNAME:CET
END:STANDARD
END:VTIMEZONE
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
DTSTART:20190331T030000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
TZNAME:CEST
END:DAYLIGHT
BEGIN:STANDARD
DTSTART:20181028T020000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
TZNAME:CET
END:STANDARD
END:VTIMEZONE
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
DTSTART:20190331T030000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
TZNAME:CEST
END:DAYLIGHT
BEGIN:STANDARD
DTSTART:20191027T020000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
TZNAME:CET
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTAMP:20190304T170552Z
UID:0ab03762-6e6d-40d7-9ceb-b49844ba61a4
DTSTART;TZID=Europe/Berlin:20190117T180025
DESCRIPTION:Zwei FH-Studentinnen (Anne und Caro) haben sich die Bar angesch
 aut und wollen wiederkommen. \nIch habe sie zu diesem Discourse eingeladen
 . \nOtto baute mit dem Laserdrucker ein Gehäuse für ein DMX Interface. \
 nEs gab die Ve&hellip\;
SUMMARY:2019-01-17 openLab
URL:/c/machbar/calendar
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20190304T170552Z
UID:d7069eb4-e82c-40af-9486-fb5bb332c328
DTSTART;TZID=Europe/Berlin:20190228T150014
DTEND;TZID=Europe/Berlin:20190228T183014
DESCRIPTION:@Bjorn:  Ich möchte hier noch kurzfristig anmelden das wir am 
 Donnerstag von 15-18:00 einen Workshop in der machBar haben. Dieses ist im
  Rahmen des DiReBio-Projekt vom Wissenschafsladen. Das Thema ist ‘Hemp a
 s a sustaina&hellip\;
SUMMARY:Hanf als nachhaltiges Material -- Workshop in der Machbar
URL:/c/machbar/calendar
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20190304T170552Z
UID:51e14101-6ccb-446c-99d4-662fe4d6acad
DTSTART;TZID=Europe/Berlin:20190301T180035
DTEND;TZID=Europe/Berlin:20190301T210035
DESCRIPTION:FYI \n\nFür euch als Info\, die Leute um matchMyMaker und beAb
 le haben uns Angefragt ob sie die machBar für einen Hackathon/Workshop zu
  Hilfsmitteln an den ersten 3 Märzwochenenden nutzen können. \nSie wollt
 en es eigentlich &hellip\;
SUMMARY:Einmietung HACKademy - erste drei Märzwochenenden
URL:/c/machbar/calendar
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20190304T170552Z
UID:903a1e32-b506-4db9-9acd-f1304c0ba8eb
DTSTART;TZID=Europe/Berlin:20190511T130021
DTEND;TZID=Europe/Berlin:20190511T200021
DESCRIPTION:Am 11.05. ist der Tag der Wissenschaften für die Potsdamer Ins
 titute von proWissen e.V. organisiert. \nEr geht von 13-20 Uhr und findet 
 dieses Jahr an der FH statt. \nWas haltet ihr davon wenn wir dort als WiLa
 P Präsent si&hellip\;
SUMMARY:Potsdamer Tag der Wissenschaften 11.5.2019
URL:/c/machbar/calendar
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/duplicated_rrule.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//CyrusIMAP.org/Cyrus 
 3.9.0-alpha0-85-gd6d859e0cf-fm-20230116.001-gd6d859e0//EN
BEGIN:VEVENT
CREATED:20230109T084023Z
LAST-MODIFIED:20230119T110732Z
DTSTAMP:20230119T110732Z
UID:56cdc4dc-11b7-407c-86c6-9faedfc28afb
SUMMARY:My repeating event
RRULE:FREQ=WEEKLY;BYDAY=TH;COUNT=20
RRULE:FREQ=WEEKLY;BYDAY=TH;COUNT=20
DTSTART;TZID=Europe/London:20230112T100000
DTEND;TZID=Europe/London:20230112T120000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/duration_edited.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T154052Z
LAST-MODIFIED:20190303T154145Z
DTSTAMP:20190303T154145Z
UID:5d4c6843-9300-4f91-8d88-6094d4b0b840
SUMMARY:original event
RRULE:FREQ=DAILY;UNTIL=20190320T030000Z
DTSTART;TZID=Europe/Berlin:20190318T040000
DTEND;TZID=Europe/Berlin:20190318T050000
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T154131Z
LAST-MODIFIED:20190303T154145Z
DTSTAMP:20190303T154145Z
UID:5d4c6843-9300-4f91-8d88-6094d4b0b840
SUMMARY:edited duration
RECURRENCE-ID;TZID=Europe/Berlin:20190319T040000
DTSTART;TZID=Europe/Berlin:20190319T040000
DURATION:PT3H
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:2
LOCATION:location
DESCRIPTION:
CLASS:
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/duration.ics`

```ics
BEGIN:VCALENDAR
X-SOURCE:https://github.com/irgangla/icalevents/blob/master/test/test_data/duration.ics
X-LICENSE:https://github.com/irgangla/icalevents/blob/master/LICENSE
BEGIN:VEVENT
DTSTART:20180110
DURATION:P3D
DESCRIPTION:Event with duration (3 days), instead of explicit end.
SUMMARY:Duration Event 1
END:VEVENT
BEGIN:VEVENT
DTSTART:20180115T100000
DURATION:PT3H
DESCRIPTION:Event with duration (3 hours), instead of explicit end.
SUMMARY:Duration Event 2
END:VEVENT
BEGIN:VEVENT
DTSTART:20180120T120000
DESCRIPTION:Event without explicit dtend, nor duration property.
SUMMARY:Short event
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/each_week_but_one_deleted.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T153829
LAST-MODIFIED:20190303T144155Z
DTSTAMP:20190303T144155Z
UID:SX2CURHKFTKKFFU3VUD7K
SUMMARY:test6
STATUS:CONFIRMED
RRULE:FREQ=WEEKLY;COUNT=8
EXDATE:20190310T233000Z
DTSTART;TZID=Europe/Berlin:20190304T003000
DTEND;TZID=Europe/Berlin:20190304T010000
CLASS:PUBLIC
SEQUENCE:1
X-MOZ-GENERATION:1
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/each_week_but_two_deleted.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T153829
LAST-MODIFIED:20190303T151329Z
DTSTAMP:20190303T151329Z
UID:SX2CURHKFTKKFFU3VUD7K
SUMMARY:test6
STATUS:CONFIRMED
RRULE:FREQ=WEEKLY;COUNT=8
EXDATE:20190310T233000Z
EXDATE:20190324T233000Z
DTSTART;TZID=Europe/Berlin:20190304T003000
DTEND;TZID=Europe/Berlin:20190304T010000
CLASS:PUBLIC
SEQUENCE:2
X-MOZ-GENERATION:2
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/end_before_start_event.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T083000
DTEND;TZID=Europe/Berlin:20190304T080000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/event_10_times.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20200115T225152Z
LAST-MODIFIED:20200115T225240Z
DTSTAMP:20200115T225240Z
UID:64374d28-089b-4958-8c95-cdd00e6d8ad3
SUMMARY:event 10 times
RRULE:FREQ=DAILY;COUNT=10
DTSTART;TZID=Europe/Berlin:20200113T074500
DTEND;TZID=Europe/Berlin:20200113T100000
TRANSP:OPAQUE
SEQUENCE:1
X-MOZ-GENERATION:1
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/fablab_cottbus.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//85.13.163.15//NONSGML kigkonsult.se iCalcreator 2.24.2//
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-FROM-URL:http://blog.fablab-cottbus.de
X-WR-TIMEZONE:Europe/Berlin
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:STANDARD
DTSTART:20181028T030000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RDATE:20191027T030000
TZNAME:CET
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:20190331T020000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RDATE:20200329T020000
TZNAME:CEST
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
UID:ai1ec-1862@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:
DESCRIPTION:Wir sind auf dem Karlstraßenfest – kommt uns besuchen: https://
 www.facebook.com/events/297637247437414/\nDie Werkstatt bleibt am Samstag 
 deswegen geschlossen.
DTSTART;VALUE=DATE:20180609
DTEND;VALUE=DATE:20180610
LOCATION:Karlstraßenfest
SEQUENCE:0
SUMMARY:Lab geschlossen: Wir sind auf dem Karlstraßenfest
URL:http://blog.fablab-cottbus.de/Veranstaltung/wir-sind-auf-dem-karlstrass
 enfest-lab-geschlossen/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Wir sind auf 
 dem Karlstraßenfest – kommt uns besuchen: https://www.facebook.com/events/
 297637247437414/<br />\nDie Werkstatt bleibt am Samstag deswegen geschloss
 en. </p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1441@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; maximilian-voigt@fablab-cottbus.de
DESCRIPTION:Es ist schon wieder Dezember! Wir können es auch kaum glauben… 
 Deswegen möchten wir das Repair Café zu diesem Anlass ein bisschen umgesta
 lten: Zum Kaffee und Kuchen gibt’s Glühwein und statt nur kaputtes kommen 
 noch schöne Weihnachtsbasteleien auf den Tisch. Lasst Euch überraschen ode
 r überrascht uns\, indem ihr ein paar schöne Ideen mitbringt! Wir freun un
 s auf Euch!\n„Ein Repair Café ist eine Selbsthilfewerkstatt zur Reparatur 
 defekter Gegenstände. Freiwillige helfen mit Wissen\, Werkzeug und Kaffee 
 sowie Rat und Tat gegen einen Unkostenbeitrag. Repair Cafés finden in fest
  oder temporär zur Verfügung gestellten Räumen wie Technikräumen an Schule
 n oder Vereinsgebäuden statt. Die Idee kommt aus den Niederlanden und hat 
 zahlreiche Nachahmer.“ Wikipedia\nHier geht’s zur entsprechenden Wiki-Seit
 e. Dort gibt’s ein paar mehr Infos und Eindrücke.
DTSTART;TZID=Europe/Berlin:20161203T140000
DTEND;TZID=Europe/Berlin:20161203T190000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:Weihnachts Repair-Café
URL:http://blog.fablab-cottbus.de/Veranstaltung/weihnachts-repair-cafe/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Es ist schon 
 wieder Dezember! Wir können es auch kaum glauben… Deswegen möchten wir das
  Repair Café zu diesem Anlass ein bisschen umgestalten: Zum Kaffee und Kuc
 hen gibt’s Glühwein und statt nur kaputtes kommen noch schöne Weihnachtsba
 steleien auf den Tisch. Lasst Euch überraschen oder überrascht uns\, indem
  ihr ein paar schöne Ideen mitbringt! Wir freun uns auf Euch!</p>\n<p>„Ein
  Repair Café ist eine Selbsthilfewerkstatt zur Reparatur defekter Gegenstä
 nde. Freiwillige helfen mit Wissen\, Werkzeug und Kaffee sowie Rat und Tat
  gegen einen Unkostenbeitrag. Repair Cafés finden in fest oder temporär zu
 r Verfügung gestellten Räumen wie Technikräumen an Schulen oder Vereinsgeb
 äuden statt. Die Idee kommt aus den Niederlanden und hat zahlreiche Nachah
 mer.“ Wikipedia</p>\n<p>Hier geht’s zur entsprechenden <a href='http://fab
 lab-cottbus.de/index.php/Repair-Cafe' target='_blank'>Wiki-Seite</a>. Dort
  gibt’s ein paar mehr Infos und Eindrücke.</p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1621@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Nanu Frechen\; nanu@fablab-cottbus.de
DESCRIPTION:Die bisherigen Tagesordnungspunkte:\nTOP 1: Änderung des Mitgli
 edsbeitrages\n    wie sieht die Fördermitgliedschaft aus?\n    kann man si
 ch einen Teil des Mitgliedsbeitrages durch allgemeinnützige Arbeiten zurüc
 kerarbeiten?\nTOP 2: Fensteröffner/RFID Zugang\n    letzte Festlegungen zu
 m Kartenpfand\nTOP 3: Anpassungen in der Satzung\, der Werkstattordnung un
 d unserer Geschäftsordnung\n    ausländerfeindliche Äußerungen über unsere
  öffentliche Kanäle satzungsmäßig ausschließen\n    Anpassung der Werkstat
 tordnung an die neuen Maschinen und Gegebenheiten\n    Geschäftsordnung: z
 .B. Mitgliedsbeitrag eintragen\, Sepa verfahren etc.\nTOP 4: Wo wollen wir
  uns mit unserem Verein hin entwickeln?\n    Wollen wir uns professionalis
 ieren?\n    Wie können wir mehr Angebote für mehr Leute anbieten?\n    Wie
  schaffen wir mehr Engagement?\n    Wie können wir mehr gemeinsame Projekt
 e und generell mehr Zusammenarbeit und Geselligkeit im fablab fördern?\n  
   Wollen wir mehr mit Firmen\, Institutionen\, der Uni zusammen arbeiten?
 \n    Oder wollen wir lieber der kleine Bastelkeller bleiben\, wo jeder vo
 r sich hin arbeitet?
DTSTART;TZID=Europe/Berlin:20170311T170000
DTEND;TZID=Europe/Berlin:20170311T210000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:Vereinssitzung
URL:http://blog.fablab-cottbus.de/Veranstaltung/vereinssitzung/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Die bisherige
 n Tagesordnungspunkte:</p>\n<p>TOP 1: Änderung des Mitgliedsbeitrages</p>
 \n<p>    wie sieht die Fördermitgliedschaft aus?<br />\n    kann man sich 
 einen Teil des Mitgliedsbeitrages durch allgemeinnützige Arbeiten zurücker
 arbeiten?</p>\n<p>TOP 2: Fensteröffner/RFID Zugang</p>\n<p>    letzte Fest
 legungen zum Kartenpfand</p>\n<p>TOP 3: Anpassungen in der Satzung\, der W
 erkstattordnung und unserer Geschäftsordnung</p>\n<p>    ausländerfeindlic
 he Äußerungen über unsere öffentliche Kanäle satzungsmäßig ausschließen<br
  />\n    Anpassung der Werkstattordnung an die neuen Maschinen und Gegeben
 heiten<br />\n    Geschäftsordnung: z.B. Mitgliedsbeitrag eintragen\, Sepa
  verfahren etc.</p>\n<p>TOP 4: Wo wollen wir uns mit unserem Verein hin en
 twickeln?</p>\n<p>    Wollen wir uns professionalisieren?<br />\n    Wie k
 önnen wir mehr Angebote für mehr Leute anbieten?<br />\n    Wie schaffen w
 ir mehr Engagement?<br />\n    Wie können wir mehr gemeinsame Projekte und
  generell mehr Zusammenarbeit und Geselligkeit im fablab fördern?<br />\n 
    Wollen wir mehr mit Firmen\, Institutionen\, der Uni zusammen arbeiten?
 <br />\n    Oder wollen wir lieber der kleine Bastelkeller bleiben\, wo je
 der vor sich hin arbeitet?</p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1648@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Nanu Frechen\; nanu@fablab-cottbus.de
DESCRIPTION:Wir unterstützen das Repair Café der Stadt Cottbus. Seid auch i
 hr dabei und repariert mit uns\, bis der Kaffee zur Neige geht!\nHier geht
  es zur Website der Veranstaltung.
DTSTART;TZID=Europe/Berlin:20170610T100000
DTEND;TZID=Europe/Berlin:20170610T160000
LOCATION:Spreegallerie Cottbus @ Karl-Marx-Straße\, 03046 Cottbus
SEQUENCE:0
SUMMARY:Repair und Recycling Café
URL:http://blog.fablab-cottbus.de/Veranstaltung/repair-und-recycling-cafe/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Wir unterstüt
 zen das Repair Café der Stadt Cottbus. Seid auch ihr dabei und repariert m
 it uns\, bis der Kaffee zur Neige geht!</p>\n<p><a href='https://www.cottb
 us.de/abfrage/events/event.pl?key=kultur&zeit=25473683'>Hier geht es zur W
 ebsite der Veranstaltung.</a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1647@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; m.voigt@fablab-cottbus.de
DESCRIPTION:„In Brandenburg ist wieder jemand gegen einen Baum gegurkt\, wa
 s soll man auch machen mit 17\, 18 in Brandenburg?“ Dass um Berlin mehr pa
 ssiert\, als es Rainald Grebe hier ironisch zuspitzt\, wissen die Brandenb
 urger Maker. Aber wir könnten sichtbarer werden. Aus diesem Grund möchten 
 wir ein Treffen aller Besucher*innen von Hack-\, Maker- und Fab-Spaces in 
 Brandenburg organisieren\, uns vernetzen und folgende Themen besprechen:\n
 \n\nRaus aus dem MakerSpace – Erfahrungen in der Zusammenarbeit mit andere
 n Akteuren.\nÜberregionale Hardwareprojekte – wie sind eure Erfahrungen? W
 orauf habt ihr Lust?\n\nZum Event auf maker-faire.de
DTSTART;TZID=Europe/Berlin:20170611T163000
DTEND;TZID=Europe/Berlin:20170611T173000
LOCATION:Maker Faire Berlin @ Luckenwalder Str. 4–6\, 10963 Berlin
SEQUENCE:0
SUMMARY:Brandenburger Maker-Treffen
URL:http://blog.fablab-cottbus.de/Veranstaltung/brandenburger-maker-treffen
 /
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>„In Brandenbu
 rg ist wieder jemand gegen einen Baum gegurkt\, was soll man auch machen m
 it 17\, 18 in Brandenburg?“ Dass um Berlin mehr passiert\, als es Rainald 
 Grebe hier ironisch zuspitzt\, wissen die Brandenburger Maker. Aber wir kö
 nnten sichtbarer werden. Aus diesem Grund möchten wir ein Treffen aller Be
 sucher*innen von Hack-\, Maker- und Fab-Spaces in Brandenburg organisieren
 \, uns vernetzen und folgende Themen besprechen:</p>\n<div>\n<ul>\n<li>Rau
 s aus dem MakerSpace – Erfahrungen in der Zusammenarbeit mit anderen Akteu
 ren.</li>\n<li>Überregionale Hardwareprojekte – wie sind eure Erfahrungen?
  Worauf habt ihr Lust?</li>\n</ul>\n<p><a href='https://maker-faire.de/wor
 kshop/berlin/2017/brandenburger-maker-meetup/'>Zum Event auf maker-faire.d
 e</a></p>\n</div>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1504@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:
DESCRIPTION:***ACHTUNG: Der Computer-Treff FÄLLT AM 5.07. AUS!***
DTSTART;TZID=Europe/Berlin:20170705T174500
DTEND;TZID=Europe/Berlin:20170705T194500
SEQUENCE:0
SUMMARY:Der Computer-Treff fällt aus
URL:http://blog.fablab-cottbus.de/Veranstaltung/der-3d-donnerstag-faellt-au
 s/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p><strong>***AC
 HTUNG: Der Computer-Treff FÄLLT AM 5.07. AUS!***</strong></p>\n</BODY></HT
 ML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1671@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; m.voigt@fablab-cottbus.de
DESCRIPTION:Es ist Zeit für Sonne und Bier! Dazu gibt’s einen heißen Grill\
 , gute Musik und natürlich eine offene Werkstatt. Für alle\, die diese ger
 ne erkunden möchten\, gibt es kleine Bauaktionen. Zum Beispiel könnt ihr e
 uer erstes 3D-Modell drucken\, aus eurem alten Handy eine Bluetooth-Musikb
 ox bauen oder euch an mitgebrachten Ideen und Projekten versuchen. \n\n\n 
 \n\n\nWir freuen uns auf einen sonnigen Tag!
DTSTART;TZID=Europe/Berlin:20170729T140000
DTEND;TZID=Europe/Berlin:20170729T220000
LOCATION:FabLab Cottbus
SEQUENCE:0
SUMMARY:Sommerfest
URL:http://blog.fablab-cottbus.de/Veranstaltung/sommerfest/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='' da
 ta-block='true' data-editor='38q22' data-offset-key='5mbcb-0-0'>\n<div cla
 ss='_1mf _1mj' data-offset-key='5mbcb-0-0'><span data-offset-key='5mbcb-0-
 0'><strong>Es ist Zeit für Sonne und Bier!</strong> Dazu gibt’s einen heiß
 en Grill\, gute Musik und natürlich eine offene Werkstatt. Für alle\, die 
 diese gerne erkunden möchten\, gibt es kleine Bauaktionen. Zum Beispiel kö
 nnt ihr euer erstes 3D-Modell drucken\, aus eurem alten Handy eine Bluetoo
 th-Musikbox bauen oder euch an mitgebrachten Ideen und Projekten versuchen
 . </span></div>\n</div>\n<div class='' data-block='true' data-editor='38q2
 2' data-offset-key='5ssq7-0-0'>\n<div class='_1mf _1mj' data-offset-key='5
 ssq7-0-0'><span data-offset-key='5ssq7-0-0'> </span></div>\n</div>\n<div c
 lass='' data-block='true' data-editor='38q22' data-offset-key='7440e-0-0'>
 \n<div class='_1mf _1mj' data-offset-key='7440e-0-0'><span data-offset-key
 ='7440e-0-0'>Wir freuen uns auf einen sonnigen Tag!</span></div>\n</div>\n
 </BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1706@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Nanu Frechen\; nanu@fablab-cottbus.de
DESCRIPTION:OpenSCAD ist eine Programmiersprache\, mit der 3D-Modelle konst
 ruiert werden können. Wir werden verrückte mathematische Formeln ausprobie
 ren\, mit denen sich faszinierende 3D-Objekte erstellen lassen. Hier geht 
 es zu mehr Informationen und zur Anmeldung
DTSTART;TZID=Europe/Berlin:20171019T160000
DTEND;TZID=Europe/Berlin:20171019T200000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5 03044 Cottbus
SEQUENCE:0
SUMMARY:3D-Modelle programmieren mit OpenSCAD
URL:http://blog.fablab-cottbus.de/Veranstaltung/3d-modelle-programmieren-mi
 t-openscad/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>OpenSCAD ist 
 eine Programmiersprache\, mit der 3D-Modelle konstruiert werden können. Wi
 r werden verrückte mathematische Formeln ausprobieren\, mit denen sich fas
 zinierende 3D-Objekte erstellen lassen. <a href='https://meet-and-code.org
 /event/details/279' rel='noopener' target='_blank'>Hier geht es zu mehr In
 formationen und zur Anmeldung</a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1705@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Nanu Fechen\; nanu@fablab-cottbus.de
DESCRIPTION:Was sind Cryptowährungen wie Bitcoin und wie funktionieren sie?
  Und welche Bedeutung werden sie in Zukunft haben? Lerne mit uns\, was man
  alles mit der Blockchain-Technologie machen kann. Hier geht es zu mehr In
 formationen und zur Anmeldung
DTSTART;TZID=Europe/Berlin:20171020T160000
DTEND;TZID=Europe/Berlin:20171020T200000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5 03044 Cottbus
SEQUENCE:0
SUMMARY:Programmier dir deine eigene Crypto-Währung
URL:http://blog.fablab-cottbus.de/Veranstaltung/programmier-dir-deine-eigen
 e-crypto-waehrung/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Was sind Cryp
 towährungen wie Bitcoin und wie funktionieren sie? Und welche Bedeutung we
 rden sie in Zukunft haben? Lerne mit uns\, was man alles mit der Blockchai
 n-Technologie machen kann. <a href='https://meet-and-code.org/event/detail
 s/278' rel='noopener' target='_blank'>Hier geht es zu mehr Informationen u
 nd zur Anmeldung</a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1703@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; m.voigt@fablab-cottbus.de
DESCRIPTION:Wir stecken uns gemeinsam ein Arduino-Board zusammen und schrei
 ben erste Programme. Am Ende hat jeder und jede eine Wetterstation für’s H
 eimklima und kann Sensordaten selbst erfassen und auswerten. Hier geht es 
 zu mehr Informationen und zur Anmeldung
DTSTART;TZID=Europe/Berlin:20171021T130000
DTEND;TZID=Europe/Berlin:20171021T180000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5 03044 Cottbus
SEQUENCE:0
SUMMARY:Programmiere deine eigene Wetterstation
URL:http://blog.fablab-cottbus.de/Veranstaltung/programmiere-deine-eigene-w
 etterstation/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Wir stecken u
 ns gemeinsam ein Arduino-Board zusammen und schreiben erste Programme. Am 
 Ende hat jeder und jede eine Wetterstation für’s Heimklima und kann Sensor
 daten selbst erfassen und auswerten. <a href='https://meet-and-code.org/ev
 ent/details/275' rel='noopener' target='_blank'>Hier geht es zu mehr Infor
 mationen und zur Anmeldung</a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1704@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Marcus Heide\; marcus@fablab-cottbus.de
DESCRIPTION:Wie sauber ist die Luft\, die ich atme? Während dieses Workshop
 s baust du dir dein eigenes Sensorsystem\, das du zur Messung der Feinstau
 bbelastung\, Temperatur und Luftfeuchtigkeit nutzen kannst. Hier geht es z
 u mehr Informationen und zur Anmeldung
DTSTART;TZID=Europe/Berlin:20171022T130000
DTEND;TZID=Europe/Berlin:20171022T180000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5 03044 Cottbus
SEQUENCE:0
SUMMARY:Luftqualität: Ein Workshop zum selber messen (Einsteiger)
URL:http://blog.fablab-cottbus.de/Veranstaltung/luftqualitaet-ein-workshop-
 zum-selber-messen-einsteiger/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Wie sauber is
 t die Luft\, die ich atme? Während dieses Workshops baust du dir dein eige
 nes Sensorsystem\, das du zur Messung der Feinstaubbelastung\, Temperatur 
 und Luftfeuchtigkeit nutzen kannst. <a href='https://meet-and-code.org/eve
 nt/details/276' rel='noopener' target='_blank'>Hier geht es zu mehr Inform
 ationen und zur Anmeldung</a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1707@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Dominik Reyke \; domryk@live.de
DESCRIPTION:Bau dir deine eigene Website. Designe deine HTML Website mit CS
 S und binde eine erste SQL Tabelle via PHP ein. Hier geht es zu mehr Infor
 mationen und zur Anmeldung
DTSTART;TZID=Europe/Berlin:20171022T130000
DTEND;TZID=Europe/Berlin:20171022T180000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5 03044 Cottbus
SEQUENCE:0
SUMMARY:Websites selbst programmieren
URL:http://blog.fablab-cottbus.de/Veranstaltung/websites-selbst-programmier
 en/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Bau dir deine
  eigene Website. Designe deine HTML Website mit CSS und binde eine erste S
 QL Tabelle via PHP ein. <a href='https://meet-and-code.org/event/details/2
 80' rel='noopener' target='_blank'>Hier geht es zu mehr Informationen und 
 zur Anmeldung</a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1669@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:
DESCRIPTION:***ACHTUNG: Der 3D-Donnerstag FÄLLT AM 6.07. AUS!***
DTSTART;TZID=Europe/Berlin:20180104T174500
DTEND;TZID=Europe/Berlin:20180104T194500
SEQUENCE:0
SUMMARY:Der 3D-Donnerstag fällt aus
URL:http://blog.fablab-cottbus.de/Veranstaltung/der-3d-donnerstag-faellt-au
 s-2/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p><strong>***AC
 HTUNG: Der 3D-Donnerstag FÄLLT AM 6.07. AUS!***</strong></p>\n</BODY></HTM
 L>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1887@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; maximilian-voigt@fablab-cottbus.de
DESCRIPTION:Dein Handy ist kaputt\, der Staubsauger streikt oder du brauchs
 t Hilfe beim Flicken deiner Hose? Dann komm ins Fablab Cottbus! Seit dem 1
 . November 2014 hilft das Fablab beim Selbermachen. Bring einfach mit\, wa
 s kaputt ist und wir versuchen es gemeinsam zu reparieren – egal ob Elektr
 onik\, Holzmöbel oder Textilien\, an dem Tag ist für jedes Problem jemand 
 fachkundiges in der Werkstatt.\n„Ein Repair Café ist eine Selbsthilfewerks
 tatt zur Reparatur defekter Gegenstände. Freiwillige helfen mit Wissen\, W
 erkzeug und Kaffee sowie Rat und Tat gegen einen Unkostenbeitrag. Repair C
 afés finden in fest oder temporär zur Verfügung gestellten Räumen wie Tech
 nikräumen an Schulen oder Vereinsgebäuden statt. Die Idee kommt aus den Ni
 ederlanden und hat zahlreiche Nachahmer.“ Wikipedia\nHier geht’s zur entsp
 rechenden Wiki-Seite. Dort gibt’s mehr Informationen und Eindrücke.
DTSTART;TZID=Europe/Berlin:20180106T140000
DTEND;TZID=Europe/Berlin:20180106T170000
GEO:+51.76882;+14.32321
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5\, 03044 Cottbus\, Deutschl
 and
RRULE:FREQ=MONTHLY;BYDAY=1SA
SEQUENCE:0
SUMMARY:Repair Café
URL:http://blog.fablab-cottbus.de/Veranstaltung/repair-cafe-2/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p style='text-a
 lign: justify\;'>Dein Handy ist kaputt\, der Staubsauger streikt oder du b
 rauchst Hilfe beim Flicken deiner Hose? Dann komm ins Fablab Cottbus! Seit
  dem 1. November 2014 hilft das Fablab beim Selbermachen. Bring einfach mi
 t\, was kaputt ist und wir versuchen es gemeinsam zu reparieren – egal ob 
 Elektronik\, Holzmöbel oder Textilien\, an dem Tag ist für jedes Problem j
 emand fachkundiges in der Werkstatt.</p>\n<p style='text-align: justify\;'
 >„Ein Repair Café ist eine Selbsthilfewerkstatt zur Reparatur defekter Geg
 enstände. Freiwillige helfen mit Wissen\, Werkzeug und Kaffee sowie Rat un
 d Tat gegen einen Unkostenbeitrag. Repair Cafés finden in fest oder tempor
 är zur Verfügung gestellten Räumen wie Technikräumen an Schulen oder Verei
 nsgebäuden statt. Die Idee kommt aus den Niederlanden und hat zahlreiche N
 achahmer.“ Wikipedia</p>\n<p>Hier geht’s zur entsprechenden <a href='http:
 //fablab-cottbus.de/index.php/Repair-Cafe' target='_blank' rel='noopener n
 oreferrer'>Wiki-Seite</a>. Dort gibt’s mehr Informationen und Eindrücke.</
 p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1781@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; maximilian-voigt@fablab-cottbus.de
DESCRIPTION:Im Workshop werden Grundkenntnisse des CNC-Fräsens vermittelt. 
 Außerdem wird in die BZT-CNC-Fräse unserer Werkstatt eingeführt. Der Works
 hop ist Voraussetzung\, wenn ihr die Fräse einsetzen möchtet.\nBitte bring
 t unbedingt euren Laptop mit!
DTSTART;TZID=Europe/Berlin:20180120T150000
DTEND;TZID=Europe/Berlin:20180120T163000
GEO:+51.76882;+14.32321
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5\, 03044 Cottbus\, Deutschl
 and
SEQUENCE:0
SUMMARY:Workshop: Einführung CNC-Fräsen
URL:http://blog.fablab-cottbus.de/Veranstaltung/workshop-einfuehrung-cnc-fr
 aesen/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2016/11/DSC_1363-300x199.jpg\;300\;199\,medium\;http://blog.fablab-cottbu
 s.de/wp-content/uploads/2016/11/DSC_1363-300x199.jpg\;300\;199\,large\;htt
 p://blog.fablab-cottbus.de/wp-content/uploads/2016/11/DSC_1363-300x199.jpg
 \;300\;199\,full\;http://blog.fablab-cottbus.de/wp-content/uploads/2016/11
 /DSC_1363-300x199.jpg\;300\;199
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p><img src='htt
 p://blog.fablab-cottbus.de/wp-content/uploads/2016/11/DSC_1363-300x199.jpg
 ' alt='' width='300' height='199' class='alignnone size-medium wp-image-16
 19' srcset='http://blog.fablab-cottbus.de/wp-content/uploads/2016/11/DSC_1
 363-300x199.jpg 300w\, http://blog.fablab-cottbus.de/wp-content/uploads/20
 16/11/DSC_1363-768x508.jpg 768w\, http://blog.fablab-cottbus.de/wp-content
 /uploads/2016/11/DSC_1363.jpg 1000w' sizes='(max-width: 300px) 100vw\, 300
 px' /><br />\nIm Workshop werden Grundkenntnisse des CNC-Fräsens vermittel
 t. Außerdem wird in die BZT-CNC-Fräse unserer Werkstatt eingeführt. Der Wo
 rkshop ist Voraussetzung\, wenn ihr die Fräse einsetzen möchtet.<br />\n<s
 trong>Bitte bringt unbedingt euren Laptop mit!</strong></p>\n</BODY></HTML
 >
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1736@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; m.voigt@fablab-cottbus.de
DESCRIPTION:Bei der Vereinssitzung besprechen wir aktuelle Ereignisse und e
 ntscheiden über das zukünftige Vorgehen\, wie über Investitionen\, Veranst
 altungen oder Vereinsregeln. Jeder und jede ist willkommen und kann der Si
 tzung beiwohnen. Mitbestimmen können allerdings nur Mitglieder des Vereins
 .
DTSTART;TZID=Europe/Berlin:20180331T170000
DTEND;TZID=Europe/Berlin:20180331T190000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5 03044 Cottbus
SEQUENCE:0
SUMMARY:Vereinssitzung
URL:http://blog.fablab-cottbus.de/Veranstaltung/vereinssitzung-2/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Bei der Verei
 nssitzung besprechen wir aktuelle Ereignisse und entscheiden über das zukü
 nftige Vorgehen\, wie über Investitionen\, Veranstaltungen oder Vereinsreg
 eln. Jeder und jede ist willkommen und kann der Sitzung beiwohnen. Mitbest
 immen können allerdings nur Mitglieder des Vereins. </p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1844@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Nanu Frechen\; nanu@fablab-cottbus.de
DESCRIPTION:Computerspiele sind voll 2017 – Brettspiele sind wieder angesag
 t! \nDie zwei Cottbuser Tüftler Jörg Kiefer und Michael Linke haben sich e
 in pfiffiges neues Spiel ausgedacht. Vor einem Jahr saßen sie noch bei uns
  im fablab und haben am 3D-Druck ihrer Spielfiguren gefeilt. Nun steht das
  Spiel verkaufsbereit im Online-Shop! \nBei „Kompass\, das Spiel“ geht es 
 um Kaufen und Verkaufen\, Investieren und Rendite machen. Doch anders als 
 bei Monopoly gewinnt nicht der mit den dicksten Immobilien\, denn bei Komp
 ass ist der Markt unberechenbar! So wie im wahren Leben bewegt sich im Spi
 el der Markt durch Boom\, Rezession\, Depression und Expansion. Man muss a
 lso genau wissen\, was in den verschiedenen Konjunkturphasen gerade angesa
 gt ist und seine Strategie darauf einstellen. So muss man sich z.B. überle
 gen ob man eher auf Sicherheit geht oder das Risiko zu nutzen weiß!\n\nAm 
 Mittwoch den 18.4. um 18 Uhr ist daher im FabLab Spieleabend angesagt! Wir
  drehen gemeinsam mit den Kompass-Entwicklern eine Runde durch den Konjunk
 turzyklus. \nWer Spaß am Spielen hat und die Kreation der beiden Cottbuser
  Entwickler kennen lernen möchte ist herzlich eingeladen!
DTSTART;TZID=Europe/Berlin:20180418T180000
DTEND;TZID=Europe/Berlin:20180418T200000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5 03044 Cottbus
SEQUENCE:0
SUMMARY:Let’s play: Kompass
URL:http://blog.fablab-cottbus.de/Veranstaltung/lets-play-kompass/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2018/04/spielbrett-1024x1024-150x150.jpeg\;150\;150\;1\,medium\;http://bl
 og.fablab-cottbus.de/wp-content/uploads/2018/04/spielbrett-1024x1024-300x3
 00.jpeg\;300\;300\;1\,large\;http://blog.fablab-cottbus.de/wp-content/uplo
 ads/2018/04/spielbrett-1024x1024.jpeg\;480\;480\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2018/04/spielbrett-1024x1024-300x300.jpeg' width='300' h
 eight='300' /></div><p>Computerspiele sind voll 2017 – Brettspiele sind wi
 eder angesagt! </p>\n<p>Die zwei Cottbuser Tüftler Jörg Kiefer und Michael
  Linke haben sich ein pfiffiges neues Spiel ausgedacht. Vor einem Jahr saß
 en sie noch bei uns im fablab und haben am 3D-Druck ihrer Spielfiguren gef
 eilt. Nun steht das Spiel verkaufsbereit im Online-Shop! </p>\n<p>Bei „<a 
 href='https://kompass-spiel.de/' rel='noopener' target='_blank'>Kompass\, 
 das Spiel</a>“ geht es um Kaufen und Verkaufen\, Investieren und Rendite m
 achen. Doch anders als bei Monopoly gewinnt nicht der mit den dicksten Imm
 obilien\, denn bei Kompass ist der Markt unberechenbar! So wie im wahren L
 eben bewegt sich im Spiel der Markt durch Boom\, Rezession\, Depression un
 d Expansion. Man muss also genau wissen\, was in den verschiedenen Konjunk
 turphasen gerade angesagt ist und seine Strategie darauf einstellen. So mu
 ss man sich z.B. überlegen ob man eher auf Sicherheit geht oder das Risiko
  zu nutzen weiß!</p>\n<p><iframe width='560' height='315' src='https://www
 .youtube.com/embed/lNHY2N2AqQk' frameborder='0' allow='autoplay\; encrypte
 d-media' allowfullscreen></iframe></p>\n<p>Am Mittwoch den <strong>18.4. u
 m 18 Uhr</strong> ist daher im FabLab Spieleabend angesagt! Wir drehen gem
 einsam mit den Kompass-Entwicklern eine Runde durch den Konjunkturzyklus. 
 </p>\n<p>Wer Spaß am Spielen hat und die Kreation der beiden Cottbuser Ent
 wickler kennen lernen möchte ist herzlich eingeladen!</p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1853@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; m.voigt@fablab-cottbus.de
DESCRIPTION:Gemeinsam mit dem Verbund Brandenburger Maker sind wir dieses J
 ahr auf der Maker Faire Berlin. Kommt uns besuchen\, entdeckt spannende Pr
 ojekte\, lasst euch inspirieren und nehmt an den zahlreichen Workshops tei
 l.
DTSTART;TZID=Europe/Berlin:20180525T090000
DTEND;TZID=Europe/Berlin:20180527T180000
LOCATION:FEZ-Berlin - Wuhlheide
SEQUENCE:0
SUMMARY:Das fablabcb auf der Maker Faire
URL:http://blog.fablab-cottbus.de/Veranstaltung/das-fablabcb-auf-der-maker-
 faire/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Gemeinsam mit
  dem <a href='https://brandenburger-maker.github.io/' rel='noopener' targe
 t='_blank'>Verbund Brandenburger Maker</a> sind wir dieses Jahr auf der Ma
 ker Faire Berlin. Kommt uns besuchen\, entdeckt spannende Projekte\, lasst
  euch inspirieren und nehmt an den zahlreichen Workshops teil. </p>\n</BOD
 Y></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1438@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Nanu Frechen\; nanu@fablab-cottbus.de
DESCRIPTION:Das Repair Café finde nicht am Samstag (1.9.) sondern am Sonnta
 g (2.9.) statt. Wir freuen uns auf euch! Die Öffnungszeit fällt am Samstag
  ebenfalls aus.
DTSTART;TZID=Europe/Berlin:20180901T180000
DTEND;TZID=Europe/Berlin:20180901T200000
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:Achtung\, verschoben: Repair Café
URL:http://blog.fablab-cottbus.de/Veranstaltung/3d-donnerstag/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p>Das Repair Ca
 fé finde nicht am Samstag (1.9.) sondern am Sonntag (2.9.) statt. Wir freu
 en uns auf euch! Die Öffnungszeit fällt am Samstag ebenfalls aus.</p>\n</B
 ODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1211@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; maximilian-voigt@fablab-cottbus.de
DESCRIPTION:Dein Handy ist kaputt\, der Staubsauger streikt oder du brauchs
 t Hilfe beim Flicken deiner Hose? Dann komm ins Fablab Cottbus! Seit dem 1
 . November 2014 hilft das Fablab beim Selbermachen. Bring einfach mit\, wa
 s kaputt ist und wir versuchen es gemeinsam zu reparieren – egal ob Elektr
 onik\, Holzmöbel oder Textilien\, an dem Tag ist für jedes Problem jemand 
 fachkundiges in der Werkstatt.\n„Ein Repair Café ist eine Selbsthilfewerks
 tatt zur Reparatur defekter Gegenstände. Freiwillige helfen mit Wissen\, W
 erkzeug und Kaffee sowie Rat und Tat gegen einen Unkostenbeitrag. Repair C
 afés finden in fest oder temporär zur Verfügung gestellten Räumen wie Tech
 nikräumen an Schulen oder Vereinsgebäuden statt. Die Idee kommt aus den Ni
 ederlanden und hat zahlreiche Nachahmer.“ Wikipedia\nHier geht’s zur entsp
 rechenden Wiki-Seite. Dort gibt’s mehr Informationen und Eindrücke.
DTSTART;TZID=Europe/Berlin:20180902T140000
DTEND;TZID=Europe/Berlin:20180902T170000
GEO:+51.76882;+14.32321
LOCATION:FabLab Cottbus @ Walther-Pauer-Straße 5\, 03044 Cottbus\, Deutschl
 and
SEQUENCE:0
SUMMARY:Repair Café
URL:http://blog.fablab-cottbus.de/Veranstaltung/repair-cafe/
X-COST-TYPE:free
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><p style='text-a
 lign: justify\;'>Dein Handy ist kaputt\, der Staubsauger streikt oder du b
 rauchst Hilfe beim Flicken deiner Hose? Dann komm ins Fablab Cottbus! Seit
  dem 1. November 2014 hilft das Fablab beim Selbermachen. Bring einfach mi
 t\, was kaputt ist und wir versuchen es gemeinsam zu reparieren – egal ob 
 Elektronik\, Holzmöbel oder Textilien\, an dem Tag ist für jedes Problem j
 emand fachkundiges in der Werkstatt.</p>\n<p style='text-align: justify\;'
 >„Ein Repair Café ist eine Selbsthilfewerkstatt zur Reparatur defekter Geg
 enstände. Freiwillige helfen mit Wissen\, Werkzeug und Kaffee sowie Rat un
 d Tat gegen einen Unkostenbeitrag. Repair Cafés finden in fest oder tempor
 är zur Verfügung gestellten Räumen wie Technikräumen an Schulen oder Verei
 nsgebäuden statt. Die Idee kommt aus den Niederlanden und hat zahlreiche N
 achahmer.“ Wikipedia</p>\n<p>Hier geht’s zur entsprechenden <a href='http:
 //fablab-cottbus.de/index.php/Repair-Cafe' target='_blank' rel='noopener n
 oreferrer'>Wiki-Seite</a>. Dort gibt’s mehr Informationen und Eindrücke.</
 p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1903@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Dominik Ryk\; domryk@live.de
DESCRIPTION:Du hast ein Projekt\, für das du eine eigene Internetseite baue
 n möchtest? Oder dich interessiert einfach wie moderne Webauftritte aufgeb
 aut sind? Beim Workshop wirst du beides lernen. Wir behandeln einfache HTM
 L-Programmierung und wie du mithilfe von CSS individuelle Designs verwirkl
 ichen kannst. \nDer Workshop ist kostenlos und für Einsteigende geeignet. 
 Bitte bringt einen Laptop mit!\nJetzt anmelden
DTSTART;TZID=Europe/Berlin:20181008T180000
DTEND;TZID=Europe/Berlin:20181008T220000
LOCATION:FabLabCB @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:Websites selbst programmieren
URL:http://blog.fablab-cottbus.de/Veranstaltung/websites-selbst-programmier
 en-2/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2018/09/29cab82cd490c77f9fa66f165007e6be27dec9e3-150x150.jpeg\;150\;150\;
 1\,medium\;http://blog.fablab-cottbus.de/wp-content/uploads/2018/09/29cab8
 2cd490c77f9fa66f165007e6be27dec9e3-300x200.jpeg\;300\;200\;1\,large\;http:
 //blog.fablab-cottbus.de/wp-content/uploads/2018/09/29cab82cd490c77f9fa66f
 165007e6be27dec9e3.jpeg\;500\;334\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2018/09/29cab82cd490c77f9fa66f165007e6be27dec9e3-300x200
 .jpeg' width='300' height='200' /></div><p>Du hast ein Projekt\, für das d
 u eine eigene Internetseite bauen möchtest? Oder dich interessiert einfach
  wie moderne Webauftritte aufgebaut sind? Beim Workshop wirst du beides le
 rnen. Wir behandeln einfache HTML-Programmierung und wie du mithilfe von C
 SS individuelle Designs verwirklichen kannst. </p>\n<p>Der Workshop ist ko
 stenlos und für Einsteigende geeignet. <strong>Bitte bringt einen Laptop m
 it!</strong></p>\n<p><a href='https://www.meet-and-code.org/de/de/event-sh
 ow/1092' rel='noopener' target='_blank'><button name='button'>Jetzt anmeld
 en</button></a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1900@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Nanu Frechen\; nanu@fablab-cottbus.de
DESCRIPTION:OpenSCAD ist eine Programmiersprache\, mit der 3D-Modelle konst
 ruiert werden können. Wir werden verrückte mathematische Formeln ausprobie
 ren\, mit denen sich faszinierende 3D-Objekte erstellen lassen. Wir zeigen
  dir\, wie du Mathematik wirklich anwenden kannst – und keine Sorge: Du mu
 sst kein Matheprofi sein! Wir helfen dir dabei die 3D-Modelle zu programmi
 eren. Wenn noch Zeit ist\, darfst du sie auch über den 3D-Drucker testen. 
 \nWir freuen uns auf einen spannenden Abend! \nDer Workshop ist kostenlos 
 und für Einsteigende. Bitte bringt einen Laptop mit!\nJetzt anmelden
DTSTART;TZID=Europe/Berlin:20181011T180000
DTEND;TZID=Europe/Berlin:20181011T200000
LOCATION:FabLabCB @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:3D-Modelle programmieren mit OpenSCAD
URL:http://blog.fablab-cottbus.de/Veranstaltung/3d-modelle-programmieren-mi
 t-openscad-2/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2016/11/waage_3d-150x150.jpg\;150\;150\;1\,medium\;http://blog.fablab-cot
 tbus.de/wp-content/uploads/2016/11/waage_3d-300x160.jpg\;300\;160\;1\,larg
 e\;http://blog.fablab-cottbus.de/wp-content/uploads/2016/11/waage_3d.jpg\;
 993\;528\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2016/11/waage_3d-300x160.jpg' width='300' height='160' /
 ></div><p>OpenSCAD ist eine Programmiersprache\, mit der 3D-Modelle konstr
 uiert werden können. Wir werden verrückte mathematische Formeln ausprobier
 en\, mit denen sich faszinierende 3D-Objekte erstellen lassen. Wir zeigen 
 dir\, wie du Mathematik wirklich anwenden kannst – und keine Sorge: Du mus
 st kein Matheprofi sein! Wir helfen dir dabei die 3D-Modelle zu programmie
 ren. Wenn noch Zeit ist\, darfst du sie auch über den 3D-Drucker testen. <
 /p>\n<p>Wir freuen uns auf einen spannenden Abend! </p>\n<p>Der Workshop i
 st kostenlos und für Einsteigende. <strong>Bitte bringt einen Laptop mit!<
 /strong></p>\n<p><a href='https://www.meet-and-code.org/de/de/event-show/1
 211' rel='noopener' target='_blank'><button name='button'>Jetzt anmelden</
 button></a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1901@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Marcus Heide\; marcus.heide@outlook.com
DESCRIPTION:Wie sauber ist die Luft\, die ich atme? Wie lassen sich eigene 
 Messdaten erheben\, um dieser Frage auf den Grund zu gehen? Während dieses
  Workshops baust du dir dein eigenes Sensorsystem\, das du zur Messung der
  Feinstaubbelastung\, Temperatur und Luftfeuchtigkeit nutzen kannst. Werde
  Teil des deutschlandweiten luftdaten.info-Netzwerkes und teile deine Date
 n mit anderen. \nDer Workshop ist kostenlos und für Einsteigende geeignet.
  Bitte bringt einen Laptop mit!\nJetzt anmelden
DTSTART;TZID=Europe/Berlin:20181013T150000
DTEND;TZID=Europe/Berlin:20181013T173000
LOCATION:FabLabCB @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:Luftqualität: Ein Workshop zum selber messen
URL:http://blog.fablab-cottbus.de/Veranstaltung/luftqualitaet-ein-workshop-
 zum-selber-messen/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2018/09/33947e55bab179ce8727f7b4385f8970df83b2dd-150x150.jpeg\;150\;150\;
 1\,medium\;http://blog.fablab-cottbus.de/wp-content/uploads/2018/09/33947e
 55bab179ce8727f7b4385f8970df83b2dd-300x212.jpeg\;300\;212\;1\,large\;http:
 //blog.fablab-cottbus.de/wp-content/uploads/2018/09/33947e55bab179ce8727f7
 b4385f8970df83b2dd.jpeg\;500\;353\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2018/09/33947e55bab179ce8727f7b4385f8970df83b2dd-300x212
 .jpeg' width='300' height='212' /></div><p>Wie sauber ist die Luft\, die i
 ch atme? Wie lassen sich eigene Messdaten erheben\, um dieser Frage auf de
 n Grund zu gehen? Während dieses Workshops baust du dir dein eigenes Senso
 rsystem\, das du zur Messung der Feinstaubbelastung\, Temperatur und Luftf
 euchtigkeit nutzen kannst. Werde Teil des deutschlandweiten luftdaten.info
 -Netzwerkes und teile deine Daten mit anderen. </p>\n<p>Der Workshop ist k
 ostenlos und für Einsteigende geeignet. <strong>Bitte bringt einen Laptop 
 mit!</strong></p>\n<p><a href='https://www.meet-and-code.org/de/de/event-s
 how/1209' rel='noopener' target='_blank'><button name='button'>Jetzt anmel
 den</button></a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1898@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Marcel Jongmanns\; mjongmanns@gmail.com
DESCRIPTION:Es ist ein Einsteigerkurs für den Umgang mit Mikrocontrollern a
 m Beispiel eines Arduino. Die Hardware und der Handhabung damit wird Stück
  für Stück vorgestellt.\nAls Beispielanwendung wird ein Gießautomat für Pf
 lanzen aufgebaut. Die Feuchtigkeit der Erde wird über einen Sensor erfasst
 . Ist diese zu niedrig\, wird eine Pumpe eingeschaltet\, die Wasser in den
  Blumentopf pumpt.\nZur Überwachung der Umgebung wird ein Sensor angeschlo
 ssen\, der die Temperatur und Luftfeuchte aufnimmt. Die Daten lassen sich 
 an einem PC anzeigen.\nMitbringen: Laptop mit installierter Arduino IDE. E
 s werden weitere Libraries benötigt. \nDer Workshop ist kostenlos und für 
 Einsteigende. Bitte bringt einen Laptop mit!\nJetzt anmelden
DTSTART;TZID=Europe/Berlin:20181014T120000
DTEND;TZID=Europe/Berlin:20181014T140000
LOCATION:FabLabCB @ Walther-Pauer-Straße 5\, 03044 Cottbus Cottbus
SEQUENCE:0
SUMMARY:Pflanzenüberwachung mit Arduino
URL:http://blog.fablab-cottbus.de/Veranstaltung/pflanzenueberwachung-mit-ar
 duino/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2018/09/86d14bcd26afa3a549a900db8de54d6e0a92a7a9-150x150.jpeg\;150\;150\;
 1\,medium\;http://blog.fablab-cottbus.de/wp-content/uploads/2018/09/86d14b
 cd26afa3a549a900db8de54d6e0a92a7a9-300x202.jpeg\;300\;202\;1\,large\;http:
 //blog.fablab-cottbus.de/wp-content/uploads/2018/09/86d14bcd26afa3a549a900
 db8de54d6e0a92a7a9.jpeg\;500\;336\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2018/09/86d14bcd26afa3a549a900db8de54d6e0a92a7a9-300x202
 .jpeg' width='300' height='202' /></div><p>Es ist ein Einsteigerkurs für d
 en Umgang mit Mikrocontrollern am Beispiel eines Arduino. Die Hardware und
  der Handhabung damit wird Stück für Stück vorgestellt.<br />\nAls Beispie
 lanwendung wird ein Gießautomat für Pflanzen aufgebaut. Die Feuchtigkeit d
 er Erde wird über einen Sensor erfasst. Ist diese zu niedrig\, wird eine P
 umpe eingeschaltet\, die Wasser in den Blumentopf pumpt.<br />\nZur Überwa
 chung der Umgebung wird ein Sensor angeschlossen\, der die Temperatur und 
 Luftfeuchte aufnimmt. Die Daten lassen sich an einem PC anzeigen.<br />\nM
 itbringen: Laptop mit installierter Arduino IDE. Es werden weitere Librari
 es benötigt. </p>\n<p>Der Workshop ist kostenlos und für Einsteigende. <st
 rong>Bitte bringt einen Laptop mit!</strong></p>\n<p><a href='https://www.
 meet-and-code.org/de/de/event-show/1212' rel='noopener' target='_blank'><b
 utton name='button'>Jetzt anmelden</button></a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1894@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Jannik Schilling\; jannik.schilling@gmail.com
DESCRIPTION:LaTeX ist ein Compiler\, der es ermöglicht sehr ansehnliche Tex
 tdokumente zu erstellen – ganz ohne Stress mit der Formatierung. Was benöt
 igt wird\, sind nur ein paar Befehle. Die lernt ihr in diesem Einsteigerku
 rs. Der ist folgendermaßen aufgebaut:\n* Einführung und Installation\n* Br
 iefe mit Latex\n* Seminar-\, Bachelor- und andere Abschlussarbeiten\n* Prä
 sentationen\n* Mathematische und chemische Formeln (optional)\n* Lebenslau
 f (optional)\n* Poster (optional) \nDer Workshop ist kostenlos und für Ein
 steigende gedacht. Bitte bringt einen Laptop mit.\nJetzt anmelden
DTSTART;TZID=Europe/Berlin:20181018T150000
DTEND;TZID=Europe/Berlin:20181018T180000
LOCATION:FabLabCB @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:LaTeX für Einsteigende
URL:http://blog.fablab-cottbus.de/Veranstaltung/latex-fuer-einsteigende/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2018/09/ccbd3d10d23a14a4dcedaa7089527d384f78dd92-150x150.png\;150\;150\;1
 \,medium\;http://blog.fablab-cottbus.de/wp-content/uploads/2018/09/ccbd3d1
 0d23a14a4dcedaa7089527d384f78dd92-261x300.png\;261\;300\;1\,large\;http://
 blog.fablab-cottbus.de/wp-content/uploads/2018/09/ccbd3d10d23a14a4dcedaa70
 89527d384f78dd92.png\;500\;575\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2018/09/ccbd3d10d23a14a4dcedaa7089527d384f78dd92-261x300
 .png' width='261' height='300' /></div><p>LaTeX ist ein Compiler\, der es 
 ermöglicht sehr ansehnliche Textdokumente zu erstellen – ganz ohne Stress 
 mit der Formatierung. Was benötigt wird\, sind nur ein paar Befehle. Die l
 ernt ihr in diesem Einsteigerkurs. Der ist folgendermaßen aufgebaut:</p>\n
 <p>* Einführung und Installation<br />\n* Briefe mit Latex<br />\n* Semina
 r-\, Bachelor- und andere Abschlussarbeiten<br />\n* Präsentationen<br />
 \n* Mathematische und chemische Formeln (optional)<br />\n* Lebenslauf (op
 tional)<br />\n* Poster (optional) </p>\n<p>Der Workshop ist kostenlos und
  für Einsteigende gedacht. <strong>Bitte bringt einen Laptop mit.</strong>
 </p>\n<p><a href='https://www.meet-and-code.org/de/de/event-show/1221' rel
 ='noopener' target='_blank'><button name='button'>Jetzt anmelden</button><
 /a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1890@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Christian Hanisch\; christian.hanisch@fablab-cottbus.de
DESCRIPTION:Wie kann ich mein Smartphone google-frei bekommen? Im Workshop 
 lernst du verschiedene Alternativen kennen und wir helfen dir dabei dein e
 igenes Gerät einzurichten.\nAblauf :\n-Welche Betriebssysteme für Smartpho
 nes gibt es?\n-Wo liegen Vor-/Nachteile\n-Vorbereitung der Installation\n-
 Praktische Anwendung \nDer Workshop ist kostenlos. Bitte bringt einen Lapt
 op und ggf. ein funktionierendes Smartphone mit.\nJetzt anmelden
DTSTART;TZID=Europe/Berlin:20181019T150000
DTEND;TZID=Europe/Berlin:20181019T180000
LOCATION:FabLabCB @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:Alternative Betriebssysteme für das Smartphone
URL:http://blog.fablab-cottbus.de/Veranstaltung/alternative-betriebssysteme
 -fuer-das-smartphone/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2018/09/5d5a7747ad81bfbef98132c8ffb1f4a76df783d3-150x150.jpeg\;150\;150\;
 1\,medium\;http://blog.fablab-cottbus.de/wp-content/uploads/2018/09/5d5a77
 47ad81bfbef98132c8ffb1f4a76df783d3-300x200.jpeg\;300\;200\;1\,large\;http:
 //blog.fablab-cottbus.de/wp-content/uploads/2018/09/5d5a7747ad81bfbef98132
 c8ffb1f4a76df783d3.jpeg\;500\;333\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2018/09/5d5a7747ad81bfbef98132c8ffb1f4a76df783d3-300x200
 .jpeg' width='300' height='200' /></div><p>Wie kann ich mein Smartphone go
 ogle-frei bekommen? Im Workshop lernst du verschiedene Alternativen kennen
  und wir helfen dir dabei dein eigenes Gerät einzurichten.</p>\n<p>Ablauf 
 :</p>\n<p>-Welche Betriebssysteme für Smartphones gibt es?<br />\n-Wo lieg
 en Vor-/Nachteile<br />\n-Vorbereitung der Installation<br />\n-Praktische
  Anwendung </p>\n<p>Der Workshop ist kostenlos. <strong>Bitte bringt einen
  Laptop und ggf. ein funktionierendes Smartphone mit.</strong></p>\n<p><a 
 href='https://www.meet-and-code.org/de/de/event-show/1221' rel='noopener' 
 target='_blank'><button name='button'>Jetzt anmelden</button></a></p>\n</B
 ODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1892@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Maximilian Voigt\; m.voigt@fablab-cottbus.de
DESCRIPTION:Täglich vermessen tausende technische Geräte mithilfe von Senso
 ren unsere Umwelt\, reagieren anhand der Ergebnisse oder speichern sie in 
 Datenbanken ab. Sind die Daten einmal erfasst\, wirken sie wie kleine Wahr
 heiten\, mit denen wir z.B. die Wasser- oder Luftqualität erforschen. Auf 
 dem Weg dahin kann aber vieles schiefgehen. Für unseren Alltag ist es also
  gut zu wissen\, wie solche Daten entstehen\, um Fehler erkennen und inter
 pretieren zu können. Thema dieses Workshops ist jener Weg\, vom natürliche
 n Ereignis zum digitalen Zahlenwert.\nAm Beispiel eines Temperatursensors\
 , eines sogenannten Heißleiters oder auch Thermistors\, werden wir gemeins
 am mit Marie erforschen\, was beim Erfassen einer Temperatur passiert. \nD
 er Workshop ist kostenlos und für Einsteigende gedacht. Bitte bringt eure 
 Notebooks mit!\nJetzt anmelden
DTSTART;TZID=Europe/Berlin:20181020T130000
DTEND;TZID=Europe/Berlin:20181020T170000
LOCATION:FabLabCB @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:Vom physikalische Ereignis zum Datensatz
URL:http://blog.fablab-cottbus.de/Veranstaltung/vom-physikalische-ereignis-
 zum-datensatz/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2018/09/8923285b3413f9a82afd63ecf224afcddb6ede50-150x150.jpeg\;150\;150\;
 1\,medium\;http://blog.fablab-cottbus.de/wp-content/uploads/2018/09/892328
 5b3413f9a82afd63ecf224afcddb6ede50-300x99.jpeg\;300\;99\;1\,large\;http://
 blog.fablab-cottbus.de/wp-content/uploads/2018/09/8923285b3413f9a82afd63ec
 f224afcddb6ede50.jpeg\;500\;165\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2018/09/8923285b3413f9a82afd63ecf224afcddb6ede50-300x99.
 jpeg' width='300' height='99' /></div><p>Täglich vermessen tausende techni
 sche Geräte mithilfe von Sensoren unsere Umwelt\, reagieren anhand der Erg
 ebnisse oder speichern sie in Datenbanken ab. Sind die Daten einmal erfass
 t\, wirken sie wie kleine Wahrheiten\, mit denen wir z.B. die Wasser- oder
  Luftqualität erforschen. Auf dem Weg dahin kann aber vieles schiefgehen. 
 Für unseren Alltag ist es also gut zu wissen\, wie solche Daten entstehen\
 , um Fehler erkennen und interpretieren zu können. Thema dieses Workshops 
 ist jener Weg\, vom natürlichen Ereignis zum digitalen Zahlenwert.</p>\n<p
 >Am Beispiel eines Temperatursensors\, eines sogenannten Heißleiters oder 
 auch Thermistors\, werden wir gemeinsam mit Marie erforschen\, was beim Er
 fassen einer Temperatur passiert. </p>\n<p>Der Workshop ist kostenlos und 
 für Einsteigende gedacht. <strong>Bitte bringt eure Notebooks mit!</strong
 ></p>\n<p><a href='https://www.meet-and-code.org/de/de/event-show/1216' re
 l='noopener' target='_blank'><button name='button'>Jetzt anmelden</button>
 </a></p>\n</BODY></HTML>
END:VEVENT
BEGIN:VEVENT
UID:ai1ec-1896@blog.fablab-cottbus.de
DTSTAMP:20190304T162103Z
CATEGORIES:
CONTACT:Marcel Jongmanns\; mjongmanns@gmail.com
DESCRIPTION:Ein Mikrofon wird an den Arduino angeschlossen und das analoge 
 Signal abgetastet. Die abgetasteten Daten werden mit einer Frequenzanalyse
  (FFT) analysiert. Keine Angst! Die Mathematik dahinter ist kein Thema. Es
  wird lediglich erklärt\, welche Daten benötigt werden und was die berechn
 eten Zahlen bedeuten. Mit einfachen statistischen Mitteln ist es nun mögli
 ch z.B. die Farbe einer RGB LED abhängig von der Frequenz und Amplitude de
 s Signales zu modulieren.\nBitte mitbringen: Laptop mit installierter Ardu
 ino IDE. Es werden weitere Libraries benötigt.\nVorraussetzung: Es sollte 
 bereits Programmiererfahrung vorhanden sein (Analogeingang\, Timer\, Array
 s\, Datentypen). Mathekenntnisse von Vorteil (Grundrechenarten\, Interpola
 tion\, Mittelwert). \nDer Workshop ist kostenlos und für Fortgeschrittene.
  Bitte bringt einen Laptop mit!\nJetzt anmelden
DTSTART;TZID=Europe/Berlin:20181021T120000
DTEND;TZID=Europe/Berlin:20181021T160000
LOCATION:FabLabCB @ Walther-Pauer-Straße 5\, 03044 Cottbus
SEQUENCE:0
SUMMARY:Audiogesteuerte Lichter
URL:http://blog.fablab-cottbus.de/Veranstaltung/audiogesteuerte-lichter/
X-COST-TYPE:free
X-WP-IMAGES-URL:thumbnail\;http://blog.fablab-cottbus.de/wp-content/uploads
 /2018/09/7bc2e0373505d888e6d2c46266003f8a06238ef1-150x150.jpeg\;150\;150\;
 1\,medium\;http://blog.fablab-cottbus.de/wp-content/uploads/2018/09/7bc2e0
 373505d888e6d2c46266003f8a06238ef1-300x199.jpeg\;300\;199\;1\,large\;http:
 //blog.fablab-cottbus.de/wp-content/uploads/2018/09/7bc2e0373505d888e6d2c4
 6266003f8a06238ef1.jpeg\;500\;331\;
X-ALT-DESC;FMTTYPE=text/html:<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 3.2//E
 N'>\\n<HTML>\\n<HEAD>\\n<TITLE></TITLE>\\n</HEAD>\\n<BODY><div class='ai1e
 c-event-avatar alignleft timely'><img src='http://blog.fablab-cottbus.de/w
 p-content/uploads/2018/09/7bc2e0373505d888e6d2c46266003f8a06238ef1-300x199
 .jpeg' width='300' height='199' /></div><p>Ein Mikrofon wird an den Arduin
 o angeschlossen und das analoge Signal abgetastet. Die abgetasteten Daten 
 werden mit einer Frequenzanalyse (FFT) analysiert. Keine Angst! Die Mathem
 atik dahinter ist kein Thema. Es wird lediglich erklärt\, welche Daten ben
 ötigt werden und was die berechneten Zahlen bedeuten. Mit einfachen statis
 tischen Mitteln ist es nun möglich z.B. die Farbe einer RGB LED abhängig v
 on der Frequenz und Amplitude des Signales zu modulieren.<br />\nBitte mit
 bringen: Laptop mit installierter Arduino IDE. Es werden weitere Libraries
  benötigt.<br />\nVorraussetzung: Es sollte bereits Programmiererfahrung v
 orhanden sein (Analogeingang\, Timer\, Arrays\, Datentypen). Mathekenntnis
 se von Vorteil (Grundrechenarten\, Interpolation\, Mittelwert). </p>\n<p>D
 er Workshop ist kostenlos und für Fortgeschrittene. <strong>Bitte bringt e
 inen Laptop mit!</strong></p>\n<p><a href='https://www.meet-and-code.org/d
 e/de/event-show/1213' rel='noopener' target='_blank'><button name='button'
 >Jetzt anmelden</button></a></p>\n</BODY></HTML>
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/Germany_Holidays.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Calendar Labs//Calendar 1.0//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Germany Holidays
X-WR-TIMEZONE:Etc/GMT
BEGIN:VEVENT
SUMMARY:New Year's Day
DTSTART:20190101
DTEND:20190101
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/new-years-day.php to know more about New Year's Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f312427a1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Epiphany
DTSTART:20190106
DTEND:20190106
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/spain/epiphany.php to know more about Epiphany. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31242de1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Carnival
DTSTART:20190305
DTEND:20190305
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/brazil/carnival.php to know more about Carnival. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f312433a1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Good Friday
DTSTART:20190419
DTEND:20190419
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/good-friday.php to know more about Good Friday. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31243901580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Easter Sunday
DTSTART:20190421
DTEND:20190421
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/easter.php to know more about Easter Sunday. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31243e91580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Easter Monday
DTSTART:20190422
DTEND:20190422
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/christian/easter-monday.php to know more about Easter Monday. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31244431580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Labor Day
DTSTART:20190501
DTEND:20190501
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/uk/may-day.php to know more about Labor Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f312449c1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Ascension Day
DTSTART:20190530
DTEND:20190530
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/romania/ascension-day.php to know more about Ascension Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31244f81580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Whit Monday
DTSTART:20190610
DTEND:20190610
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/germany/pentecost-monday.php to know more about Whit Monday. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31245501580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Corpus Christi
DTSTART:20190620
DTEND:20190620
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/corpus-christi.php to know more about Corpus Christi. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31245aa1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Assumption Day
DTSTART:20190815
DTEND:20190815
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/the-assumption-of-mary.php to know more about Assumption Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f312460b1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Unity Day (National)
DTSTART:20191003
DTEND:20191003
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/germany/unity-day.php to know more about Unity Day (National). 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31246691580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Reformation Day
DTSTART:20191031
DTEND:20191031
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/germany/reformation-day.php to know more about Reformation Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31246e21580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:All Saints Day
DTSTART:20191101
DTEND:20191101
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/philippines/all-saints-day.php to know more about All Saints Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31247411580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:National Day of Mourning
DTSTART:20191117
DTEND:20191117
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/germany/national-day-of-mourning.php to know more about National Day of Mourning. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31247a21580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Christmas Day
DTSTART:20191225
DTEND:20191225
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/christmas.php to know more about Christmas Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31248001580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Boxing Day
DTSTART:20191226
DTEND:20191226
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/canada/boxing-day.php to know more about Boxing Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f312485a1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:New Year's Day
DTSTART:20200101
DTEND:20200101
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/new-years-day.php to know more about New Year's Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31248b51580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Epiphany (BW\, BY & ST)
DTSTART:20200106
DTEND:20200106
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/spain/epiphany.php to know more about Epiphany (BW\, BY & ST). 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f312491a1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Carnival
DTSTART:20200225
DTEND:20200225
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/brazil/carnival.php to know more about Carnival. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f312497e1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Good Friday
DTSTART:20200410
DTEND:20200410
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/good-friday.php to know more about Good Friday. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f31249e41580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Easter Sunday
DTSTART:20200412
DTEND:20200412
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/easter.php to know more about Easter Sunday. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124a431580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Easter Monday
DTSTART:20200413
DTEND:20200413
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/christian/easter-monday.php to know more about Easter Monday. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124aa51580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Labor Day
DTSTART:20200501
DTEND:20200501
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/uk/may-day.php to know more about Labor Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124b021580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Ascension Day
DTSTART:20200521
DTEND:20200521
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/romania/ascension-day.php to know more about Ascension Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124b5f1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Whit Monday
DTSTART:20200601
DTEND:20200601
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/germany/pentecost-monday.php to know more about Whit Monday. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124bc41580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Corpus Christi
DTSTART:20200611
DTEND:20200611
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/corpus-christi.php to know more about Corpus Christi. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124c291580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Assumption Day
DTSTART:20200815
DTEND:20200815
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/the-assumption-of-mary.php to know more about Assumption Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124c891580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Unity Day (National)
DTSTART:20201003
DTEND:20201003
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/germany/unity-day.php to know more about Unity Day (National). 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124ceb1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Reformation Day
DTSTART:20201031
DTEND:20201031
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/germany/reformation-day.php to know more about Reformation Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124d521580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:All Saints Day
DTSTART:20201101
DTEND:20201101
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/philippines/all-saints-day.php to know more about All Saints Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124dbe1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:National Day of Mourning
DTSTART:20201115
DTEND:20201115
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/germany/national-day-of-mourning.php to know more about National Day of Mourning. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124e231580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Christmas Day
DTSTART:20201225
DTEND:20201225
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/us/christmas.php to know more about Christmas Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124e841580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
BEGIN:VEVENT
SUMMARY:Boxing Day
DTSTART:20201226
DTEND:20201226
LOCATION:Germany
DESCRIPTION:Visit https://calendarlabs.com/holidays/canada/boxing-day.php to know more about Boxing Day. 
 Like us on Facebook: http://fb.com/calendarlabs to get updates
RRULE:
UID:5e3a8f3124eeb1580896049@calendarlabs.com
DTSTAMP:20200205T094729Z
STATUS:CONFIRMED
TRANSP:TRANSPARENT
SEQUENCE:0
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_107_omitting_last_event.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Pacific Standard Time:
BEGIN:STANDARD
DTSTART:16010101T020000
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=1SU;BYMONTH=11
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:16010101T020000
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=2SU;BYMONTH=3
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
RRULE:FREQ=WEEKLY;UNTIL=20230608T170000Z;INTERVAL=1;BYDAY=TH;WKST=SU
DTSTART;TZID=Pacific Standard Time:20230105T100000
DTEND;TZID=Pacific Standard Time:20230105T110000
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_113_period_in_rdate.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
X-WR-CALNAME;VALUE=TEXT:Test RDATE
BEGIN:VTIMEZONE
TZID:America/Vancouver
BEGIN:STANDARD
DTSTART:20221106T020000
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
RDATE:20231105T020000
TZNAME:PST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:20230312T020000
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
RDATE:20240310T020000
TZNAME:PDT
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
UID:1
DESCRIPTION:Test RDATE
DTSTART;TZID=America/Vancouver:20230920T120000
DTEND;TZID=America/Vancouver:20230920T140000
EXDATE;TZID=America/Vancouver:20231220T120000
RDATE;VALUE=PERIOD;TZID=America/Vancouver:20231213T120000/20231213T150000
RRULE:FREQ=MONTHLY;COUNT=9;INTERVAL=1;BYDAY=+3WE;BYMONTH=1,2,3,4,5,9,10,11,
 12;WKST=MO
SUMMARY:Test RDATE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_113_period_rdate_duration.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART:20240912T120000Z
DTEND:20240912T130000Z
RDATE;VALUE=PERIOD:20240913T120000Z/PT2H
SUMMARY:The RDATE is a period with a duration.
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_117_until_before_dtstart.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20231102T221721Z
DTSTART;VALUE=DATE:20231002
DTEND;VALUE=DATE:20231009
SUMMARY:test123
CATEGORIES:other
SUBCALENDAR-NAME:test
EVENT-ID:538924
EVENT-ALLDAY:true
RRULE:FREQ=WEEKLY;UNTIL=20231001;INTERVAL=2;BYDAY=MO
CREATED:20231102T221633Z
LAST-MODIFIED:20231102T221716Z
TRANSP:TRANSPARENT
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_128_only_first_event.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20231102T221721Z
DTSTART;VALUE=DATE:20231002
DTEND;VALUE=DATE:20231009
SUMMARY:test123
CATEGORIES:other
SUBCALENDAR-NAME:test
EVENT-ID:538924
EVENT-ALLDAY:true
RRULE:FREQ=WEEKLY;UNTIL=20240331;COUNT=-1;INTERVAL=4;BYDAY=MO
CREATED:20231102T221633Z
LAST-MODIFIED:20231102T221716Z
TRANSP:TRANSPARENT
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_132_swapped_start_and_end.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
SUMMARY:XXX
DTSTART;TZID=Europe/Paris:20231218T234500
DTEND;TZID=Europe/Paris:20231218T233000
DTSTAMP:20231213T104027Z
UID:84A72-65798A00-5-20465200
SEQUENCE:1
ATTENDEE;CN="XXX";PARTSTAT=NEEDS-ACTION;ROLE=REQ-PARTICIPA
 NT;RSVP=TRUE:mailto:xxx@yyy.zzz
CLASS:PUBLIC
CREATED:20231213T104027Z
LAST-MODIFIED:20231213T104027Z
ORGANIZER;CN="XXX":mailto:aaa@yyy.zzz
TRANSP:OPAQUE
END:VEVENT
BEGIN:VTODO
SUMMARY:XXX
DTSTART;TZID=Europe/Paris:20231218T234500
DUE;TZID=Europe/Paris:20231218T233000
DTSTAMP:20231213T104027Z
UID:84A72-65798A00-5-20465200
SEQUENCE:1
ATTENDEE;CN="XXX";PARTSTAT=NEEDS-ACTION;ROLE=REQ-PARTICIPA
 NT;RSVP=TRUE:mailto:xxx@yyy.zzz
CLASS:PUBLIC
CREATED:20231213T104027Z
LAST-MODIFIED:20231213T104027Z
ORGANIZER;CN="XXX":mailto:aaa@yyy.zzz
TRANSP:OPAQUE
END:VTODO
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_148_edge_case_1.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
RECURRENCE-ID;VALUE=DATE:20240715
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240702
DTEND;VALUE=DATE:20240709
SUMMARY:test123 - edited event!!!!
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:2
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
EXDATE;VALUE=DATE:20240715
CREATED:20240311T051101Z
LAST-MODIFIED:20240701T063743Z
SEQUENCE:3
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_148_edge_case_2.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
RECURRENCE-ID;VALUE=DATE:20240715
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240702
DTEND;VALUE=DATE:20240709
SUMMARY:test123 - edited event!!!!
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:2
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240701T063743Z
SEQUENCE:3
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_148_exdate_and_rdate_unedited.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240702
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
EXDATE;VALUE=DATE:20240715
RDATE;VALUE=DATE:20240717
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_148_exdate_and_rdate_updated.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240702
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
EXDATE;VALUE=DATE:20240715
RDATE;VALUE=DATE:20240717
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240702
SUMMARY:test123 - edited
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
EXDATE;VALUE=DATE:20240729
RDATE;VALUE=DATE:20240730
CREATED:20240311T051101Z
LAST-MODIFIED:20240701T063743Z
SEQUENCE:2
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_148_ignored_exdate.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:test123 - edited
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240801;INTERVAL=2;BYDAY=MO
EXDATE;VALUE=DATE:20240715
CREATED:20240311T051101Z
LAST-MODIFIED:20240701T063743Z
SEQUENCE:2
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_15_duplicated_events.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART:20130803T190000Z
DTEND:20130803T210000Z
SUMMARY:This is an event
END:VEVENT
BEGIN:VEVENT
DTSTART:20130803T190000Z
DTEND:20130803T210000Z
SUMMARY:This event is almost the same event
END:VEVENT
BEGIN:VEVENT
DTSTART:20130803T190000Z
DTEND:20130803T220000Z
SUMMARY:This event is a little longer but starts at the same time
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_151_macos_linux_difference.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Saint Marina Calendar
X-WR-TIMEZONE:America/Los_Angeles
BEGIN:VTIMEZONE
TZID:America/Los_Angeles
X-LIC-LOCATION:America/Los_Angeles
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTART;TZID=America/Los_Angeles:20140801T190000
DTEND;TZID=America/Los_Angeles:20140801T200000
RRULE:FREQ=YEARLY
EXDATE;TZID=America/Los_Angeles:20160801T190000
DTSTAMP:20240807T000326Z
UID:aogpprh4bolu8ckmop49ca6404@google.com
CREATED:20140331T192650Z
LAST-MODIFIED:20150731T022326Z
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Vespers for the Feast of St. Joseph
TRANSP:OPAQUE
BEGIN:VALARM
ACTION:NONE
TRIGGER;VALUE=DATE-TIME:19760401T005545Z
X-WR-ALARMUID:0D3A9816-AC61-499A-A594-930AA281666B
UID:0D3A9816-AC61-499A-A594-930AA281666B
END:VALARM
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Los_Angeles:20140801T183000
DTEND;TZID=America/Los_Angeles:20140801T193000
DTSTAMP:20240807T000326Z
UID:aogpprh4bolu8ckmop49ca6404@google.com
RECURRENCE-ID;TZID=America/Los_Angeles:20140801T190000
CREATED:20140331T192650Z
LAST-MODIFIED:20150731T022326Z
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:Vespers for the Feast of St. Joseph
TRANSP:OPAQUE
BEGIN:VALARM
ACTION:NONE
TRIGGER;VALUE=DATE-TIME:19760401T005545Z
X-WR-ALARMUID:8744D632-C9F8-483C-B095-590E0A3D2E39
UID:8744D632-C9F8-483C-B095-590E0A3D2E39
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_151_macos_linux_difference2.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Saint Marina Calendar
X-WR-TIMEZONE:America/Los_Angeles
BEGIN:VTIMEZONE
TZID:America/Los_Angeles
X-LIC-LOCATION:America/Los_Angeles
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTART;TZID=America/Los_Angeles:20140801T190000
DTEND;TZID=America/Los_Angeles:20140801T200000
RRULE:FREQ=YEARLY
EXDATE;TZID=America/Los_Angeles:20160801T190000
DTSTAMP:20240807T000326Z
UID:aogpprh4bolu8ckmop49ca6404@google.com
CREATED:20140331T192650Z
LAST-MODIFIED:20150731T022326Z
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Vespers for the Feast of St. Joseph
TRANSP:OPAQUE
BEGIN:VALARM
ACTION:NONE
TRIGGER;VALUE=DATE-TIME:19760401T005545Z
X-WR-ALARMUID:0D3A9816-AC61-499A-A594-930AA281666B
UID:0D3A9816-AC61-499A-A594-930AA281666B
END:VALARM
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Los_Angeles:20140801T183000
DTEND;TZID=America/Los_Angeles:20140801T193000
DTSTAMP:20240807T000326Z
UID:aogpprh4bolu8ckmop49ca6404@google.com
RECURRENCE-ID;TZID=America/Los_Angeles:20140801T190000
CREATED:20140331T192650Z
LAST-MODIFIED:20150731T022326Z
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:Vespers for the Feast of St. Joseph
TRANSP:OPAQUE
BEGIN:VALARM
ACTION:NONE
TRIGGER;VALUE=DATE-TIME:19760401T005545Z
X-WR-ALARMUID:8744D632-C9F8-483C-B095-590E0A3D2E39
UID:8744D632-C9F8-483C-B095-590E0A3D2E39
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_163_deleted_modification.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240820T210909Z
DTSTART;VALUE=DATE:20240729
DTEND;VALUE=DATE:20240805
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=3;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240820T210909Z
DTSTART;VALUE=DATE:20240819
DTEND;VALUE=DATE:20240822
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=3;BYDAY=MO
RECURRENCE-ID;VALUE=DATE:20240819
CREATED:20240729T132247Z
LAST-MODIFIED:20240729T132247Z
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240820T210908Z
DTSTART;VALUE=DATE:20240729
DTEND;VALUE=DATE:20240805
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=3;BYDAY=MO
EXDATE;VALUE=DATE:20240819
CREATED:20240311T051101Z
LAST-MODIFIED:20240729T133342Z
EXDATE;VALUE=DATE:20240819
SEQUENCE:2
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_164_duplicated_event.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240821T032819Z
DTSTART;VALUE=DATE:20240401
DTEND;VALUE=DATE:20240408
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=3;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240821T032820Z
DTSTART;VALUE=DATE:20240826
DTEND;VALUE=DATE:20240902
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=3;BYDAY=MO
RECURRENCE-ID;VALUE=DATE:20240826
CREATED:20240729T125457Z
LAST-MODIFIED:20240729T125457Z
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240821T032820Z
DTSTART;VALUE=DATE:20240826
DTEND;VALUE=DATE:20240902
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=3;BYDAY=MO
RECURRENCE-ID;VALUE=DATE:20240826
CREATED:20240729T125551Z
LAST-MODIFIED:20240729T125551Z
SEQUENCE:1
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_179_example.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
UID:19970901T130000Z-123403@example.com
DTSTAMP:19970901T130000Z
DTSTART;VALUE=DATE:19971102
SUMMARY:Our Blissful Anniversary
TRANSP:TRANSPARENT
CLASS:CONFIDENTIAL
CATEGORIES:ANNIVERSARY,PERSONAL,SPECIAL OCCASION
RRULE:FREQ=YEARLY
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_18_cancel_status.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20200206T210738Z
LAST-MODIFIED:20200206T210826Z
DTSTAMP:20200206T210826Z
UID:b65c2b5b-b785-4edc-9560-e0379036d1f2
SUMMARY:one is cancelled
RRULE:FREQ=DAILY;COUNT=3
DTSTART;TZID=Europe/Berlin:20200128T220000
DTEND;TZID=Europe/Berlin:20200128T230000
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
CREATED:20200206T210806Z
LAST-MODIFIED:20200206T210826Z
DTSTAMP:20200206T210826Z
UID:b65c2b5b-b785-4edc-9560-e0379036d1f2
SUMMARY:one is cancelled
STATUS:CANCELLED
RECURRENCE-ID;TZID=Europe/Berlin:20200129T220000
DTSTART;TZID=Europe/Berlin:20200129T220000
DTEND;TZID=Europe/Berlin:20200129T230000
LOCATION:
DESCRIPTION:
TRANSP:OPAQUE
CLASS:
SEQUENCE:2
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_186_invalid_trigger.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20241002T121843Z
LAST-MODIFIED:20241002T121918Z
DTSTAMP:20241002T121918Z
UID:cd047c29-d904-47eb-bdba-ab7abafee025
SUMMARY:event
DTSTART;TZID=Europe/London:20241004T110000
DTEND;TZID=Europe/London:20241004T120000
TRANSP:OPAQUE
X-MOZ-GENERATION:2
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:no trigger
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=TIME:230000
DESCRIPTION:invalid trigger
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:20241003T130000Z
DESCRIPTION:absolute trigger
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-P1D
DESCRIPTION:correct trigger
END:VALARM
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;RELATED=ENDE:-PT15M
DESCRIPTION:Invalid related
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_20_exdate_ignored.ics`

```ics
BEGIN:VCALENDAR
PRODID:+//IDN bitfire.at//DAVx5/2.6.1.1-gplay ical4j/2.2.6
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Berlin
TZURL:http://tzurl.org/zoneinfo/Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19810329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19961027T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
BEGIN:STANDARD
TZOFFSETFROM:+005328
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:18930401T000000
RDATE:18930401T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19160430T230000
RDATE:19160430T230000
RDATE:19170416T020000
RDATE:19180415T020000
RDATE:19400401T020000
RDATE:19430329T020000
RDATE:19440403T020000
RDATE:19450402T020000
RDATE:19460414T020000
RDATE:19470406T030000
RDATE:19480418T020000
RDATE:19490410T020000
RDATE:19800406T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19161001T010000
RDATE:19161001T010000
RDATE:19170917T030000
RDATE:19180916T030000
RDATE:19421102T030000
RDATE:19431004T030000
RDATE:19441002T030000
RDATE:19451118T030000
RDATE:19461007T030000
RDATE:19471005T030000
RDATE:19481003T030000
RDATE:19491002T030000
RDATE:19800928T030000
RDATE:19810927T030000
RDATE:19820926T030000
RDATE:19830925T030000
RDATE:19840930T030000
RDATE:19850929T030000
RDATE:19860928T030000
RDATE:19870927T030000
RDATE:19880925T030000
RDATE:19890924T030000
RDATE:19900930T030000
RDATE:19910929T030000
RDATE:19920927T030000
RDATE:19930926T030000
RDATE:19940925T030000
RDATE:19950924T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+0200
TZOFFSETTO:+0300
TZNAME:CEMT
DTSTART:19450524T010000
RDATE:19450524T010000
RDATE:19470511T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETFROM:+0300
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19450924T030000
RDATE:19450924T030000
RDATE:19470629T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0100
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19460101T000000
RDATE:19460101T000000
RDATE:19800101T000000
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTAMP:20191219T182547Z
UID:f0f31ddb-6918-46af-a5a1-0a7254fbce71
SEQUENCE:11
SUMMARY:Test
LOCATION:Example
DTSTART;TZID=Europe/Berlin:20191015T161500
DURATION:PT1H30M
RRULE:FREQ=WEEKLY;UNTIL=20200204T151459Z;BYDAY=TU;WKST=SU
EXDATE:20191015T141500Z,20191022T141500Z,20191105T151500Z,20191119T151500Z,
 20191126T151500Z,20191203T151500Z,20191217T151500Z,20191224T151500Z,201912
 31T151500Z
CLASS:PUBLIC
STATUS:CONFIRMED
CREATED:20191013T184131Z
X-MOZ-GENERATION:10
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_201_mixed_datetime_and_date.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART;VALUE=DATE:20230724
CREATED:20230606T153716Z
STATUS:CONFIRMED
SUMMARY:Congés
TRANSP:TRANSPARENT
DTSTAMP:20230704T085547Z
DTEND:20230817T000000Z
SEQUENCE:1
LAST-MODIFIED:20230731T161724Z
UID:19970901T130000Z-123403@example.com
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_201_test_matrix.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART;VALUE=DATE:20000101
DTEND;VALUE=DATE:20000102
UID:VEVENT-DATE-DATE
END:VEVENT
BEGIN:VTODO
DTSTART;VALUE=DATE:20000101
DUE;VALUE=DATE:20000102
UID:VTODO-DATE-DATE
END:VTOOD
BEGIN:VEVENT
DTSTART;VALUE=DATE:20000101
DTEND:20000102T040000
UID:VEVENT-DATE-DATETIME
END:VEVENT
BEGIN:VTODO
DTSTART;VALUE=DATE:20000101
DUE:20000102T040000
UID:VTODO-DATE-DATETIME
END:VTOOD
BEGIN:VEVENT
DTSTART;VALUE=DATE:20000101
DTEND:20000103T020000Z
UID:VEVENT-DATE-UTC
END:VEVENT
BEGIN:VTODO
DTSTART;VALUE=DATE:20000101
DUE:20000103T020000Z
UID:VTODO-DATE-UTC
END:VTOOD
BEGIN:VEVENT
DTSTART;VALUE=DATE:20000101
DURATION:P3D
UID:VEVENT-DATE-DAYS
END:VEVENT
BEGIN:VTODO
DTSTART;VALUE=DATE:20000101
DURATION:P3D
UID:VTODO-DATE-DAYS
END:VTOOD
BEGIN:VEVENT
DTSTART;VALUE=DATE:20000101
DURATION:PT10H
UID:VEVENT-DATE-HOURS
END:VEVENT
BEGIN:VTODO
DTSTART;VALUE=DATE:20000101
DURATION:PT10H
UID:VTODO-DATE-HOURS
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000
DTEND;VALUE=DATE:20000102
UID:VEVENT-DATETIME-DATE
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000
DUE;VALUE=DATE:20000102
UID:VTODO-DATETIME-DATE
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000
DTEND:20000102T040000
UID:VEVENT-DATETIME-DATETIME
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000
DUE:20000102T040000
UID:VTODO-DATETIME-DATETIME
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000
DTEND:20000103T020000Z
UID:VEVENT-DATETIME-UTC
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000
DUE:20000103T020000Z
UID:VTODO-DATETIME-UTC
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000
DURATION:P3D
UID:VEVENT-DATETIME-DAYS
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000
DURATION:P3D
UID:VTODO-DATETIME-DAYS
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000
DURATION:PT10H
UID:VEVENT-DATETIME-HOURS
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000
DURATION:PT10H
UID:VTODO-DATETIME-HOURS
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000Z
DTEND;VALUE=DATE:20000102
UID:VEVENT-UTC-DATE
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000Z
DUE;VALUE=DATE:20000102
UID:VTODO-UTC-DATE
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000Z
DTEND:20000102T040000
UID:VEVENT-UTC-DATETIME
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000Z
DUE:20000102T040000
UID:VTODO-UTC-DATETIME
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000Z
DTEND:20000103T020000Z
UID:VEVENT-UTC-UTC
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000Z
DUE:20000103T020000Z
UID:VTODO-UTC-UTC
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000Z
DURATION:P3D
UID:VEVENT-UTC-DAYS
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000Z
DURATION:P3D
UID:VTODO-UTC-DAYS
END:VTOOD
BEGIN:VEVENT
DTSTART:20000101T000000Z
DURATION:PT10H
UID:VEVENT-UTC-HOURS
END:VEVENT
BEGIN:VTODO
DTSTART:20000101T000000Z
DURATION:PT10H
UID:VTODO-UTC-HOURS
END:VTOOD
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_223_one_event_with_sequence.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J
SUMMARY:test1
SEQUENCE:0
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J2
SUMMARY:test2
SEQUENCE:1
DTSTART;TZID=Europe/Berlin:20190305T080000
DTEND;TZID=Europe/Berlin:20190305T083000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_223_thunderbird.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2025a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20250421T090544Z
LAST-MODIFIED:20250421T090624Z
DTSTAMP:20250421T090624Z
UID:b143dcdc-2154-49a8-abea-5c64310ebabd
SUMMARY:event
RRULE:FREQ=DAILY;UNTIL=20250427T080000Z
DTSTART;TZID=Europe/London:20250423T090000
DTEND;TZID=Europe/London:20250423T100000
TRANSP:OPAQUE
X-MOZ-GENERATION:4
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
CREATED:20250421T090602Z
LAST-MODIFIED:20250421T090607Z
DTSTAMP:20250421T090607Z
UID:b143dcdc-2154-49a8-abea-5c64310ebabd
SUMMARY:event
RECURRENCE-ID;TZID=Europe/London:20250424T090000
DTSTART;TZID=Europe/London:20250424T110000
DTEND;TZID=Europe/London:20250424T120000
TRANSP:OPAQUE
X-MOZ-GENERATION:4
SEQUENCE:2
END:VEVENT
BEGIN:VEVENT
CREATED:20250421T090607Z
LAST-MODIFIED:20250421T090624Z
DTSTAMP:20250421T090624Z
UID:b143dcdc-2154-49a8-abea-5c64310ebabd
SUMMARY:event
RECURRENCE-ID;TZID=Europe/London:20250425T090000
DTSTART;TZID=Europe/London:20250425T090000
DTEND;TZID=Europe/London:20250425T100000
TRANSP:OPAQUE
X-MOZ-GENERATION:4
SEQUENCE:3
LOCATION:new place
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_243_recurrence_id_is_not_identical_to_dtstart.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
SUMMARY:daily testing
DTSTART:20150901T080000
DTEND:20150901T100000
DTSTAMP:20250529T181439Z
UID:test1
RRULE:FREQ=DAILY
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_253_additional_recurrence_id.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240729
DTEND;VALUE=DATE:20240804
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO
RECURRENCE-ID;VALUE=DATE:20240729
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
END:VEVENT

BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240720;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240701T063743Z
SEQUENCE:2
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_253_edge_case_1.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240729
DTEND;VALUE=DATE:20240804
SUMMARY:event 1
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO
COMMENT:Modified RECURRENCE-ID to be included
RECURRENCE-ID;VALUE=DATE:20240715
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
END:VEVENT

BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:event 2
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240720;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240701T063743Z
SEQUENCE:2
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_253_recurrence_id_included.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240729
DTEND;VALUE=DATE:20240804
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO
RECURRENCE-ID;VALUE=DATE:20240715
CREATED:20240311T051101Z
LAST-MODIFIED:20240311T051101Z
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20240707T214014Z
DTSTART;VALUE=DATE:20240701
DTEND;VALUE=DATE:20240708
SUMMARY:test123
CATEGORIES:other
UID:111
ORGANIZER:aaa
RRULE:FREQ=WEEKLY;UNTIL=20240720;INTERVAL=2;BYDAY=MO
CREATED:20240311T051101Z
LAST-MODIFIED:20240701T063743Z
SEQUENCE:2
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_27_t1.ics`

```ics
BEGIN:VCALENDAR
METHOD:PUBLISH
PRODID:Microsoft Exchange Server 2010
VERSION:2.0
X-WR-CALNAME:Events
X-EVOLUTION-DATA-REVISION:2020-04-23T17:43:39.112248Z(2)
BEGIN:VTIMEZONE
TZID:W. Europe Standard Time
BEGIN:STANDARD
DTSTART:16010101T030000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:16010101T020000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
END:VTIMEZONE

BEGIN:VEVENT
UID:3bbe38c205956551730fc9233525fe268296ec02
DTSTAMP:20200423T174240Z
DTSTART;TZID=Europe/Berlin:
 20200426T140000
DTEND;TZID=Europe/Berlin:
 20200426T143000
SUMMARY:Reoccur
SEQUENCE:7
X-LIC-ERROR;X-LIC-ERRORTYPE=VALUE-PARSE-ERROR:No value for DESCRIPTION 
 property. Removing entire property:
CREATED:20200423T174316Z
LAST-MODIFIED:20200423T174339Z
X-LIC-ERROR;X-LIC-ERRORTYPE=VALUE-PARSE-ERROR:No value for DESCRIPTION 
 property. Removing entire property:
RRULE:FREQ=DAILY;UNTIL=20200429T000000
EXDATE:20200427T120000Z

END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_27_t2.ics`

```ics
BEGIN:VCALENDAR
METHOD:PUBLISH
PRODID:Microsoft Exchange Server 2010
VERSION:2.0
X-WR-CALNAME:Events
X-EVOLUTION-DATA-REVISION:2020-04-23T17:43:39.112248Z(2)
BEGIN:VTIMEZONE
TZID:W. Europe Standard Time
BEGIN:STANDARD
DTSTART:16010101T030000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:16010101T020000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
END:VTIMEZONE

BEGIN:VEVENT
UID:3bbe38c205956551730fc9233525fe268296ec02
DTSTAMP:20200423T174240Z
DTSTART;TZID=Europe/Berlin:
 20200426T140000
DTEND;TZID=Europe/Berlin:
 20200426T143000
SUMMARY:Reoccur
SEQUENCE:7
X-LIC-ERROR;X-LIC-ERRORTYPE=VALUE-PARSE-ERROR:No value for DESCRIPTION 
 property. Removing entire property:
CREATED:20200423T174316Z
LAST-MODIFIED:20200423T174339Z
X-LIC-ERROR;X-LIC-ERRORTYPE=VALUE-PARSE-ERROR:No value for DESCRIPTION 
 property. Removing entire property:
RRULE:FREQ=DAILY;UNTIL=20200429T000000Z
EXDATE:20200427T120000Z

END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_28_rrule_with_UTC_endinginZ.ics`

```ics
BEGIN:VCALENDAR
METHOD:PUBLISH
PRODID:Microsoft Exchange Server 2010
VERSION:2.0
X-WR-CALNAME:Calendar
BEGIN:VTIMEZONE
TZID:GMT Standard Time
BEGIN:STANDARD
DTSTART:16010101T020000
TZOFFSETFROM:+0100
TZOFFSETTO:+0000
RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=-1SU;BYMONTH=10
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:16010101T010000
TZOFFSETFROM:+0000
TZOFFSETTO:+0100
RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
DESCRIPTION:\n
RRULE:FREQ=WEEKLY;UNTIL=20200916T230000Z;INTERVAL=2;BYDAY=TH;WKST=MO
UID:040000008200E00074C5B7101A82E00800000000017E1BADC42ED601000000000000000
 010000000FBF1FBAE2E9FBC4D81F16854E2F4D51B
SUMMARY:Refuse black bin
DTSTART;VALUE=DATE:20200402
DTEND;VALUE=DATE:20200403
CLASS:PUBLIC
PRIORITY:5
DTSTAMP:20200525T073743Z
TRANSP:TRANSPARENT
STATUS:CONFIRMED
SEQUENCE:0
LOCATION:
X-MICROSOFT-CDO-APPT-SEQUENCE:0
X-MICROSOFT-CDO-BUSYSTATUS:FREE
X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY
X-MICROSOFT-CDO-ALLDAYEVENT:TRUE
X-MICROSOFT-CDO-IMPORTANCE:1
X-MICROSOFT-CDO-INSTTYPE:1
X-MICROSOFT-DONOTFORWARDMEETING:FALSE
X-MICROSOFT-DISALLOW-COUNTER:FALSE
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:\n
RRULE:FREQ=WEEKLY;UNTIL=20200923T230000Z;INTERVAL=2;BYDAY=TH;WKST=MO
UID:040000008200E00074C5B7101A82E00800000000C6B92310C52ED601000000000000000
 010000000605B5A30BB664D469D7A9A45CF7F2FB3
SUMMARY:Blue Recycle bin
DTSTART;VALUE=DATE:20200409
DTEND;VALUE=DATE:20200410
CLASS:PUBLIC
PRIORITY:5
DTSTAMP:20200525T073743Z
TRANSP:TRANSPARENT
STATUS:CONFIRMED
SEQUENCE:0
LOCATION:
X-MICROSOFT-CDO-APPT-SEQUENCE:0
X-MICROSOFT-CDO-BUSYSTATUS:FREE
X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY
X-MICROSOFT-CDO-ALLDAYEVENT:TRUE
X-MICROSOFT-CDO-IMPORTANCE:1
X-MICROSOFT-CDO-INSTTYPE:1
X-MICROSOFT-DONOTFORWARDMEETING:FALSE
X-MICROSOFT-DISALLOW-COUNTER:FALSE
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:\n
UID:040000008200E00074C5B7101A82E00800000000017E1BADC42ED601000000000000000
 010000000FBF1FBAE2E9FBC4D81F16854E2F4D51B
RECURRENCE-ID;TZID=GMT Standard Time:20200416T000000
SUMMARY:Refuse black bin
DTSTART;VALUE=DATE:20200417
DTEND;VALUE=DATE:20200418
CLASS:PUBLIC
PRIORITY:5
DTSTAMP:20200525T073743Z
TRANSP:TRANSPARENT
STATUS:CONFIRMED
SEQUENCE:0
LOCATION:
X-MICROSOFT-CDO-APPT-SEQUENCE:0
X-MICROSOFT-CDO-BUSYSTATUS:FREE
X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY
X-MICROSOFT-CDO-ALLDAYEVENT:TRUE
X-MICROSOFT-CDO-IMPORTANCE:1
X-MICROSOFT-CDO-INSTTYPE:3
X-MICROSOFT-DONOTFORWARDMEETING:FALSE
X-MICROSOFT-DISALLOW-COUNTER:FALSE
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:\n
UID:040000008200E00074C5B7101A82E00800000000017E1BADC42ED601000000000000000
 010000000FBF1FBAE2E9FBC4D81F16854E2F4D51B
RECURRENCE-ID;TZID=GMT Standard Time:20200528T000000
SUMMARY:Refuse black bin
DTSTART;VALUE=DATE:20200529
DTEND;VALUE=DATE:20200530
CLASS:PUBLIC
PRIORITY:5
DTSTAMP:20200525T073743Z
TRANSP:TRANSPARENT
STATUS:CONFIRMED
SEQUENCE:0
LOCATION:
X-MICROSOFT-CDO-APPT-SEQUENCE:0
X-MICROSOFT-CDO-BUSYSTATUS:FREE
X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY
X-MICROSOFT-CDO-ALLDAYEVENT:TRUE
X-MICROSOFT-CDO-IMPORTANCE:1
X-MICROSOFT-CDO-INSTTYPE:3
X-MICROSOFT-DONOTFORWARDMEETING:FALSE
X-MICROSOFT-DISALLOW-COUNTER:FALSE
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:\n
UID:040000008200E00074C5B7101A82E00800000000017E1BADC42ED601000000000000000
 010000000FBF1FBAE2E9FBC4D81F16854E2F4D51B
RECURRENCE-ID;TZID=GMT Standard Time:20200903T000000
SUMMARY:Refuse black bin
DTSTART;VALUE=DATE:20200904
DTEND;VALUE=DATE:20200905
CLASS:PUBLIC
PRIORITY:5
DTSTAMP:20200525T073743Z
TRANSP:TRANSPARENT
STATUS:CONFIRMED
SEQUENCE:0
LOCATION:
X-MICROSOFT-CDO-APPT-SEQUENCE:0
X-MICROSOFT-CDO-BUSYSTATUS:FREE
X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY
X-MICROSOFT-CDO-ALLDAYEVENT:TRUE
X-MICROSOFT-CDO-IMPORTANCE:1
X-MICROSOFT-CDO-INSTTYPE:3
X-MICROSOFT-DONOTFORWARDMEETING:FALSE
X-MICROSOFT-DISALLOW-COUNTER:FALSE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_36_recurrence_ID_format.ics`

```ics
BEGIN:VCALENDAR

BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20200910T140000
DTEND;TZID=Europe/Berlin:20200910T150000
RRULE:FREQ=WEEKLY
SEQUENCE:0
SUMMARY:Base event
UID:series 1
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20200917T140000
DTEND;TZID=Europe/Berlin:20200917T150000
RECURRENCE-ID:20200917T120000Z
SEQUENCE:1
SUMMARY:Modified event
UID:series 1
END:VEVENT


BEGIN:VEVENT
DTSTART;VALUE=DATE:20200907
DTEND;VALUE=DATE:20200908
RRULE:FREQ=WEEKLY
SEQUENCE:0
SUMMARY:Base event
UID:series 2
END:VEVENT

BEGIN:VEVENT
DTSTART;VALUE=DATE:20200914
DTEND;VALUE=DATE:20200915
RECURRENCE-ID:20200914
SEQUENCE:1
SUMMARY:Modified event 1
UID:series 2
END:VEVENT

BEGIN:VEVENT
DTSTART;VALUE=DATE:20200921
DTEND;VALUE=DATE:20200922
RECURRENCE-ID:20200921T000000Z
SEQUENCE:2
SUMMARY:Modified event 2
UID:series 2
END:VEVENT

END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_4_rrule_until.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
SUMMARY:blabla
DTSTART;TZID=Europe/London:20190801T140000
DTEND;TZID=Europe/London:20190801T150000
DTSTAMP:20190801T083416Z
UID:blabla
SEQUENCE:0
RRULE:FREQ=WEEKLY;UNTIL=20191023;BYDAY=TH;WKST=SU
CREATED:20190729T105342Z
DESCRIPTION:blabla
LAST-MODIFIED:20190801T064315Z
LOCATION:
STATUS:CONFIRMED
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_4_weidenrinde.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
UID:2334a952-f89f-4308-9639-fc22dc70519f
RRULE:FREQ=WEEKLY;UNTIL=20190830;INTERVAL=1;BYDAY=FR
SUMMARY:TEXT
DTSTART;VALUE=DATE:20190823
DTEND;VALUE=DATE:20190824
STATUS:CONFIRMED
CLASS:PUBLIC
X-MICROSOFT-CDO-ALLDAYEVENT:TRUE
X-MICROSOFT-CDO-INTENDEDSTATUS:OOF
TRANSP:OPAQUE
LAST-MODIFIED:20190814T093121Z
DTSTAMP:20190814T093121Z
SEQUENCE:0
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;RELATED=START:-PT5M
DESCRIPTION:Reminder
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_4.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20190613T171521Z
DTSTART;VALUE=DATE:20190124
DTEND;VALUE=DATE:20190125
SUMMARY:WfH
X-CONFLUENCE-CUSTOM-TYPE-ID:6972027e-37ba-4a3e-82cb-5690b51c4ab4
CATEGORIES:WFH
SUBCALENDAR-ID:7bdacef4-2d77-432b-bd52-10dffc67d4fb
PARENT-CALENDAR-ID:5552044f-86e9-4d75-b038-9779bccf7a96
PARENT-CALENDAR-NAME:
SUBSCRIPTION-ID:
SUBCALENDAR-TZ-ID:GB
SUBCALENDAR-NAME:Calendar name here
EVENT-ID:75697
EVENT-ALLDAY:true
CUSTOM-EVENTTYPE-ID:aaaaaaaa-37ba-4a3e-82cb-5690b51c4ab4
UID:20190119T053217Z--1927336845@domain.com
DESCRIPTION:
ORGANIZER;X-CONFLUENCE-USER-KEY=aaaaaaaaaaaaa4eb01585ecded610030;CN=Fred Blo
 ggs;CUTYPE=INDIVIDUAL:mailto:person@domain.com
RRULE:FREQ=WEEKLY;INTERVAL=1;BYDAY=TH
CREATED:20190119T053217Z
LAST-MODIFIED:20190216T121411Z
ATTENDEE;X-CONFLUENCE-USER-KEY=ff808181582474eb01585ecded610030;CN=Fred Blo
 ggs;CUTYPE=INDIVIDUAL:mailto:person@domain.com
EXDATE;VALUE=DATE:20190718
EXDATE;VALUE=DATE:20190314
EXDATE;VALUE=DATE:20190307
EXDATE;VALUE=DATE:20190228
EXDATE;VALUE=DATE:20190221
SEQUENCE:6
X-CONFLUENCE-SUBCALENDAR-TYPE:custom
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_44_double_event.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:agy35@gmail.com
X-WR-TIMEZONE:Europe/London
BEGIN:VEVENT
DTSTART;VALUE=DATE:20200814
DTEND;VALUE=DATE:20200815
DTSTAMP:20200819T200956Z
UID:42sftcvqfh1jj1uk9lfrsufsi@google.com
CREATED:20200819T200939Z
DESCRIPTION:
LAST-MODIFIED:20200819T200939Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:test2
TRANSP:TRANSPARENT
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_48_daylight_aware_repeats.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Horario sem-5
X-WR-TIMEZONE:Europe/Lisbon
BEGIN:VTIMEZONE
TZID:Europe/Lisbon
X-LIC-LOCATION:Europe/Lisbon
BEGIN:STANDARD
TZOFFSETFROM:+0100
TZOFFSETTO:+0000
TZNAME:WET
DTSTART:19701025T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+0000
TZOFFSETTO:+0100
TZNAME:WEST
DTSTART:19700329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
DTSTART;TZID=Europe/Lisbon:20200921T113000
DTEND;TZID=Europe/Lisbon:20200921T130000
RRULE:FREQ=WEEKLY;BYDAY=MO
DTSTAMP:20201026T103342Z
UID:EVENT2
CREATED:20200920T235116Z
DESCRIPTION:<p><a href="https://videoconf-colibri.zoom.us/j/93800310242?pwd
 =K3FBUVJUV2hrTm1OR2RWb0ZabTJkZz09" target="_blank">https://videoconf-colibr
 i.zoom.us/j/93800310242?pwd=K3FBUVJUV2hrTm1OR2RWb0ZabTJkZz09</a></p>
LAST-MODIFIED:20200920T235214Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:MDS-t
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_48_dst.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:School
X-WR-TIMEZONE:America/Chicago
BEGIN:VTIMEZONE
TZID:America/Chicago
X-LIC-LOCATION:America/Chicago
BEGIN:DAYLIGHT
TZOFFSETFROM:-0600
TZOFFSETTO:-0500
TZNAME:CDT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0500
TZOFFSETTO:-0600
TZNAME:CST
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20201116T081500
DTEND;TZID=America/Chicago:20201116T083000
RRULE:FREQ=WEEKLY;WKST=SU;INTERVAL=1;BYDAY=MO,TU,TH,FR
EXDATE;TZID=America/Chicago:20201127T081500
EXDATE;TZID=America/Chicago:20201126T081500
DTSTAMP:20201211T121206Z
UID:c4p6@google.com
CREATED:20201116T135538Z
LAST-MODIFIED:20201116T143825Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#1 
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20201113T141500Z
DTEND:20201113T143000Z
DTSTAMP:20201211T121206Z
UID:5dru@google.com
CREATED:20201113T154536Z
DESCRIPTION:
LAST-MODIFIED:20201113T154536Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#1 
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20201109T123000
DTEND;TZID=America/Chicago:20201109T124500
RRULE:FREQ=WEEKLY;BYDAY=MO
DTSTAMP:20201211T121206Z
UID:u81j@google.com
CREATED:20200925T001723Z
DESCRIPTION:
LAST-MODIFIED:20201105T102000Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#3
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20201106T123000
DTEND;TZID=America/Chicago:20201106T124500
RRULE:FREQ=WEEKLY;BYDAY=FR
EXDATE;TZID=America/Chicago:20201127T123000
EXDATE;TZID=America/Chicago:20201106T123000
DTSTAMP:20201211T121206Z
UID:mji2s@google.com
CREATED:20200925T001657Z
DESCRIPTION:
LAST-MODIFIED:20201105T101945Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#3
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20201105T123000
DTEND;TZID=America/Chicago:20201105T124500
RRULE:FREQ=WEEKLY;BYDAY=TH
EXDATE;TZID=America/Chicago:20201126T123000
EXDATE;TZID=America/Chicago:20201112T123000
DTSTAMP:20201211T121206Z
UID:7l8ium@google.com
CREATED:20201006T173925Z
DESCRIPTION:
LAST-MODIFIED:20201105T101904Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#3
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20201103T123000
DTEND;TZID=America/Chicago:20201103T124500
RRULE:FREQ=WEEKLY;BYDAY=TU
DTSTAMP:20201211T121206Z
UID:m0lbs@google.com
CREATED:20200925T002247Z
DESCRIPTION:
LAST-MODIFIED:20201103T132721Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#3
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20200925T141500
DTEND;TZID=America/Chicago:20200925T143000
RRULE:FREQ=WEEKLY;WKST=MO
EXDATE;TZID=America/Chicago:20201127T141500
EXDATE;TZID=America/Chicago:20201106T141500
EXDATE;TZID=America/Chicago:20201023T141500
DTSTAMP:20201211T121206Z
UID:m4dpn70@google.com
CREATED:20200924T232319Z
DESCRIPTION:
LAST-MODIFIED:20200925T002438Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#4
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20200925T101500
DTEND;TZID=America/Chicago:20200925T103000
RRULE:FREQ=WEEKLY;WKST=MO
EXDATE;TZID=America/Chicago:20201127T101500
EXDATE;TZID=America/Chicago:20201023T101500
DTSTAMP:20201211T121206Z
UID:p1lc8@google.com
CREATED:20200924T232437Z
DESCRIPTION:
LAST-MODIFIED:20200925T002405Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#2
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20200928T101500
DTEND;TZID=America/Chicago:20200928T103000
RRULE:FREQ=WEEKLY;WKST=SU;INTERVAL=1;BYDAY=MO
DTSTAMP:20201211T121206Z
UID:m4b9nckq@google.com
CREATED:20200924T232601Z
DESCRIPTION:
LAST-MODIFIED:20200925T002309Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#2
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20201103T141500
DTEND;TZID=America/Chicago:20201103T143000
RRULE:FREQ=WEEKLY;BYDAY=TU
DTSTAMP:20201211T121206Z
UID:2n0o@google.com
CREATED:20200925T002208Z
DESCRIPTION:
LAST-MODIFIED:20200925T002208Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#4
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20200929T101500
DTEND;TZID=America/Chicago:20200929T103000
RRULE:FREQ=WEEKLY;WKST=SU;BYDAY=TU
DTSTAMP:20201211T121206Z
UID:2ohv@google.com
CREATED:20200925T001837Z
DESCRIPTION:
LAST-MODIFIED:20200925T002133Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#2
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20201001T101500
DTEND;TZID=America/Chicago:20201001T103000
RRULE:FREQ=WEEKLY;WKST=SU;BYDAY=TH
EXDATE;TZID=America/Chicago:20201126T101500
EXDATE;TZID=America/Chicago:20201112T101500
DTSTAMP:20201211T121206Z
UID:29kb@google.com
CREATED:20200925T001940Z
DESCRIPTION:
LAST-MODIFIED:20200925T002109Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event#2
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20200915T081500
DTEND;TZID=America/Chicago:20200915T083000
RRULE:FREQ=WEEKLY;UNTIL=20200923T045959Z;BYDAY=FR,MO,TH,TU,WE
EXDATE;TZID=America/Chicago:20200916T081500
DTSTAMP:20201211T121206Z
UID:p1lg@google.com
CREATED:20200915T115822Z
DESCRIPTION:
LAST-MODIFIED:20200916T120239Z
LOCATION:
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Event#1 
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_61_time_zone_error.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Atlassian Confluence//Calendar Plugin 1.0//EN
VERSION:2.0
CALSCALE:GREGORIAN
X-WR-CALNAME:danl-test
X-WR-CALDESC:
X-WR-TIMEZONE:America/Los_Angeles
X-MIGRATED-FOR-USER-KEY:true
METHOD:PUBLISH
X-CONFLUENCE-CUSTOM-EVENT-TYPE:false
BEGIN:VTIMEZONE
TZID:America/Los_Angeles
TZURL:http://tzurl.org/zoneinfo/America/Los_Angeles
X-LIC-LOCATION:America/Los_Angeles
UID:20211216T020534Z-1334061273@confluence.sd.apple.com
SEQUENCE:0
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
DTSTART:20070311T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:20071104T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
BEGIN:STANDARD
TZOFFSETFROM:-075258
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:18831118T120702
RDATE:18831118T120702
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
DTSTART:19180331T020000
RDATE:19180331T020000
RDATE:19190330T020000
RDATE:19480314T020100
RDATE:19500430T010000
RDATE:19510429T010000
RDATE:19520427T010000
RDATE:19530426T010000
RDATE:19540425T010000
RDATE:19550424T010000
RDATE:19560429T010000
RDATE:19570428T010000
RDATE:19580427T010000
RDATE:19590426T010000
RDATE:19600424T010000
RDATE:19610430T010000
RDATE:19620429T010000
RDATE:19630428T010000
RDATE:19640426T010000
RDATE:19650425T010000
RDATE:19660424T010000
RDATE:19670430T020000
RDATE:19680428T020000
RDATE:19690427T020000
RDATE:19700426T020000
RDATE:19710425T020000
RDATE:19720430T020000
RDATE:19730429T020000
RDATE:19740106T020000
RDATE:19750223T020000
RDATE:19760425T020000
RDATE:19770424T020000
RDATE:19780430T020000
RDATE:19790429T020000
RDATE:19800427T020000
RDATE:19810426T020000
RDATE:19820425T020000
RDATE:19830424T020000
RDATE:19840429T020000
RDATE:19850428T020000
RDATE:19860427T020000
RDATE:19870405T020000
RDATE:19880403T020000
RDATE:19890402T020000
RDATE:19900401T020000
RDATE:19910407T020000
RDATE:19920405T020000
RDATE:19930404T020000
RDATE:19940403T020000
RDATE:19950402T020000
RDATE:19960407T020000
RDATE:19970406T020000
RDATE:19980405T020000
RDATE:19990404T020000
RDATE:20000402T020000
RDATE:20010401T020000
RDATE:20020407T020000
RDATE:20030406T020000
RDATE:20040404T020000
RDATE:20050403T020000
RDATE:20060402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:19181027T020000
RDATE:19181027T020000
RDATE:19191026T020000
RDATE:19450930T020000
RDATE:19490101T020000
RDATE:19500924T020000
RDATE:19510930T020000
RDATE:19520928T020000
RDATE:19530927T020000
RDATE:19540926T020000
RDATE:19550925T020000
RDATE:19560930T020000
RDATE:19570929T020000
RDATE:19580928T020000
RDATE:19590927T020000
RDATE:19600925T020000
RDATE:19610924T020000
RDATE:19621028T020000
RDATE:19631027T020000
RDATE:19641025T020000
RDATE:19651031T020000
RDATE:19661030T020000
RDATE:19671029T020000
RDATE:19681027T020000
RDATE:19691026T020000
RDATE:19701025T020000
RDATE:19711031T020000
RDATE:19721029T020000
RDATE:19731028T020000
RDATE:19741027T020000
RDATE:19751026T020000
RDATE:19761031T020000
RDATE:19771030T020000
RDATE:19781029T020000
RDATE:19791028T020000
RDATE:19801026T020000
RDATE:19811025T020000
RDATE:19821031T020000
RDATE:19831030T020000
RDATE:19841028T020000
RDATE:19851027T020000
RDATE:19861026T020000
RDATE:19871025T020000
RDATE:19881030T020000
RDATE:19891029T020000
RDATE:19901028T020000
RDATE:19911027T020000
RDATE:19921025T020000
RDATE:19931031T020000
RDATE:19941030T020000
RDATE:19951029T020000
RDATE:19961027T020000
RDATE:19971026T020000
RDATE:19981025T020000
RDATE:19991031T020000
RDATE:20001029T020000
RDATE:20011028T020000
RDATE:20021027T020000
RDATE:20031026T020000
RDATE:20041031T020000
RDATE:20051030T020000
RDATE:20061029T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PWT
DTSTART:19420209T020000
RDATE:19420209T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETFROM:-0700
TZOFFSETTO:-0700
TZNAME:PPT
DTSTART:19450814T160000
RDATE:19450814T160000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0800
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:19460101T000000
RDATE:19460101T000000
RDATE:19670101T000000
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTAMP:20211216T020448Z
DTSTART;VALUE=DATE:20211215
DTEND;VALUE=DATE:20211216
SUMMARY:test
CATEGORIES:other
SUBCALENDAR-ID:1cfd6797-ae26-4858-b13a-eac08fa24d7d
PARENT-CALENDAR-ID:13e26edc-772b-44ba-9dfb-02a11f7f9825
PARENT-CALENDAR-NAME:
SUBSCRIPTION-ID:
SUBCALENDAR-TZ-ID:America/Los_Angeles
SUBCALENDAR-NAME:danl-test
EVENT-ID:89058
EVENT-ALLDAY:true
UID:20211215T205931Z-1325586105@confluence.sd.apple.com
DESCRIPTION:test event
ORGANIZER:X-CONFLUENCE-USER-KEY=8a4a8a8e5418da4e015496587b6d0067;CN=Danie
l Latham;CUTYPE=INDIVIDUAL:mailto:dlatham@apple.com
CREATED:20211215T183642Z
LAST-MODIFIED:20211215T213515Z
ATTENDEE:X-CONFLUENCE-USER-KEY=8a4a8a8e5418da4e015496587b6d0067;CN=Daniel
 Latham;CUTYPE=INDIVIDUAL:mailto:dlatham@apple.com
SEQUENCE:5
X-CONFLUENCE-SUBCALENDAR-TYPE:other
TRANSP:TRANSPARENT
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_62_moved_event_2.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Test Calendar
X-WR-TIMEZONE:Australia/Sydney
BEGIN:VTIMEZONE
TZID:Australia/Sydney
X-LIC-LOCATION:Australia/Sydney
BEGIN:STANDARD
TZOFFSETFROM:+1100
TZOFFSETTO:+1000
TZNAME:AEST
DTSTART:19700405T030000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=1SU
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+1000
TZOFFSETTO:+1100
TZNAME:AEDT
DTSTART:19701004T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
DTSTART;TZID=Australia/Sydney:20230808T140000
DTEND;TZID=Australia/Sydney:20230808T150000
RRULE:FREQ=WEEKLY;WKST=SU;UNTIL=20230828T135959Z;BYDAY=TU
DTSTAMP:20230629T040023Z
UID:7v3ju5ft4je5iq18nfdk2s3spk@google.com
CREATED:20230629T035454Z
LAST-MODIFIED:20230629T035851Z
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Datetime
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Australia/Sydney:20230814T140000
DTEND;TZID=Australia/Sydney:20230814T150000
DTSTAMP:20230629T040023Z
UID:7v3ju5ft4je5iq18nfdk2s3spk@google.com
RECURRENCE-ID;TZID=Australia/Sydney:20230815T140000
CREATED:20230629T035454Z
LAST-MODIFIED:20230629T035851Z
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Datetime
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20230810
DTEND;VALUE=DATE:20230811
RRULE:FREQ=WEEKLY;WKST=SU;UNTIL=20230830;BYDAY=TH
DTSTAMP:20230629T040023Z
UID:6ep37v20d728v14rcgn17v9is6@google.com
CREATED:20230629T035522Z
LAST-MODIFIED:20230629T035854Z
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:All Day
TRANSP:TRANSPARENT
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20230816
DTEND;VALUE=DATE:20230817
DTSTAMP:20230629T040023Z
UID:6ep37v20d728v14rcgn17v9is6@google.com
RECURRENCE-ID;VALUE=DATE:20230817
CREATED:20230629T035522Z
LAST-MODIFIED:20230629T035854Z
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:All Day
TRANSP:TRANSPARENT
END:VEVENT
END:VCALENDAR


```

### `recurring_ical_events/test/calendars/issue_62_moved_event.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Partyborn Zeitgeist
X-WR-TIMEZONE:Europe/Berlin
X-WR-CALDESC:Alle Events des Zeitgeist Paderborn für den Partyborn Partyala
 rm\nhttps://partyborn.de/partyalarm
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20211217T213000
DTSTAMP:20211218T004508Z
UID:38m812jicsrer5gorh3mlp7qhc@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20211231T213000
CREATED:20211218T004036Z
DESCRIPTION:Jeden letzten Freitag im Monat <a href="https://www.instagram.c
 om/p/CWwxmqbKXsC/">https://www.instagram.com/p/CWwxmqbKXsC/</a>
LAST-MODIFIED:20211218T004234Z
LOCATION:
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:Karaoke
TRANSP:TRANSPARENT
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20211126T213000
DTEND;TZID=Europe/Berlin:20211126T213000
RRULE:FREQ=MONTHLY;BYDAY=-1FR
DTSTAMP:20211218T004508Z
UID:38m812jicsrer5gorh3mlp7qhc@google.com
CREATED:20211218T004036Z
DESCRIPTION:Jeden letzten Freitag im Monat <a href="https://www.instagram.c
 om/p/CWwxmqbKXsC/">https://www.instagram.com/p/CWwxmqbKXsC/</a>
LAST-MODIFIED:20211218T004214Z
LOCATION:
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:Karaoke
TRANSP:TRANSPARENT
END:VEVENT
END:VCALENDAR
```

### `recurring_ical_events/test/calendars/issue_75_range_parameter.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:RESERVAS 1.0//EN
BEGIN:VEVENT
UID:210
DTSTART:20240901T120000Z
DTEND:20240901T140000Z
RRULE:FREQ=DAILY;INTERVAL=2;UNTIL=20250920
RDATE:20240914T090000Z
SEQUENCE:0
SUMMARY:ORIGINAL EVENT
DESCRIPTION: 2 hours long
END:VEVENT
BEGIN:VEVENT
UID:210
RECURRENCE-ID;RANGE=THISANDFUTURE:20240913T120000Z
DTSTART:20240913T090000Z
DTEND:20240913T160000Z
SEQUENCE:1
SUMMARY:MODIFIED EVENT
DESCRIPTION: move -3h, make 7 hours long
END:VEVENT
BEGIN:VEVENT
UID:210
RECURRENCE-ID:20240915T120000Z
DTSTART:20240915T170000Z
DTEND:20240915T190000Z
SEQUENCE:1
SUMMARY:MODIFIED EVENT
DESCRIPTION: move +5h, 2 hours long
END:VEVENT
BEGIN:VEVENT
UID:210
RECURRENCE-ID;RANGE=THISANDFUTURE:20240921T120000Z
DTSTART:20240922T142200Z
DTEND:20240922T161300Z
SEQUENCE:1
SUMMARY:EDITED EVENT
DESCRIPTION: moved +1 day +2h +22min, 1 hour 51min long
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_86_x_wr_timezone_without_time_zone_in_dt.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:manually_generated
X-WR-TIMEZONE:Europe/Brussels
X-WR-CALNAME:MyCalendar
X-WR-CALDESC:Description of calendar
BEGIN:VEVENT
UID:match_1025179
DTSTAMP:20210911T014015Z
DESCRIPTION:Summary
DTSTART:20210916T210000
DTEND:20210916T224500
SUMMARY:Summary
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_97_simple_journal.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Example Corp.//CalDAV Client//EN
BEGIN:VJOURNAL
UID:19920901T130000Z-123409@host.com
DTSTAMP:19920901T130000Z
DTSTART:19920420
SUMMARY:Yearly Income Tax Report
DESCRIPTION:We made it this year too.  Probably.  What's the point of a recurring journal entry?  Journals are supposed to describe past events, aren't they?
RRULE:FREQ=YEARLY
CLASS:CONFIDENTIAL
CATEGORIES:FAMILY,FINANCE
PRIORITY:1
END:VJOURNAL
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_97_simple_todo.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Example Corp.//CalDAV Client//EN
BEGIN:VTODO
UID:19920901T130000Z-123408@host.com
DTSTAMP:19920901T130000Z
DTSTART:19920415T133000Z
DUE:19920516T045959Z
SUMMARY:Yearly Income Tax Preparation
RRULE:FREQ=YEARLY
CLASS:CONFIDENTIAL
CATEGORIES:FAMILY,FINANCE
PRIORITY:1
END:VTODO
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/issue_97_todo_nodtstart.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Example Corp.//CalDAV Client//EN
BEGIN:VTODO
UID:19920901T130000Z-123408@host.com
DTSTAMP:19920901T130000Z
DUE:19920516T045959Z
SUMMARY:Yearly Income Tax Preparation
RRULE:FREQ=YEARLY
CLASS:CONFIDENTIAL
CATEGORIES:FAMILY,FINANCE
PRIORITY:1
END:VTODO
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/machbar_16_feb_2019.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:machBar - Öffentlich
X-WR-TIMEZONE:Europe/Berlin
X-WR-CALDESC:Alle öffentlichen Termine der Potsdamer machBar dem fabLab vom
  Wissenschaftsladen Potsdam e.V.
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTART:20190228T190000Z
DTEND:20190228T200000Z
DTSTAMP:20190305T185732Z
UID:4pudsugalsbuqetcfdns8demti@google.com
CREATED:20190226T145646Z
DESCRIPTION:Kennenlernen der machBar facilities zum Thema Bioökonomie
LAST-MODIFIED:20190226T145646Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:"Bioökonomie-Tag"
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190304T140000
DTEND;TZID=Europe/Berlin:20190304T180000
RRULE:FREQ=WEEKLY;WKST=SU;COUNT=6;BYDAY=MO,TU,WE
DTSTAMP:20190305T185732Z
UID:37jkbgv9regint2hqhlmd9risn@google.com
CREATED:20190226T140104Z
DESCRIPTION:
LAST-MODIFIED:20190226T140529Z
LOCATION:
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:Open Health HACKademy - freie Termine
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20190309T083000Z
DTEND:20190310T160000Z
DTSTAMP:20190305T185732Z
UID:3po7fj93mq7keq9qgqcckcm6la@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CREATED:20190226T135643Z
DESCRIPTION:In machBar und offenem Atelier\nhttps://be-able.info/de/projekt
 e/HACKademy/
LAST-MODIFIED:20190226T140317Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Open Health HACKademy
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190228T083000
DTEND;TZID=Europe/Berlin:20190228T143000
RRULE:FREQ=WEEKLY;BYDAY=TH
EXDATE;TZID=Europe/Berlin:20190307T083000
DTSTAMP:20190305T185732Z
UID:7g6502aejkun96i5fenfu6hvc1@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CREATED:20190226T134933Z
DESCRIPTION:Mario mit einer Klasse der Montessori Schule
LAST-MODIFIED:20190226T140308Z
LOCATION:machBar
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Montessori Schulklasse
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190301T083000
DTEND;TZID=Europe/Berlin:20190301T143000
RRULE:FREQ=WEEKLY;BYDAY=FR
EXDATE;TZID=Europe/Berlin:20190308T083000
DTSTAMP:20190305T185732Z
UID:1djkkpk5edlt8ocfscsd8a52et@google.com
CREATED:20190226T134824Z
DESCRIPTION:Mario mit einer Kasse der Montessori Schule
LAST-MODIFIED:20190226T140257Z
LOCATION:machBar
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:Montessori Schulklasse
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20190316T083000Z
DTEND:20190317T180000Z
DTSTAMP:20190305T185732Z
UID:0d9qpsgmsglque6b3tfquqo805@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CREATED:20190226T135810Z
DESCRIPTION:In machBar und Offenem Atelier\nhttps://be-able.info/de/projekt
 e/HACKademy/
LAST-MODIFIED:20190226T140220Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Open Health HACKademy
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20190301T163000Z
DTEND:20190303T170000Z
DTSTAMP:20190305T185732Z
UID:5v18ih724kes1sf1eeu27dsq5n@google.com
CREATED:20190226T135342Z
DESCRIPTION:HACKademy in machBar und offenem Atelier\nhttps://be-able.info/
 de/projekte/HACKademy/
LAST-MODIFIED:20190226T135342Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Open Health HACKademy
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20190228T140000Z
DTEND:20190228T170000Z
DTSTAMP:20190305T185732Z
UID:4mm2ak3in2j3pllqdk1ubtbp9p@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CREATED:20190226T134810Z
DESCRIPTION:\nWorkshop: Hemp as a sustainable material in a bio-based socie
 ty\n-closed workshop-\nyou can join us afterwards from 18:30 to 21:00 @open
 Lab- machBar Potsdam
LAST-MODIFIED:20190226T135130Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Workshop DiReBio
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190213T190000
DTEND;TZID=Europe/Berlin:20190213T210000
RRULE:FREQ=WEEKLY;BYDAY=WE
DTSTAMP:20190305T185732Z
UID:7uartkcnhf0elbvs8md0itrf6c@google.com
CREATED:20180430T161057Z
DESCRIPTION:Alle Lebensformen die sich den Werten und Inhalten der Hackeret
 hik und der Galaktischen Gemeinschaft verbunden fühlen sind eingeladen zum 
 Chaostreff! <br>Von Comics\, Code bis Netzpolitik und Datensparsamkeit steh
 en verschiedenste Themen im Fokus.<br>Hackt mit!<br><br><a href="http://www
 .ccc-p.org" target="_blank" id="ow314" __is_owner="true">www.ccc-p.org</a>
LAST-MODIFIED:20190212T124850Z
LOCATION:
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Chaostreff - CCCP
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190116T190000
DTEND;TZID=Europe/Berlin:20190116T210000
RRULE:FREQ=WEEKLY;UNTIL=20190212T225959Z;INTERVAL=2;BYDAY=WE
DTSTAMP:20190305T185732Z
UID:4m856r43sj4i6g0vat9dn4gtui_R20190116T180000@google.com
CREATED:20180430T161057Z
DESCRIPTION:Alle Lebensformen die sich den Werten und Inhalten der Hackeret
 hik und der Galaktischen Gemeinschaft verbunden fühlen sind eingeladen zum 
 Chaostreff! <br>Von Comics\, Code bis Netzpolitik und Datensparsamkeit steh
 en verschiedenste Themen im Fokus.<br>Hackt mit!<br><br><a href="http://www
 .ccc-p.de" id="ow328" __is_owner="true">www.ccc-p.de</a>
LAST-MODIFIED:20190212T124850Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Chaostreff - CCCP
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180425T190000
DTEND;TZID=Europe/Berlin:20180425T210000
RRULE:FREQ=WEEKLY;UNTIL=20190115T225959Z;INTERVAL=2;BYDAY=WE
DTSTAMP:20190305T185732Z
UID:4m856r43sj4i6g0vat9dn4gtui@google.com
CREATED:20180430T161057Z
DESCRIPTION:Alle Lebensformen die sich den Werten und Inhalten der Hackeret
 hik und der Galaktischen Gemeinschaft verbunden fühlen sind eingeladen zum 
 Chaostreff! \nVon Comics\, Code bis Netzpolitik und Datensparsamkeit stehen
  verschiedenste Themen im Fokus.\nHackt mit!\n\nhttp://chaostreff-potsdam.g
 ithub.io
LAST-MODIFIED:20190212T124850Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Chaostreff
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180212T150000
DTEND;TZID=Europe/Berlin:20180212T180000
RRULE:FREQ=WEEKLY;UNTIL=20180729T215959Z;BYDAY=MO
DTSTAMP:20190305T185732Z
UID:3gp01pk48e95mmonkqef47qtpb_R20180212T140000@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:#tec (Hashtec) ist ein Jugendlab\, welches Neugier auf Wissen u
 nd die Makerszene für sich schafft und weiter entwickelt und probiert.
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#TEC - Jugendlab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180115T150000
DTEND;TZID=Europe/Berlin:20180115T180000
RRULE:FREQ=WEEKLY;UNTIL=20180211T225959Z;BYDAY=MO
DTSTAMP:20190305T185732Z
UID:3gp01pk48e95mmonkqef47qtpb@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:#tec (Hashtec) ist ein Jugendlab\, welches Neugier auf Wissen u
 nd die Makerszene für sich schafft und weiter entwickelt und probiert.
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#tec - Jugendlab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190117T150000
DTEND;TZID=Europe/Berlin:20190117T170000
RRULE:FREQ=WEEKLY;BYDAY=TH
DTSTAMP:20190305T185732Z
UID:ctfr0ikn17n8okmi83au0qfuhs@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:\nJetzt neu immer Donnerstags!\n#tec (Hashtec) ist ein Treffpun
 kt für Jugendliche\, welche sich kreativ mit Technik beschäftigen wollen. G
 emeinsam hacken\, programmieren lernen und Spaß haben steht an erster Stell
 e. \n\nIhr braucht keine Clubmitgliedschaft und es ist kostenfrei. Kommt vo
 rbei!\n\nhttps://hashtec-potsdam.github.io/
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:#TEC - für Jugendliche
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180910T150000
DTEND;TZID=Europe/Berlin:20180910T170000
RRULE:FREQ=WEEKLY;UNTIL=20190113T225959Z;BYDAY=MO
DTSTAMP:20190305T185732Z
UID:3gp01pk48e95mmonkqef47qtpb_R20180910T130000@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:#tec (Hashtec) ist ein Treffpunkt für Jugendliche\, welche sich
  mit Technik kreativ beschäftigen wollen. Gemeinsam hacken und Spaß haben s
 teht an erster Stelle. \n\nWir erheben keine Clubmitgliedschaften und sind 
 kostenfrei.\n\nhttps://hashtec-potsdam.github.io/
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#TEC - für Jugendliche
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180730T150000
DTEND;TZID=Europe/Berlin:20180730T170000
RRULE:FREQ=WEEKLY;UNTIL=20180909T215959Z;BYDAY=MO
DTSTAMP:20190305T185732Z
UID:3gp01pk48e95mmonkqef47qtpb_R20180730T130000@google.com
CLASS:PUBLIC
CREATED:20180114T090731Z
DESCRIPTION:#tec (Hashtec) ist ein Jugendlab\, welches Neugier auf Wissen u
 nd die Makerszene für sich schafft und weiter entwickelt und probiert.\n\nh
 ttps://hashtec-potsdam.github.io/
LAST-MODIFIED:20190114T135423Z
LOCATION:Haus 5 - machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#TEC - Fällt aus bis September
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190622T110000
DTEND;TZID=Europe/Berlin:20190622T150000
RRULE:FREQ=DAILY;COUNT=1
DTSTAMP:20190305T185732Z
UID:4oe7e40bbf492tbp6eilvg9naj@google.com
CREATED:20181108T044402Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044402Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190525T110000
DTEND;TZID=Europe/Berlin:20190525T150000
RRULE:FREQ=DAILY;COUNT=1
DTSTAMP:20190305T185732Z
UID:1p5ldilgr9dtls02s3k196pbnl@google.com
CREATED:20181108T044347Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044347Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190427T110000
DTEND;TZID=Europe/Berlin:20190427T150000
RRULE:FREQ=DAILY;COUNT=1
DTSTAMP:20190305T185732Z
UID:4h75rere9lgo3atvkc810587jp@google.com
CREATED:20181108T044331Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044331Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190323T110000
DTEND;TZID=Europe/Berlin:20190323T150000
RRULE:FREQ=DAILY;COUNT=1
DTSTAMP:20190305T185732Z
UID:3r2hi43bkab7h35rb13eu3t6b6@google.com
CREATED:20181108T044307Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044307Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190224T110000
DTEND;TZID=Europe/Berlin:20190224T150000
DTSTAMP:20190305T185732Z
UID:ome5r9735mpdoo3n6lpf8oi0c4@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20190216T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044241Z
LOCATION:Treffpunkt Freizeit\, Am Neuen Garten 64\, 14469 Potsdam\, Deutsch
 land
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190127T110000
DTEND;TZID=Europe/Berlin:20190127T150000
DTSTAMP:20190305T185732Z
UID:ome5r9735mpdoo3n6lpf8oi0c4@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20190119T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044241Z
LOCATION:Treffpunkt Freizeit\, Am Neuen Garten 64\, 14469 Potsdam\, Deutsch
 land
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20181208T110000
DTEND;TZID=Europe/Berlin:20181208T150000
DTSTAMP:20190305T185732Z
UID:ome5r9735mpdoo3n6lpf8oi0c4@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20181215T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044241Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20181117T110000
DTEND;TZID=Europe/Berlin:20181117T150000
RRULE:FREQ=MONTHLY;UNTIL=20190315T225959Z;BYDAY=3SA
DTSTAMP:20190305T185732Z
UID:ome5r9735mpdoo3n6lpf8oi0c4@google.com
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044241Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20190112T110000
DTEND;TZID=Europe/Berlin:20190112T150000
RRULE:FREQ=MONTHLY;UNTIL=20190308T225959Z;BYDAY=2SA
DTSTAMP:20190305T185732Z
UID:3761q5bsqtnh74ckejfgfrailt@google.com
CREATED:20181108T043904Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20181108T044217Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20170912T180000
DTEND;TZID=Europe/Berlin:20170912T210000
RRULE:FREQ=WEEKLY;UNTIL=20181008T215959Z;INTERVAL=2;BYDAY=TU
EXDATE;TZID=Europe/Berlin:20171121T180000
DTSTAMP:20190305T185732Z
UID:5m2ic2qqn1fo43ebfp7ucovj6p@google.com
CLASS:PUBLIC
CREATED:20170908T082339Z
DESCRIPTION:Öffentliches Treffen des Freifunk Potsdam e.V.\n
LAST-MODIFIED:20180925T164518Z
LOCATION:Seminarraum
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Freifunktreffen
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20181020T110000
DTEND;TZID=Europe/Berlin:20181020T150000
DTSTAMP:20190305T185732Z
UID:52uuaoruefesorque1gpjabr6t@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20181027T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20180607T182041Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180922T110000
DTEND;TZID=Europe/Berlin:20180922T150000
DTSTAMP:20190305T185732Z
UID:52uuaoruefesorque1gpjabr6t@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20180929T110000
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20180607T182041Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180630T110000
DTEND;TZID=Europe/Berlin:20180630T150000
RRULE:FREQ=MONTHLY;UNTIL=20181123T225959Z;BYDAY=-1SA
EXDATE;TZID=Europe/Berlin:20180825T110000
EXDATE;TZID=Europe/Berlin:20180728T110000
DTSTAMP:20190305T185732Z
UID:52uuaoruefesorque1gpjabr6t@google.com
CREATED:20180607T181722Z
DESCRIPTION:Gemeinsam reparieren - Hilfe zur Selbsthilfe
LAST-MODIFIED:20180607T182041Z
LOCATION:Stadt- u. Landesbibliothek Potsdam im Bildungsforum\, Am Kanal 47\
 , 14467 Potsdam\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB-onTour: repairCafé
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20180526
DTEND;VALUE=DATE:20180528
DTSTAMP:20190305T185732Z
UID:05b6u5vfdih0cdr6q3msgemss2@google.com
CREATED:20180503T161745Z
DESCRIPTION:Das mobile Fablab auf der Maker Fair.
LAST-MODIFIED:20180503T161745Z
LOCATION:FEZ-Berlin\, Str. zum FEZ 2\, 12459 Berlin\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:mB - OnTour: Maker Fair
TRANSP:TRANSPARENT
END:VEVENT
BEGIN:VEVENT
DTSTART:20180530T070000Z
DTEND:20180530T100000Z
DTSTAMP:20190305T185732Z
UID:4ajj1k6g3vbq38rrbfe653nge4@google.com
CREATED:20180503T161414Z
DESCRIPTION:Hauptziel des Projektes FABULANDLABS ist es\, dass Betroffene s
 ich ihre Hilfsmittel mit Kostengünstigen Technologien in offen zugänglichen
  Werkstätten - sogenannten FabLabs- selbst anpassen oder herstellen.
LAST-MODIFIED:20180503T161414Z
LOCATION:Seminarrraum Haus 5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Fabulandlabs Ideen Workshop
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20181014T080000Z
DTEND:20181014T160000Z
DTSTAMP:20190305T185732Z
UID:3akehbu0brcbrno9njieufcan4@google.com
CREATED:20180430T163433Z
DESCRIPTION:Angebot im Rahmen des Eltern Medien Tag von der Medienwerkstatt
LAST-MODIFIED:20180430T163433Z
LOCATION:Treffpunkt Freizeit\, Am Neuen Garten 64\, 14469 Potsdam\, Germany
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:EXTERN: Eltern Medien Tag 
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180502T190000
DTEND;TZID=Europe/Berlin:20180502T210000
DTSTAMP:20190305T185732Z
UID:2o60r26f5pq7muep7htdi4r01n@google.com
RECURRENCE-ID;TZID=Europe/Berlin:20180501T190000
CLASS:PUBLIC
CREATED:20171126T091145Z
DESCRIPTION:Treffen der offenen OK Lab Gruppe. Informationen auf&nbsp\;<a h
 ref="https://www.google.com/url?q=http%3A%2F%2Fwww.oklab-potsdam.de&amp\;sa
 =D&amp\;usd=2&amp\;usg=AFQjCNH4ia7HdoVhwjLJiSfSMu46bTzIxA" target="_blank">
 www.oklab-potsdam.de</a><br>Themen sind: Open Data\, Civic Tech\, Programmi
 erung<br>
LAST-MODIFIED:20180423T073355Z
LOCATION:machBar Seminarraum
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:OK Lab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180411T170000Z
DTEND:20180411T190000Z
DTSTAMP:20190305T185732Z
UID:54e37ogvp0u4bcsssmr6nvklur@google.com
CREATED:20180321T073604Z
DESCRIPTION:Erstes Chaostreff in Potsdam in der machBar. \n\nWird es einen 
 neuen Erfa geben?
LAST-MODIFIED:20180323T140809Z
LOCATION:Seminarraum
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Chaostreff
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180418T160000Z
DTEND:20180418T190000Z
DTSTAMP:20190305T185732Z
UID:5it6in3t9a6bkm6sra1ei44hcd@google.com
CREATED:20180323T140717Z
DESCRIPTION:Treffen der Potsdamer Bienenmenschen.
LAST-MODIFIED:20180323T140748Z
LOCATION:Seminarraum
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Imkertreffen
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20181007T110000Z
DTEND:20181007T150000Z
DTSTAMP:20190305T185732Z
UID:7gubjda7233nr0aic7nau87ojq@google.com
CREATED:20180321T074052Z
DESCRIPTION:Reparieren\, modifizieren oder erweitern mit der machBar auf de
 m Solimarkt im freiLand
LAST-MODIFIED:20180321T074052Z
LOCATION:Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar@Solimarkt
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180909T110000Z
DTEND:20180909T150000Z
DTSTAMP:20190305T185732Z
UID:5tatrcit8g1mhaal5aecr07muo@google.com
CREATED:20180321T074031Z
DESCRIPTION:Reparieren\, modifizieren oder erweitern mit der machBar auf de
 m Solimarkt im freiLand
LAST-MODIFIED:20180321T074032Z
LOCATION:Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar@Solimarkt
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180624T110000Z
DTEND:20180624T150000Z
DTSTAMP:20190305T185732Z
UID:34umj4pa5g3ubmgpg84l57op7t@google.com
CREATED:20180321T074006Z
DESCRIPTION:Reparieren\, modifizieren oder erweitern mit der machBar auf de
 m Solimarkt im freiLand
LAST-MODIFIED:20180321T074006Z
LOCATION:Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar@Solimarkt
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180415T110000Z
DTEND:20180415T150000Z
DTSTAMP:20190305T185732Z
UID:17uhb8mltk8akncompll76d47l@google.com
CREATED:20180321T073935Z
DESCRIPTION:Reparieren\, modifizieren oder erweitern mit der machBar auf de
 m Solimarkt im freiLand
LAST-MODIFIED:20180321T073935Z
LOCATION:Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar@Solimarkt
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180317T130000Z
DTEND:20180317T170000Z
DTSTAMP:20190305T185732Z
UID:55btcmdmcp3iicf65tdjfmpaj1@google.com
CLASS:PUBLIC
CREATED:20180220T070337Z
DESCRIPTION:<span>Interessierte Kopterpiloten und Leute dies es werden woll
 en. Kommt zum 2.Koptertreffen in der Potsdamer "Machbar".<br> Neben dem Erf
 ahrungsaustausch haben wir Platz zum Fachsimpeln\, reparieren\, Getränke tr
 inken und fliegen. Auch stehen die Maschinen des Wissenschaftsladen Potsdam
  zur Verfügung<br> (3D Drucker\, CNC-Fräser\, Lasercutter\, Lötstationen)</
 span>
LAST-MODIFIED:20180220T070337Z
LOCATION:freiLand Potsdam Haus 5\, Friedrich-Engels-Straße 22\, 14473 Potsd
 am\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:2.Koptertreffen 2018
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180217T120000Z
DTEND:20180217T170000Z
DTSTAMP:20190305T185732Z
UID:08g4pq8igtt7itfud1giriscp2@google.com
CREATED:20180201T054523Z
DESCRIPTION:Haus 5\nAm Boden bleiben war gestern.
LAST-MODIFIED:20180215T191735Z
LOCATION:freiLand Potsdam\, Friedrich-Engels-Straße 22\, 14473 Potsdam\, De
 utschland
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:1. Koptertreffen 2018
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180221T190000Z
DTEND:20180221T210000Z
DTSTAMP:20190305T185732Z
UID:6lp9jql7gkfd848f1sglpe7qei@google.com
CLASS:PUBLIC
CREATED:20180215T113957Z
DESCRIPTION:Potsdamer Jungimker treffen sich zum Austausch von aktuellen En
 twicklungen in der Bienenhaltung\, Erfahrungen zu Betriebsweisen\, saisonal
 en Maßnahmen\, technischer Umsetzung von Monitoring-Lösungen für Bienenbeut
 en sowie Herstellung von Bienenbehausungen und Restaurierung von älteren im
 kerlichen Gerätschaften.
LAST-MODIFIED:20180215T155232Z
LOCATION:freiLand Potsdam Haus 5\, Friedrich-Engels-Straße 22\, 14473 Potsd
 am\, Deutschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Jungimker-Treffen
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180209T090000Z
DTEND:20180209T150000Z
DTSTAMP:20190305T185732Z
UID:0k3eu4imuol19pn1160lb7fnf2@google.com
CREATED:20180131T072126Z
DESCRIPTION:Workshop für die partizipative Prototypenentwicklung für Mensch
 en mit besonderen Bedürfnissen
LAST-MODIFIED:20180131T072254Z
LOCATION:freiLand Potsdam\, Friedrich-Engels-Straße 22\, 14473 Potsdam\, De
 utschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Fabulandlabs Workshop Tag2
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20180208T090000Z
DTEND:20180208T150000Z
DTSTAMP:20190305T185732Z
UID:31hegve2b4bpkhua6i7s4tpal0@google.com
CREATED:20180131T072058Z
DESCRIPTION:Workshop für die partizipative Prototypenentwicklung für Mensch
 en mit besonderen Bedürfnissen
LAST-MODIFIED:20180131T072247Z
LOCATION:freiLand Potsdam\, Friedrich-Engels-Straße 22\, 14473 Potsdam\, De
 utschland
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Fabulandlabs Workshop Tag1
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20171212T190000
DTEND;TZID=Europe/Berlin:20171212T210000
RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=TU
DTSTAMP:20190305T185732Z
UID:2o60r26f5pq7muep7htdi4r01n@google.com
CLASS:PUBLIC
CREATED:20171126T091145Z
DESCRIPTION:Treffen der offenen OK Lab Gruppe. Informationen auf&nbsp\;<a h
 ref="https://www.google.com/url?q=http%3A%2F%2Fwww.oklab-potsdam.de&amp\;sa
 =D&amp\;usd=2&amp\;usg=AFQjCNH4ia7HdoVhwjLJiSfSMu46bTzIxA" target="_blank">
 www.oklab-potsdam.de</a><br>Themen sind: Open Data\, Civic Tech\, Programmi
 erung<br>
LAST-MODIFIED:20180114T091342Z
LOCATION:machBar Seminarraum
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:OK Lab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20170824T180000
DTEND;TZID=Europe/Berlin:20170824T200000
RRULE:FREQ=WEEKLY;BYDAY=TH
DTSTAMP:20190305T185732Z
UID:5neh1ktep3uqvjk197abrb0gio@google.com
CLASS:PUBLIC
CREATED:20170823T154208Z
DESCRIPTION:Offener Abend der machBar - Jeder ist Willkommen - <a href="htt
 ps://www.google.com/url?q=http%3A%2F%2Fwww.machbar-potsdam.de&amp\;sa=D&amp
 \;usd=2&amp\;usg=AFQjCNHgkYi-CBwfAjzxhtvkRZXlROswdg" target="_blank">www.ma
 chbar-potsdam.de</a>
LAST-MODIFIED:20180114T091318Z
LOCATION:machBar im Freiland Haus 5 - Potsdam
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:OpenLab
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20180123T170000
DTEND;TZID=Europe/Berlin:20180123T190000
RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=TU
DTSTAMP:20190305T185732Z
UID:646brirtu83g18fhg5jtmf1dac@google.com
CLASS:PUBLIC
CREATED:20180114T085716Z
DESCRIPTION:Plenum der machBar
LAST-MODIFIED:20180114T090813Z
LOCATION:Haus 5 - Seminarraum
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:machBar Plenum
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171215T180000Z
DTEND:20171215T220000Z
DTSTAMP:20190305T185732Z
UID:1h64qnkskd7nl9l3c9qo5f4i24@google.com
CREATED:20171207T192459Z
DESCRIPTION:Öffentliche Wihnachtsfeier der machBar\, zu der alle Freundinne
 n und Freunde der machBar eingeladen sind.\n
LAST-MODIFIED:20171211T125822Z
LOCATION:machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Weihnachtsfeier
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20171227
DTEND;VALUE=DATE:20171228
DTSTAMP:20190305T185732Z
UID:27sgrcdu4099mtq830biaal87d@google.com
CREATED:20171211T125726Z
DESCRIPTION:Die Freifunker laden zum Livestream schauen vom 34c3 in die mac
 hBar ein. \n
LAST-MODIFIED:20171211T125726Z
LOCATION:machBar Haus5
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:34c3 in der machBar
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171202T100000Z
DTEND:20171202T190000Z
DTSTAMP:20190305T185732Z
UID:3auqqsk9ik7as92h61ipubamrm@google.com
CREATED:20171110T061505Z
DESCRIPTION:Umbau in Maschinenraum und Labor
LAST-MODIFIED:20171126T092204Z
LOCATION:machBar im freiLand Potsdam
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Arbeitseinsatz Part2
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171202T090000Z
DTEND:20171202T160000Z
DTSTAMP:20190305T185732Z
UID:2umrmkbncl3urpfd6k8ib7t0di@google.com
CREATED:20171126T091658Z
DESCRIPTION:Umbau in Maschinenraum und Labor\n
LAST-MODIFIED:20171126T091658Z
LOCATION:machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Arbeitseinsatz
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171119T090000Z
DTEND:20171119T170000Z
DTSTAMP:20190305T185732Z
UID:06r0tidq486ajl21l9snb3r7jh@google.com
CREATED:20171110T061418Z
DESCRIPTION:Vorbereitende Maßnahmen für den Umbau von Maschinenraum und Lab
 or
LAST-MODIFIED:20171110T061418Z
LOCATION:machBar im freiLand Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Arbeitseinsatz Part1
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171125T130000Z
DTEND:20171125T170000Z
DTSTAMP:20190305T185732Z
UID:5ek97lmft4h681a4bpf1g66i69@google.com
CREATED:20171110T061231Z
DESCRIPTION:
LAST-MODIFIED:20171110T061249Z
LOCATION:machBar im freiLand Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Drohnentreffen
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171116T193000Z
DTEND:20171116T203000Z
DTSTAMP:20190305T185732Z
UID:3e21t1trks34rdhttbvje5t7ng@google.com
CREATED:20171110T061029Z
DESCRIPTION:
LAST-MODIFIED:20171110T061137Z
LOCATION:Haus 5\, Friedrich-Engels-Str. 22\, 14473 Potsdam
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:machBar Plenum 
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171118T090000Z
DTEND:20171118T193000Z
DTSTAMP:20190305T185732Z
UID:6jv9nk3nps25428ppffa2eueod@google.com
CREATED:20170907T210759Z
DESCRIPTION:
LAST-MODIFIED:20170907T210759Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:OpenDataBarCamp - www.potsdam.io
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171118T100000Z
DTEND:20171118T140000Z
DTSTAMP:20190305T185732Z
UID:5cvfnchqjfa8a831jj8qifdm79@google.com
CREATED:20170907T210717Z
DESCRIPTION:
LAST-MODIFIED:20170907T210717Z
LOCATION:Stadt- Und Landesbibliothek\, Am Kanal 47\, 14467 Potsdam\, German
 y
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:(Stadt- und Landesbibliothek) repairCafe
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20171021T090000Z
DTEND:20171021T130000Z
DTSTAMP:20190305T185732Z
UID:69isdq0hnjfp13ovf1jr23luij@google.com
CREATED:20170907T210439Z
DESCRIPTION:
LAST-MODIFIED:20170907T210617Z
LOCATION:Stadt- und Landesbibliothek Potsdam\, Am Kanal 47\, 14467 Potsdam\
 , Germany
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:(Stadt- und Landesbibliothek) repairCafe
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20170923T090000Z
DTEND:20170923T130000Z
DTSTAMP:20190305T185732Z
UID:1gv09kcmibh8q2j2scht2j14tq@google.com
CLASS:PUBLIC
CREATED:20170823T161342Z
DESCRIPTION:www.bibliothek.potsdam.de/repair-cafe-reparieren-statt-wegwerfe
 n-2
LAST-MODIFIED:20170907T210321Z
LOCATION:Stadt- und Landesbibliothek Potsdam\, Am Kanal 47\, 14467 Potsdam\
 , Germany
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:(Stadt- und Landesbibliothek) repairCafe
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20170823T180000
DTEND;TZID=Europe/Berlin:20170823T200000
RRULE:FREQ=WEEKLY;COUNT=8;BYDAY=MO,WE
DTSTAMP:20190305T185732Z
UID:34c0eggrc3qi4te2g3km1jl05g@google.com
CLASS:PUBLIC
CREATED:20170823T161131Z
DESCRIPTION:
LAST-MODIFIED:20170823T161131Z
LOCATION:Freiland Haus 5 - Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Uni Potsdam - Drohnenseminar
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20171007
DTEND;VALUE=DATE:20171023
DTSTAMP:20190305T185732Z
UID:71vvvsbcjb3b4gsfmsjel6aqtb@google.com
CLASS:PUBLIC
CREATED:20170823T154828Z
DESCRIPTION:www.codeweek.eu
LAST-MODIFIED:20170823T154828Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:CODEWEEK
TRANSP:TRANSPARENT
END:VEVENT
BEGIN:VEVENT
DTSTART:20171006T150000Z
DTEND:20171006T200000Z
DTSTAMP:20190305T185732Z
UID:3j9e90dlt1fiah7f9upt3iimks@google.com
CLASS:PUBLIC
CREATED:20170823T154740Z
DESCRIPTION:Vernetzungstreffen von Aktiven aus Brandenburger FabLabs\, offe
 nen Werkstätten\, Hacker Spaces\, Makerspaces\, Garagen\, Hobbyräumen...
LAST-MODIFIED:20170823T154740Z
LOCATION:Freiland Haus 5 - Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Vernetzungstreffen Brandenburger FabLabs
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20170822T160000Z
DTEND:20170822T190000Z
DTSTAMP:20190305T185732Z
UID:0lkrmhsgfmq1bgaf54qs91a595@google.com
CREATED:20170823T154534Z
DESCRIPTION:www.machbar-potsdam.de
LAST-MODIFIED:20170823T154534Z
LOCATION:Freiland Haus 5 - Potsdam
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Vorstellung Sensorkit für aquatische Vor-Ort-Parameter
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=Europe/Berlin:20170822T190000
DTEND;TZID=Europe/Berlin:20170822T210000
RRULE:FREQ=WEEKLY;UNTIL=20170904T215959Z;INTERVAL=2;BYDAY=TU
DTSTAMP:20190305T185732Z
UID:7kk7rorknhett094id0k0gc3mj@google.com
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;X-NUM-GUE
 STS=0:mailto:j68lhv614hbv3u4ttbrs6glhpg@group.calendar.google.com
CLASS:PUBLIC
CREATED:20170823T153811Z
DESCRIPTION:Treffen der offenen OK Lab Gruppe. Informationen auf www.oklab-
 potsdam.de\nThemen sind: Open Data\, Civic Tech\, Programmierung
LAST-MODIFIED:20170823T153941Z
LOCATION:machBar
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:OK Lab Potsdam
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20170629T170000Z
DTEND:20170629T200000Z
DTSTAMP:20190305T185732Z
UID:557so5mpmiubtg38jihapek2o5@google.com
CREATED:20170628T085452Z
DESCRIPTION:
LAST-MODIFIED:20170628T085503Z
LOCATION:
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Open Lab
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/multiple_rrule.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//CyrusIMAP.org/Cyrus 
 3.9.0-alpha0-85-gd6d859e0cf-fm-20230116.001-gd6d859e0//EN
BEGIN:VEVENT
CREATED:20230109T084023Z
LAST-MODIFIED:20230119T110732Z
DTSTAMP:20230119T110732Z
UID:56cdc4dc-11b7-407c-86c6-9faedfc28afb
SUMMARY:My repeating event
RRULE:FREQ=WEEKLY;BYDAY=TH;COUNT=20
RRULE:FREQ=MONTHLY;BYDAY=2MO;COUNT=2
DTSTART;TZID=Europe/London:20230112T100000
DTEND;TZID=Europe/London:20230112T120000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/no_events.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/one_day_event_repeat_every_day.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J
SUMMARY:test3
CLASS:PUBLIC
STATUS:CONFIRMED
DTSTART;VALUE=DATE:20190304
DTEND;VALUE=DATE:20190305
RRULE:FREQ=DAILY
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/one_day_event.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J
SUMMARY:test2
DTSTART;VALUE=DATE:20190304
DTEND;VALUE=DATE:20190305
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/one_event_repeat_every_3_days.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J
SUMMARY:test4
CLASS:PUBLIC
STATUS:CONFIRMED
RRULE:FREQ=DAILY;INTERVAL=3
DTSTART;TZID=Europe/Berlin:20190304T000000
DTEND;TZID=Europe/Berlin:20190304T010000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/one_event.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/rdate_falls_on_rrule_until.ics`

```ics
BEGIN:VCALENDAR
PRODID:+//IDN bitfire.at//DAVx5/2.6.1.1-gplay ical4j/2.2.6
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Berlin
TZURL:http://tzurl.org/zoneinfo/Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19810329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19961027T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
BEGIN:STANDARD
TZOFFSETFROM:+005328
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:18930401T000000
RDATE:18930401T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19160430T230000
RDATE:19160430T230000
RDATE:19170416T020000
RDATE:19180415T020000
RDATE:19400401T020000
RDATE:19430329T020000
RDATE:19440403T020000
RDATE:19450402T020000
RDATE:19460414T020000
RDATE:19470406T030000
RDATE:19480418T020000
RDATE:19490410T020000
RDATE:19800406T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19161001T010000
RDATE:19161001T010000
RDATE:19170917T030000
RDATE:19180916T030000
RDATE:19421102T030000
RDATE:19431004T030000
RDATE:19441002T030000
RDATE:19451118T030000
RDATE:19461007T030000
RDATE:19471005T030000
RDATE:19481003T030000
RDATE:19491002T030000
RDATE:19800928T030000
RDATE:19810927T030000
RDATE:19820926T030000
RDATE:19830925T030000
RDATE:19840930T030000
RDATE:19850929T030000
RDATE:19860928T030000
RDATE:19870927T030000
RDATE:19880925T030000
RDATE:19890924T030000
RDATE:19900930T030000
RDATE:19910929T030000
RDATE:19920927T030000
RDATE:19930926T030000
RDATE:19940925T030000
RDATE:19950924T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+0200
TZOFFSETTO:+0300
TZNAME:CEMT
DTSTART:19450524T010000
RDATE:19450524T010000
RDATE:19470511T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETFROM:+0300
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19450924T030000
RDATE:19450924T030000
RDATE:19470629T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0100
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19460101T000000
RDATE:19460101T000000
RDATE:19800101T000000
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTAMP:20191219T182547Z
UID:f0f31ddb-6918-46af-a5a1-0a7254fbce71
SEQUENCE:11
SUMMARY:Test
LOCATION:Example
DTSTART;TZID=Europe/Berlin:20191015T161500
DURATION:PT1H30M
RDATE;TZID=Europe/Berlin:20200204T161500
RRULE:FREQ=WEEKLY;UNTIL=20200204T151459Z;BYDAY=TU;WKST=SU
EXDATE:20191015T141500Z,20191022T141500Z,20191105T151500Z,20191119T151500Z,
 20191126T151500Z,20191203T151500Z,20191217T151500Z,20191224T151500Z,201912
 31T151500Z
CLASS:PUBLIC
STATUS:CONFIRMED
CREATED:20191013T184131Z
X-MOZ-GENERATION:10
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/rdate_hackerpublicradio.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:Data::ICal 0.20
X-WR-CALNAME:Hacker Public Radio
X-WR-TIMEZONE:Europe/London
BEGIN:VEVENT
DESCRIPTION:This is from http://www.hackerpublicradio.org/eps/hpr1286/iCalendar_
 Hacking_shownotes.html
DTEND:20130803T210000Z
DTSTART:20130803T190000Z
LOCATION:mumble.openspeak.cc port: 64747
RDATE;VALUE=DATE-TIME:20130803T190000Z
RDATE;VALUE=DATE-TIME:20130831T190000Z
RDATE;VALUE=DATE-TIME:20131005T190000Z
RDATE;VALUE=DATE-TIME:20131102T190000Z
RDATE;VALUE=DATE-TIME:20131130T190000Z
RDATE;VALUE=DATE-TIME:20140104T190000Z
RDATE;VALUE=DATE-TIME:20140201T190000Z
RDATE;VALUE=DATE-TIME:20140301T190000Z
RDATE;VALUE=DATE-TIME:20140405T190000Z
RDATE;VALUE=DATE-TIME:20140503T190000Z
RDATE;VALUE=DATE-TIME:20140531T190000Z
RDATE;VALUE=DATE-TIME:20140705T190000Z
SUMMARY:HPR Community News
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/rdate.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART:20130803T190000Z
DTEND:20130803T210000Z
RDATE;VALUE=DATE-TIME:20140705T190000Z
RRULE:FREQ=DAILY;UNTIL=20150320T030000Z
SUMMARY:rdate and rrule overlap
END:VEVENT
BEGIN:VEVENT
DTSTART:20140803T190000Z
DTEND:20140803T210000Z
RDATE;VALUE=DATE-TIME:20150705T190000Z
EXDATE;VALUE=DATE-TIME:20150705T190000Z
RRULE:FREQ=DAILY;UNTIL=20160320T030000Z
SUMMARY:rdate and rrule overlap but exdate removes the date again
END:VEVENT
BEGIN:VEVENT
DTSTART:20240803T190000Z
DTEND:20240803T210000Z
RDATE;VALUE=DATE-TIME:20250705T190000Z
EXDATE;VALUE=DATE-TIME:20250705T190000Z
SUMMARY:rdate but exdate removes the date again
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/rdate2.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART:20140803T190000Z
DTEND:20140803T210000Z
RDATE;VALUE=DATE-TIME:20150705T190000Z
EXDATE;VALUE=DATE-TIME:20150705T190000Z
RRULE:FREQ=DAILY;UNTIL=20160320T030000Z
SUMMARY:rdate and rrule overlap but exdate removes the date again
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/recurrence_sequence_number.ics`

```ics
BEGIN:VCALENDAR
CALSCALE:GREGORIAN
PRODID:-//Ximian//NONSGML Evolution Calendar//EN
VERSION:2.0
BEGIN:VEVENT
UID:212e857f74c7eb0b4874e024f6537b77bd77dbd5
DTSTAMP:20200922T092948Z
DTSTART;VALUE=DATE:20200908
DTEND;VALUE=DATE:20200909
SEQUENCE:4
SUMMARY:Base event
TRANSP:OPAQUE
CLASS:PUBLIC
CREATED:20200922T155408Z
LAST-MODIFIED:20200922T155513Z
LOCATION:Changed again
RRULE:FREQ=WEEKLY;BYDAY=TU
END:VEVENT
BEGIN:VEVENT
UID:212e857f74c7eb0b4874e024f6537b77bd77dbd5
DTSTAMP:20200922T092948Z
DTSTART;VALUE=DATE:20200922
DTEND;VALUE=DATE:20200923
SEQUENCE:3
SUMMARY:Modified event
TRANSP:OPAQUE
CLASS:PUBLIC
CREATED:20200922T155408Z
LAST-MODIFIED:20200922T155424Z
RECURRENCE-ID;VALUE=DATE:20200922
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/recurring_events_changed_duration.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T154052Z
LAST-MODIFIED:20190303T154956Z
DTSTAMP:20190303T154956Z
UID:5d4c6843-9300-4f91-8d88-6094d4b0b840
SUMMARY:test7
RRULE:FREQ=DAILY;UNTIL=20190320T030000Z
DTSTART;TZID=Europe/Berlin:20190318T040000
DTEND;TZID=Europe/Berlin:20190318T050000
TRANSP:OPAQUE
X-MOZ-GENERATION:4
SEQUENCE:1
DESCRIPTION:description should be the same
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T154131Z
LAST-MODIFIED:20190303T154145Z
DTSTAMP:20190303T154145Z
UID:5d4c6843-9300-4f91-8d88-6094d4b0b840
SUMMARY:test7 - edited
RECURRENCE-ID;TZID=Europe/Berlin:20190319T040000
DTSTART;TZID=Europe/Berlin:20190319T040000
DTEND;TZID=Europe/Berlin:20190319T050000
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:2
LOCATION:location
X-LIC-ERROR:No value for CLASS property. Removing entire property:
END:VEVENT
BEGIN:VEVENT
CREATED:20190307T194152Z
LAST-MODIFIED:20190307T195005Z
DTSTAMP:20190307T195005Z
UID:a0c78729-30b1-4ba3-a86e-6aedd995d788
SUMMARY:New Event
RRULE:FREQ=DAILY;UNTIL=20190310T010000Z
DTSTART;TZID=Europe/Berlin:20190307T020000
DTEND;TZID=Europe/Berlin:20190307T030000
TRANSP:OPAQUE
SEQUENCE:1
X-MOZ-GENERATION:6
END:VEVENT
BEGIN:VEVENT
CREATED:20190307T194207Z
LAST-MODIFIED:20190307T194945Z
DTSTAMP:20190307T194945Z
UID:a0c78729-30b1-4ba3-a86e-6aedd995d788
SUMMARY:New Event
RECURRENCE-ID;TZID=Europe/Berlin:20190308T020000
DTSTART;TZID=Europe/Berlin:20190308T010000
DTEND;TZID=Europe/Berlin:20190308T030000
TRANSP:OPAQUE
SEQUENCE:3
X-MOZ-GENERATION:2
END:VEVENT
BEGIN:VEVENT
CREATED:20190307T194214Z
LAST-MODIFIED:20190307T194952Z
DTSTAMP:20190307T194952Z
UID:a0c78729-30b1-4ba3-a86e-6aedd995d788
SUMMARY:New Event
RECURRENCE-ID;TZID=Europe/Berlin:20190309T020000
DTSTART;TZID=Europe/Berlin:20190309T030000
DTEND;TZID=Europe/Berlin:20190309T033000
TRANSP:OPAQUE
SEQUENCE:3
X-MOZ-GENERATION:3
END:VEVENT
BEGIN:VEVENT
CREATED:20190307T194955Z
LAST-MODIFIED:20190307T195005Z
DTSTAMP:20190307T195005Z
UID:a0c78729-30b1-4ba3-a86e-6aedd995d788
SUMMARY:New Event
RECURRENCE-ID;TZID=Europe/Berlin:20190310T020000
DTSTART;VALUE=DATE:20190310
DTEND;VALUE=DATE:20190311
TRANSP:TRANSPARENT
SEQUENCE:2
X-MOZ-GENERATION:6
X-LIC-ERROR;X-LIC-ERRORTYPE=VALUE-PARSE-ERROR:No value for CLASS property.
  Removing entire property:
DURATION:PT0S
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/recurring_events_moved.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T154052Z
LAST-MODIFIED:20190303T154956Z
DTSTAMP:20190303T154956Z
UID:5d4c6843-9300-4f91-8d88-6094d4b0b840
SUMMARY:test7
RRULE:FREQ=DAILY;UNTIL=20190320T030000Z
DTSTART;TZID=Europe/Berlin:20190318T040000
DTEND;TZID=Europe/Berlin:20190318T050000
TRANSP:OPAQUE
X-MOZ-GENERATION:4
SEQUENCE:1
DESCRIPTION:description should be the same
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T154131Z
LAST-MODIFIED:20190303T154145Z
DTSTAMP:20190303T154145Z
UID:5d4c6843-9300-4f91-8d88-6094d4b0b840
SUMMARY:test7 - edited
RECURRENCE-ID;TZID=Europe/Berlin:20190319T040000
DTSTART;TZID=Europe/Berlin:20190319T040000
DTEND;TZID=Europe/Berlin:20190319T050000
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:2
LOCATION:location
X-LIC-ERROR:No value for CLASS property. Removing entire property:
END:VEVENT
BEGIN:VEVENT
CREATED:20190307T194152Z
LAST-MODIFIED:20190307T194216Z
DTSTAMP:20190307T194216Z
UID:a0c78729-30b1-4ba3-a86e-6aedd995d788
SUMMARY:New Event
RRULE:FREQ=DAILY;UNTIL=20190310T010000Z
DTSTART;TZID=Europe/Berlin:20190307T020000
DTEND;TZID=Europe/Berlin:20190307T030000
TRANSP:OPAQUE
SEQUENCE:1
X-MOZ-GENERATION:3
END:VEVENT
BEGIN:VEVENT
CREATED:20190307T194207Z
LAST-MODIFIED:20190307T194212Z
DTSTAMP:20190307T194212Z
UID:a0c78729-30b1-4ba3-a86e-6aedd995d788
SUMMARY:New Event
RECURRENCE-ID;TZID=Europe/Berlin:20190308T020000
DTSTART;TZID=Europe/Berlin:20190308T010000
DTEND;TZID=Europe/Berlin:20190308T020000
TRANSP:OPAQUE
SEQUENCE:2
X-MOZ-GENERATION:2
DURATION:PT0S
END:VEVENT
BEGIN:VEVENT
CREATED:20190307T194214Z
LAST-MODIFIED:20190307T194216Z
DTSTAMP:20190307T194216Z
UID:a0c78729-30b1-4ba3-a86e-6aedd995d788
SUMMARY:New Event
RECURRENCE-ID;TZID=Europe/Berlin:20190309T020000
DTSTART;TZID=Europe/Berlin:20190309T030000
DTEND;TZID=Europe/Berlin:20190309T040000
TRANSP:OPAQUE
SEQUENCE:2
X-MOZ-GENERATION:3
DURATION:PT0S
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/same_event_recurring_at_same_time.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
X-TZINFO:Europe/London[2024a]
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:-000115
TZNAME:Europe/London(STD)
DTSTART:18471201T000000
RDATE:18471201T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19160521T020000
RDATE:19160521T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19161001T030000
RDATE:19161001T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19170408T020000
RDATE:19170408T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19170917T030000
RDATE:19170917T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19180324T020000
RDATE:19180324T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19180930T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=-1MO;UNTIL=19190929T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19190330T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19200328T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19201025T030000
RDATE:19201025T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19210403T020000
RDATE:19210403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19211003T030000
RDATE:19211003T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19220326T020000
RDATE:19220326T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19221008T030000
RDATE:19221008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19230422T020000
RDATE:19230422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19240413T020000
RDATE:19240413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19230916T030000
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=3SU;UNTIL=19240921T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19250419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19260418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19270410T020000
RDATE:19270410T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19280422T020000
RDATE:19280422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19290421T020000
RDATE:19290421T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19300413T020000
RDATE:19300413T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19310419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19320417T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19251004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19321002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19330409T020000
RDATE:19330409T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19331008T030000
RDATE:19331008T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19340422T020000
RDATE:19340422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19350414T020000
RDATE:19350414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19360419T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19370418T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19380410T020000
RDATE:19380410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19341007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19381002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19390416T020000
RDATE:19390416T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19400225T020000
RDATE:19400225T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19410504T020000
RDATE:19410504T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19410810T030000
RDATE:19410810T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19420405T020000
RDATE:19420405T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19420809T030000
RDATE:19420809T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19430404T020000
RDATE:19430404T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19430815T030000
RDATE:19430815T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19440402T020000
RDATE:19440402T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19440917T030000
RDATE:19440917T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19450402T020000
RDATE:19450402T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19391119T030000
RDATE:19391119T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19450715T030000
RDATE:19450715T030000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19460414T020000
RDATE:19460414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19470316T020000
RDATE:19470316T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+020000
TZOFFSETFROM:+010000
TZNAME:Europe/London(DST)
DTSTART:19470413T020000
RDATE:19470413T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19451007T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19461006T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+020000
TZNAME:Europe/London(DST)
DTSTART:19470810T030000
RDATE:19470810T030000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19471102T030000
RDATE:19471102T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19480314T020000
RDATE:19480314T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19490403T020000
RDATE:19490403T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19481031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19491030T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19501022T030000
RDATE:19501022T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19511021T030000
RDATE:19511021T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19521026T030000
RDATE:19521026T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19500416T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19530419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19540411T020000
RDATE:19540411T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19550417T020000
RDATE:19550417T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19560422T020000
RDATE:19560422T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19570414T020000
RDATE:19570414T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19580420T020000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=3SU;UNTIL=19590419T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19600410T020000
RDATE:19600410T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19531004T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU;UNTIL=19601002T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19610326T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19630331T020000
END:DAYLIGHT
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19640322T020000
RDATE:19640322T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19611029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19641025T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19651024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19661023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19650321T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19670319T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19671029T030000
RDATE:19671029T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+010000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19681027T000000
RDATE:19681027T000000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19680218T020000
RDATE:19680218T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19711031T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19751026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19761024T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19771023T030000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19720319T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=3SU;UNTIL=19800316T020000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19781029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19801026T030000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19811025T020000
RDATE:19811025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19821024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19831023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19841028T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19871025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19881023T020000
RDATE:19881023T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19891029T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=19921025T020000
END:STANDARD
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19931024T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=4SU;UNTIL=19951022T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:Europe/London(DST)
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU;UNTIL=19960331T010000
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:Europe/London(STD)
DTSTART:19961027T020000
RDATE:19961027T020000
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETTO:+010000
TZOFFSETFROM:+000000
TZNAME:(DST)
DTSTART:19970330T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETTO:+000000
TZOFFSETFROM:+010000
TZNAME:(STD)
DTSTART:19971026T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20240926T104120Z
LAST-MODIFIED:20240926T104200Z
DTSTAMP:20240926T104200Z
UID:758bdcf4-da36-4fe1-a90c-2327612e7174
SUMMARY:event
RRULE:FREQ=DAILY;UNTIL=20240928T110000Z
DTSTART;TZID=Europe/London:20240923T120000
DTEND;TZID=Europe/London:20240923T130000
TRANSP:OPAQUE
X-MOZ-GENERATION:6
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
CREATED:20240926T104135Z
LAST-MODIFIED:20240926T104141Z
DTSTAMP:20240926T104141Z
UID:758bdcf4-da36-4fe1-a90c-2327612e7174
SUMMARY:event
RECURRENCE-ID;TZID=Europe/London:20240923T120000
DTSTART;TZID=Europe/London:20240924T120000
DTEND;TZID=Europe/London:20240924T130000
TRANSP:OPAQUE
X-MOZ-GENERATION:6
SEQUENCE:2
END:VEVENT
BEGIN:VEVENT
CREATED:20240926T104141Z
LAST-MODIFIED:20240926T104148Z
DTSTAMP:20240926T104148Z
UID:758bdcf4-da36-4fe1-a90c-2327612e7174
SUMMARY:event
RECURRENCE-ID;TZID=Europe/London:20240927T120000
DTSTART;TZID=Europe/London:20240924T120000
DTEND;TZID=Europe/London:20240924T130000
TRANSP:OPAQUE
X-MOZ-GENERATION:6
SEQUENCE:2
END:VEVENT
BEGIN:VEVENT
CREATED:20240926T104148Z
LAST-MODIFIED:20240926T104158Z
DTSTAMP:20240926T104158Z
UID:758bdcf4-da36-4fe1-a90c-2327612e7174
SUMMARY:event
RECURRENCE-ID;TZID=Europe/London:20240925T120000
DTSTART;TZID=Europe/London:20240926T120000
DTEND;TZID=Europe/London:20240926T130000
TRANSP:OPAQUE
X-MOZ-GENERATION:6
SEQUENCE:2
END:VEVENT
BEGIN:VEVENT
CREATED:20240926T104158Z
LAST-MODIFIED:20240926T104200Z
DTSTAMP:20240926T104200Z
UID:758bdcf4-da36-4fe1-a90c-2327612e7174
SUMMARY:event
RECURRENCE-ID;TZID=Europe/London:20240928T120000
DTSTART;TZID=Europe/London:20240926T120000
DTEND;TZID=Europe/London:20240926T130000
TRANSP:OPAQUE
X-MOZ-GENERATION:6
SEQUENCE:2
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/several_events_at_the_same_time.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-1
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-2
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-3
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-4
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-5
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-6
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-7
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-8
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-9
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:event-10
SUMMARY:test1
DTSTART;TZID=Europe/Berlin:20190304T080000
DTEND;TZID=Europe/Berlin:20190304T083000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/subcomponents.ics`

```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
SUMMARY:redacted
DTSTART;TZID=Europe/Berlin:20190527T140000
DTEND;TZID=Europe/Berlin:20190527T163000
DTSTAMP:20190510T070457Z
UID:00000000-0000-0000-0000-000000000000
SEQUENCE:4
ATTENDEE;CN=redacted;PARTSTAT=NEEDS-ACTION;ROLE=REQ-PARTICIPANT;RSVP=TRUE:mailto:redacted@example.com
ATTENDEE;CN="redacted";PARTSTAT=NEEDS-ACTION;ROLE=REQ-PARTICIPANT;RSVP=TRUE:mailto:redacted@example.com
ATTENDEE;CN="redacted";PARTSTAT=NEEDS-ACTION;ROLE=REQ-PARTICIPANT;RSVP=TRUE:mailto:redacted@example.com
ATTENDEE;CN="redacted";PARTSTAT=ACCEPTED;ROLE=REQ-PARTICIPANT:mailto:redacted@example.com
ATTENDEE;CUTYPE=RESOURCE;PARTSTAT=ACCEPTED;ROLE=NON-PARTICIPANT;RSVP=TRUE:mailto:redacted@example.com
ATTENDEE;CUTYPE=RESOURCE;PARTSTAT=ACCEPTED;ROLE=NON-PARTICIPANT;RSVP=TRUE:mailto:redacted@example.com
CLASS:PUBLIC
DESCRIPTION:redacted
LAST-MODIFIED:20190510T070457Z
LOCATION:redacted@example.com
ORGANIZER;CN=redacted;SENT-BY="mailto:redacted@example.com":mailto:redacted@example.com
STATUS:CONFIRMED
TRANSP:OPAQUE
X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY
X-MS-OLK-SENDER:mailto:redacted@example.com
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Reminder
TRIGGER;RELATED=START:-PT10M
END:VALARM
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/three_events_one_edited.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T154052Z
LAST-MODIFIED:20190303T154145Z
DTSTAMP:20190303T154145Z
UID:5d4c6843-9300-4f91-8d88-6094d4b0b840
SUMMARY:test7
RRULE:FREQ=DAILY;UNTIL=20190320T030000Z
DTSTART;TZID=Europe/Berlin:20190318T040000
DTEND;TZID=Europe/Berlin:20190318T050000
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:1
END:VEVENT
BEGIN:VEVENT
CREATED:20190303T154131Z
LAST-MODIFIED:20190303T154145Z
DTSTAMP:20190303T154145Z
UID:5d4c6843-9300-4f91-8d88-6094d4b0b840
SUMMARY:test7 - edited
RECURRENCE-ID;TZID=Europe/Berlin:20190319T040000
DTSTART;TZID=Europe/Berlin:20190319T040000
DTEND;TZID=Europe/Berlin:20190319T050000
TRANSP:OPAQUE
X-MOZ-GENERATION:3
SEQUENCE:2
LOCATION:location
DESCRIPTION:
CLASS:
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/three_events.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J
SUMMARY:test4
CLASS:PUBLIC
STATUS:CONFIRMED
RRULE:FREQ=DAILY;COUNT=3;INTERVAL=3
DTSTART;TZID=Europe/Berlin:20190304T000000
DTEND;TZID=Europe/Berlin:20190304T010000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/x_wr_timezone_simple_events_issue_59.ics`

```ics
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:This calendar features two events of which DTSTART and DTEND must be changed.
X-WR-TIMEZONE:America/New_York
BEGIN:VEVENT
DTSTART:20211222T170000Z
DTEND:20211222T180000Z
DTSTAMP:20211228T180046Z
UID:3bc4jff97631or97ntnk75n4se@google.com
CREATED:20211222T190737Z
DESCRIPTION:
LAST-MODIFIED:20211222T190947Z
LOCATION:
SEQUENCE:2
STATUS:CONFIRMED
SUMMARY:Google Calendar says this is noon to 1PM on 12/22/2021
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20211223T020000Z
DTEND:20211223T030000Z
DTSTAMP:20211228T180046Z
UID:14n7h56i35m32ukcq76s46d45p@google.com
CREATED:20211222T190622Z
DESCRIPTION:
LAST-MODIFIED:20211222T190622Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Google says this is 9PM to 10PM on 12/22/2021
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/calendars/zero_size_event.ics`

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SabreDAV//SabreDAV//EN
CALSCALE:GREGORIAN
X-WR-CALNAME:test
X-APPLE-CALENDAR-COLOR:#e78074
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20190303T111937
DTSTAMP:20190303T111937
LAST-MODIFIED:20190303T111937
UID:UYDQSG9TH4DE0WM3QFL2J
SUMMARY:zero size event
DTSTART;TZID=Europe/Berlin:20190304T080000
END:VEVENT
END:VCALENDAR

```

### `recurring_ical_events/test/conftest.py`

```py
import sys
import time
from datetime import timezone
from pathlib import Path

import dateutil
import icalendar
import pytest
import pytz

from recurring_ical_events import of

try:
    import zoneinfo as _zoneinfo
except ImportError:
    import backports.zoneinfo as _zoneinfo

HERE = Path(__file__).parent
REPO = Path(HERE).parent.parent

sys.path.append(str(REPO))


CALENDARS_FOLDER = HERE / "calendars"
# set the default time zone
# see https://stackoverflow.com/questions/1301493/setting-timezone-in-python
time.tzset()


class ICSCalendars:
    """A collection of parsed ICS calendars

    components is the argument to pass to the of function"""

    Calendar = icalendar.Calendar
    components = None
    skip_bad_series = None

    def __init__(self, tzp):
        """Create ICS calendars in a specific timezone."""
        self.tzp = tzp

    def get_calendar(self, content):
        """Return the calendar given the content."""
        self.tzp()
        return self.Calendar.from_ical(content)

    def __getitem__(self, name):
        return getattr(self, name)

    @property
    def raw(self):
        return ICSCalendars(self.tzp)

    def consistent_tz(self, dt):
        """Make the datetime consistent with the time zones used in these calendars."""
        assert dt.tzinfo is None or "pytz" in dt.tzinfo.__class__.__module__, (
            "We need pytz time zones for now."
        )
        return dt

    def _of(self, calendar):
        """Return the calendar but also with selected components."""
        kw = {}
        if self.skip_bad_series is not None:
            kw["skip_bad_series"] = self.skip_bad_series
        if self.components is not None:
            kw["components"] = self.components
        return of(calendar, **kw)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tzp.__name__})"


_calendar_names = []
for calendar_path in CALENDARS_FOLDER.iterdir():
    content = calendar_path.read_bytes()

    @property
    def get_calendar(self, content=content):  # noqa: PLR0206
        return self.get_calendar(content)

    attribute_name = calendar_path.stem
    setattr(ICSCalendars, attribute_name, get_calendar)
    _calendar_names.append(attribute_name)


class Calendars(ICSCalendars):
    """Collection of calendars from recurring_ical_events"""

    def get_calendar(self, content):
        return self._of(ICSCalendars.get_calendar(self, content))


class ReversedCalendars(ICSCalendars):
    """All test should run in reversed item order.

    RFC5545:
        This memo imposes no ordering of properties within an iCalendar object.
    """

    def get_calendar(self, content):
        """Calendar traversing events in reversed order."""
        calendar = ICSCalendars.get_calendar(self, content)
        _walk = calendar.walk

        def walk(*args, **kw):
            """Return properties in reversed order."""
            return reversed(_walk(*args, **kw))

        calendar.walk = walk
        return self._of(calendar)


if hasattr(icalendar, "use_pytz") and hasattr(icalendar, "use_zoneinfo"):
    tzps = [icalendar.use_pytz, icalendar.use_zoneinfo]
else:
    tzps = [lambda: ...]


@pytest.fixture(params=tzps, scope="module")
def tzp(request):
    """The timezone provider supported by icalendar."""
    return request.param


# for parametrizing fixtures, see https://docs.pytest.org/en/latest/fixture.html#parametrizing-fixtures
@pytest.fixture(params=[Calendars, ReversedCalendars])
def calendars(request, tzp) -> ICSCalendars:
    """The calendars we can use in the tests."""
    return request.param(tzp)


@pytest.fixture
def todo():
    """Skip a test because it needs to be written first."""
    pytest.skip("This test is not yet implemented.")


@pytest.fixture(scope="module")
def zoneinfo():
    """Return the zoneinfo module if present, otherwise skip the test.

    Uses backports.zoneinfo or zoneinfo.
    """
    return _zoneinfo


@pytest.fixture(scope="module")
def ZoneInfo(zoneinfo):
    """Shortcut for zoneinfo.ZoneInfo."""
    return zoneinfo.ZoneInfo


@pytest.fixture(
    scope="module",
    params=[pytz.utc, _zoneinfo.ZoneInfo("UTC"), timezone.utc, dateutil.tz.UTC],
)
def utc(request):
    """Return all the UTC implementations."""
    return request.param


class DoctestZoneInfo(_zoneinfo.ZoneInfo):
    """Constent ZoneInfo representation for tests."""

    def __repr__(self):
        return f"ZoneInfo(key={self.key!r})"


def doctest_print(obj):
    """doctest print"""
    if isinstance(obj, bytes):
        obj = obj.decode("UTF-8")
    print(str(obj).strip().replace("\r\n", "\n").replace("\r", "\n"))


@pytest.fixture
def env_for_doctest(monkeypatch):
    """Modify the environment to make doctests run."""
    monkeypatch.setitem(sys.modules, "zoneinfo", _zoneinfo)
    monkeypatch.setattr(_zoneinfo, "ZoneInfo", DoctestZoneInfo)
    from icalendar.timezone.zoneinfo import ZONEINFO

    monkeypatch.setattr(ZONEINFO, "utc", _zoneinfo.ZoneInfo("UTC"))
    return {
        "print": doctest_print,
        "CALENDARS": CALENDARS_FOLDER,
    }


# remove invalid names
_calendar_names.remove("end_before_start_event")
_calendar_names.sort()


@pytest.fixture(scope="module", params=_calendar_names)
def calendar_name(request) -> str:
    """All the calendar names."""
    return request.param


@pytest.fixture
def alarms(calendars) -> ICSCalendars:
    """The calendars to query for alarms.

    This modifies the calendars fixture.
    """
    calendars.components = ["VALARM"]
    return calendars

```

### `recurring_ical_events/test/py.py`

```py
# shim for pylib going away
# if pylib is installed this file will get skipped
# (`py/__init__.py` has higher precedence)
from __future__ import annotations

import sys

from _pytest._py import error, path

sys.modules["py.error"] = error
sys.modules["py.path"] = path

__all__ = ["error", "path"]

```

### `recurring_ical_events/test/test_after.py`

```py
"""Test getting events in a specific order."""

import datetime

import pytest
import pytz


def test_a_calendar_with_no_event_has_no_events(calendars):
    """No event"""
    for _ in calendars.no_events.after(datetime.datetime(2024, 3, 30, 12, 0, 0)):
        assert False, "No event expected."


def test_a_calendar_with_events_before_has_no_events_later(calendars):
    """No event is found."""
    for _ in calendars.event_10_times.after(
        datetime.datetime(2024, 3, 30, 12, 0, 0),
    ):
        assert False, "No event expected."


def test_different_time_zones():
    """If events with different time zones are compared."""
    pytest.skip("TODO")


def test_no_event_is_returned_twice(calendars):
    """Long events should not be returned several times."""
    i = 1
    for event in calendars.after_many_events_in_order.after("20240324"):
        assert event["SUMMARY"] == f"event {i}"
        i += 1
    assert i == 8


def test_todo_with_no_dtstart():
    pytest.skip("TODO")


@pytest.mark.parametrize(
    ("date", "count"),
    [
        ("20200113", 10),
        ("20200114", 9),
        ("20200115", 8),
        ("20200116", 7),
        ("20200117", 6),
        ("20200118", 5),
        ("20200119", 4),
        ("20200120", 3),
        ("20200121", 2),
        ("20200122", 1),
        ("20200123", 0),
        (datetime.datetime(2020, 1, 19, 0, 0, 0, tzinfo=pytz.UTC), 4),
    ],
)
def test_get_events_in_series(calendars, date, count):
    """Get a few events in a series."""
    events = list(calendars.event_10_times.after(date))
    assert len(events) == count, f"{count} events expected"


def test_zero_size_event_is_included(calendars):
    """If a zero size event happens exactly at the earliest_end, then it is included."""
    event = list(calendars.zero_size_event.after("20190304T080000Z"))[0]
    assert event["DTSTART"].to_ical() == b"20190304T080000"


def test_zero_size_event_is_excluded_one_second_later(calendars):
    """If a zero size event happens exactly at the earliest_end, then it is included."""
    assert not list(calendars.zero_size_event.after("20190304T080001Z"))

```

### `recurring_ical_events/test/test_at_function.py`

```py
from datetime import date, datetime

import pytest


@pytest.mark.parametrize(
    ("a_date", "count"),
    [
        # Year
        (2018, 3),
        ((2018,), 3),
        # Month
        ((2018, 1), 3),
        # Day
        ((2018, 1, 11), 1),
        (date(2018, 1, 11), 1),
        ("20180111", 1),
        ((2018, 1, 9), 0),
        (date(2018, 1, 9), 0),
        ("20180109", 0),
        # Datetime
        (datetime(2018, 1, 11, 10, 0, 0), 1),
        (datetime(2018, 1, 9, 10, 0, 0), 0),
    ],
)
def test_at_input_arguments(a_date, count, calendars):
    events = calendars.duration.at(a_date)
    assert len(events) == count

```

### `recurring_ical_events/test/test_bad_rrule_format.py`

```py
import pytest

from recurring_ical_events.errors import BadRuleStringFormat


def test_bad_rrule_until_format(calendars):
    with pytest.raises(BadRuleStringFormat, match=r"UNTIL parameter is missing"):
        calendars.bad_rrule_missing_until_event.at(2019)

```

### `recurring_ical_events/test/test_convert_inputs.py`

```py
"""Test that different inputs are understood

Also see test_time_arguments.py
"""

import pytest


@pytest.mark.parametrize(
    ("start", "stop", "event_count"),
    [
        (2020, 2021, 366),
        ((2020,), (2021,), 366),
        ((2019, 2), (2020, 2), 334),
        ((2019, 2, 4), (2019, 5, 21), 78),
        ("20190204", "20190521", 78),
        ("20190204T000000Z", "20190521T235959Z", 79),  # 78 = that of the day
    ],
)
def test_calendar_between_allows_tuple(calendars, start, stop, event_count):
    events = calendars.one_day_event_repeat_every_day.between(start, stop)
    assert len(events) == event_count

```

### `recurring_ical_events/test/test_count.py`

```py
"""Create an test the count() method.

We want to be able to count the amount of events really fast.
"""

import pytest


@pytest.mark.parametrize(
    ("calendar", "count"),
    [
        ("issue_20_exdate_ignored", 7),
        ("issue_148_ignored_exdate", 2),
        ("issue_117_until_before_dtstart", 0),
    ],
)
def test_check_count_of_calendars(calendars, calendar, count):
    """We count the events."""
    assert calendars[calendar].count() == count

```

### `recurring_ical_events/test/test_daylight_saving_time.py`

```py
import datetime

import pytest
from pytz import timezone

berlin = timezone("Europe/Berlin")


@pytest.mark.parametrize(
    ("date", "time"),
    [
        (
            (2019, 3, 20),
            berlin.localize(datetime.datetime(2019, 3, 20, 19)),
        ),  # winter time, UTC+1
        (
            (2019, 4, 24),
            berlin.localize(datetime.datetime(2019, 4, 24, 19)),
        ),  # summer time UTC+2
    ],
)
def test_daylight_saving_events(calendars, date, time):
    """Test the event 7uartkcnhf0elbvs8md0itrf6c@google.com."""
    event = calendars.daylight_saving_time.at(date)[0]
    expected_time = calendars.consistent_tz(time)
    print(event["UID"])
    print(event["DTEND"].dt)
    assert event["DTSTART"].dt == expected_time

```

### `recurring_ical_events/test/test_deleted_entries.py`

```py
def test_one_deleted_event(calendars):
    events = list(calendars.each_week_but_one_deleted.all())
    assert len(events) == 7


def test_one_deleted_event_2(calendars):
    events = list(calendars.each_week_but_two_deleted.all())
    assert len(events) == 6

```

### `recurring_ical_events/test/test_duration.py`

```py
"""
Test the DURATION property.

Not all events have an end.
Some events define no explicit end and some a DURATION.
RFC: https://www.kanzaki.com/docs/ical/duration.html

"""

import pytest


@pytest.mark.parametrize(
    ("date", "count"),
    [
        # event 3 days
        ("20180110", 1),
        ("20180111", 1),
        ("20180112", 1),
        ("20180109", 0),
        ("20180114", 0),
        # event 3 hours
        ((2018, 1, 15, 10), 1),
        ((2018, 1, 15, 11), 1),
        ((2018, 1, 15, 12), 1),
        ((2018, 1, 15, 9), 0),
        ((2018, 1, 15, 14), 0),
        # event with no duration nor end
        ((2018, 1, 20), 1),
        ((2018, 1, 19), 0),
        ((2018, 1, 21), 0),
    ],
)
def test_events_expected(date, count, calendars):
    events = calendars.duration.at(date)
    assert len(events) == count


@pytest.mark.parametrize(
    ("date", "summary", "expected_hours"),
    [
        ("20190318", "original event", 1),
        ("20190319", "edited duration", 3),
        ("20190320", "original event", 1),
    ],
)
def test_duration_is_edited(calendars, date, summary, expected_hours):
    """Test that the duration of an event can be edited."""
    events = calendars.duration_edited.at(date)
    assert len(events) == 1
    event = events[0]
    event_hours = (event["DTEND"].dt - event["DTSTART"].dt).total_seconds() / 3600
    assert summary == event["SUMMARY"], "we should have the correct event"
    assert event_hours == expected_hours, (
        "the duration is only edited in the edited event"
    )

```

### `recurring_ical_events/test/test_end_before_start_event.py`

```py
from datetime import datetime

import pytest

from recurring_ical_events.errors import PeriodEndBeforeStart
from recurring_ical_events.util import time_span_contains_event


def test_span_in_wrong_order():
    """The timespan only works if the order is correct."""
    with pytest.raises(PeriodEndBeforeStart):
        time_span_contains_event(
            datetime(2019, 10, 13),
            datetime(2019, 10, 12),
            datetime(2019, 10, 13),
            datetime(2019, 10, 14),
        )


def test_event_in_wrong_order():
    """The timespan only works if the order is correct."""
    with pytest.raises(PeriodEndBeforeStart):
        time_span_contains_event(
            datetime(2019, 10, 11),
            datetime(2019, 10, 12),
            datetime(2019, 10, 15),
            datetime(2019, 10, 14),
        )

```

### `recurring_ical_events/test/test_event_values_and_edits.py`

```py
"""This tests the values of the event even when edited."""

import datetime

import pytest


def test_two_events_have_the_same_values(calendars):
    events = calendars.three_events_one_edited.all()
    unedited_events = [event for event in events if event["SUMMARY"] == "test7"]
    assert len(unedited_events) == 2


def test_one_event_is_edited(calendars):
    events = calendars.three_events_one_edited.all()
    edited_events = [event for event in events if event["SUMMARY"] == "test7 - edited"]
    assert len(edited_events) == 1
    edited_event = edited_events[0]
    assert edited_event["LOCATION"] == "location"


def test_three_events_total(calendars):
    events = list(calendars.three_events_one_edited.all())
    assert len(events) == 3


# def test_edited_event_as_part_of_exdate(todo):
#    """What happens when an edited event is part of the exdate?"""
# There is nothing written in the RFC 5545 about this case
# I would assume that a software creating an event and exluding it is faulty.


def test_edited_event_as_part_of_exrule():
    """What happens when an edited event is part of the exrule?

    Well nothing, EXRULE is not supported by this module."""


@pytest.mark.parametrize(
    ("date", "hour"),
    [
        ((2019, 3, 7), 2),
        ((2019, 3, 8), 1),
        ((2019, 3, 9), 3),
        ((2019, 3, 10), 2),
    ],
)
def test_event_moved_in_time(calendars, date, hour):
    events = calendars.recurring_events_moved.at(date)
    assert len(events) == 1
    event = events[0]
    assert event["DTSTART"].dt.hour == hour


@pytest.mark.parametrize(
    ("date", "duration"),
    [
        ((2019, 3, 7), datetime.timedelta(hours=1)),
        ((2019, 3, 8), datetime.timedelta(hours=2)),
        ((2019, 3, 9), datetime.timedelta(minutes=30)),
        ((2019, 3, 10), datetime.timedelta(days=1)),
    ],
)
def test_event_moved_in_time_2(calendars, date, duration):
    events = calendars.recurring_events_changed_duration.at(date)
    assert len(events) == 1
    event = events[0]
    assert event["DTEND"].dt - event["DTSTART"].dt == duration

```

### `recurring_ical_events/test/test_example_function.py`

```py
"""Test the example function."""

import pytest

from recurring_ical_events.examples import example_calendar


def test_valid_example_is_returned():
    """We can get a valid example."""
    c = example_calendar("fablab_cottbus")
    assert c["X-FROM-URL"] == "http://blog.fablab-cottbus.de"


def test_we_can_remove_the_ics():
    """We can get a valid example."""
    assert example_calendar("duration") == example_calendar("duration.ics")


def test_we_know_which_files_are_ok():
    """The error message shows us which examples to use."""
    with pytest.raises(ValueError) as e:
        example_calendar("missing")
    assert "issue_4" in str(e.value)

```

### `recurring_ical_events/test/test_examples.py`

```py
import datetime

import pytest


def test_fablab_cottbus(calendars):
    """This calendar threw an exception.

    TypeError: can't compare offset-naive and offset-aware datetimes
    """
    today = datetime.datetime(2019, 3, 4, 16, 52, 10, 215209)
    one_year_ahead = today.replace(year=today.year + 1)
    one_year_before = today.replace(year=today.year - 1)
    calendars.fablab_cottbus.between(one_year_before, one_year_ahead)


def test_example_from_README(calendars):
    """The examples from the README should be tested so we make no
    false promises.
    """

    start_date = (2019, 3, 5)
    end_date = (2019, 4, 1)

    events = calendars.one_day_event_repeat_every_day.between(start_date, end_date)
    for event in events:
        start = event["DTSTART"].dt
        duration = event["DTEND"].dt - event["DTSTART"].dt
        print(f"start {start} duration {duration}")
    assert event


def test_no_dtend(calendars):
    """This calendar has events which have no DTEND.

    KeyError: 'DTEND'
    """
    list(calendars.discourse_no_dtend.all())


def test_date_events_are_in_the_date(calendars):
    events = calendars.Germany.at((2014, 5, 11))
    assert len(events) == 1
    event = events[0]
    assert event["SUMMARY"] == "Germany: Mother's Day [Not a public holiday]"
    assert isinstance(event["DTSTART"].dt, datetime.date)


mb_on_tour_dates = [
    (2018, 9, 22),
    (2018, 10, 20),
    (2018, 11, 17),
    (2018, 12, 8),
    (2019, 1, 12),
    (2019, 1, 27),
    (2019, 2, 9),
    (2019, 2, 24),
    (2019, 3, 23),
    (2019, 4, 27),
    (2019, 5, 25),
    (2019, 6, 22),
]


@pytest.mark.parametrize("date", mb_on_tour_dates)
def test_events_are_scheduled(calendars, date):
    events = calendars.machbar_16_feb_2019.at(date)
    assert len(events) == 1


@pytest.mark.parametrize(
    "month",
    [
        (2018, 9),
        (2018, 10),
        (2018, 11),
        (2018, 12),
        (2019, 1),
        (2019, 2),
        (2019, 3),
        (2019, 4),
        (2019, 5),
        (2019, 6),
        (2019, 7),
    ],
)
def test_no_more_events_are_scheduled(calendars, month):
    dates = [date for date in mb_on_tour_dates if date[:2] == month]
    number_of_dates = len(dates)
    events = calendars.machbar_16_feb_2019.at(month)
    mb_events = [event for event in events if "mB-onTour" in event["SUMMARY"]]
    assert len(mb_events) == number_of_dates


def test_german_holidays(calendars):
    """Test the calendar from
    https://www.calendarlabs.com/ical-calendar/ics/46/Germany_Holidays.ics
    """
    holidays = calendars.Germany_Holidays.at(2020)
    assert len(holidays) == 17


def test_exdate_date(calendars):
    """The EXDATE can be a date, too.

    See https://github.com/niccokunzmann/python-recurring-ical-events/pull/121
    """
    assert calendars.date_exclude.at("20231216") == []


@pytest.mark.parametrize(
    ("date", "count"),
    [
        ("20240923", 0),
        ("20240924", 3),
        ("20240925", 0),
        ("20240926", 3),
        ("20240927", 0),
    ],
)
def test_same_events_at_same_time(calendars, date, count):
    """Make sure that events can be moved to the same time."""
    assert len(calendars.same_event_recurring_at_same_time.at(date)) == count

```

### `recurring_ical_events/test/test_extend_classes.py`

```py
"""This tests extneding and modifying the behaviour of recurring ical events."""

from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

import pytest
from icalendar.cal import Component

from recurring_ical_events import (
    of,
)
from recurring_ical_events.adapters.event import EventAdapter
from recurring_ical_events.adapters.journal import JournalAdapter
from recurring_ical_events.adapters.todo import TodoAdapter
from recurring_ical_events.occurrence import Occurrence
from recurring_ical_events.selection.all import AllKnownComponents
from recurring_ical_events.selection.base import SelectComponents
from recurring_ical_events.selection.name import ComponentsWithName
from recurring_ical_events.series import Series

if TYPE_CHECKING:
    from icalendar.cal import Component


class SelectUID1(SelectComponents):
    """Collect only one UID."""

    def __init__(self, uid: str) -> None:
        self.uid = uid

    def collect_series_from(
        self, source: Component, suppress_errors: tuple[Exception]
    ) -> Sequence[Series]:
        return [
            series
            for adapter in [EventAdapter, JournalAdapter, TodoAdapter]
            for series in adapter.collect_series_from(source, suppress_errors)
            if series.uid == self.uid
        ]


class SelectUID2(AllKnownComponents):
    def __init__(self, uid: str) -> None:
        super().__init__()
        self.uid = uid

    def collect_series_from(
        self, source: Component, suppress_errors: tuple[Exception]
    ) -> Sequence[Series]:
        return [
            series
            for series in super().collect_series_from(source, suppress_errors)
            if series.uid == self.uid
        ]


class SelectUID3(SelectComponents):
    def __init__(self, uid: str) -> None:
        self.uid = uid

    def collect_series_from(
        self,
        source: Component,
        suppress_errors: tuple[Exception],  # noqa: ARG002
    ) -> Sequence[Series]:
        components: list[Component] = []
        for component in source.walk("VEVENT"):
            if component.get("UID") == self.uid:
                components.append(EventAdapter(component))  # noqa: PERF401
        print(components)
        return [Series(components)] if components else []


@pytest.mark.parametrize("collector", [SelectUID1, SelectUID2, SelectUID3])
def test_collect_only_one_uid(calendars, collector):
    """Test that only one UID is used."""
    uid = "4mm2ak3in2j3pllqdk1ubtbp9p@google.com"
    query = of(calendars.raw.machbar_16_feb_2019, components=[collector(uid)])
    assert query.count() == 1


class MyOccurrence(Occurrence):
    """An occurrence that modifies the component."""

    def as_component(self, keep_recurrence_attributes: bool) -> Component:  # noqa: FBT001
        """Return a shallow copy of the source component and modify some attributes."""
        component = super().as_component(keep_recurrence_attributes)
        component["X-MY-ATTRIBUTE"] = "my occurrence"
        return component


def test_added_attributes(calendars):
    """Test that attributes are added."""
    query = of(
        calendars.raw.one_event,
        components=[AllKnownComponents(occurrence=MyOccurrence)],
    )
    event = next(query.all())
    assert event["X-MY-ATTRIBUTE"] == "my occurrence"


@pytest.mark.parametrize(
    ("calendar", "count", "collector"),
    [
        # all
        ("one_event", 1, AllKnownComponents()),
        ("issue_97_simple_todo", 1, AllKnownComponents()),
        ("issue_97_simple_journal", 1, AllKnownComponents()),
        # events
        ("one_event", 1, ComponentsWithName("VEVENT")),
        ("issue_97_simple_todo", 0, ComponentsWithName("VEVENT")),
        ("issue_97_simple_journal", 0, ComponentsWithName("VEVENT")),
        # todos
        ("one_event", 0, ComponentsWithName("VTODO")),
        ("issue_97_simple_todo", 1, ComponentsWithName("VTODO")),
        ("issue_97_simple_journal", 0, ComponentsWithName("VTODO")),
        # journals
        ("one_event", 0, ComponentsWithName("VJOURNAL")),
        ("issue_97_simple_todo", 0, ComponentsWithName("VJOURNAL")),
        ("issue_97_simple_journal", 1, ComponentsWithName("VJOURNAL")),
    ],
)
def test_we_collect_all_components(
    calendars, calendar, count, collector: SelectComponents
):
    """Check that the calendars have the right amount of series collected."""
    series = collector.collect_series_from(calendars.raw[calendar], [])
    print(series)
    assert len(series) == count

```

### `recurring_ical_events/test/test_issue_101_select_components.py`

```py
"""These tests make sure that you can select which components should be returned.

By default, it should be events.
If a component is not supported, an error is raised.
"""

import pytest


@pytest.mark.parametrize(
    ("components", "count", "calendar", "message"),
    [
        (None, 0, "issue_97_simple_todo", "by default, only events are returned"),
        (None, 0, "issue_97_simple_journal", "by default, only events are returned"),
        ([], 0, "rdate", "no components, no result"),
        ([], 0, "issue_97_simple_todo", "no components, no result"),
        ([], 0, "issue_97_simple_journal", "no components, no result"),
        (["VEVENT"], 0, "issue_97_simple_todo", "no events in the calendar"),
        (["VEVENT"], 0, "issue_97_simple_journal", "no events in the calendar"),
        (["VJOURNAL"], 0, "issue_97_simple_todo", "no journal, just a todo"),
        (["VTODO"], 1, "issue_97_simple_todo", "one todo is found"),
        (["VTODO"], 0, "issue_97_simple_journal", "no todo, just a journal"),
        (["VJOURNAL"], 1, "issue_97_simple_journal", "one journal is found"),
        (["VTODO", "VEVENT"], 0, "issue_97_simple_journal", "no todo, just a journal"),
        (["VJOURNAL", "VEVENT"], 1, "issue_97_simple_journal", "one journal is found"),
        (
            ["VJOURNAL", "VEVENT", "VTODO"],
            1,
            "issue_97_simple_journal",
            "one journal is found",
        ),
    ],
)
def test_components_and_their_count(calendars, components, count, calendar, message):
    calendars.components = components
    repeated_components = calendars[calendar].at(2022)
    print(repeated_components)
    assert len(repeated_components) == count, f"{message}: {components}, {calendar}"


@pytest.mark.parametrize(
    "component",
    [
        "VTIMEZONE",  # existing but not supported
        "vevent",  # misspelled
        "ALDHKSJHK",  # does not exist
    ],
)
def test_unsupported_component_raises_error(component, calendars):
    """If a component is not recognized, we want to inform the user."""
    with pytest.raises(ValueError) as error:
        calendars.components = [component]
        calendars.rdate  # noqa: B018
    assert f'"{component}"' in str(error)

```

### `recurring_ical_events/test/test_issue_107_omitting_last_event.py`

```py
"""bug: recurring event series that start in daylight savings time and end in standard time omit last event

Using a calendar application, I created a weekly event series in Pacific Standard Time that begins on January 5th and ends on June 8th. I filtered out events using between from today's date (~January 2023) and 1 year in the future (~January 2024). However, it incorrectly omitted the last event in the series on June 8th.

Upon further investigation, it seems to just be an issue for a recurring event series that begin in standard time but end in daylight savings time.

see https://github.com/niccokunzmann/python-recurring-ical-events/issues/107
see also test_issue_20_exdate_ignored.py - same problem with pytz
"""

import datetime


def test_last_event_is_present(calendars):
    today = datetime.date(2023, 1, 30)
    future = today + datetime.timedelta(days=365)
    events = calendars.issue_107_omitting_last_event.between(today, future)
    dates = [event["DTSTART"].dt.date() for event in events]
    assert datetime.date(2023, 6, 1) in dates, "event before last is present"
    assert datetime.date(2023, 6, 8) in dates, "last event is present"

```

### `recurring_ical_events/test/test_issue_113_period_in_rdate.py`

```py
"""This tests that RDATE can be a PERIOD.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/113

    Value Type:  The default value type for this property is DATE-TIME.
       The value type can be set to DATE or PERIOD.

    If the "RDATE" property is
    specified as a PERIOD value the duration of the recurrence
    instance will be the one specified by the "RDATE" property, and
    not the duration of the recurrence instance defined by the
    "DTSTART" property.

"""

from datetime import datetime, timedelta

import pytz


def test_start_of_rdate(calendars):
    """The event starts on that time."""
    event = calendars.issue_113_period_in_rdate.at("20231213")[0]
    expected_start = pytz.timezone("America/Vancouver").localize(
        datetime(2023, 12, 13, 12, 0)
    )
    start = event["DTSTART"].dt
    assert start == expected_start


def test_end_of_rdate(calendars):
    """The event starts on that time."""
    event = calendars.issue_113_period_in_rdate.at("20231213")[0]
    assert event["DTEND"].dt == pytz.timezone("America/Vancouver").localize(
        datetime(2023, 12, 13, 15, 0)
    )


def test_rdate_with_a_period_with_duration(calendars):
    """Check that we can process RDATE with a duration as second value."""
    events = calendars.issue_113_period_rdate_duration.at("20240913")
    assert len(events) == 1, "We found the event with the rdate."
    event = events[0]
    duration = event["DTEND"].dt - event["DTSTART"].dt
    assert duration == timedelta(hours=2)

```

### `recurring_ical_events/test/test_issue_117_until_before_dtstart.py`

```py
"""The atlassian confluence calendar sets the until value lower than the DTSTART when then event is deleted.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/117
"""


def test_event_is_deleted(calendars):
    """No event takes place."""
    assert not list(calendars.issue_117_until_before_dtstart.all())

```

### `recurring_ical_events/test/test_issue_128_only_first_event.py`

```py
"""The atlassian confluence calendar sets the count value to -1 when future events are deleted.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/128
"""

import pytest

import recurring_ical_events.constants


def test_all_events_are_present(calendars):
    """All events are shown and not just the first one."""
    assert len(list(calendars.issue_128_only_first_event.all())) == 7


@pytest.mark.parametrize(
    ("string", "matches"),
    [
        ("COUNT=1", False),
        ("COUNT=1;", False),
        ("COUNT=-1", True),
        ("COUNT=-1;", True),
        ("COUNT=-100", True),
        ("COUNT=-100;", True),
    ],
)
def test_matching_negative_count(string, matches):
    """Make sure the general replacement pattern works."""
    actually_matches = (
        recurring_ical_events.constants.NEGATIVE_RRULE_COUNT_REGEX.match(string)
        is not None
    )
    assert actually_matches == matches

```

### `recurring_ical_events/test/test_issue_132_swapped_start_and_end.py`

```py
"""Check that we can still compute if start and end are swapped."""

from datetime import datetime

import pytest


def test_event_case(calendars):
    """Test an event with swapped start and end."""
    event = calendars.issue_132_swapped_start_and_end.first
    assert event.start.replace(tzinfo=None) == datetime(2023, 12, 18, 23, 30)
    assert event.end.replace(tzinfo=None) == datetime(2023, 12, 18, 23, 45)


def test_todo_case(calendars):
    """Test an event with swapped start and end."""
    calendars.components = ["VTODO"]
    todo = calendars.issue_132_swapped_start_and_end.first
    print(todo)
    assert todo.start.replace(tzinfo=None) == datetime(2023, 12, 18, 23, 30)
    assert todo.end.replace(tzinfo=None) == datetime(2023, 12, 18, 23, 45)


@pytest.mark.parametrize("skip_invalid", [True, False])
def test_old_example_works_now(calendars, ZoneInfo, skip_invalid):
    """The old tests works now."""
    calendars.skip_bad_series = skip_invalid
    events = calendars.end_before_start_event.at(2019)
    print(list(calendars.end_before_start_event.all()))
    assert len(events) == 1
    event = events[0]
    assert event.start == datetime(
        2019, 3, 4, 8, tzinfo=ZoneInfo("Europe/Berlin")
    )  # 20190304T080000
    assert event.end == datetime(
        2019, 3, 4, 8, 30, tzinfo=ZoneInfo("Europe/Berlin")
    )  # 20190304T080300

```

### `recurring_ical_events/test/test_issue_139_no_duration.py`

```py
"""We want to check that the DURATION is removed.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/139
"""


def test_no_duration_in_event(calendars):
    """Check that there is no DURATION in the event."""
    for event in calendars.duration.all():
        assert "DURATION" not in event
        assert "DTEND" in event

```

### `recurring_ical_events/test/test_issue_148_ignored_exdate_in_higher_sequence.py`

```py
"""Events can be edited and a higher sequence number assigned.

In case the whole event is edited and receives a new sequence number,
the exdate should be considered.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/148
"""

from datetime import date

import pytest


def test_total_events(calendars):
    """We should remove the edited event."""
    events = list(calendars.issue_148_ignored_exdate.all())
    assert len(events) == 2


def test_the_exdate_is_not_available(calendars):
    """Make sure we do not get an event on the ecluded date."""
    events = calendars.issue_148_ignored_exdate.at("20240715")
    assert not events


@pytest.mark.parametrize(
    ("date", "summary"),
    [
        ("20240701", "test123 - edited"),
        ("20240729", "test123 - edited"),
    ],
)
def test_summary_is_modified(calendars, date, summary):
    """The summary of the edited event is used."""
    events = calendars.issue_148_ignored_exdate.at(date)
    assert events
    event = events[0]
    print(event)
    assert event["SUMMARY"] == summary


@pytest.mark.parametrize(
    ("date", "count", "message"),
    [
        ("20240701", 1, "The original event is present"),
        (
            "20240715",
            1,
            "The formerly excluded event is present after edit - EXDATE removed",
        ),
        (
            "20240717",
            0,
            "The formerly added event is removed after edit - RDATE removed",
        ),
        (
            "20240729",
            0,
            "The formerly present recurring event is now excluded - EXDATE added",
        ),
        ("20240730", 1, "Now, there is a new RDATE - RDATE added"),
    ],
)
def test_rdate_and_exdate_are_updated(calendars, date, count, message):
    """If we have RDATE and EXDATE present, we would like to update those and
    not use the old values."""
    events = calendars.issue_148_exdate_and_rdate_updated.at(date)
    print(events)
    assert len(events) == count, message


@pytest.mark.parametrize(
    ("date", "count", "message"),
    [
        ("20240701", 1, "The original event is present"),
        ("20240715", 0, "The formerly excluded event is absent"),
        ("20240717", 1, "The formerly added event is there"),
        ("20240729", 1, "The formerly present recurring event is there"),
        ("20240730", 0, "There is no RDATE, yet"),
    ],
)
def test_rdate_and_exdate_are_unedited(calendars, date, count, message):
    """If we have RDATE and EXDATE present, we would like to check the the
    value are used before edit."""
    events = calendars.issue_148_exdate_and_rdate_unedited.at(date)
    print(events)
    assert len(events) == count, message


def test_edge_case_1(calendars):
    """Check the edge case.

    Here, we do not have a modified event.
    See https://github.com/niccokunzmann/python-recurring-ical-events/issues/163#issuecomment-2301748873
    """
    events = list(calendars["issue_148_edge_case_1"].all())
    assert len(events) == 2
    starts = [event["DTSTART"].dt for event in events]
    assert date(2024, 7, 2) not in starts, "This event is not present in edge case 1"
    assert date(2024, 7, 1) in starts
    assert date(2024, 7, 29) in starts


def test_edge_case_2(calendars):
    """Check the edge case.

    This edge case shows that we have a modified event.
    See https://github.com/niccokunzmann/python-recurring-ical-events/issues/163#issuecomment-2301748873
    """
    events = list(calendars["issue_148_edge_case_2"].all())
    assert len(events) == 3
    starts = [event["DTSTART"].dt for event in events]
    assert date(2024, 7, 2) in starts
    assert date(2024, 7, 1) in starts
    assert date(2024, 7, 29) in starts

```

### `recurring_ical_events/test/test_issue_15.py`

```py
"""This file tests the issue 15.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/15

calendars = <conftest.ReversedCalendars object at 0x79c21bcb9b70>

    def test_rdate_does_not_double_rrule_entry(calendars):
>       events = calendars.rdate.at("20140705")

test/test_rdate.py:56:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
recurring_ical_events.py:277: in at
    return self.between(dt, dt + self._DELTAS[len(date) - 3])
recurring_ical_events.py:306: in between
    add_event(repetition.as_vevent())
recurring_ical_events.py:292: in add_event
    if event["SEQUENCE"] < other["SEQUENCE"]:

"""


def test_sequence_is_not_present(calendars):
    events = calendars.issue_15_duplicated_events.at("20130803")
    assert len(events) == 3

```

### `recurring_ical_events/test/test_issue_151_macos_linux_difference.py`

```py
"""This tests if there is a difference between macOS and Linux

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/151
"""

from datetime import datetime, timezone


def test_count_events_from_issue(calendars):
    """Avents were omitted through version upgrade from 2.2.2 to 2.2.3."""

    start_time = datetime.fromtimestamp(1722564000, timezone.utc)
    end_time = datetime.fromtimestamp(1722567600, timezone.utc)
    print(f"from {start_time.timestamp()} to {end_time.timestamp()}")
    events = calendars.issue_151_macos_linux_difference.between(start_time, end_time)
    for event in events:
        print(event["UID"], event["DTSTART"], event["SUMMARY"])
    assert len(events) == 1


def test_check_event_count_for_that_day(calendars):
    """Avents were omitted through version upgrade from 2.2.2 to 2.2.3."""

    events = calendars.issue_151_macos_linux_difference.at("20240801")
    for event in events:
        print(
            event["UID"],
            event["DTSTART"],
            event["SUMMARY"],
            event["DTSTART"].dt.timestamp(),
        )
    assert len(events) == 1

```

### `recurring_ical_events/test/test_issue_163_deleted_modification.py`

```py
"""EXDATE does not exclude a modified instance for an event with higher SEQUENCE and the same UID.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/163
"""


def test_exdate_excludes_modification(calendars):
    """The exdate should exclude the modification mentioned."""
    events = calendars.issue_163_deleted_modification.at("20240819")
    assert events == []

```

### `recurring_ical_events/test/test_issue_164_duplicated_event.py`

```py
"""Duplicated instances of the same event are returned in v3.1.0. The bug is not present in v2.1.3.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/164
"""


def test_event_is_only_returned_once(calendars):
    """We should not see the same event twice!"""
    events = calendars.issue_164_duplicated_event.at([2024, 8])
    for event in events:
        start = event["DTSTART"].dt
        duration = event["DTEND"].dt - event["DTSTART"].dt
        print(f"start {start} duration {duration}")
        print(event.to_ical().decode())
    assert len(events) == 2

```

### `recurring_ical_events/test/test_issue_173_only_modification_included.py`

```py
"""Calendars do not only contain events with an RRULE but they can contain recurrences without
any RRULE in them.

I assume this can happen for example when one accepts a calendar invitation of
one instance of an recurring event.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/173
"""


def test_event_can_be_found_in_the_right_time(calendars):
    """The event reported should be present in the calculations."""
    events = calendars.issue_173_only_modifications_error.at("20240108")
    assert len(events) >= 1
    uid = "_6krj2dhl74q34b9j60sj4b9k8h238b9p6gok2ba68gojgchl6cpj0h1o88_R20231009T130000@google.com"
    assert any(event["UID"] == uid for event in events)

```

### `recurring_ical_events/test/test_issue_179_span_in_event.py`

```py
"""We want to check that even if the span falls into a day long event, the event is found.

RFC 5545:

    For cases where a "VEVENT" calendar component
    specifies a "DTSTART" property with a DATE value type but no
    "DTEND" nor "DURATION" property, the event's duration is taken to
    be one day.
"""

import pytest


@pytest.mark.parametrize(
    "dt",
    [
        (1997, 11, 2, 0),
        (1997, 11, 2, 1),
    ],
)
def test_event_occurs(calendars, dt):
    """The event should occur."""
    events = calendars.issue_179_example.at(dt)
    assert len(events) == 1

```

### `recurring_ical_events/test/test_issue_18_cancel_status.py`

```py
"""Test that cancelled events are actually repeated as cancelled."""

import pytest


@pytest.mark.parametrize(
    ("date", "attr", "value"),
    [
        ("20200128", "STATUS", None),
        ("20200129", "STATUS", "CANCELLED"),
        ("20200130", "STATUS", None),
        ("20200128", "TRANSP", "OPAQUE"),
        ("20200129", "TRANSP", "OPAQUE"),
        ("20200130", "TRANSP", "OPAQUE"),
    ],
)
def test_events_are_cancelles(calendars, date, attr, value):
    event = calendars.issue_18_cancel_status.at(date)[0]
    assert event.get(attr) == value

```

### `recurring_ical_events/test/test_issue_186_alarms.py`

```py
"""Test VALARM recurrence.

VALARM is specified in RFC 5545 and RFC 9074.
See also https://github.com/niccokunzmann/python-recurring-ical-events/issues/186
"""

from datetime import datetime, timedelta, timezone

import icalendar
import pytest


@pytest.mark.parametrize(
    ("when", "count"),
    [
        ("20241003", 1),
        ((2024, 10, 3, 13), 1),
        ((2024, 10, 3, 13, 0), 1),
        ((2024, 10, 3, 12), 0),
        ((2024, 10, 3, 14), 0),
    ],
)
def test_can_find_absolute_alarm(alarms, when, count):
    """Find the absolute alarm."""
    a = alarms.alarm_absolute.at(when)
    assert len(a) == count
    if count == 1:
        e: icalendar.Event = a[0]
        assert len(e.alarms.times) == 1
        t = e.alarms.times[0]
        assert t.trigger == datetime(2024, 10, 3, 13, 0, 0, tzinfo=timezone.utc)


def test_edited_alarm_is_moved(alarms):
    """When an absolute alarm is edited, the old one does not occur."""
    assert len(alarms.alarm_absolute_edited.at("20241004")) == 1, "New alarm is found"
    assert len(alarms.alarm_absolute_edited.at("20241003")) == 0, "Old alarm is removed"


@pytest.mark.parametrize(
    ("when", "deltas"),
    [
        ("20241003", {0, 45, 90}),
        ((2024, 10, 3, 13), {0, 45}),
        ((2024, 10, 3, 13, 0), {0}),
        ((2024, 10, 3, 12), set()),
        ((2024, 10, 3, 14), {90}),
    ],
)
def test_can_find_absolute_alarm_with_repeat(alarms, when, deltas):
    """This absolute alarm has 2 repetitions in 45 min later."""
    a = alarms.alarm_absolute_repeat.at(when)
    deltas = {timedelta(minutes=m) for m in deltas}
    e_deltas = set()
    for e in a:
        assert len(e.alarms.times) == 1
        t = e.alarms.times[0]
        e_deltas.add(t.trigger - datetime(2024, 10, 3, 13, 0, 0, tzinfo=timezone.utc))
    assert e_deltas == deltas


@pytest.mark.parametrize("day", [17, 18, 19, 20])
def test_collect_alarms_from_todos_relative_to_start(alarms, day):
    """We also collect alarms from todos."""
    todos = alarms.alarm_removed_and_moved.at((2023, 12, day))
    assert len(todos) == 1
    todo = todos[0]
    assert len(todo.alarms.times) == 1
    alarm = todo.alarms.times[0]
    assert alarm.trigger.replace(tzinfo=None) == datetime(2023, 12, day, 8, 0)


@pytest.mark.parametrize("day", [17, 18, 19, 20])
def test_collect_todos_with_alarms(calendars, day):
    """We also collect alarms from todos."""
    calendars.components = ["VTODO"]
    todos = calendars.alarm_removed_and_moved.at((2023, 12, day))
    assert len(todos) == 1
    todo = todos[0]
    assert todo.start.replace(tzinfo=None) == datetime(2023, 12, day, 9, 0)


def test_collect_alarms_from_todos_relative_to_end(alarms):
    """We also collect alarms from todos."""
    todos = alarms.alarm_removed_and_moved.at((2023, 12, 16, 10))
    assert len(todos) == 1
    todo = todos[0]
    assert todo.start.replace(tzinfo=None) == datetime(2023, 12, 16, 9, 0)
    assert len(todo.alarms.times) == 1
    alarm = todo.alarms.times[0]
    assert alarm.trigger.replace(tzinfo=None) == datetime(2023, 12, 16, 10, 0)


def test_todo_occurs(calendars):
    """The todo should occur so we can find the alarm."""
    calendars.components = ["VTODO"]
    todos = calendars.alarm_removed_and_moved.at((2023, 12, 16, 9))
    for x in todos:
        print(x.to_ical().decode())
        print()
    assert len(todos) == 1
    todo = todos[0]
    assert todo.start.replace(tzinfo=None) == datetime(2023, 12, 16, 9, 0)


def test_collect_alarms_from_todos_absolute(alarms):
    """We also collect alarms from todos."""
    todos = alarms.alarm_removed_and_moved.at((2023, 12, 13, 18, 0))
    assert len(todos) == 1
    todo = todos[0]
    assert len(todo.alarms.times) == 1
    alarm = todo.alarms.times[0]
    assert alarm.trigger.replace(tzinfo=None) == datetime(2023, 12, 13, 18, 0)


def test_series_of_events_with_alarms_but_alarm_removed(alarms):
    """We test that an alarm is removed and does not turn up."""
    assert alarms.alarm_removed_and_moved.at("20241221") == []


def test_alarm_is_moved(alarms):
    """The alarm is moved to 30 min before."""
    a = alarms.alarm_removed_and_moved.at("20241222")
    assert len(a) == 1
    e = a[0]
    assert len(e.alarms.times) == 1
    alarm = e.alarms.times[0]
    assert alarm.trigger.hour == 8
    assert alarm.trigger.minute == 30


def test_event_is_moved(alarms):
    """The event has been moved but the alarm is still 1h before."""
    a = alarms.alarm_removed_and_moved.at("20241219")
    for x in a:
        print(x.to_ical().decode())
        print()
    assert len(a) == 1
    e = a[0]
    assert len(e.alarms.times) == 1
    alarm = e.alarms.times[0]
    assert alarm.trigger.hour == 11
    assert alarm.trigger.minute == 0


def test_series_of_events_with_alarms_but_alarm_removed_relative_to_end():
    pytest.skip("TODO - but probably covered by the calculation relative to start")


def test_series_of_events_with_alarms_but_alarm_edited_relative_to_end():
    pytest.skip("TODO - but probably covered by the calculation relative to start")


def test_series_of_events_with_alarm_relative_to_end(alarms):
    """We check alarms relative to the end and start.

    DTSTART;TZID=Europe/London:20241004T110000
    DTEND;TZID=Europe/London:20241004T114500

    15min before start&end
    15min after start&end

    """
    q = alarms.alarm_around_event_boundaries
    assert len(q.at((2024, 10, 4, 10, 45))) == 1, "15 min before start"
    assert len(q.at((2024, 10, 4, 11, 15))) == 1, "15 min after start"
    assert len(q.at((2024, 10, 4, 11, 30))) == 1, "15 min before end"
    assert len(q.at((2024, 10, 4, 12, 0))) == 1, "15 min after end"


@pytest.mark.parametrize(
    ("dt", "trigger"),
    [
        ("20241126", datetime(2024, 11, 26, 13, 0, 0)),
        ("20241127", datetime(2024, 11, 27, 13, 0, 0)),
        ("20241128", datetime(2024, 11, 28, 13, 0, 0)),
        ("20241129", datetime(2024, 11, 29, 13, 0, 0)),
        # narrow it down
        ((2024, 11, 28, 12), None),
        ((2024, 11, 28, 12, 30), None),
        ((2024, 11, 28, 13), datetime(2024, 11, 28, 13, 0, 0)),
        ((2024, 11, 28, 13, 0), datetime(2024, 11, 28, 13, 0, 0)),
        ((2024, 11, 28, 13, 0, 0), datetime(2024, 11, 28, 13, 0, 0)),
        ((2024, 11, 28, 13, 0, 1), None),
        ((2024, 11, 28, 14), None),
    ],
)
def test_series_of_event_with_alarm_relative_to_start(alarms, dt, trigger):
    """This series of events all are preceded by an alarm.

    The alarm occurs 1h before the event starts.
    In this test, we narrow down our query time to make sure we find it.
    """
    a = alarms.alarm_recurring_and_acknowledged_at_2024_11_27_16_27.at(dt)
    if trigger is None:
        assert len(a) == 0
        return
    assert len(a) == 1, f"{dt} has {len(a)} alarms"
    event = a[0]
    assert len(event.alarms.times) == 1
    only_trigger = event.alarms.times[0].trigger
    assert only_trigger.replace(tzinfo=None) == trigger
    assert icalendar.timezone.tzid_from_dt(only_trigger) == "Europe/London"


def test_alarm_without_trigger_is_ignored_as_invalid(alarms):
    """Alarms can be malformed in many ways. This skips a few possibilities."""
    alarms.skip_bad_series = True
    q = alarms.issue_186_invalid_trigger
    e = list(q.all())
    for a in e:
        assert len(a.alarms.times) == 1
        description = a.alarms.times[0].alarm["DESCRIPTION"]
        assert description in ("correct trigger", "absolute trigger")
    assert len(e) == 2


def test_event_is_not_modified_with_2_alarms(alarms):
    """The base event should not be modified."""
    q = alarms.alarm_1_week_before_event
    assert len(q.at("20241202")) == 1, "We find the alarm"
    assert len(q.at("20241202")) == 1, "We find the alarm again"
    assert len(q.at("20241207")) == 1, "We also find the other alarm"


def test_repeating_event_is_not_modified_with_repeating_alarm(alarms):
    """The base event should not be modified."""
    q = alarms.alarm_absolute_repeat
    assert len(list(q.all())) == 3, "We find the alarms"
    assert len(list(q.all())) == 3, "We find the alarm again"


def test_repeating_event_is_not_modified(alarms):
    """The base event should not be modified."""
    q = alarms.alarm_recurring_and_acknowledged_at_2024_11_27_16_27
    assert len(q.between("20241126", "20241130")) == 4, "We find the alarms"
    assert len(q.between("20241126", "20241130")) == 4, "We find the alarm again"


EXPECTED_TRIGGERS = [
    datetime(2024, 12, 18, 8, 0),
    datetime(2024, 12, 19, 11, 0),
    datetime(2024, 12, 20, 8, 0),
    # datetime(2024, 12, 21, 8, 0),  # event without alarm
    datetime(2024, 12, 22, 8, 30),
    datetime(2024, 12, 23, 8, 0),
]
EXPECTED_STARTS = [
    datetime(2024, 12, 18, 9, 0),
    datetime(2024, 12, 19, 12, 0),
    datetime(2024, 12, 20, 9, 0),
    # datetime(2024, 12, 21, 9, 0),  # event without alarm
    datetime(2024, 12, 22, 9, 0),
    datetime(2024, 12, 23, 9, 0),
]


def test_after_with_alarms(alarms):
    """The after function checks if an event was already returned.

    This is likely to cause problems because it should be there several times.
    """
    found_triggers = []
    i = 0
    it = alarms.alarm_removed_and_moved.after(2024)
    for expected_trigger, event, expected_start in zip(
        EXPECTED_TRIGGERS, it, EXPECTED_STARTS
    ):
        print(
            f"{i} start {event.start} is {('' if event.start.replace(tzinfo=None) == expected_start else 'NOT ')}as expected"
        )
        assert len(event.alarms.times) == 1
        trigger = event.alarms.times[0].trigger.replace(tzinfo=None)
        found_triggers.append(trigger)
        print(
            f"{i} trigger {trigger} is {('' if trigger == expected_trigger else 'NOT ')}as expected"
        )
        i += 1  # noqa: SIM113
        print()
    print("\n".join(map(str, zip(found_triggers, EXPECTED_TRIGGERS))))
    assert found_triggers == EXPECTED_TRIGGERS
    with pytest.raises(StopIteration):
        next(it)


def test_all_alarms_are_present(alarms):
    """Check that we find all alarms."""
    events = alarms.alarm_several_in_one.all()
    triggers = []
    for event in events:
        assert len(event.alarms.times) == 1
        triggers.append(event.alarms.times[0].trigger - event.start)
    assert triggers == [
        timedelta(hours=-1),
        timedelta(minutes=-15),
        timedelta(minutes=15),
        timedelta(hours=1),
        timedelta(hours=2),
        timedelta(hours=3),
    ]


def test_several_alarms_occur_for_a_slightly_different_event(alarms):
    """Edited subevents have all an alarm that occurs at the same time.

    Thus, they all should appear.
    """
    events = list(alarms.alarms_at_the_same_time.all())
    summaries = {event["SUMMARY"] for event in events}
    assert summaries == {
        "event with alarm at the same time 1",
        "event with alarm at the same time 2",
        "event with alarm at the same time 3",
    }


@pytest.mark.parametrize("dt", ["20241220", "20241221", "20241222"])
def test_different_alarms_at_the_same_time_merge_into_one(alarms, dt):
    """If an event has different alarms happening at the same time,

    these alarms are in the event.
    """
    events: list[icalendar.Event] = alarms.alarms_different_in_same_event.at(dt)
    alarm_names = {
        alarm_time.alarm["DESCRIPTION"]
        for event in events
        for alarm_time in event.alarms.times
    }
    assert alarm_names >= {"Alarm 1", "Alarm 2", "Alarm 3"}
    if dt == "20241220":
        assert "Alarm 4" in alarm_names

```

### `recurring_ical_events/test/test_issue_186_icalendar_alarm_interface.py`

```py
"""Check icalendar's alarms interface.

We need to check if icalendar is doinng the right thing.
Also, recurring ical events now needs to consider alarms
in a different way.
"""

from datetime import date, timedelta

import pytest


def test_an_event_has_subcomponents_even_if_it_has_an_alarm(calendars):
    """We want the events to have no alarms by default."""
    events = calendars.alarm_at_start_of_event.at("20241004")
    assert len(events) == 1
    event = events[0]
    assert event.subcomponents != []
    assert len(event.alarms.times) != 0


@pytest.mark.parametrize("dt", [date(2024, 11, 26), date(2024, 11, 29)])
def test_alarm_time_for_event_is_correctly_computed_for_recurring_instance(
    calendars, dt
):
    """When an event is a repeated instance, we want the alarm times to be right."""
    events = calendars.alarm_recurring_and_acknowledged_at_2024_11_27_16_27.at(dt)
    assert len(events) == 1
    event = events[0]
    assert len(event.alarms.times) == 1
    assert event.alarms.times[0].trigger == event.start - timedelta(hours=1)

```

### `recurring_ical_events/test/test_issue_20_exdate_ignored.py`

```py
"""
This tests the issue 20. Exdates seem to be ignored.
https://github.com/niccokunzmann/python-recurring-ical-events/issues/20

Another issue of this calendar is that the UNTIL value ends one second
before the next event.
The event in February should be exluded therefore.
"""

import pytest


@pytest.mark.parametrize(
    "exdate",
    # exdates copied from the source
    [
        "20191015T141500Z",
        "20191022T141500Z",
        "20191105T151500Z",
        "20191119T151500Z",
        "20191126T151500Z",
        "20191203T151500Z",
        "20191217T151500Z",
        "20191224T151500Z",
        "20191231T151500Z",
    ],
)
def test_exdates_do_not_show_up(exdate, calendars):
    """Test that certain exdates do not occur."""
    events = calendars.issue_20_exdate_ignored.at(exdate[:8])
    assert not events, f"{events[0].to_ical().decode()} should not occur at {exdate}."


expected_dates = [
    #    "20191015", # exdates are commented out
    #    "20191022",
    "20191029",
    #    "20191105",
    "20191112",
    #    "20191119",
    #    "20191126",
    #    "20191203",
    "20191210",
    #    "20191217",
    #    "20191224",
    #    "20191231",
    "20200107",
    "20200114",
    "20200121",
    "20200128",
]


@pytest.mark.parametrize("date", expected_dates)
def test_rrule_dates_show_up(date, calendars):
    """Test that the other events are present.

    The exdates are commented out.
    """
    events = calendars.issue_20_exdate_ignored.at(date)
    assert len(events) == 1, "There should be an event at.".format()


def test_there_are_n_events(calendars):
    """Test the total numer of events."""
    events = list(calendars.issue_20_exdate_ignored.all())
    for event, expected_date in zip(events, expected_dates):
        print("start: {} expected: {}".format(event["DTSTART"].dt, expected_date))
    for date in expected_dates[len(events) :]:
        print(f"expected: {date}")
    for event in events[len(expected_dates) :]:
        print("not expected: {}".format(event["DTSTART"].dt))
    assert len(events) == 7


def test_rdate_after_until_also_in_rrule(calendars):
    """Special test for pytz, if the event is included."""
    events = calendars.rdate_falls_on_rrule_until.at("20200204")
    for event in events:
        print(event)
    assert len(events) == 1

```

### `recurring_ical_events/test/test_issue_201_incompatible_dates.py`

```py
"""These are tests to make sure that the mixture of datetime and date works.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/201
"""

from datetime import date, datetime, timedelta

import pytest

from recurring_ical_events.types import Time
from recurring_ical_events.util import has_timezone, is_date, is_datetime


def test_can_calculate_times_of_issue_example(calendars, utc):
    """The example from the issue should work."""
    events = list(calendars.issue_201_mixed_datetime_and_date.all())
    assert len(events) == 1
    event = events[0]
    assert event.start == datetime(2023, 7, 24, 0, 0, tzinfo=utc)
    assert event.end == datetime(2023, 8, 17, 0, 0, tzinfo=utc)


def test_is_date(utc):
    """Identify dates."""
    assert is_date(date(2023, 7, 24))
    assert not is_date(datetime(2023, 7, 24, 0, 0, tzinfo=utc))
    assert not is_date(datetime(2023, 7, 24, 0, 0))


def test_is_datetime(utc):
    """Identify datetimes."""
    assert is_datetime(datetime(2023, 7, 24, 0, 0, tzinfo=utc))
    assert not is_datetime(date(2023, 7, 24))
    assert is_datetime(datetime(2023, 7, 24, 0, 0))


def test_has_timezone(utc):
    """Check if we have a timezone."""
    assert has_timezone(datetime(2023, 7, 24, 0, 0, tzinfo=utc))
    assert not has_timezone(datetime(2023, 7, 24, 0, 0))
    assert not has_timezone(date(2023, 7, 24))


@pytest.mark.parametrize("component", ["VEVENT", "VTODO"])
@pytest.mark.parametrize("start", ["DATE", "DATETIME", "UTC"])
@pytest.mark.parametrize("end", ["DATE", "DATETIME", "UTC", "DAYS", "HOURS"])
def test_all_possiblilities_are_considered(calendars, component, start, end):
    """All possibilities are present in the result."""
    calendars.components = [component]
    uids = {str(c["UID"]) for c in calendars.issue_201_test_matrix.all()}
    assert f"{component}-{start}-{end}" in uids


@pytest.mark.parametrize(
    ("end", "duration"),
    [
        ("DATE", timedelta(days=1)),
        ("DATETIME", timedelta(days=1, hours=4)),
        ("UTC", timedelta(days=2, hours=2)),
        ("DAYS", timedelta(days=3)),
        ("HOURS", timedelta(hours=10)),
    ],
)
def test_duration(calendars, end, duration):
    """Check the duration."""
    calendars.components = ["VEVENT", "VTODO"]
    components = [
        c for c in calendars.issue_201_test_matrix.all() if c["UID"].endswith(end)
    ]
    for component in components:
        uid = str(component["UID"])
        assert component.duration == duration, uid
        assert component.end - component.start == duration, uid


def is_datetime_without_timezone(dt: Time) -> bool:
    """Wether this has no timrzone."""
    return is_datetime(dt) and not has_timezone(dt)


def is_datetime_with_timezone(dt: Time) -> bool:
    """Wether this has no timrzone."""
    return is_datetime(dt) and has_timezone(dt)


def is_days(td: timedelta):
    """Wether this is only days, not hours."""
    return td.days != 0 and td.seconds == 0


def is_hours(td: timedelta):
    """Wether this is only days, not hours."""
    return td.seconds != 0


@pytest.mark.parametrize(
    ("uid", "check"),
    [
        ("DATE", is_date),
        ("DATETIME", is_datetime_without_timezone),
        ("UTC", is_datetime_with_timezone),
    ],
)
def test_start_is_correct(calendars, uid, check):
    """Check the start of the components."""
    components = calendars.raw.issue_201_test_matrix.walk(
        select=lambda c: c.get("UID", "--").split("-")[1] == uid
    )
    for component in components:
        assert check(component.DTSTART), f"{component['UID']}.DTSTART"


@pytest.mark.parametrize(
    ("uid", "check"),
    [
        ("DATE", is_date),
        ("DATETIME", is_datetime_without_timezone),
        ("UTC", is_datetime_with_timezone),
        ("DAYS", is_days),
        ("HOURS", is_hours),
    ],
)
def test_end_is_correct(calendars, uid, check):
    """Check the start of the components."""
    components = calendars.raw.issue_201_test_matrix.walk(
        select=lambda c: c.get("UID", "--").split("-")[2] == uid
    )
    for component in components:
        if uid in ("DAYS", "HOURS"):
            assert check(component.DURATION)
        elif component.name == "VEVENT":
            assert check(component.DTEND), f"{component['UID']}.DTEND"
        else:
            assert component.name == "VTODO"
            assert check(component.DUE), f"{component['UID']}.DUE"

```

### `recurring_ical_events/test/test_issue_211_pagination.py`

```py
"""Test the pagination behaviour of the query."""

from datetime import date, timedelta
from typing import Callable, Iterator

import pytest
from icalendar import Component

from recurring_ical_events.occurrence import OccurrenceID
from recurring_ical_events.pages import Page, Pages
from recurring_ical_events.test.conftest import ICSCalendars
from recurring_ical_events.util import compare_greater


@pytest.fixture(params=[1, 5, 30])
def page_size(request: pytest.FixtureRequest) -> int:
    """Return the number of events per page."""
    return request.param


GET_PAGES = Callable[[], Pages]


def iterate_pages(get_pages: GET_PAGES):
    """Iterate over the pages and return all the events as a list."""
    pages = get_pages()
    for page in pages:
        components = page.components
        assert len(components) == pages.size or (
            not page.has_next_page() and 0 < len(components) <= pages.size
        )
        yield from components


def iterate_next_page(get_pages: GET_PAGES):
    """Iterate with the next page attribute."""
    pages = get_pages()
    while True:
        page = pages.generate_next_page()
        yield from page.components
        if not page:
            break


def continue_iteration_with_page_id(get_pages: Callable[[str], Pages]):
    """Restart the iteration process with a new pages object."""
    pages: Pages = get_pages()
    page = pages.generate_next_page()
    while page:
        yield from page.components
        assert (page.next_page_id == "") == page.is_last()
        if not page.next_page_id:
            break
        pages = get_pages(page.next_page_id)
        page = pages.generate_next_page()


@pytest.fixture(
    params=[iterate_pages, iterate_next_page, continue_iteration_with_page_id]
)
def page_iterator(
    request: pytest.FixtureRequest,
) -> Callable[[Pages], Iterator[Component]]:
    return request.param


check_calendars = pytest.mark.parametrize(
    ("calendar", "start", "stop", "expected_count"),
    [
        ("no_events", date(1970, 12, 11), date(2030, 12, 12), 0),
        ("one_event", date(2000, 12, 11), date(2020, 12, 12), 1),
        ("event_10_times", date(2020, 1, 13), date(2020, 1, 14), 1),
        ("event_10_times", date(2020, 1, 13), date(2023, 12, 14), 10),
        ("event_10_times", date(2020, 1, 13), None, 10),
        ("event_10_times", date(2020, 1, 13), date(1970, 12, 14), 0),
        ("several_events_at_the_same_time", date(2019, 1, 13), None, 10),
    ],
)


@check_calendars
def test_compare_events_with_expected(
    calendars: ICSCalendars,
    calendar: str,
    start: date,
    stop: date,
    page_size: int,
    page_iterator: Callable[[Pages], Iterator[Component]],
    expected_count: int,
):
    """Test the pagination with only one event."""

    def paginate(next_page_id: str = ""):
        return calendars[calendar].paginate(page_size, start, stop, next_page_id)

    count = 0
    for page_component, after_component in zip(
        page_iterator(paginate), calendars[calendar].after(start)
    ):
        assert page_component == after_component
        assert stop is None or compare_greater(stop, page_component.start)
        print(f"page_component: {page_component}")
        count += 1
    assert count == expected_count


def test_empty_page_bool():
    """Check an empty page."""
    assert not Page([])


def test_filled_page_bool():
    """Check the page has content."""
    assert Page([1])


@pytest.mark.parametrize("last_page", [Page([]), Page([1])])
def test_next_page_absent(last_page: Page):
    """Check not having a next page."""
    assert not last_page.has_next_page()
    assert last_page.next_page_id == ""
    assert last_page.is_last()


@pytest.mark.parametrize(
    "page", [Page([1, 2, 3], next_page_id="123"), Page([1], next_page_id="asd")]
)
def test_next_page_present(page: Page):
    """Check having a next page.

    We must at least have a component.
    """
    assert page.next_page_id != ""
    assert page.has_next_page()
    assert not page.is_last()


def test_pages_size_is_the_same_as_parameter(page_size: int):
    """The size parameter is passed."""
    pages = Pages([], page_size)
    assert pages.size == page_size


@pytest.mark.parametrize("invalid_page_size", [-1, 0, -1100])
def test_paginate_invalid_int(invalid_page_size):
    """Raise a ValueError if we have an invalid page size."""
    with pytest.raises(ValueError):
        Pages([], invalid_page_size)


def test_count_events(calendars: ICSCalendars):
    """Check that there is an event."""
    assert calendars.one_event.count() == 1
    assert calendars.no_events.count() == 0


def test_cannot_escape_start_with_pagination_id(calendars: ICSCalendars):
    """The pagination id is passed from outside to this.

    We must make sure that we cannot be hacked.
    """
    start = date(2020, 1, 17)  # the first event is at the 13th
    pages: Pages = calendars.event_10_times.paginate(1, start)
    first_page = pages.generate_next_page()
    assert first_page
    assert not first_page.is_last()
    # request the next page but with an earlier id
    oid = OccurrenceID.from_string(first_page.next_page_id)
    new_oid = OccurrenceID(
        oid.name, oid.uid, oid.recurrence_id, oid.start - timedelta(days=30)
    )
    pages: Pages = calendars.event_10_times.paginate(
        1, start, next_page_id=new_oid.to_string()
    )
    # we cannot be earlier than start though
    next_page = pages.generate_next_page()
    assert next_page.components[0].start == first_page.components[0].start
    assert next_page.components == first_page.components


def invalidate_recurrence_id(next_page_id: str) -> str:
    """We change the recurrence id."""
    oid = OccurrenceID.from_string(next_page_id)
    return OccurrenceID(oid.name, oid.uid, date(1990, 10, 11), oid.start).to_string()


def invalidate_uid(next_page_id: str) -> str:
    """We change the uid."""
    oid = OccurrenceID.from_string(next_page_id)
    return OccurrenceID(
        oid.name, oid.uid + "-changed", oid.recurrence_id, oid.start
    ).to_string()


@pytest.mark.parametrize("invalidate_id", [invalidate_uid, invalidate_recurrence_id])
def test_invalid_recurrence_id_uid_will_not_go_though_all_events_but_stop_after_that_date(
    calendars: ICSCalendars, invalidate_id: Callable[[str], str]
):
    """If we cannot find an event, the page starts on the day it should."""
    start = date(2020, 1, 17)  # the first event is at the 13th
    pages: Pages = calendars.event_10_times.paginate(1, start)
    first_page = pages.generate_next_page()
    real_next_page = pages.generate_next_page()
    # invalidate the event we are looking for
    pages: Pages = calendars.event_10_times.paginate(
        1, start, next_page_id=invalidate_id(first_page.next_page_id)
    )
    # we will still find the correct event because of the start
    # and we only have one event per day
    modified_next_page = pages.generate_next_page()
    assert real_next_page.components[0].start == modified_next_page.components[0].start
    assert real_next_page.components == modified_next_page.components

```

### `recurring_ical_events/test/test_issue_217_expose_occurrences_api.py`

```py
"""Test the occurrence-returning query and pagination API."""

from datetime import date, datetime, timedelta
from typing import Callable, Iterator

import pytest

import recurring_ical_events
from recurring_ical_events.occurrence import (
    AlarmOccurrence,
    Occurrence,
    OccurrenceID,
)
from recurring_ical_events.pages import (
    OccurrencePage,
    OccurrencePages,
    Page,
    Pages,
)
from recurring_ical_events.test.conftest import ICSCalendars


def _to_components(occurrences):
    """Convert occurrences to components the same way the public API does."""
    return [
        occurrence.as_component(keep_recurrence_attributes=False)
        for occurrence in occurrences
    ]


check_calendars = pytest.mark.parametrize(
    "calendar",
    [
        "no_events",
        "one_event",
        "event_10_times",
        "several_events_at_the_same_time",
        "three_events",
    ],
)


@check_calendars
@pytest.mark.parametrize(
    "between_args",
    [
        ((2000, 1, 1), (2030, 1, 1)),
        ((2020, 1, 13), (2020, 1, 14)),
        ((1970, 1, 1), (1971, 1, 1)),
    ],
)
def test_occurrences_between_matches_between(
    calendars: ICSCalendars, calendar: str, between_args: tuple
):
    """``occurrences_between`` produces the same components as ``between``."""
    query = calendars[calendar]
    start, stop = between_args
    assert _to_components(query.occurrences_between(start, stop)) == query.between(
        start, stop
    )


@check_calendars
@pytest.mark.parametrize(
    "at_argument",
    [
        2020,
        (2020,),
        (2020, 1),
        (2020, 1, 13),
        "20200113",
        date(2020, 1, 13),
        datetime(2020, 1, 13, 7, 45),
        (2020, 1, 13, 7),
        (2020, 1, 13, 7, 45),
        (2020, 1, 13, 7, 45, 0),
    ],
)
def test_occurrences_at_matches_at(calendars: ICSCalendars, calendar: str, at_argument):
    """``occurrences_at`` and ``at`` agree for every supported input form."""
    query = calendars[calendar]
    assert _to_components(query.occurrences_at(at_argument)) == query.at(at_argument)


@check_calendars
def test_occurrences_after_matches_after(calendars: ICSCalendars, calendar: str):
    """``occurrences_after`` and ``after`` agree element by element."""
    limit = 20
    query = calendars[calendar]
    after_components = []
    for i, component in enumerate(query.after(date(2000, 1, 1))):
        if i >= limit:
            break
        after_components.append(component)
    occurrence_components = []
    for i, occurrence in enumerate(query.occurrences_after(date(2000, 1, 1))):
        if i >= limit:
            break
        occurrence_components.append(
            occurrence.as_component(keep_recurrence_attributes=False)
        )
    assert occurrence_components == after_components


@check_calendars
def test_occurrences_all_matches_all(calendars: ICSCalendars, calendar: str):
    """``occurrences_all`` and ``all`` agree element by element."""
    limit = 20
    query = calendars[calendar]
    all_components = []
    for i, component in enumerate(query.all()):
        if i >= limit:
            break
        all_components.append(component)
    occurrence_components = []
    for i, occurrence in enumerate(query.occurrences_all()):
        if i >= limit:
            break
        occurrence_components.append(
            occurrence.as_component(keep_recurrence_attributes=False)
        )
    assert occurrence_components == all_components


@check_calendars
def test_occurrences_count_matches_count(calendars: ICSCalendars, calendar: str):
    """``occurrences_count`` and ``count`` agree."""
    query = calendars[calendar]
    assert query.occurrences_count() == query.count()


def test_first_occurrence_matches_first(calendars: ICSCalendars):
    """``first_occurrence`` produces the same component as ``first``."""
    query = calendars.one_event
    assert (
        query.first_occurrence.as_component(keep_recurrence_attributes=False)
        == query.first
    )


def test_first_occurrence_raises_index_error_when_empty(calendars: ICSCalendars):
    """``first`` and ``first_occurrence`` both raise on an empty calendar."""
    query = calendars.no_events
    with pytest.raises(IndexError):
        _ = query.first
    with pytest.raises(IndexError):
        _ = query.first_occurrence


def test_first_occurrence_is_an_occurrence(calendars: ICSCalendars):
    """``first_occurrence`` returns an :class:`Occurrence` instance."""
    assert isinstance(calendars.one_event.first_occurrence, Occurrence)


@pytest.fixture(params=[1, 5, 30])
def page_size(request: pytest.FixtureRequest) -> int:
    return request.param


def _iterate_pages(get_pages: Callable[[], OccurrencePages]) -> Iterator[Occurrence]:
    pages = get_pages()
    for page in pages:
        occurrences = page.occurrences
        assert len(occurrences) == pages.size or (
            not page.has_next_page() and 0 < len(occurrences) <= pages.size
        )
        yield from occurrences


def _iterate_next_page(
    get_pages: Callable[[], OccurrencePages],
) -> Iterator[Occurrence]:
    pages = get_pages()
    while True:
        page = pages.generate_next_page()
        yield from page.occurrences
        if not page:
            break


def _continue_with_page_id(
    get_pages: Callable[[str], OccurrencePages],
) -> Iterator[Occurrence]:
    pages = get_pages()
    page = pages.generate_next_page()
    while page:
        yield from page.occurrences
        assert (page.next_page_id == "") == page.is_last()
        if not page.next_page_id:
            break
        pages = get_pages(page.next_page_id)
        page = pages.generate_next_page()


@pytest.fixture(params=[_iterate_pages, _iterate_next_page, _continue_with_page_id])
def occurrence_page_iterator(request: pytest.FixtureRequest):
    return request.param


@pytest.mark.parametrize(
    ("calendar", "start", "stop", "expected_count"),
    [
        ("no_events", date(1970, 12, 11), date(2030, 12, 12), 0),
        ("one_event", date(2000, 12, 11), date(2020, 12, 12), 1),
        ("event_10_times", date(2020, 1, 13), date(2020, 1, 14), 1),
        ("event_10_times", date(2020, 1, 13), date(2023, 12, 14), 10),
        ("event_10_times", date(2020, 1, 13), None, 10),
        ("event_10_times", date(2020, 1, 13), date(1970, 12, 14), 0),
        ("several_events_at_the_same_time", date(2019, 1, 13), None, 10),
    ],
)
def test_occurrences_paginate_matches_paginate(
    calendars: ICSCalendars,
    calendar: str,
    start: date,
    stop,
    page_size: int,
    occurrence_page_iterator,
    expected_count: int,
):
    """``occurrences_paginate`` produces the same components as ``paginate``."""

    def paginate(next_page_id: str = ""):
        return calendars[calendar].occurrences_paginate(
            page_size, start, stop, next_page_id
        )

    count = 0
    for occurrence, after_component in zip(
        occurrence_page_iterator(paginate), calendars[calendar].after(start)
    ):
        assert (
            occurrence.as_component(keep_recurrence_attributes=False) == after_component
        )
        count += 1
    assert count == expected_count


def test_empty_occurrence_page_bool():
    """An empty page is falsy."""
    assert not OccurrencePage([])


def test_filled_occurrence_page_bool():
    """A non-empty page is truthy."""
    assert OccurrencePage([object()])


@pytest.mark.parametrize("last_page", [OccurrencePage([]), OccurrencePage([object()])])
def test_occurrence_page_next_absent(last_page: OccurrencePage):
    """A page with no ``next_page_id`` reports itself as last."""
    assert not last_page.has_next_page()
    assert last_page.next_page_id == ""
    assert last_page.is_last()


@pytest.mark.parametrize(
    "page",
    [
        OccurrencePage([object(), object()], next_page_id="123"),
        OccurrencePage([object()], next_page_id="abc"),
    ],
)
def test_occurrence_page_next_present(page: OccurrencePage):
    """A page with a ``next_page_id`` reports itself as not last."""
    assert page.next_page_id != ""
    assert page.has_next_page()
    assert not page.is_last()


def test_occurrence_pages_size_is_the_same_as_parameter(page_size: int):
    """``OccurrencePages.size`` reflects the ``size`` constructor argument."""
    assert OccurrencePages(iter([]), page_size).size == page_size


@pytest.mark.parametrize("invalid_page_size", [-1, 0, -1100])
def test_occurrence_paginate_invalid_int(invalid_page_size: int):
    """Invalid sizes raise ``ValueError``."""
    with pytest.raises(ValueError):
        OccurrencePages(iter([]), invalid_page_size)


def test_occurrences_paginate_cannot_escape_start_with_pagination_id(
    calendars: ICSCalendars,
):
    """Tampered ``next_page_id`` start times can't reach behind ``earliest_end``."""
    start = date(2020, 1, 17)
    pages = calendars.event_10_times.occurrences_paginate(1, start)
    first_page = pages.generate_next_page()
    assert first_page
    assert not first_page.is_last()
    oid = OccurrenceID.from_string(first_page.next_page_id)
    rewound = OccurrenceID(
        oid.name, oid.uid, oid.recurrence_id, oid.start - timedelta(days=30)
    )
    pages = calendars.event_10_times.occurrences_paginate(
        1, start, next_page_id=rewound.to_string()
    )
    next_page = pages.generate_next_page()
    assert next_page.occurrences[0].start == first_page.occurrences[0].start


def _invalidate_recurrence_id(next_page_id: str) -> str:
    oid = OccurrenceID.from_string(next_page_id)
    return OccurrenceID(oid.name, oid.uid, date(1990, 10, 11), oid.start).to_string()


def _invalidate_uid(next_page_id: str) -> str:
    oid = OccurrenceID.from_string(next_page_id)
    return OccurrenceID(
        oid.name, oid.uid + "-changed", oid.recurrence_id, oid.start
    ).to_string()


@pytest.mark.parametrize("invalidate_id", [_invalidate_uid, _invalidate_recurrence_id])
def test_occurrences_paginate_invalid_id_falls_back_to_date(
    calendars: ICSCalendars, invalidate_id: Callable[[str], str]
):
    """If the resume id can't be found, pagination resumes at the requested date."""
    start = date(2020, 1, 17)
    pages = calendars.event_10_times.occurrences_paginate(1, start)
    first_page = pages.generate_next_page()
    real_next_page = pages.generate_next_page()
    pages = calendars.event_10_times.occurrences_paginate(
        1, start, next_page_id=invalidate_id(first_page.next_page_id)
    )
    modified_next_page = pages.generate_next_page()
    assert (
        real_next_page.occurrences[0].start == modified_next_page.occurrences[0].start
    )


def test_occurrences_paginate_resume_past_the_end_yields_no_pages(
    calendars: ICSCalendars,
):
    """A resume id past the last occurrence produces no pages."""
    far_future = OccurrenceID("VEVENT", "ghost-uid", None, date(9999, 1, 1)).to_string()
    pages = calendars.event_10_times.occurrences_paginate(1, next_page_id=far_future)
    first_page = pages.generate_next_page()
    assert len(first_page) == 0
    assert first_page.is_last()


def test_occurrence_pages_yield_occurrence_objects(calendars: ICSCalendars):
    """Pages from ``occurrences_paginate`` yield :class:`Occurrence` instances."""
    pages = calendars.event_10_times.occurrences_paginate(2)
    page = pages.generate_next_page()
    assert page
    for occurrence in page:
        assert isinstance(occurrence, Occurrence)


def test_alarm_pages_yield_alarm_occurrence_objects(calendars: ICSCalendars):
    """Alarm queries yield :class:`AlarmOccurrence` instances."""
    calendars.components = ["VALARM"]
    pages = calendars.alarm_15_min_before_event_snoozed.occurrences_paginate(2)
    page = pages.generate_next_page()
    assert page
    for occurrence in page:
        assert isinstance(occurrence, AlarmOccurrence)


def test_top_level_reexports_pagination_classes():
    """The pagination classes re-export from the package root."""
    assert recurring_ical_events.Page is Page
    assert recurring_ical_events.Pages is Pages
    assert recurring_ical_events.OccurrencePage is OccurrencePage
    assert recurring_ical_events.OccurrencePages is OccurrencePages


def test_paginated_occurrence_can_keep_recurrence_attributes(calendars: ICSCalendars):
    """The caller controls ``keep_recurrence_attributes`` at materialization time."""
    pages = calendars.event_10_times.occurrences_paginate(1)
    occurrence = pages.generate_next_page().occurrences[0]
    stripped = occurrence.as_component(keep_recurrence_attributes=False)
    kept = occurrence.as_component(keep_recurrence_attributes=True)
    assert "RRULE" not in stripped
    assert "RRULE" in kept

```

### `recurring_ical_events/test/test_issue_219_recurrence_id_in_events.py`

```py
"""Add the RECURRENCE-ID to all the resuts.

It is problematic to assume that recurrences are identified by their DTSTART.
This adds the recurrence id to the events.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/219
"""

from __future__ import annotations

from datetime import date, datetime, timedelta

import pytest
from icalendar import Calendar, Event
from icalendar.timezone import tzp

import recurring_ical_events

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo  # noqa: F401, RUF100


def create_event_without_recurrence_id(
    start: date,
    rdate: timedelta | None = None,
    is_rdate: bool = False,  # noqa: FBT001
) -> Event:
    """Return"""
    delta = timedelta(days=10)
    event = Event()
    rdate = start + delta
    if is_rdate:
        rdate, start = start, rdate
    event.add("DTSTART", start)
    event.add("UID", "test")
    if rdate:
        event.add("RDATE", rdate)
        print("start", start, "rdate", rdate)
    else:
        print("start", start)
    print("--- calendar ---")
    print(event.to_ical().decode())
    return event


param_start = pytest.mark.parametrize(
    "start",
    [
        date(2019, 5, 15),
        datetime(2019, 5, 15),
        datetime(2019, 5, 15, 12),
        datetime(2021, 5, 15, 12, tzinfo=ZoneInfo("UTC")),
        datetime(2021, 5, 15, 12, tzinfo=ZoneInfo("Europe/Moscow")),
    ],
)


@param_start
@pytest.mark.parametrize(
    ("rdate", "is_rdate"),
    [
        (None, False),
        (timedelta(days=1), False),
        (timedelta(days=-2), True),
    ],
)
def test_recurrence_id_of_first_event(start, rdate, is_rdate):
    """Check the the events returned have the right recurrence id."""
    event = create_event_without_recurrence_id(start, rdate=rdate, is_rdate=is_rdate)
    assert get_recurrence_id_at(event, start) == start


def get_recurrence_id_at(event: Event, start: date) -> datetime:
    """Return the recurrence id of the event at the start."""
    query = recurring_ical_events.of(event)
    events = list(query.between(start - timedelta(days=1), start + timedelta(days=1)))
    assert len(events) == 1
    event = events[0]
    print("looking at", start)
    print("--- result ---")
    print(event.to_ical().decode())
    return event["RECURRENCE-ID"].dt


def test_event_with_recurrence_id_keeps_it_in_series(calendars):
    """The event got moved."""
    events = calendars.recurring_events_moved.at("20190309")
    assert len(events) == 1
    event = events[0]
    # RECURRENCE-ID;TZID=Europe/Berlin:20190309T020000
    rid = tzp.localize(datetime(2019, 3, 9, 2), "Europe/Berlin")
    # DTSTART;TZID=Europe/Berlin:20190309T030000
    start = tzp.localize(datetime(2019, 3, 9, 3), "Europe/Berlin")
    print("start")
    print(start)
    print(event.start)
    print("rid")
    print(rid)
    print(event["RECURRENCE-ID"].dt)
    assert event.start == start
    assert event["RECURRENCE-ID"].dt == rid


def test_event_with_recurrence_id_keeps_it_standalone(calendars):
    """Test an event without rule, just recurrence id."""
    # UID:_6krj2dhl74q34b9j60sj4b9k8h238b9p6gok2ba68gojgchl6cpj0h1o88_R20231009T130000@google.com
    # RECURRENCE-ID;TZID=Europe/Paris:20240108T150000
    # DTSTART;TZID=Europe/Paris:20240108T170000
    uid = "_6krj2dhl74q34b9j60sj4b9k8h238b9p6gok2ba68gojgchl6cpj0h1o88_R20231009T130000@google.com"
    events = calendars.issue_173_only_modifications_error.at("20240108")
    event = next(event for event in events if event["UID"] == uid)
    expected = tzp.localize(datetime(2024, 1, 8, 15), "Europe/Paris")
    recid = event["RECURRENCE-ID"].dt
    print("expected", expected, "\n   start", event.start, "\n     rid", recid)
    assert recid == expected, "RECURRENCE-ID;TZID=Europe/Paris:20240108T150000"


def test_recurrence_id_defaults_to_start(calendars):
    """Test the we always have one so we can edits events."""
    event = calendars.one_event.first
    assert event.start == event["RECURRENCE-ID"].dt


def test_if_we_add_an_event_with_recurrence_id_we_edit_it(calendars):
    """Test the we always have one so we can edits events."""
    event = calendars.one_event.first
    modified = event.copy()
    del event["RECURRENCE-ID"]  # this looks like the base event
    modified["modified"] = True
    calendar = Calendar()
    calendar.add_component(event)
    calendar.add_component(modified)
    events = list(recurring_ical_events.of(calendar).all())
    print(calendar.to_ical().decode())
    assert len(events) == 1
    event = events[0]
    assert event["modified"]


def test_modify_event_with_sequence_number(calendars):
    """Test the we always have one so we can edits events."""
    calendar = calendars.raw.recurring_events_moved
    events = recurring_ical_events.of(calendar).at("20190309")
    assert len(events) == 1
    event = events[0]

    # This event happens on 2019-03-09
    assert event["SUMMARY"] == "New Event"
    assert event["SEQUENCE"]

    # The attributes can be set, just not mutated
    event["SEQUENCE"] = event.get("SEQUENCE", 0) + 1
    event["SUMMARY"] = "Modified Again!"

    # Add the modified event ot the calendar
    calendar.add_component(event)
    print(calendar.to_ical().decode())

    # Get the day again and see the modified event
    events = recurring_ical_events.of(calendar).at("20190309")
    assert len(events) == 1
    event = events[0]

    assert event["SUMMARY"] == "Modified Again!"


def test_alarm_has_no_recurrence_id(alarms):
    """Alarms usually do not have those ids."""
    a = alarms.alarm_absolute.at("20241003")
    assert len(a) == 1
    print(a[0].to_ical().decode())
    alarm = a[0].subcomponents[0]
    assert "RECURRENCE-ID" not in alarm

```

### `recurring_ical_events/test/test_issue_223_sequence_number.py`

```py
"""This tests generating the right sequence number for event editing.

A computed, recurring event of a UID taking an event with a higher sequence in account,
will be of that sequence.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/223
"""

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from icalendar import Event


def test_sequence_number_is_not_set_for_single_events(calendars):
    """If we have singe events, they should not need a sequence number."""
    assert "SEQUENCE" not in calendars.one_event.first


@pytest.mark.parametrize(("date", "sequence"), [("20190305", 1), ("20190304", 0)])
def test_sequence_is_not_deleted(calendars, date, sequence):
    """We do not delete the sequence if it is 0."""
    events: list[Event] = calendars.issue_223_one_event_with_sequence.at(date)
    assert len(events) == 1
    event = events[0]
    assert event["SEQUENCE"] == sequence, "sequence remains in here"


def test_sequence_number_is_not_set_for_recurrence(calendars):
    """If we do not use sequences at all, we should not set them."""
    events = calendars.one_day_event_repeat_every_day.at("20190308")
    assert len(events) == 1
    event = events[0]
    assert "SEQUENCE" not in event, "is not set if not needed"


def test_sequence_number_is_highest_for_edited_event(calendars):
    """If an event was edited, it uses this sequence number."""
    events: list[Event] = calendars.issue_223_thunderbird.at("20250424")
    assert len(events) == 1
    event = events[0]
    assert event["SEQUENCE"] == 3, "2 -> 3"


def test_sequence_number_is_highest_for_base_event(calendars):
    """The base event with no modification has the highest sequence number."""
    events: list[Event] = calendars.issue_223_thunderbird.at("20250423")
    assert len(events) == 1
    event = events[0]
    assert event["SEQUENCE"] == 3, "1 -> 3"


def test_sequence_number_is_highest_for_last_event(calendars):
    """The last edited event keeps its sequence number."""
    events: list[Event] = calendars.issue_223_thunderbird.at("20250425")
    assert len(events) == 1
    event = events[0]
    assert event["SEQUENCE"] == 3, "3 -> 3"

```

### `recurring_ical_events/test/test_issue_243_recurrence_id_is_not_identical_to_dtstart.py`

```py
"""The RECURRENCE-ID should not be identical to DTSTART.

That is confusing.
See https://github.com/niccokunzmann/python-recurring-ical-events/issues/243
"""

from datetime import datetime


def test_recurrence_id_is_not_identical_to_dtstart(calendars):
    """We need to make sure they are distinct to set the values independently."""
    start = datetime(2015, 9, 1)
    end = datetime(2015, 9, 4)
    recurrings = calendars.issue_243_recurrence_id_is_not_identical_to_dtstart.between(
        start, end
    )
    r = recurrings[0]

    ## This break, it should pass
    assert id(r["dtstart"]) != id(r["recurrence-id"])
    assert r["dtstart"] is not r["recurrence-id"]

    ## This is true
    assert r["recurrence-id"].dt == datetime(2015, 9, 1, 8)

    ## The test recurrence at this particlar day should start at 9, not at 8
    r["dtstart"].dt = datetime(2015, 9, 1, 9)

    ## This should not break, but breaks
    assert r["recurrence-id"].dt == datetime(2015, 9, 1, 8)

    r["dtstart"] = datetime(2015, 9, 1, 9)

    ## This should not break, but breaks
    assert r["recurrence-id"].dt == datetime(2015, 9, 1, 8)

```

### `recurring_ical_events/test/test_issue_253_additional_recurrence_id.py`

```py
"""A new sequence should override an older one."""

from datetime import date, datetime, timezone

import pytest

from recurring_ical_events.util import convert_to_date_range


def test_calendar_from_issue(calendars):
    """We have exactly two events in sequence 2.

    start 2024-07-01 duration 7 days, 0:00:00
    start 2024-07-15 duration 7 days, 0:00:00
    """
    events = list(calendars.issue_253_additional_recurrence_id.at((2024, 7)))
    for event in events:
        start = event["DTSTART"].dt
        duration = event["DTEND"].dt - event["DTSTART"].dt
        print(f"start {start} duration {duration}")

    assert len(events) == 2
    assert events[0].start == date(2024, 7, 1)
    assert events[1].start == date(2024, 7, 15)


def test_edge_case_1(calendars):
    """Modified edge case

    Although the old core has a recurrence id, it should not be returned.

    Dates stay the same.
    start 2024-07-01 duration 7 days, 0:00:00
    start 2024-07-15 duration 7 days, 0:00:00
    """
    events = sorted(
        calendars.issue_253_edge_case_1.at((2024, 7)), key=lambda e: e.start
    )
    for event in events:
        start = event["DTSTART"].dt
        duration = event["DTEND"].dt - event["DTSTART"].dt
        print(f"start {start} duration {duration} symmary: {event['SUMMARY']}")

    assert len(events) == 2
    assert events[0].start == date(2024, 7, 1)
    assert events[1].start == date(2024, 7, 29)

    assert events[0]["SUMMARY"] == "event 2"
    assert events[1]["SUMMARY"] == "event 1"


def test_edge_case_2(calendars):
    """Modified edge case

    > The first event should not be ignored if, for example, it had
    > RECURRENCE-ID;VALUE=DATE:20240715 or had not RECURRENCE-ID at all like in #164

    Dates differ
    start 2024-07-01 duration 7 days, 0:00:00
    start 2024-07-29 duration 7 days, 0:00:00
    """
    events = sorted(
        calendars.issue_253_edge_case_1.at((2024, 7)), key=lambda e: e.start
    )
    for event in events:
        start = event["DTSTART"].dt
        duration = event["DTEND"].dt - event["DTSTART"].dt
        print(f"start {start} duration {duration} symmary: {event['SUMMARY']}")

    assert len(events) == 2
    assert events[0].start == date(2024, 7, 1)
    assert events[1].start == date(2024, 7, 29)


@pytest.mark.parametrize(
    ("dt", "start", "stop"),
    [
        (datetime(2024, 1, 2, 3, 4), datetime(2024, 1, 2), datetime(2024, 1, 3)),
        (
            datetime(2025, 12, 31, 3, 4, tzinfo=timezone.utc),
            datetime(2025, 12, 31, tzinfo=timezone.utc),
            datetime(2026, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
        ),
        (
            datetime(1990, 2, 1, 23, 59, 59),
            datetime(1990, 2, 1, 0, 0, 0),
            datetime(1990, 2, 2),
        ),
        (date(1993, 2, 23), date(1993, 2, 23), date(1993, 2, 24)),
    ],
)
def test_convert_to_date_range(dt, start, stop):
    """Test converting the date range."""
    date_range = convert_to_date_range(dt)
    assert date_range == (start, stop)

```

### `recurring_ical_events/test/test_issue_27.py`

```py
"""These tests are for Issue 27
https://github.com/niccokunzmann/python-recurring-ical-events/issues/27
https://github.com/niccokunzmann/python-recurring-ical-events/pull/32

Diff of the two files:

diff test/calendars/issue-27-t1.ics test/calendars/issue-27-t2.ics

    < RRULE:FREQ=DAILY;UNTIL=20200429T000000
    < EXDATE:20200427T120000Z
    ---
    > RRULE:FREQ=DAILY;UNTIL=20200429T000000Z
    > EXDATE:20200427T140000Z

"""

start_date = (2020, 4, 25)
end_date = (2020, 4, 30)


def print_events(events):
    for event in events:
        start = event["DTSTART"].dt
        duration = event["DTEND"].dt - event["DTSTART"].dt
        print(f"start {start} duration {duration}")


def test_until_value_with_UNKNOWN_timezone_works_with_exdate(calendars):
    """The until value has no time zone attached."""
    events = calendars.issue_27_t1.between(start_date, end_date)
    print_events(events)
    assert len(events) == 2, "two events, exdate matches one"


def test_until_value_with_DEFAULT_timezone_works_with_exdate(calendars):
    """The until value uses the default time zone."""
    events = calendars.issue_27_t2.between(start_date, end_date)
    print_events(events)
    assert len(events) == 2, "two events, exdate matches one"

```

### `recurring_ical_events/test/test_issue_28_timezone_with_z.py`

```py
"""These tests are for Issue 28
https://github.com/niccokunzmann/python-recurring-ical-events/issues/28

"""


def test_expected_amount_of_events(calendars):
    events = calendars.issue_28_rrule_with_UTC_endinginZ.between(
        (2020, 5, 25),
        (2020, 9, 5),
    )
    assert len(events) == 15, (
        "Microsoft Outlook online imports this calendar and shows that there are 15 events."
    )


def test_modification_of_event(calendars):
    events = calendars.issue_28_rrule_with_UTC_endinginZ.between(
        (2020, 9, 3),
        (2020, 9, 5),
    )
    assert len(events) == 1, "Microsoft Outlook online shows one event moved."

```

### `recurring_ical_events/test/test_issue_36_recurrence_id_format.py`

```py
"""
These tests are for issue 36
https://github.com/niccokunzmann/python-recurring-ical-events/issues/36
"""


def test_datetime_replaced_by_datetime(calendars):
    events = calendars.issue_36_recurrence_ID_format.at("20200917")
    assert len(events) == 1
    assert events[0].get("SUMMARY") == "Modified event"


def test_date_replaced_by_date(calendars):
    events = calendars.issue_36_recurrence_ID_format.at("20200914")
    assert len(events) == 1
    assert events[0].get("SUMMARY") == "Modified event 1"


def test_date_replaced_by_datetime(calendars):
    events = calendars.issue_36_recurrence_ID_format.at("20200921")
    assert len(events) == 1
    assert events[0].get("SUMMARY") == "Modified event 2"

```

### `recurring_ical_events/test/test_issue_4.py`

```py
"""
These are tests concerning issue 4
https://github.com/niccokunzmann/python-recurring-ical-events/issues/4

It seems the rrule until parameter includes the last date
https://dateutil.readthedocs.io/en/stable/rrule.html
"""

import datetime

start_date = (2019, 6, 13, 12, 00, 00, 00)
end_date = (2019, 6, 14)
a_date = (2019, 6, 13)


def test_print_events(calendars):
    events = calendars.issue_4.between((2019, 6, 1), (2019, 7, 1))
    for event in events:
        print(event["DTSTART"].dt)


def test_between(calendars):
    events = calendars.issue_4.between(start_date, end_date)
    print(events)
    assert len(events) == 1
    assert events[0]["DTSTART"].dt == datetime.date(2019, 6, 13)


def test_at(calendars):
    events = calendars.issue_4.at(a_date)
    print(events)
    assert len(events) == 1
    assert events[0]["DTSTART"].dt == datetime.date(2019, 6, 13)


def test_can_use_different_rrule_until(calendars):
    events = list(calendars.issue_4_rrule_until.all())
    assert len(events) == 12


def test_weidenrinde(calendars):
    events = list(calendars.issue_4_weidenrinde.all())
    assert len(events) == 2

```

### `recurring_ical_events/test/test_issue_44_day_event_reported_twice.py`

```py
"""
It seems that the event is reported on its day and the next.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/44
"""

import pytest


def test_event_is_present_where_it_should_be(calendars):
    events = calendars.issue_44_double_event.at((2020, 8, 14))
    assert len(events) == 1
    event = events[0]
    assert event["SUMMARY"] == "test2"


def test_event_is_absent_on_the_next_day(calendars):
    events = calendars.issue_44_double_event.at((2020, 8, 15))
    assert events == [], "the issue is that an event could turn up here"


def test_event_is_absent_on_the_previous_day(calendars):
    events = calendars.issue_44_double_event.at((2020, 8, 13))
    assert events == [], "the issue is that an event could turn up here"


@pytest.mark.parametrize("offset", list(range(4)))
def test_event_of_recurrence_should_behave_the_same(calendars, offset):
    """we should check that a repeated event does not have the same problem."""
    events = calendars.one_day_event_repeat_every_day.at((2019, 3, 4 + offset))
    assert len(events) == 1, (
        "Events of the the day before and after should not be mentioned."
    )

```

### `recurring_ical_events/test/test_issue_48_daylight.py`

```py
"""These tests are for Issue 48
https://github.com/niccokunzmann/python-recurring-ical-events/issues/48

These were the events occurring when the issue was raised:
    EVENT2:
    start: 2020-11-02 11:30:00+00:00
    stop:  2020-11-02 13:00:00+00:00

March to October: UTC+1
October to March: UTC+0

"""

from datetime import datetime

import pytest
from pytz import timezone

TZ = timezone("Europe/Lisbon")


@pytest.mark.parametrize(
    ("date", "event_name"),
    [
        (datetime(2020, 11, 2, 11, 15, 0, 0), 0),
        (datetime(2020, 11, 2, 11, 31, 0, 0), "EVENT2"),
        (datetime(2020, 11, 2, 12, 0, 0, 0), "EVENT2"),
        (datetime(2020, 11, 2, 12, 1, 0, 0), "EVENT2"),
        (datetime(2020, 11, 2, 12, 59, 0, 0), "EVENT2"),
        (datetime(2020, 11, 2, 13, 1, 0, 0), 0),
    ],
)
def test_event_timing(calendars, date, event_name):
    date = TZ.localize(date)
    events = calendars.issue_48_daylight_aware_repeats.at(date)
    if event_name:
        assert len(events) == 1
        assert events[0]["UID"] == event_name
    else:
        assert not events, "no events expected"

```

### `recurring_ical_events/test/test_issue_48_dst.py`

```py
"""
These are tests concerning issue 4
https://github.com/niccokunzmann/python-recurring-ical-events/issues/4

It seems the rrule until parameter includes the last date
https://dateutil.readthedocs.io/en/stable/rrule.html
"""

import datetime

import pytest
import pytz

chicago = pytz.timezone("America/Chicago")


@pytest.mark.parametrize(
    ("start_time", "end_time", "expected_count"),
    [
        # (
        #     chicago.localize(datetime.datetime(2020, 12, 11, 8)),
        #     chicago.localize(datetime.datetime(2020, 12, 11, 15)),
        #     4,
        # ),
        # (
        #     chicago.localize(datetime.datetime(2020, 12, 11, 9)),
        #     chicago.localize(datetime.datetime(2020, 12, 11, 15)),
        #     3,
        # ),
        (
            chicago.localize(datetime.datetime(2020, 12, 11, 10)),
            chicago.localize(datetime.datetime(2020, 12, 11, 15)),
            3,
        ),
    ],
)
def test_between(calendars, start_time, end_time, expected_count):
    events = calendars.issue_48_dst.between(start_time, end_time)
    assert len(events) == expected_count, (
        f"{expected_count} events expected between {start_time} and {end_time}"
    )

```

### `recurring_ical_events/test/test_issue_6_copy_subcomponents.py`

```py
"""
This tests that subcomponents are carried over to different events.
"""


def test_subcomponents_are_compied(calendars):
    event = next(calendars.subcomponents.all())
    assert event.subcomponents


def test_there_are_no_subcomponents(calendars):
    event = next(calendars.Germany.all())
    assert not event.subcomponents

```

### `recurring_ical_events/test/test_issue_61.py`

```py
"""This file tests the issue 61.

See https://github.com/niccokunzmann/python-recurring-ical-events/issues/61

We expect DATE as the value.

    DTSTART;VALUE=DATE:20211215
    DTEND;VALUE=DATE:20211216

"""

import datetime

from pytz import timezone


def test_sequence_is_not_present(calendars):
    tz = str(calendars.raw.issue_61_time_zone_error.get("X-WR-TIMEZONE"))
    now = timezone(tz).localize(
        datetime.datetime(2021, 12, 15, 17, 41, 1, 446354)
    )  # datetime.datetime.now(timezone(tz)) # use fixed time
    events = calendars.issue_61_time_zone_error.at(now)
    assert len(events) == 1
    assert isinstance(events[0]["DTSTART"].dt, datetime.date)

```

### `recurring_ical_events/test/test_issue_62_moved_event.py`

```py
"""
This tests the move of a december event.

Issue: https://github.com/niccokunzmann/python-recurring-ical-events/issues/62
"""

import pytest


def test_event_is_absent(calendars):
    """RRULE:FREQ=MONTHLY;BYDAY=-1FR"""
    events = calendars.issue_62_moved_event.at("20211231")
    assert events == []


def test_event_has_moved(calendars):
    """DTSTART;TZID=Europe/Berlin:20211217T213000"""
    events = calendars.issue_62_moved_event.at("20211217")
    assert len(events) == 1


def test_there_is_only_one_event_in_december(calendars):
    """Maybe, if we get the whole December, there might be one event."""
    events = calendars.issue_62_moved_event.at((2021, 12))
    assert len(events) == 1


@pytest.mark.parametrize(
    ("date", "summary"),
    [
        ("20230810", "All Day"),
        ("20230816", "All Day"),
        ("20230824", "All Day"),
        ("20230808", "Datetime"),
        ("20230814", "Datetime"),
        ("20230822", "Datetime"),
    ],
)
def test_event_is_present(calendars, date, summary):
    """Test that the middle event has moved"""
    events = calendars.issue_62_moved_event_2.at(date)
    assert len(events) == 1
    event = events[0]
    assert event["SUMMARY"] == summary


@pytest.mark.parametrize("date", ["20230815", "20230817"])
def test_event_is_absent_2(calendars, date):
    """We make sure that the moved event is not there."""
    events = calendars.issue_62_moved_event_2.at(date)
    assert len(events) == 0


def test_total_amount_of_events(calendars):
    """There are only 6 events!"""
    events = calendars.issue_62_moved_event_2.at((2023, 8))
    assert len(events) == 6

```

### `recurring_ical_events/test/test_issue_7_datetime_and_date_start_stop.py`

```py
"""
This file contains the test cases which test that the
event uses the right class: date or datetime.
See https://github.com/niccokunzmann/python-recurring-ical-events/issues/7
"""

import datetime

import pytest
from icalendar import Event


def test_can_serialize(calendars):
    """Test that the event can be serialized."""
    event = next(calendars.one_day_event.all())
    string = event.to_ical()
    assert isinstance(string, bytes)


@pytest.mark.parametrize(
    ("attribute", "dt_type", "event_name"),
    [
        ("dtstart", datetime.date, "one_day_event"),
        ("dtend", datetime.date, "one_day_event"),
        ("dtstart", datetime.datetime, "one_event"),
        ("dtend", datetime.datetime, "one_event"),
    ],
)
def test_is_date(calendars, attribute, dt_type, event_name):
    """Check the type of the attributes"""
    event = next(calendars[event_name].all())
    event = Event.from_ical(event.to_ical())
    dt = event[attribute]
    assert isinstance(dt.dt, dt_type), "content of ical should match"

```

### `recurring_ical_events/test/test_issue_75_range_parameter.py`

```py
"""This tests the range parameter for ics file.
see https://github.com/niccokunzmann/python-recurring-ical-events/issues/75
Description:  This parameter can be specified on a property that
    specifies a recurrence identifier.  The parameter specifies the
    effective range of recurrence instances that is specified by the
    property.  The effective range is from the recurrence identifier
    specified by the property.  If this parameter is not specified on
    an allowed property, then the default range is the single instance
    specified by the recurrence identifier value of the property.  The
    parameter value can only be "THISANDFUTURE" to indicate a range
    defined by the recurrence identifier and all subsequent instances.
    The value "THISANDPRIOR" is deprecated by this revision of
    iCalendar and MUST NOT be generated by applications.

    - https://www.rfc-editor.org/rfc/rfc5545.html#section-3.2.13
"""

from datetime import time
from datetime import timedelta as td
from typing import TYPE_CHECKING

import pytest

from recurring_ical_events.adapters.event import EventAdapter

if TYPE_CHECKING:
    from calendar import Calendar


@pytest.mark.parametrize(
    ("date", "summary"),
    [
        ("20240901", "ORIGINAL EVENT"),
        ("20240911", "ORIGINAL EVENT"),
        ("20240913", "MODIFIED EVENT"),
        ("20240914", "MODIFIED EVENT"),  # RDATE
        ("20240915", "MODIFIED EVENT"),  # Normal recurrence-id
        ("20240917", "MODIFIED EVENT"),
        ("20240919", "MODIFIED EVENT"),
        ("20240922", "EDITED EVENT"),
        ("20240924", "EDITED EVENT"),
        ("20240926", "EDITED EVENT"),
    ],
)
def test_issue_75_RANGE_AT_parameter(calendars, date, summary):
    events = calendars.issue_75_range_parameter.at(date)
    assert len(events) == 1, f"Expecting one event at {date}"
    event = events[0]
    assert str(event["SUMMARY"]) == summary


@pytest.mark.parametrize(
    ("start", "end", "summary", "total"),
    [
        ("20240901T000000Z", "20240911T235959Z", "ORIGINAL EVENT", 6),
        ("20240901T000000Z", "20240913T000000Z", "ORIGINAL EVENT", 6),
        ("20240901T000000Z", "20240913T235959Z", "MODIFIED EVENT", 7),
        ("20240901T000000Z", "20240914T235959Z", "MODIFIED EVENT", 8),  # RDATE
        (
            "20240901T000000Z",
            "20240915T235959Z",
            "MODIFIED EVENT",
            9,
        ),  # Normal recurrence-id
        ("20240901T000000Z", "20240917T235959Z", "MODIFIED EVENT", 10),
        ("20240901T000000Z", "20240919T235959Z", "MODIFIED EVENT", 11),
        ("20240901T000000Z", "20240921T235959Z", "MODIFIED EVENT", 11),
        ("20240901T000000Z", "20240922T000000Z", "MODIFIED EVENT", 11),
        ("20240901T000000Z", "20240922T235959Z", "EDITED EVENT", 12),
        ("20240901T000000Z", "20240923T000000Z", "EDITED EVENT", 12),
        ("20240901T000000Z", "20240923T235959Z", "EDITED EVENT", 12),
        ("20240901T000000Z", "20240924T235959Z", "EDITED EVENT", 13),
        ("20240901T000000Z", "20240925T235959Z", "EDITED EVENT", 13),
        (
            "20240913T000000Z",
            "20240922T000000Z",
            "MODIFIED EVENT",
            5,
        ),  # out of query bounds
        (
            "20240913T000000Z",
            "20240922T235959Z",
            "EDITED EVENT",
            6,
        ),  # out of query bounds
        (
            "20240924T000000Z",
            "20240925T235959Z",
            "EDITED EVENT",
            1,
        ),  # out of query bounds
    ],
)
def test_issue_75_RANGE_BETWEEN_parameter(calendars, start, end, summary, total):
    events = calendars.issue_75_range_parameter.between(start, end)
    assert len(events) == total, (
        f"Expecting {total} events at range {start}, {end}, get {len(events)}"
    )
    event = events[-1]
    assert str(event["SUMMARY"]) == summary


@pytest.mark.parametrize(
    ("date", "start", "end"),
    [
        # moved by 3 hours forward
        ((2024, 9, 13, 9), (9, 0), (16, 0)),  # The modification itself
        ((2024, 9, 17, 9), (9, 0), (16, 0)),  # The recurrence after this moved
        # moved by 2h22m backward
        ((2024, 9, 22, 14, 22), (14, 22), (16, 13)),  # The modification itself
        ((2024, 9, 24, 14, 22), (14, 22), (16, 13)),  # The recurrence after this moved
    ],
)
def test_the_length_of_modified_events(calendars, date, start, end):
    """There should be one event exactly starting and ending at these times."""
    events = calendars.issue_75_range_parameter.at(date)
    assert len(events) != 0, "The calculation could not find an event!"
    assert len(events) == 1, "Modify the test to yield one event only!"
    event = events[0]
    assert event["DTSTART"].dt.time() == time(*start)
    assert event["DTEND"].dt.time() == time(*end)


@pytest.mark.parametrize(
    ("calendar", "event_index", "expected_start_delta", "expected_end_delta"),
    [
        # no recurrence id means 0
        ("issue_62_moved_event", 1, td(0), td(0)),
        # we moved 31 -> 17; 31-17
        ("issue_62_moved_event", 0, td(0), td(14)),
        # we have a duration added on top
        ("one_event", 0, td(minutes=30), td(0)),
        # we move to a later date, +1 day
        ("same_event_recurring_at_same_time", 1, td(days=1, hours=1), td(0)),
        # we move to the front, so we should still add the duration
        ("same_event_recurring_at_same_time", 2, td(0), td(hours=1)),
        # we moved with the THISANDFUTURE
        (
            "issue_75_range_parameter",
            3,
            td(days=1, hours=2, minutes=22) + td(hours=1, minutes=51),
            td(0),
        ),
    ],
)
def test_span_extension(
    calendars, calendar, event_index, expected_start_delta, expected_end_delta
):
    """If we have an event that is moved with THISANDFUTURE,
    other events move, too.

    This requires us to extend the range which we query:
    - If an event moves forward, we need to extend the span to the back ...
    - If an event moves backward, we need to extend the span to the front ...
    ... in order to capture the recurrences from the rrule that would yield
    the occurrence.

    If the length is extended, we can shorten the span
    If the length is reduced, we have to extend the span

    This tests the adapter to yield the correct values for the given types
    of moves.

    We only have to extend the range for THISANDFUTURE events because
    we iterate over all modifications either way.
    TODO: However, for optimization, one could approach to create ranges that
    specify how to extend and contract the spans.

    This test has to test of types of recurrence id, start and end.
    - date
    - datetime without tzinfo
    - datetime with UTC
    - datetime with tzinfo other than UTC

    >.The default value type is DATE-TIME.  The value type can
      be set to a DATE value type.  This property MUST have the same
      value type as the "DTSTART" property contained within the
      recurring component.  Furthermore, this property MUST be specified
      as a date with local time if and only if the "DTSTART" property
      contained within the recurring component is specified as a date
      with local time.
      - https://www.rfc-editor.org/rfc/rfc5545.html#section-3.8.4.4

    moves must include:
    - time forward
    - time backward
    - several days forward
    - several days backward

    Assumptions
    -----------

    This test is for a rought estimate. We can extend the range by +1 day into each direction.
    This will allow us to capture everything.
    Future examples and tests may help us improve the situation by narrowing it further down.

    Safe:
    - move 1 h forward -> END: add 1 day for timezone + 1 day for timedelta without timezone involvement (round up)
    """
    cal = calendars.raw[calendar]
    event = list(cal.walk("VEVENT"))[event_index]
    adapter = EventAdapter(event)
    assert adapter.duration >= td(0)
    start_delta, end_delta = adapter.extend_query_span_by
    assert start_delta >= expected_start_delta
    assert end_delta >= expected_end_delta


def test_can_calculate_query_span_extension_on_all_events(calendars, calendar_name):
    """Check that the calclulation succeeds."""
    for i, event in enumerate(calendars.raw[calendar_name].walk("VEVENT")):
        adapter = EventAdapter(event)
        start_delta, end_delta = adapter.extend_query_span_by
        message = f"{calendar_name}.VEVENT[{i}]"
        assert isinstance(start_delta, td), message
        assert isinstance(end_delta, td), message
        assert start_delta >= td(0), message
        assert end_delta >= td(0), message


def test_deletion_of_THISANDFUTURE_by_SEQUENCE():
    """We need to make sure that the components we have only work on what is actual."""
    pytest.skip("TODO")


def test_RDATE_with_PERIOD():
    """When an RDATE has a PERIOD, we can assume that that defines the new length."""
    pytest.skip("TODO")


@pytest.mark.parametrize(
    ("calendar_name", "event_index", "delta"),
    [
        ("one_event", 0, td(0)),
        ("same_event_recurring_at_same_time", 0, td(0)),
        ("issue_75_range_parameter", 1, td(hours=-3)),
        ("issue_75_range_parameter", 3, td(days=1, hours=2, minutes=22)),
    ],
)
def test_move_by_time(calendars, calendar_name, event_index, delta):
    """Check the moving of events."""
    cal: Calendar = calendars.raw[calendar_name]
    event = list(cal.walk("VEVENT"))[event_index]
    adapter = EventAdapter(event)
    assert adapter.move_recurrences_by == delta


# TODO: Test event with DTSTART = DATE - does it occur properly as it is
#       one day long, I believe. Loot at the RFC 5545.

```

### `recurring_ical_events/test/test_issue_86_x_wr_timezone_but_no_tzid_in_dt.py`

```py
"""
This tests the fix present in x-wr-timezone v0.0.4.
See https://github.com/niccokunzmann/python-recurring-ical-events/issues/86

"""


def test_event_can_be_retrieved(calendars):
    event = next(calendars.issue_86_x_wr_timezone_without_time_zone_in_dt.all())
    assert event["DTSTART"].dt.tzinfo is not None, "should be replaced"
    assert event["DTSTART"].dt.tzname() == "CEST"
    assert event["DTSTART"].dt.year == 2021
    assert event["DTSTART"].dt.month == 9
    assert event["DTSTART"].dt.day == 16
    assert event["DTSTART"].dt.hour == 21
    assert event["DTSTART"].dt.minute == 0

```

### `recurring_ical_events/test/test_issue_97_simple_recurrent_todos_and_journals.py`

```py
import pytest

calendars_parametrized = pytest.mark.parametrize(
    "ical_file",
    [
        "issue_97_simple_todo",
        "issue_97_simple_journal",
        "issue_97_todo_nodtstart",
    ],
)


@calendars_parametrized
def test_recurring_task_is_not_included1(calendars, ical_file):
    """The three files given starts in late 1991, no recurrences
    should be found before 1991.  Refers to
    https://github.com/niccokunzmann/python-recurring-ical-events/issues/97.
    Test passes prior to fixing #97, should still pass after #97 is
    fixed.
    """
    calendars.components = ["VJOURNAL", "VTODO", "VEVENT"]
    tasks = calendars[ical_file].between((1989, 1, 1), (1991, 1, 1))
    assert not tasks


@calendars_parametrized
def test_recurring_task_is_not_included2(calendars, ical_file):
    """Every recurrence of the three ical files is in October, hence
    no recurrences should be found.  Refers to
    https://github.com/niccokunzmann/python-recurring-ical-events/issues/97.
    Test passes prior to fixing #97, should still pass after #97 is
    fixed.
    """
    calendars.components = ["VJOURNAL", "VTODO", "VEVENT"]
    tasks = calendars[ical_file].between((1998, 1, 1), (1998, 4, 14))
    assert not tasks


@calendars_parametrized
def test_recurring_task_is_repeated(calendars, ical_file):
    """Expansion of a yearly task over seven years.
    The issue
    https://github.com/niccokunzmann/python-recurring-ical-events/issues/97
    needs to be fixed before this test can pass
    """
    calendars.components = ["VJOURNAL", "VTODO", "VEVENT"]
    events = calendars[ical_file].between((1995, 1, 1), (2002, 1, 1))
    assert len(events) == 7

```

### `recurring_ical_events/test/test_keep_recurrence_attributes.py`

```py
"""Test that some attributes of the calendar objects
are kept if required.

See Issue 23 https://github.com/niccokunzmann/python-recurring-ical-events/issues/23.
"""

import pytest

from recurring_ical_events import of

RRULE = b"FREQ=DAILY;UNTIL=20160320T030000Z"
RDATE = b"20150705T190000Z"
EXDATE = b"20150705T190000Z"


class Default:
    @staticmethod
    def to_ical():
        return None


@pytest.mark.parametrize(
    ("keywords", "rrule", "rdate", "exdate"),
    [
        ({}, None, None, None),
        ({"keep_recurrence_attributes": False}, None, None, None),
        ({"keep_recurrence_attributes": True}, RRULE, RDATE, EXDATE),
    ],
)
def test_keep_recurrence_attributes_default(calendars, keywords, rrule, rdate, exdate):
    calendar = calendars.raw.rdate2
    rcalendar = of(calendar, **keywords)
    events = rcalendar.at(2014)
    assert events
    for event in events:
        assert event.get("RRULE", Default).to_ical() == rrule
        assert event.get("RDATE", Default).to_ical() == rdate
        assert event.get("EXDATE", Default).to_ical() == exdate

```

### `recurring_ical_events/test/test_multiple_rrule.py`

```py
from datetime import date


def test_multiple_rrule(calendars):
    events = calendars.multiple_rrule.at(2023)
    assert len(events) == 20 + 2
    event_dstarts = [event["DTSTART"].dt.date() for event in events]
    assert date(2023, 2, 9) in event_dstarts
    assert date(2023, 2, 13) in event_dstarts
    assert date(2023, 2, 16) in event_dstarts
    assert date(2023, 3, 13) in event_dstarts

```

### `recurring_ical_events/test/test_occurrence.py`

```py
"""The all() function can be exposed now that we have the after() function.

all() becomes a Generator.
We do not wish to retain a high memory footprint on the occurrences.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING, NamedTuple

import pytest

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo

from recurring_ical_events.occurrence import Occurrence, OccurrenceID

if TYPE_CHECKING:
    from recurring_ical_events.types import RecurrenceIDs, Time


class Adapter(NamedTuple):
    uid: str
    name: str
    recurrence_ids: RecurrenceIDs
    start: Time
    end: Time = date(2020, 10, 10)

    def component_name(self):
        return self.name


def occurrence_id(adapter: Adapter):
    """Check the id of the occurrence."""
    return Occurrence(adapter).id


def occurrence_id_string(adapter: Adapter):
    """Check the string of the occurrence id."""
    return Occurrence(adapter).id.to_string()


def occurrence_id_string_parsed(adapter: Adapter):
    """Check the string of the occurrence id."""
    return OccurrenceID.from_string(Occurrence(adapter).id.to_string())


@pytest.mark.parametrize(
    ("adapter1", "adapter2", "equality", "message"),
    [
        (
            Adapter("asd", "asd", (date(2020, 10, 2),), date(2020, 10, 2)),
            Adapter("asd", "asd", (date(2020, 10, 2),), date(2020, 10, 2)),
            True,
            "same copy",
        ),
        (
            Adapter("asd1", "asd", (date(2020, 10, 2),), date(2020, 10, 2)),
            Adapter("asd", "asd", (date(2020, 10, 2),), date(2020, 10, 2)),
            False,
            "different name",
        ),
        (
            Adapter("asd", "asd", (date(2020, 10, 2),), date(2020, 10, 2)),
            Adapter("asd", "asd1", (date(2020, 10, 2),), date(2020, 10, 2)),
            False,
            "different uid",
        ),
        (
            Adapter("asd", "asd", (date(2020, 10, 1),), date(2020, 10, 2)),
            Adapter("asd", "asd", (date(2020, 10, 2),), date(2020, 10, 2)),
            False,
            "different recurrence id",
        ),
        ## I cannot think of a possible example where the recurrence id is the same but the
        ## start differs - especially after the occurrences are calculated.
        # (
        #     Adapter("asd", "asd", (date(2020, 10, 2),), date(2020, 10, 1)),
        #     Adapter("asd", "asd", (date(2020, 10, 2),), date(2020, 10, 2)),
        #     True,
        #     "different start but recurrence id is the same",
        # ),
        (
            Adapter("asd", "asd", (), date(2020, 10, 2)),
            Adapter("asd", "asd", (), date(2020, 10, 2)),
            True,
            "no recurrence id but copy",
        ),
        (
            Adapter("asd", "asd", (), date(2020, 10, 2)),
            Adapter("asd", "asd", (), date(2020, 10, 1)),
            False,
            "no recurrence id but start differs",
        ),
        (
            Adapter("VEVENT", "uid", (), datetime(2020, 10, 2, 10)),
            Adapter("VEVENT", "uid", (), datetime(2020, 10, 2, 10)),
            True,
            "datetime",
        ),
        (
            Adapter(
                "VEVENT", "uid", (), datetime(2020, 10, 2, 10, tzinfo=ZoneInfo("UTC"))
            ),
            Adapter(
                "VEVENT", "uid", (), datetime(2020, 10, 2, 10, tzinfo=ZoneInfo("UTC"))
            ),
            True,
            "UTC date",
        ),
        (
            Adapter(
                "VEVENT",
                "uid",
                (),
                datetime(2020, 10, 2, 10, tzinfo=ZoneInfo("Europe/Berlin")),
            ),
            Adapter(
                "VEVENT",
                "uid",
                (),
                datetime(2020, 10, 2, 10, tzinfo=ZoneInfo("Europe/Berlin")),
            ),
            True,
            "Europe/Berlin date",
        ),
        (
            Adapter(
                "VEVENT", "uid", (), datetime(2020, 10, 2, 10, tzinfo=ZoneInfo("UTC"))
            ),
            Adapter("VEVENT", "uid", (), datetime(2020, 10, 2, 10)),
            False,
            "timezone differs - UTC",
        ),
        (
            Adapter(
                "VEVENT",
                "uid",
                (),
                datetime(2020, 10, 2, 10, tzinfo=ZoneInfo("Europe/Berlin")),
            ),
            Adapter("VEVENT", "uid", (), datetime(2020, 10, 2, 10)),
            False,
            "timezone differs - Europe/Berlin",
        ),
        (
            Adapter(
                "VEVENT",
                "uid",
                (),
                datetime(2020, 10, 2, 10, tzinfo=ZoneInfo("Europe/Berlin")),
            ),
            Adapter(
                "VEVENT", "uid", (), datetime(2020, 10, 2, 10, tzinfo=ZoneInfo("UTC"))
            ),
            False,
            "timezone differs - Europe/Berlin + UTC",
        ),
    ],
)
@pytest.mark.parametrize(
    "create_occurrence",
    [Occurrence, occurrence_id, occurrence_id_string, occurrence_id_string_parsed],
)
def test_equality(adapter1, adapter2, equality, message, create_occurrence):
    """Check the equality of Occurrences."""
    occurrence1 = create_occurrence(adapter1)
    occurrence2 = create_occurrence(adapter2)
    assert (occurrence1 == occurrence2) == equality, "1 == 2 - " + message
    assert (occurrence1 != occurrence2) != equality, "1 != 2 - " + message
    assert (occurrence2 == occurrence1) == equality, "2 == 1 - " + message
    assert (occurrence2 != occurrence1) != equality, "2 != 1 - " + message
    assert (hash(occurrence1) == hash(occurrence2)) == equality, (
        "hash1 == hash2 - " + message
    )
    assert (hash(occurrence1) != hash(occurrence2)) != equality, (
        "hash1 != hash2 - " + message
    )


ALL_CHARS = "".join(map(chr, range(256)))


@pytest.mark.parametrize(
    ("original_component_id", "message"),
    [
        (
            OccurrenceID("VEVENT", "awdd", date(1970, 2, 12), date(1971, 2, 12)),
            "date and all values given",
        ),
        (
            OccurrenceID(
                "VTODO", "+-2123_", datetime(1970, 2, 12), datetime(1971, 2, 12)
            ),
            "datetime and all values given",
        ),
        (
            OccurrenceID("VTODO", "+-2123_", None, datetime(1971, 2, 12, 10, 21)),
            "datetime no recurrence id",
        ),
        (
            OccurrenceID("asd", "+-2123_", None, date(1971, 2, 12)),
            "date no recurrence id",
        ),
        (
            OccurrenceID("VALARM", ALL_CHARS, None, date(1971, 2, 12)),
            "no recurrence id and a wild UID",
        ),
        (
            OccurrenceID(
                "asd",
                ALL_CHARS,
                datetime(2025, 2, 11, 14, 14),
                datetime(1971, 2, 12, 10, 23),
            ),
            "recurrence id and a wild UID",
        ),
        (
            OccurrenceID(
                "VEVENT",
                "",
                None,
                datetime(1971, 2, 12, 10, 23, tzinfo=ZoneInfo("UTC")),
            ),
            "start in UTC",
        ),
        (
            OccurrenceID(
                "VEVENT",
                "",
                None,
                datetime(1971, 2, 12, 10, 23, tzinfo=ZoneInfo("Europe/Berlin")),
            ),
            "start in Europe/Berlin",
        ),
    ],
)
def test_equality_after_parsed(original_component_id: OccurrenceID, message: str):
    """Check the equality after parsing."""
    parsed_component_id = OccurrenceID.from_string(original_component_id.to_string())
    assert original_component_id == parsed_component_id, (
        "The parsed component id should be equal to its source. " + message
    )
    assert original_component_id.to_string() == parsed_component_id.to_string(), (
        "The string representation cannot change. " + message
    )

```

### `recurring_ical_events/test/test_properties.py`

```py
"""Test the properties of events."""

import pytest


def test_event_has_summary(calendars):
    event = next(calendars.one_event.all())
    assert event["SUMMARY"] == "test1"


@pytest.mark.parametrize("attribute", ["DTSTART", "DTEND"])
def test_recurrent_events_change_start_and_end(calendars, attribute):
    events = calendars.three_events_one_edited.all()
    values = set(event[attribute] for event in events)
    assert len(values) == 3


@pytest.mark.parametrize("index", [1, 2])
def test_duration_stays_the_same(calendars, index):
    events = list(calendars.three_events_one_edited.all())
    duration1 = events[0]["DTEND"].dt - events[0]["DTSTART"].dt
    duration2 = events[index]["DTEND"].dt - events[index]["DTSTART"].dt
    assert duration1 == duration2


def test_attributes_are_created(calendars):
    """Some properties should be part of every event

    This is, even if they are not given in the event at the beginning."""
    events = calendars.discourse_no_dtend.at((2019, 1, 17))
    assert len(events) == 1
    event = events[0]
    assert "DTEND" in event

```

### `recurring_ical_events/test/test_rdate.py`

```py
"""From https://tools.ietf.org/html/rfc5545#section-3.8.5.2

Property Name:  RDATE

   Purpose:  This property defines the list of DATE-TIME values for
      recurring events, to-dos, journal entries, or time zone
      definitions.

   Value Type:  The default value type for this property is DATE-TIME.
      The value type can be set to DATE or PERIOD.

   Property Parameters:  IANA, non-standard, value data type, and time
      zone identifier property parameters can be specified on this
      property.

   Conformance:  This property can be specified in recurring "VEVENT",
      "VTODO", and "VJOURNAL" calendar components as well as in the
      "STANDARD" and "DAYLIGHT" sub-components of the "VTIMEZONE"
      calendar component.

   Description:  This property can appear along with the "RRULE"
      property to define an aggregate set of repeating occurrences.
      When they both appear in a recurring component, the recurrence
      instances are defined by the union of occurrences defined by both
      the "RDATE" and "RRULE".

      The recurrence dates, if specified, are used in computing the
      recurrence set.  The recurrence set is the complete set of
      recurrence instances for a calendar component.  The recurrence set
      is generated by considering the initial "DTSTART" property along
      with the "RRULE", "RDATE", and "EXDATE" properties contained
      within the recurring component.  The "DTSTART" property defines
      the first instance in the recurrence set.  The "DTSTART" property
      value SHOULD match the pattern of the recurrence rule, if
      specified.  The recurrence set generated with a "DTSTART" property
      value that doesn't match the pattern of the rule is undefined.
      The final recurrence set is generated by gathering all of the
      start DATE-TIME values generated by any of the specified "RRULE"
      and "RDATE" properties, and then excluding any start DATE-TIME
      values specified by "EXDATE" properties.  This implies that start
      DATE-TIME values specified by "EXDATE" properties take precedence
      over those specified by inclusion properties (i.e., "RDATE" and
      "RRULE").  Where duplicate instances are generated by the "RRULE"
      and "RDATE" properties, only one recurrence is considered.
      Duplicate instances are ignored.
"""

import pytest


@pytest.mark.parametrize(
    "day",
    [
        "20130803",
        "20130831",
        "20131005",
        "20131102",
        "20131130",
        "20140104",
        "20140201",
        "20140301",
        "20140405",
        "20140503",
        "20140531",
        "20140705",
    ],
)
def test_rdate_is_included(calendars, day):
    events = calendars.rdate_hackerpublicradio.at(day)
    assert len(events) == 1


def test_rdate_does_not_double_rrule_entry(calendars):
    """
    When the combination of the "RRULE" and "RDATE" properties in a
    recurring component produces multiple instances having the same
    start DATE-TIME value, they should be collapsed to, and
    considered as, a single instance.
    """
    events = calendars.rdate.at("20140705")
    assert len(events) == 1


def test_rdate_can_be_excluded_by_exdate(calendars):
    events = calendars.rdate.at("20250705")
    assert len(events) == 0


def test_rdate_and_rrule_can_be_excluded_by_exdate(calendars):
    events = calendars.rdate.at("20150705")
    assert len(events) == 0


def test_rdate_occurs_multiple_times(calendars):
    """An event can not only have an RDATE once but also many of them."""
    events = list(calendars.rdate_hackerpublicradio.all())
    assert len(events) == 12

```

### `recurring_ical_events/test/test_readme.py`

```py
"""
Test the README file.

This is necessary because a deployment does not work if the README file
has errors.

Credits: https://stackoverflow.com/a/47494076/1320237
"""

from pathlib import Path

import restructuredtext_lint

HERE = Path(__file__).parent
readme_path = Path(HERE).parent.parent / "README.rst"


def test_readme_file():
    """CHeck README file for errors."""
    messages = restructuredtext_lint.lint_file(str(readme_path))
    error_message = "expected to have no messages about the README file!"
    for message in messages:
        print(message.astext())
        error_message += "\n" + message.astext()
    assert len(messages) == 0, error_message

```

### `recurring_ical_events/test/test_recurrence_sequence_number.py`

```py
"""
Tests for modified recurrences with lower sequence number than their base event
"""


def test_modified_recurrence_lower_sequence_number(calendars):
    events = calendars.recurrence_sequence_number.at("20200922")
    assert len(events) == 1
    assert events[0].get("SUMMARY") == "Modified event"

```

### `recurring_ical_events/test/test_repeated_properties.py`

```py
def test_duplicated_rrule(calendars):
    # Test that a repetition of the same `RRULE` property should be ignored
    assert len(calendars.duplicated_rrule.at(2023)) == 20

```

### `recurring_ical_events/test/test_repetitions_do_not_change.py`

```py
"""The objective of this test is to ensure that repeated events can be copied
into an ICAL calendar again without multiplying themselves to wrong dates.
"""

import recurring_ical_events


def assert_event_does_not_duplicate(event):
    for i, _ in enumerate(recurring_ical_events.of(event).all()):
        assert i <= 1, event


def assert_events_do_not_duplicate(events):
    assert events
    for event in events:
        assert_event_does_not_duplicate(event)


def test_simple_event(calendars):
    """An event with no repetitions."""
    assert_events_do_not_duplicate(calendars.duration.at(2018))


def test_rdate_event(calendars):
    """An event with rdate."""
    assert_events_do_not_duplicate(calendars.rdate_hackerpublicradio.all())


def test_rrule(calendars):
    """An event with rrule and a number of events."""
    assert_events_do_not_duplicate(calendars.event_10_times.at(2020))


def test_rrule_with_exdate(calendars):
    """An event with rrule and exrule."""
    assert_events_do_not_duplicate(calendars.each_week_but_two_deleted.at(2019))


def test_exdate_is_removed_because_it_is_not_needed(calendars):
    """A repeated event removed RDATE and RRULE and as such should
    also remove the EXDATE values."""
    for event in calendars.rdate.all():
        assert "EXDATE" not in event

```

### `recurring_ical_events/test/test_simple_recurrent_events.py`

```py
import pytest

from recurring_ical_events.constants import DATE_MAX


def test_event_is_not_included_if_it_is_later(calendars):
    events = calendars.three_events.between((2000, 1, 1), (2001, 1, 1))
    assert not events


def test_event_is_not_included_if_it_is_earlier(calendars):
    events = calendars.three_events.between((2030, 1, 1), DATE_MAX)
    assert not events


def test_all_events_in_time_span(calendars):
    events = calendars.three_events.between((2000, 1, 1), DATE_MAX)
    assert len(events) == 3


@pytest.mark.parametrize(
    ("count", "end"),
    [
        (0, (2019, 3, 3)),
        (1, (2019, 3, 5)),
        (2, (2019, 3, 8)),
    ],
)
def test_events_occur_after_and_before_span_end(calendars, count, end):
    events = calendars.three_events.between((2000, 1, 1), end)
    assert len(events) == count


@pytest.mark.parametrize(
    ("count", "start"),
    [
        (3, (2019, 3, 3)),
        (2, (2019, 3, 5)),
        (1, (2019, 3, 8)),
    ],
)
def test_events_occur_after_and_before_span_start(calendars, count, start):
    events = calendars.three_events.between(start, DATE_MAX)
    assert len(events) == count

```

### `recurring_ical_events/test/test_single_events.py`

```py
from recurring_ical_events.constants import DATE_MAX


def test_a_calendar_with_no_events_has_no_events(calendars):
    events = calendars.no_events.between((2000, 1, 1), DATE_MAX)
    assert not events


def test_a_calendar_with_one_event_has_one_event(calendars):
    events = calendars.one_event.between((2000, 1, 1), DATE_MAX)
    assert len(events) == 1


def test_event_is_not_included_if_it_is_later(calendars):
    events = calendars.one_event.between((2000, 1, 1), (2001, 1, 1))
    assert not events


def test_event_is_not_included_if_it_is_earlier(calendars):
    events = calendars.one_event.between((2030, 1, 1), DATE_MAX)
    assert not events


def test_all_events(calendars):
    assert len(list(calendars.one_event.all())) == 1
    assert len(list(calendars.no_events.all())) == 0

```

### `recurring_ical_events/test/test_skip_bad_events.py`

```py
from datetime import date

import pytest

from recurring_ical_events import of
from recurring_ical_events.errors import InvalidCalendar


@pytest.mark.parametrize(
    ("calendar_name", "start", "end"),
    [
        ("bad_rrule_missing_until_event", date(2019, 3, 1), date(2019, 12, 31)),
    ],
)
def test_skip_bad_events(calendars, calendar_name, start, end):
    calendar = calendars.raw[calendar_name]
    with pytest.raises(InvalidCalendar):
        rcalendar = of(calendar, skip_bad_series=False)
        rcalendar.between(start, end)

    rcalendar = of(calendar, skip_bad_series=True)
    rcalendar.between(start, end)

```

### `recurring_ical_events/test/test_time_arguments.py`

```py
"""This file tests whether the time input is correctly converted.

Also see test_convert_inputs.py
"""

from datetime import datetime

import pytest
from pytz import utc

from recurring_ical_events.query import CalendarQuery


@pytest.mark.parametrize(
    ("input_date", "output_datetime"),
    [
        ((2019, 1, 1), datetime(2019, 1, 1)),
        ((2000, 12, 2), datetime(2000, 12, 2)),
        ((2000, 12, 2, 4), datetime(2000, 12, 2, 4)),
        ((2000, 12, 2, 4, 44), datetime(2000, 12, 2, 4, 44)),
        ((2000, 12, 2, 4, 44, 55), datetime(2000, 12, 2, 4, 44, 55)),
        (datetime(2001, 3, 12, tzinfo=utc), datetime(2001, 3, 12, tzinfo=utc)),
        ("20140511T000000Z", datetime(2014, 5, 11)),
        ("20150521", datetime(2015, 5, 21)),
    ],
)
def test_conversion(input_date, output_datetime):
    assert CalendarQuery.to_datetime(input_date) == output_datetime

```

### `recurring_ical_events/test/test_time_span_contains_event.py`

```py
from datetime import date, datetime

import pytest
from pytz import timezone, utc

from recurring_ical_events.errors import PeriodEndBeforeStart
from recurring_ical_events.util import time_span_contains_event

berlin = timezone("Europe/Berlin").localize


@pytest.mark.parametrize(
    ("span_start", "span_stop", "event_start", "event_stop", "result", "message"),
    [
        (0, 5, 1, 3, True, "event lies inside"),
        (0, 5, -3, -1, False, "event lies before"),
        (0, 5, 34, 41, False, "event lies after "),
        (0, 5, 4, 6, True, "event overlaps end"),
        (0, 5, -1, 2, True, "event overlaps start"),
        (0, 5, -1, 7, True, "event overlaps start and end"),
        (0, 5, 0, 4, True, "event begins at start"),
        (0, 5, 1, 5, True, "event ends at end"),
        # check that datetime and date can be used and mixed
        (
            datetime(2019, 1, 1, 1),
            datetime(2019, 1, 4, 1),
            date(2019, 1, 2),
            date(2019, 1, 3),
            True,
            "date is in datetime span",
        ),
        (
            date(2019, 1, 3),
            date(2019, 1, 4),
            date(2019, 1, 2),
            date(2019, 1, 3),
            False,
            "date is before span",
        ),
        (
            date(2019, 1, 4),
            date(2019, 1, 4),
            datetime(2019, 1, 2, 1),
            datetime(2019, 1, 4),
            False,
            "datetime is before date span start",
        ),
        (
            date(2019, 1, 4),
            date(2019, 1, 5),
            datetime(2019, 1, 4, 1),
            datetime(2019, 1, 4, 2),
            True,
            "datetime is in date span end",
        ),
        (
            berlin(datetime(2019, 1, 1, 1)),
            berlin(datetime(2019, 1, 4, 2)),
            datetime(2019, 1, 4, 1, 10),
            datetime(2019, 1, 4, 1, 20),
            True,
            "without time zone is put into time zone",
        ),
        (
            berlin(datetime(2019, 1, 1, 1)),
            berlin(datetime(2019, 1, 1, 2)),
            datetime(2019, 1, 1, 0, tzinfo=utc),
            datetime(2019, 1, 1, 1, tzinfo=utc),
            True,
            "comparing times from different time zones 1",
        ),
        (
            berlin(datetime(2019, 1, 1, 4)),
            berlin(datetime(2019, 1, 1, 5)),
            datetime(2019, 1, 1, 0, tzinfo=utc),
            datetime(2019, 1, 1, 1, tzinfo=utc),
            False,
            "comparing times from different time zones 2",
        ),
        # The end of the VEVENT is exclusive, see RFC5545
        #    Note that the "DTEND" property is
        #    set to July 9th, 2007, since the "DTEND" property specifies the
        #    non-inclusive end of the event.
        #
        # Tests:
        # - We should not include an event which ends at a requested start date.
        # - We should include an event which ends at an end date but is included
        #  in the range.
        (
            date(2019, 1, 4),
            date(2019, 1, 5),
            date(2019, 1, 3),
            date(2019, 1, 4),
            False,
            "We should not include an event which ends at a requested start date.",
        ),
        (
            datetime(2019, 1, 4),
            datetime(2019, 1, 5),
            date(2019, 1, 3),
            date(2019, 1, 4),
            False,
            "We should not include an event which ends at a requested start date.",
        ),
        (
            datetime(2019, 1, 4),
            datetime(2019, 1, 5),
            datetime(2019, 1, 4, 3),
            datetime(2019, 1, 5),
            True,
            "We should include an event which ends at an end date but is included",
        ),
        # Events with 0 duration should be tested
        (0, 1, 0, 0, True, "zero size event at start"),
        (0, 2, 1, 1, True, "zero size event in middle"),
        (0, 1, 1, 1, False, "zero size event at end"),
        (1, 1, 1, 1, True, "zero size event at zero size span"),
        (
            date(2019, 1, 4),
            date(2019, 1, 4),
            date(2019, 1, 4),
            date(2019, 1, 4),
            True,
            "We should include an event which is of the same size as the span",
        ),
        (
            date(2019, 1, 3),
            date(2019, 1, 4),
            date(2019, 1, 4),
            date(2019, 1, 4),
            False,
            "We should NOT include an event which ends at an end date but is included",
        ),
        (0, 0, 1, 1, False, "zero size event after"),
        (2, 2, 1, 1, False, "zero size event before"),
        # Test the exclusivity of the end of the span
        (
            1,
            3,
            3,
            4,
            False,
            "When the event starts at the end of the span, it should not be included.",
        ),
        # Test zero size spans
        (1, 1, 0, 0, False, "zero size event before zero size span"),
        (1, 1, 0, 1, False, "event ending at zero size span"),
        (1, 1, 0, 2, True, "event around zero size span"),
        (1, 1, 1, 2, True, "event starting at zero size span"),
        (1, 1, 2, 3, False, "event after zero size span"),
        (1, 1, 2, 2, False, "zero size event after zero size span"),
    ],
)
def test_time_span_inclusion(
    span_start, span_stop, event_start, event_stop, result, message
):
    assert (
        time_span_contains_event(
            span_start,
            span_stop,
            event_start,
            event_stop,
        )
        == result
    ), message


@pytest.mark.parametrize(
    ("span_start", "span_stop", "event_start", "event_stop", "exception_message"),
    [
        (1, 2, 1, 2, None),
        (1, 1, 1, 1, None),
        (1, 2, 2, 1, r"^the event"),
        (2, 1, 1, 2, r"^the time span"),
        (date(2024, 4, 4), date(2024, 4, 4), date(2024, 4, 4), date(2024, 4, 4), None),
        (date(2024, 4, 4), date(2024, 4, 5), date(2024, 4, 4), date(2024, 4, 5), None),
        (
            date(2024, 4, 4),
            date(2024, 4, 5),
            date(2024, 4, 5),
            date(2024, 4, 4),
            r"^the event",
        ),
        (
            date(2024, 4, 5),
            date(2024, 4, 4),
            date(2024, 4, 4),
            date(2024, 4, 5),
            r"^the time span",
        ),
        (
            datetime(2024, 4, 4),
            datetime(2024, 4, 4),
            datetime(2024, 4, 4),
            datetime(2024, 4, 4),
            None,
        ),
        (
            datetime(2024, 4, 4),
            datetime(2024, 4, 5),
            datetime(2024, 4, 4),
            datetime(2024, 4, 5),
            None,
        ),
        (
            datetime(2024, 4, 4),
            datetime(2024, 4, 5),
            datetime(2024, 4, 5),
            datetime(2024, 4, 4),
            r"^the event",
        ),
        (
            datetime(2024, 4, 5),
            datetime(2024, 4, 4),
            datetime(2024, 4, 4),
            datetime(2024, 4, 5),
            r"^the time span",
        ),
    ],
)
def test_time_span_end_before_start_raise_exception(
    span_start, span_stop, event_start, event_stop, exception_message
):
    if exception_message:
        with pytest.raises(PeriodEndBeforeStart, match=exception_message):
            time_span_contains_event(span_start, span_stop, event_start, event_stop)
    else:
        time_span_contains_event(span_start, span_stop, event_start, event_stop)

```

### `recurring_ical_events/test/test_time_zones_differ.py`

```py
"""Imputs of different time zones should make a difference in the output"""

import datetime

import pytest
import pytz


@pytest.mark.parametrize(
    ("date", "hours", "timezone", "number_of_events", "calendar_name"),
    [
        # DTSTART;TZID=Europe/Berlin:20190304T000000
        # time zone offset 6:07:00 between Europe/Berlin and Asia/Ho_Chi_Minh
        ((2019, 3, 4), 24, "Europe/Berlin", 1, "three_events"),
        ((2019, 3, 4), 24, "America/Panama", 0, "three_events"),
        ((2019, 3, 4), 24, "Asia/Ho_Chi_Minh", 1, "three_events"),
        ((2019, 3, 4), 1, "Asia/Ho_Chi_Minh", 0, "three_events"),
        ((2019, 3, 4), 6, "Asia/Ho_Chi_Minh", 0, "three_events"),
        ((2019, 3, 4), 7, "Asia/Ho_Chi_Minh", 1, "three_events"),
        # events that have no time zone, New Year
        ((2019, 1, 1), 1, "Europe/Berlin", 1, "Germany"),
        ((2019, 1, 1), 1, "Asia/Ho_Chi_Minh", 1, "Germany"),
        ((2019, 1, 1), 1, "America/Panama", 1, "Germany"),
    ],
)
def test_include_events_if_the_time_zone_differs(
    calendars, date, hours, timezone, number_of_events, calendar_name
):
    """When the time zone is different, events can be included or
    excluded because they are in another time zone.
    """
    tzinfo = pytz.timezone(timezone)
    start = tzinfo.localize(datetime.datetime(*date))
    stop = start + datetime.timedelta(hours=hours)
    events = calendars[calendar_name].between(start, stop)
    assert len(events) == number_of_events, (
        f"in calendar {calendar_name} and {date} in {timezone}"
    )

```

### `recurring_ical_events/test/test_timedelta_for_between.py`

```py
"""This tests that a timedelta can be used as the second argument to between.

This is useful when you do not want to calculate this yourself.
"""

from datetime import timedelta

import pytest


@pytest.mark.parametrize(
    ("start", "delta", "count"),
    [
        ("20190301", timedelta(days=3), 0),
        ("20190301", timedelta(days=5), 1),
        ("20190301", timedelta(days=3, hours=8), 0),
        ("20190301", timedelta(days=3, hours=9), 1),
        ("20190301", timedelta(days=3, hours=8, seconds=1), 1),
        ("20190304", timedelta(days=1), 1),
        ("20190304", timedelta(hours=8), 0),
        ("20190304", timedelta(hours=9), 1),
    ],
)
def test_event_with_between_and_timedelta(calendars, start, delta, count):
    """The event starts at 20190304T080000 and ends at 20190304T080000"""
    events = calendars.one_event.between(start, delta)
    assert len(events) == count

```

### `recurring_ical_events/test/test_util_functions.py`

```py
"""Check some utility functions."""

from typing import NamedTuple

import pytest

from recurring_ical_events.util import with_highest_sequence


class Component(NamedTuple):
    sequence: int


@pytest.mark.parametrize(
    ("a1", "a2", "result"),
    [
        (None, None, None),
        (Component(1), Component(2), Component(2)),
        (Component(5), Component(2), Component(5)),
        (Component(1), None, Component(1)),
        (None, Component(4), Component(4)),
        (None, Component(-3), Component(-3)),
        (Component(-1), None, Component(-1)),
    ],
)
def test_highest_sequence(a1, a2, result):
    """Check the result"""
    assert with_highest_sequence(a1, a2) == result

```

### `recurring_ical_events/test/test_with_doctest.py`

```py
"""This file tests the source code provided by the documentation.

See
- doctest documentation: https://docs.python.org/3/library/doctest.html
- Issue 443: https://github.com/collective/icalendar/issues/443

This file should be tests, too:

    >>> print("Hello World!")
    Hello World!

"""

import doctest
import importlib
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).parent
PROJECT_PATH = HERE.parent.parent

PYTHON_FILES = list(PROJECT_PATH.rglob("*.py"))

MODULE_NAMES = [
    "recurring_ical_events",
]


@pytest.mark.parametrize("module_name", MODULE_NAMES)
def test_docstring_of_python_file(module_name):
    """This test runs doctest on the Python module."""
    module = importlib.import_module(module_name)
    test_result = doctest.testmod(module, name=module_name)
    assert test_result.failed == 0, f"{test_result.failed} errors in {module_name}"


# This collection needs to exclude .tox and other subdirectories
DOCS = PROJECT_PATH / "docs"
DOCUMENT_PATHS = [
    PROJECT_PATH / "README.rst",
    *list(DOCS.glob("*/*.rst")),
    *list(DOCS.glob("*.rst")),
    *list(DOCS.glob("*/*.md")),
    *list(DOCS.glob("*/*.md")),
]


@pytest.mark.parametrize("document", DOCUMENT_PATHS)
def test_documentation_file(document, env_for_doctest):
    """This test runs doctest on a documentation file.

    functions are also replaced to work.
    """
    test_result = doctest.testfile(
        str(document),
        module_relative=False,
        globs=env_for_doctest,
        raise_on_error=False,
    )
    assert test_result.failed == 0, f"{test_result.failed} errors in {document.name}"


def test_can_import_zoneinfo(env_for_doctest):  # noqa: ARG001
    """Allow importing zoneinfo for tests."""
    assert "zoneinfo" in sys.modules

```

### `recurring_ical_events/test/test_x_wr_timezone.py`

```py
"""These test the support of the non-standard X-WR-TIMEZONE attribute.

See Issue 71: https://github.com/niccokunzmann/python-recurring-ical-events/issues/71
"""

import datetime

import pytest
from pytz import UTC, timezone

from recurring_ical_events.util import timestamp

tz_london = timezone("Europe/London")

c1_t_utc = UTC.localize(datetime.datetime(2013, 8, 3, 19))
c1_t_london = tz_london.localize(datetime.datetime(2013, 8, 3, 20))

hour_1 = datetime.timedelta(hours=1)
hour_2 = hour_1 + hour_1


def test_dates_are_equal():
    """These dates need to be equal so that the next test 'test_events_with_x_wr_timezone_returned()' works."""
    t1 = timestamp(c1_t_utc)
    t2 = timestamp(c1_t_london)
    assert t1 == t2, f"time stamp should equal, delta {t1 - t2}"
    assert c1_t_utc == c1_t_london, "dates should equal"


c1 = "rdate_hackerpublicradio"
c2 = "x_wr_timezone_simple_events_issue_59"


@pytest.mark.parametrize(
    ("calendar_name", "a_date", "event_count", "message"),
    [
        # test c1
        #     Europe/London changes into summer time after March to October.
        #     We test with UTC as time zone
        (c1, c1_t_utc, 1, "(1) Exact start of the first event."),
        (c1, c1_t_utc + hour_1, 1, "(1) Middle of the first event."),
        (c1, c1_t_utc + hour_2, 0, "(1) Exact end of the first event."),
        #     Other time zone as argument
        (c1, c1_t_london, 1, "(2) Exact start of the first event. (London)"),
        (c1, c1_t_london + hour_1, 1, "(2) Middle of the first event. (London)"),
        (c1, c1_t_london + hour_2, 0, "(2) Exact end of the first event. (London)"),
        # test c2
        #     here, we have the dates and times of the events given
        #     test the first event
        (c2, (2021, 12, 22, 12, 0), 1, "(3) Exact start of the event. New York"),
        (c2, (2021, 12, 22, 11, 59), 0, "(3) Before the event. New York"),
        (c2, (2021, 12, 22, 12, 59), 1, "(3) Event almost over. New York"),
        (c2, (2021, 12, 22, 13, 0), 0, "(3) After the event. New York"),
        #    second event
        (c2, (2021, 12, 22, 21), 1, "(4) Exact start of the event. New York"),
        (c2, (2021, 12, 22, 20, 59), 0, "(4) Before the event. New York"),
        (c2, (2021, 12, 22, 21, 59), 1, "(4) Event almost over. New York"),
        (c2, (2021, 12, 22, 22), 0, "(4) After the event. New York"),
    ],
)
def test_events_with_x_wr_timezone_returned(
    calendars, calendar_name, a_date, event_count, message
):
    """Test that X-WR-TIMEZONE influences the event results."""
    calendar = calendars[calendar_name]
    for e in calendar.all():
        print(e.to_ical().decode("UTF-8"))
    events = calendar.at(a_date)
    assert len(events) == event_count, message

```

### `recurring_ical_events/test/test_zero_size_events.py`

```py
"""This tests events of zero size.

In the specification, the DTSTART is the only mandatory attribute.
DTEND and DURATION are both optimal.
"""

import pytest


@pytest.mark.parametrize(
    ("date", "event_count"),
    [
        # DTSTART:20190304T080000
        ("20190303", 0),
        ("20190304", 1),
        ("20190305", 0),
        ((2019, 3, 4, 7), 0),
        ((2019, 3, 4, 8), 1),
        ((2019, 3, 4, 9), 0),
    ],
)
def test_zero_sized_events_at(calendars, date, event_count):
    events = calendars.zero_size_event.at(date)
    assert len(events) == event_count


@pytest.mark.parametrize(
    ("start", "stop", "event_count", "message"),
    [
        # DTSTART:20190304T080000
        ((2019, 3, 4, 7), (2019, 3, 4, 8), 0, "event is at end of span"),
        ((2019, 3, 4, 8), (2019, 3, 4, 9), 1, "event is at start of span"),
        ((2019, 3, 4, 8), (2019, 3, 4, 8), 1, "event is at the exact span"),
    ],
)
def test_zero_sized_events_at_2(calendars, start, stop, event_count, message):
    events = calendars.zero_size_event.between(start, stop)
    assert len(events) == event_count, message

```

### `recurring_ical_events/test/test_zoneinfo_issue_57.py`

```py
"""Test that zoneinfo timezones can be used.

See also Issue https://github.com/niccokunzmann/python-recurring-ical-events/issues/57
"""

import sys
from datetime import datetime, timedelta

import pytest
import pytz
from icalendar import Calendar, Event, vDDDTypes

import recurring_ical_events
import recurring_ical_events.util


def test_zoneinfo_example_yields_events(ZoneInfo):
    """Test that there is no error.

    Source code is taken from Issue 57.
    """
    tz = ZoneInfo("Europe/London")

    cal = Calendar()
    event = Event()
    cal.add_component(event)

    dt = datetime(2021, 6, 24, 21, 15).astimezone().astimezone(tz)
    # datetime.datetime(2021, 6, 24, 21, 15, tzinfo=zoneinfo.ZoneInfo(key='Europe/London'))
    d = dt.date()

    event["dtstart"] = vDDDTypes(dt)

    events = recurring_ical_events.of(cal).between(d, d + timedelta(1))

    assert len(events) == 1, "The event was found."


def test_zoneinfo_must_be_installed_if_it_is_possible():
    """Make sure that zoneinfo and tzdata are installed if possible."""
    python_version = sys.version_info[:2]
    if python_version < (3, 7):
        return  # no zoneinfo
    from importlib.util import find_spec as module_exists

    if python_version <= (3, 8):
        assert module_exists("backports.zoneinfo"), (
            "zoneinfo should be installed with pip install backports.zoneinfo"
        )
    else:
        assert module_exists("zoneinfo"), "We assume that zoneinfo exists."
    assert module_exists("tzdata"), (
        "tzdata is necessary to test current time zone understanding."
    )


@pytest.mark.parametrize(
    "dt1",
    [
        datetime(2019, 4, 24, 19),
        pytz.timezone("Europe/Berlin").localize(datetime(2019, 4, 24, 19)),
        pytz.timezone("America/New_York").localize(datetime(2019, 4, 24, 19)),
    ],
)
def test_zoneinfo_consistent_conversion(calendars, dt1):
    """Make sure that the conversion function actually works."""
    dt2 = calendars.consistent_tz(dt1)
    assert dt1.year == dt2.year
    assert dt1.month == dt2.month
    assert dt1.day == dt2.day
    assert dt1.hour == dt2.hour
    assert dt1.minute == dt2.minute
    assert dt1.second == dt2.second


ATTRS = ["year", "month", "day", "hour", "minute", "second"]


@pytest.mark.parametrize(
    ("dt", "tz", "times"),
    [
        (datetime(2019, 2, 22, 4, 30), "Europe/Berlin", (2019, 2, 22, 4, 30)),
        (datetime(2019, 2, 22, 4, 30), "UTC", (2019, 2, 22, 4, 30)),
    ],
)
def test_convert_to_date(dt, tz, times, ZoneInfo):
    """Check that a datetime conversion takes place properly."""
    new = recurring_ical_events.util.convert_to_datetime(dt, ZoneInfo(tz))
    converted = ()
    for attr, _ in zip(ATTRS, times):
        converted += (getattr(new, attr),)
    assert converted == times

```

### `recurring_ical_events/types.py`

```py
"""Type annotations."""

from __future__ import annotations

import datetime
from typing import Tuple, Union

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

# Any types documented here should also be mentioned in the docs/conf.py.

Time: TypeAlias = Union[datetime.date, datetime.datetime]
DateArgument: TypeAlias = Union[Tuple[int], datetime.date, str, int]
UID: TypeAlias = str
Timestamp: TypeAlias = float
RecurrenceID: TypeAlias = datetime.datetime
RecurrenceIDs: TypeAlias = Tuple[RecurrenceID]


__all__ = [
    "UID",
    "DateArgument",
    "RecurrenceID",
    "RecurrenceIDs",
    "Time",
    "Timestamp",
]

```

### `recurring_ical_events/util.py`

```py
"""Utility functions."""

from __future__ import annotations

import datetime
from functools import wraps
from typing import TYPE_CHECKING, Callable, Optional, Sequence

from recurring_ical_events.errors import PeriodEndBeforeStart

if TYPE_CHECKING:
    from recurring_ical_events.adapters.component import ComponentAdapter
    from recurring_ical_events.types import RecurrenceIDs, Time, Timestamp


def timestamp(dt: datetime.datetime) -> Timestamp:
    """Return the time stamp of a datetime"""
    return dt.timestamp()


def convert_to_date(date: Time) -> datetime.date:
    """Converts a date or datetime to a date"""
    return datetime.date(date.year, date.month, date.day)


def is_pytz(tzinfo: datetime.tzinfo | Time):
    """Whether the time zone requires localize() and normalize().

    pytz requires these funtions to be used in order to correctly use the
    time zones after operations.
    """
    return hasattr(tzinfo, "localize")


def normalize_pytz(time: Time) -> Time:
    """We have to normalize the time after a calculation if we use pytz."""
    if is_pytz_dt(time):
        return time.tzinfo.normalize(time)
    return time


def is_date(time: Time) -> bool:
    """Whether this is a date and not a datetime."""
    return isinstance(time, datetime.date) and not isinstance(time, datetime.datetime)


def is_datetime(time: Time) -> bool:
    """Whether this is a datetime and not a date."""
    return isinstance(time, datetime.datetime)


def has_timezone(time: Time) -> bool:
    """Whether this date/datetime has a timezone."""
    return is_datetime(time) and time.tzinfo is not None


def convert_to_datetime(
    date: Time, tzinfo: Optional[datetime.tzinfo]
) -> datetime.datetime:
    """Converts a date to a datetime.

    Dates are converted to datetimes with tzinfo.
    Datetimes loose their timezone if tzinfo is None.
    Datetimes receive tzinfo as a timezone if they do not have a timezone.
    Datetimes retain their timezone if they have one already (tzinfo is not None).
    """
    if is_date(date):
        date = datetime.datetime(date.year, date.month, date.day)  # noqa: DTZ001
    if isinstance(date, datetime.datetime):
        if date.tzinfo is None:
            if tzinfo is not None:
                if is_pytz(tzinfo):
                    return tzinfo.localize(date)
                return date.replace(tzinfo=tzinfo)
        elif tzinfo is None:
            return normalize_pytz(date).replace(tzinfo=None)
        return date
    return date


def convert_to_date_range(dt: Time) -> tuple[datetime.datetime, datetime.datetime]:
    """Convert the datetime to a start and end date in between it occurs.

    Returns:
        (start, end) where start <= dt < end
    """
    start = dt if is_date(dt) else dt.replace(hour=0, microsecond=0, minute=0, second=0)
    return start, start + datetime.timedelta(days=1)


def make_comparable(dates: Sequence[Time]) -> list[Time]:
    """Make an list or tuple of dates comparable.

    Returns an list.
    """
    tzinfo = None
    all_dates = True
    for date in dates:
        if not is_date(date):
            all_dates = False
            if has_timezone(date):
                tzinfo = date.tzinfo
                break
    if all_dates:
        return dates
    return [convert_to_datetime(date, tzinfo) for date in dates]


def time_span_contains_event(
    span_start: Time,
    span_stop: Time,
    event_start: Time,
    event_stop: Time,
    comparable: bool = False,  # noqa: FBT001
) -> bool:
    """Return whether an event should is included within a time span.

    - span_start and span_stop define the time span
    - event_start and event_stop define the event time
    - comparable indicates whether the dates can be compared.
        You can set it to True if you are sure you have timezones and
        date/datetime correctly or used make_comparable() before.

    Note that the stops are exlusive but the starts are inclusive.

    This is an essential function of the module. It should be tested in
    test/test_time_span_contains_event.py.

    This raises a PeriodEndBeforeStart exception if a start is after an end.
    """
    if not comparable:
        span_start, span_stop, event_start, event_stop = make_comparable(
            (span_start, span_stop, event_start, event_stop)
        )
    if event_start > event_stop:
        raise PeriodEndBeforeStart(
            (
                "the event must start before it ends"
                f"(start: {event_start} end: {event_stop})"
            ),
            event_start,
            event_stop,
        )
    if span_start > span_stop:
        raise PeriodEndBeforeStart(
            (
                "the time span must start before it ends"
                f"(start: {span_start} end: {span_stop})"
            ),
            span_start,
            span_stop,
        )
    if event_start == event_stop:
        if span_start == span_stop:
            return event_start == span_start
        return span_start <= event_start < span_stop
    if span_start == span_stop:
        return event_start <= span_start < event_stop
    return event_start < span_stop and span_start < event_stop


def compare_greater(date1: Time, date2: Time) -> bool:
    """Compare two dates if date1 > date2 and make them comparable before."""
    date1, date2 = make_comparable((date1, date2))
    return date1 > date2


def cmp(date1: Time, date2: Time) -> int:
    """Compare two dates, like cmp().

    Returns
    -------
        -1 if date1 < date2
         0 if date1 = date2
         1 if date1 > date2

    """
    # credits: https://www.geeksforgeeks.org/python-cmp-function/
    # see https://stackoverflow.com/a/22490617/1320237
    date1, date2 = make_comparable((date1, date2))
    return (date1 > date2) - (date1 < date2)


def is_pytz_dt(time: Time) -> bool:
    """Whether the time requires localize() and normalize().

    pytz requires these funtions to be used in order to correctly use the
    time zones after operations.
    """
    return isinstance(time, datetime.datetime) and is_pytz(time.tzinfo)


def cached_property(func: Callable) -> property:
    """Cache the property value for speed up."""
    name = f"_cached_{func.__name__}"
    not_found = object()

    @property
    @wraps(func)
    def cached_property(self: object):
        value = self.__dict__.get(name, not_found)
        if value is not_found:
            self.__dict__[name] = value = func(self)
        return value

    return cached_property


def to_recurrence_ids(time: Time) -> RecurrenceIDs:
    """Convert the time to a recurrence id so it can be hashed and recognized.

    The first value should be used to identify a component as it is a datetime in UTC.
    The other values can be used to look the component up.
    """
    # We are inside the Series calculation with this and want to identify
    # a date. It is fair to assume that the timezones are the same now.
    if not isinstance(time, datetime.datetime):
        return (convert_to_datetime(time, None),)
    if time.tzinfo is None:
        return (time,)
    return (
        time.astimezone(datetime.timezone.utc).replace(tzinfo=None),
        time.replace(tzinfo=None),
    )


def with_highest_sequence(
    adapter1: ComponentAdapter | None, adapter2: ComponentAdapter | None
):
    """Return the one with the highest sequence."""
    return max(
        adapter1,
        adapter2,
        key=lambda adapter: -1e10 if adapter is None else adapter.sequence,
    )


def get_any(dictionary: dict, keys: Sequence[object], default: object = None):
    """Get any item from the keys and return it."""
    result = default
    for key in keys:
        result = dictionary.get(key, result)
    return result


__all__ = [
    "PeriodEndBeforeStart",
    "cmp",
    "convert_to_date_range",
    "convert_to_datetime",
    "get_any",
    "has_timezone",
    "is_date",
    "is_datetime",
    "is_pytz",
    "is_pytz_dt",
    "make_comparable",
    "normalize_pytz",
    "time_span_contains_event",
    "to_recurrence_ids",
    "with_highest_sequence",
]

```

### `recurring_ical_events/version.py`

```py
# SPDX-FileCopyrightText: 2024 Nicco Kunzmann and Open Web Calendar Contributors <https://open-web-calendar.quelltext.eu/>
#
# SPDX-License-Identifier: GPL-2.0-only

try:
    from ._version import __version__, __version_tuple__, version, version_tuple
except ModuleNotFoundError:
    __version__ = version = "0.0dev0"
    __version_tuple__ = version_tuple = (0, 0, "dev0")

__all__ = [
    "__version__",
    "__version_tuple__",
    "version",
    "version_tuple",
]

```

### `rfc9074.html`

```html

<!DOCTYPE html>
<html lang="en" class="RFC">
<head>
<meta charset="utf-8">
<meta content="Common,Latin" name="scripts">
<meta content="initial-scale=1.0" name="viewport">
<title>RFC 9074: "VALARM" Extensions for iCalendar</title>
<meta content="Cyrus Daboo" name="author">
<meta content="Kenneth Murchison" name="author">
<meta content='
       This document defines a set of extensions to the iCalendar
      "VALARM" component to enhance the use of alarms and improve
      interoperability between clients and servers. 
       This document updates RFC 5545. 
    ' name="description">
<meta content="xml2rfc 3.9.1" name="generator">
<meta content="alarms" name="keyword">
<meta content="calendaring" name="keyword">
<meta content="iCalendar" name="keyword">
<meta content="CalDAV" name="keyword">
<meta content="9074" name="rfc.number">
<!-- Generator version information:
  xml2rfc 3.9.1
    Python 3.6.10
    appdirs 1.4.4
    ConfigArgParse 1.2.3
    google-i18n-address 2.3.5
    html5lib 1.0.1
    intervaltree 3.0.2
    Jinja2 2.11.2
    kitchen 1.2.6
    lxml 4.4.2
    pycairo 1.19.0
    pycountry 19.8.18
    pyflakes 2.1.1
    PyYAML 5.3.1
    requests 2.22.0
    setuptools 40.6.2
    six 1.14.0
    WeasyPrint 51
-->
<link href="rfc9074.xml" rel="alternate" type="application/rfc+xml">
<link href="#copyright" rel="license">
<style type="text/css">/*

  NOTE: Changes at the bottom of this file overrides some earlier settings.

  Once the style has stabilized and has been adopted as an official RFC style,
  this can be consolidated so that style settings occur only in one place, but
  for now the contents of this file consists first of the initial CSS work as
  provided to the RFC Formatter (xml2rfc) work, followed by itemized and
  commented changes found necssary during the development of the v3
  formatters.

*/

/* fonts */
@import url('https://fonts.googleapis.com/css?family=Noto+Sans'); /* Sans-serif */
@import url('https://fonts.googleapis.com/css?family=Noto+Serif'); /* Serif (print) */
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono'); /* Monospace */

@viewport {
  zoom: 1.0;
  width: extend-to-zoom;
}
@-ms-viewport {
  width: extend-to-zoom;
  zoom: 1.0;
}
/* general and mobile first */
html {
}
body {
  max-width: 90%;
  margin: 1.5em auto;
  color: #222;
  background-color: #fff;
  font-size: 14px;
  font-family: 'Noto Sans', Arial, Helvetica, sans-serif;
  line-height: 1.6;
  scroll-behavior: smooth;
}
.ears {
  display: none;
}

/* headings */
#title, h1, h2, h3, h4, h5, h6 {
  margin: 1em 0 0.5em;
  font-weight: bold;
  line-height: 1.3;
}
#title {
  clear: both;
  border-bottom: 1px solid #ddd;
  margin: 0 0 0.5em 0;
  padding: 1em 0 0.5em;
}
.author {
  padding-bottom: 4px;
}
h1 {
  font-size: 26px;
  margin: 1em 0;
}
h2 {
  font-size: 22px;
  margin-top: -20px;  /* provide offset for in-page anchors */
  padding-top: 33px;
}
h3 {
  font-size: 18px;
  margin-top: -36px;  /* provide offset for in-page anchors */
  padding-top: 42px;
}
h4 {
  font-size: 16px;
  margin-top: -36px;  /* provide offset for in-page anchors */
  padding-top: 42px;
}
h5, h6 {
  font-size: 14px;
}
#n-copyright-notice {
  border-bottom: 1px solid #ddd;
  padding-bottom: 1em;
  margin-bottom: 1em;
}
/* general structure */
p {
  padding: 0;
  margin: 0 0 1em 0;
  text-align: left;
}
div, span {
  position: relative;
}
div {
  margin: 0;
}
.alignRight.art-text {
  background-color: #f9f9f9;
  border: 1px solid #eee;
  border-radius: 3px;
  padding: 1em 1em 0;
  margin-bottom: 1.5em;
}
.alignRight.art-text pre {
  padding: 0;
}
.alignRight {
  margin: 1em 0;
}
.alignRight > *:first-child {
  border: none;
  margin: 0;
  float: right;
  clear: both;
}
.alignRight > *:nth-child(2) {
  clear: both;
  display: block;
  border: none;
}
svg {
  display: block;
}
.alignCenter.art-text {
  background-color: #f9f9f9;
  border: 1px solid #eee;
  border-radius: 3px;
  padding: 1em 1em 0;
  margin-bottom: 1.5em;
}
.alignCenter.art-text pre {
  padding: 0;
}
.alignCenter {
  margin: 1em 0;
}
.alignCenter > *:first-child {
  border: none;
  /* this isn't optimal, but it's an existence proof.  PrinceXML doesn't
     support flexbox yet.
  */
  display: table;
  margin: 0 auto;
}

/* lists */
ol, ul {
  padding: 0;
  margin: 0 0 1em 2em;
}
ol ol, ul ul, ol ul, ul ol {
  margin-left: 1em;
}
li {
  margin: 0 0 0.25em 0;
}
.ulCompact li {
  margin: 0;
}
ul.empty, .ulEmpty {
  list-style-type: none;
}
ul.empty li, .ulEmpty li {
  margin-top: 0.5em;
}
ul.ulBare, li.ulBare {
  margin-left: 0em !important;
}
ul.compact, .ulCompact,
ol.compact, .olCompact {
  line-height: 100%;
  margin: 0 0 0 2em;
}

/* definition lists */
dl {
}
dl > dt {
  float: left;
  margin-right: 1em;
}
/* 
dl.nohang > dt {
  float: none;
}
*/
dl > dd {
  margin-bottom: .8em;
  min-height: 1.3em;
}
dl.compact > dd, .dlCompact > dd {
  margin-bottom: 0em;
}
dl > dd > dl {
  margin-top: 0.5em;
  margin-bottom: 0em;
}

/* links */
a {
  text-decoration: none;
}
a[href] {
  color: #22e; /* Arlen: WCAG 2019 */
}
a[href]:hover {
  background-color: #f2f2f2;
}
figcaption a[href],
a[href].selfRef {
  color: #222;
}
/* XXX probably not this:
a.selfRef:hover {
  background-color: transparent;
  cursor: default;
} */

/* Figures */
tt, code, pre, code {
  background-color: #f9f9f9;
  font-family: 'Roboto Mono', monospace;
}
pre {
  border: 1px solid #eee;
  margin: 0;
  padding: 1em;
}
img {
  max-width: 100%;
}
figure {
  margin: 0;
}
figure blockquote {
  margin: 0.8em 0.4em 0.4em;
}
figcaption {
  font-style: italic;
  margin: 0 0 1em 0;
}
@media screen {
  pre {
    overflow-x: auto;
    max-width: 100%;
    max-width: calc(100% - 22px);
  }
}

/* aside, blockquote */
aside, blockquote {
  margin-left: 0;
  padding: 1.2em 2em;
}
blockquote {
  background-color: #f9f9f9;
  color: #111; /* Arlen: WCAG 2019 */
  border: 1px solid #ddd;
  border-radius: 3px;
  margin: 1em 0;
}
cite {
  display: block;
  text-align: right;
  font-style: italic;
}

/* tables */
table {
  width: 100%;
  margin: 0 0 1em;
  border-collapse: collapse;
  border: 1px solid #eee;
}
th, td {
  text-align: left;
  vertical-align: top;
  padding: 0.5em 0.75em;
}
th {
  text-align: left;
  background-color: #e9e9e9;
}
tr:nth-child(2n+1) > td {
  background-color: #f5f5f5;
}
table caption {
  font-style: italic;
  margin: 0;
  padding: 0;
  text-align: left;
}
table p {
  /* XXX to avoid bottom margin on table row signifiers. If paragraphs should
     be allowed within tables more generally, it would be far better to select on a class. */
  margin: 0;
}

/* pilcrow */
a.pilcrow {
  color: #666; /* Arlen: AHDJ 2019 */
  text-decoration: none;
  visibility: hidden;
  user-select: none;
  -ms-user-select: none;
  -o-user-select:none;
  -moz-user-select: none;
  -khtml-user-select: none;
  -webkit-user-select: none;
  -webkit-touch-callout: none;
}
@media screen {
  aside:hover > a.pilcrow,
  p:hover > a.pilcrow,
  blockquote:hover > a.pilcrow,
  div:hover > a.pilcrow,
  li:hover > a.pilcrow,
  pre:hover > a.pilcrow {
    visibility: visible;
  }
  a.pilcrow:hover {
    background-color: transparent;
  }
}

/* misc */
hr {
  border: 0;
  border-top: 1px solid #eee;
}
.bcp14 {
  font-variant: small-caps;
}

.role {
  font-variant: all-small-caps;
}

/* info block */
#identifiers {
  margin: 0;
  font-size: 0.9em;
}
#identifiers dt {
  width: 3em;
  clear: left;
}
#identifiers dd {
  float: left;
  margin-bottom: 0;
}
#identifiers .authors .author {
  display: inline-block;
  margin-right: 1.5em;
}
#identifiers .authors .org {
  font-style: italic;
}

/* The prepared/rendered info at the very bottom of the page */
.docInfo {
  color: #666; /* Arlen: WCAG 2019 */
  font-size: 0.9em;
  font-style: italic;
  margin-top: 2em;
}
.docInfo .prepared {
  float: left;
}
.docInfo .prepared {
  float: right;
}

/* table of contents */
#toc  {
  padding: 0.75em 0 2em 0;
  margin-bottom: 1em;
}
nav.toc ul {
  margin: 0 0.5em 0 0;
  padding: 0;
  list-style: none;
}
nav.toc li {
  line-height: 1.3em;
  margin: 0.75em 0;
  padding-left: 1.2em;
  text-indent: -1.2em;
}
/* references */
.references dt {
  text-align: right;
  font-weight: bold;
  min-width: 7em;
}
.references dd {
  margin-left: 8em;
  overflow: auto;
}

.refInstance {
  margin-bottom: 1.25em;
}

.references .ascii {
  margin-bottom: 0.25em;
}

/* index */
.index ul {
  margin: 0 0 0 1em;
  padding: 0;
  list-style: none;
}
.index ul ul {
  margin: 0;
}
.index li {
  margin: 0;
  text-indent: -2em;
  padding-left: 2em;
  padding-bottom: 5px;
}
.indexIndex {
  margin: 0.5em 0 1em;
}
.index a {
  font-weight: 700;
}
/* make the index two-column on all but the smallest screens */
@media (min-width: 600px) {
  .index ul {
    -moz-column-count: 2;
    -moz-column-gap: 20px;
  }
  .index ul ul {
    -moz-column-count: 1;
    -moz-column-gap: 0;
  }
}

/* authors */
address.vcard {
  font-style: normal;
  margin: 1em 0;
}

address.vcard .nameRole {
  font-weight: 700;
  margin-left: 0;
}
address.vcard .label {
  font-family: "Noto Sans",Arial,Helvetica,sans-serif;
  margin: 0.5em 0;
}
address.vcard .type {
  display: none;
}
.alternative-contact {
  margin: 1.5em 0 1em;
}
hr.addr {
  border-top: 1px dashed;
  margin: 0;
  color: #ddd;
  max-width: calc(100% - 16px);
}

/* temporary notes */
.rfcEditorRemove::before {
  position: absolute;
  top: 0.2em;
  right: 0.2em;
  padding: 0.2em;
  content: "The RFC Editor will remove this note";
  color: #9e2a00; /* Arlen: WCAG 2019 */
  background-color: #ffd; /* Arlen: WCAG 2019 */
}
.rfcEditorRemove {
  position: relative;
  padding-top: 1.8em;
  background-color: #ffd; /* Arlen: WCAG 2019 */
  border-radius: 3px;
}
.cref {
  background-color: #ffd; /* Arlen: WCAG 2019 */
  padding: 2px 4px;
}
.crefSource {
  font-style: italic;
}
/* alternative layout for smaller screens */
@media screen and (max-width: 1023px) {
  body {
    padding-top: 2em;
  }
  #title {
    padding: 1em 0;
  }
  h1 {
    font-size: 24px;
  }
  h2 {
    font-size: 20px;
    margin-top: -18px;  /* provide offset for in-page anchors */
    padding-top: 38px;
  }
  #identifiers dd {
    max-width: 60%;
  }
  #toc {
    position: fixed;
    z-index: 2;
    top: 0;
    right: 0;
    padding: 0;
    margin: 0;
    background-color: inherit;
    border-bottom: 1px solid #ccc;
  }
  #toc h2 {
    margin: -1px 0 0 0;
    padding: 4px 0 4px 6px;
    padding-right: 1em;
    min-width: 190px;
    font-size: 1.1em;
    text-align: right;
    background-color: #444;
    color: white;
    cursor: pointer;
  }
  #toc h2::before { /* css hamburger */
    float: right;
    position: relative;
    width: 1em;
    height: 1px;
    left: -164px;
    margin: 6px 0 0 0;
    background: white none repeat scroll 0 0;
    box-shadow: 0 4px 0 0 white, 0 8px 0 0 white;
    content: "";
  }
  #toc nav {
    display: none;
    padding: 0.5em 1em 1em;
    overflow: auto;
    height: calc(100vh - 48px);
    border-left: 1px solid #ddd;
  }
}

/* alternative layout for wide screens */
@media screen and (min-width: 1024px) {
  body {
    max-width: 724px;
    margin: 42px auto;
    padding-left: 1.5em;
    padding-right: 29em;
  }
  #toc {
    position: fixed;
    top: 42px;
    right: 42px;
    width: 25%;
    margin: 0;
    padding: 0 1em;
    z-index: 1;
  }
  #toc h2 {
    border-top: none;
    border-bottom: 1px solid #ddd;
    font-size: 1em;
    font-weight: normal;
    margin: 0;
    padding: 0.25em 1em 1em 0;
  }
  #toc nav {
    display: block;
    height: calc(90vh - 84px);
    bottom: 0;
    padding: 0.5em 0 0;
    overflow: auto;
  }
  img { /* future proofing */
    max-width: 100%;
    height: auto;
  }
}

/* pagination */
@media print {
  body {

    width: 100%;
  }
  p {
    orphans: 3;
    widows: 3;
  }
  #n-copyright-notice {
    border-bottom: none;
  }
  #toc, #n-introduction {
    page-break-before: always;
  }
  #toc {
    border-top: none;
    padding-top: 0;
  }
  figure, pre {
    page-break-inside: avoid;
  }
  figure {
    overflow: scroll;
  }
  h1, h2, h3, h4, h5, h6 {
    page-break-after: avoid;
  }
  h2+*, h3+*, h4+*, h5+*, h6+* {
    page-break-before: avoid;
  }
  pre {
    white-space: pre-wrap;
    word-wrap: break-word;
    font-size: 10pt;
  }
  table {
    border: 1px solid #ddd;
  }
  td {
    border-top: 1px solid #ddd;
  }
}

/* This is commented out here, as the string-set: doesn't
   pass W3C validation currently */
/*
.ears thead .left {
  string-set: ears-top-left content();
}

.ears thead .center {
  string-set: ears-top-center content();
}

.ears thead .right {
  string-set: ears-top-right content();
}

.ears tfoot .left {
  string-set: ears-bottom-left content();
}

.ears tfoot .center {
  string-set: ears-bottom-center content();
}

.ears tfoot .right {
  string-set: ears-bottom-right content();
}
*/

@page :first {
  padding-top: 0;
  @top-left {
    content: normal;
    border: none;
  }
  @top-center {
    content: normal;
    border: none;
  }
  @top-right {
    content: normal;
    border: none;
  }
}

@page {
  size: A4;
  margin-bottom: 45mm;
  padding-top: 20px;
  /* The follwing is commented out here, but set appropriately by in code, as
     the content depends on the document */
  /*
  @top-left {
    content: 'Internet-Draft';
    vertical-align: bottom;
    border-bottom: solid 1px #ccc;
  }
  @top-left {
    content: string(ears-top-left);
    vertical-align: bottom;
    border-bottom: solid 1px #ccc;
  }
  @top-center {
    content: string(ears-top-center);
    vertical-align: bottom;
    border-bottom: solid 1px #ccc;
  }
  @top-right {
    content: string(ears-top-right);
    vertical-align: bottom;
    border-bottom: solid 1px #ccc;
  }
  @bottom-left {
    content: string(ears-bottom-left);
    vertical-align: top;
    border-top: solid 1px #ccc;
  }
  @bottom-center {
    content: string(ears-bottom-center);
    vertical-align: top;
    border-top: solid 1px #ccc;
  }
  @bottom-right {
      content: '[Page ' counter(page) ']';
      vertical-align: top;
      border-top: solid 1px #ccc;
  }
  */

}

/* Changes introduced to fix issues found during implementation */
/* Make sure links are clickable even if overlapped by following H* */
a {
  z-index: 2;
}
/* Separate body from document info even without intervening H1 */
section {
  clear: both;
}


/* Top align author divs, to avoid names without organization dropping level with org names */
.author {
  vertical-align: top;
}

/* Leave room in document info to show Internet-Draft on one line */
#identifiers dt {
  width: 8em;
}

/* Don't waste quite as much whitespace between label and value in doc info */
#identifiers dd {
  margin-left: 1em;
}

/* Give floating toc a background color (needed when it's a div inside section */
#toc {
  background-color: white;
}

/* Make the collapsed ToC header render white on gray also when it's a link */
@media screen and (max-width: 1023px) {
  #toc h2 a,
  #toc h2 a:link,
  #toc h2 a:focus,
  #toc h2 a:hover,
  #toc a.toplink,
  #toc a.toplink:hover {
    color: white;
    background-color: #444;
    text-decoration: none;
  }
}

/* Give the bottom of the ToC some whitespace */
@media screen and (min-width: 1024px) {
  #toc {
    padding: 0 0 1em 1em;
  }
}

/* Style section numbers with more space between number and title */
.section-number {
  padding-right: 0.5em;
}

/* prevent monospace from becoming overly large */
tt, code, pre, code {
  font-size: 95%;
}

/* Fix the height/width aspect for ascii art*/
pre.sourcecode,
.art-text pre {
  line-height: 1.12;
}


/* Add styling for a link in the ToC that points to the top of the document */
a.toplink {
  float: right;
  margin-right: 0.5em;
}

/* Fix the dl styling to match the RFC 7992 attributes */
dl > dt,
dl.dlParallel > dt {
  float: left;
  margin-right: 1em;
}
dl.dlNewline > dt {
  float: none;
}

/* Provide styling for table cell text alignment */
table td.text-left,
table th.text-left {
  text-align: left;
}
table td.text-center,
table th.text-center {
  text-align: center;
}
table td.text-right,
table th.text-right {
  text-align: right;
}

/* Make the alternative author contact informatio look less like just another
   author, and group it closer with the primary author contact information */
.alternative-contact {
  margin: 0.5em 0 0.25em 0;
}
address .non-ascii {
  margin: 0 0 0 2em;
}

/* With it being possible to set tables with alignment
  left, center, and right, { width: 100%; } does not make sense */
table {
  width: auto;
}

/* Avoid reference text that sits in a block with very wide left margin,
   because of a long floating dt label.*/
.references dd {
  overflow: visible;
}

/* Control caption placement */
caption {
  caption-side: bottom;
}

/* Limit the width of the author address vcard, so names in right-to-left
   script don't end up on the other side of the page. */

address.vcard {
  max-width: 30em;
  margin-right: auto;
}

/* For address alignment dependent on LTR or RTL scripts */
address div.left {
  text-align: left;
}
address div.right {
  text-align: right;
}

/* Provide table alignment support.  We can't use the alignX classes above
   since they do unwanted things with caption and other styling. */
table.right {
 margin-left: auto;
 margin-right: 0;
}
table.center {
 margin-left: auto;
 margin-right: auto;
}
table.left {
 margin-left: 0;
 margin-right: auto;
}

/* Give the table caption label the same styling as the figcaption */
caption a[href] {
  color: #222;
}

@media print {
  .toplink {
    display: none;
  }

  /* avoid overwriting the top border line with the ToC header */
  #toc {
    padding-top: 1px;
  }

  /* Avoid page breaks inside dl and author address entries */
  .vcard {
    page-break-inside: avoid;
  }

}
/* Tweak the bcp14 keyword presentation */
.bcp14 {
  font-variant: small-caps;
  font-weight: bold;
  font-size: 0.9em;
}
/* Tweak the invisible space above H* in order not to overlay links in text above */
 h2 {
  margin-top: -18px;  /* provide offset for in-page anchors */
  padding-top: 31px;
 }
 h3 {
  margin-top: -18px;  /* provide offset for in-page anchors */
  padding-top: 24px;
 }
 h4 {
  margin-top: -18px;  /* provide offset for in-page anchors */
  padding-top: 24px;
 }
/* Float artwork pilcrow to the right */
@media screen {
  .artwork a.pilcrow {
    display: block;
    line-height: 0.7;
    margin-top: 0.15em;
  }
}
/* Make pilcrows on dd visible */
@media screen {
  dd:hover > a.pilcrow {
    visibility: visible;
  }
}
/* Make the placement of figcaption match that of a table's caption
   by removing the figure's added bottom margin */
.alignLeft.art-text,
.alignCenter.art-text,
.alignRight.art-text {
   margin-bottom: 0;
}
.alignLeft,
.alignCenter,
.alignRight {
  margin: 1em 0 0 0;
}
/* In print, the pilcrow won't show on hover, so prevent it from taking up space,
   possibly even requiring a new line */
@media print {
  a.pilcrow {
    display: none;
  }
}
/* Styling for the external metadata */
div#external-metadata {
  background-color: #eee;
  padding: 0.5em;
  margin-bottom: 0.5em;
  display: none;
}
div#internal-metadata {
  padding: 0.5em;                       /* to match the external-metadata padding */
}
/* Styling for title RFC Number */
h1#rfcnum {
  clear: both;
  margin: 0 0 -1em;
  padding: 1em 0 0 0;
}
/* Make .olPercent look the same as <ol><li> */
dl.olPercent > dd {
  margin-bottom: 0.25em;
  min-height: initial;
}
/* Give aside some styling to set it apart */
aside {
  border-left: 1px solid #ddd;
  margin: 1em 0 1em 2em;
  padding: 0.2em 2em;
}
aside > dl,
aside > ol,
aside > ul,
aside > table,
aside > p {
  margin-bottom: 0.5em;
}
/* Additional page break settings */
@media print {
  figcaption, table caption {
    page-break-before: avoid;
  }
}
/* Font size adjustments for print */
@media print {
  body  { font-size: 10pt;      line-height: normal; max-width: 96%; }
  h1    { font-size: 1.72em;    padding-top: 1.5em; } /* 1*1.2*1.2*1.2 */
  h2    { font-size: 1.44em;    padding-top: 1.5em; } /* 1*1.2*1.2 */
  h3    { font-size: 1.2em;     padding-top: 1.5em; } /* 1*1.2 */
  h4    { font-size: 1em;       padding-top: 1.5em; }
  h5, h6 { font-size: 1em;      margin: initial; padding: 0.5em 0 0.3em; }
}
/* Sourcecode margin in print, when there's no pilcrow */
@media print {
  .artwork,
  .sourcecode {
    margin-bottom: 1em;
  }
}
/* Avoid narrow tables forcing too narrow table captions, which may render badly */
table {
  min-width: 20em;
}
/* ol type a */
ol.type-a { list-style-type: lower-alpha; }
ol.type-A { list-style-type: upper-alpha; }
ol.type-i { list-style-type: lower-roman; }
ol.type-I { list-style-type: lower-roman; }
/* Apply the print table and row borders in general, on request from the RPC,
and increase the contrast between border and odd row background sligthtly */
table {
  border: 1px solid #ddd;
}
td {
  border-top: 1px solid #ddd;
}
tr:nth-child(2n+1) > td {
  background-color: #f8f8f8;
}
/* Use style rules to govern display of the TOC. */
@media screen and (max-width: 1023px) {
  #toc nav { display: none; }
  #toc.active nav { display: block; }
}
/* Add support for keepWithNext */
.keepWithNext {
  break-after: avoid-page;
  break-after: avoid-page;
}
/* Add support for keepWithPrevious */
.keepWithPrevious {
  break-before: avoid-page;
}
/* Change the approach to avoiding breaks inside artwork etc. */
figure, pre, table, .artwork, .sourcecode  {
  break-before: avoid-page;
  break-after: auto;
}
/* Avoid breaks between <dt> and <dd> */
dl {
  break-before: auto;
  break-inside: auto;
}
dt {
  break-before: auto;
  break-after: avoid-page;
}
dd {
  break-before: avoid-page;
  break-after: auto;
  orphans: 3;
  widows: 3
}
span.break, dd.break {
  margin-bottom: 0;
  min-height: 0;
  break-before: auto;
  break-inside: auto;
  break-after: auto;
}
/* Undo break-before ToC */
@media print {
  #toc {
    break-before: auto;
  }
}
/* Text in compact lists should not get extra bottim margin space,
   since that would makes the list not compact */
ul.compact p, .ulCompact p,
ol.compact p, .olCompact p {
 margin: 0;
}
/* But the list as a whole needs the extra space at the end */
section ul.compact,
section .ulCompact,
section ol.compact,
section .olCompact {
  margin-bottom: 1em;                    /* same as p not within ul.compact etc. */
}
/* The tt and code background above interferes with for instance table cell
   backgrounds.  Changed to something a bit more selective. */
tt, code {
  background-color: transparent;
}
p tt, p code, li tt, li code {
  background-color: #f8f8f8;
}
/* Tweak the pre margin -- 0px doesn't come out well */
pre {
   margin-top: 0.5px;
}
/* Tweak the comact list text */
ul.compact, .ulCompact,
ol.compact, .olCompact,
dl.compact, .dlCompact {
  line-height: normal;
}
/* Don't add top margin for nested lists */
li > ul, li > ol, li > dl,
dd > ul, dd > ol, dd > dl,
dl > dd > dl {
  margin-top: initial;
}
/* Elements that should not be rendered on the same line as a <dt> */
/* This should match the element list in writer.text.TextWriter.render_dl() */
dd > div.artwork:first-child,
dd > aside:first-child,
dd > figure:first-child,
dd > ol:first-child,
dd > div:first-child > pre.sourcecode,
dd > table:first-child,
dd > ul:first-child {
  clear: left;
}
/* fix for weird browser behaviour when <dd/> is empty */
dt+dd:empty::before{
  content: "\00a0";
}
/* Make paragraph spacing inside <li> smaller than in body text, to fit better within the list */
li > p {
  margin-bottom: 0.5em
}
/* Don't let p margin spill out from inside list items */
li > p:last-of-type {
  margin-bottom: 0;
}
</style>
<link href="rfc-local.css" rel="stylesheet" type="text/css">
<link href="https://dx.doi.org/10.17487/rfc9074" rel="alternate">
  <link href="urn:issn:2070-1721" rel="alternate">
  <link href="https://datatracker.ietf.org/doc/draft-ietf-calext-valarm-extensions-07" rel="prev">
  </head>
<body>
<script src="https://www.rfc-editor.org/js/metadata.min.js"></script>
<table class="ears">
<thead><tr>
<td class="left">RFC 9074</td>
<td class="center">VALARM Extensions</td>
<td class="right">August 2021</td>
</tr></thead>
<tfoot><tr>
<td class="left">Daboo &amp; Murchison</td>
<td class="center">Standards Track</td>
<td class="right">[Page]</td>
</tr></tfoot>
</table>
<div id="external-metadata" class="document-information"></div>
<div id="internal-metadata" class="document-information">
<dl id="identifiers">
<dt class="label-stream">Stream:</dt>
<dd class="stream">Internet Engineering Task Force (IETF)</dd>
<dt class="label-rfc">RFC:</dt>
<dd class="rfc"><a href="https://www.rfc-editor.org/rfc/rfc9074" class="eref">9074</a></dd>
<dt class="label-updates">Updates:</dt>
<dd class="updates">
<a href="https://www.rfc-editor.org/rfc/rfc5545" class="eref">5545</a> </dd>
<dt class="label-category">Category:</dt>
<dd class="category">Standards Track</dd>
<dt class="label-published">Published:</dt>
<dd class="published">
<time datetime="2021-08" class="published">August 2021</time>
    </dd>
<dt class="label-issn">ISSN:</dt>
<dd class="issn">2070-1721</dd>
<dt class="label-authors">Authors:</dt>
<dd class="authors">
<div class="author">
      <div class="author-name">C. Daboo</div>
<div class="org">Apple</div>
</div>
<div class="author">
      <div class="author-name">K. Murchison, <span class="editor">Ed.</span>
</div>
<div class="org">Fastmail</div>
</div>
</dd>
</dl>
</div>
<h1 id="rfcnum">RFC 9074</h1>
<h1 id="title">"VALARM" Extensions for iCalendar</h1>
<section id="section-abstract">
      <h2 id="abstract"><a href="#abstract" class="selfRef">Abstract</a></h2>
<p id="section-abstract-1">This document defines a set of extensions to the iCalendar
      "VALARM" component to enhance the use of alarms and improve
      interoperability between clients and servers.<a href="#section-abstract-1" class="pilcrow">¶</a></p>
<p id="section-abstract-2">This document updates RFC 5545.<a href="#section-abstract-2" class="pilcrow">¶</a></p>
</section>
<div id="status-of-memo">
<section id="section-boilerplate.1">
        <h2 id="name-status-of-this-memo">
<a href="#name-status-of-this-memo" class="section-name selfRef">Status of This Memo</a>
        </h2>
<p id="section-boilerplate.1-1">
            This is an Internet Standards Track document.<a href="#section-boilerplate.1-1" class="pilcrow">¶</a></p>
<p id="section-boilerplate.1-2">
            This document is a product of the Internet Engineering Task Force
            (IETF).  It represents the consensus of the IETF community.  It has
            received public review and has been approved for publication by
            the Internet Engineering Steering Group (IESG).  Further
            information on Internet Standards is available in Section 2 of 
            RFC 7841.<a href="#section-boilerplate.1-2" class="pilcrow">¶</a></p>
<p id="section-boilerplate.1-3">
            Information about the current status of this document, any
            errata, and how to provide feedback on it may be obtained at
            <span><a href="https://www.rfc-editor.org/info/rfc9074">https://www.rfc-editor.org/info/rfc9074</a></span>.<a href="#section-boilerplate.1-3" class="pilcrow">¶</a></p>
</section>
</div>
<div id="copyright">
<section id="section-boilerplate.2">
        <h2 id="name-copyright-notice">
<a href="#name-copyright-notice" class="section-name selfRef">Copyright Notice</a>
        </h2>
<p id="section-boilerplate.2-1">
            Copyright (c) 2021 IETF Trust and the persons identified as the
            document authors. All rights reserved.<a href="#section-boilerplate.2-1" class="pilcrow">¶</a></p>
<p id="section-boilerplate.2-2">
            This document is subject to BCP 78 and the IETF Trust's Legal
            Provisions Relating to IETF Documents
            (<span><a href="https://trustee.ietf.org/license-info">https://trustee.ietf.org/license-info</a></span>) in effect on the date of
            publication of this document. Please review these documents
            carefully, as they describe your rights and restrictions with
            respect to this document. Code Components extracted from this
            document must include Simplified BSD License text as described in
            Section 4.e of the Trust Legal Provisions and are provided without
            warranty as described in the Simplified BSD License.<a href="#section-boilerplate.2-2" class="pilcrow">¶</a></p>
</section>
</div>
<div id="toc">
<section id="section-toc.1">
        <a href="#" onclick="scroll(0,0)" class="toplink">▲</a><h2 id="name-table-of-contents">
<a href="#name-table-of-contents" class="section-name selfRef">Table of Contents</a>
        </h2>
<nav class="toc"><ul class="compact toc ulEmpty ulBare">
<li class="compact toc ulEmpty ulBare" id="section-toc.1-1.1">
            <p id="section-toc.1-1.1.1" class="keepWithNext"><a href="#section-1" class="xref">1</a>.  <a href="#name-introduction" class="xref">Introduction</a></p>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.2">
            <p id="section-toc.1-1.2.1" class="keepWithNext"><a href="#section-2" class="xref">2</a>.  <a href="#name-conventions-used-in-this-do" class="xref">Conventions Used in This Document</a></p>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.3">
            <p id="section-toc.1-1.3.1" class="keepWithNext"><a href="#section-3" class="xref">3</a>.  <a href="#name-extensible-syntax-for-valar" class="xref">Extensible Syntax for VALARM</a></p>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.4">
            <p id="section-toc.1-1.4.1"><a href="#section-4" class="xref">4</a>.  <a href="#name-alarm-unique-identifier" class="xref">Alarm Unique Identifier</a></p>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.5">
            <p id="section-toc.1-1.5.1"><a href="#section-5" class="xref">5</a>.  <a href="#name-alarm-related-to" class="xref">Alarm Related To</a></p>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.6">
            <p id="section-toc.1-1.6.1"><a href="#section-6" class="xref">6</a>.  <a href="#name-alarm-acknowledgement" class="xref">Alarm Acknowledgement</a></p>
<ul class="ulEmpty toc compact ulBare">
<li class="ulEmpty toc compact ulBare" id="section-toc.1-1.6.2.1">
                <p id="section-toc.1-1.6.2.1.1"><a href="#section-6.1" class="xref">6.1</a>.  <a href="#name-acknowledged-property" class="xref">Acknowledged Property</a></p>
</li>
            </ul>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.7">
            <p id="section-toc.1-1.7.1"><a href="#section-7" class="xref">7</a>.  <a href="#name-snoozing-alarms" class="xref">Snoozing Alarms</a></p>
<ul class="ulEmpty toc compact ulBare">
<li class="ulEmpty toc compact ulBare" id="section-toc.1-1.7.2.1">
                <p id="section-toc.1-1.7.2.1.1"><a href="#section-7.1" class="xref">7.1</a>.  <a href="#name-relationship-type-property-" class="xref">Relationship Type Property Parameter</a></p>
</li>
              <li class="ulEmpty toc compact ulBare" id="section-toc.1-1.7.2.2">
                <p id="section-toc.1-1.7.2.2.1"><a href="#section-7.2" class="xref">7.2</a>.  <a href="#name-example" class="xref">Example</a></p>
</li>
            </ul>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.8">
            <p id="section-toc.1-1.8.1"><a href="#section-8" class="xref">8</a>.  <a href="#name-alarm-proximity-trigger" class="xref">Alarm Proximity Trigger</a></p>
<ul class="ulEmpty toc compact ulBare">
<li class="ulEmpty toc compact ulBare" id="section-toc.1-1.8.2.1">
                <p id="section-toc.1-1.8.2.1.1"><a href="#section-8.1" class="xref">8.1</a>.  <a href="#name-proximity-property" class="xref">Proximity Property</a></p>
</li>
              <li class="ulEmpty toc compact ulBare" id="section-toc.1-1.8.2.2">
                <p id="section-toc.1-1.8.2.2.1"><a href="#section-8.2" class="xref">8.2</a>.  <a href="#name-example-2" class="xref">Example</a></p>
</li>
            </ul>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.9">
            <p id="section-toc.1-1.9.1"><a href="#section-9" class="xref">9</a>.  <a href="#name-security-considerations" class="xref">Security Considerations</a></p>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.10">
            <p id="section-toc.1-1.10.1"><a href="#section-10" class="xref">10</a>. <a href="#name-privacy-considerations" class="xref">Privacy Considerations</a></p>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.11">
            <p id="section-toc.1-1.11.1"><a href="#section-11" class="xref">11</a>. <a href="#name-iana-considerations" class="xref">IANA Considerations</a></p>
<ul class="ulEmpty toc compact ulBare">
<li class="ulEmpty toc compact ulBare" id="section-toc.1-1.11.2.1">
                <p id="section-toc.1-1.11.2.1.1"><a href="#section-11.1" class="xref">11.1</a>.  <a href="#name-property-registrations" class="xref">Property Registrations</a></p>
</li>
              <li class="ulEmpty toc compact ulBare" id="section-toc.1-1.11.2.2">
                <p id="section-toc.1-1.11.2.2.1"><a href="#section-11.2" class="xref">11.2</a>.  <a href="#name-relationship-types-registry" class="xref">Relationship Types Registry</a></p>
</li>
              <li class="ulEmpty toc compact ulBare" id="section-toc.1-1.11.2.3">
                <p id="section-toc.1-1.11.2.3.1"><a href="#section-11.3" class="xref">11.3</a>.  <a href="#name-proximity-values-registry" class="xref">Proximity Values Registry</a></p>
</li>
            </ul>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.12">
            <p id="section-toc.1-1.12.1"><a href="#section-12" class="xref">12</a>. <a href="#name-references" class="xref">References</a></p>
<ul class="ulEmpty toc compact ulBare">
<li class="ulEmpty toc compact ulBare" id="section-toc.1-1.12.2.1">
                <p id="section-toc.1-1.12.2.1.1"><a href="#section-12.1" class="xref">12.1</a>.  <a href="#name-normative-references" class="xref">Normative References</a></p>
</li>
              <li class="ulEmpty toc compact ulBare" id="section-toc.1-1.12.2.2">
                <p id="section-toc.1-1.12.2.2.1"><a href="#section-12.2" class="xref">12.2</a>.  <a href="#name-informative-references" class="xref">Informative References</a></p>
</li>
            </ul>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.13">
            <p id="section-toc.1-1.13.1"><a href="#appendix-A" class="xref"></a><a href="#name-acknowledgements" class="xref">Acknowledgements</a></p>
</li>
          <li class="compact toc ulEmpty ulBare" id="section-toc.1-1.14">
            <p id="section-toc.1-1.14.1"><a href="#appendix-B" class="xref"></a><a href="#name-authors-addresses" class="xref">Authors' Addresses</a></p>
</li>
        </ul>
</nav>
</section>
</div>
<section id="section-1">
      <h2 id="name-introduction">
<a href="#section-1" class="section-number selfRef">1. </a><a href="#name-introduction" class="section-name selfRef">Introduction</a>
      </h2>
<p id="section-1-1">The <span><a href="#RFC5545" class="xref">iCalendar specification</a> [<a href="#RFC5545" class="xref">RFC5545</a>]</span>
      defines a set of components used to describe calendar data. One
      of those is the "VALARM" component, which appears as a
      subcomponent of the "VEVENT" and "VTODO" components. The "VALARM"
      component is used to specify a reminder for an event or
      task. Different alarm actions are possible, as are different
      ways to specify how the alarm is triggered.<a href="#section-1-1" class="pilcrow">¶</a></p>
<p id="section-1-2">As iCalendar has become more widely used and as client-server
      protocols, such as <span><a href="#RFC4791" class="xref">Calendaring Extensions to WebDAV
      (CalDAV)</a> [<a href="#RFC4791" class="xref">RFC4791</a>]</span>, have
      become more prevalent, several issues with "VALARM" components
      have arisen. Most of these relate to the need to extend the
      existing "VALARM" component with new properties and behaviors to
      allow clients and servers to accomplish specific tasks in an
      interoperable manner. For example, clients typically need a way
      to specify that an alarm has been dismissed by a calendar user
      or has been "snoozed" by a set amount of time. To date, this has
      been done through the use of custom "X-" properties specific to
      each client implementation, leading to poor
      interoperability.<a href="#section-1-2" class="pilcrow">¶</a></p>
<p id="section-1-3">This specification defines a set of extensions to "VALARM"
      components to cover common requirements for alarms not currently
      addressed in iCalendar. Each extension is defined in a separate
      section below. For the most part, each extension can be
      supported independently of the others; though, in some cases, one
      extension will require another. In addition, this specification
      describes mechanisms by which clients can interoperably
      implement common features, such as "snoozing".<a href="#section-1-3" class="pilcrow">¶</a></p>
</section>
<section id="section-2">
      <h2 id="name-conventions-used-in-this-do">
<a href="#section-2" class="section-number selfRef">2. </a><a href="#name-conventions-used-in-this-do" class="section-name selfRef">Conventions Used in This Document</a>
      </h2>
<p id="section-2-1">
    The key words "<span class="bcp14">MUST</span>", "<span class="bcp14">MUST NOT</span>", "<span class="bcp14">REQUIRED</span>", "<span class="bcp14">SHALL</span>", "<span class="bcp14">SHALL NOT</span>", "<span class="bcp14">SHOULD</span>", "<span class="bcp14">SHOULD NOT</span>", "<span class="bcp14">RECOMMENDED</span>", "<span class="bcp14">NOT RECOMMENDED</span>",
    "<span class="bcp14">MAY</span>", and "<span class="bcp14">OPTIONAL</span>" in this document are to be interpreted as
    described in BCP 14 <span>[<a href="#RFC2119" class="xref">RFC2119</a>]</span> <span>[<a href="#RFC8174" class="xref">RFC8174</a>]</span> 
    when, and only when, they appear in all capitals, as shown here.<a href="#section-2-1" class="pilcrow">¶</a></p>
<p id="section-2-2">The notation used in this memo to (re-)define iCalendar elements is the ABNF notation of <span>[<a href="#RFC5234" class="xref">RFC5234</a>]</span> as used by <span>[<a href="#RFC5545" class="xref">RFC5545</a>]</span>.
   Any syntax elements shown below that are not explicitly defined in this specification come from iCalendar <span>[<a href="#RFC5545" class="xref">RFC5545</a>]</span>.<a href="#section-2-2" class="pilcrow">¶</a></p>
<p id="section-2-3">When XML element types in the namespaces "DAV:" and
      "urn:ietf:params:xml:ns:caldav" are referenced in this document
      outside of the context of an XML fragment, the string "DAV:" and
      "CALDAV:" will be prefixed to the element type names,
      respectively.<a href="#section-2-3" class="pilcrow">¶</a></p>
</section>
<div id="syntax">
<section id="section-3">
      <h2 id="name-extensible-syntax-for-valar">
<a href="#section-3" class="section-number selfRef">3. </a><a href="#name-extensible-syntax-for-valar" class="section-name selfRef">Extensible Syntax for VALARM</a>
      </h2>
<p id="section-3-1" class="keepWithNext"><span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-3.6.6" class="relref">Section 3.6.6</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span> defines the syntax
      for "VALARM" components and properties within them. However, as
      written, it is hard to extend this, e.g., by adding a new
      property common to all types of alarms. Since many of the
      extensions defined in this document need to extend the base
      syntax, an alternative form for the base syntax is defined here,
      with the goal of simplifying specification of the extensions
      while augmenting the existing functionality defined in
      <span>[<a href="#RFC5545" class="xref">RFC5545</a>]</span> to allow for nested subcomponents
      (as required by
      <span><a href="#proximity" class="xref">proximity alarm triggers</a> (<a href="#proximity" class="xref">Section 8</a>)</span>).<a href="#section-3-1" class="pilcrow">¶</a></p>
<p id="section-3-2">A "VALARM" calendar component is redefined by the following notation:<a href="#section-3-2" class="pilcrow">¶</a></p>
<div id="section-3-3">
<pre class="sourcecode lang-abnf">
alarmcext  = "BEGIN" ":" "VALARM" CRLF
             *alarmprop *alarm-subcomp
             "END" ":" "VALARM" CRLF

alarmprop  = (
             ;
             ; the following are REQUIRED
             ; but MUST NOT occur more than once
             ;
             action / trigger /
             ;
             ; one set of action properties MUST be
             ; present and MUST match the action specified
             ; in the ACTION property
             ;
             actionprops /
             ;
             ; the following are OPTIONAL
             ; and MAY occur more than once
             ;
             x-prop / iana-prop
             ;
             )

actionprops = *audiopropext / *disppropext / *emailpropext

audiopropext  = (
                ;
                ; 'duration' and 'repeat' are both OPTIONAL
                ; and MUST NOT occur more than once each,
                ; but if one occurs, so MUST the other
                ;
                duration / repeat /
                ;
                ; the following is OPTIONAL
                ; but MUST NOT occur more than once
                ;
                attach
                ;
                )

disppropext = (
              ;
              ; the following are REQUIRED
              ; but MUST NOT occur more than once
              ;
              description /
              ;
              ; 'duration' and 'repeat' are both OPTIONAL
              ; and MUST NOT occur more than once each,
              ; but if one occurs, so MUST the other
              ;
              duration / repeat
              ;
              )

emailpropext = (
               ;
               ; the following are all REQUIRED
               ; but MUST NOT occur more than once
               ;
               description / summary /
               ;
               ; the following is REQUIRED
               ; and MAY occur more than once
               ;
               attendee /
               ;
               ; 'duration' and 'repeat' are both OPTIONAL
               ; and MUST NOT occur more than once each,
               ; but if one occurs, so MUST the other
               ;
               duration / repeat
               ;
               ; the following is OPTIONAL
               ; and MAY occur more than once
               ;
               attach
               ;
               )

alarm-subcomp = (
                ;
                ; the following are OPTIONAL
                ; and MAY occur more than once
                ;
                x-comp / iana-comp
                ;
                )
</pre><a href="#section-3-3" class="pilcrow">¶</a>
</div>
</section>
</div>
<div id="uid">
<section id="section-4">
      <h2 id="name-alarm-unique-identifier">
<a href="#section-4" class="section-number selfRef">4. </a><a href="#name-alarm-unique-identifier" class="section-name selfRef">Alarm Unique Identifier</a>
      </h2>
<p id="section-4-1">This extension adds a "UID"
      property to "VALARM" components to allow a unique identifier to
      be specified. The value of this property can then be used to refer
      uniquely to the "VALARM" component.<a href="#section-4-1" class="pilcrow">¶</a></p>
<p id="section-4-2">The "UID" property defined here follows the definition in
      <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-3.8.4.7" class="relref">Section 3.8.4.7</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span> with the security
      and privacy updates in <span><a href="https://www.rfc-editor.org/rfc/rfc7986#section-5.3" class="relref">Section 5.3</a> of [<a href="#RFC7986" class="xref">RFC7986</a>]</span>.
      In particular, it <span class="bcp14">MUST</span> be a globally unique identifier that does
      not contain any security- or privacy-sensitive information.<a href="#section-4-2" class="pilcrow">¶</a></p>
<p id="section-4-3">The "VALARM" component defined in <a href="#syntax" class="xref">Section 3</a> is
      extended here as:<a href="#section-4-3" class="pilcrow">¶</a></p>
<div id="section-4-4">
<pre class="sourcecode lang-abnf">
alarmprop  =/ (
              ;
              ; the following is OPTIONAL
              ; but MUST NOT occur more than once
              ;
              uid
              ;
              )
</pre><a href="#section-4-4" class="pilcrow">¶</a>
</div>
</section>
</div>
<div id="RELATED">
<section id="section-5">
      <h2 id="name-alarm-related-to">
<a href="#section-5" class="section-number selfRef">5. </a><a href="#name-alarm-related-to" class="section-name selfRef">Alarm Related To</a>
      </h2>
<p id="section-5-1">It is often convenient to relate one or more "VALARM"
      components to other "VALARM" components (e.g., see <a href="#snooze" class="xref">Section 7</a>). This can be accomplished if the "VALARM"
      components each have their own "UID" property (as per <a href="#uid" class="xref">Section 4</a>).<a href="#section-5-1" class="pilcrow">¶</a></p>
<p id="section-5-2">This specification updates the usage of the "RELATED-TO"
      property defined in <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-3.8.4.5" class="relref">Section 3.8.4.5</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span>
      to enable its use with "VALARM" components. Specific types of
      relationships between "VALARM" components can be identified by
      registering new values for the "RELTYPE" property parameter
      defined in <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-3.2.15" class="relref">Section 3.2.15</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span>.<a href="#section-5-2" class="pilcrow">¶</a></p>
<p id="section-5-3">The "VALARM" component defined in <a href="#syntax" class="xref">Section 3</a> is
      extended here as:<a href="#section-5-3" class="pilcrow">¶</a></p>
<div id="section-5-4">
<pre class="sourcecode lang-abnf">
alarmprop  =/ (
              ;
              ; the following is OPTIONAL
              ; and MAY occur more than once
              ;
              related
              ;
              )
</pre><a href="#section-5-4" class="pilcrow">¶</a>
</div>
</section>
</div>
<section id="section-6">
      <h2 id="name-alarm-acknowledgement">
<a href="#section-6" class="section-number selfRef">6. </a><a href="#name-alarm-acknowledgement" class="section-name selfRef">Alarm Acknowledgement</a>
      </h2>
<p id="section-6-1">There is currently no way for a "VALARM" component to
      indicate whether it has been triggered and acknowledged. With
      the advent of a standard client/server protocol for calendaring
      and scheduling data (<span>[<a href="#RFC4791" class="xref">RFC4791</a>]</span>), it is quite
      possible for an event with an alarm to exist on multiple clients
      in addition to the server. If each of those is responsible for
      performing the action when an alarm triggers, then multiple
      "alerts" are generated by different devices. In such a
      situation, a calendar user would like to be able to "dismiss"
      the alarm on one device and have it automatically dismissed on
      the others, too.<a href="#section-6-1" class="pilcrow">¶</a></p>
<p id="section-6-2">Also, with recurring events that have alarms, it is important
      to know when the last alarm in the recurring set was
      acknowledged so that the client can determine whether past
      alarms have been missed.<a href="#section-6-2" class="pilcrow">¶</a></p>
<p id="section-6-3">To address these needs, this specification adds an
      "ACKNOWLEDGED" property to "VALARM" components to indicate when
      the alarm was last acknowledged (or sent, if acknowledgement is
      not possible).
      This is defined by the
      syntax below.<a href="#section-6-3" class="pilcrow">¶</a></p>
<div id="section-6-4">
<pre class="sourcecode lang-abnf">
alarmprop       =/ (
                   ;
                   ; the following is OPTIONAL
                   ; but MUST NOT occur more than once
                   ;
                   acknowledged
                   ;
                   )
</pre><a href="#section-6-4" class="pilcrow">¶</a>
</div>
<div id="ACKNOWLEDGED">
<section id="section-6.1">
        <h3 id="name-acknowledged-property">
<a href="#section-6.1" class="section-number selfRef">6.1. </a><a href="#name-acknowledged-property" class="section-name selfRef">Acknowledged Property</a>
        </h3>
<span class="break"></span><dl class="dlParallel" id="section-6.1-1">
          <dt id="section-6.1-1.1">Property Name:</dt>
          <dd style="margin-left: 1.5em" id="section-6.1-1.2">ACKNOWLEDGED<a href="#section-6.1-1.2" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-6.1-1.3">Purpose:</dt>
          <dd style="margin-left: 1.5em" id="section-6.1-1.4">This property specifies the UTC
            date and time at which the corresponding alarm was last
            sent or acknowledged.<a href="#section-6.1-1.4" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-6.1-1.5">Value Type:</dt>
          <dd style="margin-left: 1.5em" id="section-6.1-1.6">DATE-TIME<a href="#section-6.1-1.6" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-6.1-1.7">Property Parameters:</dt>
          <dd style="margin-left: 1.5em" id="section-6.1-1.8">IANA and nonstandard
            property parameters can be specified on this property.<a href="#section-6.1-1.8" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-6.1-1.9">Conformance:</dt>
          <dd style="margin-left: 1.5em" id="section-6.1-1.10">This property can be specified
            within "VALARM" calendar components.<a href="#section-6.1-1.10" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-6.1-1.11">Description:</dt>
          <dd style="margin-left: 1.5em" id="section-6.1-1.12">
            <p id="section-6.1-1.12.1">This property is used to
            specify when an alarm was last sent or acknowledged. This
            allows clients to determine when a pending alarm has been
            acknowledged by a calendar user so that any alerts can be
            dismissed across multiple devices. It also allows clients
            to track repeating alarms or alarms on recurring events or
            to-dos to ensure that the right number of missed alarms
            can be tracked.<a href="#section-6.1-1.12.1" class="pilcrow">¶</a></p>
<p id="section-6.1-1.12.2">Clients <span class="bcp14">SHOULD</span> set this property to the current
            date-time value in UTC when a calendar user acknowledges a
            pending alarm.
            Certain kinds of alarms, such as email-based alerts, might
            not provide feedback as to when the calendar user sees them.
            For those kinds of alarms, the
            client <span class="bcp14">SHOULD</span> set this property when the alarm is
            triggered and the action is successfully carried out.<a href="#section-6.1-1.12.2" class="pilcrow">¶</a></p>
<p id="section-6.1-1.12.3">When an alarm is triggered on a
            client, clients can check to see if an "ACKNOWLEDGED"
            property is present. If it is, and the value of that
            property is greater than or equal to the computed trigger
            time for the alarm, then the client <span class="bcp14">SHOULD NOT</span> trigger the
            alarm. Similarly, if an alarm has been triggered and an
            "alert" has been presented to a calendar user, clients can monitor
            the iCalendar data to determine whether an "ACKNOWLEDGED" property
            is added or changed in the alarm component. If the value
            of any "ACKNOWLEDGED" property in the alarm changes and is greater
            than or equal to the trigger time of the alarm, then
            clients <span class="bcp14">SHOULD</span> dismiss or cancel any "alert" presented to
            the calendar user.<a href="#section-6.1-1.12.3" class="pilcrow">¶</a></p>
</dd>
          <dd class="break"></dd>
<dt id="section-6.1-1.13">Format Definition:</dt>
          <dd style="margin-left: 1.5em" id="section-6.1-1.14">
            <p id="section-6.1-1.14.1">This property is defined
            by the following notation:<a href="#section-6.1-1.14.1" class="pilcrow">¶</a></p>
<div id="section-6.1-1.14.2">
<pre class="sourcecode lang-abnf">
acknowledged = "ACKNOWLEDGED" *acknowledgedparam ":" datetime CRLF

acknowledgedparam  = (
                     ;
                     ; the following is OPTIONAL
                     ; and MAY occur more than once
                     ;
                     (";" other-param)
                     ;
                     )
</pre><a href="#section-6.1-1.14.2" class="pilcrow">¶</a>
</div>
</dd>
          <dd class="break"></dd>
<dt id="section-6.1-1.15">Example:</dt>
          <dd style="margin-left: 1.5em" id="section-6.1-1.16">
            <p id="section-6.1-1.16.1">The following is an example of this property:<a href="#section-6.1-1.16.1" class="pilcrow">¶</a></p>
<div id="section-6.1-1.16.2">
<pre class="sourcecode">
ACKNOWLEDGED:20090604T084500Z
</pre><a href="#section-6.1-1.16.2" class="pilcrow">¶</a>
</div>
</dd>
        <dd class="break"></dd>
</dl>
</section>
</div>
</section>
<div id="snooze">
<section id="section-7">
      <h2 id="name-snoozing-alarms">
<a href="#section-7" class="section-number selfRef">7. </a><a href="#name-snoozing-alarms" class="section-name selfRef">Snoozing Alarms</a>
      </h2>
<p id="section-7-1">Users often want to "snooze" an alarm, and this specification
      defines a standard approach to accomplish that.<a href="#section-7-1" class="pilcrow">¶</a></p>
<p id="section-7-2">To "snooze" an alarm that has been triggered, clients <span class="bcp14">MUST</span> do
      the following:<a href="#section-7-2" class="pilcrow">¶</a></p>
<ol start="1" type="1" class="normal type-1" id="section-7-3">
 <li id="section-7-3.1">
          <p id="section-7-3.1.1">Set the "ACKNOWLEDGED" property
        (see <a href="#ACKNOWLEDGED" class="xref">Section 6.1</a>) on the triggered alarm.<a href="#section-7-3.1.1" class="pilcrow">¶</a></p>
</li>
        <li id="section-7-3.2">
          <p id="section-7-3.2.1">Create a new "VALARM" component (the "snooze" alarm) within
        the parent component of the triggered alarm
        (i.e., as a "sibling" component of the triggered alarm).<a href="#section-7-3.2.1" class="pilcrow">¶</a></p>
<ol start="1" type="a" class="normal type-a" id="section-7-3.2.2">
     <li id="section-7-3.2.2.1">The new "snooze" alarm <span class="bcp14">MUST</span> be set to trigger
          at the user's chosen "snooze" interval after the original alarm is
          triggered. Clients <span class="bcp14">SHOULD</span> use an absolute "TRIGGER" property
          with a "DATE-TIME" value specified in UTC.<a href="#section-7-3.2.2.1" class="pilcrow">¶</a>
</li>
            <li id="section-7-3.2.2.2">The new "snooze" alarm <span class="bcp14">MUST</span> have a "RELATED-TO" property
          (see <a href="#RELATED" class="xref">Section 5</a>)
          with a value set to the "UID" property value of the original
          "VALARM" component that was triggered.
          If the triggered "VALARM" component does not
          already have a "UID" property, the client <span class="bcp14">MUST</span> add one. The
          "RELATED-TO" property added to the new "snooze" alarm <span class="bcp14">MUST</span>
          include a "RELTYPE" property parameter with a value set to
          "SNOOZE" (see <a href="#SNOOZE-PARAM" class="xref">Section 7.1</a>).<a href="#section-7-3.2.2.2" class="pilcrow">¶</a>
</li>
          </ol>
</li>
        <li id="section-7-3.3">
          <p id="section-7-3.3.1">When the "snooze" alarm is triggered, the client <span class="bcp14">MUST</span> do the
        following:<a href="#section-7-3.3.1" class="pilcrow">¶</a></p>
<ol start="1" type="a" class="normal type-a" id="section-7-3.3.2">
     <li id="section-7-3.3.2.1">Update the "ACKNOWLEDGED" property on the original related
          alarm.<a href="#section-7-3.3.2.1" class="pilcrow">¶</a>
</li>
            <li id="section-7-3.3.2.2">
              <p id="section-7-3.3.2.2.1">If the "snooze" alarm is itself "snoozed", the client <span class="bcp14">MUST</span>
          remove the "snooze" alarm component and return to step 2.<a href="#section-7-3.3.2.2.1" class="pilcrow">¶</a></p>
<p id="section-7-3.3.2.2.2">
          Otherwise, if the "snooze" alarm is dismissed, the client
          <span class="bcp14">MUST</span> do one of the following:<a href="#section-7-3.3.2.2.2" class="pilcrow">¶</a></p>
<ul class="normal">
<li class="normal" id="section-7-3.3.2.2.3.1">Set the "ACKNOWLEDGED" property on the "snooze" alarm.<a href="#section-7-3.3.2.2.3.1" class="pilcrow">¶</a>
</li>
                <li class="normal" id="section-7-3.3.2.2.3.2">Remove the "snooze" alarm component.<a href="#section-7-3.3.2.2.3.2" class="pilcrow">¶</a>
</li>
              </ul>
</li>
          </ol>
</li>
      </ol>
<p id="section-7-4">Note that regardless of the final disposition of the "snooze"
      alarm when triggered, the original "VALARM" component is left
      unchanged other than updating its "ACKNOWLEDGED" property.<a href="#section-7-4" class="pilcrow">¶</a></p>
<div id="SNOOZE-PARAM">
<section id="section-7.1">
        <h3 id="name-relationship-type-property-">
<a href="#section-7.1" class="section-number selfRef">7.1. </a><a href="#name-relationship-type-property-" class="section-name selfRef">Relationship Type Property Parameter</a>
        </h3>
<p id="section-7.1-1">
            This specification adds the "SNOOZE" relationship type for
            use with the "RELTYPE" property defined in
            <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-3.2.15" class="relref">Section 3.2.15</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span>. This is used when relating a
            "snoozed" "VALARM" component to the original alarm that
            the "snooze" was generated for.<a href="#section-7.1-1" class="pilcrow">¶</a></p>
</section>
</div>
<section id="section-7.2">
        <h3 id="name-example">
<a href="#section-7.2" class="section-number selfRef">7.2. </a><a href="#name-example" class="section-name selfRef">Example</a>
        </h3>
<p id="section-7.2-1">The following example shows the "snoozing", "re-snoozing", and
        dismissal of an alarm.  Note that the encompassing
        "VCALENDAR" component has been omitted for brevity and that the
        line breaks surrounding the "VALARM" components are for clarity
        only and would not be present in the actual iCalendar data.<a href="#section-7.2-1" class="pilcrow">¶</a></p>
<p id="section-7.2-2">Assume that we have the following event with an alarm set
        to trigger 15 minutes before the meeting:<a href="#section-7.2-2" class="pilcrow">¶</a></p>
<div id="section-7.2-3">
<pre class="sourcecode">
BEGIN:VEVENT
CREATED:20210302T151004Z
UID:AC67C078-CED3-4BF5-9726-832C3749F627
DTSTAMP:20210302T151004Z
DTSTART;TZID=America/New_York:20210302T103000
DTEND;TZID=America/New_York:20210302T113000
SUMMARY:Meeting

BEGIN:VALARM
UID:8297C37D-BA2D-4476-91AE-C1EAA364F8E1
TRIGGER:-PT15M
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM

END:VEVENT
</pre><a href="#section-7.2-3" class="pilcrow">¶</a>
</div>
<p id="section-7.2-4">When the alarm is triggered, the user decides to "snooze" it
        for 5 minutes.  The client acknowledges the original alarm and
        creates a new "snooze" alarm as a sibling of, and relates it
        to, the original alarm (note that both occurrences of "VALARM" reside within the
        same "parent" VEVENT):<a href="#section-7.2-4" class="pilcrow">¶</a></p>
<div id="section-7.2-5">
<pre class="sourcecode">
BEGIN:VEVENT
CREATED:20210302T151004Z
UID:AC67C078-CED3-4BF5-9726-832C3749F627
DTSTAMP:20210302T151516Z
DTSTART;TZID=America/New_York:20210302T103000
DTEND;TZID=America/New_York:20210302T113000
SUMMARY:Meeting

BEGIN:VALARM
UID:8297C37D-BA2D-4476-91AE-C1EAA364F8E1
TRIGGER:-PT15M
DESCRIPTION:Event reminder
ACTION:DISPLAY
ACKNOWLEDGED:20210302T151514Z
END:VALARM

BEGIN:VALARM
UID:DE7B5C34-83FF-47FE-BE9E-FF41AE6DD097
TRIGGER;VALUE=DATE-TIME:20210302T152000Z
RELATED-TO;RELTYPE=SNOOZE:8297C37D-BA2D-4476-91AE-C1EAA364F8E1
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM

END:VEVENT
</pre><a href="#section-7.2-5" class="pilcrow">¶</a>
</div>
<p id="section-7.2-6">When the "snooze" alarm is triggered, the user decides to
        "snooze" it again for an additional 5 minutes.  The client
        once again acknowledges the original alarm, removes the triggered
        "snooze" alarm, and creates another new "snooze" alarm as a
        sibling of, and relates it to, the original alarm (note the
        different UID for the new "snooze" alarm):<a href="#section-7.2-6" class="pilcrow">¶</a></p>
<div id="section-7.2-7">
<pre class="sourcecode">
BEGIN:VEVENT
CREATED:20210302T151004Z
UID:AC67C078-CED3-4BF5-9726-832C3749F627
DTSTAMP:20210302T152026Z
DTSTART;TZID=America/New_York:20210302T103000
DTEND;TZID=America/New_York:20210302T113000
SUMMARY:Meeting

BEGIN:VALARM
UID:8297C37D-BA2D-4476-91AE-C1EAA364F8E1
TRIGGER:-PT15M
DESCRIPTION:Event reminder
ACTION:DISPLAY
ACKNOWLEDGED:20210302T152024Z
END:VALARM

BEGIN:VALARM
UID:87D690A7-B5E8-4EB4-8500-491F50AFE394
TRIGGER;VALUE=DATE-TIME:20210302T152500Z
RELATED-TO;RELTYPE=SNOOZE:8297C37D-BA2D-4476-91AE-C1EAA364F8E1
DESCRIPTION:Event reminder
ACTION:DISPLAY
END:VALARM

END:VEVENT
</pre><a href="#section-7.2-7" class="pilcrow">¶</a>
</div>
<p id="section-7.2-8">When the second "snooze" alarm is triggered, the user
        decides to dismiss it.  The client acknowledges both the
        original alarm and the second "snooze" alarm:<a href="#section-7.2-8" class="pilcrow">¶</a></p>
<div id="section-7.2-9">
<pre class="sourcecode">
BEGIN:VEVENT
CREATED:20210302T151004Z
UID:AC67C078-CED3-4BF5-9726-832C3749F627
DTSTAMP:20210302T152508Z
DTSTART;TZID=America/New_York:20210302T103000
DTEND;TZID=America/New_York:20210302T113000
SUMMARY:Meeting

BEGIN:VALARM
UID:8297C37D-BA2D-4476-91AE-C1EAA364F8E1
TRIGGER:-PT15M
DESCRIPTION:Event reminder
ACTION:DISPLAY
ACKNOWLEDGED:20210302T152507Z
END:VALARM

BEGIN:VALARM
UID:87D690A7-B5E8-4EB4-8500-491F50AFE394
TRIGGER;VALUE=DATE-TIME:20210302T152500Z
RELATED-TO;RELTYPE=SNOOZE:8297C37D-BA2D-4476-91AE-C1EAA364F8E1
DESCRIPTION:Event reminder
ACTION:DISPLAY
ACKNOWLEDGED:20210302T152507Z
END:VALARM

END:VEVENT
</pre><a href="#section-7.2-9" class="pilcrow">¶</a>
</div>
</section>
</section>
</div>
<div id="proximity">
<section id="section-8">
      <h2 id="name-alarm-proximity-trigger">
<a href="#section-8" class="section-number selfRef">8. </a><a href="#name-alarm-proximity-trigger" class="section-name selfRef">Alarm Proximity Trigger</a>
      </h2>
<p id="section-8-1">Currently, a "VALARM" is triggered when a specific date-time value is
      reached. It is also desirable to be able to trigger alarms based
      on location, e.g., when arriving at or departing from a
      particular location.<a href="#section-8-1" class="pilcrow">¶</a></p>
<p id="section-8-2">This specification adds the following elements to "VALARM"
      components to indicate when an alarm can be triggered based on
      location.<a href="#section-8-2" class="pilcrow">¶</a></p>
<span class="break"></span><dl class="dlParallel" id="section-8-3">
        <dt id="section-8-3.1">"PROXIMITY" property:</dt>
        <dd style="margin-left: 1.5em" id="section-8-3.2">indicates that a location-based trigger is to
        be used and which action is used for the trigger<a href="#section-8-3.2" class="pilcrow">¶</a>
</dd>
        <dd class="break"></dd>
<dt id="section-8-3.3">
<span><a href="#RFC9073" class="xref">"VLOCATION" component(s)</a> [<a href="#RFC9073" class="xref">RFC9073</a>]</span>:</dt>
        <dd style="margin-left: 1.5em" id="section-8-3.4">used to indicate the actual
        location(s) to trigger off of, specified with a URL property containing a
        <span><a href="#RFC5870" class="xref">'geo' URI</a> [<a href="#RFC5870" class="xref">RFC5870</a>]</span>, which allows for two or three
        coordinate values with an optional uncertainty<a href="#section-8-3.4" class="pilcrow">¶</a>
</dd>
      <dd class="break"></dd>
</dl>
<div id="section-8-4">
<pre class="sourcecode lang-abnf">
alarmprop       =/ (
                   ;
                   ; the following is OPTIONAL
                   ; but MUST NOT occur more than once
                   ;
                   proximity
                   ;
                   )

alarm-subcomp   =/ (
                   ;
                   ; the following is OPTIONAL
                   ; and MAY occur more than once but only
                   ; when a PROXIMITY property is also present
                   ;
                   locationc
                   ;
                   )
</pre><a href="#section-8-4" class="pilcrow">¶</a>
</div>
<p id="section-8-5">
        Typically, when a "PROXIMITY" property is used, there is no
        need to specify a time-based trigger using the "TRIGGER"
        property. However, since "TRIGGER" is defined as a required
        property for a "VALARM" component, for backwards compatibility,
        it has to be present but ignored. To indicate a "TRIGGER"
        that is to be ignored, clients <span class="bcp14">SHOULD</span> use a value a long time
        in the past. A value of "19760401T005545Z" has been commonly
        used for this purpose.<a href="#section-8-5" class="pilcrow">¶</a></p>
<div id="PROXIMITY">
<section id="section-8.1">
        <h3 id="name-proximity-property">
<a href="#section-8.1" class="section-number selfRef">8.1. </a><a href="#name-proximity-property" class="section-name selfRef">Proximity Property</a>
        </h3>
<span class="break"></span><dl class="dlParallel" id="section-8.1-1">
          <dt id="section-8.1-1.1">Property Name:</dt>
          <dd style="margin-left: 1.5em" id="section-8.1-1.2">PROXIMITY<a href="#section-8.1-1.2" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-8.1-1.3">Purpose:</dt>
          <dd style="margin-left: 1.5em" id="section-8.1-1.4">This property indicates that a
            location-based trigger is applied to an alarm.<a href="#section-8.1-1.4" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-8.1-1.5">Value Type:</dt>
          <dd style="margin-left: 1.5em" id="section-8.1-1.6">TEXT<a href="#section-8.1-1.6" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-8.1-1.7">Property Parameters:</dt>
          <dd style="margin-left: 1.5em" id="section-8.1-1.8">IANA and nonstandard
            property parameters can be specified on this property.<a href="#section-8.1-1.8" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-8.1-1.9">Conformance:</dt>
          <dd style="margin-left: 1.5em" id="section-8.1-1.10">This property can be specified
            within "VALARM" calendar components.<a href="#section-8.1-1.10" class="pilcrow">¶</a>
</dd>
          <dd class="break"></dd>
<dt id="section-8.1-1.11">Description:</dt>
          <dd style="margin-left: 1.5em" id="section-8.1-1.12">
            <p id="section-8.1-1.12.1">This property is used to
            indicate that an alarm has a location-based trigger.
            Its value identifies the action that will trigger the alarm.<a href="#section-8.1-1.12.1" class="pilcrow">¶</a></p>
<p id="section-8.1-1.12.2">When the property value is set to "ARRIVE", the alarm
            is triggered when the calendar user agent arrives in the
            vicinity of one or more locations.  When set to
            "DEPART", the alarm is triggered when the calendar user
            agent departs from the vicinity of one or more locations.
            Each location <span class="bcp14">MUST</span> be specified with a "VLOCATION"
            component.
            Note that the meaning of "vicinity" in this
            context is implementation defined.<a href="#section-8.1-1.12.2" class="pilcrow">¶</a></p>
<p id="section-8.1-1.12.3">When the property value is set to "CONNECT", the alarm
            is triggered when the calendar user agent connects to an
            automobile to which it has been paired via
            <span><a href="#BTcore" class="xref">Bluetooth</a> [<a href="#BTcore" class="xref">BTcore</a>]</span>.
            When set to "DISCONNECT", the alarm is
            triggered when the calendar user agent disconnects from an
            automobile to which it has been paired via Bluetooth.
            Note that neither current implementations of proximity
            alarms nor this document have a mechanism to target a
            particular automobile.
            Such a mechanism may be specified in a future extension.<a href="#section-8.1-1.12.3" class="pilcrow">¶</a></p>
</dd>
          <dd class="break"></dd>
<dt id="section-8.1-1.13">Format Definition:</dt>
          <dd style="margin-left: 1.5em" id="section-8.1-1.14">
            <p id="section-8.1-1.14.1">This property is defined
            by the following notation:<a href="#section-8.1-1.14.1" class="pilcrow">¶</a></p>
<div id="section-8.1-1.14.2">
<pre class="sourcecode lang-abnf">
proximity = "PROXIMITY" *proximityparam ":" proximityvalue CRLF

proximityparam  = (
                  ;
                  ; the following is OPTIONAL
                  ; and MAY occur more than once
                  ;
                  (";" other-param)
                  ;
                  )

proximityvalue  = "ARRIVE" / "DEPART" /
                  "CONNECT" / "DISCONNECT" / iana-token / x-name
</pre><a href="#section-8.1-1.14.2" class="pilcrow">¶</a>
</div>
</dd>
        <dd class="break"></dd>
</dl>
</section>
</div>
<section id="section-8.2">
        <h3 id="name-example-2">
<a href="#section-8.2" class="section-number selfRef">8.2. </a><a href="#name-example-2" class="section-name selfRef">Example</a>
        </h3>
<p id="section-8.2-1">The following example shows a "VALARM" component with a
        proximity trigger set to trigger when the device running the
        calendar user agent leaves the vicinity defined by the
        URL property in the "VLOCATION" component. Note use of the "u=" parameter
        with the 'geo' URI to define the uncertainty of the location
        determination.<a href="#section-8.2-1" class="pilcrow">¶</a></p>
<div id="section-8.2-2">
<pre class="sourcecode">
BEGIN:VALARM
UID:77D80D14-906B-4257-963F-85B1E734DBB6
ACTION:DISPLAY
TRIGGER;VALUE=DATE-TIME:19760401T005545Z
DESCRIPTION:Remember to buy milk
PROXIMITY:DEPART
BEGIN:VLOCATION
UID:123456-abcdef-98765432
NAME:Office
URL:geo:40.443,-79.945;u=10
END:VLOCATION
END:VALARM
</pre><a href="#section-8.2-2" class="pilcrow">¶</a>
</div>
</section>
</section>
</div>
<section id="section-9">
      <h2 id="name-security-considerations">
<a href="#section-9" class="section-number selfRef">9. </a><a href="#name-security-considerations" class="section-name selfRef">Security Considerations</a>
      </h2>
<p id="section-9-1">In addition to the security properties of iCalendar
      (see <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-7" class="relref">Section 7</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span>),
      a "VALARM", if not monitored properly, can be used to disturb
      users and/or leak personal information.  For instance, an
      undesirable audio alert could cause embarrassment; an
      unwanted display alert could be considered an annoyance; or an
      email alert could be used to leak a user's location to a third
      party or to send unsolicited email to multiple users.
      Therefore, CalDAV clients and servers that accept iCalendar data
      from a third party (e.g., via iCalendar Transport-Independent Interoperability Protocol (iTIP) <span>[<a href="#RFC5546" class="xref">RFC5546</a>]</span>,
      a subscription feed, or a shared calendar) <span class="bcp14">SHOULD</span> remove each
      "VALARM" from the data prior to storing in their calendar system.<a href="#section-9-1" class="pilcrow">¶</a></p>
<p id="section-9-2">Security considerations related to unique identifiers for "VALARM"
      are discussed in <a href="#uid" class="xref">Section 4</a>.<a href="#section-9-2" class="pilcrow">¶</a></p>
</section>
<section id="section-10">
      <h2 id="name-privacy-considerations">
<a href="#section-10" class="section-number selfRef">10. </a><a href="#name-privacy-considerations" class="section-name selfRef">Privacy Considerations</a>
      </h2>
<p id="section-10-1">A proximity "VALARM", if not used carefully, can leak a
      user's past, present, or future location.  For instance,
      storing an iCalendar resource containing proximity "VALARM"s to a
      shared calendar on CalDAV server can expose to anyone that has
      access to that calendar the user's intent to leave
      from or arrive at a particular location at some future time.
      Furthermore, if a CalDAV client updates the shared iCalendar
      resource with an "ACKNOWLEDGED" property when the alarm is
      triggered, this will leak the exact date and time that the user left
      from or arrived at the location.
      
      Therefore, CalDAV clients that implement proximity alarms
      <span class="bcp14">SHOULD</span> give users the option of storing and/or acknowledging the
      alarms on the local device only and not storing the alarm and/or
      acknowledgement on a remote server.<a href="#section-10-1" class="pilcrow">¶</a></p>
<p id="section-10-2">Privacy considerations related to unique identifiers for "VALARM"
      are discussed in <a href="#uid" class="xref">Section 4</a>.<a href="#section-10-2" class="pilcrow">¶</a></p>
</section>
<section id="section-11">
      <h2 id="name-iana-considerations">
<a href="#section-11" class="section-number selfRef">11. </a><a href="#name-iana-considerations" class="section-name selfRef">IANA Considerations</a>
      </h2>
<section id="section-11.1">
        <h3 id="name-property-registrations">
<a href="#section-11.1" class="section-number selfRef">11.1. </a><a href="#name-property-registrations" class="section-name selfRef">Property Registrations</a>
        </h3>
<p id="section-11.1-1">This document defines the following new iCalendar
        properties that have been added to the "Properties" registry defined in
        <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-8.2.3" class="relref">Section 8.2.3</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span> and located here:
        <span>&lt;<a href="https://www.iana.org/assignments/icalendar">https://www.iana.org/assignments/icalendar</a>&gt;</span>.<a href="#section-11.1-1" class="pilcrow">¶</a></p>
<span id="name-additions-to-the-properties"></span><table class="center" id="table-1">
          <caption>
<a href="#table-1" class="selfRef">Table 1</a>:
<a href="#name-additions-to-the-properties" class="selfRef">Additions to the Properties Registry</a>
          </caption>
<thead>
            <tr>
              <th class="text-left" rowspan="1" colspan="1">Property</th>
              <th class="text-left" rowspan="1" colspan="1">Status</th>
              <th class="text-left" rowspan="1" colspan="1">Reference</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-left" rowspan="1" colspan="1">ACKNOWLEDGED</td>
              <td class="text-left" rowspan="1" colspan="1">Current</td>
              <td class="text-left" rowspan="1" colspan="1">RFC 9074, <a href="#ACKNOWLEDGED" class="xref">Section 6.1</a>
</td>
            </tr>
            <tr>
              <td class="text-left" rowspan="1" colspan="1">PROXIMITY</td>
              <td class="text-left" rowspan="1" colspan="1">Current</td>
              <td class="text-left" rowspan="1" colspan="1">RFC 9074, <a href="#PROXIMITY" class="xref">Section 8.1</a>
</td>
            </tr>
          </tbody>
        </table>
</section>
<section id="section-11.2">
        <h3 id="name-relationship-types-registry">
<a href="#section-11.2" class="section-number selfRef">11.2. </a><a href="#name-relationship-types-registry" class="section-name selfRef">Relationship Types Registry</a>
        </h3>
<p id="section-11.2-1">This document defines the following new iCalendar
        relationship type that has been added to the "Relationship Types" registry defined in
        <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-8.3.8" class="relref">Section 8.3.8</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span> and located here:
        <span>&lt;<a href="https://www.iana.org/assignments/icalendar">https://www.iana.org/assignments/icalendar</a>&gt;</span>.<a href="#section-11.2-1" class="pilcrow">¶</a></p>
<span id="name-addition-to-the-relationshi"></span><table class="center" id="table-2">
          <caption>
<a href="#table-2" class="selfRef">Table 2</a>:
<a href="#name-addition-to-the-relationshi" class="selfRef">Addition to the Relationship Types Registry</a>
          </caption>
<thead>
            <tr>
              <th class="text-left" rowspan="1" colspan="1">Relationship Type</th>
              <th class="text-left" rowspan="1" colspan="1">Status</th>
              <th class="text-left" rowspan="1" colspan="1">Reference</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-left" rowspan="1" colspan="1">SNOOZE</td>
              <td class="text-left" rowspan="1" colspan="1">Current</td>
              <td class="text-left" rowspan="1" colspan="1">RFC 9074, <a href="#SNOOZE-PARAM" class="xref">Section 7.1</a>
</td>
            </tr>
          </tbody>
        </table>
</section>
<section id="section-11.3">
        <h3 id="name-proximity-values-registry">
<a href="#section-11.3" class="section-number selfRef">11.3. </a><a href="#name-proximity-values-registry" class="section-name selfRef">Proximity Values Registry</a>
        </h3>
<p id="section-11.3-1">A new iCalendar registry for values
          of the "PROXIMITY" property has been created and is located here:
          <span>&lt;<a href="https://www.iana.org/assignments/icalendar">https://www.iana.org/assignments/icalendar</a>&gt;</span>.<a href="#section-11.3-1" class="pilcrow">¶</a></p>
<p id="section-11.3-2">Additional values <span class="bcp14">MAY</span> be used, provided the process described in
          <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-8.2.1" class="relref">Section 8.2.1</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span> is used to
          register them, using the template in
          <span><a href="https://www.rfc-editor.org/rfc/rfc5545#section-8.2.6" class="relref">Section 8.2.6</a> of [<a href="#RFC5545" class="xref">RFC5545</a>]</span>.<a href="#section-11.3-2" class="pilcrow">¶</a></p>
<p id="section-11.3-3">The following table has been used to initialize the
          Proximity Value Registry.<a href="#section-11.3-3" class="pilcrow">¶</a></p>
<span id="name-initial-contents-of-the-pro"></span><table class="center" id="table-3">
          <caption>
<a href="#table-3" class="selfRef">Table 3</a>:
<a href="#name-initial-contents-of-the-pro" class="selfRef">Initial Contents of the Proximity Values Registry</a>
          </caption>
<thead>
            <tr>
              <th class="text-left" rowspan="1" colspan="1">Value</th>
              <th class="text-left" rowspan="1" colspan="1">Status</th>
              <th class="text-left" rowspan="1" colspan="1">Reference</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-left" rowspan="1" colspan="1">ARRIVE</td>
              <td class="text-left" rowspan="1" colspan="1">Current</td>
              <td class="text-left" rowspan="1" colspan="1">RFC 9074, <a href="#PROXIMITY" class="xref">Section 8.1</a>
</td>
            </tr>
            <tr>
              <td class="text-left" rowspan="1" colspan="1">DEPART</td>
              <td class="text-left" rowspan="1" colspan="1">Current</td>
              <td class="text-left" rowspan="1" colspan="1">RFC 9074, <a href="#PROXIMITY" class="xref">Section 8.1</a>
</td>
            </tr>
            <tr>
              <td class="text-left" rowspan="1" colspan="1">CONNECT</td>
              <td class="text-left" rowspan="1" colspan="1">Current</td>
              <td class="text-left" rowspan="1" colspan="1">RFC 9074, <a href="#PROXIMITY" class="xref">Section 8.1</a>
</td>
            </tr>
            <tr>
              <td class="text-left" rowspan="1" colspan="1">DISCONNECT</td>
              <td class="text-left" rowspan="1" colspan="1">Current</td>
              <td class="text-left" rowspan="1" colspan="1">RFC 9074, <a href="#PROXIMITY" class="xref">Section 8.1</a>
</td>
            </tr>
          </tbody>
        </table>
</section>
</section>
<section id="section-12">
      <h2 id="name-references">
<a href="#section-12" class="section-number selfRef">12. </a><a href="#name-references" class="section-name selfRef">References</a>
      </h2>
<section id="section-12.1">
        <h3 id="name-normative-references">
<a href="#section-12.1" class="section-number selfRef">12.1. </a><a href="#name-normative-references" class="section-name selfRef">Normative References</a>
        </h3>
<dl class="references">
<dt id="RFC2119">[RFC2119]</dt>
        <dd>
<span class="refAuthor">Bradner, S.</span>, <span class="refTitle">"Key words for use in RFCs to Indicate Requirement Levels"</span>, <span class="seriesInfo">BCP 14</span>, <span class="seriesInfo">RFC 2119</span>, <span class="seriesInfo">DOI 10.17487/RFC2119</span>, <time datetime="1997-03" class="refDate">March 1997</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc2119">https://www.rfc-editor.org/info/rfc2119</a>&gt;</span>. </dd>
<dd class="break"></dd>
<dt id="RFC5234">[RFC5234]</dt>
        <dd>
<span class="refAuthor">Crocker, D., Ed.</span> and <span class="refAuthor">P. Overell</span>, <span class="refTitle">"Augmented BNF for Syntax Specifications: ABNF"</span>, <span class="seriesInfo">STD 68</span>, <span class="seriesInfo">RFC 5234</span>, <span class="seriesInfo">DOI 10.17487/RFC5234</span>, <time datetime="2008-01" class="refDate">January 2008</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc5234">https://www.rfc-editor.org/info/rfc5234</a>&gt;</span>. </dd>
<dd class="break"></dd>
<dt id="RFC5545">[RFC5545]</dt>
        <dd>
<span class="refAuthor">Desruisseaux, B., Ed.</span>, <span class="refTitle">"Internet Calendaring and Scheduling Core Object Specification (iCalendar)"</span>, <span class="seriesInfo">RFC 5545</span>, <span class="seriesInfo">DOI 10.17487/RFC5545</span>, <time datetime="2009-09" class="refDate">September 2009</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc5545">https://www.rfc-editor.org/info/rfc5545</a>&gt;</span>. </dd>
<dd class="break"></dd>
<dt id="RFC5870">[RFC5870]</dt>
        <dd>
<span class="refAuthor">Mayrhofer, A.</span> and <span class="refAuthor">C. Spanring</span>, <span class="refTitle">"A Uniform Resource Identifier for Geographic Locations ('geo' URI)"</span>, <span class="seriesInfo">RFC 5870</span>, <span class="seriesInfo">DOI 10.17487/RFC5870</span>, <time datetime="2010-06" class="refDate">June 2010</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc5870">https://www.rfc-editor.org/info/rfc5870</a>&gt;</span>. </dd>
<dd class="break"></dd>
<dt id="RFC7986">[RFC7986]</dt>
        <dd>
<span class="refAuthor">Daboo, C.</span>, <span class="refTitle">"New Properties for iCalendar"</span>, <span class="seriesInfo">RFC 7986</span>, <span class="seriesInfo">DOI 10.17487/RFC7986</span>, <time datetime="2016-10" class="refDate">October 2016</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc7986">https://www.rfc-editor.org/info/rfc7986</a>&gt;</span>. </dd>
<dd class="break"></dd>
<dt id="RFC8174">[RFC8174]</dt>
        <dd>
<span class="refAuthor">Leiba, B.</span>, <span class="refTitle">"Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words"</span>, <span class="seriesInfo">BCP 14</span>, <span class="seriesInfo">RFC 8174</span>, <span class="seriesInfo">DOI 10.17487/RFC8174</span>, <time datetime="2017-05" class="refDate">May 2017</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc8174">https://www.rfc-editor.org/info/rfc8174</a>&gt;</span>. </dd>
<dd class="break"></dd>
<dt id="RFC9073">[RFC9073]</dt>
      <dd>
<span class="refAuthor">Douglass, M.</span>, <span class="refTitle">"Event Publishing Extensions to iCalendar"</span>, <span class="seriesInfo">RFC 9073</span>, <span class="seriesInfo">DOI 10.17487/RFC9073</span>, <time datetime="2021-08" class="refDate">August 2021</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc9073">https://www.rfc-editor.org/info/rfc9073</a>&gt;</span>. </dd>
<dd class="break"></dd>
</dl>
</section>
<section id="section-12.2">
        <h3 id="name-informative-references">
<a href="#section-12.2" class="section-number selfRef">12.2. </a><a href="#name-informative-references" class="section-name selfRef">Informative References</a>
        </h3>
<dl class="references">
<dt id="BTcore">[BTcore]</dt>
        <dd>
<span class="refAuthor">Bluetooth Special Interest Group</span>, <span class="refTitle">"Bluetooth Core Specification Version 5.0 Feature Overview"</span>, <time datetime="2016-12" class="refDate">December 2016</time>, <span>&lt;<a href="https://www.bluetooth.com/bluetooth-resources/bluetooth-5-%20%20%20%20%20%20%20%20go-faster-go-further/">https://www.bluetooth.com/bluetooth-resources/bluetooth-5-        go-faster-go-further/</a>&gt;</span>. </dd>
<dd class="break"></dd>
<dt id="RFC4791">[RFC4791]</dt>
        <dd>
<span class="refAuthor">Daboo, C.</span>, <span class="refAuthor">Desruisseaux, B.</span>, and <span class="refAuthor">L. Dusseault</span>, <span class="refTitle">"Calendaring Extensions to WebDAV (CalDAV)"</span>, <span class="seriesInfo">RFC 4791</span>, <span class="seriesInfo">DOI 10.17487/RFC4791</span>, <time datetime="2007-03" class="refDate">March 2007</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc4791">https://www.rfc-editor.org/info/rfc4791</a>&gt;</span>. </dd>
<dd class="break"></dd>
<dt id="RFC5546">[RFC5546]</dt>
      <dd>
<span class="refAuthor">Daboo, C., Ed.</span>, <span class="refTitle">"iCalendar Transport-Independent Interoperability Protocol (iTIP)"</span>, <span class="seriesInfo">RFC 5546</span>, <span class="seriesInfo">DOI 10.17487/RFC5546</span>, <time datetime="2009-12" class="refDate">December 2009</time>, <span>&lt;<a href="https://www.rfc-editor.org/info/rfc5546">https://www.rfc-editor.org/info/rfc5546</a>&gt;</span>. </dd>
<dd class="break"></dd>
</dl>
</section>
</section>
<section id="appendix-A">
      <h2 id="name-acknowledgements">
<a href="#name-acknowledgements" class="section-name selfRef">Acknowledgements</a>
      </h2>
<p id="appendix-A-1">This specification came about via discussions at The
      Calendaring and Scheduling Consortium. Also, thanks to the
      following for providing feedback: <span class="contact-name">Bernard Desruisseaux</span>, <span class="contact-name">Mike       Douglass</span>, <span class="contact-name">Jacob Farkas</span>, <span class="contact-name">Jeffrey Harris</span>, <span class="contact-name">Ciny Joy</span>, <span class="contact-name">Barry Leiba</span>,
      and <span class="contact-name">Daniel Migault</span>.<a href="#appendix-A-1" class="pilcrow">¶</a></p>
</section>
<div id="authors-addresses">
<section id="appendix-B">
      <h2 id="name-authors-addresses">
<a href="#name-authors-addresses" class="section-name selfRef">Authors' Addresses</a>
      </h2>
<address class="vcard">
        <div dir="auto" class="left"><span class="fn nameRole">Cyrus Daboo</span></div>
<div dir="auto" class="left"><span class="org">Apple Inc.</span></div>
<div dir="auto" class="left"><span class="street-address">1 Infinite Loop</span></div>
<div dir="auto" class="left">
<span class="locality">Cupertino</span>, <span class="region">CA</span> <span class="postal-code">95014</span>
</div>
<div dir="auto" class="left"><span class="country-name">United States of America</span></div>
<div class="email">
<span>Email:</span>
<a href="mailto:cyrus@daboo.name" class="email">cyrus@daboo.name</a>
</div>
<div class="url">
<span>URI:</span>
<a href="http://www.apple.com/" class="url">http://www.apple.com/</a>
</div>
</address>
<address class="vcard">
        <div dir="auto" class="left"><span class="fn nameRole">Kenneth Murchison (<span class="role">editor</span>)</span></div>
<div dir="auto" class="left"><span class="org">Fastmail US LLC</span></div>
<div dir="auto" class="left"><span class="extended-address">Suite 1201</span></div>
<div dir="auto" class="left"><span class="street-address">1429 Walnut St</span></div>
<div dir="auto" class="left">
<span class="locality">Philadelphia</span>, <span class="region">PA</span> <span class="postal-code">19102</span>
</div>
<div dir="auto" class="left"><span class="country-name">United States of America</span></div>
<div class="email">
<span>Email:</span>
<a href="mailto:murch@fastmailteam.com" class="email">murch@fastmailteam.com</a>
</div>
<div class="url">
<span>URI:</span>
<a href="https://www.fastmail.com/" class="url">http://www.fastmail.com/</a>
</div>
</address>
</section>
</div>
<script>const toc = document.getElementById("toc");
toc.querySelector("h2").addEventListener("click", e => {
  toc.classList.toggle("active");
});
toc.querySelector("nav").addEventListener("click", e => {
  toc.classList.remove("active");
});
</script>
</body>
</html>


```

### `SECURITY.md`

```md
Security Policy
===============

Supported Versions
------------------

Security fixes will be released as a new version. Since the API is relatively stable and this is a small project, we release security fixes in new releases.

Reporting a Vulnerability
-------------------------

To report a security vulnerability, please use the
[Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.

```

### `tox.ini`

```ini
# tox (https://tox.readthedocs.io/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
skipsdist = True
envlist = py38, py39, py310, py311, py312, ruff, build

[testenv]
setenv = TMPDIR={envtmpdir}
passenv = TZ
deps = -e .[test]
commands =
    pytest --basetemp="{envtmpdir}" {posargs}

[testenv:ruff]
deps = ruff
skip_install = True
commands =
    ruff format
    ruff check --fix

[testenv:build]
deps =
    build
    twine
    pip-tools
commands =
    pip-compile
    python -c "from shutil import rmtree; rmtree('dist', ignore_errors=True)"
    python -m build .
    twine check dist/*

[testenv:docs]
basepython = python3.14
skip_install = True
changedir = docs
deps =
    -r docs/requirements.txt
    -e .
allowlist_externals =
    rm
commands =
    # copied from Makefile
    rm -rf _build
    # see https://stackoverflow.com/a/59897351/1320237
    sphinx-build -b html --fresh-env --write-all . _build/html

```
