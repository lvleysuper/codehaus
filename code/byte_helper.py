#!/usr/bin/env python
# coding: utf-8
"""
util for bytes and str
[python3] bytes: 字符数组 str: 字符串, unicode
[python2] str: 字符数组 unicode: 字符串
"""

import sys


def get_version():
    major = sys.version.split(".")[0]
    return int(major)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode("utf-8")
    else:
        return bytes_or_str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode("utf-8")
    else:
        return bytes_or_str


if __name__ == "__main__":
    print(get_version())
    print(to_bytes("hello"))
    print(to_str("hello"))