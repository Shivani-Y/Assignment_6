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

        if self.iteration_count == 0:#if limit is 0 then return 0 and add to counter
            self.iteration_count += 1
            return self.number_1

        if self.iteration_count == 1:#if limit is 1 then return 1 and add to counter
            self.iteration_count += 1
            return self.number_2

        if self.iteration_count > 1:#if limit is a +int (not 0 0r 1) and iteration_count
        #is more than 1 then add to counter and return sum of last 2 digits
            self.sum_of_last_two_digits = self.number_1 + self.number_2
            self.number_1 = self.number_2
            self.number_2 = self.sum_of_last_two_digits
            self.iteration_count += 1
            return self.sum_of_last_two_digits

        return None
