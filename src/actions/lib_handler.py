"""
actual implementation of all "lib" action functionality
"""

import re, glob, shutil
import yaml

from os import path

class Library(object):
  """
  represents a single library on the FS
  """
  def __init__(self, config):
    """
    config object:
    {
      name: FooLib,
      basedir: $DIR,
      versions: [{
          vnumber: $VERSION,
          files: [$FILE, $FILE]
      }]
    }
    """
    self.name = config['name']
    self.basedir = config['basedir']

    self.versions = dict()
    for ver in config['versions']:
      self.versions[ver['vnumber']] = ver['files']

  def __str__(self):
    version_string = ", ".join(
        map(lambda ver: "@%s"%(ver,), self.sorted_versions())
        )
    return "%s [ %s ]"%(self.name, version_string)

  def _get_files(self, version):
    return self.versions[version]

  def _get_full_name(self, version):
    return "%s@%s"%(self.name, version)

  @staticmethod
  def _print(msg, verbose):
    if verbose:
      print msg

  @staticmethod
  def normalize_version(v):
    """
    normalizes the version numbers so we can compare/sort them. see:
    http://stackoverflow.com/a/1714190/119117
    """
    return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]

  def sorted_versions(self):
    """
    caches and returns the sorted version list
    """
    try:
      self._sortedv
    except AttributeError:
      self._sortedv = sorted(self.versions.keys(), 
          key=lambda v: self.normalize_version(v), reverse=True)
    return self._sortedv

  def check_name(self, name):
    """
    returns True if the given name matches this library
    """
    if self.name.lower() == name.lower():
      return True
    else:
      return False

  def put(self, version, dest, verbose):
    """
    copies all files for the specified version to the specified dir
    """
    if not version:
      version = self.sorted_versions()[0]
    elif version not in self.versions.keys(): # check if the required version actually exists
      raise LibraryNotFound("Library [%s] version [%s] not found"%(self.name, version))

    if not path.isdir(dest):
      raise IOError("Destination [%s] is not a directory"%(dest,))

    self._print("Copying files for %s =>"%(self._get_full_name(version),), verbose)
    # get a list of files for the required version and put them at the destination
    files = self._get_files(version)
    for cur_file in files:
      file_path = path.abspath(path.join(self.basedir, cur_file))
      self._put_file(file_path, dest, verbose)

  def _put_file(self, src, dest, verbose):
    if not path.exists(src):
      raise IOError("File [%s] does not exist"%(src,))
    elif not (path.isfile(src) or path.isdir(src)):
      raise IOError("[%s] is not a file or directory"%(src,))

    if path.isfile(src):
      file_name = path.basename(src)
      dest_path = path.join(dest, file_name)
      self._print("  file: %s"%(file_name,), verbose)
      shutil.copy(src, dest_path)
    elif path.isdir(src):
      dir_name = path.basename(src)
      dest_path = path.join(dest, dir_name)
      self._print("  dir: %s"%(dir_name,), verbose)
      shutil.copytree(src, dest_path)

class LibraryCollection(object):
  """
  searches basedir for all *.foolib files, parses them and creates
  Library objects for each file
  """
  def __init__(self, basedir):
    self.basedir = basedir
    self.libraries = []

    lib_files = glob.iglob(path.join(basedir, "*.foolib"))
    for lib in lib_files:
      config = yaml.safe_load(open(lib))
      library = Library(config)
      self.libraries.append(library)

  def __str__(self):
    """
    returns a string representation of the LibraryCollection
    """
    return "\n".join(map(lambda lib: str(lib), self.libraries))

  def put_lib(self, name, dest_dir, verbose=False):
    """
    searches for the library specified in "name" and puts it in the dest_dir
    """
    # check if "name" has a version component. if so, sperate it
    lib_name = ""
    lib_version = ""
    if name.find("@") != -1:
      lib_name, lib_version = name.split("@")
    else:
      lib_name = name

    # find our required library
    library = None
    for lib in self.libraries:
      if lib.check_name(lib_name):
        library = lib
        break
    if library is None:
      raise LibraryNotFound("Library [%s] not found"%(lib_name,))
    else:
      library.put(lib_version, dest_dir, verbose)


class LibraryNotFound(Exception):
  pass
