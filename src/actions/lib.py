"""
contains functionality for the "lib" action:
  - add a library to the current path
  - list available libraries
"""

import os, sys

import config

from actions import lib_handler

def config_subparser(subparser):
  """
  adds and configures a subparser for the "lib" action
  """
  lib_actions_group = subparser.add_mutually_exclusive_group(required=True)
  lib_actions_group.add_argument("-a", "--add", nargs="+", metavar="LIB",
      dest="libs", help="add the specified libraries to the current dir")
  lib_actions_group.add_argument("-l", "--list", action="store_true",
      help="list available libraries")

def execute(ns):
  """
  based on selected options (from the given argparse.Namespace) executes this action
  """
  libraries = lib_handler.LibraryCollection(config.LIB_PATH)
  if ns.list:
    print libraries
  elif len(ns.libs) != 0:
    cwd = os.getcwd()
    for lib in ns.libs:
      try:
        libraries.put_lib(lib, cwd, ns.verbose)
      except lib_handler.LibraryNotFound as e:
        sys.stderr.write(e.message)
        sys.stderr.write("\n")
      except IOError as e:
        sys.stderr.write("IOError encountered: %s\n"%(e.message,))
        sys.stderr.write("Check config file for library [%s]\n"%(lib,))

