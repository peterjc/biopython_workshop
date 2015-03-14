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


use_curl = (sys.platform == "darwin")

print("Extracting commands from %s to fetch sample data..." % sample_data)
commands = []
with open(sample_data) as handle:
    for line in handle:
        if line.startswith("    $ "):
            line = line[5:].strip()
            if line.startswith("curl "):
                if use_curl:
                    # Use this in preference to previous entry,
                    commands.pop()
                else:
                    # Ignore this
                    continue
            commands.append(line)

def wget_to_curl(cmd):
    if not cmd.startswith("wget "):
        return cmd
    if cmd.startswith(("wget http", "wget ftp")):
        return "curl -O " + cmd[5:]
    elif cmd.startswith("wget -O "):
        return "curl -o " + cmd[8:]
    else:
        # Currently hard coding tricky wget/curl cases
        # directly in the input RST file...
        raise NotImplementedError(cmd)
assert wget_to_curl('wget http://example.org/data.ext') == \
    'curl -O http://example.org/data.ext'
assert wget_to_curl('wget -O "example.ext" http://example.org/data?arg=value"') == \
    'curl -o "example.ext" http://example.org/data?arg=value"'


for cmd in commands:
    if use_curl:
        cmd = wget_to_curl(cmd)
    print(cmd)
    return_code = os.system(cmd)
    if return_code:
        sys.stderr.write("Return code %i from: %s" % (return_code, cmd))
        sys.exit(return_code)

print("Done")
