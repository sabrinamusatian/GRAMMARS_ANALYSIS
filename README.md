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

## Test data:

All grammars are stored in grammars folder
name_homsky - grammars in NHF
name_gr - grammars represented as graphs