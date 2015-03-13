#!/usr/bin/env python
"""Check the sample python scripts run.

Useful to catch any Python 2 vs Python 3 syntax errors.

TODO: Check output against embedded examples in README.rst?
TODO: Handle any command line switches?
"""

from __future__ import print_function
import os
import sys
import subprocess

filename = os.path.split(__file__)[1]
if os.path.isfile(filename):
    #Already in the tests directory
    #base_path = ".."
    #Assume sample data files in the repository root directory
    os.chdir("..")
if os.path.isfile(os.path.join("tests", filename)):
    #Already in the repository root directory
    base_path = "."
else:
    sys.stderr.write("Should be in base folder or tests folder.\n")
    sys.exit(1)


def check(script):
    """Runs script and Will increment good, warn or errors."""
    global good, warn, errors
    #TODO - This assumes 'python' will be aliased as on TravisCI
    child = subprocess.Popen(["python", script],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             )
    stdout, stderr = child.communicate()
    if child.returncode:
        errors += 1
        sys.stderr.write("Return code %i from %s\n" % (child.returncode, script))
    elif stderr:
        warn += 1
        sys.stderr.write(stderr)
    else:
        good += 1
        # TODO - shorten this when verbose
        sys.stdout.write(stdout)


good = 0
warn = 0
errors = 0
for dirpath, dirnames, filenames in os.walk(base_path):
    if "README.rst" not in filenames:
        continue
    readme = os.path.join(dirpath, "README.rst")
    if readme.endswith("/tests/README.rst"):
        continue
    scripts = [f for f in filenames if f.endswith(".py")]
    if not scripts:
        continue
    print("-" * 40)
    print("Checking %s (%i scripts)" % (dirpath, len(scripts)))
    print("-" * 40)
    for f in scripts:
        script = os.path.join(dirpath, f)
        print("Checking %s" % script)
        check(script)
print("=" * 40)
print("%i good, %i warnings, %i errors" % (good, warn, errors))
if errors:
    sys.stderr.write("Test failed")
    sys.exit(1)

