from libcpp.vector cimport vector

cdef extern from "test.h":
    int run(vector[int])

def run_from_python(ls):
    cdef vector[int] cls
    for l in ls:
        cls.push_back(l)
    return run(cls)
