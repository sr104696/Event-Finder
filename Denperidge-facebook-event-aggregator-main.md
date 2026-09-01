# Denperidge/facebook-event-aggregator@main

- Files included: 46
- Files skipped: 3
- Total size: 65.0 KB
- Estimated tokens: ~16,628

## Directory Structure

```
├── .github
│   └── workflows
│       ├── publish-docker.yml
│       ├── publish-pypi.yml
│       └── tests.yml
├── src
│   ├── facebook_event_aggregator
│   │   ├── export
│   │   │   ├── templates
│   │   │   │   ├── base.css
│   │   │   │   ├── base.html
│   │   │   │   ├── index.html
│   │   │   │   ├── index.js
│   │   │   │   └── workaround.py
│   │   │   ├── __init__.py
│   │   │   ├── to_html.py
│   │   │   ├── to_ics.py
│   │   │   └── utils.py
│   │   ├── scraper
│   │   │   ├── __init__.py
│   │   │   ├── driver.py
│   │   │   ├── fb_login.py
│   │   │   ├── scrape_all.py
│   │   │   ├── scrape_event_page.py
│   │   │   ├── scrape_events_page.py
│   │   │   └── utils.py
│   │   ├── utils
│   │   │   ├── fb_regexes.py
│   │   │   └── url_converter.py
│   │   ├── __main__.py
│   │   ├── Event.py
│   │   └── repo.py
│   ├── tests
│   │   ├── export
│   │   │   ├── __init__.py
│   │   │   ├── helpers.py
│   │   │   ├── test_export_html.py
│   │   │   ├── test_export_ics.py
│   │   │   └── test_utils.py
│   │   ├── scraper
│   │   │   ├── event_page.htm
│   │   │   ├── events_page.htm
│   │   │   └── test_scrape.py
│   │   ├── utils
│   │   │   ├── __init__.py
│   │   │   ├── test_fb_regexes.py
│   │   │   └── test_url_converter.py
│   │   ├── __init__.py
│   │   ├── test_Event.py
│   │   └── test_repo.py
│   └── __init__.py
├── .env.example
├── .gitignore
├── coverage.svg
├── Dockerfile
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
├── requirements-test.txt
└── requirements.txt
```

## Code Digest

### `.env.example`

```example
pages=[["community", "https://www.facebook.com/ID/events/?ref=page_internal"], ["page", "https://www.facebook.com/ID/upcoming_hosted_events"]]
title=Facebook Events
domain=https://domain.example.com
fb_locale=en-gb
auto_pull=True
tz=Europe/London

```

### `.github/workflows/publish-docker.yml`

```yml
name: Publish to Docker

on:
  push:
    tags:
      - "*"

  workflow_dispatch:

jobs:
  tests:
    uses: ./.github/workflows/tests.yml

  publish-docker:
      runs-on: ubuntu-latest
      needs:
        - tests

      steps:
        - name: Checkout
          uses: actions/checkout@v3

        - name: Login to Docker Hub
          uses: docker/login-action@v3
          with:
            username: ${{ secrets.DOCKERHUB_USERNAME }}
            password: ${{ secrets.DOCKERHUB_TOKEN }}
      
        - name: Set up Docker Buildx
          uses: docker/setup-buildx-action@v3

        - name: Build and push
          uses: docker/build-push-action@v5
          with:
            context: .
            push: true
            tags: ${{ secrets.DOCKERHUB_USERNAME }}/facebook-event-aggregator:latest , ${{ secrets.DOCKERHUB_USERNAME }}/facebook-event-aggregator:${{github.ref_name}}

```

### `.github/workflows/publish-pypi.yml`

```yml
name: Publish to PyPI

on:
  push:
    tags:
      - "*"

  workflow_dispatch:

jobs:
  tests:
    uses: ./.github/workflows/tests.yml

  build-and-publish-pypi:
    needs:
      - tests
    
    runs-on: ubuntu-latest
  
    permissions:
      id-token: write  # IMPORTANT: mandatory for trusted publishing

    environment:
      name: pypi
      url: https://pypi.org/p/facebook-event-aggregator
    
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Use Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10' 
      
      - name: Install requirements
        run: make install
  
      - name: Install build requirements
        run: python3 -m pip install --upgrade build setuptools

      - name: Build
        run: python3 -m build
 
      - name: Publish package distributions to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1

```

### `.github/workflows/tests.yml`

```yml
name: Run tests

on:
  push:
  workflow_call:
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Use Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10' 
            
      - name: Prepare venv
        run: make
        
      - name: Install (test) requirements
        run: make install-test
  
      - name: Run tests
        run: make test

```

### `.gitignore`

```gitignore
node_modules
.env
.venv
public/
__pycache__
geckodriver.log
.pytest_cache

.coverage

*.egg-info
dist/
```

### `Dockerfile`

```
FROM selenium/standalone-chrome:latest

WORKDIR /src/src/app

RUN sudo apt-get update
RUN sudo apt-get install -y git python3.11 python3-pip

COPY requirements.txt ./
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3.11", "-m", "src.facebook_event_aggregator"]
```

### `LICENSE`

```
MIT License

Copyright (c) 2022 Denperidge

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

### `Makefile`

```
.ONESHELL:
all: .venv install

.venv:
	python -m venv .venv

.PHONY: install
install:
	.venv/bin/pip install -r requirements.txt

.PHONY: install-test
install-test:
	.venv/bin/pip install -r requirements.txt -r requirements-test.txt

.PHONY: test
test:
	.venv/bin/python -m pytest
	.venv/bin/python -m coverage_badge -fo coverage.svg

```

### `pyproject.toml`

```toml
[project]
name = "facebook_event_aggregator"
version = "0.1.21"
authors = [
    { name="Denperidge", email="denperidge@gmail.com" },
]
description = ""
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "python-slugify >= 7.0.0",
    "python_dateutil >= 2.8.2",
    "gitpython >= 3.1.40",
    "webdriver_manager >= 4.0.1",
    "selenium >= 4.15.2",
    "ics >= 0.7.2",
    "Jinja2 >= 3.1.2",
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
]

[project.urls]
"Homepage" = "https://github.com/Denperidge/facebook-event-aggregator"
"Bug Tracker" = "https://github.com/Denperidge/facebook-event-aggregator/issues"

[project.scripts]
facebook_event_aggregator = "facebook_event_aggregator.__main__:cli"
f_a_e = "facebook_event_aggregator.__main__:cli"

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
htmlexport = ["*.html", "*.css", "*.js"]

[tool.pytest.ini_options]
addopts = "--cov=src/facebook_event_aggregator --cov-report term-missing"

[tool.coverage.report]
omit = [
    "driver.py",  # selenium doesn't export options, and the other code is platform dependant
    "fb_login.py",  # Currently unimplemented
]
```

### `README.md`

```md
# Facebook Event Aggregator

![The coverage badge](coverage.svg)

A Facebook event scraper & aggregator, that fetches multiple pages' events and exports them to a static website and .ics file, automatically pushing it to Git(Hub Pages).

If you're looking for the original script-based version, check out the [archive-before-rework branch](https://github.com/Denperidge/facebook-event-aggregator/tree/archive-before-package-rework)

## How-to guides
### Usage
#### Run using Docker
Pre-requisites: Docker

```bash
docker run -i denperidge/facebook-event-aggregator --host-domain ...
```

#### Install & run using pip
Pre-requisites: >= py3.10, pip

> Before running, make sure to follow the [installing chromedriver instructions](#installing-chromedriver)

```bash
python -m pip install --upgrade facebook-event-aggregator
```

#### Install & run using pipx
Pre-requisites: pipx

> Before running, make sure to follow the [installing chromedriver instructions](#installing-chromedriver)

```bash
pipx run facebook-event-aggregator --help
```

#### Install & run using a local clone
Pre-requisites: >= py3.10, pip, git

> Before running, make sure to follow the [installing chromedriver instructions](#installing-chromedriver)

```bash
# Clone locally
git clone https://github.com/Denperidge/facebook-event-aggregator.git
cd facebook-event-aggregator

# Create venv & install requirements
python -m venv .venv
.venv/bin/pip install -r requirements.txt

# Run facebook event aggregator
. .venv/bin/activate
python -m src.facebook_event_aggregator --host-domain ...
```
> NOTE: Your shell or operating system might have a different method for activating the venv

> Alternatively, you can create the venv & install dependencies using `make`. *(Using make to run the application is not supported due to the lack of direct command line arguments)*

### Installing chromedriver
- If running on a distro supporting rpm/yum, use
    - `yum install google-chrome` (keep note of what version is installed)
    - `cd /usr/local/bin/`
    - `npx @puppeteer/browsers install chromedriver@121` (ensure the @VERSION is the same major version as yum installed)
- If running on a platform without an official Chromium distrubition (e.g. Raspberry Pi 3b, Linux32...): `apt-get install chromium-chromedriver`

### Configure git
<details>
    <summary>Don't forget to configure Git on the device if that's not done already!</summary>
    ```bash
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    ``` 
</details>

### Run tests
```bash
# Clone locally
git clone https://github.com/Denperidge/facebook-event-aggregator.git
cd facebook-event-aggregator

# Create venv & install requirements
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt -r requirements-test.txt

# Run tests
. .venv/bin/activate
pytest && python -m coverage_badge -fo coverage.svg
```
> Alternatively, use `make install-test` & `make test`

### Crontab (WIP)
```bash
echo "Optionally, add the following line to crontab to automatically run every 24 hours (can be modified ofcourse): "
# echo "0 5 * * * python3 \"$(pwd)/app/main.py\" headless update"
```
See also [crontab guru](https://crontab.guru/)!


## Reference
### Maintaining/troubleshooting
This application is made to be as platform-agnostic as possible. However, the weak link is in the Facebook scraping. The parse_* functions in [src/facebook_event_aggregator/scraper/](src/facebook_event_aggregator/scraper/) are most likely to need changes down the line. So if the application doesn't find any events, look there first.

Make sure to run the `pipreqs` command if any modules get added to a python file.
(Note: pipreqs seems to have some issues with the match statement. If that's still the case, comment those lines out before running)

## Discussions
### GitHub Actions & why this application shouldn't be run on it & why you probably don't want to use a logged in Facebook session
Besides the hosting through GitHub Pages, everything is done locally. If you look in the branches, you'll notice an old entirely GitHub Actions based version. However, doing it locally avoids the login sequence that Facebook asks when this is run from GitHub Actions (presumably due to rate limiting). The non-logged in Facebook interface is easier to scrape, presumably due to GraphQL (although that might be incorrect).


### Structure (out of date)
- [app/](app/) - All code (Python and otherwise) here
    - [export/](app/scrape_and_parse/) - Everything concerning turning the Event objects into viewable data
        - [templates/](app/export/templates/) - Jinja templates used to render the static website
        - [to_html.py](app/export/to_html.py) - Code that implements the above Jinja templates to create public/index.html
        - [to_ics.py](app/export/to_ics.py) - Code that turns Event objects into (a) .ics file(s)
    - [scrape_and_parse/](app/scrape_and_parse/) - Everything concerning scraping information into JSON & Event objects
        - [driver.py](app/scrape_and_parse/driver.py) - Selenium Driver settings (selected browser, startup args...)
        - [fb_login.py](app/scrape_and_parse/fb_login.py) - Handles logging into Facebook
        - [locale.py](app/scrape_and_parse/locale.py) - Handles converting www.facebook to lang-country.facebook and back
        - [regex.py](app/scrape_and_parse/regex.py) - Includes regex patterns and functions to use them
        - [scrape_and_parse.py](app/scrape_and_parse/scrape_and_parse.py) - Handles the actual scraping & parsing part
    - [Event.py](app/Event.py) - Python Class to handle Events
    - [main.py](app/main.py) - Entrypoint that combines everything into one script
    - [repo.py](app/repo.py) - Handles the upkeep of the repo within public/
- public/ - Generated at runtime, contains the end result/exported files
- [requirements.txt](requirements.txt) - Python packages that have to be installed


## License
All the code written by me in this repository is licensed under the [MIT License](LICENSE).

```

### `requirements-test.txt`

```txt
pytest==8.3.4
pytest-cov==6.0.0
coverage-badge==1.1.2

```

### `requirements.txt`

```txt
python-slugify==7.0.0
python_dateutil==2.8.2
gitpython==3.1.40
webdriver_manager==4.0.1
selenium==4.15.2
ics==0.7.2
Jinja2==3.1.2

```

### `src/__init__.py`

```py

```

### `src/facebook_event_aggregator/__main__.py`

```py
# Built-in imports
from sys import argv, executable
from os import makedirs, getenv, execv, getcwd
from os.path import realpath, join, abspath, dirname
from pathlib import Path
from json import dump, load
from argparse import ArgumentParser

# Local imports
from .repo import clone_or_pull_repo, update_repo
from .Event import load_events_from_json, events_to_json
from .export import events_to_html, events_to_ics, cleanup_images

from .scraper import setup_driver, scrape_all


argparse = ArgumentParser()
argparse.add_argument("--target", "-t", nargs="+", help="Facebook page to extract from. Usage: --target https://www.facebook.com/trixonline/ --target https://www.facebook.com/botaniquebxl/")
argparse.add_argument("--update", "-u", action="store_true", help="Whether to push to Git")
argparse.add_argument("--scrape", "-s", action="store_true", help="Whether to run scraper (alternatively, load from cache)")
argparse.add_argument("--chromedriver-path", "--cp", default=None, help="Path to chromedriver. For example, using chromium-chromedriver, this would be /usr/lib/chromium-browser/chromedriver")

argparse.add_argument("--host-domain", "--hd", required=True, help="Domain where your files will be hosted. E.g. https://example.com")
argparse.add_argument("--timezone", "--tz", default="Europe/London", help="What timezone to use for ics events")
argparse.add_argument("--title", default="Title", help="What title to use for the html export")

argparse.add_argument("--repo", "--repo-url", required=True, help="Domain where your files will be hosted. E.g. https://example.com")

argparse.add_argument("--remote-debugging-port", "--rdp", default=0, help="(Troubleshooting) Set Chrome debugging port. Default value: 0")
argparse.add_argument("--extra-opts", "--eo", default=[], nargs="*", help="(Troubleshooting) Set Selenium args. '--' gets prepended automatically and shouldn't be passed. Default value: []")

def cli():
    args = argparse.parse_args()
    print(args)

    cwd = Path.cwd()
    export_dir = cwd.joinpath("public/")
    events_json_path = export_dir.joinpath("events.json") 
    img_dir = export_dir.joinpath("img/")
    


    #events_json = join(public_dir, "events.json")

    # Load .env file and startup params
    #startup_args = [arg.lower() for arg in argv[1:]]
    #headless = "headless" in startup_args
    #update = "update" in startup_args
    #scrape = "noscrape" not in startup_args
    scrape = args.scrape
    headless = True

    
    # Clone repo into public/
    clone_or_pull_repo(parent_dir_path=str(cwd), clone_dirname="public", repo_url=args.repo)
    makedirs(str(img_dir), exist_ok=True)

    if scrape:
        # Prepare img_dir in case it's needed

        # Setup Selenium scraper
        driver = setup_driver(args.chromedriver_path, headless, args.remote_debugging_port, extra_opts=args.extra_opts)

        # Scrape events
        events = scrape_all(driver, args.target, str(img_dir))
    else:
        events = load_events_from_json(events_json_path)
                

    
    # Export
    if scrape:
        events_to_json(events, str(events_json_path))

    events_to_ics(events, str(export_dir))
    events_to_html(
        events=events,
        output_dir=str(export_dir),
        absolute_img_dir=str(img_dir),
        relative_from_html_img_dir="public/",
        host_domain=args.host_domain,
        page_urls=args.target,
        timezone=args.timezone,
        title=args.title)
    cleanup_images(events, str(img_dir))

    if args.update:
        update_repo(parent_dir_path=str(cwd), clone_dirname="public")

    # Cleanup
    if scrape:
        driver.quit()
            
if __name__ == "__main__":
    cli()
```

### `src/facebook_event_aggregator/Event.py`

```py
"""An Event """

# Built-in imports
from copy import deepcopy
from json import load, dump
from os.path import join, basename
from glob import glob
from re import match, RegexFlag

# Package imports
from datetime import timedelta, datetime
from dateutil import parser
from slugify import slugify

# Local imports
from .utils.url_converter import facebook_locale_to_www

class Event(object):
    """
    name = str
    datetime = date
    url = str
    """


    def __init__(self, name: str, datetime_param: str, source: str, location: str , url: str):
        self.name = name
        # Replacement due to bug ? https://github.com/dateutil/dateutil/issues/70#issuecomment-945080282
        try:
            # TODO better replacer using regex
            self.datetime = parser.parse(datetime_param.replace("UTC", "").replace(",", "").replace("MON", "").replace("TUES", "").replace("WED", "").replace("THURS", "").replace("FRI", "").replace("SAT", "").replace("SUN", ""))
        except parser.ParserError:
            print("Couldn't parse " + datetime_param)
            self.datetime = datetime.now()
        self.location = location
        self.url = url
        self.source: str = source
    
    # Thanks to https://stackoverflow.com/a/682545 & https://www.programiz.com/python-programming/methods/built-in/classmethod
    @classmethod
    def from_dict(cls, dict):
        return cls(
            name=dict["name"], 
            datetime_param=dict["datetime"],
            source=dict["source"],
            location=dict["location"],
            url=dict["url"]
            )
    
    
    def to_json(self):
        serializable_event = deepcopy(self)
        serializable_event.datetime = self.datetime.isoformat()
        return serializable_event.__dict__


    @property
    def clean_url(self):
        url = facebook_locale_to_www(self.url)
        if "?" in url:
            url = url[:url.index("?")]
        return url
    
    @property
    def description(self):
        return "Organized by {0}. See {1} for more info".format(self.source, self.clean_url)
    

    # Thanks to https://www.geeksforgeeks.org/getter-and-setter-in-python/
    @property
    def uid(self):
        # Facebook allows double entries of the same event, but in different times.
        # So the URL + datetime should be unique
        return slugify(self.clean_url) + slugify(self.datetime.isoformat())
    
    # See Add To Calendar Button documentation: https://github.com/add2cal/add-to-calendar-button#typical-structure
    @property
    def endTime(self):
        return self.datetime + timedelta(hours=2)
    
    """
    Okay so this is a doozy.
    - Glob is being used to future proof, in case of png or jpg or jpeg. That's good.
    - But it requires a local path to find the image
    - But that path cannot be relative. Originally this was passed img_dir=public/img,
      which then got public/ removed to img/filename.png.
      That works when running from the project dir! When run in C:/ProjectDir, it will
      look in C:/ProjectDir/public/img, find the thing, and replace as said above

      But the glob will fail when run from a different folder
      Cause then it will look for the file in C:/Differentdir/public/img and return None

    So this function got redesigned to not return ANY path, and instead just a filename.
    With optionally a relative path added as a paremeter

   
    """
    def get_image_filename(self, image_dir, return_with_path=None):
        try:
            image_glob_str = join(image_dir, self.uid + "*")
            filename_no_path = basename(glob(image_glob_str)[0])

            if not return_with_path:
                filename = filename_no_path
            else:
                filename = join(return_with_path, filename_no_path)

            return filename

        except IndexError:
            print("No image found for " + self.uid)
            return None
    
        
        

def load_events_from_json(json_path):
    events = []
    with open(json_path, "r") as file:
        raw_events = load(file)
        for raw_event in raw_events:
            event = Event.from_dict(raw_event)
            events.append(event)
    return events

def events_to_json(events, json_path):
    serializable_events = []
    for event in events:
        serializable_events.append(event.to_json())
    
    with open(json_path, "w") as file:
        dump(serializable_events, file)

```

### `src/facebook_event_aggregator/export/__init__.py`

```py
from .to_html import events_to_html
from .to_ics import events_to_ics
from .utils import cleanup_images
```

### `src/facebook_event_aggregator/export/templates/base.css`

```css
body {
    width: 80%;
    margin: auto;
}
```

### `src/facebook_event_aggregator/export/templates/base.html`

```html
<!DOCTYPE html>
<html lang="{% block lang %}en{% endblock lang %}">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- https://picocss.com/ -->
    <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css">

    <style>
        {% include "base.css" %}
    </style>

    <title>{{ title|default("Facebook Event Aggregator") }}</title>

    {% block head %}
    {% endblock head %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

### `src/facebook_event_aggregator/export/templates/index.html`

```html
{% extends "base.html" %}

{% block head %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/add-to-calendar-button@1/assets/css/atcb.min.css">
{% endblock head %}

{% block body %}
<main>
    <h1>{{ title }}</h1>
    <section>
        <h2>Upcoming Events</h2>

        <nav>
            <ul id="sources">
                <li>Filter:</li>
                {% for source in sources %}
                <li><a href="#" id="{{ source|slug }}">{{ source }}</a></li>
                {% endfor %}
            </ul>
        </nav>

        <div id="events" class="grid">
            {% for event in events %}
            <article class="{{ event.source|slug }}">

                <img src="{{ event.get_image_filename(image_dir, img_path_relative_to_index) }}"/>
                
                <h3>{{ event.name }}</h3>
    
                <p>{{ event.datetime.strftime("%H:%M - %A %d %b %Y") }}</p>
                {% if event.location %}
                <p>@ {{ event.location }}</p>
                {% endif %}
                {% if event.source %}
                <p>Organised by {{ event.source }}</p>
                {% endif %}
                {% if event.url %}
                <a href="{{ event.url }}" target="_blank">View on Facebook</a>
                {% endif %}
                
                <br><br>

                <div class="atcb" style="display: none;">
                    {# As of writing, icsFile only has affect on direct ics downloads. Manual setting is either way required, and thus preferred #}
                    {
                        {# Event info #}
                        "name": "{{ event.name }}",
                        "startDate": "{{ event.datetime.strftime("%Y-%m-%d") }}",
                        "startTime": "{{ event.datetime.strftime("%H:%M") }}",
                        "endTime": "{{ event.endTime.strftime("%H:%M") }}",
                        {#
                            Requires name|email
                        "organizer": "{{ event.organizer }}", 
                        #}
                        "location": "{{ event.location }}",
                        "description": "{{ event.description|escape }}",
                        "timeZone": "{{ timezone }}",
                        "uid": "{{ event.uid }}",

                        {# atcb configuration #}
                        "label": "Add {{ event.name|truncate(12, killwords=False)|escape }} to your Calendar",
                        "iCalFileName": "{{ event.uid }}",

                        "options": ["Apple", "Google|Google Calendar", "Microsoft365", "Outlook.com", "Yahoo", "iCal|iCal (.ics file)"],
                        "trigger": "click",
                        "listStyle": "overlay",
                        "lightMode": "system"
                    }
                </div>
            </article>
            {% endfor %}
        </div>
    </section>

    {% if domain %}
    <section>
        <h2>Calendar feeds</h2>
        <p>If you want to, you can also subscribe to an ical/.ics feed (sometimes called public url).<br>This will automatically add any events added here to your own calendar.</p>
        <ul class="grid">
            <li>Subscribe to all pages & communities listed here: <input type="url" value="{{ domain }}/ical/all.ics" readonly></li>
            {% for source in sources %}
                <li>
                    <label>Subscribe to {{ source }}: </label>
                    <input type="url" readonly value="{{ domain }}/ical/{{ source|slug }}.ics">
                </li>
            {% endfor %}
        </ul>
    </section>
    {% endif %}

    <section id="pages">
        <h2>Pages & communities</h2>
        <p>Check out the pages and communities that organise these events!</p>
        <ul>
            {% for page in pages %}
            <li><a href="{{ page }}" target="_blank">{{ page }}</a></li>
            {% endfor %}
        </ul>
        <p>(Note: this page is not made by the owners of the pages/communities listed above)</p>
    </section>
</main>

<footer class="grid">
    <span>
        Events collected & page generated using
        <a href="https://github.com/Denperidge/facebook-event-aggregator">Facebook Event Aggregator</a>.
    </span>
    <span>CSS Stylesheet by <a href="https://picocss.com/" target="_blank">Pico.css</a></span>
    <span>Calendar buttons by <a href="https://add-to-calendar-button.com/" target="_blank">ATCB</a></span>
    <span id="last-update">Last update: <span id="{{ now.isoformat() }}">{{ now.strftime("%H:%M, %D") }}</span></span>
</footer>

<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.1/dist/jquery.min.js"></script>
<!-- https://github.com/add2cal/add-to-calendar-button -->
<script src="https://cdn.jsdelivr.net/npm/add-to-calendar-button@1" async defer></script>
<script>{% include "index.js" %}</script>
{% endblock body %}
```

### `src/facebook_event_aggregator/export/templates/index.js`

```js
$(document).ready(function() {
    sourceFilters = $("nav a");
    eventSelector = "#events article";
    events = $(eventSelector);

    sourceFilters.on("click", function(e) {
        sourceFilter = $(e.target);
        console.log(sourceFilter.attr("id"))

        // If not pressed before,
        if (sourceFilter.attr("role") != "button") {
            sourceFilters.attr("role", "");  // Disable any other active buttons
            sourceFilter.attr("role", "button");  // Activate the current

            let selectedEvents = $(`${eventSelector}.${sourceFilter.attr("id")}`);

            events.not(selectedEvents).hide(400);  // Hide all events
            // Besides of the selected source
            selectedEvents.show(400);
        } else {
            sourceFilter.attr("role", "");
            events.show(400);
        }
    });

    lastUpdateElement = $("#last-update span").first();
    lastUpdate = Date.parse(lastUpdateElement.attr("id"));
    // Thanks to https://stackoverflow.com/a/5511376
    let yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);

    if (lastUpdate < yesterday) {
        lastUpdateElement.css("color", "red");
    }

    
});

```

### `src/facebook_event_aggregator/export/templates/workaround.py`

```py
# TODO stop using this
templates = {
    "base.css": """
body {
    width: 80%;
    margin: auto;
}
    """,
    "base.html": """
<!DOCTYPE html>
<html lang="{% block lang %}en{% endblock lang %}">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- https://picocss.com/ -->
    <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css">

    <style>
        {% include "base.css" %}
    </style>

    <title>{{ title|default("Facebook Event Aggregator") }}</title>

    {% block head %}
    {% endblock head %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
    """,
    "index.html": """
{% extends "base.html" %}

{% block head %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/add-to-calendar-button@1/assets/css/atcb.min.css">
{% endblock head %}

{% block body %}
<main>
    <h1>{{ title }}</h1>
    <section>
        <h2>Upcoming Events</h2>

        <nav>
            <ul id="sources">
                <li>Filter:</li>
                {% for source in sources %}
                <li><a href="#" id="{{ source|slug }}">{{ source }}</a></li>
                {% endfor %}
            </ul>
        </nav>

        <div id="events" class="grid">
            {% for event in events %}
            <article class="{{ event.source|slug }}">

                <img src="{{ event.get_image_filename(image_dir, img_path_relative_to_index) }}"/>
                
                <h3>{{ event.name }}</h3>
    
                <p>{{ event.datetime.strftime("%H:%M - %A %d %b %Y") }}</p>
                {% if event.location %}
                <p>@ {{ event.location }}</p>
                {% endif %}
                {% if event.source %}
                <p>Organised by {{ event.source }}</p>
                {% endif %}
                {% if event.url %}
                <a href="{{ event.url }}" target="_blank">View on Facebook</a>
                {% endif %}
                
                <br><br>

                <div class="atcb" style="display: none;">
                    {# As of writing, icsFile only has affect on direct ics downloads. Manual setting is either way required, and thus preferred #}
                    {
                        {# Event info #}
                        "name": "{{ event.name }}",
                        "startDate": "{{ event.datetime.strftime("%Y-%m-%d") }}",
                        "startTime": "{{ event.datetime.strftime("%H:%M") }}",
                        "endTime": "{{ event.endTime.strftime("%H:%M") }}",
                        {#
                            Requires name|email
                        "organizer": "{{ event.organizer }}", 
                        #}
                        "location": "{{ event.location }}",
                        "description": "{{ event.description|escape }}",
                        "timeZone": "{{ timezone }}",
                        "uid": "{{ event.uid }}",

                        {# atcb configuration #}
                        "label": "Add {{ event.name|truncate(12, killwords=False)|escape }} to your Calendar",
                        "iCalFileName": "{{ event.uid }}",

                        "options": ["Apple", "Google|Google Calendar", "Microsoft365", "Outlook.com", "Yahoo", "iCal|iCal (.ics file)"],
                        "trigger": "click",
                        "listStyle": "overlay",
                        "lightMode": "system"
                    }
                </div>
            </article>
            {% endfor %}
        </div>
    </section>

    {% if domain %}
    <section>
        <h2>Calendar feeds</h2>
        <p>If you want to, you can also subscribe to an ical/.ics feed (sometimes called public url).<br>This will automatically add any events added here to your own calendar.</p>
        <ul class="grid">
            <li>Subscribe to all pages & communities listed here: <input type="url" value="{{ domain }}/ical/all.ics" readonly></li>
            {% for source in sources %}
                <li>
                    <label>Subscribe to {{ source }}: </label>
                    <input type="url" readonly value="{{ domain }}/ical/{{ source|slug }}.ics">
                </li>
            {% endfor %}
        </ul>
    </section>
    {% endif %}

    <section id="pages">
        <h2>Pages & communities</h2>
        <p>Check out the pages and communities that organise these events!</p>
        <ul>
            {% for page in pages %}
            <li><a href="{{ page }}" target="_blank">{{ page }}</a></li>
            {% endfor %}
        </ul>
        <p>(Note: this page is not made by the owners of the pages/communities listed above)</p>
    </section>
</main>

<footer class="grid">
    <span>
        Events collected & page generated using
        <a href="https://github.com/Denperidge/facebook-event-aggregator">Facebook Event Aggregator</a>.
    </span>
    <span>CSS Stylesheet by <a href="https://picocss.com/" target="_blank">Pico.css</a></span>
    <span>Calendar buttons by <a href="https://add-to-calendar-button.com/" target="_blank">ATCB</a></span>
    <span id="last-update">Last update: <span id="{{ now.isoformat() }}">{{ now.strftime("%H:%M, %D") }}</span></span>
</footer>

<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.1/dist/jquery.min.js"></script>
<!-- https://github.com/add2cal/add-to-calendar-button -->
<script src="https://cdn.jsdelivr.net/npm/add-to-calendar-button@1" async defer></script>
<script>{% include "index.js" %}</script>
{% endblock body %}
    """,
    "index.js": """
$(document).ready(function() {
    sourceFilters = $("nav a");
    eventSelector = "#events article";
    events = $(eventSelector);

    sourceFilters.on("click", function(e) {
        sourceFilter = $(e.target);
        console.log(sourceFilter.attr("id"))

        // If not pressed before,
        if (sourceFilter.attr("role") != "button") {
            sourceFilters.attr("role", "");  // Disable any other active buttons
            sourceFilter.attr("role", "button");  // Activate the current

            let selectedEvents = $(`${eventSelector}.${sourceFilter.attr("id")}`);

            events.not(selectedEvents).hide(400);  // Hide all events
            // Besides of the selected source
            selectedEvents.show(400);
        } else {
            sourceFilter.attr("role", "");
            events.show(400);
        }
    });

    lastUpdateElement = $("#last-update span").first();
    lastUpdate = Date.parse(lastUpdateElement.attr("id"));
    // Thanks to https://stackoverflow.com/a/5511376
    let yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);

    if (lastUpdate < yesterday) {
        lastUpdateElement.css("color", "red");
    }

    
});

    """
}
```

### `src/facebook_event_aggregator/export/to_html.py`

```py
# Built-in imports
from os import getenv, listdir, remove
from os.path import realpath, dirname, join, isfile
from pathlib import Path
from sys import argv
from json import load
from datetime import datetime

# Package imports
from dateutil import parser
from jinja2 import FileSystemLoader, Environment, PrefixLoader, PackageLoader, DictLoader
from slugify import slugify

# Local imports
from ..Event import load_events_from_json
from .templates.workaround import templates


#try:
    #loader = PackageLoader("htmlexport")
  #  template_dir = join(realpath(dirname(__file__)), "templates")
 #   loader = FileSystemLoader(template_dir)
#except:
loader = DictLoader(templates)

jinja_env = Environment(
    loader=loader,
    autoescape=True,
    trim_blocks=True,  # Thanks to https://stackoverflow.com/a/35777386
    lstrip_blocks=True,
)

jinja_env.filters["slug"] = slugify


# img_dir: absolute path to look for in images
# img_path_relative_to_index: relative path from index.html to where images are stored on the host
# See Event.py
def events_to_html(
        events: list, 
        absolute_img_dir: str, 
        relative_from_html_img_dir: str,
        page_urls: list, 
        output_dir: str,
        title="Document Title",
        host_domain="https://domain.example.com",
        timezone="Europe/London"):
    """
    events: Events to export
    page_urls: 
    """
    template_index = jinja_env.get_template("index.html")

    sources = set([event.source for event in events])
    
    output = template_index.render(
        # 
        events=events,
        # Absolute image
        image_dir=absolute_img_dir,
        # Image path to be used in html to load images
        img_path_relative_to_index=relative_from_html_img_dir,
        title=title,
        domain=host_domain,
        timezone=timezone,
        pages=page_urls,
        sources=sources,
        now=datetime.now())

    filename_index = join(output_dir, "index.html")
    with open(filename_index, "w") as file:
        file.writelines(output)
    
    return output



# if __name__ == "__main__":
#     events_json = realpath(argv[1])
#     dir = dirname(events_json)

#     events = load_events_from_json(events_json)

#     events_to_html(events, dir)
```

### `src/facebook_event_aggregator/export/to_ics.py`

```py
# Built-in imports
from sys import argv
from os import makedirs
from os.path import realpath, dirname, join, exists
from json import load

# Package imports
from dateutil import parser
from ics import Calendar, Event as IcsEvent
from slugify import slugify

# Local imports
from ..repo import update_repo
from ..Event import load_events_from_json

def _read_ics_if_exists(ics_path):
    if exists(ics_path):
        with open(ics_path, "r", encoding="UTF-8") as file:
            ics_text = file.read()
        return Calendar(ics_text)
    else:
        return Calendar()

def events_to_ics(events: list, output_dir: str):
    output_dir = join(realpath(output_dir), "ical/")
    makedirs(output_dir, exist_ok=True)
    ics_all = join(output_dir, "all.ics")

    all_calendar = _read_ics_if_exists(ics_all)
    source_calendars = dict()

    sources = set([event.source for event in events])
    for source in sources:
        source_ics = join(output_dir, slugify(source) + ".ics")
        source_calendars[source] = _read_ics_if_exists(source_ics)
    

    for event in events:
        ics_event = IcsEvent()
        ics_event.name = event.name
        ics_event.begin = event.datetime
        # organizer also requires email
        #ics_event.organizer = event.organizer
        ics_event.location = event.location
        ics_event.url = event.url
        ics_event.uid = event.uid  # Thanks to uid, no duplicate entries will be made

        ics_event.description = event.description

        all_calendar.events.add(ics_event)
        source_calendars[event.source].events.add(ics_event)
        

    with open(ics_all, "w" , encoding="UTF-8") as file:
        file.writelines(all_calendar.serialize_iter())
    
    for source in source_calendars:
        dest = join(output_dir, slugify(source) + ".ics")
        calendar = source_calendars[source]

        with open(dest, "w", encoding="UTF-8") as file:
            file.writelines(calendar.serialize_iter())


```

### `src/facebook_event_aggregator/export/utils.py`

```py
from os import getenv, listdir, remove
from os.path import realpath, dirname, join, isfile
from pathlib import Path

# This will remove any images in the provided directory that aren't from provided events
def cleanup_images(still_upcoming_events: list, directory: str):
    upcoming_events_slugs = [event.uid for event in still_upcoming_events]

    files = listdir(directory)
    for filename in files:
        file = join(directory, filename)
        if isfile(file):
            filename_no_ext_or_path = Path(file).stem
            if filename_no_ext_or_path not in upcoming_events_slugs:
                remove(file)

```

### `src/facebook_event_aggregator/repo.py`

```py
# Built-in imports
from subprocess import run
from os.path import realpath, isdir, join, exists
from datetime import datetime

from git import Repo 

"""This module handles Git repo stuff"""

def _normalize_path(dir) -> str:
    return realpath(dir)

def _get_repo_path(parent_dir_path, repo_path) -> str:
    repo_path = _normalize_path(join(str(parent_dir_path), str(repo_path)))
    return repo_path

def _generate_commit_message():
    current_date = datetime.now().strftime("%d %m %Y")
    commit_msg = "Update from {}".format(current_date)
    return commit_msg


def clone_or_pull_repo(parent_dir_path, clone_dirname, repo_url: str):
    repo_path = _get_repo_path(parent_dir_path, clone_dirname)

    if not exists(repo_path):
        return Repo.clone_from(repo_url, repo_path)
    else:
        return Repo(repo_path).remote("origin").pull()

    
def update_repo(parent_dir_path, clone_dirname, commit_msg=None):
    repo_path = _get_repo_path(parent_dir_path, clone_dirname)
    
    if commit_msg is None:
        commit_msg = _generate_commit_message()
    
    repo = Repo(repo_path)
    
    repo.git.add(all=True)
    repo.index.commit(commit_msg)
    repo.remote("origin").push()

```

### `src/facebook_event_aggregator/scraper/__init__.py`

```py
from .driver import setup_driver
from .scrape_all import scrape_all

```

### `src/facebook_event_aggregator/scraper/driver.py`

```py
# Built-in imports
from platform import system, machine

# Package imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup Driver
def setup_driver(chromedriver_path: str=None, headless=False, remote_debugging_port = 0, extra_opts: list[str] = []) -> webdriver.Chrome:
    options = Options()

    if (headless):
        headless_opts = [
            "--headless=new",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            #"--no-sandbox",
            #"--disable-dev-shm-usage",
            "--remote-debugging-port=" + str(remote_debugging_port),
            #"--disable-setuid-sandbox"
        ]
        for opt in headless_opts:
            options.add_argument(opt)
            #print(opt)
        for opt in extra_opts:
            options.add_argument("--" + opt)
    
    # Much thanks to https://stackoverflow.com/a/71042821
    try:
        if not chromedriver_path:
            service = Service(ChromeDriverManager().install())
        else:
            #display = Display(visible=0, size=(1920,1200))
            #display.start()
            service = Service(chromedriver_path)
            #options.binary_location = raspbian_chromium
    except:
        # Attempt selenium fallback
        service = Service()
                

    return webdriver.Chrome(service=service, options=options)



```

### `src/facebook_event_aggregator/scraper/fb_login.py`

```py
# Built-in imports
from os import getenv
from time import sleep
from getpass import getpass

# Package imports
from selenium.webdriver.common.by import By

"""NOTE: currently unimplemented"""

def handle_fb_login(driver, headless):
    # If an email is provided, log into Facebook
    logged_in = False
    if getenv("facebook_email") is not None:
        facebook_email = getenv("facebook_email")
        print("Facebook email passed...")
        # Password provided, use that
        if getenv("facebook_password") is not None:
            print("... and a password. Using that to login.")
            facebook_password = getenv("facebook_password")
            login(driver, facebook_email, facebook_password)
            logged_in = True

        # No password provided, but running interactively, so prompt
        elif not headless:
            print("... but no password. Please enter it in the following prompt:")
            facebook_password = getpass()
            login(driver, facebook_email, facebook_password)
            logged_in = True
        
        # No password provided, but running headless, so quit
        else:
            print("Email was passed, but no password in headless mode. Skipping login")    
    
    return logged_in

def login(driver, email, password):
    driver.get("https://www.facebook.com/login")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.TAG_NAME, "form").submit()
    sleep(5)
```

### `src/facebook_event_aggregator/scraper/scrape_all.py`

```py
# Built-in imports
from os import getenv
from os.path import join, realpath
from time import sleep
from json import loads
from urllib.request import urlretrieve

# Package imports
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Local imports
from ..utils.fb_regexes import find_and_remove, regex_in, re_line_with_characters, re_guests, re_three_letter_two_digit_date, re_utc_time, re_utc_and_more
from ..Event import Event
from .driver import setup_driver
from ..utils.url_converter import facebook_www_to_locale
from .scrape_events_page import scrape_events_page

""" PARSING FUNCTIONS """


def scrape_all(driver, pages: list[str], img_dir: str):
    """ RUNNING PARSE FUNCTIONS ON PAGES """
    img_dir = realpath(img_dir)  # Directory where images get stored

    events = []
    for page in pages:
        driver.get(page)
        sleep(20)
        try:
            events.extend(scrape_events_page(driver, page, img_dir))


        except NoSuchElementException as e:
            print(f"Error parsing {page}")
            print("No events found.")
            print(e)

        except Exception as e:
            print(f"Error parsing {page}")
            raise e

    return events

```

### `src/facebook_event_aggregator/scraper/scrape_event_page.py`

```py
from time import sleep

from .driver import setup_driver
from ..utils.url_converter import facebook_www_to_locale

from selenium.webdriver.common.by import By

# Parse the event page in a secondary driver. This is universal for pages & communities
def scrape_event_page(event_url):
    location = None
    image_url = None
    event_url = facebook_www_to_locale(event_url)
    try:
        print("Searching for location & image in " + event_url)
        tmp_driver = setup_driver(headless=True)
        tmp_driver.get(event_url)
        sleep(20)
        info_rows = tmp_driver.find_elements(By.XPATH, "//div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/*")
        # Assume the first row is location, except if it contains specific text
        for info_row in info_rows:
            info = info_row.text
            info_lower = info.lower()
            if "details" in info_lower or "event by" in info_lower or "people respon" in info_lower:
                continue
                    
            # If location hasn't been found yet, assume the first line (that isn't excluded) is
            location = info
            break
            """ The following code can be used to begin implementing duration
            if not location:
                location = info
            if "duration" in info_lower:
                pass  
            """
                
        image_url = tmp_driver.find_element(By.CSS_SELECTOR,"img[data-imgperflogname=\"profileCoverPhoto\"]").get_attribute("src")

        tmp_driver.quit()
                
    except Exception as e:
        print(e)
        print("Location could not be fetched")

    
    return (location, image_url)

```

### `src/facebook_event_aggregator/scraper/scrape_events_page.py`

```py
from time import sleep

from .driver import setup_driver
from ..utils.url_converter import facebook_www_to_locale

from selenium.webdriver.common.by import By

from os import getenv
from os.path import join, realpath
from time import sleep
from json import loads
from urllib.request import urlretrieve

# Package imports
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Local imports
from ..utils.fb_regexes import find_and_remove, regex_in, re_line_with_characters, re_guests, re_three_letter_two_digit_date, re_utc_time, re_utc_and_more
from ..Event import Event
from .driver import setup_driver
from ..utils.url_converter import facebook_www_to_locale

from .utils import save_image
from .scrape_event_page import scrape_event_page

from time import sleep

def scrape_events_page(driver, event_url, img_dir) -> list[Event]:
    driver.get(facebook_www_to_locale(event_url))
    sleep(20)
    source = driver.find_element(By.XPATH, "//h1").text.strip()
    event_container = driver.find_element(By.XPATH, """//div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]""")
    raw_events = event_container.find_elements(By.XPATH, "*")
    events = []
    for event in raw_events:
        print("Detected upcoming event in {}!".format("page"))
        raw_data = event.text
        if regex_in(raw_data, re_utc_and_more): # Events with multiple times have multiple entries + one main. This is the main, so skip it
            print("detected main event with times, skipping current")
            continue

        try:
            lines = raw_data.split("\n")
            name = lines[1]
            datetime = lines[0]
            url = ""
            location = ""
        except IndexError:
            print("Failed to add event from page")
            print("Provided data: {}".format(lines))
            continue
    
        try:
            # find_element doesn't work, perhaps due to grandchild?
            urls = event.find_elements(By.TAG_NAME, "a")
            url = urls[0].get_attribute("href")
        except IndexError:
            print("No url found")
        
        location, image_url = scrape_event_page(url)

        event = Event(name, datetime, source, location, url)
        events.append(event)

        if image_url:
            save_image(event, image_url, img_dir)

        
    return events
```

### `src/facebook_event_aggregator/scraper/utils.py`

```py
from os.path import join
from urllib.request import urlretrieve 

def read_pages_from_env(replace_locale=True):
    """ LOADING & PARSING PAGES FROM .ENV """
    raw_pages = loads(getenv("pages"))
    pages = []
    for raw_page in raw_pages:
        page_type = raw_page[0].lower().strip()
        url = raw_page[1]

        match page_type:
            case "page":
                func = parse_page
            case "community":
                func = parse_community
            case _:  # Default
                func = parse_page
    
        if replace_locale:
            # Specify localisation
            url = facebook_www_to_locale(url)

        pages.append((func, url))
    return pages


def save_image(event, image_url, img_dir):
    if ".png" in image_url:
        ext = ".png"
    else:
        ext = ".jpg"
    print(event.uid)
    urlretrieve(image_url, join(img_dir, event.uid + ext))

```

### `src/facebook_event_aggregator/utils/fb_regexes.py`

```py
# Built-in imports
import re

""" Regexes to parse input from Facebook """

"""
Example:
    NOV
    11
    Text

    Returns: 
        Nov
        11
"""
re_three_letter_two_digit_date = r"^[a-zA-Z]{3}\W\d{1,2}$"

"""
Example:
    Fri 19:00 UTC+01 · 84 guests

    returns: Fri 19:00 UTC+01
"""
re_utc_time = r".*UTC\+\d{2}"

"""
Example:
    NOV
    19
    Name - 32 guests

    Returns: Name - 32 guests 
"""
re_guests = r".*guest.*"

# Matches any line with 1 or more characters
re_line_with_characters = r"^.{1,}$"

"""
Example:
    WED, 5 NOV AT 08:30 UTC+01 AND 1 MORE

    Returns: UTC+01 AND 1 MORE

"""
re_utc_and_more = r"UTC\+\d* AND \d{1,} MORE"

def regex_in(data, pattern):
    return bool(re.search(pattern, data))

def find_and_remove(data, pattern):
    try:
        found = re.search(pattern, data, flags=re.MULTILINE).group()
        data = data.replace(found, "")
    except AttributeError as e:
        print("Error during {0} Regex search".format(pattern))
        found = ""
    finally:
        return data, found

```

### `src/facebook_event_aggregator/utils/url_converter.py`

```py
from os import getenv

""" Helper functions for different facebook url's """

# To help get consistent results from scraping, a locale can be specified in .env
# This defaults to en-gb if none is provided
def facebook_www_to_locale(url, locale=getenv("fb_locale", "en-gb")):
    return url.replace("www.facebook", "{}.facebook".format(locale))

# And this function does the opposite, by removing the locale specification
# So that Facebook will detemine the language from the the end users' preference
def facebook_locale_to_www(url, locale=getenv("fb_locale", "en-gb")):
    return url.replace("{}.facebook".format(locale), "www.facebook")

```

### `src/tests/__init__.py`

```py

```

### `src/tests/export/__init__.py`

```py
#from src.facebook_event_aggregator.

```

### `src/tests/export/helpers.py`

```py
from pathlib import Path
from datetime import datetime

from src.facebook_event_aggregator.Event import Event

test_event_one = Event(
    name="Underscores - Botanique",
    datetime_param=str(datetime.now()),
    source="Botanique",
    location="Brussels",
    url="https://www.facebook.com/events/3483289855332151"
)

test_event_two = Event(
    name="Chase Petra - Trix",
    datetime_param=str(datetime.now()),
    source="Trix",
    location="Antwerp",
    url="https://www.facebook.com/events/956264055785138/"
)

example = {
    "events": [test_event_one, test_event_two],
    "title": "Concerts",
    "host_domain": "https://concerts.example.com",
    
    "page_urls": ["https://www.facebook.com/botaniquebxl", "https://www.facebook.com/trixonline"],
    "timezone": "Europe/Brussels"
}


def check_event_contents_in(event: Event, haystack):
    for property in [event.name, event.description, event.location, event.clean_url]:
        assert property in haystack

def write_test_ics(path):
    with open(path.joinpath(str(path)), "w", encoding="UTF-8") as file:
        file.write(
            """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:ics.py - http://git.io/RANDOM
BEGIN:VEVENT
CREATED:20151219T021727Z
DTEND;TZID=America/Toronto:20170515T110000
DTSTAMP:20151219T021727Z
DTSTART;TZID=America/Toronto:20170515T100000
LAST-MODIFIED:20151219T021727Z
RRULE:FREQ=DAILY;UNTIL=20170519T035959Z
SEQUENCE:0
SUMMARY:Meeting
TRANSP:OPAQUE
UID:21B97459-D97B-4B23-AF2A-E2759745C299
END:VEVENT
END:VCALENDAR
""")
        
        
```

### `src/tests/export/test_export_html.py`

```py

from pathlib import Path

from src.facebook_event_aggregator.Event import Event
from src.facebook_event_aggregator.export.to_html import events_to_html

from .helpers import example, check_event_contents_in

def test_events_to_html(tmp_path: Path):
    events_to_html(
        events=example["events"],
        absolute_img_dir=tmp_path.joinpath("images"),
        relative_from_html_img_dir="images/",
        page_urls=example["page_urls"],
        output_dir=tmp_path,
        title=example["title"],
        host_domain=example["host_domain"],
        timezone=example["timezone"]
    )

    with open(tmp_path.joinpath("index.html"), encoding="UTF-8") as file:
        data = file.read()
        for item in example.values():
            if type(item) == list:
                for value in item:
                    if not isinstance(value, Event):
                        assert value in data
                    else:
                        check_event_contents_in(value, data)
            else:
                assert item in data

```

### `src/tests/export/test_export_ics.py`

```py
from pathlib import Path

from ics import Calendar

from src.facebook_event_aggregator.export.to_ics import events_to_ics, _read_ics_if_exists

from .helpers import example, check_event_contents_in, write_test_ics

def test_read_ics_if_exists(tmp_path: Path):

    test_path = tmp_path.joinpath("test.ics")
    
    assert not test_path.exists()
    read_when_not_exist = _read_ics_if_exists(str(test_path))

    assert read_when_not_exist == Calendar()  # Empty calendar
    assert len(read_when_not_exist.events) == 0

    write_test_ics(test_path)
    read_when_exists = _read_ics_if_exists(str(test_path))
    
    assert test_path.exists()
    assert read_when_exists != Calendar()
    assert len(read_when_exists.events) > 0
    



def test_events_to_ics(tmp_path: Path):
    events_to_ics(example["events"], str(tmp_path))

    ical_dir = tmp_path.joinpath("ical/")

    all_filepath = ical_dir.joinpath("all.ics")

    assert ical_dir.joinpath("all.ics").exists()
    with open(str(all_filepath), "r", encoding="utf-8") as all_file:
        all_content = all_file.read()

    for event in example["events"]:
        check_event_contents_in(event, all_content)

        source_filepath = ical_dir.joinpath(event.source.lower() + ".ics")
        assert source_filepath.exists()
        with open(str(source_filepath), "r", encoding="UTF-8") as source_file:
            source_contents = source_file.read()
            check_event_contents_in(event, source_contents)
        

```

### `src/tests/export/test_utils.py`

```py
from pathlib import Path

from src.facebook_event_aggregator.export.utils import cleanup_images
from src.facebook_event_aggregator.Event import Event
from .helpers import example

def assert_exist(path: Path, filenames, exist=True):
    for filename in filenames:
        assert (path.joinpath(filename)).exists() == exist

def test_cleanup_images(tmp_path: Path):
    events = example["events"]
    
    filenames = ["test.png", events[0].uid + ".png", "meow.png", events[1].uid]

    for filename in filenames:
        with open(str(tmp_path.joinpath(filename)), "w", encoding="UTF-8") as file:
            file.write("")
    
    assert_exist(tmp_path, filenames)

    for file in tmp_path.glob("*"):
        print(file)
    
    cleanup_images(events, str(tmp_path))

    for file in tmp_path.glob("*"):
        print(file)


    assert_exist(tmp_path, [filenames[0], filenames[2]], exist=False)
    assert_exist(tmp_path, [filenames[1], filenames[3]], exist=True)
    
        
```

### `src/tests/scraper/test_scrape.py`

```py
from os.path import join, abspath, dirname

from pathlib import Path

from dateutil import parser

from src.facebook_event_aggregator.scraper.driver import setup_driver
from src.facebook_event_aggregator.scraper.scrape_event_page import scrape_event_page
from src.facebook_event_aggregator.scraper.scrape_events_page import scrape_events_page
from src.facebook_event_aggregator.scraper.scrape_all import scrape_all


def test_scrape_event_page():
    return
    location, image_url = scrape_event_page("file://" + abspath(join(dirname(__file__).replace("\\", "/"), "event_page.htm")))
    assert location == "Le Botanique"
    assert image_url == "https://scontent-bru2-1.xx.fbcdn.net/v/t39.30808-6/384365949_704986814996124_1745966508573235950_n.jpg?stp=dst-jpg_s960x960&_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_ohc=YrHGPpoEZssAX8FBBH7&_nc_oc=AQkB4iDsJKhbaZq2oCPLR0ui77bF_fqimfD7hV3pTDczYXSTcO1tqLKSYFY4YbV-q0I&_nc_ht=scontent-bru2-1.xx&oh=00_AfA6LQP9omvSzhV9fQH8_NVYL8pT2d7rkxnBlOGt87251A&oe=653DDCD4"


def events_page_tester(tmp_path: Path, func, events_as_list:bool=False):
    events_page = "file://" + abspath(join(dirname(__file__).replace("\\", "/"), "events_page.htm"))
    if events_as_list:
        events_page = [events_page]
    events = func(setup_driver(headless=True), events_page, str(tmp_path))
    
    things_to_find = [
        {
            # TODO finish datetime tests
            "name": "Business As Usual #2 Money Talks pt 2 in AMOR",
            #"datetime": parser.parse("25 oct 08:00 +2")



        },
        {
            "name": "Coach Party / Trix - HiFive Concert - UITVERKOCHT!"
        },
        {
            "name": "Eric Steckel / Trix"
        },
        {
            "name": "Brass Against / Trix"
        },
        {
            "name": "It It Anita + Godcaster / Trix"
        },
        {
            "name": "Birds in Row + Walfang + Quentin Sauvé / Trix"
        },
        {
            "name": "Vrijdag Vrijdag met Fabulae Dramatis + C I M E + Wendung"
        },
        {
            "name": "Protomartyr + Es + dust / Trix"
        }
    ]

    for event in events:

        assert event.source == "Trix"
        to_find = things_to_find.pop(0)
        assert event.name == to_find["name"]
        #assert event.location == "Trix" or event.location == "AMOR van De Roma"
        #assert event.location == "Trix"  # TODO: location is not consistent
        print(event.name)
        print(event.source)
        print(event.datetime)
        
        print(event.location)
        print("---")
    


def test_scrape_events_page(tmp_path: Path):
    events_page_tester(tmp_path, scrape_events_page)

def test_scrape_all(tmp_path: Path):
    events_page_tester(tmp_path, scrape_all, events_as_list=True)
```

### `src/tests/test_Event.py`

```py
from os import makedirs
from json import loads, dumps
from pathlib import Path

from dateutil import parser
from datetime import datetime


from src.facebook_event_aggregator.Event import Event, load_events_from_json, events_to_json
from src.facebook_event_aggregator.utils.url_converter import facebook_locale_to_www, facebook_www_to_locale

class TestEventClass():
    """Test helpers"""
    event = Event(
        name="Test",
        datetime_param="20 Nov 2023 18:00 UTC+1",
        source="Organisation",
        location="Belgium",
        url="https://en-gb.facebook.com/test"
    )

    def compare_to_original(self, event):
        assert event.name == "Test"
        assert event.datetime == parser.parse("20/11/2023 18:00+1")
        assert event.source == "Organisation"
        assert event.location == "Belgium"
        assert event.url == "https://en-gb.facebook.com/test"


    """Init tests"""
    def test_init(self):
        self.compare_to_original(self.event)

    def test_init_from_dict(self):
        event = Event.from_dict({
            "name":"Test",
            "datetime": "20 Nov 2023 18:00 UTC+1",
            "source": "Organisation",
            "location": "Belgium",
            "url": "https://en-gb.facebook.com/test"
        })
        assert event.to_json() == self.event.to_json()

    """Property tests"""
    def test_clean_url(self):
        assert self.event.clean_url == facebook_locale_to_www(self.event.url)
        assert self.event.clean_url != facebook_www_to_locale(self.event.url)


        test_event = Event("Name", "20 Nov 2023 18:00", "Source", "Location", "https://www.facebook.com/profile/?should_not_be_here")
        assert "should_not_be_here" not in test_event.clean_url
        assert "?" not in test_event.clean_url
        assert test_event.clean_url == "https://www.facebook.com/profile/"

    def test_description(self):
        assert type(self.event.description) == str
        assert self.event.source in self.event.description
        assert self.event.clean_url in self.event.description
    
    def test_uid(self):
        assert type(self.event.uid) == str
    
    def test_endTime(self):
        assert type(self.event.endTime) == datetime

    # TODO get_image

    """Method tests"""
    def test_to_json(self):
        self.compare_to_original(Event.from_dict(self.event.to_json()))
    
    def test_get_image_filename(self, tmp_path: Path):
        output_filename = self.event.uid + ".png"
        output_filepath = tmp_path.joinpath(output_filename)


        # does not exist
        assert self.event.get_image_filename(tmp_path) == None


        with open(output_filepath, "w") as file:
            file.write("")

        # return_with_path = None
        assert self.event.get_image_filename(tmp_path, return_with_path=None) == output_filename
        # return_with_path = defined
        assert self.event.get_image_filename(tmp_path, return_with_path=tmp_path) == str(output_filepath)
        


    """Global func tests"""
    def test_events_to_json_and_from_json(self, tmp_path: Path):
        output_path = str(tmp_path.joinpath("events.json"))
        
        events_to_json([self.event, self.event], output_path)
        events = load_events_from_json(output_path)

        for event in events:
            self.compare_to_original(event)

    
    #def test_events_from_json(self, tmp_path: Path):
     #   with open(tmp_path.joinpath("data.json"), "w", encoding="UTF-8") as file:
      #      file.write(f"{"",}")

```

### `src/tests/test_repo.py`

```py
from os.path import exists, realpath
from pathlib import Path
from datetime import datetime

from src.facebook_event_aggregator.repo import _normalize_path, _get_repo_path, _generate_commit_message, clone_or_pull_repo, update_repo

from git import Repo, FetchInfo
from git.util import IterableList
from git.exc import GitCommandError

class TestRepo():    
    """Test helper funcs"""
    def test_normalize_path(self):
        assert _normalize_path("../") == realpath("../")
    
    def test_get_repo_path(self, tmp_path: Path):
        assert str(tmp_path.joinpath("test")) == _get_repo_path(tmp_path, "test")

    def test_generate_commit_message(self):
        assert _generate_commit_message() == f'Update from {datetime.now().strftime("%d %m %Y")}'


    def clone_or_pull_shortcut(self, tmp_path: Path):
        return clone_or_pull_repo(tmp_path, "test", "https://github.com/github/dev.git")

    def test_clone_or_pull(self, tmp_path: Path):
        repo_dir = _get_repo_path(tmp_path, "test")

        assert not exists(repo_dir)
        
        assert type(self.clone_or_pull_shortcut(tmp_path)) == Repo
        assert exists(repo_dir)

        assert type(self.clone_or_pull_shortcut(tmp_path)) == IterableList
        
        
    def test_update_repo(self, tmp_path: Path):
        repo_dir = _get_repo_path(tmp_path, "test")

        assert not exists(repo_dir)
        
        repo = self.clone_or_pull_shortcut(tmp_path)
        
        try:
            generated_commit_msg = _generate_commit_message()  # Do this before so there's less chance of bad timing failing the test
            update_repo(tmp_path, "test", commit_msg=None)
        except GitCommandError:
            pass  # This will return 403, which is normal
        finally:
            assert repo.commit(repo.branches[0]).message == generated_commit_msg
        
        try:
            update_repo(tmp_path, "test", commit_msg="Test succeeded!")
        except GitCommandError:
            pass  # This will return 403, which is normal
        finally:
            assert repo.commit(repo.branches[0]).message == "Test succeeded!"

```

### `src/tests/utils/__init__.py`

```py

```

### `src/tests/utils/test_fb_regexes.py`

```py
from src.facebook_event_aggregator.utils.fb_regexes import re_guests, re_line_with_characters, re_utc_and_more, re_three_letter_two_digit_date, re_utc_time, find_and_remove, regex_in

class TestFacebookRegexes():
    basic_string = "this is a string"
    complex_string = "Test! Meow!\nNOV\n11\nMore test!\nFri 19:00 UTC+01 AND 1 MORE\nName - 32 guests"
    
    def test_regex_in(self):
        assert regex_in(self.basic_string, r"[a-z]") == True
        assert regex_in(self.basic_string, r"[0-9]") == False
    

    def test_find_and_remove(self):
        remains, result = find_and_remove(self.basic_string, r"str.*ng")

        assert remains == "this is a "
        assert result == "string"

        remains, result = find_and_remove(self.basic_string, r"0.*9")

        assert remains == "this is a string"
        assert result == ""
    

    def test_re_line_with_characters(self):
        assert regex_in("Test", re_line_with_characters) == True
        assert regex_in("", re_line_with_characters) == False


    def test_re_utc_time(self):
        remains, result = find_and_remove(self.complex_string, re_utc_time)
        assert result == "Fri 19:00 UTC+01"


    def test_re_three_letter_two_digit_date(self):
        remains, result = find_and_remove(self.complex_string, re_three_letter_two_digit_date)
        assert result == "NOV\n11" 
        

    
    def test_re_guests(self):
        remains, result = find_and_remove(self.complex_string, re_guests)
        assert result == "Name - 32 guests"


    def test_re_utc_and_more(self):
        remains, result = find_and_remove(self.complex_string, re_utc_and_more)
        assert result == "UTC+01 AND 1 MORE"
```

### `src/tests/utils/test_url_converter.py`

```py
from src.facebook_event_aggregator.utils.url_converter import facebook_locale_to_www, facebook_www_to_locale

class TestUrlConverter():
    www_url = "https://www.facebook.com/test"
    locale_url = "https://en-gb.facebook.com/test"


    def test_www_to_locale(self):
        assert facebook_www_to_locale(self.www_url, "en-gb") == self.locale_url

    def test_locale_to_www(self):
        assert facebook_locale_to_www(self.locale_url, "en-gb") == self.www_url
    
```
