#!/usr/bin/env python
"""Check the sample python scripts run.

Useful to catch any Python 2 vs Python 3 syntax errors.

TODO: Check output against embedded examples in README.rst?
TODO: Handle any command line switches?
"""

from __future__ import print_function
import os
import sys

filename = os.path.split(__file__)[1]
if os.path.isfile(filename):
    #Already in the tests directory
    #base_path = ".."
    #Assume sample data files in the repository root directory
    os.chdir("..")
if os.path.isfile(os.path.join("tests", filename)):
    #Already in the repository root directory
    base_path ="."
else:
    sys.stderr.write("Should be in base folder or tests folder.\n")
    sys.exit(1)

def check(script):
    """Runs script and Will increment good, warn or errors."""
    global errors
    #TODO - Capture stderr, look for warnings
    #TODO - This assumes 'python' will be aliased as on TravisCI
    rc = os.system("python %s" % script)
    if rc:
        errors += 1
        sys.stderr.write("Return code %i from %s\n" % (rc, script))

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

            
