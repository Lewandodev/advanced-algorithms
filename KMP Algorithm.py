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



#KMP and LPS function:

def KMP(text,pattern):
    if pattern=='':
        return 0
    lps=[0]*len(pattern) #lps is always gonna be as big as our pattern
    prev_lps=0
    i=1
    # the whole while loop is our LPS function
    while i<len(pattern): #we going through every index
        if pattern[i]==pattern[prev_lps]: #simpliest case characters match each other
            lps[i]=prev_lps+1
            prev_lps+=1
            i+=1  #we want to check next indexes
            #if i is 1 two first characters already match we don't need to start from beginning

        else:
            if prev_lps==0:
                lps[i]=0 #if first character the last we can't have possible prefix that matches suffix
                i+=1
            else:
                prev_lps=lps[prev_lps-1] #if indexes dont match we set the prev_lps value to whatever is on the left of our index in lps array

    #KMP
    a=0 #pointer for text
    b=0 #pointer for pattern

    while a<len(text): #loop in which we look for match to our pattern
        if text[a]==pattern[b]:
            a,b=a+1,b+1
        else:
            if b==0:
                a+=1
            else:
                b=lps[b-1]
        if b==len(pattern):
            return a-len(pattern)
    return -1







