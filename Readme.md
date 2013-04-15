project\_utils
=============
 project\_utils is a destined to be a number of things. Right now, it does only 1
thing. But one day!

 Right now, project\_utils is a simple python script that can be used to create new
web based project source trees based on *very* simple templates. Well, it
_should_ be in a little time.

__tl;dr;__: an in-development python utility to create new projects based on 
__simple__ templates.

Features:
---------
- No config file required for template creation. Any directory will do. Which means
that you can store anything, including nginx configs to quickly get a web dev project
up.
- A simple set of options when creating a project allows selection of availalble
libraries (jquery, backbone.js) and frameworks (bootstrap, 960gs). The selected
set is also included in the html files at places indicated by markers
- All text files are processed as templates, so basic options like project name can
be set automatically in all source files
- __putils__ can also copy the files for a specific library to the current directory.
Useful to have all the libraries in one place and get them as required. No symlinks 
as that would interfere with deployment

Working Features:
-----------------
- Library adding functionality is working. Try putils.py -h for details

Future Features:
----------------
###Golang Project Creation:
  - `pu tem golang` should create a new $GOPATH style dir structure in the
current folder {src, pkg, bin}
  - Template should have a shell script that activates the go-env like
virtualenv for python. Script should add project dir to start of $GOPATH
and bin to start of $PATH. Script should also provide ability to revert back
these changes

