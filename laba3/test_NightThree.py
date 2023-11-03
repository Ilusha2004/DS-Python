import pytest
from laba3.NightThree import *

testdata = [("great(programming)", "programming"),
            ("testing(function(scopes)deleter)", "function(scopes)deleter")]

@pytest.mark.parametrize('string, expected', testdata)
def test_removeScopes(string, expected):
     assert removeScopes(string) == expected

testdata1=[("kfsjbsbdkfbsdfbksdjbkfs", {'k': 4, 'f': 4, 's': 5, 'j': 2, 'b': 5, 'd': 3}),
           ("ABBCAB", {'A': 2, 'B': 3, 'C': 1}),
           ("AAAGGGOOOpd", {'A': 3, 'G': 3, 'O': 3, 'p': 1, 'd': 1})]

@pytest.mark.parametrize('string, expected', testdata1)
def test_dictionaryCounter(string, expected):
     assert dictionaryCounter(string) == expected