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
    sep = [' ', '.', ',']
    path = Path(file)
    with path.open('r') as f:
        for line in f:
            wlist = line.strip().lower().split()
            for word in wlist:
                cdict[word] = cdict.get(word, 0) + 1
    result = [(k,v) for k,v in cdict.items()]
    # add soring methods
    c_sorted = sorted(result, key = lambda x: x[1])
    a_sorted = sorted(result, key = lambda x: x[0])
    return c_sorted, a_sorted

def show_sorted(file):
    c_sorted, a_sorted = freq_analyzer(file)
    print('Word Frequency - Sorted based on Count')
    for k,v in c_sorted:
        print(f'{k} --> {v}')
    print('\n\nWord Frequency - Sorted based on Alphabet')
    for k,v in a_sorted:
        print(f'{k} --> {v}')






