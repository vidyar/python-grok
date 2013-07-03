GROK
====

Grok is a Python port of ruby-grok written by @jordansissel.

Here is the refrerence implementation [Link](https://github.com/jordansissel/ruby-grok)

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
