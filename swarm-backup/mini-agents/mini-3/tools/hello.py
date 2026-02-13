#!/usr/bin/env python3
"""Simple utility script.

This script prints a greeting and the current UTC timestamp.
Useful for quick checks of the environment.
"""

import datetime

if __name__ == "__main__":
    now = datetime.datetime.utcnow().replace(microsecond=0)
    print("Hello, World!")
    print(f"Current UTC time: {now}")
