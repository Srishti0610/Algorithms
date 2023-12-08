# Rabin Karp Method:
import time


def RabinKarpStringMatcher(Text, Pattern, d, q):
    print("Rabin Karp String Matching Program")
    indexList = []
    patLen = len(Pattern)
    textLen = len(Text)
    pat = 0
    tex = 0
    h = 1
    i = 0
    j = 0
    found = 0

    for i in range(patLen-1):
        h = (h*d) % q

    # Calculation of the hash values for text and pattern
    for i in range(patLen):
        pat = (d*pat + ord(Pattern[i])) % q
        tex = (d*tex + ord(Text[i])) % q

    # Check if there is a match
    
    v1=time.monotonic_ns()
    for i in range(textLen-patLen+1):
        if pat == tex:
            for j in range(patLen):
                if Text[i+j] != Pattern[j]:
                    break

            j += 1
            if j == patLen:
                indexList.append(i+1)
                found = 1

        if i < textLen-patLen:
            tex = (d*(tex-ord(Text[i])*h) + ord(Text[i+patLen])) % q

            if tex < 0:
                tex = tex+q
    
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

RabinKarpStringMatcher(Text, Pattern, 40, 7573)


