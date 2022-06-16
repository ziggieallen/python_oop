"""Python serial number generator."""

from tracemalloc import start


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, _start = 0):
        """Make a new generator starting at start"""
        # self.val = 99 (my attempt)
        self.start = self.next = _start
        # How does the above line work?

    def __repr__(self):
        """Show representation"""
        return f"<SerialGenerator start = {self.start} next = {self.next}"    

    def generate(self):
        """increment val by 1"""
        # self.val += 1
        # return self.val (my attempt)
        ret = self.next
        self.next += 1
        return ret
        # increment by 1, then return decremented value?

    def reset(self):
        """reset value"""
        # self.val = 99  (my attempt)
        # self.next = self.start    
        self.next = self.start



