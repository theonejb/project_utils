from actions import lib

def setup_actions(subparsers):
  """
  setup all action subparsers. we're doing this here so that all setup related to 
  "actions" is kept within the module
  """
  subparser_lib = subparsers.add_parser("lib")
  lib.config_subparser(subparser_lib)

def do_action(ns):
  """
  calls the correct action handler given the namespace returned by parser.parse_args()
  """
  if ns.action == "lib":
    lib.execute(ns)
  else:
    print "%s is not currently supported."%(ns['action'],)
