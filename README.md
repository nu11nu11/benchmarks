# benchmarks

A set of tools to drive your services to their limits - any maybe beyond.

## dos_plone.py

This is the Plone DoS test tool - Availability does matter.

Use it to drown a Plone instance in non-cachable requests.

###Synopsis:

```
usage: dos_plone.py [-h] -t TARGET [-a ATTACK] [-n NUMBER] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        The target to test (default: https://localhost)
  -a ATTACK, --attack ATTACK
                        Different attacks. 0: GET random page, 1: spam search,
                        2: spam contact-info, 3: run all attacks at once
                        (default: 3)
  -n NUMBER, --number NUMBER
                        Start that many threads (default: 1)
  -v, --version         show program's version number and exit

While the program is running, one character will be printed out for each
request. E: connection error, 5: HTTP status 5xx, .: all other HTTP status
codes.
```


