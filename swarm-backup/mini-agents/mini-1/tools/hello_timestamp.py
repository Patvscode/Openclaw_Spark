#!/usr/bin/env python3
"""Hello world with timestamp."""
import datetime

if __name__ == "__main__":
    now = datetime.datetime.now().isoformat()
    print(f"Hello from Alpha! Current time: {now}")
