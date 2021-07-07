'''
Script to test py test module

The cmd: python -m pytest - It will run the function starting test_ in test_ module by default 

'''

def some_other():
    assert 1 + 1 == 2


def test_one_plus_one():
    print("invoce test")
    assert 1 + 1 == 2


def test_one_plus_two():
    a =1
    b=2
    c= 3
    assert a + b == c

import pytest

#to test if it raises a special case raised an exeption
def test_one_dived_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    
    assert 'division by zero' in str(e.value)

#test multiple cases parameter in one functions
products = [
    (2,3,6),    #test mutiply 2 positive ints
    (2,1,2),    #test mutiply by indetity
    (2,0,0),    #test mutiply by zero
    (2,-2,-4),  #test mutiply by one negative 
    (-2,-2,4),  #test mutiply by two negative
    (.5,5.0,2.5)  #test mutiply by floats
]

@pytest.mark.parametrize('a,b,c', products)
def test_multiplication(a,b,c):
    assert a * b == c