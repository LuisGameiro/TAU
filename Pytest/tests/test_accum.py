'''
this module contains basic unit test for the accumulator module
'''

# --------------------------
# Imports
# --------------------------

import pytest
from stuff.accum import Accumulator

# --------------------------
# Fixture - A function that handles setup and cleanup operations for a test case.
# check accum(scope="session") where accum initization runs one time and yield for clean up procedures
# --------------------------

@pytest.fixture
def accum():
    return Accumulator()

# -------------------------
# tests
# ------------------------

#arrange
def test_accumulator_init(accum):
    assert accum.count == 0

#act
def test_accumulator_add_one(accum):
    accum.add_count()
    assert accum.count == 1

def test_accumulator_add_tree(accum):
    accum.add_count(3)
    assert accum.count == 3

def test_accumulator_add_twice(accum):
    accum.add_count(3)
    accum.add_count(3)
    assert accum.count == 6

#assert
def test_accumulator_cant_add_count_direcly(accum):
    with pytest.raises(AttributeError, match="can't set attribute") as error:
        accum.count = 10