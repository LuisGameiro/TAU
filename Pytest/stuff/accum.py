'''
This module contains a basic accumulator class

'''

#-------------------------------------------------------
# Class: Accumulator
#-------------------------------------------------------

class Accumulator:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add_count(self, more =1):
        self._count += more
    