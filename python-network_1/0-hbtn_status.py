#!/usr/bin/python3
"""
This module fetches the status from a given URL using urllib.
"""

import urllib.request


def main():
    """Fetches URL and displays the response body."""
    url = "https://intranet.hbtn.io/status"

    req = urllib.request.Request(
        url,
        headers={"cfclearance": "true"}
    )

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))


if __name__ == "__main__":
    main()
