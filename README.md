# Python C Extension Wrapping C Shared Library

A simple example to illusrate how to build a python extension to wrap a C shared library to expose methods in the library with the help of `Cython`.

## Usage

Prepare virtual enviroment,

```sh
▶ python3 -m venv .venv
▶ source .venv/bin/activate
(.venv) 
▶ pip install -r requirements_dev.txt 
```

Test locally,

```sh
▶ python setup.py build_ext --inplace
▶ cp example-hello-c-lib/build/src/libhello.dylib hello_py 
▶ python -c "import hello_py; print(hello_py.version); hello_py.show('David'); print(hello_py.sinx(2))" 
1.0
Hello David
-0.7568024953079282
```

Build binary wheel,

```sh
▶ python setup.py build bdist_wheel
▶ unzip -l dist/hello_py-1.0-cp37-cp37m-macosx_10_9_x86_64.whl
Archive:  dist/hello_py-1.0-cp37-cp37m-macosx_10_9_x86_64.whl
  Length      Date    Time    Name
---------  ---------- -----   ----
       42  05-12-2021 16:26   hello_py/__init__.py
    25852  05-13-2021 15:14   hello_py/_hello_py.cpython-37m-darwin.so
      188  05-13-2021 15:14   hello_py-1.0.dist-info/METADATA
      110  05-13-2021 15:14   hello_py-1.0.dist-info/WHEEL
        9  05-13-2021 15:14   hello_py-1.0.dist-info/top_level.txt
      466  05-13-2021 15:14   hello_py-1.0.dist-info/RECORD
---------                     -------
    26667                     6 files

# patch our dynamic library `libhello.dylib` into the built wheel `hello_py-1.0-*.whl`
▶ zip -rv dist/hello_py-1.0-cp37-cp37m-macosx_10_9_x86_64.whl hello_py/libhello.dylib
  adding: libhello.dylib	(in=12484) (out=717) (deflated 94%)
total bytes=39151, compressed=9046 -> 77% savings

# list files in `*.whl` again
▶ unzip -l dist/hello_py-1.0-cp37-cp37m-macosx_10_9_x86_64.whl
Archive:  dist/hello_py-1.0-cp37-cp37m-macosx_10_9_x86_64.whl
  Length      Date    Time    Name
---------  ---------- -----   ----
       42  05-12-2021 16:26   hello_py/__init__.py
    25852  05-13-2021 15:14   hello_py/_hello_py.cpython-37m-darwin.so
      188  05-13-2021 15:14   hello_py-1.0.dist-info/METADATA
      110  05-13-2021 15:14   hello_py-1.0.dist-info/WHEEL
        9  05-13-2021 15:14   hello_py-1.0.dist-info/top_level.txt
      466  05-13-2021 15:14   hello_py-1.0.dist-info/RECORD
    12484  05-13-2021 00:24   hello_py/libhello.dylib
---------                     -------
    39151                     7 files
```

Install,

```sh
▶ pip install dist/hello_py-1.0-*.whl

# move to other directory to test again
▶ cd..
▶ python -c "import hello_py; print(hello_py.version); hello_py.show('David'); print(hello_py.sinx(2))" 
1.0
Hello David
-0.7568024953079282
```
