#!/usr/bin/python3
import os


def create_new():
    f = open("test_file", "a")
    f.write("go lakers")
    f.close()


def test_create_new():
     assert os.path.isfile("test_file") == True 
