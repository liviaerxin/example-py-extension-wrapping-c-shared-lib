from libc.string cimport const_char

version = "1.0"

cdef extern from "hello.h":

    void say(const_char* s)

def show(s: str):
    # string -> char bytes
    b = s.encode('utf-8')
    say(b)


from libc.math cimport sin

cdef double f(double x):
    return sin(x * x)

def sinx(x):
    return f(x)