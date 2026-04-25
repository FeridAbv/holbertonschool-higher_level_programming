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
        body = response.read()

        print("Body response:")
        print("type: {}".format(type(body)))
        print("content: {}".format(body))
        print("utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    main()
