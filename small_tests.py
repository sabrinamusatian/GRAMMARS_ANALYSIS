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
small3_test = [(0, 'S', 1)]
small4_test = [(0, 'S', 1), (0, 'S', 2), (0, 'S', 3),
               (0, 'S', 4), (0, 'S', 5), (1, 'S', 2),
               (1, 'S', 3), (1, 'S', 4), (1, 'S', 5),
               (2, 'S', 3), (2, 'S', 4), (2, 'S', 5),
               (3, 'S', 4), (3, 'S', 5), (4, 'S', 5)]

small5_test = [(1, 'S', 4), (0, 'S', 6), (3, 'S', 7), (2, 'S', 7),
               (1, 'S', 7), (1, 'S', 0), (3, 'S', 4), (1, 'S', 5),
               (2, 'S', 6), (3, 'S', 0), (0, 'S', 0), (3, 'S', 5),
               (2, 'S', 5), (1, 'S', 6), (0, 'S', 4), (0, 'S', 7),
               (2, 'S', 4), (0, 'S', 5), (3, 'S', 6), (2, 'S', 0)]

def check_list_eq(res, ans_list):
    if len(res) == len(ans_list):
        for temp in res:
            if not temp in ans_list:
                return False
        for temp in ans_list:
            if not temp in res:
                return False
    else:
        return False
    return True


def test_glr_method(graph_name, grammar_name, ans_list):
    print ("Test for " + grammar_name + " and " + graph_name + " started.")
    res = list(filter(lambda x: x[1] == 'S',
                      glr("./small_tests/" + grammar_name, "./small_tests/" + graph_name)))
    if not check_list_eq(res, ans_list):
        print (graph_name + " failed")
        return False
    print ("Test for " + grammar_name + " and "  + graph_name + " completed successfully.")
    return True

def test_gll_method(graph_name, grammar_name, ans_list):
    print ("Test for " + grammar_name + " and " + graph_name + " started.")
    res = list(filter(lambda x: x[1] == 'S',
                      list(gll("./small_tests/" + grammar_name, "./small_tests/" + graph_name))))

    if not check_list_eq(res, ans_list):
        print (graph_name + " failed")
        return False
    print ("Test for " + grammar_name + " and " + graph_name + " completed successfully.")
    return True

def test_matrix_method(graph_name, grammar_name, ans_list):
    print ("Test for " + grammar_name + "  and " + graph_name + " started.")
    res = list(filter(lambda x: x[1] == 'S',
                      matrix_method("./small_tests/" + grammar_name, "./small_tests/" + graph_name)))
    if not check_list_eq(res, ans_list):
        print (graph_name + " failed")
        return False
    print ("Test for " + grammar_name + " and "  + graph_name + " completed successfully.")
    return True

if __name__ == '__main__':
    print ("Tests for glr method started")
    glr_1 = test_glr_method('small1_graph.dot', "small1_gr", small1_test)
    glr_2 = test_glr_method('small2_graph.dot', "small2_gr", small2_test)
    glr_3 = test_glr_method('small3_graph.dot', "small3_gr", small3_test)
    glr_4 = test_glr_method('small4_graph.dot', "small4_gr", small4_test)
    glr_5 = test_glr_method('small5_graph.dot', "small5_gr", small5_test)

    print ("Tests for gll method started")
    gll_1 = test_gll_method('small1_graph.dot', "small1_gr", small1_test)
    gll_2 = test_gll_method('small2_graph.dot', "small2_gr", small2_test)
    gll_3 = test_gll_method('small3_graph.dot', "small3_gr", small3_test)
    gll_4 = test_gll_method('small4_graph.dot', "small4_gr", small4_test)
    gll_5 = test_gll_method('small5_graph.dot', "small5_gr", small5_test)

    print ("Tests for matrix method started")
    mat_1 = test_matrix_method('small1_graph.dot', "small1_homsky", small1_test)
    mat_2 = test_matrix_method('small2_graph.dot', "small2_homsky", small2_test)
    mat_3 = test_matrix_method('small3_graph.dot', "small3_homsky", small3_test)
    mat_4 = test_matrix_method('small4_graph.dot', "small4_homsky", small4_test)
    mat_5 = test_matrix_method('small5_graph.dot', "small5_homsky", small5_test)
