import pweave
print pweave.__file__


def test_nbformat():
    """Test whether we can write an IPython Notebook.
    """
    infile = 'tests/simple.mdw'
    pweave.pweave(file=infile, doctype='ipynb', figdir='tests/figures')
