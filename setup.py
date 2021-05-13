import os
from os.path import join, dirname
from setuptools import setup
from setuptools.extension import Extension
import platform

extra_compile_args = ["-Wall", "-g", "-x", "c++"] # "-std=c++11" c++
extra_link_args = []

if platform.system() == "Darwin":
    extra_compile_args += ["-stdlib=libc++"]
    # Assume that shared library with install name `@rpath/libhello.dylib`, and it's in the same folder as the built extension *.dylib is also in. So in linking stage, we can set RPATH in extension *.dylib as `@loader_path`
    extra_link_args += ["-Wl,-rpath,@loader_path"]

vendor_include = "./example-hello-c-lib/include"
vendor_lib_dirs = "./example-hello-c-lib/build/src"

module1 = Extension(
    "hello_py._hello_py",
    sources=["hello_py/_hello_py.pyx"],
    include_dirs=[vendor_include],
    library_dirs=[vendor_lib_dirs],
    # runtime_library_dirs = [vendor_lib],
    libraries=["hello"],
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args,
)

setup(
    name="hello_py",
    version="1.0",
    description="trying to link extern lib",
    ext_modules=[module1],
    packages=["hello_py"],
)

