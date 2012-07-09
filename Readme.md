project_utils
=============
 project_utils is a destined to be a number of things. Right now, it does only 1
thing. But one day! <EVIL_LAUGH>

 Right now, project\_utils is a simple python script that can be used to create new
web based project source trees based on *very* simple templates. Well, it
_should_ be in a little time.

__tl;dr;__: an in-development (ZERO LOC) python utility to create new projects based
on __simple__ templates.

Features:
---------
- No config file required for template creation. Any directory will do. Which means
that you can store anything, including nginx configs to quickly get a web dev project
up.
- A simple set of options when creating a project allows selection of availalble
libraries (jquery, backbone.js) and frameworks (bootstrap, 960gs). The selected
set is also included in the html files at places indicated by markers
- Source files also processed as templates, so basic options like project name can
be set automatically in all places in the source file
