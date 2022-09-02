#Knuth–Morris–Pratt KMP is an advanced pattern search algorithm with time complexity of O(n+m)

#KMP algorithm cuts out some repeated work which is found in naive pattern search such as moving only +1 index after finding mismatch in substring of our main string
#for example in if we look for pattern:AA in AAAXAAYAAAA only 3 first letters match 4 is mismatch the "brute force" way of finding pattern will move only by 1
#and repeat the process of looking for matches going from AAAX to AAXA,AXAA,XAAY and so on making making the process time inefficient

#Our "pivot" should be at the place of our mismatch to prevent unnecessary repeats, this optimization is called  "Longest Prefix Suffix" (LPS for short)
#as we will be going through parts of our inserted string we will be looking for the longest prefix of our substring which will be also substrings suffix


#LPS Function description:

#LPS Array - same size as our pattern it's gonna correspond to every prefix and suffix of our pattern we are looking for
#for exmp.: for string - AAA a prefix is every substring starting at the beginning meaning every character combination (firs one first 2 char. all 3 char.) are prefixes
#suffix is the opposite every substring ending at last character (last character, last 2 characters, last 3 (whole pattern))

#In practice for for pattern: BBBB    which has 3 substrings
#the first substring: B THE STRING b is both prefix and suffix LPS is 0 because the prefix itself cannot be the entire string itself
# LPS=[0,...]
#for substring BB the first character is the saem as the last character therefore LPS is gonna be 1
#LPS=[0,1,..]
#BBB LPS are first 2 and last 2 characters
#LPS=[0,1,2,.]
#lastly for entire pattern BBBB first 3 characters match last 3 so longest prefix suffix is gonna be 3
#LPS=[]0,1,2,3]



#LPS function: