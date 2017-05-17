#!/usr/bin/env python3

"""
Find the path of a key / value in a JSON hierarchy easily.

It was made for JSON files, but it also works with dictionaries,
of course.

Inspired by:
* http://stackoverflow.com/a/34837235/232485 (doesn't treat nested lists)
* http://chris.photobooks.com/json/default.htm (in-browser visualization)

Author:
* Laszlo Szathmary, alias Jabba Laci, 2017, jabba.laci@gmail.com
"""

import json
import sys


def traverse(path, obj):
    """
    Traverse the object recursively and print every path / value pairs.
    """
    cnt = -1
    if isinstance(obj, dict):
        d = obj
        for k, v in d.items():
            if isinstance(v, dict):
                traverse(path + "." + k, v)
            elif isinstance(v, list):
                traverse(path + "." + k, v)
            else:
                print(path + "." + k, "=>", v)
    if isinstance(obj, list):
        li = obj
        for e in li:
            cnt += 1
            if isinstance(e, dict):
                traverse("{path}[{cnt}]".format(path=path, cnt=cnt), e)
            elif isinstance(e, list):
                traverse("{path}[{cnt}]".format(path=path, cnt=cnt), e)
            else:
                print("{path}[{cnt}] => {e}".format(path=path, cnt=cnt, e=e))


def read_file(fpath):
    """
    Read the JSON file and return its content as a Python data structure.
    """
    with open(fpath) as f:
        return json.load(f)


def process(fname):
    """
    Process the given JSON file.
    """
    d = read_file(fname)
    traverse("root", d)

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: json_path <input.json>")
        sys.exit(1)
    #
    fname = sys.argv[1]
    process(fname)
