#!/usr/bin/env python3
"""greet.py
A simple tool that prints a greeting with the current UTC timestamp.
Usage: python greet.py [name]
If no name is given, it defaults to 'World'.
"""

import sys
from datetime import datetime, timezone


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"Hello, {name}! Current time is {ts}")

if __name__ == "__main__":
    main()
