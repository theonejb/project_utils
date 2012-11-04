#!/usr/bin/env python

"""
main() for project_utils. parses command line options and routes to correct
handler
"""

import argparse

from os import path

import config
import actions

# construct argparser and setup main app options
parser = argparse.ArgumentParser(prog="putils",
    description="a set of cli commands to help during development")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("--version", action="version", version="%(prog)s 0.1")

# add subparsers for each of the individual functions
subparsers = parser.add_subparsers(dest="action")
actions.setup_actions(subparsers)

actions.do_action(parser.parse_args())
