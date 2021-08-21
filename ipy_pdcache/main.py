import os

import pandas as pd

from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring


def write_data(fname, data):
    """Save data to file. Create sub-directories as necessary."""
    if os.sep in fname:
        # file is in some directory
        path = os.path.dirname(fname)

        if not os.path.exists(path):
            os.makedirs(path)

    data.to_csv(fname, index=True)


def load_data(fname):
    """Load data from file."""
    return pd.read_csv(fname, index_col=0)


@magics_class
class PDCache(Magics):
    @magic_arguments()
    @argument("variable", type=str, help="Variable to be cached.")
    @argument("fname", type=str, help="File which variable is saved in.")
    @cell_magic
    def pdcache(self, line, cell):
        """Cache variables to file."""
        ip = self.shell
        args = parse_argstring(self.pdcache, line)

        if os.path.exists(args.fname):
            # load cached data
            print("Loading data from cache")
            data = load_data(args.fname)
            ip.push({args.variable: data})
        else:
            # execute and cache data (if successful)
            exec_res = ip.run_cell(cell)

            if exec_res.success:
                print("Caching new data")
                data = ip.user_ns[args.variable]
                write_data(args.fname, data)
            else:
                print("Skip caching due to error")
