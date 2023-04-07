#!/usr/bin/python3
"""Displays X-Request-Id in the response header of a request to a given URL.
Eg: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
