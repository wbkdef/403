# dispersion_example.py

# uses nltk v0.9.5
#
# plots dispersion of word occurences in
# Sense and Sensibility by Jane Austen

from nltk.corpus import gutenberg
from nltk.draw import dispersion_plot
words = ['Elinor', 'Marianne', 'Edward', 'Willoughby']
dispersion_plot(gutenberg.words('austen-sense.txt'), words)
