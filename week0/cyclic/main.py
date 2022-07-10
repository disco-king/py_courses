from cyclic import CyclicIterator
import sys

lst = [i for i in range(1000000)]
print(sys.getsizeof(lst))

it = CyclicIterator(lst)
print(sys.getsizeof(it))