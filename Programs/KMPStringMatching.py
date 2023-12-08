# Knuth Morris Pratt Method:
import time

def KMPStringMatcher(Text, Pattern):
    print("Knuth Morris Pratt String Matching Program")
    indexList = []
    patLen = len(Pattern)
    textLen = len(Text)
    found = 0
 
    j = 0 
    i = 0
    prefix = [0]*patLen
    j = 0 
    
    v1=time.monotonic_ns()
    computePrefixFunction(Pattern, patLen, prefix)
 
 
    while i < textLen:
        if Pattern[j] == Text[i]:
            i += 1
            j += 1
 
        if j == patLen:
            indexList.append(i-j+1)
            found = 1
            j = prefix[j-1]
 

        elif i < textLen and Pattern[j] != Text[i]:
            if j != 0:
                j = prefix[j-1]
            else:
                i += 1
                
    v2=time.monotonic_ns()
    if(found == 0):
        print("Pattern does not match")
    else:    
        print("Match found at positions", *indexList, sep = ", ")
    print("Time Taken = " ,(v2-v1)/1e9, "seconds")
    
 
def computePrefixFunction(Pattern, patLen, prefix):
    len = 0
 
    prefix[0]
    i = 1
 
    while i < patLen:
        if Pattern[i]== Pattern[len]:
            len += 1
            prefix[i] = len
            i += 1
        else:
            if len != 0:
                len = prefix[len-1]
 
            else:
                prefix[i] = 0
                i += 1
  


 
with open('string.txt','r') as stringData:
    Text = stringData.read()
with open('pattern.txt','r') as patternData:
    Pattern = patternData.read()

              
KMPStringMatcher(Text, Pattern)


