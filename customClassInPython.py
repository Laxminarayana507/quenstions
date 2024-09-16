"""Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}"""

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0  # Initialize index for iteration

    # Define the iterable method
    def __iter__(self):
        self._index = 0  # Reset index on each new iteration
        return self

    # Define the iterator method
    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration  # End of iteration

# Example usage:
rectangle = Rectangle(length=10, width=5)

# Iterating over the rectangle instance
for dimension in rectangle:
    print(dimension)
