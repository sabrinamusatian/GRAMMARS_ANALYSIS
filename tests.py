from common_util import count_res
from matrix_method import matrix_method
from glr_method import glr
from gll_method import gll

import sys

test_data_Q1 = {
    'skos.dot': 810,
    'generations.dot' : 2164,
    'travel.dot' : 2499,
    'univ-bench.dot' : 2540,
    'atom-primitive.dot' : 15454,
    'biomedical-mesure-primitive.dot' : 15156,
    'foaf.dot' : 4118,
    'people_pets.dot' : 9472,
    'funding.dot' : 17634,
    'wine.dot' : 66572,
    'pizza.dot' : 56195,
}

test_data_Q2 = {
    'skos.dot': 1,
    'generations.dot' : 0,
    'travel.dot' : 63,
    'univ-bench.dot' : 81,
    'atom-primitive.dot' : 122,
    'biomedical-mesure-primitive.dot' : 2871,
    'foaf.dot' : 10,
    'people_pets.dot' : 37,
    'funding.dot' : 1158,
    'wine.dot' : 133,
    'pizza.dot' : 1262,
}

def test_matrix_method(test_data, grammar_name):
    for key in test_data.items():
        name, val = key
        print ("Test for " + grammar_name + " and " + name + " started.")
        leng = count_res(matrix_method("./grammars/" + grammar_name, "./data/" + name))
        if (leng != val):
            print (name + " failed")
            return False
        else:
            print ("Test for " + grammar_name + " and "  + name + " completed successfully.")
    return True

def test_glr_method(test_data, grammar_name):
    for key in test_data.items():
        name, val = key
        print ("Test for " + grammar_name + " and " + name + " started.")
        leng = count_res(glr("./grammars/" + grammar_name, "./data/" + name))
        if (leng != val):
            print (name + " failed")
            return False
        else:
            print ("Test for " + grammar_name + " and "  + name + " completed successfully.")
    return True

def test_gll_method(test_data, grammar_name):
    for key in test_data.items():
        name, val = key
        print ("Test for " + grammar_name + " and " + name + " started.")
        leng = count_res(gll("./grammars/" + grammar_name, "./data/" + name))
        if (leng != val):
            print leng
            print (name + " failed")
            return False
        else:
            print ("Test for " + grammar_name + " and "  + name + " completed successfully.")
    return True

def unit_matrix_method():
    print("Tests for matrix method started")
    Q1_tests = test_matrix_method(test_data_Q1, "Q1_homsky")
    Q2_tests = test_matrix_method(test_data_Q2, "Q2_homsky")
    if (Q1_tests and Q2_tests):
        print ("All tests for matrix_method passed successfully")
        return True
    return False

def unit_glr_method():
    print("Tests for glr method started")
    Q1_tests = test_glr_method(test_data_Q1, "Q1_gr")
    Q2_tests = test_glr_method(test_data_Q2, "Q2_gr")
    if (Q1_tests and Q2_tests):
        print ("All tests for glr_method passed successfully")
        return True
    return False

def unit_gll_method():
    print("Tests for gll method started")
    Q1_tests = test_gll_method(test_data_Q1, "Q1_gr")
    Q2_tests = test_gll_method(test_data_Q2, "Q2_gr")
    if (Q1_tests and Q2_tests):
        print ("All tests for gll_method passed successfully")
        return True
    return False

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python tests.py all")
        sys.exit()

    if (sys.argv[1] == "matrix_method"):
        unit_matrix_method()

    if (sys.argv[1] == "glr_method"):
        unit_glr_method()

    if (sys.argv[1] == "gll_method"):
        unit_gll_method()

    if (sys.argv[1] == "all"):
        if unit_gll_method() and unit_matrix_method() and unit_glr_method():
            print("Tests for all methods finished successfully")
