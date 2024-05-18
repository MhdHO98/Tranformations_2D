#!/usr/bin/env python3

import sys
import os
import matplotlib

# Ensure the directory of the my_tests.py file is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Tests'))

from Tests.my_tests import run_tests

if __name__ == "__main__":
    run_tests()
