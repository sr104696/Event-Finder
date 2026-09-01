# seatgeek/thefuzz@master

- Files included: 22
- Files skipped: 1
- Total size: 81.3 KB
- Estimated tokens: ~20,794

## Directory Structure

```
├── .github
│   └── workflows
│       └── ci.yml
├── data
│   └── titledata.csv
├── thefuzz
│   ├── __init__.py
│   ├── fuzz.py
│   ├── fuzz.pyi
│   ├── process.py
│   ├── py.typed
│   ├── utils.py
│   └── utils.pyi
├── .editorconfig
├── .gitignore
├── benchmarks.py
├── CHANGES.rst
├── LICENSE.txt
├── MANIFEST.in
├── README.rst
├── release
├── requirements.txt
├── setup.py
├── test_thefuzz_hypothesis.py
├── test_thefuzz_pytest.py
├── test_thefuzz.py
└── tox.ini
```

## Code Digest

### `.editorconfig`

```editorconfig
# .editorconfig
# http://editorconfig.org/
root = true

[*]
charset = utf-8
end_of_line = lf
indent_size = 2
indent_style = space
insert_final_newline = true
trim_trailing_whitespace = true

[*.bat]
end_of_line = crlf

[*.go]
indent_size = 4
indent_style = tab

[*.html]
indent_size = 4

[*Makefile]
indent_size = 4
indent_style = tab

[*.php]
indent_size = 4

[*.py]
indent_size = 4

[*.xml]
indent_size = 4

```

### `.github/workflows/ci.yml`

```yml
name: The Fuzz

on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"]
        test-cmd: [pytest]
        include:
          - python-version: "3.8"
            test-cmd: python setup.py check --restructuredtext --strict --metadata
          - python-version: "3.11"
            test-cmd: python setup.py check --restructuredtext --strict --metadata
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
          allow-prereleases: true
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip setuptools wheel
          pip install pytest pycodestyle docutils Pygments hypothesis

      - name: Install project
        run: pip install .

      - name: Test with pytest
        run: ${{ matrix.test-cmd }}

```

### `.gitignore`

```gitignore
*.py[oc]

# Temp files
*~
~*
.*~
\#*
.#*
*#

# Build files
build
dist
pkg
*.egg
*.egg-info

# Debian Files
debian/files
debian/python-beaver*

# Sphinx build
doc/_build

# Generated man page
doc/aws_hostname.1

# tox
.tox

# Hypothesis - keep the examples database
.hypothesis/tmp
.hypothesis/unicodedata
.hypothesis

# pytest
.cache/
.pytest_cache
__pycache__

# Pycharm
.idea/

# vscode
.vscode/

```

### `benchmarks.py`

```py
from timeit import timeit
import math
import csv

iterations = 100000


reader = csv.DictReader(open('data/titledata.csv'), delimiter='|')
titles = [i['custom_title'] for i in reader]
title_blob = '\n'.join(titles)


cirque_strings = [
    "cirque du soleil - zarkana - las vegas",
    "cirque du soleil ",
    "cirque du soleil las vegas",
    "zarkana las vegas",
    "las vegas cirque du soleil at the bellagio",
    "zarakana - cirque du soleil - bellagio"
]

choices = [
    "",
    "new york yankees vs boston red sox",
    "",
    "zarakana - cirque du soleil - bellagio",
    None,
    "cirque du soleil las vegas",
    None
]

mixed_strings = [
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    "C\\'est la vie",
    "Ça va?",
    "Cães danados",
    "\xacCamarões assados",
    "a\xac\u1234\u20ac\U00008000"
]

common_setup = "from thefuzz import fuzz, utils; "


def print_result_from_timeit(stmt='pass', setup='pass', number=1000000):
    """
    Clean function to know how much time took the execution of one statement
    """
    units = ["s", "ms", "us", "ns"]
    duration = timeit(stmt, setup, number=int(number))
    avg_duration = duration / float(number)
    thousands = int(math.floor(math.log(avg_duration, 1000)))

    print("Total time: {:f}s. Average run: {:.3f}{}.".format(
        duration, avg_duration * (1000 ** -thousands), units[-thousands]))


for s in mixed_strings + cirque_strings + choices:
    print('Test full_process for: "%s"' % s)
    print_result_from_timeit('utils.full_process(u\'%s\')' % s,
                             common_setup, number=iterations)

# benchmarking the core matching methods...

for s in cirque_strings:
    print('Test fuzz.ratio for string: "%s"' % s)
    print('-------------------------------')
    print_result_from_timeit('fuzz.ratio(u\'cirque du soleil\', u\'%s\')' % s,
                             common_setup, number=iterations / 100)

for s in cirque_strings:
    print('Test fuzz.partial_ratio for string: "%s"' % s)
    print('-------------------------------')
    print_result_from_timeit('fuzz.partial_ratio(u\'cirque du soleil\', u\'%s\')'
                             % s, common_setup, number=iterations / 100)

for s in cirque_strings:
    print('Test fuzz.WRatio for string: "%s"' % s)
    print('-------------------------------')
    print_result_from_timeit('fuzz.WRatio(u\'cirque du soleil\', u\'%s\')' % s,
                             common_setup, number=iterations / 100)

print('Test process.extract(scorer =  fuzz.QRatio) for string: "%s"' % s)
print('-------------------------------')
print_result_from_timeit('process.extract(u\'cirque du soleil\', choices, scorer =  fuzz.QRatio)',
                             common_setup + " from thefuzz import process; import string,random; random.seed(18);"
                             " choices = [\'\'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30)) for s in range(5000)]",
                              number=10)

print('Test process.extract(scorer =  fuzz.WRatio) for string: "%s"' % s)
print('-------------------------------')
print_result_from_timeit('process.extract(u\'cirque du soleil\', choices, scorer =  fuzz.WRatio)',
                             common_setup + " from thefuzz import process; import string,random; random.seed(18);"
                             " choices = [\'\'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30)) for s in range(5000)]",
                              number=10)


# let me show you something

s = 'New York Yankees'

test = 'import functools\n'
test += 'title_blob = """%s"""\n' % title_blob
test += 'title_blob = title_blob.strip()\n'
test += 'titles = title_blob.split("\\n")\n'

print('Real world ratio(): "%s"' % s)
print('-------------------------------')
test += 'prepared_ratio = functools.partial(fuzz.ratio, "%s")\n' % s
test += 'titles.sort(key=prepared_ratio)\n'
print_result_from_timeit(test, common_setup, number=100)

```

### `CHANGES.rst`

```rst
Changelog
=========

0.17.0 (2018-08-20)
-------------------

- Make benchmarks script Py3 compatible. [Stefan Behnel]

- Add Go lang port. [iddober]

- Add reference to C# port. [ericcoleman]

- Chore: remove license header from files. [Jose Diaz-Gonzalez]

  The files should all inherit the projects license.


- Fix README title style. [Thomas Grainger]

- Add readme check. [Thomas Grainger]

  install docutils and Pygments


- Cache pip. [Thomas Grainger]

- Upgrade pip/setuptools for hypothesis. [Thomas Grainger]

- Feat: drop py26 and py33 support from tox. [Jose Diaz-Gonzalez]

- Feat: drop support for 2.6 in test_thefuzz.py. [Jose Diaz-Gonzalez]

- Feat: drop reference to 2.4 from readme. [Jose Diaz-Gonzalez]

- Feat: drop py2.6 and py3.3 classifiers. [Jose Diaz-Gonzalez]

- Feat: drop 2.6 and 3.3 support. [Jose Diaz-Gonzalez]

  These are no longer supported. Please upgrade your python version if you are using either version.

- Fuzz: _token_sort: check for equivalence. [Ralf Ramsauer]

  If we don't have to full_process the strings, we can safely assume to
  return 100 in case both candidates equal.

  Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>


- Test: add more test cases. [Ralf Ramsauer]

  Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>


- Utils: add and use check_for_equivalence decorator. [Ralf Ramsauer]

  And decorate basic scoring functions.

  The check_for_equivalence decorator MUST be used after the
  check_for_none decorator, as otherwise ratio(None, None) will get a
  score of 100.

  This fixes the first part of the recently introduced changes in the test
  set.

  Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>


- Tests: add some corner cases. [Ralf Ramsauer]

  '' and '' are equal, so are '{' and '{'. Test if thefuzz gives them a
  score of 100.

  For the moment, this patch breaks tests, fixes in thefuzz follow.

  Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>


- Utils: remove superfluous check. [Ralf Ramsauer]

  Decorators make sure that only non None-values are passed. We can safely
  assume that None will never get here.

  Other than that, None's shouldn't simply be ignored and erroneously
  changed to empty strings. Better let users fail.

  This commit doesn't break any tests.

  Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>


- README: add missing requirements. [Ralf Ramsauer]

  pycodestyle and hypothesis are required for automatic testing. Add them
  to README's requirement section.

  Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>


- Remove empty document. [Ralf Ramsauer]

  Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>


0.16.0 (2017-12-18)
-------------------

- Add punctuation characters back in so process does something.
  [davidcellis]

- Simpler alphabet and even fewer examples. [davidcellis]

- Fewer examples and larger deadlines for Hypothesis. [davidcellis]

- Slightly more examples. [davidcellis]

- Attempt to fix the failing 2.7 and 3.6 python tests. [davidcellis]

- Readme: add link to C++ port. [Lizard]

- Fix tests on Python 3.3. [Jon Banafato]

  Modify tox.ini and .travis.yml to install enum34 when running with
  Python 3.3 to allow hypothesis tests to pass.


- Normalize Python versions. [Jon Banafato]

  - Enable Travis-CI tests for Python 3.6
  - Enable tests for all supported Python versions in tox.ini
  - Add Trove classifiers for Python 3.4 - 3.6 to setup.py

  ---

  Note: Python 2.6 and 3.3 are no longer supported by the Python core
  team. Support for these can likely be dropped, but that's out of scope
  for this change set.


- Fix typos. [Sven-Hendrik Haase]

0.15.1 (2017-07-19)
-------------------

- Fix setup.py (addresses #155) [Paul O'Leary McCann]

- Merge remote-tracking branch 'upstream/master' into
  extract_optimizations. [nolan]

- Seed random before generating benchmark strings. [nolan]

- Cleaner implementation of same idea without new param, but adding
  existing full_process param to Q,W,UQ,UW. [nolan]

- Fix benchmark only generate list once. [nolan]

- Only run util.full_process once on query when using extract functions,
  add new benchmarks. [nolan]

0.15.0 (2017-02-20)
-------------------

- Add extras require to install python-levenshtein optionally. [Rolando
  Espinoza]

  This allows to install python-levenshtein as dependency.


- Fix link formatting in the README. [Alex Chan]

- Add fuzzball.js JavaScript port link. [nolan]

- Added Rust Port link. [Logan Collins]

- Validate_string docstring. [davidcellis]

- For full comparisons test that ONLY exact matches (after processing)
  are added. [davidcellis]

- Add detailed docstrings to WRatio and QRatio comparisons.
  [davidcellis]

0.14.0 (2016-11-04)
-------------------

- Possible PEP-8 fix + make pep-8 warnings appear in test. [davidcellis]

- Possible PEP-8 fix. [davidcellis]

- Possible PEP-8 fix. [davidcellis]

- Test for stderr log instead of warning. [davidcellis]

- Convert warning.warn to logging.warning. [davidcellis]

- Additional details for empty string warning from process.
  [davidcellis]

  String formatting fix for python 2.6


- Enclose warnings.simplefilter() inside a with statement. [samkennerly]

0.13.0 (2016-11-01)
-------------------

- Support alternate git status output. [Jose Diaz-Gonzalez]

- Split warning test into new test file, added to travis execution on
  2.6 / pypy3. [davidcellis]

- Remove hypothesis examples database from gitignore. [davidcellis]

- Add check for warning to tests. [davidcellis]

  Reordered test imports


- Check processor and warn before scorer may remove processor.
  [davidcellis]

- Renamed test - tidied docstring. [davidcellis]

- Add token ratios to the list of scorers that skip running full_process
  as a processor. [davidcellis]

- Added tokex_sort, token_set to test. [davidcellis]

- Test docstrings/comments. [davidcellis]

  Removed redundant check from test.


- Added py.test .cache/ removed duplicated build from gitignore.
  [davidcellis]

- Added default_scorer, default_processor parameters to make it easier
  to change in the future. [davidcellis]

  Added warning if the processor reduces the input query to an empty string.


- Rewrote extracts to explicitly use default values for processor and
  scorer. [davidcellis]

- Changed Hypothesis tests to use pytest parameters. [davidcellis]

- Added Hypothesis based tests for identical strings. [Ducksual]

  Added support for hypothesis to travis config.
  Hypothesis based tests are skipped on Python 2.6 and pypy3.

  Added .hypothesis/ folder to gitignore


- Added test for simple 'a, b' string on process.extractOne. [Ducksual]

- Process the query in process.extractWithoutOrder when using a scorer
  which does not do so. [Ducksual]

  Closes 139


- Mention that difflib and levenshtein results may differ. [Jose Diaz-
  Gonzalez]

  Closes #128

0.12.0 (2016-09-14)
-------------------

- Declare support for universal wheels. [Thomas Grainger]

- Clarify that license is GPLv2. [Gareth Tan]

0.11.1 (2016-07-27)
-------------------

- Add editorconfig. [Jose Diaz-Gonzalez]

- Added tox.ini cofig file for easy local multi-environment testing
  changed travis config to use py.test like tox updated use of pep8
  module to pycodestyle. [Pedro Rodrigues]

0.11.0 (2016-06-30)
-------------------

- Clean-up. [desmaisons_david]

- Improving performance. [desmaisons_david]

- Performance Improvement. [desmaisons_david]

- Fix link to Levenshtein. [Brian J. McGuirk]

- Fix readme links. [Brian J. McGuirk]

- Add license to StringMatcher.py. [Jose Diaz-Gonzalez]

  Closes #113

0.10.0 (2016-03-14)
-------------------

- Handle None inputs same as empty string (Issue #94) [Nick Miller]

0.9.0 (2016-03-07)
------------------

- Pull down all keys when updating local copy. [Jose Diaz-Gonzalez]

0.8.2 (2016-02-26)
------------------

- Remove the warning for "slow" sequence matcher on PyPy. [Julian
  Berman]

  where it's preferable to use the pure-python implementation.

0.8.1 (2016-01-25)
------------------

- Minor release changes. [Jose Diaz-Gonzalez]

- Clean up wiki link in readme. [Ewan Oglethorpe]

0.8.0 (2015-11-16)
------------------

- Refer to Levenshtein distance in readme. Closes #88. [Jose Diaz-
  Gonzalez]

- Added install step for travis to have pep8 available. [Pedro
  Rodrigues]

- Added a pep8 test. The way I add the error 501 to the ignore tuple is
  probably wrong but from the docs and source code of pep8 I could not
  find any other way. [Pedro Rodrigues]

  I also went ahead and removed the pep8 call from the release file.


- Added python 3.5, pypy, and ypyp3 to the travis config file. [Pedro
  Rodrigues]

- Added another step to the release file to run the tests before
  releasing. [Pedro Rodrigues]

- Fixed a few pep8 errors Added a verification step in the release
  automation file. This step should probably be somewhere at git level.
  [Pedro Rodrigues]

- Pep8. [Pedro Rodrigues]

- Leaving TODOs in the code was never a good idea. [Pedro Rodrigues]

- Changed return values to be rounded integers. [Pedro Rodrigues]

- Added a test with the recovered data file. [Pedro Rodrigues]

- Recovered titledata.csv. [Pedro Rodrigues]

- Move extract test methods into the process test. [Shale Craig]

  Somehow, they ended up in the `RatioTest`, despite asserting that the
  `ProcessTest` works.


0.7.0 (2015-10-02)
------------------

- Use portable syntax for catching exception on tests. [Luis Madrigal]

- [Fix] test against correct variable. [Luis Madrigal]

- Add unit tests for validator decorators. [Luis Madrigal]

- Move validators to decorator functions. [Luis Madrigal]

  This allows easier composition and IMO makes the functions more readable


- Fix typo: dictionery -> dictionary. [shale]

- FizzyWuzzy -> TheFuzz typo correction. [shale]

- Add check for gitchangelog. [Jose Diaz-Gonzalez]

0.6.2 (2015-09-03)
------------------

- Ensure the rst-lint binary is available. [Jose Diaz-Gonzalez]

0.6.1 (2015-08-07)
------------------

- Minor whitespace changes for PEP8. [Jose Diaz-Gonzalez]

0.6.0 (2015-07-20)
------------------

- Added link to a java port. [Andriy Burkov]

- Patched "name 'unicode' is not defined" python3. [Carlos Garay]

  https://github.com/seatgeek/thefuzz/issues/80

- Make process.extract accept {dict, list}-like choices. [Nathan
  Typanski]

  Previously, process.extract expected lists or dictionaries, and tested
  this with isinstance() calls. In keeping with the spirit of Python (duck
  typing and all that), this change enables one to use extract() on any
  dict-like object for dict-like results, or any list-like object for
  list-like results.

  So now we can (and, indeed, I've added tests for these uses) call
  extract() on things like:

  - a generator of strings ("any iterable")
  - a UserDict
  - custom user-made classes that "look like" dicts
    (or, really, anything with a .items() method that behaves like a dict)
  - plain old lists and dicts

  The behavior is exactly the same for previous use cases of
  lists-and-dicts.

  This change goes along nicely with PR #68, since those docs suggest
  dict-like behavior is valid, and this change makes that true.


- Merge conflict. [Adam Cohen]

- Improve docs for thefuzz.process. [Nathan Typanski]

  The documentation for this module was dated and sometimes inaccurate.
  This overhauls the docs to accurately describe the current module,
  including detailing optional arguments that were not previously
  explained - e.g., limit argument to extract().

  This change follows the Google Python Style Guide, which may be found
  at:

  <https://google-styleguide.googlecode.com/svn/trunk/pyguide.html?showone=Comments#Comments>


0.5.0 (2015-02-04)
------------------

- FIX: 0.4.0 is released, no need to specify 0.3.1 in README. [Josh
  Warner (Mac)]

- Fixed a small typo. [Rostislav Semenov]

- Reset `processor` and `scorer` defaults to None with argument
  checking. [foxxyz]

- Catch generators without lengths. [Jeremiah Lowin]

- Fixed python3 issue and deprecated assertion method. [foxxyz]

- Fixed some docstrings, typos, python3 string method compatibility,
  some errors that crept in during rebase. [foxxyz]

- [mod] The lamdba in extract is not needed. [Olivier Le Thanh Duong]

  [mod] Pass directly the defaults functions in the args

  [mod] itertools.takewhile() can handle empty list just fine no need to test for it

  [mod] Shorten extractOne by removing double if

  [mod] Use a list comprehention in extract()

  [mod] Autopep8 on process.py

  [doc] Document make_type_consistent

  [mod] bad_chars shortened

  [enh] Move regex compilation outside the method, otherwise we don't get the benefit from it

  [mod] Don't need all the blah just to redefine method from string module

  [mod] Remove unused import

  [mod] Autopep8 on string_processing.py

  [mod] Rewrote asciidammit without recursion to make it more readable

  [mod] Autopep8 on utils.py

  [mod] Remove unused import

  [doc] Add some doc to fuzz.py

  [mod] Move the code to sort string in a separate function

  [doc] Docstrings for WRatio, UWRatio


- Add note on which package to install. Closes #67. [Jose Diaz-Gonzalez]

0.4.0 (2014-10-31)
------------------

- In extarctBests() and extractOne() use '>=' instead of '>' [Юрий
  Пайков]

- Fixed python3 issue with SequenceMatcher import. [Юрий Пайков]

0.3.3 (2014-10-22)
------------------

- Fixed issue #59 - "partial" parameter for `_token_set()` is now
  honored. [Юрий Пайков]

- Catch generators without lengths. [Jeremiah Lowin]

- Remove explicit check for lists. [Jeremiah Lowin]

  The logic in `process.extract()` should support any Python sequence/iterable. The explicit check for lists is unnecessary and limiting (for example, it forces conversion of generators and other iterable classes to lists).

0.3.2 (2014-09-12)
------------------

- Make release command an executable. [Jose Diaz-Gonzalez]

- Simplify MANIFEST.in. [Jose Diaz-Gonzalez]

- Add a release script. [Jose Diaz-Gonzalez]

- Fix readme codeblock. [Jose Diaz-Gonzalez]

- Minor formatting. [Jose Diaz-Gonzalez]

- Use __version__ from thefuzz package. [Jose Diaz-Gonzalez]

- Set __version__ constant in __init__.py. [Jose Diaz-Gonzalez]

- Rename LICENSE to LICENSE.txt. [Jose Diaz-Gonzalez]

0.3.0 (2014-08-24)
------------------

- Test dict input to extractOne() [jamesnunn]

- Remove whitespace. [jamesnunn]

- Choices parameter for extract() accepts both dict and list objects.
  [jamesnunn]

- Enable automated testing with Python 3.4. [Corey Farwell]

- Fixed typo: lettters -> letters. [Tal Einat]

- Fixing LICENSE and README's license info. [Dallas Gutauckis]

- Proper ordered list. [Jeff Paine]

- Convert README to rst. [Jeff Paine]

- Add requirements.txt per discussion in #44. [Jeff Paine]

- Add LICENSE TO MANIFEST.in. [Jeff Paine]

- Rename tests.py to more common test_thefuzz.py. [Jeff Paine]

- Add proper MANIFEST template. [Jeff Paine]

- Remove MANIFEST file Not meant to be kept in version control. [Jeff
  Paine]

- Remove unused file. [Jeff Paine]

- Pep8. [Jeff Paine]

- Pep8 formatting. [Jeff Paine]

- Pep8 formatting. [Jeff Paine]

- Pep8 indentations. [Jeff Paine]

- Pep8 cleanup. [Jeff Paine]

- Pep8. [Jeff Paine]

- Pep8 cleanup. [Jeff Paine]

- Pep8 cleanup. [Jeff Paine]

- Pep8 import style. [Jeff Paine]

- Pep8 import ordering. [Jeff Paine]

- Pep8 import ordering. [Jeff Paine]

- Remove unused module. [Jeff Paine]

- Pep8 import ordering. [Jeff Paine]

- Remove unused module. [Jeff Paine]

- Pep8 import ordering. [Jeff Paine]

- Remove unused imports. [Jeff Paine]

- Remove unused module. [Jeff Paine]

- Remove import * where present. [Jeff Paine]

- Avoid import * [Jeff Paine]

- Add Travis CI badge. [Jeff Paine]

- Remove python 2.4, 2.5 from Travis (not supported) [Jeff Paine]

- Add python 2.4 and 2.5 to Travis. [Jeff Paine]

- Add all supported python versions to travis. [Jeff Paine]

- Bump minor version number. [Jeff Paine]

- Add classifiers for python versions. [Jeff Paine]

- Added note about python-Levenshtein speedup. Closes #34. [Jose Diaz-
  Gonzalez]

- Fixed tests on 2.6. [Grigi]

- Fixed py2.6. [Grigi]

- Force bad_chars to ascii. [Grigi]

- Since importing unicode_literals, u decorator not required on strings
  from py2.6 and up. [Grigi]

- Py3 support without 2to3. [Grigi]

- Created: Added .travis.yml. [futoase]

- [enh] Add docstrings to process.py. [Olivier Le Thanh Duong]

  Turn the existings comments into docstrings so they can be seen via introspection


- Don't condense multiple punctuation characters to a single whitespace.
  this is a behavioral change. [Adam Cohen]

- UQRatio and UWRatio shorthands. [Adam Cohen]

- Version 0.2. [Adam Cohen]

- Unicode/string comparison bug. [Adam Cohen]

- To maintain backwards compatibility, default is to force_ascii as
  before. [Adam Cohen]

- Fix merge conflict. [Adam Cohen]

- New process function: extractBests. [Flávio Juvenal]

- More readable reverse sorting. [Flávio Juvenal]

- Further honoring of force_ascii. [Adam Cohen]

- Indentation fix. [Adam Cohen]

- Handle force_ascii in fuzz methods. [Adam Cohen]

- Add back relevant tests. [Adam Cohen]

- Utility method to make things consistent. [Adam Cohen]

- Re-commit asciidammit and add a parameter to full_process to determine
  behavior. [Adam Cohen]

- Added a test for non letters/digits replacements. [Tristan Launay]

- ENG-741 fixed benchmark line length. [Laurent Erignoux]

- Fixed Unicode flag for tests. [Tristan Launay]

- ENG-741 commented code removed not erased for review from creator.
  [Laurent Erignoux]

- ENG-741 cut long lines in fuzzy wizzy benchmark. [Laurent Erignoux]

- Re-upped the limit on benchmark, now that performance is not an issue
  anymore. [Tristan Launay]

- Fixed comment. [Tristan Launay]

- Simplified processing of strings with built-in regex code in python.
  Also fixed empty string detection in token_sort_ratio. [Tristan
  Launay]

- Proper benchmark display. Introduce methods to explicitly do all the
  unicode preprocessing *before* using fuzz lib. [Tristan Launay]

- ENG-741: having a true benchmark, to see when we improve stuff.
  [Benjamin Combourieu]

- Unicode support in benchmark.py. [Benjamin Combourieu]

- Added file for processing strings. [Tristan Launay]

- Uniform treatment of strings in Unicode. Non-ASCII chars are now
  considered in strings, which allows for matches in Cyrillic, Chinese,
  Greek, etc. [Tristan Launay]

- Fixed bug in _token_set. [Michael Edward]

- Removed reference to PR. [Jose Diaz-Gonzalez]

- Sadist build and virtualenv dirs are not part of the project. [Pedro
  Rodrigues]

- Fixes https://github.com/seatgeek/thefuzz/issues/10 and correctly
  points to README.textile. [Pedro Rodrigues]

- Info on the pull request. [Pedro Rodrigues]

- Pullstat.us button. [Pedro Rodrigues]

- Fuzzywuzzy really needs better benchmarks. [Pedro Rodrigues]

- Moved tests and benchmarks out of the package. [Pedro Rodrigues]

- Report better ratio()s redundant import try. [Pedro Rodrigues]

- AssertGreater did not exist in python 2.4. [Pedro Rodrigues]

- Remove debug output. [Adam Cohen]

- Looks for python-Levenshtein package, and if present, uses that
  instead of difflib. 10x speedup if present. add benchmarks. [Adam
  Cohen]

- Add gitignore. [Adam Cohen]

- Fix a bug in WRatio, as well as an issue in full_process, which was
  failing on strings with all unicode characters. [Adam Cohen]

- Error in partial_ratio. closes #7. [Adam Cohen]

- Adding some real-life event data for benchmarking. [Adam Cohen]

- Cleaned up utils.py. [Pedro Rodrigues]

- Optimized speed for full_process() [Pedro Rodrigues]

- Speed improvements to asciidammit. [Pedro Rodrigues]

- Removed old versions of validate_string() and remove_ponctuation()
  kept from previous commits. [Pedro Rodrigues]

- Issue #6 from github updated license headers to match MIT license.
  [Pedro Rodrigues]

- Clean up. [Pedro Rodrigues]

- Changes to utils.validate_string() and benchmarks. [Pedro Rodrigues]

- Some benchmarks to test the changes made to remove_punctuation. [Pedro
  Rodrigues]

- Faster remove_punctuation. [Pedro Rodrigues]

- AssertIsNone did not exist in Python 2.4. [Pedro Rodrigues]

- Just adding some simple install instructions for pip. [Chris Dary]

- Check for null/empty strings in QRatio and WRatio. Add tests. Closes
  #3. [Adam Cohen]

- More README. [Adam Cohen]

- README. [Adam Cohen]

- README. [Adam Cohen]

- Slight change to README. [Adam Cohen]

- Some readme. [Adam Cohen]

- Distutils. [Adam Cohen]

- Change directory structure. [Adam Cohen]

- Initial commit. [Adam Cohen]



```

### `LICENSE.txt`

```txt
MIT License

Copyright (c) 2014 SeatGeek

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
include *.txt
include *.rst
include test_thefuzz.py

```

### `README.rst`

```rst
.. image:: https://github.com/seatgeek/thefuzz/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/seatgeek/thefuzz

TheFuzz
=======

Fuzzy string matching like a boss. It uses `Levenshtein Distance <https://en.wikipedia.org/wiki/Levenshtein_distance>`_ to calculate the differences between sequences in a simple-to-use package.

Requirements
============

-  Python 3.8 or higher
-  `rapidfuzz <https://github.com/maxbachmann/RapidFuzz/>`_

For testing
~~~~~~~~~~~
-  pycodestyle
-  hypothesis
-  pytest

Installation
============

Using pip via PyPI

.. code:: bash

    pip install thefuzz


Using pip via GitHub

.. code:: bash

    pip install git+git://github.com/seatgeek/thefuzz.git@0.19.0#egg=thefuzz

Adding to your ``requirements.txt`` file (run ``pip install -r requirements.txt`` afterwards)

.. code:: bash

    git+ssh://git@github.com/seatgeek/thefuzz.git@0.19.0#egg=thefuzz

Manually via GIT

.. code:: bash

    git clone git://github.com/seatgeek/thefuzz.git thefuzz
    cd thefuzz
    python setup.py install


Usage
=====

.. code:: python

    >>> from thefuzz import fuzz
    >>> from thefuzz import process

Simple Ratio
~~~~~~~~~~~~

.. code:: python

    >>> fuzz.ratio("this is a test", "this is a test!")
        97

Partial Ratio
~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.partial_ratio("this is a test", "this is a test!")
        100

Token Sort Ratio
~~~~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
        91
    >>> fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
        100

Token Set Ratio
~~~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
        84
    >>> fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
        100

Partial Token Sort Ratio
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.token_sort_ratio("fuzzy was a bear", "wuzzy fuzzy was a bear")
        84
    >>> fuzz.partial_token_sort_ratio("fuzzy was a bear", "wuzzy fuzzy was a bear")
        100

Process
~~~~~~~

.. code:: python

    >>> choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
    >>> process.extract("new york jets", choices, limit=2)
        [('New York Jets', 100), ('New York Giants', 78)]
    >>> process.extractOne("cowboys", choices)
        ("Dallas Cowboys", 90)

You can also pass additional parameters to ``extractOne`` method to make it use a specific scorer. A typical use case is to match file paths:

.. code:: python

    >>> process.extractOne("System of a down - Hypnotize - Heroin", songs)
        ('/music/library/good/System of a Down/2005 - Hypnotize/01 - Attack.mp3', 86)
    >>> process.extractOne("System of a down - Hypnotize - Heroin", songs, scorer=fuzz.token_sort_ratio)
        ("/music/library/good/System of a Down/2005 - Hypnotize/10 - She's Like Heroin.mp3", 61)

.. |Build Status| image:: https://github.com/seatgeek/thefuzz/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/seatgeek/thefuzz

```

### `release`

```
#!/usr/bin/env bash
set -eo pipefail; [[ $RELEASE_TRACE ]] && set -x

PACKAGE_NAME='thefuzz'
INIT_PACKAGE_NAME='thefuzz'
PUBLIC="true"

# Colors
COLOR_OFF="\033[0m"   # unsets color to term fg color
RED="\033[0;31m"      # red
GREEN="\033[0;32m"    # green
YELLOW="\033[0;33m"   # yellow
MAGENTA="\033[0;35m"  # magenta
CYAN="\033[0;36m"     # cyan

# ensure wheel is available
pip install wheel > /dev/null

# ensure Pygment is available
pip install Pygments > /dev/null

command -v gitchangelog >/dev/null 2>&1 || {
    echo -e "${RED}WARNING: Missing gitchangelog binary, please run: pip install gitchangelog==2.2.0${COLOR_OFF}\n"
    exit 1
}

command -v rst-lint > /dev/null || {
    echo -e "${RED}WARNING: Missing rst-lint binary, please run: pip install restructuredtext_lint${COLOR_OFF}\n"
    exit 1
}

set +e;
python test_thefuzz.py &> /dev/null  # run the tests
if [ ! $? -eq 0 ]; then
    echo -e "${RED}WARNING: The tests are failing.${COLOR_OFF}"
    exit 1
fi
set -e;

if [[ "$@" != "major" ]] && [[ "$@" != "minor" ]] && [[ "$@" != "patch" ]]; then
    echo -e "${RED}WARNING: Invalid release type, must specify 'major', 'minor', or 'patch'${COLOR_OFF}\n"
    exit 1
fi

echo -e "\n${GREEN}STARTING RELEASE PROCESS${COLOR_OFF}\n"

set +e;
git status | grep -Eo "working (directory|tree) clean" &> /dev/null
if [ ! $? -eq 0 ]; then # working directory is NOT clean
    echo -e "${RED}WARNING: You have uncommitted changes, you may have forgotten something${COLOR_OFF}\n"
    exit 1
fi
set -e;

echo -e "${YELLOW}--->${COLOR_OFF} Updating local copy"
git pull -q origin master
git fetch --tags > /dev/null

echo -e "${YELLOW}--->${COLOR_OFF} Retrieving release versions"

current_version=$(cat ${INIT_PACKAGE_NAME}/__init__.py |grep '__version__ ='|sed 's/[^0-9.]//g')
major=$(echo $current_version | awk '{split($0,a,"."); print a[1]}')
minor=$(echo $current_version | awk '{split($0,a,"."); print a[2]}')
patch=$(echo $current_version | awk '{split($0,a,"."); print a[3]}')

if [[ "$@" == "major" ]]; then
    major=$(($major + 1));
    minor="0"
    patch="0"
elif [[ "$@" == "minor" ]]; then
    minor=$(($minor + 1));
    patch="0"
elif [[ "$@" == "patch" ]]; then
    patch=$(($patch + 1));
fi

next_version="${major}.${minor}.${patch}"

echo -e  "${YELLOW}   >${COLOR_OFF} ${MAGENTA}${current_version}${COLOR_OFF} -> ${MAGENTA}${next_version}${COLOR_OFF}"

echo -e "${YELLOW}--->${COLOR_OFF} Ensuring readme passes lint checks (if this fails, run rst-lint)"
rst-lint README.rst > /dev/null

echo -e "${YELLOW}--->${COLOR_OFF} Creating necessary temp file"
tempfoo=$(basename $0)
TMPFILE=$(mktemp /tmp/${tempfoo}.XXXXXX) || {
    echo -e "${RED}WARNING: Cannot create temp file using mktemp in /tmp dir ${COLOR_OFF}\n"
    exit 1
}

find_this="__version__ = '$current_version'"
replace_with="__version__ = '$next_version'"

echo -e "${YELLOW}--->${COLOR_OFF} Updating ${INIT_PACKAGE_NAME}/__init__.py"
sed "s/$find_this/$replace_with/" ${INIT_PACKAGE_NAME}/__init__.py > $TMPFILE && mv $TMPFILE ${INIT_PACKAGE_NAME}/__init__.py

echo -e "${YELLOW}--->${COLOR_OFF} Updating README.rst"
find_this="${PACKAGE_NAME}.git@$current_version"
replace_with="${PACKAGE_NAME}.git@$next_version"
sed "s/$find_this/$replace_with/" README.rst > $TMPFILE && mv $TMPFILE README.rst
find_this="${PACKAGE_NAME}==$current_version"
replace_with="${PACKAGE_NAME}==$next_version"
sed "s/$find_this/$replace_with/" README.rst > $TMPFILE && mv $TMPFILE README.rst

if [ -f docs/conf.py ]; then
    echo -e "${YELLOW}--->${COLOR_OFF} Updating docs"
    find_this="version = '${current_version}'"
    replace_with="version = '${next_version}'"
    sed "s/$find_this/$replace_with/" docs/conf.py > $TMPFILE && mv $TMPFILE docs/conf.py

    find_this="release = '${current_version}'"
    replace_with="release = '${next_version}'"
    sed "s/$find_this/$replace_with/" docs/conf.py > $TMPFILE && mv $TMPFILE docs/conf.py
fi

echo -e "${YELLOW}--->${COLOR_OFF} Updating CHANGES.rst for new release"
version_header="$next_version ($(date +%F))"
set +e; dashes=$(yes '-'|head -n ${#version_header}|tr -d '\n') ; set -e
gitchangelog |sed "4s/.*/$version_header/"|sed "5s/.*/$dashes/" > $TMPFILE && mv $TMPFILE CHANGES.rst

echo -e "${YELLOW}--->${COLOR_OFF} Adding changed files to git"
git add CHANGES.rst README.rst ${INIT_PACKAGE_NAME}/__init__.py
if [ -f docs/conf.py ]; then git add docs/conf.py; fi

echo -e "${YELLOW}--->${COLOR_OFF} Creating release"
git commit -q -m "Release version $next_version"

echo -e "${YELLOW}--->${COLOR_OFF} Tagging release"
git tag -a $next_version -m "Release version $next_version"

echo -e "${YELLOW}--->${COLOR_OFF} Pushing release and tags to github"
git push -q origin master && git push -q --tags

if [[ "$PUBLIC" == "true" ]]; then
    echo -e "${YELLOW}--->${COLOR_OFF} Creating python release"
    cp README.rst README
    python setup.py sdist bdist_wheel upload > /dev/null
    rm README
else
    echo -e "${YELLOW}--->${COLOR_OFF} Creating local python dist and wheel for manual release"
    python setup.py sdist bdist_wheel > /dev/null
fi

echo -e "\n${CYAN}RELEASED VERSION ${next_version}${COLOR_OFF}\n"

```

### `requirements.txt`

```txt
rapidfuzz==3.4.0
pycodestyle==2.11.1
hypothesis==6.88.1
pytest==7.4.3
docutils==0.20.1
Pygments==2.16.1
wheel==0.41.3
setuptools==68.2.2
gitchangelog==3.0.4
restructuredtext_lint==1.4.0

```

### `setup.py`

```py
#!/usr/bin/env python

# Copyright (c) 2014 SeatGeek

# This file is part of thefuzz.

from thefuzz import __version__
from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='thefuzz',
    version=__version__,
    author='Adam Cohen',
    author_email='adam@seatgeek.com',
    packages=['thefuzz'],
    # keep for backwards compatibility of projects depending on `thefuzz[speedup]`
    extras_require={'speedup': []},
    install_requires=['rapidfuzz>=3.0.0, < 4.0.0'],
    url='https://github.com/seatgeek/thefuzz',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3 :: Only',
    ],
    description='Fuzzy string matching in python',
    long_description=long_description,
    zip_safe=True,
    python_requires='>=3.8'
)

```

### `test_thefuzz_hypothesis.py`

```py
from itertools import product
from functools import partial
from string import ascii_letters, digits, punctuation

from hypothesis import given, assume, settings, HealthCheck
import hypothesis.strategies as st
import pytest

from thefuzz import fuzz, process, utils


HYPOTHESIS_ALPHABET = ascii_letters + digits + punctuation


def scorers_processors():
    """
    Generate a list of (scorer, processor) pairs for testing

    :return: [(scorer, processor), ...]
    """
    scorers = [fuzz.ratio,
               fuzz.partial_ratio]
    processors = [lambda x: x,
                  partial(utils.full_process, force_ascii=False),
                  partial(utils.full_process, force_ascii=True)]
    splist = list(product(scorers, processors))
    splist.extend(
        [(fuzz.WRatio, partial(utils.full_process, force_ascii=True)),
         (fuzz.QRatio, partial(utils.full_process, force_ascii=True)),
         (fuzz.UWRatio, partial(utils.full_process, force_ascii=False)),
         (fuzz.UQRatio, partial(utils.full_process, force_ascii=False)),
         (fuzz.token_set_ratio, partial(utils.full_process, force_ascii=True)),
         (fuzz.token_sort_ratio, partial(utils.full_process, force_ascii=True)),
         (fuzz.partial_token_set_ratio, partial(utils.full_process, force_ascii=True)),
         (fuzz.partial_token_sort_ratio, partial(utils.full_process, force_ascii=True))]
    )

    return splist


def full_scorers_processors():
    """
    Generate a list of (scorer, processor) pairs for testing for scorers that use the full string only

    :return: [(scorer, processor), ...]
    """
    scorers = [fuzz.ratio]
    processors = [lambda x: x,
                  partial(utils.full_process, force_ascii=False),
                  partial(utils.full_process, force_ascii=True)]
    splist = list(product(scorers, processors))
    splist.extend(
        [(fuzz.WRatio, partial(utils.full_process, force_ascii=True)),
         (fuzz.QRatio, partial(utils.full_process, force_ascii=True)),
         (fuzz.UWRatio, partial(utils.full_process, force_ascii=False)),
         (fuzz.UQRatio, partial(utils.full_process, force_ascii=False))]
    )

    return splist


@pytest.mark.parametrize('scorer,processor',
                         scorers_processors())
@given(data=st.data())
@settings(max_examples=20, deadline=5000, suppress_health_check=[HealthCheck.data_too_large])
def test_identical_strings_extracted(scorer, processor, data):
    """
    Test that identical strings will always return a perfect match.

    :param scorer:
    :param processor:
    :param data:
    :return:
    """
    # Draw a list of random strings
    strings = data.draw(
        st.lists(
            st.text(min_size=10, max_size=100, alphabet=HYPOTHESIS_ALPHABET),
            min_size=1,
            max_size=10
        )
    )
    # Draw a random integer for the index in that list
    choiceidx = data.draw(st.integers(min_value=0, max_value=(len(strings) - 1)))

    # Extract our choice from the list
    choice = strings[choiceidx]

    # Check process doesn't make our choice the empty string
    assume(processor(choice) != '')

    # Extract all perfect matches
    result = process.extractBests(choice,
                                  strings,
                                  scorer=scorer,
                                  processor=processor,
                                  score_cutoff=100,
                                  limit=None)

    # Check we get a result
    assert result != []

    # Check the original is in the list
    assert (choice, 100) in result


@pytest.mark.parametrize('scorer,processor',
                         full_scorers_processors())
@given(data=st.data())
@settings(max_examples=20, deadline=5000)
def test_only_identical_strings_extracted(scorer, processor, data):
    """
    Test that only identical (post processing) strings score 100 on the test.

    If two strings are not identical then using full comparison methods they should
    not be a perfect (100) match.

    :param scorer:
    :param processor:
    :param data:
    :return:
    """
    # Draw a list of random strings
    strings = data.draw(
        st.lists(
            st.text(min_size=10, max_size=100, alphabet=HYPOTHESIS_ALPHABET),
            min_size=1,
            max_size=10)
    )
    # Draw a random integer for the index in that list
    choiceidx = data.draw(st.integers(min_value=0, max_value=(len(strings) - 1)))

    # Extract our choice from the list
    choice = strings[choiceidx]

    # Check process doesn't make our choice the empty string
    assume(processor(choice) != '')

    # Extract all perfect matches
    result = process.extractBests(choice,
                                  strings,
                                  scorer=scorer,
                                  processor=processor,
                                  score_cutoff=100,
                                  limit=None)

    # Check we get a result
    assert result != []

    # Check THE ONLY result(s) we get are a perfect match for the (processed) original data
    pchoice = processor(choice)
    for r in result:
        assert pchoice == processor(r[0])

```

### `test_thefuzz_pytest.py`

```py
from thefuzz import process


def test_process_warning(caplog):
    """Check that a string reduced to 0 by processor logs a warning to stderr"""

    query = ':::::::'
    choices = [':::::::']

    _ = process.extractOne(query, choices)

    logstr = ("Applied processor reduces "
              "input query to empty string, "
              "all comparisons will have score 0. "
              "[Query: ':::::::']")

    assert 1 == len(caplog.records)
    log = caplog.records[0]

    assert log.levelname == "WARNING"
    assert log.name == "thefuzz.process"
    assert logstr == log.message

```

### `test_thefuzz.py`

```py
import unittest
import re
import pycodestyle

from thefuzz import fuzz
from thefuzz import process
from thefuzz import utils

scorers = [
    fuzz.ratio,
    fuzz.partial_ratio,
    fuzz.token_sort_ratio,
    fuzz.token_set_ratio,
    fuzz.partial_token_sort_ratio,
    fuzz.partial_token_set_ratio,
    fuzz.QRatio,
    fuzz.UQRatio,
    fuzz.WRatio,
    fuzz.UWRatio,
]

class StringProcessingTest(unittest.TestCase):
    def test_replace_non_letters_non_numbers_with_whitespace(self):
        strings = ["new york mets - atlanta braves", "Cães danados",
                   "New York //// Mets $$$", "Ça va?"]
        for string in strings:
            proc_string = utils.full_process(string)
            regex = re.compile(r"(?ui)[\W]")
            for expr in regex.finditer(proc_string):
                self.assertEqual(expr.group(), " ")

    def test_dont_condense_whitespace(self):
        s1 = "new york mets - atlanta braves"
        s2 = "new york mets atlanta braves"
        s3 = "new york mets   atlanta braves"
        p1 = utils.full_process(s1)
        p2 = utils.full_process(s2)
        p3 = utils.full_process(s3)
        self.assertEqual(p1, s3)
        self.assertEqual(p2, s2)
        self.assertEqual(p3, s3)


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"
        self.mixed_strings = [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "C'est la vie",
            "Ça va?",
            "Cães danados",
            "\xacCamarões assados",
            "a\xac\u1234\u20ac\U00008000",
            "\u00C1"
        ]

    def tearDown(self):
        pass

    def test_ascii_only(self):
        for s in self.mixed_strings:
            utils.ascii_only(s)

    def test_fullProcess(self):
        for s in self.mixed_strings:
            utils.full_process(s)

    def test_fullProcessForceAscii(self):
        for s in self.mixed_strings:
            utils.full_process(s, force_ascii=True)


class RatioTest(unittest.TestCase):

    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"
        self.s7 = 'new york city mets - atlanta braves'
        # test silly corner cases
        self.s8 = '{'
        self.s8a = '{'
        self.s9 = '{a'
        self.s9a = '{a'
        self.s10 = 'a{'
        self.s10a = '{b'

        self.cirque_strings = [
            "cirque du soleil - zarkana - las vegas",
            "cirque du soleil ",
            "cirque du soleil las vegas",
            "zarkana las vegas",
            "las vegas cirque du soleil at the bellagio",
            "zarakana - cirque du soleil - bellagio"
        ]

        self.baseball_strings = [
            "new york mets vs chicago cubs",
            "chicago cubs vs chicago white sox",
            "philladelphia phillies vs atlanta braves",
            "braves vs mets",
        ]

    def tearDown(self):
        pass

    def testEqual(self):
        self.assertEqual(fuzz.ratio(self.s1, self.s1a), 100)
        self.assertEqual(fuzz.ratio(self.s8, self.s8a), 100)
        self.assertEqual(fuzz.ratio(self.s9, self.s9a), 100)

    def testCaseInsensitive(self):
        self.assertNotEqual(fuzz.ratio(self.s1, self.s2), 100)
        self.assertEqual(fuzz.ratio(utils.full_process(self.s1), utils.full_process(self.s2)), 100)

    def testPartialRatio(self):
        self.assertEqual(fuzz.partial_ratio(self.s1, self.s3), 100)

    def testTokenSortRatio(self):
        self.assertEqual(fuzz.token_sort_ratio(self.s1, self.s1a), 100)

    def testPartialTokenSortRatio(self):
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s1, self.s1a), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s4, self.s5), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s8, self.s8a, full_process=False), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s9, self.s9a, full_process=True), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s9, self.s9a, full_process=False), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s10, self.s10a, full_process=False), 67)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s10a, self.s10, full_process=False), 67)

    def testTokenSetRatio(self):
        self.assertEqual(fuzz.token_set_ratio(self.s4, self.s5), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s8, self.s8a, full_process=False), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s9, self.s9a, full_process=True), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s9, self.s9a, full_process=False), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s10, self.s10a, full_process=False), 50)

    def testPartialTokenSetRatio(self):
        self.assertEqual(fuzz.partial_token_set_ratio(self.s4, self.s7), 100)

    def testQuickRatioEqual(self):
        self.assertEqual(fuzz.QRatio(self.s1, self.s1a), 100)

    def testQuickRatioCaseInsensitive(self):
        self.assertEqual(fuzz.QRatio(self.s1, self.s2), 100)

    def testQuickRatioNotEqual(self):
        self.assertNotEqual(fuzz.QRatio(self.s1, self.s3), 100)

    def testWRatioEqual(self):
        self.assertEqual(fuzz.WRatio(self.s1, self.s1a), 100)

    def testWRatioCaseInsensitive(self):
        self.assertEqual(fuzz.WRatio(self.s1, self.s2), 100)

    def testWRatioPartialMatch(self):
        # a partial match is scaled by .9
        self.assertEqual(fuzz.WRatio(self.s1, self.s3), 90)

    def testWRatioMisorderedMatch(self):
        # misordered full matches are scaled by .95
        self.assertEqual(fuzz.WRatio(self.s4, self.s5), 95)

    def testWRatioStr(self):
        self.assertEqual(fuzz.WRatio(str(self.s1), str(self.s1a)), 100)

    def testQRatioStr(self):
        self.assertEqual(fuzz.WRatio(str(self.s1), str(self.s1a)), 100)

    def testEmptyStringsScore100(self):
        self.assertEqual(fuzz.ratio("", ""), 100)
        self.assertEqual(fuzz.partial_ratio("", ""), 100)

    def testIssueSeven(self):
        s1 = "HSINCHUANG"
        s2 = "SINJHUAN"
        s3 = "LSINJHUANG DISTRIC"
        s4 = "SINJHUANG DISTRICT"

        self.assertGreater(fuzz.partial_ratio(s1, s2), 75)
        self.assertGreater(fuzz.partial_ratio(s1, s3), 75)
        self.assertGreater(fuzz.partial_ratio(s1, s4), 75)

    def testRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzz.ratio(s1, s2)
        self.assertEqual(0, score)

    def testPartialRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzz.partial_ratio(s1, s2)
        self.assertEqual(0, score)

    def testWRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(0, score)

        # Cyrillic.
        s1 = "\u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433"
        s2 = "\u043f\u0441\u0438\u0445\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442"
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

        # Chinese.
        s1 = "\u6211\u4e86\u89e3\u6570\u5b66"
        s2 = "\u6211\u5b66\u6570\u5b66"
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

    def testQRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzz.QRatio(s1, s2)
        self.assertEqual(0, score)

        # Cyrillic.
        s1 = "\u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433"
        s2 = "\u043f\u0441\u0438\u0445\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442"
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

        # Chinese.
        s1 = "\u6211\u4e86\u89e3\u6570\u5b66"
        s2 = "\u6211\u5b66\u6570\u5b66"
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

    def testQratioForceAscii(self):
        s1 = "ABCD\u00C1"
        s2 = "ABCD"

        score = fuzz.QRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testQRatioForceAscii(self):
        s1 = "ABCD\u00C1"
        s2 = "ABCD"

        score = fuzz.WRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testPartialTokenSetRatioForceAscii(self):
        s1 = "ABCD\u00C1 HELP\u00C1"
        s2 = "ABCD HELP"

        score = fuzz.partial_token_set_ratio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzz.partial_token_set_ratio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testPartialTokenSortRatioForceAscii(self):
        s1 = "ABCD\u00C1 HELP\u00C1"
        s2 = "ABCD HELP"

        score = fuzz.partial_token_sort_ratio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzz.partial_token_sort_ratio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testCheckForNone(self):
        for scorer in scorers:
            self.assertEqual(scorer(None, None), 0)
            self.assertEqual(scorer('Some', None), 0)
            self.assertEqual(scorer(None, 'Some'), 0)

            self.assertNotEqual(scorer('Some', 'Some'), 0)

    def testCheckEmptyString(self):
        for scorer in scorers:
            if scorer in {fuzz.token_set_ratio, fuzz.partial_token_set_ratio, fuzz.WRatio, fuzz.UWRatio, fuzz.QRatio, fuzz.UQRatio}:
                self.assertEqual(scorer('', ''), 0)
            else:
                self.assertEqual(scorer('', ''), 100)

            self.assertEqual(scorer('Some', ''), 0)
            self.assertEqual(scorer('', 'Some'), 0)
            self.assertNotEqual(scorer('Some', 'Some'), 0)


class ProcessTest(unittest.TestCase):

    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"

        self.cirque_strings = [
            "cirque du soleil - zarkana - las vegas",
            "cirque du soleil ",
            "cirque du soleil las vegas",
            "zarkana las vegas",
            "las vegas cirque du soleil at the bellagio",
            "zarakana - cirque du soleil - bellagio"
        ]

        self.baseball_strings = [
            "new york mets vs chicago cubs",
            "chicago cubs vs chicago white sox",
            "philladelphia phillies vs atlanta braves",
            "braves vs mets",
        ]

    def testGetBestChoice1(self):
        query = "new york mets at atlanta braves"
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], "braves vs mets")

    def testGetBestChoice2(self):
        query = "philadelphia phillies at atlanta braves"
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[2])

    def testGetBestChoice3(self):
        query = "atlanta braves at philadelphia phillies"
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[2])

    def testGetBestChoice4(self):
        query = "chicago cubs vs new york mets"
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[0])

    def testWithProcessor(self):
        events = [
            ["chicago cubs vs new york mets", "CitiField", "2011-05-11", "8pm"],
            ["new york yankees vs boston red sox", "Fenway Park", "2011-05-11", "8pm"],
            ["atlanta braves vs pittsburgh pirates", "PNC Park", "2011-05-11", "8pm"],
        ]
        query = ["new york mets vs chicago cubs", "CitiField", "2017-03-19", "8pm"],

        best = process.extractOne(query, events, processor=lambda event: event[0])
        self.assertEqual(best[0], events[0])

    def testIssue57(self):
        """
        account for force_ascii
        """
        query = str(("test", "test"))
        choices = [("test", "test")]
        assert process.extract(query, choices)[0][1] == 100

    def testWithScorer(self):
        choices = [
            "new york mets vs chicago cubs",
            "chicago cubs at new york mets",
            "atlanta braves vs pittsbugh pirates",
            "new york yankees vs boston red sox"
        ]

        choices_dict = {
            1: "new york mets vs chicago cubs",
            2: "chicago cubs vs chicago white sox",
            3: "philladelphia phillies vs atlanta braves",
            4: "braves vs mets"
        }

        # in this hypothetical example we care about ordering, so we use quick ratio
        query = "new york mets at chicago cubs"
        scorer = fuzz.QRatio

        # first, as an example, the normal way would select the "more
        # 'complete' match of choices[1]"

        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

        # now, use the custom scorer

        best = process.extractOne(query, choices, scorer=scorer)
        self.assertEqual(best[0], choices[0])

        best = process.extractOne(query, choices_dict)
        self.assertEqual(best[0], choices_dict[1])

    def testWithCutoff(self):
        choices = [
            "new york mets vs chicago cubs",
            "chicago cubs at new york mets",
            "atlanta braves vs pittsbugh pirates",
            "new york yankees vs boston red sox"
        ]

        query = "los angeles dodgers vs san francisco giants"

        # in this situation, this is an event that does not exist in the list
        # we don't want to randomly match to something, so we use a reasonable cutoff

        best = process.extractOne(query, choices, score_cutoff=50)
        self.assertIsNone(best)

        # however if we had no cutoff, something would get returned

        # best = process.extractOne(query, choices)
        # self.assertIsNotNone(best)

    def testWithCutoff2(self):
        choices = [
            "new york mets vs chicago cubs",
            "chicago cubs at new york mets",
            "atlanta braves vs pittsbugh pirates",
            "new york yankees vs boston red sox"
        ]

        query = "new york mets vs chicago cubs"
        # Only find 100-score cases
        res = process.extractOne(query, choices, score_cutoff=100)
        self.assertIsNotNone(res)
        best_match, score = res
        self.assertIs(best_match, choices[0])

    def testEmptyStrings(self):
        choices = [
            "",
            "new york mets vs chicago cubs",
            "new york yankees vs boston red sox",
            "",
            ""
        ]

        query = "new york mets at chicago cubs"

        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

    def testNullStrings(self):
        choices = [
            None,
            "new york mets vs chicago cubs",
            "new york yankees vs boston red sox",
            None,
            None
        ]

        query = "new york mets at chicago cubs"

        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

    def test_list_like_extract(self):
        """We should be able to use a list-like object for choices."""
        def generate_choices():
            choices = ['a', 'Bb', 'CcC']
            yield from choices
        search = 'aaa'
        result = [(value, confidence) for value, confidence in
                  process.extract(search, generate_choices())]
        self.assertGreater(len(result), 0)

    def test_dict_like_extract(self):
        """We should be able to use a dict-like object for choices, not only a
        dict, and still get dict-like output.
        """
        try:
            from UserDict import UserDict
        except ImportError:
            from collections import UserDict
        choices = UserDict({'aa': 'bb', 'a1': None})
        search = 'aaa'
        result = process.extract(search, choices)
        self.assertGreater(len(result), 0)
        for value, confidence, key in result:
            self.assertIn(value, choices.values())

    def test_dedupe(self):
        """We should be able to use a list-like object for contains_dupes
        """
        # Test 1
        contains_dupes = ['Frodo Baggins', 'Tom Sawyer', 'Bilbo Baggin', 'Samuel L. Jackson', 'F. Baggins', 'Frody Baggins', 'Bilbo Baggins']

        result = process.dedupe(contains_dupes)
        self.assertLess(len(result), len(contains_dupes))

        # Test 2
        contains_dupes = ['Tom', 'Dick', 'Harry']

        # we should end up with the same list since no duplicates are contained in the list (e.g. original list is returned)
        deduped_list = ['Tom', 'Dick', 'Harry']

        result = process.dedupe(contains_dupes)
        self.assertEqual(result, deduped_list)

    def test_simplematch(self):
        basic_string = 'a, b'
        match_strings = ['a, b']

        result = process.extractOne(basic_string, match_strings, scorer=fuzz.ratio)
        part_result = process.extractOne(basic_string, match_strings, scorer=fuzz.partial_ratio)

        self.assertEqual(result, ('a, b', 100))
        self.assertEqual(part_result, ('a, b', 100))


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        pep8style = pycodestyle.StyleGuide(quiet=False)
        pep8style.options.ignore = pep8style.options.ignore + tuple(['E501'])
        pep8style.input_dir('thefuzz')
        result = pep8style.check_files()
        self.assertEqual(result.total_errors, 0, "PEP8 POLICE - WOOOOOWOOOOOOOOOO")

if __name__ == '__main__':
    unittest.main()         # run all tests

```

### `thefuzz/__init__.py`

```py
__version__ = '0.22.1'

```

### `thefuzz/fuzz.py`

```py
#!/usr/bin/env python

from rapidfuzz.fuzz import (
    ratio as _ratio,
    partial_ratio as _partial_ratio,
    token_set_ratio as _token_set_ratio,
    token_sort_ratio as _token_sort_ratio,
    partial_token_set_ratio as _partial_token_set_ratio,
    partial_token_sort_ratio as _partial_token_sort_ratio,
    WRatio as _WRatio,
    QRatio as _QRatio,
)

from . import utils

###########################
# Basic Scoring Functions #
###########################


def _rapidfuzz_scorer(scorer, s1, s2, force_ascii, full_process):
    """
    wrapper around rapidfuzz function to be compatible with the API of thefuzz
    """
    if full_process:
        if s1 is None or s2 is None:
            return 0

        s1 = utils.full_process(s1, force_ascii=force_ascii)
        s2 = utils.full_process(s2, force_ascii=force_ascii)

    return int(round(scorer(s1, s2)))


def ratio(s1, s2):
    return _rapidfuzz_scorer(_ratio, s1, s2, False, False)


def partial_ratio(s1, s2):
    """
    Return the ratio of the most similar substring
    as a number between 0 and 100.
    """
    return _rapidfuzz_scorer(_partial_ratio, s1, s2, False, False)


##############################
# Advanced Scoring Functions #
##############################

# Sorted Token
#   find all alphanumeric tokens in the string
#   sort those tokens and take ratio of resulting joined strings
#   controls for unordered string elements
def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
    """
    Return a measure of the sequences' similarity between 0 and 100
    but sorting the token before comparing.
    """
    return _rapidfuzz_scorer(_token_sort_ratio, s1, s2, force_ascii, full_process)


def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
    """
    Return the ratio of the most similar substring as a number between
    0 and 100 but sorting the token before comparing.
    """
    return _rapidfuzz_scorer(
        _partial_token_sort_ratio, s1, s2, force_ascii, full_process
    )


def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
    return _rapidfuzz_scorer(_token_set_ratio, s1, s2, force_ascii, full_process)


def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
    return _rapidfuzz_scorer(
        _partial_token_set_ratio, s1, s2, force_ascii, full_process
    )


###################
# Combination API #
###################

# q is for quick
def QRatio(s1, s2, force_ascii=True, full_process=True):
    """
    Quick ratio comparison between two strings.

    Runs full_process from utils on both strings
    Short circuits if either of the strings is empty after processing.

    :param s1:
    :param s2:
    :param force_ascii: Allow only ASCII characters (Default: True)
    :full_process: Process inputs, used here to avoid double processing in extract functions (Default: True)
    :return: similarity ratio
    """
    return _rapidfuzz_scorer(_QRatio, s1, s2, force_ascii, full_process)


def UQRatio(s1, s2, full_process=True):
    """
    Unicode quick ratio

    Calls QRatio with force_ascii set to False

    :param s1:
    :param s2:
    :return: similarity ratio
    """
    return QRatio(s1, s2, force_ascii=False, full_process=full_process)


# w is for weighted
def WRatio(s1, s2, force_ascii=True, full_process=True):
    """
    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.

    **Steps in the order they occur**

    #. Run full_process from utils on both strings
    #. Short circuit if this makes either string empty
    #. Take the ratio of the two processed strings (fuzz.ratio)
    #. Run checks to compare the length of the strings
        * If one of the strings is more than 1.5 times as long as the other
          use partial_ratio comparisons - scale partial results by 0.9
          (this makes sure only full results can return 100)
        * If one of the strings is over 8 times as long as the other
          instead scale by 0.6

    #. Run the other ratio functions
        * if using partial ratio functions call partial_ratio,
          partial_token_sort_ratio and partial_token_set_ratio
          scale all of these by the ratio based on length
        * otherwise call token_sort_ratio and token_set_ratio
        * all token based comparisons are scaled by 0.95
          (on top of any partial scalars)

    #. Take the highest value from these results
       round it and return it as an integer.

    :param s1:
    :param s2:
    :param force_ascii: Allow only ascii characters
    :type force_ascii: bool
    :full_process: Process inputs, used here to avoid double processing in extract functions (Default: True)
    :return:
    """
    return _rapidfuzz_scorer(_WRatio, s1, s2, force_ascii, full_process)


def UWRatio(s1, s2, full_process=True):
    """
    Return a measure of the sequences' similarity between 0 and 100,
    using different algorithms. Same as WRatio but preserving unicode.
    """
    return WRatio(s1, s2, force_ascii=False, full_process=full_process)

```

### `thefuzz/fuzz.pyi`

```pyi
def ratio(s1: str, s2: str) -> int: ...
def partial_ratio(s1: str, s2: str) -> int: ...
def token_sort_ratio(s1: str, s2: str, force_ascii: bool = ..., full_process: bool = ...) -> int: ...
def partial_token_sort_ratio(s1: str, s2: str, force_ascii: bool = ..., full_process: bool = ...) -> int: ...
def token_set_ratio(s1: str, s2: str, force_ascii: bool = ..., full_process: bool = ...) -> int: ...
def partial_token_set_ratio(s1: str, s2: str, force_ascii: bool = ..., full_process: bool = ...) -> int: ...
def QRatio(s1: str, s2: str, force_ascii: bool = ..., full_process: bool = ...) -> int: ...
def UQRatio(s1: str, s2: str, full_process: bool = ...) -> int: ...
def WRatio(s1: str, s2: str, force_ascii: bool = ..., full_process: bool = ...) -> int: ...
def UWRatio(s1: str, s2: str, full_process: bool = ...) -> int: ...

```

### `thefuzz/process.py`

```py
#!/usr/bin/env python
from . import fuzz
from . import utils
import logging
import typing as t
from rapidfuzz import fuzz as rfuzz
from rapidfuzz import process as rprocess
from functools import partial

_T = t.TypeVar("_T")
_Processor = t.Callable[[str], str]
_Scorer = t.Callable[[str, str], float]
_Choices = t.Iterable[str]
_ChoicesMap = t.Mapping[_T, str]
_Result = t.Tuple[str, float]
_MappedResult = t.Tuple[str, float, _T]

_logger = logging.getLogger(__name__)

default_scorer = fuzz.WRatio
default_processor = utils.full_process


def _get_processor(processor, scorer):
    """
    thefuzz runs both the default preprocessing of the function and the preprocessing
    function passed into process.* while rapidfuzz only runs the one passed into
    process.*. This function wraps the processor to mimic this behavior
    """
    if scorer not in (fuzz.WRatio, fuzz.QRatio,
                      fuzz.token_set_ratio, fuzz.token_sort_ratio,
                      fuzz.partial_token_set_ratio, fuzz.partial_token_sort_ratio,
                      fuzz.UWRatio, fuzz.UQRatio):
        return processor

    force_ascii = scorer not in [fuzz.UWRatio, fuzz.UQRatio]
    pre_processor = partial(utils.full_process, force_ascii=force_ascii)

    if not processor or processor == utils.full_process:
        return pre_processor

    def wrapper(s):
        return pre_processor(processor(s))

    return wrapper


# this allows lowering the scorers back to the scorers used in rapidfuzz
# this allows rapidfuzz to perform more optimizations behind the scenes.
# These mapped scorers are the same with two expceptions
# - default processor
# - result is not rounded
# these two exceptions need to be taken into account in the implementation
_scorer_lowering = {
    fuzz.ratio: rfuzz.ratio,
    fuzz.partial_ratio: rfuzz.partial_ratio,
    fuzz.token_set_ratio: rfuzz.token_set_ratio,
    fuzz.token_sort_ratio: rfuzz.token_sort_ratio,
    fuzz.partial_token_set_ratio: rfuzz.partial_token_set_ratio,
    fuzz.partial_token_sort_ratio: rfuzz.partial_token_sort_ratio,
    fuzz.WRatio: rfuzz.WRatio,
    fuzz.QRatio: rfuzz.QRatio,
    fuzz.UWRatio: rfuzz.WRatio,
    fuzz.UQRatio: rfuzz.QRatio,
}


def _get_scorer(scorer):
    """
    rapidfuzz scorers require the score_cutoff argument to be available
    This generates a compatible wrapper function
    """
    def wrapper(s1, s2, score_cutoff=0):
        return scorer(s1, s2)

    return _scorer_lowering.get(scorer, wrapper)


def _validate_query_preprocessing(query, processor):
    if processor:
        processed_query = processor(query)
        if len(processed_query) == 0:
            _logger.warning("Applied processor reduces input query to empty string, "
                            "all comparisons will have score 0. "
                            f"[Query: \'{query}\']")


@t.overload
def extractWithoutOrder(
    query: str,
    choices: _ChoicesMap[_T],
    processor: t.Optional[_Processor] = ...,
    scorer: _Scorer = ...,
    score_cutoff: t.Optional[float] = ...,
) -> t.Iterator[_MappedResult[_T]]:
    ...


@t.overload
def extractWithoutOrder(
    query: str,
    choices: _Choices,
    processor: t.Optional[_Processor] = ...,
    scorer: _Scorer = ...,
    score_cutoff: t.Optional[float] = ...,
) -> t.Iterator[_Result]:
    ...


def extractWithoutOrder(
    query: str,
    choices: t.Union[_ChoicesMap[_T], _Choices],
    processor: t.Optional[_Processor] = default_processor,
    scorer: _Scorer = default_scorer,
    score_cutoff: t.Optional[float] = 0,
) -> t.Union[t.Iterator[_MappedResult[_T]], t.Iterator[_Result]]:
    """
    Select the best match in a list or dictionary of choices.

    Find best matches in a list or dictionary of choices, return a
    generator of tuples containing the match and its score. If a dictionary
    is used, also returns the key for each match.

    Arguments:
        query: An object representing the thing we want to find.
        choices: An iterable or dictionary-like object containing choices
            to be matched against the query. Dictionary arguments of
            {key: value} pairs will attempt to match the query against
            each value.
        processor: Optional function of the form f(a) -> b, where a is the query or
            individual choice and b is the choice to be used in matching.

            This can be used to match against, say, the first element of
            a list:

            lambda x: x[0]

            Defaults to thefuzz.utils.full_process().
        scorer: Optional function for scoring matches between the query and
            an individual processed choice. This should be a function
            of the form f(query, choice) -> int.

            By default, fuzz.WRatio() is used and expects both query and
            choice to be strings.
        score_cutoff: Optional argument for score threshold. No matches with
            a score less than this number will be returned. Defaults to 0.

    Returns:
        Generator of tuples containing the match and its score.

        If a list is used for choices, then the result will be 2-tuples.
        If a dictionary is used, then the result will be 3-tuples containing
        the key for each match.

        For example, searching for 'bird' in the dictionary

        {'bard': 'train', 'dog': 'man'}

        may return

        ('train', 22, 'bard'), ('man', 0, 'dog')
    """
    is_mapping = hasattr(choices, "items")
    is_lowered = scorer in _scorer_lowering

    _validate_query_preprocessing(query, processor)
    it = rprocess.extract_iter(
        query, choices,
        processor=_get_processor(processor, scorer),
        scorer=_get_scorer(scorer),
        score_cutoff=score_cutoff
    )

    for choice, score, key in it:
        if is_lowered:
            score = int(round(score))

        yield (choice, score, key) if is_mapping else (choice, score)


@t.overload
def extract(
    query: str,
    choices: _ChoicesMap[_T],
    processor: t.Optional[_Processor] = ...,
    scorer: _Scorer = ...,
    limit: t.Optional[float] = ...,
) -> t.List[_MappedResult[_T]]:
    ...


@t.overload
def extract(
    query: str,
    choices: t.Iterable[str],
    processor: t.Optional[_Processor] = ...,
    scorer: _Scorer = ...,
    limit: t.Optional[float] = ...,
) -> t.List[_Result]:
    ...


def extract(
    query: str,
    choices: t.Union[_ChoicesMap[_T], _Choices],
    processor: t.Optional[_Processor] = default_processor,
    scorer: _Scorer = default_scorer,
    limit: t.Optional[float] = 5,
) -> t.Union[t.List[_MappedResult[_T]], t.List[_Result]]:
    """
    Select the best match in a list or dictionary of choices.

    Find best matches in a list or dictionary of choices, return a
    list of tuples containing the match and its score. If a dictionary
    is used, also returns the key for each match.

    Arguments:
        query: An object representing the thing we want to find.
        choices: An iterable or dictionary-like object containing choices
            to be matched against the query. Dictionary arguments of
            {key: value} pairs will attempt to match the query against
            each value.
        processor: Optional function of the form f(a) -> b, where a is the query or
            individual choice and b is the choice to be used in matching.

            This can be used to match against, say, the first element of
            a list:

            lambda x: x[0]

            Defaults to thefuzz.utils.full_process().
        scorer: Optional function for scoring matches between the query and
            an individual processed choice. This should be a function
            of the form f(query, choice) -> int.
            By default, fuzz.WRatio() is used and expects both query and
            choice to be strings.
        limit: Optional maximum for the number of elements returned. Defaults
            to 5.

    Returns:
        List of tuples containing the match and its score.

        If a list is used for choices, then the result will be 2-tuples.
        If a dictionary is used, then the result will be 3-tuples containing
        the key for each match.

        For example, searching for 'bird' in the dictionary

        {'bard': 'train', 'dog': 'man'}

        may return

        [('train', 22, 'bard'), ('man', 0, 'dog')]
    """
    return extractBests(query, choices, processor=processor, scorer=scorer, limit=limit)


@t.overload
def extractBests(
    query: str,
    choices: _ChoicesMap[_T],
    processor: t.Optional[_Processor] = ...,
    scorer: _Scorer = ...,
    score_cutoff: t.Optional[float] = ...,
    limit: t.Optional[float] = ...,
) -> t.List[_MappedResult[_T]]:
    ...


@t.overload
def extractBests(
    query: str,
    choices: t.Iterable[str],
    processor: t.Optional[_Processor] = ...,
    scorer: _Scorer = ...,
    score_cutoff: t.Optional[float] = ...,
    limit: t.Optional[int] = ...,
) -> t.List[_Result]:
    ...


def extractBests(
    query: str,
    choices: t.Union[_ChoicesMap[_T], _Choices],
    processor: t.Optional[_Processor] = default_processor,
    scorer: _Scorer = default_scorer,
    score_cutoff: t.Optional[float] = 0,
    limit: t.Optional[float] = 5,
) -> t.Union[t.List[_MappedResult[_T]], t.List[_Result]]:
    """
    Get a list of the best matches to a collection of choices.

    Convenience function for getting the choices with best scores.

    Args:
        query: A string to match against
        choices: A list or dictionary of choices, suitable for use with
            extract().
        processor: Optional function for transforming choices before matching.
            See extract().
        scorer: Scoring function for extract().
        score_cutoff: Optional argument for score threshold. No matches with
            a score less than this number will be returned. Defaults to 0.
        limit: Optional maximum for the number of elements returned. Defaults
            to 5.

    Returns: A a list of (match, score) tuples.
    """
    is_mapping = hasattr(choices, "items")
    is_lowered = scorer in _scorer_lowering

    _validate_query_preprocessing(query, processor)
    results = rprocess.extract(
        query, choices,
        processor=_get_processor(processor, scorer),
        scorer=_get_scorer(scorer),
        score_cutoff=score_cutoff,
        limit=limit
    )

    for i, (choice, score, key) in enumerate(results):
        if is_lowered:
            score = int(round(score))

        results[i] = (choice, score, key) if is_mapping else (choice, score)

    return results


@t.overload
def extractOne(
    query: str,
    choices: _ChoicesMap[_T],
    procprocessor: t.Optional[_Processor] = ...,
    scorer: _Scorer = ...,
    score_cutoff: t.Optional[float] = ...,
) -> t.Optional[_MappedResult[_T]]:
    ...


@t.overload
def extractOne(
    query: str,
    choices: t.Iterable[str],
    procprocessor: t.Optional[_Processor] = ...,
    scorer: _Scorer = ...,
    score_cutoff: t.Optional[float] = ...,
) -> t.Optional[_Result]:
    ...


def extractOne(
    query: str,
    choices: t.Union[_ChoicesMap[_T], _Choices],
    processor: t.Optional[_Processor] = default_processor,
    scorer: _Scorer = default_scorer,
    score_cutoff: t.Optional[float] = 0,
) -> t.Optional[t.Union[_MappedResult[_T], _Result]]:
    """
    Find the single best match above a score in a list of choices.

    This is a convenience method which returns the single best choice.
    See extract() for the full arguments list.

    Args:
        query: A string to match against
        choices: A list or dictionary of choices, suitable for use with
            extract().
        processor: Optional function for transforming choices before matching.
            See extract().
        scorer: Scoring function for extract().
        score_cutoff: Optional argument for score threshold. If the best
            match is found, but it is not greater than this number, then
            return None anyway ("not a good enough match").  Defaults to 0.

    Returns:
        A tuple containing a single match and its score, if a match
        was found that was above score_cutoff. Otherwise, returns None.
    """
    is_mapping = hasattr(choices, "items")
    is_lowered = scorer in _scorer_lowering

    _validate_query_preprocessing(query, processor)
    res = rprocess.extractOne(
        query, choices,
        processor=_get_processor(processor, scorer),
        scorer=_get_scorer(scorer),
        score_cutoff=score_cutoff
    )

    if res is None:
        return res

    choice, score, key = res

    if is_lowered:
        score = int(round(score))

    return (choice, score, key) if is_mapping else (choice, score)


_TC = t.TypeVar("_TC", bound=t.Collection[str])


def dedupe(
    contains_dupes: _TC,
    threshold: float = 70,
    scorer: _Scorer = fuzz.token_set_ratio,
) -> t.Union[t.List[str], _TC]:
    """
    This convenience function takes a list of strings containing duplicates and uses fuzzy matching to identify
    and remove duplicates. Specifically, it uses process.extract to identify duplicates that
    score greater than a user defined threshold. Then, it looks for the longest item in the duplicate list
    since we assume this item contains the most entity information and returns that. It breaks string
    length ties on an alphabetical sort.

    Note: as the threshold DECREASES the number of duplicates that are found INCREASES. This means that the
        returned deduplicated list will likely be shorter. Raise the threshold for dedupe to be less
        sensitive.

    Args:
        contains_dupes: A list of strings that we would like to dedupe.
        threshold: the numerical value (0,100) point at which we expect to find duplicates.
            Defaults to 70 out of 100
        scorer: Optional function for scoring matches between the query and
            an individual processed choice. This should be a function
            of the form f(query, choice) -> int.
            By default, fuzz.token_set_ratio() is used and expects both query and
            choice to be strings.

    Returns:
        A deduplicated list. For example:

            In: contains_dupes = ['Frodo Baggin', 'Frodo Baggins', 'F. Baggins', 'Samwise G.', 'Gandalf', 'Bilbo Baggins']
            In: dedupe(contains_dupes)
            Out: ['Frodo Baggins', 'Samwise G.', 'Bilbo Baggins', 'Gandalf']
    """
    deduped = set()
    for item in contains_dupes:
        matches = extractBests(item, contains_dupes, scorer=scorer, score_cutoff=threshold, limit=None)
        deduped.add(max(matches, key=lambda x: (len(x[0]), x[0]))[0])

    return list(deduped) if len(deduped) != len(contains_dupes) else contains_dupes

```

### `thefuzz/py.typed`

```typed


```

### `thefuzz/utils.py`

```py
from rapidfuzz.utils import default_process as _default_process

translation_table = {i: None for i in range(128, 256)}  # ascii dammit!


def ascii_only(s):
    return s.translate(translation_table)


def full_process(s, force_ascii=False):
    """
    Process string by
    -- removing all but letters and numbers
    -- trim whitespace
    -- force to lower case
    if force_ascii == True, force convert to ascii
    """

    if force_ascii:
        s = ascii_only(str(s))

    return _default_process(s)

```

### `thefuzz/utils.pyi`

```pyi

def ascii_only(s: str) -> str: ...
def full_process(s: str, force_ascii: bool = ...) -> str: ...

```

### `tox.ini`

```ini
[tox]
envlist = py{38, 39, 310, 311, 312, py3}
skip_missing_interpreters = True

[testenv]
deps = pytest
       pycodestyle
       hypothesis
commands = pytest

```
