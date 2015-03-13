#!/usr/bin/env python
"""Check the sample python scripts match the emmbeded copies in README.rst files.

This is a workaround for the fact that (due to security concerns)
neither BitBucket nor GitHub support the reStructuredText include
directive, which would have allowed direct embedding of small
Python scripts into the documentation. See:

- https://bitbucket.org/site/master/issue/5411/restructuredtext-include-directive
- https://github.com/github/markup/issues/172
"""

from __future__ import print_function
import os
import sys

filename = os.path.split(__file__)[1]
if os.path.isfile(filename):
    #Already in the tests directory
    base_path = ".."
elif os.path.isfile(os.path.join("tests", filename)):
    #Already in the repository root directory
    base_path ="."
else:
    sys.stderr.write("Should be in base folder or tests folder.\n")
    sys.exit(1)

def load_and_indent(filename, indent=" "*4):
    """Load a text file as a string, adding the indent to each line."""
    lines = []
    for line in open(filename):
        lines.append(indent + line)
    return "".join(lines)

good = 0
warn = 0
errors = 0
for dirpath, dirnames, filenames in os.walk(base_path):
    if "README.rst" not in filenames:
        continue
    readme = os.path.join(dirpath, "README.rst")
    if readme.endswith("/tests/README.rst"):
        continue
    print("-" * 40)
    print("Checking %s" % readme)
    #Which script files might this contain?
    scripts = dict()
    for f in filenames:
        if f.endswith(".py"):
            scripts[f] = load_and_indent(os.path.join(dirpath, f))
    if not scripts:
        print("No local script files for this")
        continue
    #Now check the README.rst file contains them...
    print("Using: %s" % ", ".join(sorted(scripts)))
    with open(readme) as handle:
        text = handle.read()
    for filename, script in sorted(scripts.items()):
        filename_used = (("``%s``" % filename) in text) or (("$ python %s" % filename) in text)
        script_embedded = script in text
        if filename_used and script_embedded:
            print(" - %s named and embedded" % filename)
            good += 1
        elif filename_used:
            print(" - %s named but not embedded (warning)" % filename)
            warn += 1
        elif script_embedded:
            print(" - %s not named, but embedded in text (ERROR)" % filename)
            errors += 1
        else:
            print(" - %s neither named nor embedded (ERROR)" % filename)
            errors += 1
print("=" * 40)
print("%i good, %i warnings, %i errors" % (good, warn, errors))
if errors:
    sys.stderr.write("Consistency test failed")
    sys.exit(1)

            
