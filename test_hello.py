from multiprocessing.context import assert_spawning
import unittest,hello

def test_hello():
    output = hello.hello()
    assert output == "helloworld"

