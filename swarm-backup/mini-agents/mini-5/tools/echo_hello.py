#!/usr/bin/env python3
"""Echo Hello Tool

This is a minimal example tool that prints a greeting. It can be used
by other agents or the orchestrator to verify that Echo's tooling
environment is operational.

Run with:
    python3 tools/echo_hello.py

"""

import datetime


def main():
    now = datetime.datetime.now().isoformat()
    print(f"Hello from Echo! Current time: {now}")


if __name__ == "__main__":
    main()
