#Word Frequency Analyzer

"""Steps:
    1. Take a text file. Iterate through the lines.convert the line into a list words (temporarily save)
    2. If a word occure for the first time , add to dict and assign a val of 1
    3. If the word occurs again raise the val by one.
    4. Return a tuple of (word, count). 
    5. Sort the dict based on the val return a tuple of word, count pair--> Sorted by Count
    6. Sort the dict based on the key, return a tuple of word count pair--> Sorted alphabetically """
from pathlib import Path

def freq_analyzer(file):
    cdict = {}
    path = Path(str(file))
    with path.open('r') as f:
        for line in f:
            wlist = line.strip().lower().split()
            for word in wlist:
                cdict[word] = cdict.get(word, 0) + 1
    result = [(k,v) for k,v in cdict.items()]
    # add soring methods





