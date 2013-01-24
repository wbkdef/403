
from random import *

# generator for a reverse iterator over an array
def reverse_iterator(data):
  for index in range(len(data)-1, -1, -1):
    yield index

# fisher yates random shuffle of an array
def fisher_yates_shuffle(array):
  for i in reverse_iterator(array):
    j = int(randrange(i+1))
    (array[i],array[j]) = (array[j],array[i])

if __name__ == "__main__":
  x = range(1,51)
  fisher_yates_shuffle(x)
  print " ".join(str(i) for i in x)

