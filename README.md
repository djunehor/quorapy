# quorapy
[![Build Status](https://travis-ci.org/djunehor/quorapy.svg?branch=master)](https://travis-ci.org/djunehor/quorapy) [![HitCount](http://hits.dwyl.io/djunehor/quorapy.svg)](http://hits.dwyl.io/djunehor/quorapy)

#### Issues and pull requests welcome.

A Python module to fetch and parse data from Quora.

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Contribute](#contribute)

## Installation
You will need [Python 3.x](https://www.python.org/download/) and [pip](http://pip.readthedocs.org/en/latest/installing.html).

Install using pip: `pip install quorapy`
Install via repo:
- Clone repor `git clone https://github.com/djunehor/quorapy`
- Install requirements via `pip install -r requirements.txt`
- Place quorapy in your project root folder

## Usage

```python
from quorapy import Quora
import os
from quorapy.browser import Browser

browser = Browser(os.getenv('LINUX'))
quora = Quora(browser)

# search for `Python`
results = quora.search('Python')

# Sample response:
{  "answer_limit": 1,
  "data": [
    {
      "comments": [
        {
          "text": "Rather than giving you a boring step by step process of learning Python, I would share my personal journey about how I started learning Python.\nHere is my personal learning experience:\nWhat motivated me to start learn Python ?\nI fell in love with Python after reading a bunch of answers on Quora about how people were doing wonderful things with Python.\nSome were writing scripts to automate their Whats app messages.\nSome wrote a script to download their favourite songs,\nwhile some built a system to receive cricket score updates on their phones.\nAll of this seemed very excited to me and I finally dec...(more)",
          "user": {
            "datetime": "2019-09-29 02:52:30.692237",
            "name": "",
            "url": "https://www.quora.com/profile/Neha-Ahuja-178"
          }
        }
      ],
      "question": {
        "datetime": "2019-09-28 23:57:00",
        "text": "How should I start learning Python?",
        "user": {
          "name": "Quora Content Review",
          "url": "https://quora.com/profile/Quora-Content-Review"
        }
      },
      "url": "https://www.quora.com/How-should-I-start-learning-Python-1"
    }
  ],
  "load_user": null,
  "query": "python",
  "question_limit": 1
}
```

## Features
### Currently implemented
* Search


## Contribute
Check out the issues on GitHub and/or make a pull request to contribute!