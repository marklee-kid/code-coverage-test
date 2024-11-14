import os
import time


def get_current_path():
    return "."


def get_time():
    return time.time()


def get_separator():
    return os.sep


def get_tz():
    return time.timezone


def get_root():
    return "/"


def foo():
    mytime = time.time()
    if get_time() > mytime:
        return "bar"
    return "uhuh"


def bar():
    return "foo"


def funk1():
    return "sdgsdfg"


def func2():
    return "ccsdgsdfg"


def func3(maybe = True):
    if maybe:
        return "bbsdgsdfg"
    return "sdfd"


def func4():
    return "aasdgsdfg"
