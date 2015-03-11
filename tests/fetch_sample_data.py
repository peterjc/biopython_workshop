#!/usr/bin/env python
"""Scan SAMPLE_DATA.rst for wget etc commands, and execute them.

Intended for use within TravisCI for automated testing.

Assumes running on Linux. Will not work on Mac OS X (unless you
happen to have wget etc installed).
"""

from __future__ import print_function
import os
import sys

sample_data = "SAMPLE_DATA.rst"
filename = os.path.split(__file__)[1]
if os.path.isfile(filename):
    #Already in the tests directory
    #base_path = ".."
    #Put sample data files in the repository root directory
    os.chdir("..")
if os.path.isfile(os.path.join("tests", filename)):
    #Already in the repository root directory
    base_path ="."
else:
    sys.stderr.write("Should be in base folder or tests folder.\n")
    sys.exit(1)


print("Extracting commands from %s to fetch sample data..." % sample_data)
commands = []
with open(sample_data) as handle:
    for line in handle:
        if line.startswith("    $ "):
            line = line[5:].strip()
            if line.startswith("curl "):
                # Mac OS X variant, ignore
                continue
            commands.append(line)

for cmd in commands:
    print(cmd)
    return_code = os.system(cmd)
    if return_code:
        sys.stderr.write("Return code %i from: %s" % (return_code, cmd))
        sys.exit(return_code)

print("Done")
