from .main import PDCache


def load_ipython_extension(ipython):
    """Register extension with IPython."""
    ipython.register_magics(PDCache)
