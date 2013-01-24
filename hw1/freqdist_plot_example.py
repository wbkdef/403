
from __future__ import division
from nltk.probability import FreqDist
import pylab
import math
import random

text = """
What is the air-speed velocity of an unladen swallow ? 
What do you mean ? 
An African or European swallow ? 
What ? 
I don't know that ! 
Auuuuuuuugh ! 
How do know so much about swallows ?
"""

# collect word counts in nltk.probability.FreqDist
fd = FreqDist(word.lower() for word in text.split())
for w in fd.keys():
    print w, fd[w]
freqs = [fd[w] for w in fd.keys()]
pylab.grid(True)
pylab.plot(freqs, range(0,len(freqs)), label='Frequency')
# for large data use pylab.loglog for a logscale plot

sz = fd.B()+1 # number of word types in text

randvals = [random.randrange(1,5,1) for r in range(1,sz)]
pylab.plot(sorted(randvals, reverse=True), label='Random')

# show all plots
pylab.xlabel("Word Types")
pylab.ylabel("Counts")
pylab.legend(loc='upper right')
pylab.savefig("freqdist.png")
#pylab.show()

