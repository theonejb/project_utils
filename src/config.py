"""
holds config for project_utils
"""

from os import path

# absolute path to base resource directory
RESOURCE_DIR = "/Users/asad/Programming/Personal/project_utils"

# paths for library and template dirs. relative to RESOURCE_DIR
LIB_DIR = "lib"
TEMPLATE_DIR = "templates"

RESOURCE_PATH = path.abspath(RESOURCE_DIR)
LIB_PATH = path.join(RESOURCE_PATH, LIB_DIR)
TEMPLATE_PATH = path.join(RESOURCE_PATH, TEMPLATE_DIR)

