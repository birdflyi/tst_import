# tst_import
Test the import error when import packages generated by setup.py and debug a single .py file which import other sub-modules.

This is an attempt inspired by answer https://stackoverflow.com/a/45305718/10351422 to the question [Git submodule raises import error once used in python project](https://stackoverflow.com/questions/45305101/git-submodule-raises-import-error-once-used-in-python-project).

# Test
Change your terminal directory into root dir.

1. Run `python setup.py sdist` for Windows platform to create a source distribution. 

Here is [A Simple Example](https://docs.python.org/2/distutils/introduction.html#a-simple-example). 
If you want to write a new script in setup.py, see [Writing the Setup Script](https://docs.python.org/2/distutils/setupscript.html#setup-script).

2. Run the pip install or uninstall command in the new project to import your package. 

e.g. `pip install tst_import-1.0.0.tar.gz`, `pip uninstall tst_import -y`.
