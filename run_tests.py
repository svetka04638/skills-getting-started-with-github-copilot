#!/usr/bin/env python
import subprocess
import sys
import os

os.chdir('/workspaces/skills-getting-started-with-github-copilot')
result = subprocess.run([sys.executable, '-m', 'pytest', 'tests/', '-v'], capture_output=True, text=True)
print("STDOUT:")
print(result.stdout)
print("STDERR:")
print(result.stderr)
print("Return code:", result.returncode)