# %%pdcache cell magic

[![pypi version](https://img.shields.io/pypi/v/ipy-pdcache.svg)](https://pypi.org/project/ipy-pdcache/)
[![Tests](https://github.com/kpj/ipy_pdcache/workflows/Tests/badge.svg)](https://github.com/kpj/ipy_pdcache/actions)


Automatically cache results of intensive computations in IPython.

Inspired by [ipycache](https://github.com/rossant/ipycache).


## Installation

```bash
$ pip install ipy-pdcache
```


## Usage

In IPython:

```python
In [1]: %load_ext ipy_pdcache

In [2]: import pandas as pd

In [3]: %%pdcache df data.csv
   ...: df = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})
   ...:

In [4]: !cat data.csv
,A,B
0,1,4
1,2,5
2,3,6
```

This will cache the dataframe and automatically load it when re-executing the cell.
