GROK
====

Grok is a Python port of ruby-grok written by @jordansissel.

Here is the refrerence implementation [Link](https://github.com/jordansissel/ruby-grok)


Status
------

The project is a work in progress. I have implemented a few base line tests to prove out the api and have started filling these in, but this is no where near working.

Here are things to do:

[x] Setup test framework
[x] Setup Python classes for dummy api
[ ] Tox tests for py26, py27, py33, pypy, jython
[ ] Setup Travis-CI
[x] Grok.add\_pattern(name, pattern)
[x] Grok.add\_patterns\_from\_file(filename)
[ ] Grok.compile(pattern)
[ ] Grok.discover(input)
[ ] Grok.match(text)
[ ] Release to pypi

Usage
-----

```python
from grok import Grok

grok = Grok()
grok.add_patterns_from_file('/path/to/my/patterns')

grok.compile('%{GREEDYDATA} - %{NUMBER}')

input = "My Fancy Input 9999"

print(input)
print("Matches" if grok.matches(input) else "Doens't Match")
```

For more usage, see the _specs/example_spec.py_.

Installation
------------

```bash
$ pip install grok
```
