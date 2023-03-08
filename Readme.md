![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![GitHub repo size](https://img.shields.io/github/repo-size/Lonely-Dark/helperclass-pack?style=flat-square)
![GitHub](https://img.shields.io/github/license/Lonely-Dark/helperclass-pack?style=flat-square)

# Helperclass-pack
Helperclass-pack is a Python library developed by Lonely-Dark to facilitate logging in their projects. It provides a Helper class that can be used to easily configure logging settings and log messages to various output streams.

## Installation
Via cloning
`git clone https://github.com/Lonely-Dark/helperclass-pack.git`

## Usage
To use Helperclass-pack, simply import the Helper class from the helperclass_pack module and create an instance of it.

```python
from helperclass import Helper

helper = Helper()
helper.logger.debug("This is a log message.")
```

By default, logging messages are sent to the console with a log level of DEBUG. You can configure the log level and output streams by passing arguments to the Helper constructor.

```python
from helper import Helper

helper = Helper(log_level=20, filename="log_my.log", streams=3)
helper.logger.info("This is a log message.")
```

## Configuration options
Helperclass-pack provides the following configuration options:

```
log_level: The minimum log level at which messages will be logged. Defaults to DEBUG.
filename: The name of the file to which log messages will be written. Defaults to log.
streams: 1,2,3; 1 - StreamHandler, 2 - FileHandler, 3 - All Handlers
```
## License
Helperclass-pack is licensed under the GPL-3.0. See the LICENSE file for details.