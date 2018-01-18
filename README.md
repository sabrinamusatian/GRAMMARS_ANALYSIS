# GRAMMARS_ANALYSIS
Solutions for FL course at SPBsU

### Requirments: python 2.7

## Methods:

### Matrix method

To run the algorithm type:
```
python matrix_method.py grammars/Q1_homsky data/skos.dot res.txt
```

To run tests only for this method:

```
python tests.py "matrix_method"
```


### GLR method

To run the algorithm type:
```
python glr_method.py grammars/Q1 data/skos.dot res.txt
```

To run tests only for this method:

```
python tests.py "glr_method"
```

###


### GLL method

To run the algorithm type:
```
python gll_method.py grammars/Q1_gr data/skos.dot res.txt
```

To run tests only for this method:

```
python tests.py "gll_method"
```

###
## Tests:
There are two types of tests: unit tests with big data and small examples.

How to run both small and big tests for each method see above.

If you want to run both small and big tests for all methods at once type:

```
python tests.py "all"
```

It takes approximately 30 minutes to run all the tests at once.

If you want to run only small tests for all methods type:
```
python tests.py "small_tests"
```

Small tests are executed for all methods at the same run.
It takes a few minutes to run small tests because of some big generated tests for corner cases.

## Test data:

All grammars for big tests are stored in grammars folder:

name_homsky - grammars in CNF(for matrix method)

name_gr - grammars represented as graphs(for gll and glr methods)

All graphs for big tests are stored in data folder.

Both grammars and graphs for small tests are stored in small_tests folder.
In small_tests folder you may also find files with answers for each test.