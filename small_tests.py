from common_util import *
from matrix_method import matrix_method
from glr_method import glr
from gll_method import gll

import sys

small1_test = [(0, 'S', 0),
               (1, 'S', 0),
               (1, 'S', 1),
               (2, 'S', 2)]

small2_test = [(0, 'S', 0)]

def test_glr_method(graph_name, grammar_name, ans_list):
    print ("Test for " + grammar_name + " and " + graph_name + " started.")
    res = glr("./small_tests/" + grammar_name, "./small_tests/" + graph_name)
    if (res != ans_list):
        print res
        print (graph_name + " failed")
        return False
    else:
        print ("Test for " + grammar_name + " and "  + graph_name + " completed successfully.")
    return True

def test_gll_method(graph_name, grammar_name, ans_list):
    print ("Test for " + grammar_name + " and " + graph_name + " started.")
    res = list(gll("./small_tests/" + grammar_name, "./small_tests/" + graph_name))
    if (res != ans_list):
        print (graph_name + " failed")
        return False
    else:
        print ("Test for " + grammar_name + " and " + graph_name + " completed successfully.")
    return True


if __name__ == '__main__':
    print ("Tests for glr method started")
    test_glr_method('small1_graph.dot', "small1_gr", small1_test)
    test_glr_method('small2_graph.dot', "small2_gr", small2_test)

    print ("Tests for gll method started")
    test_gll_method('small1_graph.dot', "small1_gr", small1_test)
    test_gll_method('small2_graph.dot', "small2_gr", small2_test)

