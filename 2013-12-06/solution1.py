"""Manually looked for characters that are the same upside down: H I N O S X Z
And then search a dictionary with English words for words matching the puzzle.
"""
import re, urllib2
# word list form http://www-personal.umich.edu/~jlawler/wordlist.html
for line in urllib2.urlopen('http://www-personal.umich.edu/~jlawler/wordlist'):
    word = line.strip()
    if re.match(r'^[HINOSXZ]{4}$', word, re.IGNORECASE) and word[0] == word[3] and word[1] == word[2]:
        print word.upper()
