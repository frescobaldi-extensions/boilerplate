# Frescobaldi Boilerplate Extension

This repository contains a minimal working boilerplate extension for
[Frescobaldi](http://frescobaldi.org). It can be used to quickly start creating
a new extension.

To get started simply copy the content of this repository in a subdirectory of
Frescobaldi's extensions directory and restart Frescobaldi. A minimalistic “My
Extension” extension should be visible in the Tools menu, the editor's and
viewers' context menu, and the Extensions Preference page.

The boilerplate code is designed to provide stubs for all relevant functions
that need to be implemented in an extension, with very little comments getting
in the way. More thoroughly commented code is available in the complementing
[Sample Extension](https://github.com/frescobaldi-extensions/sample-extension).

If the extension doesn't need a Tool panel or a configuration widget simply
remove `widget.py` or `config.py`. Then edit `__init__.py` by removing the
corresponding `import` statements and class variables in `Extension`.

To get a custom extension icon replace the file `icons/extension.svg` with
another SVG file. Further icons can be added to this directory *TODO:
Investigate about how accepted PNG files have to be stored*.

Frescobaldi extensions have access to all packages and modules in Frescobaldi,
as well as the `ly` package that is required as a dependency anyway.
Additionally the extension infrastructure provides some shortcuts for easier
access to elements such as the current document or cursor, but it is out of
scope of this boilerplate project to give any further information about this.
