# Naive Method:
import time

   

def NaiveStringMatcher(Text,Pattern):
    print("Naive String Matching Program")
    indexList = []
    textLen=len(Text)
    patLen=len(Pattern)
    found = 0
    v1=time.monotonic_ns()
    for i in range(0, textLen-patLen+1):
        j=0
        for j in range(0,patLen):
            if(Text[i+j] != Pattern[j]):
                break;
        if(j == patLen-1):
            indexList.append(i+1)
            found = 1
    v2=time.monotonic_ns()
    if(found == 0):
        print("Pattern does not match")
    else:    
        print("Match found at positions", *indexList, sep = ", ")
    print("Time Taken = " ,(v2-v1)/1e9, "seconds")
    

with open('string.txt','r') as stringData:
    Text = stringData.read()
with open('pattern.txt','r') as patternData:
    Pattern = patternData.read()
    
    
NaiveStringMatcher(Text, Pattern)
