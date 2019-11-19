"""
This is a Fibonacci Iterator
"""
class Fibonacci:
    """The class accepts a sinlge agrument which should be a integer"""

    def __init__(self, limit):

        self.limit = limit
        self.number_1 = 0 #setting defaults
        self.number_2 = 1 #setting defaults
        self.iteration_count = 0 #setting defaults
        self.sum_of_last_two_digits = 1 #setting defaults

    def __iter__(self):

        if not isinstance(self.limit, int):#raising a value error if limit not int
            raise ValueError

        if self.limit < 0:#if limit is negative the value is empty
            pass
        return self

    def __next__(self):

        if self.iteration_count > self.limit:#if the iterations add up tp more
        #than the limit the iterator stops
            raise StopIteration
